#!/usr/bin/env python3
"""Footnote refs/defs integrity check across the manuscript.

For every manuscript file (and index.md), compares footnote references
(`[^label]`) with definitions (`[^label]: ...`):

  * defined but never referenced — pandoc drops the note SILENTLY from
    the rendered book (only a build-log warning), losing its citations
  * referenced but never defined — pandoc renders the marker literally

Both directions are defects (`make check-notes`); exit code is non-zero
when anything is found. CI runs this as a warning step.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REF = re.compile(r"\[\^([^\]\s]+)\]")
DEF = re.compile(r"^\s*\[\^([^\]\s]+)\]:", re.MULTILINE)


def manuscript_files():
    index = ROOT / "index.md"
    if index.exists():
        yield index
    yield from sorted((ROOT / "manuscript").rglob("*.md"))


def main():
    problems = 0
    for path in manuscript_files():
        text = path.read_text(encoding="utf-8")
        def_labels = DEF.findall(text)
        defs = set(def_labels)
        def_counts = {label: def_labels.count(label) for label in defs}
        # Remove definition markers before collecting references. A citation
        # followed by ordinary prose punctuation (for example "[^id]:") is
        # still a reference unless it begins a line.
        refs = set(REF.findall(DEF.sub("", text)))
        rel = path.relative_to(ROOT)
        for label in sorted(defs - refs):
            print(f"{rel}: [^{label}] defined but never referenced "
                  f"(note will be silently dropped)")
            problems += 1
        for label in sorted(refs - defs):
            print(f"{rel}: [^{label}] referenced but never defined "
                  f"(marker renders literally)")
            problems += 1
        for label in sorted(label for label, count in def_counts.items() if count > 1):
            print(f"{rel}: [^{label}] defined {def_counts[label]} times "
                  f"(Pandoc keeps only one definition)")
            problems += 1
    if problems:
        print(f"\n{problems} footnote integrity problem(s).")
        return 1
    print("Footnote refs/defs integrity: clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
