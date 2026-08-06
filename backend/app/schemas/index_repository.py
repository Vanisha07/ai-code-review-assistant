from pydantic import BaseModel


class IndexRepositoryRequest(BaseModel):
    repository: str