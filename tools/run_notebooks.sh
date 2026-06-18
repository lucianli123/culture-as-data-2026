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
#   * GPU notebooks (Week 5) run on CPU with a tiny corpus (SMOKE=1) so CI finishes;
#     the full-size T4 run is a separate, manual Colab check (BUILD-PLAN §4d).
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NB_DIR="$REPO/notebooks"
OUT_DIR="$NB_DIR/_executed"
COLAB_IMAGE="us-docker.pkg.dev/colab-images/public/runtime"
MODE="${1:---local}"

# Run notebooks in tiny/mocked mode so CI is fast and key-free. The notebooks read
# these env vars; see each notebook's config cell.
export CULTURE_AS_DATA_SMOKE=1     # tiny corpora, CPU-only
# GEMINI_API_KEY intentionally unset here -> Week 7 uses its recorded cassette.

run_local() {
  python -m pip install -q nbclient nbconvert jupyter
  mkdir -p "$OUT_DIR"
  jupyter nbconvert --to notebook --execute \
    --ExecutePreprocessor.timeout=900 \
    --output-dir "$OUT_DIR" \
    "$NB_DIR"/_smoke_test.ipynb "$NB_DIR"/week*.ipynb
  echo "All notebooks executed with zero cell errors. Output in $OUT_DIR"
}

run_docker() {
  echo "Pulling Colab base image (matches the student runtime)…"
  docker pull "$COLAB_IMAGE"
  docker run --rm -v "$REPO":/work -w /work \
    -e CULTURE_AS_DATA_SMOKE=1 \
    "$COLAB_IMAGE" bash -lc '
      pip install -q nbclient nbconvert jupyter &&
      pip install -q -r notebooks/requirements.txt -c notebooks/constraints.txt &&
      mkdir -p notebooks/_executed &&
      jupyter nbconvert --to notebook --execute \
        --ExecutePreprocessor.timeout=900 \
        --output-dir notebooks/_executed \
        notebooks/_smoke_test.ipynb notebooks/week*.ipynb
    '
  echo "All notebooks executed in the Colab base image with zero cell errors."
}

case "$MODE" in
  --docker) run_docker ;;
  --local)  run_local  ;;
  *) echo "usage: $0 [--docker|--local]"; exit 2 ;;
esac
