#!/usr/bin/env python3
"""Render clean, journal-style PDFs from Hugo paper pages.

Flow per paper:
1) Load rendered Hugo page (/papers/<slug>/).
2) Extract only paper metadata + abstract + article content (strip site chrome/buttons).
3) Build a clean print HTML with KaTeX auto-render.
4) Print that clean HTML to PDF with headless Chrome.

This preserves math rendering behavior (KaTeX) while producing a document-style PDF.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen


DEFAULT_CONTENT_DIR = "content/papers"
DEFAULT_OUTPUT_DIR = "static/pdfs/clean"
DEFAULT_STATE_FILE = "data/paper_clean_pdf_status.json"
DEFAULT_LOG_DIR = ".run_logs/paper_clean_pdf_logs"


TITLE_RE = re.compile(r'<h1 class="text-3xl sm:text-4xl font-bold mb-3">(.*?)</h1>', re.S | re.I)
AUTHOR_RE = re.compile(r'<p class="text-xl text-gray-700 mb-2">(.*?)</p>', re.S | re.I)
YEAR_RE = re.compile(r'<p class="text-xl text-gray-600">(.*?)</p>', re.S | re.I)
ABSTRACT_RE = re.compile(r'<div class="mb-8 abstract-container">\s*(.*?)\s*</div>', re.S | re.I)
ARTICLE_RE = re.compile(r'<article class="paper-content">\s*(.*?)\s*</article>', re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")
PDF_UNRENDERED_MATH_STRONG_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\$\$"),
    re.compile(r"\\begin\{"),
    re.compile(r"\\end\{"),
    re.compile(r"\\tag\{"),
    re.compile(r"\\(?:frac|sum|int|prod|sqrt|left|right|cdot|times|alpha|beta|gamma|delta|Delta|rho|sigma|theta|eta|zeta|mu|nu|pi|lambda)\b"),
)
PDF_INLINE_DOLLAR_PATTERN = re.compile(r"\$[A-Za-z\\(]")


@dataclass
class FileStatus:
    status: str
    attempts: int
    last_run_utc: str | None
    return_code: int | None
    duration_sec: float | None
    output_pdf: str | None
    source_url: str | None
    error: str | None

    def as_dict(self) -> dict:
        return {
            "status": self.status,
            "attempts": self.attempts,
            "last_run_utc": self.last_run_utc,
            "return_code": self.return_code,
            "duration_sec": self.duration_sec,
            "output_pdf": self.output_pdf,
            "source_url": self.source_url,
            "error": self.error,
        }


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_state(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_state(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def list_paper_files(content_dir: Path) -> list[Path]:
    return sorted(content_dir.glob("*.md"), key=lambda p: p.name.lower())


def find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def wait_for_http(url: str, timeout_sec: int = 45) -> bool:
    deadline = time.time() + timeout_sec
    while time.time() < deadline:
        try:
            with urlopen(url, timeout=3) as resp:
                if resp.status < 500:
                    return True
        except Exception:
            pass
        time.sleep(0.5)
    return False


def http_get_text(url: str, timeout_sec: int = 30) -> str:
    with urlopen(url, timeout=timeout_sec) as resp:
        return resp.read().decode("utf-8", errors="replace")


def find_group(regex: re.Pattern[str], text: str) -> str | None:
    m = regex.search(text)
    if not m:
        return None
    return m.group(1).strip()


def strip_tags(s: str) -> str:
    return TAG_RE.sub("", s).strip()


def tag_no_indent_after_display_math(article_html: str) -> str:
    # Hugo can emit block math as raw `$$...$$` between paragraph tags:
    #   </p> $$ ... $$ <p>...
    # Mark the following paragraph explicitly no-indent so styling is deterministic.
    pattern = re.compile(r"(\$\$[\s\S]*?\$\$)\s*<p>", re.S)
    return pattern.sub(r'\1<p class="no-indent-after-display">', article_html)

def extract_pdf_text(pdf_path: Path, timeout_sec: int = 30) -> str | None:
    pdftotext_bin = shutil.which("pdftotext")
    if not pdftotext_bin:
        return None
    cp = subprocess.run(
        [pdftotext_bin, str(pdf_path), "-"],
        capture_output=True,
        text=True,
        check=False,
        timeout=timeout_sec,
    )
    if cp.returncode != 0:
        return None
    return cp.stdout


def find_unrendered_math_markers(pdf_text: str) -> list[str]:
    markers: list[str] = []
    seen: set[str] = set()
    for pattern in PDF_UNRENDERED_MATH_STRONG_PATTERNS:
        for match in pattern.finditer(pdf_text):
            snippet = pdf_text[max(0, match.start() - 24) : match.end() + 24]
            snippet = " ".join(snippet.split())
            if snippet and snippet not in seen:
                seen.add(snippet)
                markers.append(snippet)
            if len(markers) >= 5:
                return markers
    inline_dollar_matches = list(PDF_INLINE_DOLLAR_PATTERN.finditer(pdf_text))
    if len(inline_dollar_matches) >= 3:
        for match in inline_dollar_matches[:5]:
            snippet = pdf_text[max(0, match.start() - 24) : match.end() + 24]
            snippet = " ".join(snippet.split())
            if snippet and snippet not in seen:
                seen.add(snippet)
                markers.append(snippet)
            if len(markers) >= 5:
                return markers
    return markers


def detect_unrendered_math(pdf_path: Path) -> str | None:
    pdf_text = extract_pdf_text(pdf_path)
    if pdf_text is None:
        return None
    markers = find_unrendered_math_markers(pdf_text)
    if not markers:
        return None
    return "unrendered math markers in PDF text: " + " | ".join(markers)


def build_clean_html(source_html: str, slug: str) -> str:
    article_html = find_group(ARTICLE_RE, source_html)
    if not article_html:
        raise ValueError("Could not extract article body from rendered page")
    article_html = tag_no_indent_after_display_math(article_html)

    title_html = find_group(TITLE_RE, source_html) or html.escape(slug)
    author_html = find_group(AUTHOR_RE, source_html) or ""
    year_html = find_group(YEAR_RE, source_html) or ""
    abstract_inner = find_group(ABSTRACT_RE, source_html) or ""
    title_text = html.escape(strip_tags(title_html) or slug)
    author_text = html.escape(strip_tags(author_html))
    year_text = html.escape(strip_tags(year_html))

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_text}</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.25/dist/katex.min.css" crossorigin="anonymous">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.25/dist/katex.min.js" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.25/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
  <style>
    @page {{ size: Letter; margin: 1in 1in 1in 1in; }}
    body {{
      font-family: "Times New Roman", Times, serif;
      color: #111111;
      font-size: 13.5pt;
      line-height: 1.52;
      margin: 0;
      background: #fff;
      text-rendering: optimizeLegibility;
      -webkit-font-smoothing: antialiased;
    }}
    .paper {{
      max-width: 6.5in;
      margin: 0 auto;
    }}
    .title {{
      font-size: 1.64em;
      line-height: 1.2;
      font-weight: 700;
      margin: 0 0 0.34rem 0;
      text-align: center;
    }}
    .year {{
      text-align: center;
      color: #444444;
      font-size: 0.91em;
      margin: 0 0 0.85rem 0;
    }}
    .authors {{
      text-align: center;
      color: #222222;
      font-size: 1em;
      margin: 0 0 0.18rem 0;
    }}
    .abstract {{
      max-width: 82%;
      margin-left: auto;
      margin-right: auto;
      padding: 0;
      margin-top: 0;
      margin-bottom: 1rem;
      color: #222;
      font-size: 0.95em;
      text-align: justify;
    }}
    .abstract strong {{
      font-weight: 700;
    }}
    article {{
      max-width: 100%;
      text-align: justify;
    }}
    article h1, article h2, article h3, article h4, article h5, article h6 {{
      page-break-after: avoid;
      break-after: avoid-page;
      margin-top: 1.1em;
      margin-bottom: 0.35em;
      font-weight: 700;
      line-height: 1.2;
    }}
    article h1 {{
      font-size: 1.2em;
      padding-bottom: 0;
    }}
    article h2 {{ font-size: 1.11em; }}
    article h3 {{ font-size: 1.04em; }}
    article p {{
      margin: 0;
      text-indent: 1.15em;
      orphans: 3;
      widows: 3;
    }}
    article p + p {{
      margin-top: 0.14em;
    }}
    article blockquote + p,
    article ul + p,
    article ol + p,
    article table + p,
    article .katex-display + p {{
      text-indent: 0;
      margin-top: 0.3em;
    }}
    article ul, article ol {{
      margin: 0.28em 0 0.55em 1.15em;
      padding: 0;
    }}
    article li {{ margin-bottom: 0.25em; }}
    article blockquote {{
      border-left: 0;
      margin: 0.6em 0 0.6em 1.2em;
      padding: 0;
      color: #333;
      font-style: italic;
    }}
    article table {{
      border-collapse: collapse;
      width: 100%;
      margin: 0.68em 0;
      font-size: 0.91em;
      page-break-inside: avoid;
      break-inside: avoid;
    }}
    article th, article td {{
      border: 0;
      border-bottom: 1px solid #d8d8d8;
      padding: 0.2em 0.32em;
      vertical-align: top;
    }}
    article th {{
      font-weight: 700;
      border-top: 1px solid #bfbfbf;
    }}
    article img {{
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0.7rem auto;
      page-break-inside: avoid;
    }}
    article hr {{
      display: none;
    }}
    a {{
      color: #111;
      text-decoration: none;
    }}
    sup {{
      font-size: 0.74em;
      line-height: 0;
      vertical-align: super;
    }}
    .footnotes {{
      margin-top: 0.9em;
      padding-top: 0.2em;
      border-top: 0;
      font-size: 0.89em;
    }}
    .footnotes ol {{
      margin: 0.4em 0 0 1.2em;
      padding: 0;
    }}
    .footnotes li {{
      margin-bottom: 0.25em;
    }}
    .katex-display {{
      overflow: visible;
      white-space: normal;
      page-break-inside: avoid;
      break-inside: avoid;
      margin: 0.55em 0 0.65em 0;
      text-indent: 0;
    }}
    .katex {{
      font-size: 1.04em;
      line-height: 1.2;
    }}
    article .katex-display + p {{
      text-indent: 0 !important;
    }}
    article p:has(.katex-display) + p {{
      text-indent: 0 !important;
      margin-top: 0.3em;
    }}
    article p.no-indent-after-display {{
      text-indent: 0 !important;
      margin-top: 0.3em;
    }}
    pre, code {{
      white-space: pre-wrap;
      word-break: break-word;
    }}
  </style>
  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      function markNextParagraphNoIndent(fromElement) {{
        let next = fromElement ? fromElement.nextElementSibling : null;
        while (next && next.tagName && next.tagName.toLowerCase() !== "p") {{
          next = next.nextElementSibling;
        }}
        if (next) next.classList.add("no-indent-after-display");
      }}

      // Pass 1: detect raw markdown display-math paragraphs before KaTeX runs.
      document.querySelectorAll("article p").forEach((p) => {{
        const txt = (p.textContent || "").trim();
        if (txt.startsWith("$$") && txt.endsWith("$$")) {{
          markNextParagraphNoIndent(p);
        }}
      }});

      function runMathRender() {{
        if (!window.renderMathInElement) return false;
        window.renderMathInElement(document.body, {{
          delimiters: [
            {{left: "$$", right: "$$", display: true}},
            {{left: "\\\\[", right: "\\\\]", display: true}},
            {{left: "$", right: "$", display: false}},
            {{left: "\\\\(", right: "\\\\)", display: false}}
          ],
          output: "html",
          throwOnError: false,
          strict: "ignore",
          trust: true
        }});

        // Pass 2: detect KaTeX display output wrappers and mark next paragraph.
        document.querySelectorAll("article .katex-display").forEach((disp) => {{
          let block = disp.closest("p, div, figure, blockquote, li, td, th");
          if (!block) block = disp.parentElement;
          markNextParagraphNoIndent(block);
        }});
        return true;
      }}

      // KaTeX assets are loaded via external deferred scripts.
      // Retry briefly in case network/script execution is delayed for long papers.
      let attempts = 0;
      const maxAttempts = 80; // ~8s at 100ms interval
      const timer = setInterval(() => {{
        attempts += 1;
        if (runMathRender() || attempts >= maxAttempts) {{
          clearInterval(timer);
        }}
      }}, 100);
    }});
  </script>
</head>
<body>
  <div class="paper">
    <h1 class="title">{title_html}</h1>
    {"<p class='authors'>" + author_html + "</p>" if author_text else ""}
    {"<p class='year'>" + year_html + "</p>" if year_text else ""}
    {"<section class='abstract'>" + abstract_inner + "</section>" if abstract_inner else ""}
    <article>
      {article_html}
    </article>
  </div>
</body>
</html>
"""


