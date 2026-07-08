#!/usr/bin/env bash
# run_notebooks.sh — Layer 2 of the compatibility harness (BUILD-PLAN §4c).
#
# Executes every notebook top-to-bottom WITHOUT a browser and fails on any cell error.
# The point is faithfulness to the student's environment, so the default is to run
# inside Google's published Colab base image rather than a clean local Python.
#
#   Faithful (recommended):   bash tools/run_notebooks.sh --docker
#   Quick/local (approximate): bash tools/run_notebooks.sh --local
#
# Two safety rails make this CI-able with no key and no spend:
#   * Week 7's live Gemini cells are gated behind `if os.environ.get("GEMINI_API_KEY")`
#     and ship a recorded sample response, so the notebook runs end-to-end mocked.
#   * Week 5's embedder falls back to a deterministic stand-in when the model can't
#     load; the full-size T4 run is a separate, manual Colab check (BUILD-PLAN §4d).
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NB_DIR="$REPO/notebooks"
OUT_DIR="$NB_DIR/_executed"
COLAB_IMAGE="us-docker.pkg.dev/colab-images/public/runtime"
MODE="${1:---local}"

# No keys are set here, so live paths fall back gracefully: Week 7 uses its recorded
# cassette, and loaders prefer the repo's data snapshots.

run_local() {
  python -m pip install -q nbclient nbconvert jupyter
  mkdir -p "$OUT_DIR"
  jupyter nbconvert --to notebook --execute \
    --ExecutePreprocessor.timeout=900 \
    --output-dir "$OUT_DIR" \
    $(ls "$NB_DIR"/week*.ipynb | grep -vE "_GUIDED|_SKELETON")
  echo "All notebooks executed with zero cell errors. Output in $OUT_DIR"
  # GUIDED/SKELETON variants are completion problems: their blank cells error by
  # design until a student fills them, so they are excluded from headless execution.
}

run_docker() {
  echo "Pulling Colab base image (matches the student runtime)…"
  docker pull "$COLAB_IMAGE"
  docker run --rm -v "$REPO":/work -w /work \
    "$COLAB_IMAGE" bash -lc '
      pip install -q nbclient nbconvert jupyter &&
      pip install -q -r notebooks/requirements.txt -c notebooks/constraints.txt &&
      mkdir -p notebooks/_executed &&
      jupyter nbconvert --to notebook --execute \
        --ExecutePreprocessor.timeout=900 \
        --output-dir notebooks/_executed \
        $(ls notebooks/week*.ipynb | grep -vE "_GUIDED|_SKELETON")
    '
  echo "All notebooks executed in the Colab base image with zero cell errors."
}

case "$MODE" in
  --docker) run_docker ;;
  --local)  run_local  ;;
  *) echo "usage: $0 [--docker|--local]"; exit 2 ;;
esac
