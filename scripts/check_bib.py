#!/usr/bin/env python3
"""Cross-check bib keys referenced in manuscript comments against sources.bib.

Chapters reference sources via HTML comments near their endnotes:

    <!-- bib: key_one, key_two -->

This script reports:
  * keys referenced in manuscript/ (and index.md) but missing from
    research/sources.bib
  * keys defined in research/sources.bib but never referenced

Exit code is non-zero only for missing keys (unreferenced entries are
informational: the bibliography may legitimately run ahead of the text).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIB = ROOT / "research" / "sources.bib"

BIB_COMMENT = re.compile(r"<!--\s*bib:\s*([^>]*?)-->")
BIB_ENTRY = re.compile(r"^@\w+\{([^,\s]+)\s*,", re.MULTILINE)


def manuscript_files():
    index = ROOT / "index.md"
    if index.exists():
        yield index
    yield from sorted((ROOT / "manuscript").rglob("*.md"))


def main():
    referenced = {}  # key -> [files]
    for path in manuscript_files():
        text = path.read_text(encoding="utf-8")
        for match in BIB_COMMENT.finditer(text):
            for key in re.split(r"[,\s]+", match.group(1).strip()):
                if key:
                    referenced.setdefault(key, []).append(
                        str(path.relative_to(ROOT))
                    )

    defined = set(BIB_ENTRY.findall(BIB.read_text(encoding="utf-8")))

    missing = {k: v for k, v in referenced.items() if k not in defined}
    unreferenced = sorted(defined - set(referenced))

    print(f"bib keys referenced in manuscript: {len(referenced)}")
    print(f"bib entries defined in {BIB.relative_to(ROOT)}: {len(defined)}")

    if missing:
        print(f"\nMISSING from sources.bib ({len(missing)}):")
        for key in sorted(missing):
            print(f"  {key}  <- {', '.join(sorted(set(missing[key])))}")
    else:
        print("\nAll referenced keys are present in sources.bib.")

    if unreferenced:
        print(f"\nDefined but never referenced ({len(unreferenced)}):")
        for key in unreferenced:
            print(f"  {key}")

    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
