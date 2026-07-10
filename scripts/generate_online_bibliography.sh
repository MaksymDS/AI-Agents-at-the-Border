#!/usr/bin/env bash
set -euo pipefail

# The print edition asks Quarto to render the #refs placeholder in Appendix G.
# The React reader consumes Markdown directly, so it needs a committed,
# generated Markdown bibliography from the same sources.bib file.
root="$(cd "$(dirname "$0")/.." && pwd)"
quarto_bin="${QUARTO:-quarto}"

printf '%s\n' \
  '---' \
  'nocite: |' \
  '  @*' \
  '---' \
  '' \
  '# Bibliography' \
  '' \
  '::: {#refs}' \
  ':::' \
  | "$quarto_bin" pandoc -f markdown -t markdown --citeproc --bibliography="$root/research/sources.bib" \
  | sed -E '/^:{3,}.*$/d' \
  | sed -E 's/\[([^]]+)\]\{\.nocase\}/\1/g; s/---/—/g' \
  | { printf '<!-- GENERATED from research/sources.bib; run scripts/generate_online_bibliography.sh after bibliography edits. -->\n\n'; cat; } \
  > "$root/web/bibliography.md"
