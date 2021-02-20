default: run

run:
	PYTHONPATH=. python src/app.py

install:
	pip install --upgrade pip --quiet && pip install -r requirements.txt --quiet

lint:
	python -m black . --check

fixlint:
	python -m black .
