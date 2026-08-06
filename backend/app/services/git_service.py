import os
from git import Repo

REPOSITORY_FOLDER = "repositories"


def clone_repository(repo_url: str):

    repo_name = repo_url.split("/")[-1].replace(".git", "")
    local_path = os.path.join(REPOSITORY_FOLDER, repo_name)

    if os.path.exists(local_path):
        return {
            "status": "already_exists",
            "repository": repo_name,
            "path": local_path,
        }

    Repo.clone_from(repo_url, local_path)

    return {
        "status": "success",
        "repository": repo_name,
        "path": local_path,
    }