# Notebooks, how to open, run, and re-verify

These are the labs the course teaches *from*. Students don't write them from scratch, the AI
assistant writes code during class, so the code here is optimized for being **read and
narrated**, not for being clever. Every code cell has a plain-language Markdown cell above it.

## Opening in Colab

1. [colab.research.google.com](https://colab.research.google.com/) → `File → Open notebook`.
2. Upload a `weekNN_*.ipynb`, or open it from GitHub.
3. Run the **first code cell**: `%pip install -q -r requirements.txt -c constraints.txt`.
   (Opening a lone notebook without the repo files? Each notebook also has a commented explicit
   pinned `%pip install` line you can use instead.)
4. Run the **imports cell**. If it errors, open `../kits/common-errors-cheatsheet.md`.

Run **`_smoke_test.ipynb` first** on day one. It imports every package the course uses, prints
each version, and runs one trivial operation per library. A green report means your runtime is
healthy; a red one points you at the exact cheat-sheet entry.

## Which notebook is which

| Notebook | Act | Form | Tool |
|---|---|---|---|
| `week01_first_investigation.ipynb` | 1 | fully worked | load a CSV / first chart / pixel-count an image corpus / the unblocking drill |
| `week02_counting.ipynb` | 1 | fully worked | counting / tf-idf / signature vocabulary |
| `week03_classification.ipynb` | 1 | fully worked | logistic regression + signed weights |
| `week04_data_cookbook.ipynb` | 2 | fully worked | file load + API pull + polite scrape |
| `week05_embeddings.ipynb` | 2 | fully worked | text + CLIP image embeddings |
| `week05_embeddings_GUIDED.ipynb` | 2 | completion (fuller guidance) | embeddings |
| `week05_embeddings_SKELETON.ipynb` | 2 | completion (skeleton) | embeddings |
| `week07_annotator.ipynb` | 2 | fully worked | Gemini LLM-as-annotator |
| `week07_annotator_GUIDED.ipynb` | 2 | completion (fuller guidance) | annotator |
| `week07_annotator_SKELETON.ipynb` | 2 | completion (skeleton) | annotator |

Act-1 ships fully-worked notebooks. Act-2 ships **completion problems** in two parallel
difficulty versions, *GUIDED* (fuller scaffolding) and *SKELETON* (more blanked), so one room
serves a first-timer and an experienced coder at once.

## Runtime expectations (Colab free tier)

- Intermittent **T4 GPU**, ~12 GB RAM, no persistent storage.
- Only **Week 5** wants a GPU (embeddings + CLIP). It detects the GPU and falls back to a small
  CPU run if none is attached.
- **Week 7** needs no GPU but wants a free **Gemini API key** (Colab secret `GEMINI_API_KEY`).
  Without a key it runs end-to-end on a recorded sample response, so you can read the pipeline.
- Cost: **$0**. The only paid path is an optional API key, and Gemini's free tier covers it.

## "Tested as of", the version stamp

The honest record of the working version set is the printed output of `_smoke_test.ipynb` from a
real Colab run. Fill this in after the first green run:

| Field | Value |
|---|---|
| Date passed | _PLACEHOLDER. Run `_smoke_test.ipynb` in Colab and record the date_ |
| Python | _e.g. 3.11.x_ |
| numpy | _from the smoke-test printout_ |
| torch | _from the smoke-test printout_ |
| scikit-learn | _from the smoke-test printout_ |
| sentence-transformers | _from the smoke-test printout_ |

Colab updates its image periodically. When the date above is stale, re-run the harness
(`tools/check_compat.py`, then `tools/run_notebooks.sh`), re-freeze pins from a successful Colab
`pip freeze`, and update this table.

## The compatibility harness (re-run when Colab changes)

- **Layer 1, `tools/check_compat.py`**: resolver dry-run. Seconds. "Do the pins resolve?"
- **Layer 2, `tools/run_notebooks.sh`**: headless execution in the Colab base image. Catches
  import-time and runtime breakage. Gemini mocked, GPU cells on a tiny CPU corpus.
- **Layer 3, `_smoke_test.ipynb`**: the student-facing safety net, run in real Colab.

A separate **manual** full-size run of `week05_embeddings.ipynb` on a real T4 confirms the heavy
path fits the runtime limits; note the wall-clock time so the instructor knows what to expect in
class (BUILD-PLAN §4d).
