default:
	@echo "Options: run, test."

run:
	uv run main.py

test:
	uv run -m unittest discover -s tests/ -p '*.py'

