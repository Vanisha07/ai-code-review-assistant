from fastapi import APIRouter

from app.schemas.read_repository import ReadRepositoryRequest
from app.services.code_reader import read_repository

router = APIRouter(
    prefix="/repository",
    tags=["Repository Reader"],
)


@router.post("/read")
def read_repo(request: ReadRepositoryRequest):

    code_files = read_repository(request.repository)

    return {
        "repository": request.repository,
        "total_files": len(code_files),
        "files": code_files,
    }