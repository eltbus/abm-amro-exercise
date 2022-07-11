# Overview
This util outputs the join of two datasets with client information: personal data and financial data.

This can be achieved by running the CLI program or spining up an API and calling the endpoint.

# Requirements
To run the util or spin up the API locally `python3.10` (or later) is required.
To run the util or spin up the API via the containerized util `docker` is required.

# Installation

## System
**NOTE**: it's recommended to use a Virtual Environment. Read [this](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).
- Install the requirements with: `pip install -r requirements.txt`.

## Docker
- Build the image: `docker build --network=host . -t abm-amro-exercise`.

# Tests
Run tests with the system installation or within the built docker image as follows:

## System
Run tests with: `python -m pytest tests`.
Run tests generating a coverage report with: `python -m coverage run -m pytest tests`.
To show the coverage report, run `python -m coverage report --omit 'tests/conftest.py'`.

## Docker
Run tests with: `python -m pytest tests`.
```
docker run \
    --rm \
    -it \
    -v <LOCAL PATH TO FINANCIAL AND PERSONAL DATA>:/home/abm/data \
    -v <LOCAL PATH TO STORE LOGS FROM DOCKER APP>:/home/abm/logs \
    --network=host \
    --entrypoint python \
    abm-amro-exercise -m pytest tests`
```

NOTE: Change `pytest tests` to `coverage run -m pytest tests` to generate a coverage file (remember to add another volume to persist it in local!)

# Usage
## System install
- Run util with `python -B app/core.py` (see options with flag `-h`), OR spin up the API (locally) with `python -Bm uvicorn app.__main__:api --port 8000`.

CLI usage example:
```
python -B app/core.py \
    --path-to-personal-info-file data/personal_info.csv
    --path-to-financial-info-file data/financial_info.csv
    --countries Netherlands 'United Kingdom'
```

## Docker install
- Run util with:
```
docker run \
    --rm \
    -it \
    -v $(pwd)/data:/home/abm/data \
    -v $(pwd)/docker-logs:/home/abm/logs \
    --network=host \
    abm-amro-exercise
```
**Once inside the container, run the util following the same instructions for System install.**

**NOTE**: add/modify volumes to map to other datasets, write the output, etc.
**NOTE2**: network=host allows reaching the API easily (after spining it up).
**NOTE3**: Docker must use a different folder for logs (or add USERs and permissions to the image). Otherwise, it will
cause write permission issues when used along the locall installation.


# `client_data/result.csv`
## System install
```
# Create the desired destination folder
mkdir -p client_data

# Pipe the output of the program to the deesired filepath
python -B app/core.py \
    --path-to-personal-info-file data/personal_info.csv
    --path-to-financial-info-file data/financial_info.csv
    --countries Netherlands 'United Kingdom' > client_data/result.csv
```

## Docker install
```
# Create the desired destination folder
mkdir -p client_data

# Pipe the output of the program to the desired filepath.
docker run \
    --rm \
    -it \
    -v $(pwd)/data:/home/abm/data \
    -v $(pwd)/docker-logs:/home/abm/logs \
    --network=host \
    --entrypoint=python \
    abm-amro-exercise \
    --path-to-personal-info-file data/personal_info.csv
    --path-to-financial-info-file data/financial_info.csv
    --countries Netherlands 'United Kingdom' > client_data/result.csv
```
