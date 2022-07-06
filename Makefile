SHELL = /usr/bin/bash

install:
	@command -v poetry &>/dev/null || echo "ERROR: Poetry not installed" && poetry install

requirements:
	@poetry export -f requirements.txt --only main,test --output requirements.txt

test:
	@PYTHONPATH=app poetry run python -Bm coverage run -m pytest -rs tests

show-coverage-report:
	@PYTHONPATH=app poetry run python -Bm coverage report --omit 'tests/conftest.py'

serve:
	@poetry run python -Bm uvicorn app.__main__:api --port 8000 --reload

run:
	@poetry run python -B app/main.py --path-to-personal-info-file data/personal_info.csv --path-to-financial-info-file data/financial_info.csv --countries-to-filter Netherlands 'United Kingdom' > client_data/result.csv
