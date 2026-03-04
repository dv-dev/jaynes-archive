archives:
	python3 scripts/build_pdf_archives.py

app:
	python3 scripts/build_pdf_archives.py
	hugo serve

workbench:
	@echo "Starting Hugo server and workbench API..."
	python3 scripts/build_pdf_archives.py
	hugo serve &
	python3 scripts/workbench_server.py
