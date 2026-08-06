from pathlib import Path
from git import Repo

BASE_DIR = Path(__file__).resolve().parents[2]
REPOSITORY_FOLDER = BASE_DIR / "repositories"

# Ensure the folder exists
REPOSITORY_FOLDER.mkdir(parents=True, exist_ok=True)


def clone_repository(repo_url: str):

    repo_name = repo_url.split("/")[-1].replace(".git", "")
    local_path = REPOSITORY_FOLDER / repo_name

    if local_path.exists():
        return {
            "status": "already_exists",
            "repository": repo_name,
            "path": str(local_path),
        }

    Repo.clone_from(repo_url, str(local_path))

    return {
        "status": "success",
        "repository": repo_name,
        "path": str(local_path),
    }