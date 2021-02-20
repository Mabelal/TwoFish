default: run

run:
	python app.py

install:
	pip install --upgrade pip --quiet && pip install -r requirements.txt

lint:
	pylint-fail-under --fail_under 10.0 . && python -m black . --exclude venv --exclude /*.json/ --check

fixlint:
	python -m black . --exclude venv --exclude /*.json/
