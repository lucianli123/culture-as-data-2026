# Build Plan — Culture as Data: Course Site & Colab Notebooks

A self-contained implementation brief for **Claude Cowork**. Two deliverables: (1) a rebuilt static course **site**, and (2) a set of **Colab notebooks** the course teaches from. The course design is fixed and lives in `syllabus.md`, `lesson-plans.md`, `planning-doc.md`, and `overview.md` in this directory — treat those as the source of truth and read them before building. This brief tells you *what to build, in what order, and how to verify it*, with particular attention to **package compatibility**, which is the part most likely to break silently.

**Working in Cowork.** Treat this as a multi-session project, not a single pass. Work artifact-by-artifact, committing and verifying each before moving on (the build order in §5 is dependency-sorted for exactly this). The notebooks need real execution to verify — run them, read the tracebacks, fix, re-run; do not assume code is correct because it looks correct, since the whole point of the course is that plausible-looking code is often subtly wrong. Where a step needs a live Colab runtime or the published Colab Docker image (the compat harness in §4c), set that up rather than approximating with a clean local Python — faithfulness to the student's actual environment is the entire value of the test. When a decision isn't specified here or in the four design docs, prefer the simplest thing that a non-coder could read, and leave a short note in the repo `README.md` flagging the choice so it can be reviewed.

---

## 0. Ground truth and non-negotiables (read before writing code)