def print_progress(done: int, total: int, current: str, width: int = 34) -> None:
    ratio = 1.0 if total == 0 else done / total
    filled = int(ratio * width)
    bar = "#" * filled + "-" * (width - filled)
    msg = f"[{bar}] {done}/{total} | {current}"
    print("\r" + msg[:220], end="", flush=True)


def ensure_entries(state: dict, files_rel: list[str]) -> None:
    file_map = state.setdefault("files", {})
    if not isinstance(file_map, dict):
        state["files"] = {}
        file_map = state["files"]

    for relpath in files_rel:
        if relpath not in file_map:
            file_map[relpath] = FileStatus(
                status="pending",
                attempts=0,
                last_run_utc=None,
                return_code=None,
                duration_sec=None,
                output_pdf=None,
                source_url=None,
                error=None,
            ).as_dict()
        elif isinstance(file_map[relpath], dict) and file_map[relpath].get("status") == "running":
            file_map[relpath]["status"] = "pending"

    for relpath in list(file_map.keys()):
        if relpath not in files_rel and isinstance(file_map[relpath], dict):
            file_map[relpath]["status"] = "skipped_missing_from_repo"


def count_status(state: dict) -> dict[str, int]:
    ctr: Counter[str] = Counter()
    files = state.get("files", {})
    if isinstance(files, dict):
        for v in files.values():
            if isinstance(v, dict):
                ctr[str(v.get("status", "unknown"))] += 1
    return dict(ctr)


