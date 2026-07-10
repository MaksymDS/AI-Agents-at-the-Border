# Diagrams

Designer-delivered SVG sources for book figures, imported verbatim. The
build pipeline owns embedding: figures are referenced from chapters and
converted to vector PDF at compile time by `rsvg-convert` (locally:
`brew install librsvg`; CI installs `librsvg2-bin`).

## File naming (per STYLE-GUIDE.md §5)

- `fig-chXX-slug.svg` — color/primary variant
  (e.g., `fig-ch04-opportunity-map.svg`)
- `fig-chXX-slug-bw.svg` — grayscale variant for print

## How chapters embed a figure

```markdown
![Figure 4.1 — The Agentic Opportunity Map](/assets/diagrams/fig-ch04-opportunity-map.svg){width=100%}
```

The alt text carries the full `Figure X.Y — Title` caption (numbering is
manual, per chapter; LaTeX's own "Figure N:" label is suppressed in
`latex/endnotes.tex`). `width=100%` fills the 4.55 in text block of the
6"×9" page.

## Fonts

The accepted delivery format uses **live `<text>` elements with no
`font-family`** — text inherits the renderer default. The pipeline pins
that default to the vendored Inter (`assets/fonts/inter/` +
`assets/fonts/fonts.conf`, activated via `FONTCONFIG_FILE` and
`PANGOCAIRO_BACKEND=fc` in the Makefile, `scripts/build.sh`, and CI), so
figure text renders in Inter 400/500/600/700 deterministically on every
machine. Do not add `font-family` attributes pointing at other fonts
without extending the vendored set.

## SVG export requirements (relay to the Designer)

1. Plain SVG 1.1, one file per figure; live text is fine (see Fonts
   above). No external references (linked images, CSS files, webfonts);
   no embedded rasters unless unavoidable (if so: ≥300 dpi at final size).
2. Uniform artboard `viewBox="0 0 576 864"` (6"×9" at 96 dpi CSS px), as
   in the accepted set.
3. Design for a 4.55 in maximum printed width: minimum stroke 0.5 pt and
   minimum type ~6.5 pt at that width.
4. Use the locked design system (level color ramp #E9EDF1→#1B3A5C,
   amber = decision authority) and deliver the `-bw` grayscale variant
   alongside.
