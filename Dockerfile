FROM python:3.10-slim

WORKDIR /home/abm
RUN pip install -U pip
COPY ./app app
COPY ./tests tests
COPY ./requirements.txt requirements.txt
RUN pip --no-cache-dir install -r requirements.txt
ENTRYPOINT ["/bin/bash"]
