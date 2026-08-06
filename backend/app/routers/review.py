from fastapi import APIRouter

from app.schemas.review import ReviewRequest
from app.services.search_service import search_repository
from app.services.ai_review_service import review_code

router = APIRouter(
    prefix="/repository",
    tags=["AI Review"],
)


@router.post("/review")
def review(request: ReviewRequest):

    chunks = search_repository(
        request.repository,
        request.question,
        n_results=8,
    )

    answer = review_code(
        request.question,
        chunks,
    )

    return {
        "repository": request.repository,
        "question": request.question,
        "answer": answer,
    }