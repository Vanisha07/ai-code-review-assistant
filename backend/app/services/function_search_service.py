import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
REPOSITORY_FOLDER = BASE_DIR / "repositories"

LANGUAGE_MAP = {
    ".py": "Python",
    ".java": "Java",
    ".cpp": "C++",
    ".c": "C",
    ".h": "C Header",
    ".hpp": "C++ Header",
    ".js": "JavaScript",
    ".jsx": "React JSX",
    ".ts": "TypeScript",
    ".tsx": "React TSX",
    ".go": "Go",
    ".rs": "Rust",
    ".php": "PHP",
}


def extract_python_function(lines, start_index):
    """
    Extract a complete Python function using indentation.
    """

    function_lines = []

    base_indent = len(lines[start_index]) - len(lines[start_index].lstrip())

    for i in range(start_index, len(lines)):

        line = lines[i]

        current_indent = len(line) - len(line.lstrip())

        if (
            i > start_index
            and line.strip()
            and current_indent <= base_indent
            and (
                line.lstrip().startswith("def ")
                or line.lstrip().startswith("class ")
                or line.lstrip().startswith("async def ")
            )
        ):
            break

        function_lines.append(line)

    return "\n".join(function_lines)


def find_class_name(lines, start_index):
    """
    Find the class containing the function.
    """

    for i in range(start_index, -1, -1):

        line = lines[i].strip()

        if line.startswith("class "):
            return (
                line.split("(")[0]
                .replace("class", "")
                .replace(":", "")
                .strip()
            )

    return None


def search_function(repository: str, function_name: str):

    repo_path = REPOSITORY_FOLDER / repository

    if not repo_path.exists():
        raise FileNotFoundError("Repository not found.")

    results = []

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
    }

    ignore_dirs = {
        ".git",
        "__pycache__",
        "venv",
        ".venv",
        "node_modules",
        "dist",
        "build",
    }

    patterns = [
        # Python
        rf"^\s*(?:async\s+)?def\s+{re.escape(function_name)}\s*\(",

        # JavaScript / TypeScript
        rf"^\s*function\s+{re.escape(function_name)}\s*\(",
        rf"^\s*(?:export\s+)?(?:const|let|var)\s+{re.escape(function_name)}\s*=\s*(?:async\s*)?\(",

        # Java / C++ / Go / Rust / PHP
        rf"^\s*(?:public|private|protected|static|final|virtual|inline|constexpr|extern|friend|export|\s)*[\w:<>\[\],*&]+\s+{re.escape(function_name)}\s*\(",
    ]

    for file in repo_path.rglob("*"):

        if file.is_dir():
            continue

        if any(part in ignore_dirs for part in file.parts):
            continue

        if file.suffix.lower() not in extensions:
            continue

        try:

            lines = file.read_text(
                encoding="utf-8",
                errors="ignore",
            ).splitlines()

            for line_number, line in enumerate(lines, start=1):

                for pattern in patterns:

                    if re.search(pattern, line):

                        code = ""
                        class_name = None

                        if file.suffix == ".py":
                            code = extract_python_function(
                                lines,
                                line_number - 1,
                            )

                            class_name = find_class_name(
                                lines,
                                line_number - 1,
                            )

                        results.append(
                            {
                                "file": str(file.relative_to(repo_path)),
                                "line": line_number,
                                "class": class_name,
                                "signature": code.split("):")[0] + "):" if code else line.strip(),
                                "language": LANGUAGE_MAP.get(
                                    file.suffix,
                                    "Unknown",
                                ),
                                "code": code,
                            }
                        )

                        break

        except Exception:
            continue

    results.sort(
        key=lambda x: (
            x["file"],
            x["line"],
        )
    )

    return results