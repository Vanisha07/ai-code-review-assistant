from pydantic import BaseModel


class ReadRepositoryRequest(BaseModel):
    repository: str