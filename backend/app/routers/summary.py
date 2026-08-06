from fastapi import APIRouter

from app.schemas.summary import SummaryRequest
from app.services.summary_service import generate_summary

router = APIRouter(
    prefix="/repository",
    tags=["Repository Summary"],
)


@router.post("/summary")
def summary(request: SummaryRequest):

    result = generate_summary(
        request.repository,
    )

    return {
        "repository": request.repository,
        "summary": result,
    }