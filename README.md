# Culture as Data

A 10-week, project-based community course that teaches curious adults to investigate cultural
data at scale with an AI assistant as a coding partner — counting, classification, embeddings,
and AI annotation — ending in a published web essay. This repository is the **buildable
artifact** for the course: the static course **site** and the Colab **notebooks** the course
teaches from.

The course design lives in four markdown documents (kept one directory up, in the project
root): `overview.md`, `syllabus.md`, `lesson-plans.md`, and `planning-doc.md`. Those are the
source of truth. This repo turns them into things you can open, run, and deploy.

## What's here

```
culture-as-data/
├── README.md                  ← you are here
├── docs/                      ← the static course site (deploy to GitHub Pages)
│   ├── index.html  syllabus.html  schedule.html  resources.html  about.html
│   ├── weeks/week-01.html … week-10.html
│   ├── assets/style.css
│   └── _build/                ← note on how the site is generated
├── notebooks/                 ← the Colab notebooks
│   ├── README.md              ← how to open in Colab + the "tested as of" stamp
│   ├── requirements.txt       ← pinned "extra" packages only
│   ├── constraints.txt        ← hard pins for the resolver
│   ├── _smoke_test.ipynb      ← run this first in Colab to confirm a healthy runtime
│   ├── week02_counting.ipynb           (fully worked)
│   ├── week03_classification.ipynb     (fully worked)
│   ├── week04_data_cookbook.ipynb      (fully worked)
│   ├── week05_embeddings.ipynb         (fully worked)
│   ├── week05_embeddings_GUIDED.ipynb  (Act-2 completion, fuller guidance)
│   ├── week05_embeddings_SKELETON.ipynb(Act-2 completion, skeleton)
│   ├── week07_annotator.ipynb          (fully worked)
│   ├── week07_annotator_GUIDED.ipynb
│   ├── week07_annotator_SKELETON.ipynb
│   └── cool-methods/          ← optional starter notebooks
├── kits/
│   ├── common-errors-cheatsheet.md     ← the unblocking kit
│   └── pivot-kit-corpora.md            ← fallback corpus + question bank
└── tools/
    ├── build_site.py          ← regenerates docs/ for GitHub Pages
    ├── check_compat.py        ← package-compatibility resolver check (Layer 1)
    └── run_notebooks.sh        ← headless execution in a Colab-like container (Layer 2)
```

## Using the notebooks in Colab

1. Open [Google Colab](https://colab.research.google.com/) and sign in with a Google account.
2. `File → Open notebook → GitHub` (or `Upload`), and pick a `weekNN_*.ipynb` file.
3. Run the **first code cell** — it installs the pinned extra packages with
   `%pip install -q -r requirements.txt -c constraints.txt`. (When opening a single notebook
   without the repo, each notebook also carries an explicit pinned `%pip install` fallback.)
4. Run the **imports cell**. If anything fails, see `kits/common-errors-cheatsheet.md`.
5. For Week 7 you'll need a free **Gemini API key** from
   [Google AI Studio](https://aistudio.google.com/). Paste it into Colab Secrets as
   `GEMINI_API_KEY` (never hard-code it). The notebook runs end-to-end without a key using a
   recorded sample response, so you can read the whole pipeline first.

**Runtime expectations.** Everything is built for the **Colab free tier** (intermittent T4 GPU,
~12 GB RAM, no persistent storage). Week 5 (embeddings + CLIP) is the only notebook that wants
a GPU; it falls back to CPU on a tiny corpus. Cost target is **$0 per student** — the only paid
path is an optional API key, and the Gemini free tier covers the course.

## Re-running the compatibility harness (when Colab changes)

Colab refreshes its preinstalled image periodically. The `notebooks/README.md` carries a "tested
as of" date and the Python / numpy / torch versions it passed against. When that date is stale,
re-run the harness:

```bash
# Layer 1 — does the pinned set even resolve? (seconds, no execution)
python tools/check_compat.py

# Layer 2 — do all notebooks run top-to-bottom in a Colab-like image?
bash tools/run_notebooks.sh

# Layer 3 — the student-facing safety net: open notebooks/_smoke_test.ipynb in real Colab
#           and read the all-green report. Its printed output IS the "tested as of" record.
```

If anything moved, re-freeze the working versions from a successful Colab run (`pip freeze`)
back into `requirements.txt` / `constraints.txt`, and update the stamp in `notebooks/README.md`.

## Building the site

The site is generated from structured content by a small Python script (no framework, no build
toolchain beyond Python):

```bash
python tools/build_site.py      # regenerates everything under docs/
```

See the header comment in `tools/build_site.py` for the rationale and how to edit content. Deploy by pushing the
`docs/` directory to a `gh-pages` branch or serving it from `/docs` (the default this repo is set up for) on GitHub Pages — there is
no build step on the server; it's plain HTML + one CSS file and reads fully with JavaScript off.

## Design notes / choices flagged for review

- **Site generation** uses a Python build script (BUILD-PLAN §2 preferred option) rather than
  Quarto, for trivially-reproducible regeneration and zero server build step. The content is
  curated from the four design docs and held as structured data in `tools/build_site.py`.
- **LLM provider** defaults to the **Gemini API free tier** per the design docs. Keys are read
  from a Colab secret / environment variable, never hard-coded.
- **Heavy/GPU and live-API notebook paths** (Week 5 embeddings/CLIP at full size on a T4, and
  Week 7 live Gemini calls) require a real Colab runtime or the published Colab Docker image to
  verify at full fidelity. The harness runs them on tiny CPU corpora with the API mocked; the
  one full-size T4 run is a documented manual step (BUILD-PLAN §4d).
