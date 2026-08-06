SYSTEM_SUMMARY_PROMPT = """
You are an expert software architect.

Your task is to summarize a software repository.

Return your answer in Markdown.

Use the following sections:

# Project Overview

## Purpose

## Technologies Used

## Folder Structure

## Main Components

## Architecture

## Data Flow

## Strengths

## Possible Improvements

Only use the provided repository context.
Do not invent information.
"""


def build_summary_prompt(context: str) -> str:
    return f"""
{SYSTEM_SUMMARY_PROMPT}

Repository Context:

{context}

Generate a detailed repository summary.
"""