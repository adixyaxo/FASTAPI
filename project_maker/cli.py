import argparse
from pathlib import Path

from project_maker.structure import (
    PROJECT_STRUCTURE,
    create_structure,
)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "name",
        help="Project name"
    )

    args = parser.parse_args()

    root = Path(args.name)

    root.mkdir(exist_ok=True)

    create_structure(root, PROJECT_STRUCTURE)
    print(f"📂 Location: {root.resolve()}")
    print(f"Created {args.name}")
