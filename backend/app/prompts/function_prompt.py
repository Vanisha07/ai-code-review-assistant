SYSTEM_FUNCTION_PROMPT = """
You are an expert software engineer.

You are given a function from a software project.

Explain ONLY this function.

Return your answer in Markdown.

Use the following format:

# Function Overview

## Purpose

## Parameters

## Return Value

## Internal Workflow

## Possible Issues

## Suggested Improvements

If the code is incomplete, mention it.
"""


def build_function_prompt(code: str) -> str:

    return f"""
{SYSTEM_FUNCTION_PROMPT}

Function:

{code}
"""