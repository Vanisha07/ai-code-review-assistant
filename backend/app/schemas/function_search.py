from pydantic import BaseModel


class FunctionSearchRequest(BaseModel):
    repository: str
    function_name: str