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

    print("\n========== INDEX START ==========")

    print("Step 1: Reading repository...")
    files = read_repository(request.repository)
    print(f"Repository contains {len(files)} files")

    print("Step 2: Splitting documents...")
    chunks = split_documents(files)
    print(f"Created {len(chunks)} chunks")

    print("Step 3: Creating embeddings...")
    total = store_embeddings(
        request.repository,
        chunks,
    )

    print(f"Stored {total} embeddings")
    print("========== INDEX COMPLETE ==========\n")

    return {
        "repository": request.repository,
        "files": len(files),
        "chunks": len(chunks),
        "stored_embeddings": total,
    }