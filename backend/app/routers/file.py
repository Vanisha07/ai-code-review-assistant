from fastapi import APIRouter

from app.schemas.file import RepositoryFilesRequest
from app.services.file_service import get_repository_files

router = APIRouter(
    prefix="/repository",
    tags=["Repository Explorer"],
)


@router.post("/files")
def repository_files(request: RepositoryFilesRequest):

    files = get_repository_files(request.repository)

    return {
        "repository": request.repository,
        "total_files": len(files),
        "files": files,
    }