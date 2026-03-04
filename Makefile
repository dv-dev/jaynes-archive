archives:
	python3 scripts/build_pdf_archives.py

qa-all:
	python3 scripts/qa_papers_with_codex.py --retry-failed

clean-pdfs-all:
	./scripts/render_papers_clean_pdf.py --force

app:
	python3 scripts/build_pdf_archives.py
	hugo serve

workbench:
	@echo "Starting Hugo server and workbench API..."
	python3 scripts/build_pdf_archives.py
	hugo serve &
	python3 scripts/workbench_server.py
