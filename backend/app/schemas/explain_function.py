from pydantic import BaseModel


class ExplainFunctionRequest(BaseModel):
    repository: str
    function_name: str