SHELL = /usr/bin/bash

install:
	@command -v poetry &>/dev/null || echo "ERROR: Poetry not installed" && poetry install

requirements:
	@poetry export -f requirements.txt --only main --output requirements.txt
	@poetry export -f requirements.txt --only dev --without-hashes --output requirements-dev.txt
	@poetry export -f requirements.txt --only main,test --without-hashes --output requirements-test.txt
	@poetry export -f requirements.txt --only main,docs --without-hashes --output requirements-docs.txt

test:
	@poetry run python -Bm coverage run -m pytest -rs --html=docs/pytest-report/report.html --self-contained-html tests

show-coverage-report:
	@poetry run python -Bm coverage report --omit 'tests/conftest.py'
