import os
import json
import glob
from typing import List, Dict
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CONTENT_DIR = os.path.join(BASE_DIR, 'content', 'papers')
PDF_DIR = os.path.join(BASE_DIR, 'static', 'pdfs', 'raw')
IMAGE_DIR = os.path.join(BASE_DIR, 'static', 'images', 'papers')
AUDIT_STATUS_FILE = os.path.join(DATA_DIR, 'audit_status.json')
WORKBENCH_STATIC = os.path.join(os.path.dirname(__file__), 'workbench')

class AuditStatusUpdate(BaseModel):
    approved: bool

class FigureCaptureRequest(BaseModel):
    page: int
    x: float
    y: float
    width: float
    height: float
    figure_num: int

class Paper(BaseModel):
    filename: str
    title: str
    has_pdf: bool
    approved: bool

def get_audit_status() -> Dict[str, bool]:
    if not os.path.exists(AUDIT_STATUS_FILE):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(AUDIT_STATUS_FILE, 'w') as f:
            json.dump({}, f)
        return {}
    
    with open(AUDIT_STATUS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def update_audit_status(filename: str, approved: bool):
    status = get_audit_status()
    status[filename] = approved
    with open(AUDIT_STATUS_FILE, 'w') as f:
        json.dump(status, f, indent=2)

def list_papers() -> List[Dict]:
    papers = []
    status = get_audit_status()
    
    if not os.path.exists(CONTENT_DIR):
        return []

    md_files = glob.glob(os.path.join(CONTENT_DIR, "*.md"))

    for filepath in md_files:
        filename = os.path.basename(filepath)
        name_no_ext = os.path.splitext(filename)[0]
        
        pdf_path = os.path.join(PDF_DIR, f"{name_no_ext}.pdf")
        has_pdf = os.path.exists(pdf_path)
        
        approved = status.get(name_no_ext, False)
        
        title = name_no_ext
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith("title:"):
                        title = line.replace("title:", "").strip().strip('"').strip("'")
                        break
        except Exception:
            pass
        
        papers.append({
            "filename": name_no_ext,
            "title": title,
            "has_pdf": has_pdf,
            "approved": approved
        })
    
    papers.sort(key=lambda x: x['filename'])
    return papers

def extract_figure(filename: str, page_num: int, x: float, y: float, w: float, h: float, fig_num: int) -> bool:
    import fitz
    pdf_path = os.path.join(PDF_DIR, f"{filename}.pdf")
    if not os.path.exists(pdf_path):
        return False
    
    os.makedirs(IMAGE_DIR, exist_ok=True)
    output_path = os.path.join(IMAGE_DIR, f"{filename}_fig_{fig_num}.png")
    
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num - 1)
    
    rect = fitz.Rect(x, y, x + w, y + h)
    mat = fitz.Matrix(3, 3)
    pix = page.get_pixmap(matrix=mat, clip=rect)
    pix.save(output_path)
    doc.close()
    return True

HUGO_BASE_URL = "http://localhost:1313"

@app.get("/hugo-proxy/{path:path}")
async def hugo_proxy(path: str):
    import httpx
    async with httpx.AsyncClient() as client:
        try:
            url = f"{HUGO_BASE_URL}/{path}"
            response = await client.get(url)
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=dict(response.headers)
            )
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"Hugo server not reachable: {e}")

@app.get("/api/papers", response_model=List[Paper])
def api_list_papers():
    return list_papers()

@app.get("/api/status")
def api_get_status():
    return get_audit_status()

@app.post("/api/status/{filename}")
def api_update_status(filename: str, update: AuditStatusUpdate):
    update_audit_status(filename, update.approved)
    return {"status": "success", "filename": filename, "approved": update.approved}

@app.post("/api/papers/{filename}/capture")
def api_capture_figure(filename: str, request: FigureCaptureRequest):
    success = extract_figure(
        filename, 
        request.page, 
        request.x, 
        request.y, 
        request.width, 
        request.height, 
        request.figure_num
    )
    if not success:
        raise HTTPException(status_code=404, detail="Paper not found or extraction failed")
    return {"status": "success", "path": f"/static/images/papers/{filename}_fig_{request.figure_num}.png"}

# Mount project PDFs specifically to avoid conflict with workbench static files
app.mount("/project-static/pdfs", StaticFiles(directory=os.path.join(BASE_DIR, "static", "pdfs")), name="project-pdfs")

# Mount workbench UI
app.mount("/", StaticFiles(directory=WORKBENCH_STATIC, html=True), name="workbench")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
