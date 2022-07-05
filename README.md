# Overview
This util outputs the join of two datasets with client information: personal data and financial data.

This can be achieved by running the util locally, calling `python entrypoint.py` with the required arguments described in the parser (see options with flag `-h`).
This functionality can also be served as an API.

# Requirements
To run the util or spin up the API locally `python3.10` (or later) is required.
NOTE: To use some `Make GNU` instructions, Poetry, and a subsequent installation on a virtual environment is required.

To run the util or spin up the API via the containerized util `docker` is required.

# How to use
## Locally
To run it locally you must install the requirements .

### System install
- Install the requirements locally with: `pip install -r requirements.txt`.
- Run util with `python -B app/main.py` (see options with flag `-h`).
- Spin up the API (locally) with `python -Bm uvicorn app.__main__:api --port 8000`.

### Virtual Environment install (with Poetry)
Used to develop the util. Requires Poetry 1.2 (installation from GitHub branch).

- Install the requirements locally with: `poetry install`.
- Run util with `poetry run python -B app/main.py` (see options with flag `-h`).
- Spin up the API (locally) with `poetry run python -Bm uvicorn app.__main__:api --port 8000`.

## Docker
- Build the image: `docker build --network=host . -t abm-amro-exercise`.

- Run util with:
```
docker run \
    --rm \
    -it \
    -v $(pwd)/data:/home/abm/data \
    -v $(pwd)/docker-logs:/home/abm/logs \
    --network=host \
    abm-amro-exercise

# Once inside the container, run the util following the same instructions for System install.
# NOTE: add/modify volumes to map to other datasets.
# NOTE2: network=host allows reaching the API easily (after spining it up).
# NOTE3: Docker must use a different folder for logs (or add USERs and permissions to the image). Otherwise, it will
# cause write permission issues when used along the locall installation.
```
