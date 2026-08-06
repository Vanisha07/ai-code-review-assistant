from fastapi import APIRouter

from app.schemas.repository import CloneRepositoryRequest
from app.services.git_service import clone_repository

router = APIRouter(prefix="/repository", tags=["Repository"])


@router.post("/clone")
def clone_repo(request: CloneRepositoryRequest):
    return clone_repository(str(request.url))