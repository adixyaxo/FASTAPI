from pathlib import Path

# -----------------------------
# Project Structure Definition
# -----------------------------
PROJECT_STRUCTURE = {
    ".env": None,
    ".gitignore": None,
    "requirements.txt": None,
    "README.md": None,
    "main.py": None,
    "index.py": None,

    "src": {
        "__init__.py": None,

        "auth": {
            "__init__.py": None,
            "controller.py": None,
            "service.py": None,
            "repository.py": None,
            "router.py": None,
            "schemas.py": None,
            "models.py": None,
            "jwt.py": None,
            "password.py": None,
        },

        "users": {
            "__init__.py": None,
            "controller.py": None,
            "service.py": None,
            "repository.py": None,
            "router.py": None,
            "schemas.py": None,
            "models.py": None,
        },

        "tasks": {
            "__init__.py": None,
            "controller.py": None,
            "service.py": None,
            "repository.py": None,
            "router.py": None,
            "schemas.py": None,
            "models.py": None,
        },

        "routes": {
            "__init__.py": None,
            "api.py": None,
            "web.py": None,
        },

        "models": {
            "__init__.py": None,
            "base.py": None,
            "mixins.py": None,
        },

        "schemas": {
            "__init__.py": None,
            "common.py": None,
            "response.py": None,
        },

        "config": {
            "__init__.py": None,
            "database.py": None,
            "settings.py": None,
            "security.py": None,
            "logging.py": None,
            "environment.py": None,
        },

        "exceptions": {
            "__init__.py": None,
            "handlers.py": None,
            "custom.py": None,
        },

        "middlewares": {
            "__init__.py": None,
            "auth.py": None,
            "cors.py": None,
            "logging.py": None,
        },

        "services": {
            "__init__.py": None,
            "email.py": None,
            "notification.py": None,
        },

        "repositories": {
            "__init__.py": None,
            "base.py": None,
        },

        "utils": {
            "__init__.py": None,
            "helpers.py": None,
            "validators.py": None,
            "constants.py": None,
            "logger.py": None,
            "pagination.py": None,
        },
    },

    "migrations": {
        "versions": {},
        "env.py": None,
        "script.py.mako": None,
        "README": None,
    },

    "templates": {
        "base.html": None,
        "index.html": None,
        "login.html": None,
        "dashboard.html": None,

        "errors": {
            "404.html": None,
            "500.html": None,
        },
    },

    "static": {
        "css": {"style.css": None},
        "js": {"script.js": None},
        "images": {},
        "uploads": {},
    },

    "tests": {
        "__init__.py": None,
        "conftest.py": None,

        "unit": {
            "test_users.py": None,
            "test_tasks.py": None,
            "test_auth.py": None,
        },

        "integration": {
            "test_api.py": None,
            "test_database.py": None,
        },
    },

    "docs": {
        "api.md": None,
        "architecture.md": None,
        "deployment.md": None,
    },
}


# -----------------------------
# Recursive Creator
# -----------------------------
def create_structure(base_path: Path, structure: dict):
    for name, content in structure.items():
        current = base_path / name

        if content is None:
            current.parent.mkdir(parents=True, exist_ok=True)
            current.touch(exist_ok=True)
            print(f"📄 {current}")

        elif isinstance(content, dict):
            current.mkdir(parents=True, exist_ok=True)
            print(f"📁 {current}")
            create_structure(current, content)


# -----------------------------
# Main
# -----------------------------
def main():
    project_name = input("Project Name: ").strip()

    if not project_name:
        print("Project name cannot be empty.")
        return

    root = Path(project_name)
    root.mkdir(exist_ok=True)

    create_structure(root, PROJECT_STRUCTURE)

    print("\n🎉 Project created successfully!")
    print(f"📂 Location: {root.resolve()}")


if __name__ == "__main__":
    main()