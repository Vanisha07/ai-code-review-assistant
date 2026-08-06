from pydantic import BaseModel


class ReviewRequest(BaseModel):
    repository: str
    question: str