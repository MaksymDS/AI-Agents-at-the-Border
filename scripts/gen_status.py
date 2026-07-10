#!/usr/bin/env python3
"""Regenerate STATUS.md from manuscript front matter.

Reads the YAML header (title, part, chapter, status, version,
last-updated) of every file under manuscript/ plus index.md and writes
the chapter-status table to STATUS.md. Run via `make status`.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "STATUS.md"

FIELD = re.compile(r"^([A-Za-z-]+):\s*(.*)$")


def front_matter(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fm = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = FIELD.match(line)
        if m:
            fm[m.group(1).lower()] = m.group(2).strip().strip('"')
    return fm


def title_fallback(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return re.sub(r"\s*\{[^}]*\}\s*$", "", line[2:]).strip()
    return path.stem


def collect():
    rows = []
    files = sorted((ROOT / "manuscript").rglob("*.md"))
    if (ROOT / "index.md").exists():
        files.insert(0, ROOT / "index.md")
    for path in files:
        fm = front_matter(path)
        rel = path.relative_to(ROOT)
        title = fm.get("title") or title_fallback(path)
        chapter = fm.get("chapter", "")
        if not chapter:
            m = re.match(r"ch(\d+)", path.stem)
            if m:
                chapter = str(int(m.group(1)))
            elif "appendix" in path.stem:
                chapter = path.stem.split("-")[1].upper()
            else:
                chapter = "—"
        rows.append({
            "chapter": chapter,
            "title": title,
            "part": fm.get("part", ""),
            "status": fm.get("status", "unknown"),
            "version": fm.get("version", ""),
            "updated": fm.get("last-updated", ""),
            "file": str(rel),
        })
    return rows


def sort_key(row):
    ch = row["chapter"]
    if ch.isdigit():
        return (1, int(ch), "")
    if ch == "—":
        return (0, 0, row["file"])
    return (2, 0, ch)  # appendices


def main():
    rows = sorted(collect(), key=sort_key)
    lines = [
        "# STATUS",
        "",
        "Chapter status overview, generated from front matter by",
        "`scripts/gen_status.py` (`make status`). Do not edit by hand.",
        "",
        "Lifecycle: outline → draft → review → final (see CONTRIBUTING.md).",
        "",
        "| Ch. | Title | Part | Status | Version | Last updated |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| {r['chapter']} | [{r['title']}]({r['file']}) | {r['part']} "
            f"| `{r['status']}` | {r['version']} | {r['updated']} |"
        )
    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    summary = ", ".join(f"{v} {k}" for k, v in sorted(counts.items()))
    lines += ["", f"**Totals:** {summary}.", ""]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(rows)} entries: {summary})")


if __name__ == "__main__":
    main()
