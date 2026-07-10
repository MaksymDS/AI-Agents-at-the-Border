#!/usr/bin/env bash
# Build the book (PDF + EPUB) into _build/.
# Usage: scripts/build.sh [pdf|epub|all]
set -euo pipefail

cd "$(dirname "$0")/.."

# Deterministic fonts for SVG figure conversion (see assets/fonts/fonts.conf)
export FONTCONFIG_FILE="$PWD/fonts/fonts.conf"
export PANGOCAIRO_BACKEND=fc

if ! command -v quarto >/dev/null 2>&1; then
  echo "error: quarto not found. Install it (https://quarto.org/docs/get-started/)" >&2
  echo "       and the LaTeX toolchain: quarto install tinytex" >&2
  exit 1
fi

bash scripts/prebuild.sh
rsvg-convert -f png -w 1200 -o assets/prebuilt/cover-final.png assets/cover/cover-final.svg
for n in 1 2 3 4 5; do
  sed 's|<text x="288" y="812"[^>]*>[^<]*</text>||' "assets/interior/interior-part-$n.svg" > "assets/prebuilt/part-$n-tmp.svg"
  rsvg-convert -f pdf -o "assets/prebuilt/interior-part-$n.pdf" "assets/prebuilt/part-$n-tmp.svg"
  rm "assets/prebuilt/part-$n-tmp.svg"
done

target="${1:-all}"
case "$target" in
  pdf)  quarto render --to pdf ;;
  epub) quarto render --to epub ;;
  all)  quarto render ;;
  *)    echo "usage: $0 [pdf|epub|all]" >&2; exit 2 ;;
esac

echo "Build output in _build/"
