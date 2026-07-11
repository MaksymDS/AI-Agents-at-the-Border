QUARTO ?= quarto
BOOK_VERSION ?= v1.9.3

# Deterministic fonts for SVG figure conversion: pin the renderer's font
# lookup to the vendored Inter (see fonts/fonts.conf). The Pango backend
# override forces fontconfig on macOS, where CoreText would otherwise
# ignore FONTCONFIG_FILE.
export FONTCONFIG_FILE := $(CURDIR)/fonts/fonts.conf
export PANGOCAIRO_BACKEND := fc

# OPENANY=1 renders the digital layout (chapters open on any page, no
# blank versos); default is the print layout (recto-open).
OPENANY_PROFILE := $(if $(OPENANY),--profile openany,)

.PHONY: build pdf epub executive-summary deliverable deliverable-epub deliverable-executive kindle-assets kindle-epub kindle-docx deliverable-kindle deliverable-kindle-docx reader-spread review-pdf prebuild embed-figures clean check-bib check-notes audit-publication status

# Convert front-of-book and part-opener SVGs to PDF/PNG pages
prebuild:
	bash scripts/prebuild.sh

# Re-apply the figure manifest after content re-imports (idempotent)
embed-figures:
	python3 scripts/embed_figures.py

# Render all formats in one pass; rendering a single format cleans
# _build/, so pdf/epub targets are for iteration only.
build: prebuild
	$(QUARTO) render $(OPENANY_PROFILE)
	python3 scripts/pad_print_pdf.py _build/ai-agents-at-the-border.pdf

pdf: prebuild
	$(QUARTO) render --to pdf $(OPENANY_PROFILE)
	python3 scripts/pad_print_pdf.py _build/ai-agents-at-the-border.pdf

# A reviewable, versioned book artifact kept under version control. The
# ignored _build/ directory remains the compiler's workspace; prior
# editions remain available for comparison rather than being overwritten.
# A companion reader-spread PDF places each pair of consecutive book pages
# on one landscape sheet; it is not printer imposition and does not replace
# the portrait, print-ready PDF.
deliverable: pdf
	mkdir -p deliverables
	cp _build/ai-agents-at-the-border.pdf deliverables/ai-agents-at-the-border-$(BOOK_VERSION).pdf
	$(MAKE) reader-spread

# Recreate the landscape, two-pages-per-sheet proof from the recorded
# portrait deliverable without rerendering the manuscript.
reader-spread:
	python3 scripts/make_reader_spread.py \
		deliverables/ai-agents-at-the-border-$(BOOK_VERSION).pdf \
		deliverables/ai-agents-at-the-border-$(BOOK_VERSION)-spread.pdf

epub: prebuild
	$(QUARTO) render --to epub

# EPUB companion to the versioned PDF release. Keep the artifact under the
# same release number so readers can compare editions and restore exactly.
deliverable-epub: epub
	mkdir -p deliverables
	cp _build/ai-agents-at-the-border.epub deliverables/ai-agents-at-the-border-$(BOOK_VERSION).epub

kindle-assets:
	python3 scripts/prepare_kindle_assets.py

kindle-epub: kindle-assets prebuild
	$(QUARTO) render --profile kindle --to epub

deliverable-kindle: kindle-epub
	mkdir -p deliverables
	cp _build-kindle/ai-agents-at-the-border-kindle.epub \
		deliverables/ai-agents-at-the-border-kindle-$(BOOK_VERSION).epub

# Direct KDP fallback when the EPUB converter reports an HTML package error.
# Kindle reflows this DOCX; it is not a replacement for the paperback PDF.
kindle-docx: kindle-assets prebuild
	$(QUARTO) render --profile kindle-docx --to docx

deliverable-kindle-docx: kindle-docx
	mkdir -p deliverables
	cp _build-kindle-docx/ai-agents-at-the-border-kindle.docx \
		deliverables/ai-agents-at-the-border-kindle-$(BOOK_VERSION).docx

# Standalone executive decision brief. It shares the book's typography and
# visual grammar but has its own title, contents and output directory.
executive-summary: prebuild
	$(QUARTO) render executive-summary --to pdf
	python3 scripts/pad_print_pdf.py executive-summary/_build/ai-agents-at-the-border-executive-summary.pdf

deliverable-executive: executive-summary
	mkdir -p deliverables
	cp executive-summary/_build/ai-agents-at-the-border-executive-summary.pdf \
		deliverables/ai-agents-at-the-border-executive-summary-$(BOOK_VERSION).pdf

# Review edition: REVIEW DRAFT title marking, page watermark, reviewer's
# brief bound in after the title page. Output in _build-review/.
review-pdf: prebuild
	$(QUARTO) pandoc reviewer-brief.md -f markdown -t latex \
		--top-level-division=chapter -o latex/review-brief.tex
	$(QUARTO) render --profile review --to pdf

check-bib:
	python3 scripts/check_bib.py

check-notes:
	python3 scripts/check_notes.py

# Reader-facing source audit: unresolved bracket placeholders and common
# assistant boilerplate are release blockers. Appendix worksheet blanks are
# intentional working fields and are not matched by this check.
audit-publication:
	python3 scripts/audit_publication.py

status:
	python3 scripts/gen_status.py

clean:
	rm -rf _build _build-review executive-summary/_build _build-assets assets/prebuilt .quarto executive-summary/.quarto
