from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
REPOSITORY_FOLDER = BASE_DIR / "repositories"


def read_repository(repo_name: str):

    repo_path = REPOSITORY_FOLDER / repo_name

    print("Looking for repository at:", repo_path)

    if not repo_path.exists():
        raise FileNotFoundError("Repository not found.")
    
    code_files = []

    extensions = {
        ".py",
        ".java",
        ".cpp",
        ".c",
        ".h",
        ".hpp",
        ".js",
        ".ts",
        ".tsx",
        ".jsx",
        ".go",
        ".rs",
        ".php",
        ".html",
        ".css",
        ".md",
        ".json",
        ".yaml",
        ".yml",
        ".xml",
    }

    ignore_dirs = {
        ".git",
        "node_modules",
        "__pycache__",
        "venv",
        ".venv",
        "dist",
        "build",
    }

    for file in repo_path.rglob("*"):

        if file.is_dir():
            continue

        if any(part in ignore_dirs for part in file.parts):
            continue

        if file.suffix.lower() not in extensions:
            continue

        try:

            content = file.read_text(
                encoding="utf-8",
                errors="ignore",
            )

            code_files.append(
                {
                    "path": str(file.relative_to(repo_path)),
                    "content": content,
                }
            )

        except Exception:
            continue

    return code_files