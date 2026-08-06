from app.prompts.review_prompt import build_prompt
from app.services.llm_service import generate_response


def review_code(question: str, code_chunks):

    context = ""

    for chunk in code_chunks:
        context += f"""
File: {chunk["path"]}

{chunk["content"]}

-------------------------
"""

    prompt = build_prompt(
    question=question,
    context=context,
    )

    return generate_response(prompt)