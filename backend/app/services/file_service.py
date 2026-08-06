from pathlib import Path

# Folders we never want to scan
IGNORE_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    "venv",
    ".venv",
    "dist",
    "build",
    ".idea",
    ".vscode",
}


BASE_DIR = Path(__file__).resolve().parent.parent.parent
REPOSITORY_FOLDER = BASE_DIR / "repositories"


def get_repository_files(repo_name: str):
    """
    Returns a list of all files inside a repository.
    """

    repo_path = REPOSITORY_FOLDER / repo_name

    if not repo_path.exists():
        raise FileNotFoundError(f"Repository '{repo_name}' not found.")

    files = []

    for path in repo_path.rglob("*"):

        if path.is_dir():
            continue

        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        files.append(str(path.relative_to(repo_path)))

    return files