#!/usr/bin/env python3
"""Embed figures at their prose references (idempotent).

The Editor's chapter files never carry embed directives (prose references
are the Editor's layer; embeds are the Developer's). After any content
re-import, run `make embed-figures` to (re)apply the full manifest.

Placement rule: directly after the first paragraph containing the
"Figure X.Y" reference (whitespace-normalized). Special modes:
  after-quote  — after the blockquote containing the reference (floats
                 cannot live inside panel boxes)
  heading      — after the intro paragraph of the anchor heading (used
                 when prose lacks a reference — flagged to the Editor)
  append       — at the end of the file (front-matter frontispiece)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

M = "manuscript"
FIGS = [
    # (file, anchor, svg, caption, mode)
    (f"{M}/part1-landscape/ch01-customs-mandate.md", "Figure 1.1",
     "fig-ch01-arithmetic", "Figure 1.1 — The Arithmetic", "ref"),
    (f"{M}/part1-landscape/ch01-customs-mandate.md", "Figure 1.2",
     "fig-ch01-adoption-funnel", "Figure 1.2 — The Adoption Funnel", "ref"),
    (f"{M}/part1-landscape/ch01-customs-mandate.md",
     "Three commitments run through",
     "fig-three-pillars", "The Stance", "ref"),
    (f"{M}/part1-landscape/ch02-from-rules-to-agents.md", "Figure 2.1",
     "fig-ch02-autonomy-ladder", "Figure 2.1 — The Autonomy Ladder", "ref"),
    (f"{M}/part1-landscape/ch02-from-rules-to-agents.md", "Figure 2.2",
     "fig-ch02-four-eras", "Figure 2.2 — Four Eras in One Page", "ref"),
    (f"{M}/part1-landscape/ch03-genai-first.md", "Figure 3.1",
     "fig-ch03-maturity-ladder", "Figure 3.1 — The Maturity Ladder", "ref"),
    (f"{M}/part1-landscape/ch03-genai-first.md", "Figure 3.2",
     "fig-ch03-deployment-tree", "Figure 3.2 — Deployment Decision Tree", "ref"),
    (f"{M}/part1-landscape/ch03-genai-first.md", "Figure 3.3",
     "fig-ch03-quick-wins", "Figure 3.3 — The Quick-Wins Catalog", "ref"),
    (f"{M}/part1-landscape/ch04-opportunity-map.md", "Figure 4.1",
     "fig-ch04-opportunity-map", "Figure 4.1 — The Agentic Opportunity Map", "ref"),
    (f"{M}/part2-business-case/ch05-value-economics.md", "Figure 5.1",
     "fig-ch05-value-board", "Figure 5.1 — The Verified Value Board", "ref"),
    (f"{M}/part2-business-case/ch06-readiness-assessment.md", "Figure 6.1",
     "fig-ch06-readiness-profile", "Figure 6.1 — The Readiness Profile", "ref"),
    (f"{M}/part2-business-case/ch07-build-buy-partner.md", "Figure 7.1",
     "fig-ch07-judgment-boundary", "Figure 7.1 — The Judgment Boundary", "ref"),
    (f"{M}/part3-governance/ch08-regulatory-landscape.md", "Figure 8.1",
     "fig-ch08-three-layers", "Figure 8.1 — The Three Regulatory Layers", "ref"),
    (f"{M}/part3-governance/ch08-regulatory-landscape.md", "Figure 8.2",
     "fig-ch08-eu-ai-act-timeline", "Figure 8.2 — The EU AI Act Timeline", "ref"),
    (f"{M}/part3-governance/ch09-responsible-ai.md", "Figure 9.1",
     "fig-ch09-oversight-selector", "Figure 9.1 — Oversight Architecture Selector", "ref"),
    (f"{M}/part3-governance/ch09-responsible-ai.md", "Figure 9.2",
     "fig-ch09-autonomy-agency", "Figure 9.2 — Autonomy × Agency", "ref"),
    (f"{M}/part3-governance/ch10-security-agentic.md", "Figure 10.1",
     "fig-ch10-two-channels", "Figure 10.1 — Two Channels, One Boundary", "ref"),
    (f"{M}/part3-governance/ch10-security-agentic.md", "Figure 10.2",
     "fig-ch10-injection-curve", "Figure 10.2 — The 1 / 10 / 100 Number", "ref"),
    (f"{M}/part3-governance/ch11-data-foundations.md", "Figure 11.1",
     "fig-ch11-entity-network", "Figure 11.1 — From Filings to a Network", "after-quote"),
    (f"{M}/part4-execution/ch12-pilot-playbook.md", "Figure 12.1",
     "fig-ch12-pilot-stages", "Figure 12.1 — Piloting in Stages", "ref"),
    (f"{M}/part4-execution/ch14-people-organization.md", "Figure 14.1",
     "fig-ch14-hub-and-spoke", "Figure 14.1 — Hub and Spoke", "ref"),
    (f"{M}/part5-horizon/ch15-case-studies.md", "Figure 15.1",
     "fig-ch15-case-comparison", "Figure 15.1 — Case Studies at a Glance", "ref"),
    (f"{M}/part5-horizon/ch16-road-ahead.md", "Figure 16.1",
     "fig-ch16-agent-to-agent", "Figure 16.1 — Agent to Agent, Across the Border", "ref"),
    (f"{M}/part5-horizon/ch16-road-ahead.md",
     "Chapter 1 opened this book with three commitments",
     "fig-three-pillars", "The Stance", "ref"),
    (f"{M}/appendices/appendix-c-scorecard.md", "Figure C.1",
     "fig-appc-scorecard-weights", "Figure C.1 — The Vendor Scorecard", "ref"),
    (f"{M}/00-front-matter/how-to-read.md", None,
     "fig-book-map", "Map of the Book", "append"),
]


def embed_line(svg, caption):
    # Diagrams are visual exhibits, not full-page slide reproductions.
    # Capping height lets a figure share a spread with its interpretation
    # instead of stranding a large blank lower half of a page.
    return f"![{caption}](/assets/diagrams/{svg}.svg){{width=100% height=75%}}"


def main():
    problems = 0
    for path, anchor, svg, caption, mode in FIGS:
        p = ROOT / path
        text = p.read_text(encoding="utf-8")
        emb = embed_line(svg, caption)
        if emb in text:
            continue
        paras = text.split("\n\n")
        if mode == "append":
            paras.append(emb)
        else:
            pat = re.escape(anchor).replace(r"\ ", r"\s+")
            hits = [i for i, para in enumerate(paras)
                    if re.search(pat, para) and "![" not in para]
            if not hits:
                print(f"MISSING ANCHOR: {anchor!r} in {path}")
                problems += 1
                continue
            i = hits[0]
            if mode == "after-quote":
                while i + 1 < len(paras) and paras[i + 1].lstrip().startswith(">"):
                    i += 1
            paras.insert(i + 1, emb)
        p.write_text("\n\n".join(paras), encoding="utf-8")
        print(f"embedded {svg} in {Path(path).name}")
    if problems:
        print(f"\n{problems} anchor problem(s).")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
