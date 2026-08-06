from fastapi import APIRouter

from app.schemas.index_repository import IndexRepositoryRequest
from app.services.code_reader import read_repository
from app.services.chunker import split_documents
from app.services.embedding_service import store_embeddings

router = APIRouter(
    prefix="/repository",
    tags=["Repository Index"],
)


@router.post("/index")
def index_repository(request: IndexRepositoryRequest):

    files = read_repository(request.repository)
    print("FILES:", len(files))
    print(files[:2])
    chunks = split_documents(files)
    print("CHUNKS:", len(chunks))
    print(chunks[:2])
    total = store_embeddings(
        request.repository,
        chunks,
    )

    return {
        "repository": request.repository,
        "files": len(files),
        "chunks": len(chunks),
        "stored_embeddings": total,
    }