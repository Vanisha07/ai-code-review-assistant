from app.prompts.summary_prompt import build_summary_prompt
from app.services.search_service import search_repository
from app.services.llm_service import generate_response


def generate_summary(repository: str):

    chunks = search_repository(
        repository=repository,
        query="Explain the complete architecture of this repository",
        n_results=15,
    )

    context = ""

    for chunk in chunks:
        context += f"""
File: {chunk["path"]}

{chunk["content"]}

----------------------------------
"""

    prompt = build_summary_prompt(context)

    return generate_response(prompt)