def pick_chrome_binary() -> str | None:
    for name in ("google-chrome", "google-chrome-stable", "chromium-browser", "chromium"):
        path = shutil.which(name)
        if path:
            return path
    return None


def start_hugo(repo_root: Path, port: int) -> subprocess.Popen[str]:
    cmd = [
        "hugo",
        "server",
        "--bind",
        "127.0.0.1",
        "--port",
        str(port),
        "--disableFastRender",
        "--renderToMemory",
        "--noHTTPCache",
    ]
    return subprocess.Popen(
        cmd,
        cwd=str(repo_root),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )


def render_pdf_from_html(chrome_bin: str, html_path: Path, out_pdf: Path, wait_ms: int, timeout_sec: int) -> subprocess.CompletedProcess[str]:
    cmd = [
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--disable-dev-shm-usage",
        f"--virtual-time-budget={wait_ms}",
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={out_pdf}",
        html_path.as_uri(),
    ]
    return subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=timeout_sec)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render clean PDFs from Hugo paper pages with KaTeX support.")
    parser.add_argument("--repo-root", default=".", help="Repository root path (default: .)")
    parser.add_argument("--content-dir", default=DEFAULT_CONTENT_DIR, help=f"Relative content dir (default: {DEFAULT_CONTENT_DIR})")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help=f"Output PDF directory (default: {DEFAULT_OUTPUT_DIR})")
    parser.add_argument("--state-file", default=DEFAULT_STATE_FILE, help=f"State JSON path (default: {DEFAULT_STATE_FILE})")
    parser.add_argument("--log-dir", default=DEFAULT_LOG_DIR, help=f"Per-file log directory (default: {DEFAULT_LOG_DIR})")
    parser.add_argument("--wait-ms", type=int, default=60000, help="Chrome virtual time budget per file (ms)")
    parser.add_argument("--timeout-sec", type=int, default=120, help="Per-file Chrome timeout (seconds)")
    parser.add_argument("--retry-failed", action="store_true", help="Retry files with status=failed")
    parser.add_argument("--force", action="store_true", help="Render all files regardless of current status")
    parser.add_argument("--max-files", type=int, default=0, help="Optional cap on files processed this run (0 = no cap)")
    parser.add_argument("--slugs", default="", help="Optional comma-separated paper slugs to process")
    parser.add_argument("--render-retries", type=int, default=2, help="Extra render attempts per file when verification fails")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    content_dir = (repo_root / args.content_dir).resolve()
    output_dir = (repo_root / args.output_dir).resolve()
    state_path = (repo_root / args.state_file).resolve()
    log_dir = (repo_root / args.log_dir).resolve()

    if not content_dir.exists():
        print(f"Error: content directory not found: {content_dir}", file=sys.stderr)
        return 1
    if not shutil.which("hugo"):
        print("Error: hugo not found in PATH", file=sys.stderr)
        return 1
    chrome_bin = pick_chrome_binary()
    if not chrome_bin:
        print("Error: Chrome/Chromium not found in PATH", file=sys.stderr)
        return 1

    files_abs = list_paper_files(content_dir)
    selected_slugs = {slug.strip().lower() for slug in args.slugs.split(",") if slug.strip()}
    if selected_slugs:
        files_abs = [p for p in files_abs if p.stem.lower() in selected_slugs]
        missing_slugs = sorted(selected_slugs - {p.stem.lower() for p in files_abs})
        if missing_slugs:
            print(f"Error: requested slugs not found: {', '.join(missing_slugs)}", file=sys.stderr)
            return 1
    files_rel = [str(p.relative_to(repo_root)) for p in files_abs]
    if not files_rel:
        print("No markdown files found.")
        return 0

    state = load_state(state_path)
    state["schema_version"] = 1
    state["repo_root"] = str(repo_root)
    state["content_dir"] = str(Path(args.content_dir))
    state["output_dir"] = str(Path(args.output_dir))
    state["state_file"] = str(Path(args.state_file))
    state["log_dir"] = str(Path(args.log_dir))
    state["last_run_started_utc"] = utc_now()
    ensure_entries(state, files_rel)
    save_state(state_path, state)

    file_map = state["files"]
    assert isinstance(file_map, dict)

    to_process: list[str] = []
    for rel in files_rel:
        ent = file_map.get(rel, {})
        status = ent.get("status") if isinstance(ent, dict) else None
        if args.force:
            to_process.append(rel)
            continue
        if status == "completed":
            continue
        if status == "failed" and not args.retry_failed:
            continue
        to_process.append(rel)
    if args.max_files > 0:
        to_process = to_process[: args.max_files]

    total = len(files_rel)
    done_before = sum(
        1 for rel in files_rel if isinstance(file_map.get(rel), dict) and file_map[rel].get("status") == "completed"
    )
    planned = len(to_process)
    print(f"Found {total} files. Already completed: {done_before}. Planned this run: {planned}.")
    if planned == 0:
        state["counts"] = count_status(state)
        state["last_run_finished_utc"] = utc_now()
        save_state(state_path, state)
        print("Nothing to process.")
        return 0

    port = find_free_port()
    base_url = f"http://127.0.0.1:{port}"
    hugo_proc = start_hugo(repo_root, port)
    try:
        if not wait_for_http(base_url, timeout_sec=60):
            hugo_logs = ""
            if hugo_proc.stdout:
                hugo_logs = hugo_proc.stdout.read(8000)
            print(f"Error: Hugo server failed to start at {base_url}\n{hugo_logs}", file=sys.stderr)
            return 1

        output_dir.mkdir(parents=True, exist_ok=True)
        log_dir.mkdir(parents=True, exist_ok=True)

        processed = 0
        with tempfile.TemporaryDirectory(prefix="paper-clean-pdf-") as tempdir:
            temp_root = Path(tempdir)
            for rel in to_process:
                processed += 1
                done_count = done_before + processed - 1
                slug = Path(rel).stem
                src_url = f"{base_url}/papers/{slug.lower()}/"
                out_pdf = output_dir / f"{slug}.pdf"
                log_path = log_dir / f"{slug}.log"
                clean_html_path = temp_root / f"{slug}.html"

                print_progress(done_count, total, f"rendering {slug}.pdf")

                ent = file_map.get(rel, {})
                if not isinstance(ent, dict):
                    ent = FileStatus("pending", 0, None, None, None, None, None, None).as_dict()
                    file_map[rel] = ent
                ent["status"] = "running"
                ent["last_run_utc"] = utc_now()
                ent["return_code"] = None
                ent["duration_sec"] = None
                ent["output_pdf"] = str(out_pdf.relative_to(repo_root))
                ent["source_url"] = src_url
                ent["error"] = None
                save_state(state_path, state)

                log_chunks: list[str] = []
                max_attempts = max(1, args.render_retries + 1)
                for render_attempt in range(1, max_attempts + 1):
                    started = time.time()
                    ent["status"] = "running"
                    ent["attempts"] = int(ent.get("attempts", 0)) + 1
                    ent["last_run_utc"] = utc_now()
                    ent["return_code"] = None
                    ent["duration_sec"] = None
                    ent["error"] = None
                    save_state(state_path, state)

                    try:
                        rendered_html = http_get_text(src_url, timeout_sec=35)
                        clean_html = build_clean_html(rendered_html, slug)
                        clean_html_path.write_text(clean_html, encoding="utf-8")

                        cp = render_pdf_from_html(
                            chrome_bin=chrome_bin,
                            html_path=clean_html_path,
                            out_pdf=out_pdf,
                            wait_ms=args.wait_ms,
                            timeout_sec=args.timeout_sec,
                        )
                        duration = round(time.time() - started, 3)
                        ent["duration_sec"] = duration
                        ent["last_run_utc"] = utc_now()
                        ent["return_code"] = cp.returncode

                        verify_error = None
                        if cp.returncode == 0 and out_pdf.exists() and out_pdf.stat().st_size > 0:
                            verify_error = detect_unrendered_math(out_pdf)
                            if verify_error is None:
                                ent["status"] = "completed"
                            else:
                                ent["status"] = "failed"
                                ent["error"] = verify_error
                        else:
                            ent["status"] = "failed"
                            err = (cp.stderr or cp.stdout or "").strip()
                            ent["error"] = err[-1200:] if err else "chrome print failed"

                        log_chunks.append(
                            f"attempt: {render_attempt}/{max_attempts}\n"
                            f"source_url: {src_url}\n"
                            f"clean_html: {clean_html_path}\n"
                            f"output_pdf: {out_pdf}\n"
                            f"duration_sec: {duration}\n"
                            f"verification: {verify_error or 'ok'}\n\n"
                            f"=== STDOUT ===\n{cp.stdout}\n\n"
                            f"=== STDERR ===\n{cp.stderr}\n"
                        )
                    except Exception as exc:
                        duration = round(time.time() - started, 3)
                        ent["duration_sec"] = duration
                        ent["last_run_utc"] = utc_now()
                        ent["status"] = "failed"
                        ent["return_code"] = 1
                        ent["error"] = str(exc)
                        log_chunks.append(
                            f"attempt: {render_attempt}/{max_attempts}\n"
                            f"source_url: {src_url}\n"
                            f"output_pdf: {out_pdf}\n"
                            f"duration_sec: {duration}\n\n"
                            f"ERROR: {exc}\n"
                        )

                    save_state(state_path, state)
                    if ent["status"] == "completed":
                        break

                log_path.write_text("\n\n".join(log_chunks) + "\n", encoding="utf-8")

        final_done = sum(
            1 for rel in files_rel if isinstance(file_map.get(rel), dict) and file_map[rel].get("status") == "completed"
        )
        print_progress(final_done, total, "done")
        print()

        state["counts"] = count_status(state)
        state["last_run_finished_utc"] = utc_now()
        save_state(state_path, state)

        completed_now = sum(
            1 for rel in to_process if isinstance(file_map.get(rel), dict) and file_map[rel].get("status") == "completed"
        )
        failed_now = planned - completed_now
        print(f"Run complete. Completed this run: {completed_now}. Failed this run: {failed_now}.")
        print(f"Output dir: {output_dir}")
        print(f"State:      {state_path}")
        print(f"Logs:       {log_dir}")
        return 0 if failed_now == 0 else 2
    finally:
        if hugo_proc.poll() is None:
            hugo_proc.terminate()
            try:
                hugo_proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                hugo_proc.kill()


if __name__ == "__main__":
    raise SystemExit(main())
