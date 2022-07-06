# -*-coding:utf8-*-
from typing import List
from io import BytesIO

import logging

from fastapi import APIRouter, UploadFile, Query
from fastapi.responses import JSONResponse, StreamingResponse
from starlette.status import HTTP_400_BAD_REQUEST

from app.core import pipeline

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/exercise")
async def getResult(
    *,
    personal_info: UploadFile | None = None,
    financial_info: UploadFile | None = None,
    countries_to_filter: List[str] = Query(default=[])
):
    """
    Insert/Update route prices to the database.
    """
    if not personal_info:
        content = {"message": "No personal_info file sent"}
        return JSONResponse(content, status_code=HTTP_400_BAD_REQUEST)
    elif not financial_info:
        content = {"message": "No financial_info file sent"}
        return JSONResponse(content, status_code=HTTP_400_BAD_REQUEST)
    else:
        try:
            result = pipeline(
                personal_info.file,  # type:ignore
                financial_info.file,  # type:ignore
                countries_to_filter=countries_to_filter,
            )
            stream = BytesIO()
            result.to_csv(stream, index=False)  # type:ignore
        except KeyError as e:
            return f"Fuck: {repr(e)}"
        except ValueError as e:
            return f"Fuck: {repr(e)}"
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            await personal_info.close()
            await financial_info.close()
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response
