#!/usr/bin/env python3
"""Fail a publication-source audit if clear placeholders or AI boilerplate leak in.

This intentionally scans reader-facing Markdown only. Blank cells in appendices
are working templates, not unresolved publication placeholders.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "index.md",
    *sorted((ROOT / "manuscript").rglob("*.md")),
    *sorted((ROOT / "executive-summary").glob("*.md")),
]

CHECKS = {
    "unresolved bracket marker": re.compile(
        r"\[(?:TODO|TBD|TBC|XXX|FIXME|SOURCE|CASE|INSERT|ADD|CONFIRM|VERIFY|"
        r"PLACEHOLDER|TO BE ANNOUNCED)\b[^\]]*\]",
        re.IGNORECASE,
    ),
    "assistant boilerplate": re.compile(
        r"\b(?:as an ai|as a language model|i (?:cannot|can't|am unable to|’m unable to))\b",
        re.IGNORECASE,
    ),
    "filler text": re.compile(r"\blorem ipsum\b", re.IGNORECASE),
}


def main() -> int:
    findings: list[str] = []
    for path in FILES:
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), 1):
            for label, pattern in CHECKS.items():
                if pattern.search(line):
                    findings.append(f"{path.relative_to(ROOT)}:{line_no}: {label}: {line.strip()}")

    if findings:
        print("Publication audit failed:")
        print("\n".join(findings))
        return 1

    print(f"Publication audit: clean ({len(FILES)} reader-facing Markdown files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
