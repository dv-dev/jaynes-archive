document.addEventListener('DOMContentLoaded', () => {
    let papers = [];
    let currentIndex = -1;

    const paperListEl = document.getElementById('paper-list');
    const filenameEl = document.getElementById('current-filename');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const hugoIframe = document.getElementById('hugo-iframe');
    const approvedChk = document.getElementById('approved-chk');
    const sidebarEl = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const paperSearch = document.getElementById('paper-search');

    // PDF.js variables
    const pdfjsLib = window['pdfjs-dist/build/pdf'];
    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';

    let pdfDoc = null;
    let pageNum = 1;
    let scale = 1.0;
    const canvasContainer = document.getElementById('pdf-canvas-container');

    const zoomInBtn = document.getElementById('zoom-in');
    const zoomOutBtn = document.getElementById('zoom-out');
    const zoomLevelEl = document.getElementById('zoom-level');
    const pageNumEl = document.getElementById('page-num');
    const pageCountEl = document.getElementById('page-count');
    const pdfPlaceholder = document.getElementById('pdf-placeholder');
    const prevPageBtn = document.getElementById('prev-page');
    const nextPageBtn = document.getElementById('next-page');

    // Selection variables
    let isSelecting = false;
    let startX, startY;
    let selectionBox = null;
    let selectedPageNum = null;

    canvasContainer.addEventListener('mousedown', (e) => {
        const wrapper = e.target.closest('.pdf-page-wrapper');
        if (!wrapper) return;

        isSelecting = true;
        selectedPageNum = parseInt(wrapper.dataset.pageNumber);
        
        const rect = wrapper.getBoundingClientRect();
        startX = e.clientX - rect.left;
        startY = e.clientY - rect.top;

        if (selectionBox) selectionBox.remove();
        selectionBox = document.createElement('div');
        selectionBox.style.position = 'absolute';
        selectionBox.style.border = '2px dashed #007aff';
        selectionBox.style.backgroundColor = 'rgba(0, 122, 255, 0.2)';
        selectionBox.style.pointerEvents = 'none';
        wrapper.appendChild(selectionBox);
        
        updateSelectionBox(e, wrapper);
    });

    window.addEventListener('mousemove', (e) => {
        if (!isSelecting) return;
        const wrapper = canvasContainer.querySelector(`[data-page-number="${selectedPageNum}"]`);
        if (!wrapper) return;
        updateSelectionBox(e, wrapper);
    });

    window.addEventListener('mouseup', () => {
        isSelecting = false;
    });

    function updateSelectionBox(e, wrapper) {
        const rect = wrapper.getBoundingClientRect();
        let currentX = e.clientX - rect.left;
        let currentY = e.clientY - rect.top;

        const left = Math.min(startX, currentX);
        const top = Math.min(startY, currentY);
        const width = Math.abs(startX - currentX);
        const height = Math.abs(startY - currentY);

        selectionBox.style.left = `${left}px`;
        selectionBox.style.top = `${top}px`;
        selectionBox.style.width = `${width}px`;
        selectionBox.style.height = `${height}px`;

        // Store PDF coordinates (unscaled)
        const pdfScale = scale; // This is our internal scale factor
        selectionBox.dataset.pdfX = left / pdfScale;
        selectionBox.dataset.pdfY = top / pdfScale;
        selectionBox.dataset.pdfW = width / pdfScale;
        selectionBox.dataset.pdfH = height / pdfScale;
    }

    const captureBtn = document.getElementById('capture-btn');
    const figNumInput = document.getElementById('fig-num');

    captureBtn.addEventListener('click', async () => {
        if (!selectionBox || currentIndex === -1) {
            alert('Please select a region first');
            return;
        }

        const paper = papers[currentIndex];
        const data = {
            page: selectedPageNum,
            x: parseFloat(selectionBox.dataset.pdfX),
            y: parseFloat(selectionBox.dataset.pdfY),
            width: parseFloat(selectionBox.dataset.pdfW),
            height: parseFloat(selectionBox.dataset.pdfH),
            figure_num: parseInt(figNumInput.value)
        };

        try {
            captureBtn.disabled = true;
            captureBtn.textContent = 'Capturing...';
            const response = await fetch(`/api/papers/${paper.filename}/capture`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            const result = await response.json();
            if (response.ok) {
                alert(`Figure captured successfully! Saved to ${result.path}`);
            } else {
                alert(`Error: ${result.detail}`);
            }
        } catch (error) {
            console.error('Capture failed:', error);
            alert('Capture failed. See console for details.');
        } finally {
            captureBtn.disabled = false;
            captureBtn.textContent = 'Capture Selection';
        }
    });

    // Observer to update current page number in header
    const pageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                pageNum = parseInt(entry.target.dataset.pageNumber);
                pageNumEl.textContent = pageNum;
            }
        });
    }, { threshold: 0.5 });

    async function renderPage(num, canvas) {
        const page = await pdfDoc.getPage(num);
        const ctx = canvas.getContext('2d');
        const viewport = page.getViewport({ scale: scale * window.devicePixelRatio });
        
        canvas.height = viewport.height;
        canvas.width = viewport.width;
        canvas.style.width = `${viewport.width / window.devicePixelRatio}px`;
        canvas.style.height = `${viewport.height / window.devicePixelRatio}px`;

        const renderContext = {
            canvasContext: ctx,
            viewport: viewport
        };
        await page.render(renderContext).promise;
    }

    async function loadPDF(filename) {
        const url = `/project-static/pdfs/raw/${filename}.pdf`;
        pdfPlaceholder.style.display = 'block';
        canvasContainer.innerHTML = '';
        
        try {
            const loadingTask = pdfjsLib.getDocument(url);
            pdfDoc = await loadingTask.promise;
            pageCountEl.textContent = pdfDoc.numPages;
            
            // Initial Fit to Width
            const firstPage = await pdfDoc.getPage(1);
            const containerWidth = canvasContainer.clientWidth - 60; // Padding
            const unscaledViewport = firstPage.getViewport({ scale: 1 });
            scale = containerWidth / unscaledViewport.width;
            zoomLevelEl.textContent = `${Math.round(scale * 100)}%`;

            pdfPlaceholder.style.display = 'none';
            
            // Create canvases for all pages (Continuous Scroll)
            for (let i = 1; i <= pdfDoc.numPages; i++) {
                const wrapper = document.createElement('div');
                wrapper.className = 'pdf-page-wrapper';
                wrapper.dataset.pageNumber = i;
                
                const canvas = document.createElement('canvas');
                canvas.id = `pdf-canvas-${i}`;
                wrapper.appendChild(canvas);
                canvasContainer.appendChild(wrapper);
                
                pageObserver.observe(wrapper);
                
                // Render the page
                await renderPage(i, canvas);
            }
        } catch (error) {
            console.error('Error loading PDF:', error);
            pdfPlaceholder.innerHTML = `<h3 style="color:red">Error loading PDF</h3><p>${error.message}</p>`;
        }
    }

    async function reRenderAll() {
        if (!pdfDoc) return;
        zoomLevelEl.textContent = `${Math.round(scale * 100)}%`;
        for (let i = 1; i <= pdfDoc.numPages; i++) {
            const canvas = document.getElementById(`pdf-canvas-${i}`);
            if (canvas) await renderPage(i, canvas);
        }
    }

    zoomInBtn.addEventListener('click', () => {
        scale += 0.2;
        reRenderAll();
    });

    zoomOutBtn.addEventListener('click', () => {
        if (scale <= 0.2) return;
        scale -= 0.2;
        reRenderAll();
    });

    prevPageBtn.addEventListener('click', () => {
        if (pageNum <= 1) return;
        const prevWrapper = canvasContainer.querySelector(`[data-page-number="${pageNum - 1}"]`);
        if (prevWrapper) prevWrapper.scrollIntoView();
    });

    nextPageBtn.addEventListener('click', () => {
        if (!pdfDoc || pageNum >= pdfDoc.numPages) return;
        const nextWrapper = canvasContainer.querySelector(`[data-page-number="${pageNum + 1}"]`);
        if (nextWrapper) nextWrapper.scrollIntoView();
    });

    const findInput = document.getElementById('find-input');
    const findCounter = document.getElementById('find-counter');
    let searchMatches = 0;
    let currentMatchIndex = 0;
    let lastQuery = '';

    findInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            const query = findInput.value.trim();
            if (!query) {
                findCounter.textContent = '';
                return;
            }

            const backward = e.shiftKey;
            
            // If query changed, count matches
            if (query !== lastQuery) {
                const doc = hugoIframe.contentDocument || hugoIframe.contentWindow.document;
                const text = doc.body.innerText;
                const regex = new RegExp(query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
                const matches = text.match(regex);
                searchMatches = matches ? matches.length : 0;
                currentMatchIndex = 0;
                lastQuery = query;
            }

            const found = hugoIframe.contentWindow.find(query, false, backward, true);
            
            if (found) {
                if (backward) {
                    currentMatchIndex = currentMatchIndex <= 1 ? searchMatches : currentMatchIndex - 1;
                } else {
                    currentMatchIndex = currentMatchIndex >= searchMatches ? 1 : currentMatchIndex + 1;
                }
            } else {
                // Wrap around
                hugoIframe.contentWindow.find(query, false, backward, true);
                currentMatchIndex = backward ? searchMatches : 1;
            }

            findCounter.textContent = searchMatches > 0 ? `${currentMatchIndex}/${searchMatches}` : '0/0';
        }
    });

    findInput.addEventListener('input', () => {
        if (!findInput.value.trim()) {
            findCounter.textContent = '';
            lastQuery = '';
        }
    });

    sidebarToggle.addEventListener('click', () => {
        sidebarEl.classList.toggle('collapsed');
    });

    async function fetchPapers() {
        try {
            console.log('Fetching papers...');
            const response = await fetch('/api/papers');
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            papers = await response.json();
            console.log(`Loaded ${papers.length} papers`);
            
            if (papers.length === 0) {
                paperListEl.innerHTML = '<li style="color:red; cursor:default;">No papers found. Check server logs.</li>';
                return;
            }
            
            renderPaperList();
            if (papers.length > 0) {
                const hash = window.location.hash.substring(1);
                const foundIndex = papers.findIndex(p => p.filename === hash);
                selectPaper(foundIndex !== -1 ? foundIndex : 0);
            }
        } catch (error) {
            console.error('Failed to fetch papers:', error);
        }
    }

    function renderPaperList() {
        const filter = paperSearch.value.toLowerCase();
        paperListEl.innerHTML = '';
        papers.forEach((paper, index) => {
            if (filter && !paper.title.toLowerCase().includes(filter) && !paper.filename.toLowerCase().includes(filter)) {
                return;
            }
            
            const li = document.createElement('li');
            li.textContent = paper.title || paper.filename;
            if (index === currentIndex) li.classList.add('active');
            if (paper.approved) li.classList.add('approved');
            li.addEventListener('click', () => selectPaper(index));
            paperListEl.appendChild(li);
        });
    }

    function selectPaper(index) {
        if (index < 0 || index >= papers.length) return;
        currentIndex = index;
        const paper = papers[currentIndex];

        filenameEl.textContent = paper.filename;
        approvedChk.checked = paper.approved;
        
        hugoIframe.src = `/hugo-proxy/papers/${paper.filename.toLowerCase()}/`;

        if (paper.has_pdf) {
            loadPDF(paper.filename);
        } else {
            canvasContainer.innerHTML = '';
            pdfPlaceholder.style.display = 'block';
            pdfPlaceholder.innerHTML = '<h3>No PDF available</h3>';
        }

        history.replaceState(null, null, `#${paper.filename}`);
        renderPaperList();
        
        setTimeout(() => {
            const activeItem = paperListEl.querySelector('.active');
            if (activeItem) activeItem.scrollIntoView({ block: 'nearest' });
        }, 0);
    }

    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) selectPaper(currentIndex - 1);
    });

    nextBtn.addEventListener('click', () => {
        if (currentIndex < papers.length - 1) selectPaper(currentIndex + 1);
    });

    paperSearch.addEventListener('input', () => {
        renderPaperList();
    });

    approvedChk.addEventListener('change', async () => {
        if (currentIndex === -1) return;
        const paper = papers[currentIndex];
        try {
            const response = await fetch(`/api/status/${paper.filename}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ approved: approvedChk.checked })
            });
            if (response.ok) {
                paper.approved = approvedChk.checked;
                renderPaperList();
            }
        } catch (error) {
            console.error('Failed to update status:', error);
        }
    });

    fetchPapers();
});
