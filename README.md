# AI Agents at the Border

*An Executive Guide to Trustworthy AI in Trade and Customs* is a
decision-oriented book for leaders of customs, border and trade
administrations deploying generative and agentic AI.

Read the current edition at [era-society.ae](https://era-society.ae),
or download the versioned PDF and EPUB from [`deliverables/`](deliverables/).

## What this repository is for

This is the public source and evidence repository for the book. It is the
place to suggest factual corrections, submit evidence-backed cases, report
legal developments and improve the reader experience. The working build
repository remains separate; this repository contains only publication-safe
material.

The current public edition is **v1.5.2**, legally cut off on **10 July
2026**. It is a management guide, not legal advice.

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
make deliverable BOOK_VERSION=v1.5.2
make deliverable-epub BOOK_VERSION=v1.5.2
```

Before a pull request, run:

```bash
make audit-publication
make check-bib
make check-notes
```

## Rights and contribution terms

The publication licence is intentionally not finalised while the publication
route is decided. The text, design and assets remain © Maksym Nechepurenko.
Public availability of this repository is an invitation to review and propose
improvements; it is not a grant to republish the book commercially or create
unapproved editions. By submitting a contribution, you grant the author the
right to edit, incorporate and publish that contribution with attribution
where appropriate. See [RIGHTS.md](RIGHTS.md).
