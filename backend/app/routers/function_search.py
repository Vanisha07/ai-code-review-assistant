from fastapi import APIRouter

from app.schemas.function_search import FunctionSearchRequest
from app.services.function_search_service import search_function

router = APIRouter(
    prefix="/repository",
    tags=["Function Search"],
)


@router.post("/function")
def find_function(request: FunctionSearchRequest):

    results = search_function(
        request.repository,
        request.function_name,
    )

    return {
        "repository": request.repository,
        "function": request.function_name,
        "matches": results,
    }