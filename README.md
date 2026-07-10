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

The current public edition is **v1.7.1**, legally cut off on **10 July
2026**. It is a management guide, not legal advice.

Version 1.7.1 makes the Executive Decision Brief operationally
self-contained. Its Eight Decisions are now a dependency chain: operating
constraint, task/baseline, autonomy/agency, and sovereignty must be complete
before value, sourcing, right-to-operate, or renewal decisions. Five
one-page Core Tools cover the mandate, metrics, regulatory applicability,
RFP decision rights, and pilot gate. The agency section now contrasts an L2
copilot with broad estate credentials against an L3 one-case, allowlisted,
read-only agent. The full book remains the depth reference; the brief is
sufficient to begin the work. See
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
make deliverable BOOK_VERSION=v1.7.1
make deliverable-executive BOOK_VERSION=v1.7.1
make deliverable-epub BOOK_VERSION=v1.7.1
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
