#!/usr/bin/env bash
# Build the styled weekly PowerPoint decks into slides/pptx/.
#   1. refresh slides.json from the site data   2. render with pptxgenjs
# Requires: python3, node, and `npm install pptxgenjs` (once).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 slides/export_slides.py
( cd slides && node styled_pptx.js )
