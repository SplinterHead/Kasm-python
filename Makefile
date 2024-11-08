.PHONY: fmt test

fmt: 
	poetry run black kasm_python/ tests/
	poetry run isort --profile black kasm_python/ tests/

test:
	poetry run pytest


all: fmt test