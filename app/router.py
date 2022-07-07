# -*-coding:utf8-*-
from typing import List
from io import BytesIO

import logging

from fastapi import APIRouter, UploadFile, Query
from fastapi.responses import JSONResponse, StreamingResponse
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from app.core import pipeline

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/marketing_push_targets")
async def return_targets(
    personal_info: UploadFile | None = None,
    financial_info: UploadFile | None = None,
    countries_to_filter: List[str] = Query(default=[]),
) -> JSONResponse | StreamingResponse:
    """
    Returns targets for a marketing campaing, which are the result of an inner join between personal info dataset
    and financial info dataset with an optional country filter.
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
        except FileNotFoundError:
            content = {"message": "Upload file not found"}
            return JSONResponse(content, status_code=HTTP_400_BAD_REQUEST)
        except ValueError as e:
            content = {"message": repr(e)}
            return JSONResponse(content, status_code=HTTP_400_BAD_REQUEST)
        except Exception:
            content = {"message": "There was an error processing the file"}
            return JSONResponse(content, status_code=HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            await personal_info.close()
            await financial_info.close()
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response
