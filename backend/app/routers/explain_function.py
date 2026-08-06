from fastapi import APIRouter

from app.schemas.explain_function import ExplainFunctionRequest
from app.services.function_ai_service import explain_function

router = APIRouter(
    prefix="/repository",
    tags=["Function AI"],
)


@router.post("/explain-function")
def explain(request: ExplainFunctionRequest):

    return explain_function(
        request.repository,
        request.function_name,
    )