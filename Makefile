app:
	hugo serve

workbench:
	@echo "Starting Hugo server and workbench API..."
	hugo serve &
	python3 scripts/workbench_server.py
