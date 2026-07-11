# AI Agents at the Border

*An Executive Guide to Trustworthy AI in Trade and Customs* is a
decision-oriented book for leaders of customs, border and trade
administrations deploying generative and agentic AI.

Read the current edition at [era-society.ae](https://www.era-society.ae),
or download the full PDF, the 60-page Executive Decision Brief, and the full EPUB
from [`deliverables/`](deliverables/).

## What this repository is for

This is the public source and evidence repository for the book. It is the
place to suggest factual corrections, submit evidence-backed cases, report
legal developments and improve the reader experience. The working build
repository remains separate; this repository contains only publication-safe
material.

The current public edition is **v1.9.3**, legally cut off on **10 July
2026**. It is a management guide, not legal advice.

Paperback ISBN: **9798186760252** · Imprint: **Independently published**.

Version 1.9.3 adds the ISBN, imprint and formal copyright-verso without
altering the manuscript or legal baseline. Version 1.9.2 gives the third
Stance-card label additional right-side safety padding across every reader
format. Version 1.9.1 retains the dedicated executive visual system
and corrects the intrinsic fit of the third Stance card plus the spacing
before the final board question. Version 1.9.0 introduced full-page
ladder and case figures, decision-evidence-stop strips, value, 90-day and
board-dashboard infographics, writable approval grids, and five visual
operating rules. Figures retain their native proportions and the 60-page
print signature contains no inserted blanks. The regulatory cut-off is now
visible on both title pages and at each regulatory entry point; the online
[regulatory watch record](https://www.era-society.ae/read/regulatory-reference)
provides the dated baseline and public update route. See
[`VERSION-LOG.md`](VERSION-LOG.md) and the review
[`disposition record`](reviews/2026-07-10-critical-review-disposition.md).

## Contribute

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or
pull request. Every factual addition needs a source, publication date,
jurisdiction where relevant, and an attribution label. The book deliberately
does not turn digitalisation claims into AI claims.

- Report a correction or legal update through GitHub Issues.
- Propose a case or evidence improvement through a pull request.
- Use the website's private feedback form for editorial comments or to
  contact the author without creating a public discussion.

## Build locally

The canonical print build is the 6 × 9 inch PDF. With Quarto, LuaLaTeX and
the SVG renderer installed:

```bash
make deliverable BOOK_VERSION=v1.9.3
make deliverable-executive BOOK_VERSION=v1.9.3
make deliverable-epub BOOK_VERSION=v1.9.3
```

Before a pull request, run:

```bash
make audit-publication
make check-bib
make check-notes
```

## Rights and contribution terms

*AI Agents at the Border* is licensed under [Creative Commons Attribution 4.0
International](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).
You may share and adapt the book, including commercially, provided that you
give appropriate credit, link to the licence and indicate changes. See
[LICENSE](LICENSE) and [RIGHTS.md](RIGHTS.md) for the preferred attribution
and treatment of third-party material.
