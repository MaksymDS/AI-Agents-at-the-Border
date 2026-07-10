# Version Log

This file records reader-facing releases. Git commits and annotated
release tags are the source of truth for restoring manuscript, design,
and build settings. Each published PDF and EPUB companion is kept under
`deliverables/` with the same version number.

## Release convention

- **Major/minor (`v1.3.0`)** — a completed editorial or design revision.
- **Patch (`v1.3.1`)** — a correction or production-only revision after a
  release candidate.
- Recreate a recorded PDF with `make deliverable BOOK_VERSION=vX.Y.Z`.
- Recreate only its landscape reader-spread proof with
  `make reader-spread BOOK_VERSION=vX.Y.Z`. This pairs consecutive pages
  for on-screen reading; it is not printer imposition.
- Restore a source state with `git checkout book-vX.Y.Z` (or create a
  working branch from that tag); do not edit a historical release tag.

## v1.8.0 — Operational controls and compact brief

- **Status:** released.
- **Source tag:** `book-v1.8.0`.
- **Full PDF:** `deliverables/ai-agents-at-the-border-v1.8.0.pdf`.
- **Executive Decision Brief:**
  `deliverables/ai-agents-at-the-border-executive-summary-v1.8.0.pdf`.
- **Full EPUB:** `deliverables/ai-agents-at-the-border-v1.8.0.epub`.
- **Scope:** renames the internal *safety case* as the **operational
  assurance record**. The brief adds measurable board thresholds,
  stopping/escalation logic for its ninety-day plan, five operating rules,
  a chapter-specific reference map, and a legal-cut-off warning for
  Sections 8.2–8.4. The print brief is now 56 physical pages including
  covers; one intentional blank verso preserves the back-cover position.

## v1.7.1 — Agency-profile clarification

- **Status:** released.
- **Source tag:** `book-v1.7.1`.
- **Full PDF:** `deliverables/ai-agents-at-the-border-v1.7.1.pdf`.
- **Executive Decision Brief:**
  `deliverables/ai-agents-at-the-border-executive-summary-v1.7.1.pdf`.
- **Full EPUB:** `deliverables/ai-agents-at-the-border-v1.7.1.epub`.
- **Internal spread proof:**
  `deliverables/ai-agents-at-the-border-v1.7.1-spread.pdf` (not a public
  release artifact).
- **Scope:** expands the brief's second dial with a six-line agency-profile
  record and two customs-specific counterexamples. An L2 HS copilot with
  estate-wide credentials is shown as dangerous despite human confirmation;
  an L3 case-file agent with one-case, allowlisted, read-only reach is shown
  as manageable. The brief remains 60 physical pages with no inserted blanks.

## v1.7.0 — Self-contained Executive Decision Brief

- **Status:** released.
- **Source tag:** `book-v1.7.0`.
- **Full PDF:** `deliverables/ai-agents-at-the-border-v1.7.0.pdf`.
- **Executive Decision Brief:**
  `deliverables/ai-agents-at-the-border-executive-summary-v1.7.0.pdf`.
- **Full EPUB:** `deliverables/ai-agents-at-the-border-v1.7.0.epub`.
- **Internal spread proof:**
  `deliverables/ai-agents-at-the-border-v1.7.0-spread.pdf` (not a public
  release artifact).
- **Scope:** makes the brief operationally self-contained. The Eight
  Decisions become a gated dependency chain with Gates 1-4 required before
  value, sourcing, right-to-operate, or renewal decisions. The brief adds a
  five-tool executive starter kit: mandate card, minimum metric spine,
  regulatory applicability checklist, RFP decision-rights clause, and pilot
  gate. Each Core Tool is a complete one-page worksheet, supported by a
  90-minute working-session sequence. The revised brief is 60 physical pages
  including covers, with no inserted blank pages.

## v1.6.2 — Executive Summary technical corrections

- **Status:** released.
- **Source tag:** `book-v1.6.2`.
- **Full PDF:** `deliverables/ai-agents-at-the-border-v1.6.2.pdf`.
- **Executive Summary:**
  `deliverables/ai-agents-at-the-border-executive-summary-v1.6.2.pdf`.
- **Full EPUB:** `deliverables/ai-agents-at-the-border-v1.6.2.epub`.
- **Internal spread proof:**
  `deliverables/ai-agents-at-the-border-v1.6.2-spread.pdf`.
