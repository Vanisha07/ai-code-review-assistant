from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import repository
from app.routers import file
from app.routers import read_repository
from app.routers import index_repository
from app.routers import function_search
from app.routers import search
from app.routers import review
from app.routers import explain_function
from app.routers import summary

app = FastAPI(
    title="AI Code Review Assistant API",
    version="1.0.0",
)

# Allow React frontend to access FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://ai-code-review-assistant-two-flame.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(repository.router)
app.include_router(file.router)
app.include_router(read_repository.router)
app.include_router(index_repository.router)
app.include_router(search.router)
app.include_router(function_search.router)
app.include_router(explain_function.router)
app.include_router(review.router)
app.include_router(summary.router)


@app.get("/")
def home():
    return {
        "message": "Backend Running 🚀"
    }