import os
from fastapi import FastAPI


def create_api() -> FastAPI:
    """
    Initialize the API
    """
    api = FastAPI(
        title="ABM AMRO Exercise REST API",
        description="Exercise implemented as a REST API",
        version=os.environ.get("VERSION") or "DEVELOP",
    )
    from app.router import router

    api.include_router(router)
    return api
