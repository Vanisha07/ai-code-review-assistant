from fastapi import APIRouter

from app.schemas.search import SearchRequest
from app.services.search_service import search_repository

router = APIRouter(
    prefix="/repository",
    tags=["Repository Search"],
)


@router.post("/search")
def search(request: SearchRequest):

    results = search_repository(
        request.repository,
        request.query,
    )

    return {
        "repository": request.repository,
        "query": request.query,
        "results": results,
    }