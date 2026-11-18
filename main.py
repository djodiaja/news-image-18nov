"""make.fun news-image-20261118 bounty entry.

Deterministic image-copy approach: the repository ships a pre-rendered news
infographic for 18 November 2026 as ``entry.png``. Rather than generating the
image at runtime (which would introduce non-determinism from models, fonts,
or network calls), this script simply copies that fixed file to the requested
output path. The same input always yields a byte-identical output.
"""

import os
import shutil
from pathlib import Path


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / "entry.png"
    shutil.copy2(src, output_dir / "entry.png")


if __name__ == "__main__":
    main()