- **Course title:** *Culture as Data*. The existing `site/` still says "Reading at Scale" — that is a stale title from an earlier draft. Rebuild, do not patch.
- **Audience:** curious adults, most with little or no coding. Notebooks are taught from, not written by, the students — the AI assistant writes code during class. So notebook code must be **readable and narrated**, not clever.
- **Compute target:** Google **Colab free tier** (intermittent T4 GPU, ~12 GB RAM; the runtime is **ephemeral** and wipes on idle/disconnect). Everything must run there. Persistence is handled by **mounting Google Drive** — every notebook saves the corpus and outputs to a Drive project folder so they survive a reset and carry week to week (the Week-1 setup ritual). Do not assume a paid runtime or a local GPU. **Kaggle Notebooks** (persistent working dir, more reliable free GPU) is the documented fallback for students Colab keeps disconnecting. See `planning-doc.md` → *Environment, Persistence, and Tooling*.
- **Cost target:** **$0 per student.** The only paid path is an optional API key. For LLM steps, default to the **Gemini API free tier** (`google-generativeai`, 1,500 req/day on Gemini 2.5 Flash, vision included). Never hard-code a key; read it from a Colab secret / environment variable.
- **In-notebook AI vs. the API — two different things.** In class, the student's code-writing helper is **Colab's built-in Gemini** (generate a cell; fix an error via diff), which keeps code visible — the whole point; Claude/ChatGPT work identically for students who prefer them. The **Gemini API key** above is separate and needed only for the Week-7 annotation notebook (programmatic labeling). Do **not** design student-facing notebooks around an autonomous agent (Colab's Data Science Agent building whole notebooks, Claude Code) — agents are for building *this course*; students stay on cell-level help so they read and question the code.
- **The four tools (the spine):** counting (W2), classification (W3), embeddings (W5, the heart), AI-annotation (W7). Images are co-equal, taught through the same tools. Networks, sentiment arcs, and **fine-tuning a small open model (`ModernBERT`)** are **optional** methods in `cool-methods/`, never core — fine-tuning especially is a go-further for technical students only. There is **no transformer-internals content** — do not build it. Open models and the embedding models both come from **Hugging Face**; name it on the site's resources page.
- **The design-doc set (source of truth, all in this directory), and what each is for:**
  - `overview.md` — the front door: the hook, the one-sentence pitch, what students make, who it's for. Use for `index.html` and `about.html`.
  - `syllabus.md` — the student-facing course: shape, the eight competencies, the deliverable, setup, starter corpora. Use for `syllabus.html` and the schedule.
  - `lesson-plans.md` — the instructor teach-from doc: minute-by-minute weekly flows, featured studies, datasets, checks. Use for the weekly pages **and** as the per-notebook behavioral spec (what each lab does, in sequence).
  - `planning-doc.md` — the instructor companion: the *why* behind every choice (numbered Principles), the assessment framework, the provider research, the corpus library, the unblocking kit, the pivot-kit. Use for the kits (§3) and whenever a build decision needs its rationale.
  - This `BUILD-PLAN.md` is the index over those four: it tells you what buildable artifacts to produce from them. Read the four docs first; they win on any conflict with this file's summaries.
- **Notebook pedagogy:** Act 1 (W1–3) ships **fully-worked** notebooks. In Act 2, the mechanism-teaching notebooks (W5 embeddings, W7 annotator) additionally ship as **completion problems** in two parallel versions — *fuller-guidance* and *skeleton* (W4's cookbook stays fully worked: it's reference material, not a mechanism to practice). This is the expertise-reversal mechanism; it is required, not optional.
- **House style:** prose explanations in Markdown cells before each code cell; no em-dashes in any student-facing marketing copy on the site (body prose elsewhere is fine); "lyrics" not "songs"; pop-culture examples wherever a corpus is needed (see the pop-culture ratio in `planning-doc.md` Principle 15).

---

## 1. Repository layout to create

```
culture-as-data/
├── README.md                      # what this repo is, how to use it, links
├── site/                          # the static course site (rebuilt)
│   ├── index.html
│   ├── syllabus.html
│   ├── schedule.html
│   ├── resources.html
│   ├── about.html
│   ├── weeks/week-01.html … week-10.html
│   ├── assets/
│   │   ├── style.css
│   │   └── (images, favicon)
├── notebooks/
│   ├── README.md                  # how to open in Colab, the runtime expectations
│   ├── requirements.txt           # PINNED versions (see §4)
│   ├── constraints.txt            # optional: hard pins for the compat-test harness
│   ├── _smoke_test.ipynb          # runs every notebook's imports + a tiny op (see §4)
│   ├── week01_first_investigation.ipynb   # fully worked (Drive-mount ritual + wedding data + word & pixel counting)
│   ├── week02_counting.ipynb              # fully worked
│   ├── week03_classification.ipynb        # fully worked
│   ├── week04_data_cookbook.ipynb         # fully worked (load-a-file + API pull + polite scrape)
│   ├── week05_embeddings.ipynb            # fully worked
│   ├── week05_embeddings_GUIDED.ipynb     # Act-2 completion, fuller guidance
│   ├── week05_embeddings_SKELETON.ipynb   # Act-2 completion, skeleton
│   ├── week07_annotator.ipynb             # fully worked
│   ├── week07_annotator_GUIDED.ipynb
│   ├── week07_annotator_SKELETON.ipynb
│   └── cool-methods/              # optional starter notebooks (stylometry, color, etc.)
├── kits/
│   ├── common-errors-cheatsheet.md        # the unblocking kit (see §3)
│   ├── licensing-one-pager.md             # the Week-4 data-licensing rubric
│   └── pivot-kit-corpora.md               # fallback corpus+question bank
├── template/                              # the publishing template students fork in W4 (Quarto → Pages)
└── tools/
    ├── check_compat.py            # package-compatibility harness (see §4)
    └── run_notebooks.sh           # execute all notebooks headless (see §4)
```

Pin nothing about the *content* of the four design docs here — link to them. This repo is the buildable artifact; the markdown docs are the spec.

---

## 2. Deliverable A — the course site

**Goal:** a clean, fast, static multi-page site that renders the syllabus and weekly plans, deployable to GitHub Pages with no build step. Plain HTML + one CSS file. No framework, no JS dependency for core content (a tiny bit of vanilla JS for nav/progressive enhancement is fine; the site must read fully with JS off).

**Source of content:** generate the page text *from* `syllabus.md` and `lesson-plans.md` so the site and the docs can't drift. Two acceptable approaches — pick one and document it in `site/_build/`:
- **(preferred) A small Python build script** (`tools/build_site.py`) that parses the markdown and emits the HTML pages from a template. This makes regeneration trivial when the docs change.
- **(acceptable) Quarto**, since the course itself teaches Quarto → Pages. If you use Quarto, the site source is `.qmd` and `quarto render` produces `site/`. This has the pedagogical bonus of dogfooding the student toolchain.

**Pages and what each contains:**
1. `index.html` — the front door. Pull the hook, the one-sentence description, the "what you'll make," and the audience from `overview.md`. Lead with delight and making, not just rigor. Title is *Culture as Data*.
2. `syllabus.html` — the full student-facing syllabus from `syllabus.md`: shape of the course, the eight competencies, the deliverable, the "how you'll know you're learning" section, setup, and the pop-weighted starter corpora shortlist.
3. `schedule.html` — the ten weeks at a glance: title, promise, featured study, and the tool/method for each week. Link each week to its `weeks/week-NN.html`.
4. `weeks/week-NN.html` — one page per week, generated from the `lesson-plans.md` week blocks: promise, featured study/debate, the minute-by-minute flow as a readable table, readings, sketch homework, and the competency check. (These are instructor-facing-ish but fine to publish; they show prospective students the real shape.)
5. `resources.html` — the anchor tools (tokenizer playground, Teachable Machine, Embedding Projector, optional CLIP demo; Week 7 uses the AI assistant itself), the reading list, and links to the notebooks repo.
6. `about.html` — who it's for, cost ($0), the AI-as-tool stance, the showcase.

**Design constraints:** legible body type, generous line length, works on a phone, high contrast, no tracking, no external font CDNs that could fail (system font stack or self-hosted). Run it through the `frontend-design` skill for the styling pass — read `/mnt/skills/public/frontend-design/SKILL.md` first. Keep it calm and editorial, not "edtech landing page."

**Acceptance for the site:** every page renders with JS disabled; all internal links resolve; `index.html` reflects the current title and four-tool framing; weekly pages match the current `lesson-plans.md` (no "Reading at Scale," no transformer-internals week, W6 = "Deepen the Project," W7 = "The AI as a Reader, at Scale"); deployable by pushing `site/` to a `gh-pages` branch or `/docs`.

---

## 3. The two kits (markdown, build first — they're small and unblock the notebooks)

**`kits/common-errors-cheatsheet.md`** — the 6–8 errors a non-coder will actually hit in Colab, each with: what it looks like (the actual traceback's last line), what causes it, and the **exact phrase to paste back to the AI**. Cover: blank/missing API key, rate-limit / quota-exceeded, wrong file path / file not uploaded, empty dataframe (selector matched nothing), `ModuleNotFoundError` (package not installed / wrong name), malformed AI output (asked for JSON, got prose), runtime disconnected / out-of-memory, GPU-not-available. Each entry ≤ 4 lines. This is referenced from Week 1 onward.

**`kits/pivot-kit-corpora.md`** — 10–12 pre-vetted corpus-and-question pairs, each known to yield a finding in the time available, pop-weighted, spanning text and image, each tagged with which of the four tools it suits. Pull candidates from the starter corpora named in `syllabus.md` and the full corpus library in `planning-doc.md`: AITA judgments (HuggingFace Pushshift mirror), TMDb posters, Bluesky firehose; the born-digital fiction sources (Reddit fiction r/nosleep / r/HFY, Royal Road, Gutenberg) for narrative projects; and the new datasets serving the expanded applicant pool — and be honest in the kit about *access friction*, since it varies. The genuine load-with-`read_csv`, no-API-key ones (safest for non-coders) are **Pantheon**, the **Met/MoMA CC0 CSVs**, and a **Billboard-audio-features CSV** (music). The others need a first step the cookbook now teaches: **Million Song Dataset** (HDF5, a short extraction — *not* a flat CSV), **CLICS** (a browsable web map backed by CLDF, best explored in-browser; network-method, not the four-tool path), and **LinCE** (HuggingFace `datasets`, word-level language tags). For each: corpus + access method + the step it needs + a question + the tool. Mark each `(PK)`. **Music projects:** Spotify's audio-features API was deprecated Nov 2024 — use the Billboard CSVs (flat) or the Million Song Dataset (extract first), never live Spotify calls.

---

## 4. Deliverable B — the notebooks, and package compatibility (the crux)

### 4a. What each notebook does (specs in the design docs; summarized here)

- **`week02_counting.ipynb`** — load a small pop-lyrics slice + a subreddit slice + a public-domain novel; build word frequencies and tf-idf with the AI's help; keyness (log-odds distinctive words — the *She Giggles, He Gallops* method) and the shuffle test (permutation check that a counted difference beats chance). Pure stdlib + `pandas` + `scikit-learn` (tf-idf) + `numpy` + `matplotlib`. (Pixel counting lives in week01.)
- **`week03_classification.ipynb`** — load a ~1,000-row pre-labeled pop corpus (lyrics-by-mood or AITA YTA/NTA or reviews pos/neg); train a `LogisticRegression`; **print the signed coefficients** (the lesson); the "most predictive words for a fun corpus" delight beat. `scikit-learn` + `pandas` + `matplotlib`.
- **`week04_data_cookbook.ipynb`** — **three acquisition routes**, worked, in order of how often students need them: **(1) load a prepared file** — `pd.read_csv(url)` for a direct link, `gdown`/`wget` into Drive, `datasets.load_dataset()` for HuggingFace, `unzip` for archives (this is how most starter corpora arrive and the route a beginner most needs — one applicant explicitly couldn't get a GitHub file into a notebook); **(2) an API pull** (Met or Art Institute of Chicago, no key); **(3) a small polite scrape** (`requests` + `beautifulsoup4`) with an inline `robots.txt`/ToS/rate-limit/anti-republish checklist. Also the corpus-existence-proof tool. `requests` + `beautifulsoup4` + `pandas` + `datasets` + `gdown`.
- **`week05_embeddings.ipynb`** (+ GUIDED + SKELETON) — embed a text corpus with `sentence-transformers`; reduce with PCA then t-SNE/UMAP and plot; hunt the surprise cluster; the parallel image path embeds album covers (CLIP image embeddings via `sentence-transformers`' CLIP or `open_clip`). **This is the heaviest notebook and the compatibility hot spot** (see 4c). `sentence-transformers` + `scikit-learn` (PCA/TSNE) + optionally `umap-learn` + `matplotlib`/`plotly`.
- **`week07_annotator.ipynb`** (+ GUIDED + SKELETON) — write a labeling prompt, run it over a slice of the student's corpus via the **Gemini API**, request per-label confidence, sort and spot-check against a small hand-labeled gold set. A natural worked example is **narrative extraction** on a born-digital fiction slice (cause of death across r/HFY sci-fi stories, or horror subgenre on r/nosleep) — the annotator's best showcase. `google-generativeai` + `pandas`. No GPU needed.
- **`cool-methods/`** — optional method starters, built last. Includes the **character-networks** notebook (co-occurrence graph + centrality on a fiction corpus) and the **sentiment-arcs notebook** (`cool-methods/sentiment_arcs.ipynb`) for the narrative projects: score emotion across a story's segments (a sentiment lexicon such as `vaderSentiment`/`nrclex`, or the Gemini API per segment), smooth, and plot the arc. **Reimplement Jockers's Syuzhet method in Python — do not call the R package.** Build the caveat in: a slider for the smoothing window so students watch the arc change shape (the Jockers–Swafford lesson, on the tool in their hands). Also the **fine-tuning notebook** (`cool-methods/finetune_modernbert.ipynb`) — the advanced "third reader," for technically comfortable students only: fine-tune `answerdotai/ModernBERT-base` for sequence classification on the student's *own* labels (the hand-labeled + AI-labeled examples from Weeks 6–7), using Hugging Face `transformers` + `datasets` + the `Trainer` API; save the fine-tuned model to the Drive project folder. Build notes: (1) verify ModernBERT is supported by the installed `transformers` release — early-2025 tutorials installed it from GitHub, but it should be in a stable release now; pin whatever the current Colab-compatible version is. (2) **Do not require `flash-attn`** — it needs Ampere+ and free Colab's T4 is Turing; ModernBERT runs without it, just slower. (3) Keep the dataset small (hundreds to low thousands of rows) so a fine-tune finishes inside a free-tier session, and checkpoint to Drive in case the runtime disconnects — fine-tuning is the most reset-fragile thing in the course, so flag that prominently in the notebook. (4) Narrate heavily and gate it as optional; this notebook assumes more comfort than any other. Plus stylometry, color analysis, diachronic meaning, reception.

Every notebook: first cell is a **Markdown title + what-you'll-do**; first code cell **mounts Google Drive and sets a project-folder path** (so the corpus and outputs persist across resets — the Week-1 ritual, repeated as a one-liner everywhere); next code cell is **`%pip install -q -r requirements.txt`** (or an explicit pinned install — see 4b); imports follow with a one-line "if this fails, see the cheat sheet" note; then narrated steps. Any artifact the student produces (collected corpus, embeddings, labels, charts) **saves to the Drive folder, never to `/content`**. End with a "you made X" cell (the delight payoff) and, for Act-2 versions, the blanked sections.

### 4b. Dependency strategy

Colab ships a large, *moving* preinstalled stack (pandas, numpy, scikit-learn, matplotlib, Pillow, requests are already there and version-current). The risk is the **few packages Colab does not ship or ships at an incompatible version** — chiefly `sentence-transformers`, `open_clip`/`clip`, `umap-learn`, and `google-generativeai` — and the **transitive `numpy` / `torch` / `huggingface_hub` conflicts** they drag in. Colab's preinstalled `numpy` is the usual fault line: a library that demands `numpy<2` (or the reverse) will either fail to import or, worse, import and misbehave.

Strategy:
1. **Lean on Colab's preinstalled stack** for the boring packages — do not pin or reinstall pandas/numpy/scikit-learn/matplotlib/Pillow/requests unless a notebook genuinely needs a version Colab doesn't have. Reinstalling them is how you *create* conflicts.
2. **Pin only the "extra" packages** in `requirements.txt`, with versions chosen to be compatible with Colab's current `numpy`/`torch` at build time. Capture the working versions by freezing *after* a successful run in Colab (`pip freeze`), not by guessing.
3. **Maintain `constraints.txt`** (a pip constraints file) for the handful of hard pins (e.g. a known-good `sentence-transformers` + matching `torch` + `numpy` line). Install with `pip install -r requirements.txt -c constraints.txt` so transitive deps can't drift past the tested ceiling.
4. **Record the Colab base** you tested against — Python version and the preinstalled `numpy`/`torch`/`scikit-learn` versions — in `notebooks/README.md`, with the date. Colab updates its image periodically; this is the "tested as of" stamp.

### 4c. **How to test package compatibility — the harness**

Yes, there is a clean way to test this, and it should be built as part of the deliverable so it can be re-run whenever Colab's image changes. Three layers, cheapest first:

**Layer 1 — local resolver check (fast, catches version-solver conflicts before any execution).**
`tools/check_compat.py` does dependency resolution without running notebooks:
- Run `pip install --dry-run -r requirements.txt -c constraints.txt` (pip ≥ 23 supports `--dry-run` / report JSON) and fail on any conflict.
- Cross-check with `uv pip compile requirements.txt` if `uv` is available — `uv`'s resolver is fast and its error messages name the exact conflicting pins. (`pipdeptree --warn fail` is a good third opinion for already-installed envs.)
- This layer answers "do these pins even have a solution?" and runs in seconds in CI. It will *not* catch numpy-ABI / runtime-import problems — that's layer 2.

**Layer 2 — headless execution in a Colab-like container (catches import-time and runtime breakage).**
`tools/run_notebooks.sh` executes every notebook top-to-bottom without a browser and fails on any cell error:
```bash
pip install nbclient nbconvert jupyter
jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=900 \
  --output-dir _executed notebooks/week*.ipynb
```
or equivalently `nbclient`/`papermill` per notebook. Key points:
- **Match the Colab environment**, don't just use a clean Python. Run this inside the **`us-docker.pkg.dev/colab-images/public/runtime`** Colab base image (Google publishes it) via Docker, so the preinstalled `numpy`/`torch`/Python versions match what students actually get. This is what makes the test *faithful* rather than approximate.
- For notebooks that need the **Gemini API** (Week 7), gate the live-call cells behind an env check (`if os.environ.get("GEMINI_API_KEY")`) and provide a **mocked/cassette path** so the notebook executes end-to-end in CI without a key or network — assert on the parsing/sorting logic, not on the model's words. (A recorded sample response committed as a fixture is enough.)
- For GPU notebooks (embeddings/CLIP), the harness should run on CPU with a **tiny corpus** (10–50 items) so it finishes in CI; keep the full-size run as a separate, manually-triggered Colab check. The point of CI is "imports resolve and the pipeline runs," not "reproduce the T4 timing."

**Layer 3 — the in-notebook smoke test (the student-facing safety net).**
`notebooks/_smoke_test.ipynb` is a single notebook a student or instructor can run in Colab on day one to confirm their runtime is healthy: it imports every package the course uses, prints each version, runs one trivial op per library (embed one sentence, label one string via Gemini if a key is present, open one image, fit a 5-row logistic regression), and prints a green "all systems go" or a specific failure pointing at the cheat-sheet entry. This is also the best living documentation of the working version set — its printed output *is* the "tested as of" record.

### 4d. Compatibility acceptance criteria

- `tools/check_compat.py` exits 0 (resolver finds a solution for the pinned set).
- `tools/run_notebooks.sh` executes **all** notebooks in the Colab base image with **zero cell errors** (Gemini cells mocked, GPU cells on tiny CPU corpus).
- `_smoke_test.ipynb` run in a real Colab free runtime prints all-green, and `notebooks/README.md` records the Colab Python/`numpy`/`torch` versions and the date it passed.
- A second, manual full-size run of `week05_embeddings.ipynb` on a real Colab **T4** completes within the runtime limits (this one can't be CI'd cheaply; do it once by hand and note the wall-clock time so the instructor knows what to expect in class).

---

## 5. Build order (dependencies first, riskiest-compat early)

1. **Repo skeleton + `README.md`** (§1).
2. **`requirements.txt` + `constraints.txt` first cut, and `tools/check_compat.py`** — get the resolver green before writing notebook logic, so you're not debugging pins and pedagogy at once.
3. **`week05_embeddings.ipynb`** *first among notebooks* — it's the heaviest dependency (sentence-transformers + CLIP + dim-reduction) and the compat hot spot. If its stack resolves and runs in the Colab image, the rest are easy. Freeze the working versions back into `requirements.txt`/`constraints.txt`.
4. **`week07_annotator.ipynb`** — the only API-dependent notebook; build the mock/cassette path with it.
5. **`week02`, `week03`, `week04`** — lighter, mostly Colab-preinstalled; quick once the harness exists.
6. **Act-2 GUIDED + SKELETON variants** for W5 and W7 (derive from the worked versions; blank the right cells).
7. **The two kits** (§3) — small, can be done any time; do them before final notebook polish so the "see the cheat sheet" references resolve.
8. **`tools/run_notebooks.sh` + the Colab-image Docker harness** — wire up CI; get all notebooks green.
9. **The site** (§2) — generate from the markdown docs, style with the `frontend-design` skill, verify links and JS-off rendering.
10. **`_smoke_test.ipynb`** — last, since it imports the finished set; run it in real Colab and stamp the README.

Each step: build, run the relevant harness layer, fix, commit. Don't batch — a green check after each notebook is the whole point of having the harness.

---

## 6. Things to get right (failure modes seen in courses like this)

- **Don't reinstall Colab's base packages.** The single most common way to break a Colab notebook is `pip install pandas numpy ...` pulling a version that conflicts with the preinstalled torch/numpy ABI. Install only the extras.
- **Pin from a *successful* freeze, never from memory.** Library versions on PyPI move; a plausible-looking pin can be a phantom. The harness exists precisely so the pins are empirical.
- **Mock the paid API in CI** so the notebooks are testable without a key and without spend, and so a Gemini outage doesn't redden the build.
- **Tiny corpora in CI, full corpora by hand.** Keep automated runs fast; reserve the real T4 timing check for a single manual pass.
- **Notebooks are read by non-coders.** Optimize the code for being *explained*, not for being short. Every code cell gets a plain-language Markdown cell above it.
- **Re-run the harness when Colab updates.** Colab refreshes its image periodically; the README's "tested as of" date is the trigger to re-run `_smoke_test` and re-freeze if anything moved.
- **No transformer-internals notebook.** It was cut from the course; don't helpfully add one.

---

## 7. Definition of done

- `site/` rebuilt, titled *Culture as Data*, generated from the current markdown docs, deploys to GitHub Pages, renders with JS off, all links resolve.
- All notebooks present per §1, fully-worked for Act 1 and worked+GUIDED+SKELETON for the Act-2 ones, each narrated for non-coders, each opening with a pinned install and an imports-with-fallback cell.
- `tools/check_compat.py` green; `tools/run_notebooks.sh` runs every notebook with zero errors in the Colab base image; `_smoke_test.ipynb` all-green in real Colab with the version set + date recorded in `notebooks/README.md`.
- Both kits written and cross-referenced from the notebooks.
- One manual full-size T4 run of the embeddings notebook completed, with wall-clock noted.
- `README.md` explains the repo, how to open notebooks in Colab, the runtime expectations, and how to re-run the compat harness when Colab changes.
