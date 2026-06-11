.PHONY: install run test lint fmt typecheck check clean

install:
	poetry install

run:
	poetry run uvicorn jhansi_fleet.main:app --reload

test:
	poetry run pytest

lint:
	poetry run ruff check . 

fmt:
	poetry run ruff format .
	poetry run ruff check . --fix

typecheck:
	poetry run mypy .

check: lint fmt typecheck

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.pyc" -delete
