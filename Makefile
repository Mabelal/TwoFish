default: run

run:
	python app.py

install:
	pip install --upgrade pip --quiet && pip install -r requirements.txt --quiet

lint:
	pylint-fail-under --fail_under 10.0 src && python -m black . --check

fixlint:
	python -m black .
