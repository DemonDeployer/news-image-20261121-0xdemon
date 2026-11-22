#!/usr/bin/env python3
"""Publish the finished front page for the news-image-20261121 bounty.

The entry image (entry.png, 1024x1024) is rendered separately and stored
in this repository. This program only copies it into the directory the
grader provides, because the grading environment has no Pillow and no
fonts installed, so it cannot redraw the image itself. Copying a fixed
file is deterministic: every run writes the same bytes.

Usage:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"


def main() -> int:
    repo_dir = Path(__file__).resolve().parent
    source = repo_dir / SOURCE_NAME
    if not source.is_file():
        print(f"error: {SOURCE_NAME} not found next to main.py", file=sys.stderr)
        return 1
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, output_dir / SOURCE_NAME)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
