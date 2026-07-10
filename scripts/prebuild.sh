#!/usr/bin/env bash
# Convert front-of-book and part-opener SVGs to PDF/PNG pages.
# Requires FONTCONFIG_FILE/PANGOCAIRO_BACKEND (exported by the Makefile).
set -euo pipefail
cd "$(dirname "$0")/.."

mkdir -p assets/prebuilt

for f in cover-final half-title title-page executive-summary-title back-cover; do
  rsvg-convert -f pdf -o "assets/prebuilt/$f.pdf" "assets/cover/$f.svg"
done
rsvg-convert -f png -w 1200 -o assets/prebuilt/cover-final.png assets/cover/cover-final.svg
rsvg-convert -f pdf -o assets/prebuilt/fig-book-map.pdf assets/diagrams/fig-book-map.svg
rsvg-convert -f pdf -o assets/prebuilt/fig-appc-scorecard-weights.pdf assets/diagrams/fig-appc-scorecard-weights.svg

# Part openers: strip the Designer's static sample folio (centered text at
# y=812) — the build supplies the real folio via the plain page style.
for n in 1 2 3 4 5; do
  tmp="assets/prebuilt/part-$n-tmp.svg"
  sed 's|<text x="288" y="812"[^>]*>[^<]*</text>||' \
    "assets/interior/interior-part-$n.svg" > "$tmp"
  rsvg-convert -f pdf -o "assets/prebuilt/interior-part-$n.pdf" "$tmp"
  rm "$tmp"
done
