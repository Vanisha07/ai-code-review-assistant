from pydantic import BaseModel, HttpUrl


class CloneRepositoryRequest(BaseModel):
    url: HttpUrl