- **Scope:** removes a compound phrase that could collapse during PDF text
  extraction; renders the portable-baseline warning as a complete compact
  box; and makes the brief's 12–24 month watch record explicitly
  self-contained rather than relying on the full edition's Appendix D.5.

## v1.6.1 — Executive Summary pagination patch

- **Status:** released.
- **Source tag:** `book-v1.6.1`.
- **Full PDF:** `deliverables/ai-agents-at-the-border-v1.6.1.pdf`.
- **Executive Summary:**
  `deliverables/ai-agents-at-the-border-executive-summary-v1.6.1.pdf`.
- **Full EPUB:** `deliverables/ai-agents-at-the-border-v1.6.1.epub`.
- **Internal spread proof:**
  `deliverables/ai-agents-at-the-border-v1.6.1-spread.pdf`.
- **Scope:** Executive Summary folios now use one continuous Arabic sequence
  after the unnumbered title; the unnecessary title verso and
  pre-back-cover padding pages are removed; the local-law warning becomes a
  compact editorial box; and one security/data passage is copyedited to
  eliminate a two-line orphan without changing its control requirements.
  The brief is now exactly 52 physical pages, including covers, with the
  original 11 pt / 1.46 typography preserved.

## v1.6.0 — Critical-review revision and Executive Summary

- **Status:** released.
- **Source tag:** `book-v1.6.0`.
- **Full PDF:** `deliverables/ai-agents-at-the-border-v1.6.0.pdf`.
- **Executive Summary:**
  `deliverables/ai-agents-at-the-border-executive-summary-v1.6.0.pdf`.
- **Full EPUB:** `deliverables/ai-agents-at-the-border-v1.6.0.epub`.
- **Internal spread proof:**
  `deliverables/ai-agents-at-the-border-v1.6.0-spread.pdf` (not a public
  website download).
- **Scope:** response to the independent critical review dated 10 July
  2026. Added an agent/fixed-workflow bright-line test; paired the Autonomy
  Ladder with a mandatory agency profile; strengthened evidence labels and
  case-transfer boundaries; clarified sovereign-cloud accreditation and a
  safe transition from excluded territory; made readiness explicitly
  per-use-case; classified the twenty-samples exercise as qualitative
  pre-qualification; added local-law, portable-baseline, and internal-
  safety-case caveats; extended the 12–24 month regulatory watch; added the
  non-scaling pilot to the cautionary museum and new glossary terms; and
  strengthened the Stance visual. The full book remains the reference
  edition. A separately designed approximately 50-page Executive Summary
  now provides the leadership fast route.

## v1.5.2 — Legal cut-off and publication audit

- **Status:** released.
- **Source tag:** `book-v1.5.2`.
- **PDF:** `deliverables/ai-agents-at-the-border-v1.5.2.pdf`.
- **EPUB:** `deliverables/ai-agents-at-the-border-v1.5.2.epub`.
- **Reader spreads:** `deliverables/ai-agents-at-the-border-v1.5.2-spread.pdf`.
- **Scope:** Chapter 8 and Appendix D legally cut off at 10 July 2026
  against named official sources; all reader-facing `[MOVING]` markers
  resolved into dated records; Malaysia, Korea, China, Singapore, Egypt,
  UAE, Kuwait and EU status corrected where the source check changed the
  record; automated publication-artifact audit added and passed; back
  cover points to `era-society.ae`, while the in-text companion link
  remains the public repository.

## v1.5.1 — Reader-facing corrections

- **Status:** released.
- **Source tag:** `book-v1.5.1`.
- **PDF:** `deliverables/ai-agents-at-the-border-v1.5.1.pdf`.
- **EPUB:** `deliverables/ai-agents-at-the-border-v1.5.1.epub`.
- **Reader spreads:** `deliverables/ai-agents-at-the-border-v1.5.1-spread.pdf`.
- **Scope:** duplicate title-page author credit removed; author affiliation
  standardised to Agility; public companion-repository link added; three
  overflowing executive blocks tightened; Figure C.1 given a dedicated
  full-page treatment; Bibliography begins on a fresh page and appears in
  the table of contents. Print PDF remains 376 physical pages, a multiple
  of four.

## v1.5.0 — Complete-cover and reader-layout revision

