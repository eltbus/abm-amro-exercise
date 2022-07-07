docker run \
    --network=host \
    --rm \
    -it \
    -v $(pwd)/data:/home/abm/data \
    -v $(pwd)/logs:/home/abm/logs \
    --entrypoint python \
    abm-amro-exercise -m pytest tests
