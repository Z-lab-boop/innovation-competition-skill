#!/usr/bin/env python3
"""Initialize a non-destructive innovation-competition workspace."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "assets" / "workspace"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy competition workspace templates without overwriting files."
    )
    parser.add_argument("target", type=Path, help="Target project directory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    templates = sorted(path for path in TEMPLATE_DIR.iterdir() if path.is_file())
    if not templates:
        raise SystemExit(f"No templates found in {TEMPLATE_DIR}")

    target = args.target.expanduser().resolve()
    conflicts = [target / path.name for path in templates if (target / path.name).exists()]
    if conflicts:
        joined = "\n".join(f"- {path}" for path in conflicts)
        raise SystemExit(f"Refusing to overwrite existing files:\n{joined}")

    target.mkdir(parents=True, exist_ok=True)
    for template in templates:
        shutil.copy2(template, target / template.name)

    print(f"Created {len(templates)} workspace files in {target}")
    for template in templates:
        print(f"- {template.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