- **Status:** released.
- **Source tag:** `book-v1.5.0`.
- **PDF:** `deliverables/ai-agents-at-the-border-v1.5.0.pdf`.
- **EPUB:** `deliverables/ai-agents-at-the-border-v1.5.0.epub`.
- **Reader spreads:** `deliverables/ai-agents-at-the-border-v1.5.0-spread.pdf`.
- **Scope:** full back cover and a print-signature check (376 physical pages,
  a multiple of four); map of the book on its own page; all primary diagrams
  restored to full usable width; compact, reader-oriented opportunity and
  commercial-normalisation tables; endnote-break control; red publication
  placeholders; revised author card (UAE); 10.7 pt / 1.40 reader typography.

## v1.4.1-spread — Reader-spread companion

- **Status:** released.
- **Source tag:** `book-v1.4.1-spread`.
- **PDF:** `deliverables/ai-agents-at-the-border-v1.4.1-spread.pdf`.
- **Scope:** 12 × 9 inch landscape viewing proof with page 1 next to page 2,
  page 3 next to page 4, and so on. The source PDF remains the 6 × 9 inch
  portrait, print-ready edition; this companion deliberately does not
  reorder pages for physical printer signatures.

## v1.4.1 — Reader-edition front matter

- **Status:** released.
- **Source tag:** `book-v1.4.1`.
- **PDF:** `deliverables/ai-agents-at-the-border-v1.4.1.pdf`.
- **EPUB:** `deliverables/ai-agents-at-the-border-v1.4.1.epub`.
- **Scope:** review half-title removed; formal title page followed by
  intentional blank verso; short foreword before the table of contents;
  navy table of contents and 1.25 leading to retain 350+ pages.

## v1.4.0 — Reader-edition front-matter candidate

- **Source tag:** `book-v1.4.0` (commit `469d034`).
- **PDF:** `deliverables/ai-agents-at-the-border-v1.4.0.pdf`.
- **Scope:** half-title removal and title → blank verso → foreword → ToC
  ordering; retained as an auditable build before final typography tuning.

## v1.2.2 — Full-content and layout revision

- **Source tag:** `book-v1.2.2` (commit `338afed`).
- **PDF:** `deliverables/ai-agents-at-the-border-v1.2.2.pdf`.
- **Scope:** full chapter and appendix expansion; evidence, procurement,
  operational-control, security and workforce tools; cropped SVG figures;
  6 × 9 typography with 1.20 leading; versioned build pipeline.

## v1.3.4 — Editorial and production revision

- **Status:** released.
- **Source tag:** `book-v1.3.4`.
- **PDF:** `deliverables/ai-agents-at-the-border-v1.3.4.pdf`.
- **EPUB:** `deliverables/ai-agents-at-the-border-v1.3.4.epub`.
- **Scope:** author note relocated and reduced; anti-orphan controls for
  headings and callouts; compact bibliography; O'Reilly-compatible
  structural and production rules; 1.24 leading to preserve the 350+
  page executive-book format; blank-verso and stranded-Endnotes fixes;
  endnotes print directly below their chapter heading; no automatic blank
  versos between parts, chapters and appendices.

## v1.3.3 — Production revision candidate

- **Source tag:** `book-v1.3.3` (commit `a82e035`).
- **PDF:** `deliverables/ai-agents-at-the-border-v1.3.3.pdf`.
- **Scope:** endnotes moved beneath their heading; retained as an
  auditable build before the final blank-verso override.

## v1.3.2 — Production revision candidate

- **Source tag:** `book-v1.3.2` (commit `7266b7d`).
- **PDF:** `deliverables/ai-agents-at-the-border-v1.3.2.pdf`.
- **Scope:** custom part blank-verso and short-page correction; retained
  as an auditable build before endnote-output sequencing was corrected.

## v1.3.1 — Production revision candidate

- **Source tag:** `book-v1.3.1` (commit `2669c66`).
- **PDF:** `deliverables/ai-agents-at-the-border-v1.3.1.pdf`.
- **Scope:** 1.24 leading applied after bibliography compaction; retained
  as an auditable pre-release build.

## v1.3.0 — Editorial revision candidate

- **Source commit:** `15b3832`.
- **PDF:** `deliverables/ai-agents-at-the-border-v1.3.0.pdf`.
- **Scope:** initial author-note relocation, anti-orphan controls and
  bibliography compaction; retained as an auditable pre-release build.
