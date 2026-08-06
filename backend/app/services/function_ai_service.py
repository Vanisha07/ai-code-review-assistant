from app.prompts.function_prompt import build_function_prompt
from app.services.function_search_service import search_function
from app.services.llm_service import generate_response


def explain_function(repository: str, function_name: str):

    matches = search_function(
        repository,
        function_name,
    )

    if not matches:
        return {
            "error": "Function not found."
        }

    function = matches[0]

    prompt = build_function_prompt(
        function["code"]
    )

    explanation = generate_response(prompt)

    return {
        "file": function["file"],
        "class": function["class"],
        "line": function["line"],
        "signature": function["signature"],
        "language": function["language"],
        "code": function["code"],
        "explanation": explanation,
    }