

# Makefile – Hybrid Alignment Architecture 

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

test:
	pytest

lint:
	ruff check app tests

format:
	ruff format app tests

env:
	cp .env.example .env

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +

all: install run