#!/usr/bin/env python3
"""Rasterise reader diagrams for a Kindle-safe EPUB without changing source art."""

from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "diagrams"
TARGET = ROOT / "assets" / "kindle" / "diagrams"


def main() -> None:
    TARGET.mkdir(parents=True, exist_ok=True)
    for source in sorted(SOURCE.glob("*.svg")):
        subprocess.run(
            ["rsvg-convert", "-w", "1800", "-f", "png", "-o", str(TARGET / f"{source.stem}.png"), str(source)],
            check=True,
        )


if __name__ == "__main__":
    main()
