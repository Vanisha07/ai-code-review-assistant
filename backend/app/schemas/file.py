from pydantic import BaseModel


class RepositoryFilesRequest(BaseModel):
    repository: str