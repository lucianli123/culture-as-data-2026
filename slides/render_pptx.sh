#!/usr/bin/env bash
# Re-render every weekly Markdown deck to PowerPoint (.pptx) into slides/pptx/.
# Requires pandoc (https://pandoc.org). Run from the repo root: bash slides/render_pptx.sh
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p pptx
for md in week-*.md; do
  pandoc "$md" -o "pptx/${md%.md}.pptx" --slide-level=2
  echo "rendered pptx/${md%.md}.pptx"
done
