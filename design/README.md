# Culture as Data — Course Project

This folder is the complete, self-contained specification for **Culture as Data**, a 10-week, 2-hour-per-session community course that teaches curious adults (no coding prerequisite) to investigate cultural data — lyrics, art, fan fiction, Reddit, images — at scale, with an AI assistant writing the code as plumbing rather than as the subject.

The course **design is finished and authoritative.** The buildable artifacts it specifies — the **Colab notebooks** and the static **course site** — are now built and live in this repository (`notebooks/`, `docs/`, `slides/`); this folder remains the spec they are checked against (`tools/check_sync.py` fails CI when the generators drift from these docs).

---

## Start here

**Read `BUILD-PLAN.md` first.** It is the entry point and the index over everything else: it explains what to build, in what order, how to verify it (especially the package-compatibility harness, which is the part most likely to break silently), and how each of the other documents feeds the build.

The four design docs are the **source of truth**. If anything in `BUILD-PLAN.md` ever seems to conflict with them, the design docs win.

---

## What's in this project

| File | What it is | Used for |
|---|---|---|
| `BUILD-PLAN.md` | The implementation brief and index | The buildable spec: repo layout, the two deliverables, build order, the compatibility harness, the definition of done |
| `overview.md` | The front door | The site's home + about pages: the hook, the one-sentence pitch, what students make, who it's for |
| `syllabus.md` | The student-facing course | The site's syllabus + schedule: shape of the course, the eight competencies, the deliverable, setup, starter corpora |
| `lesson-plans.md` | The instructor teach-from doc | The weekly pages **and** the per-notebook behavioral spec — each lab's minute-by-minute sequence, datasets, and checks |
| `planning-doc.md` | The instructor companion | The *why* behind every choice (numbered Principles), the assessment framework, the environment/persistence/tooling decision, the corpus library, and the source for the two kits (the common-errors cheat sheet and the pivot-kit fallback corpora) |

---

## The non-negotiables, at a glance

(Full detail in `BUILD-PLAN.md` §0 and `planning-doc.md`. If you read nothing else before building, read these.)

- **The four tools (the spine):** counting (Week 2) → classification (Week 3) → embeddings (Week 5, the heart) → AI-annotation (Week 7). Images are a **co-equal** corpus taught through the same four tools. Networks and sentiment arcs (Syuzhet, reimplemented in Python) are **optional** methods for the projects that fit them. There is **no transformer-internals content** — it was deliberately cut; do not build it.
- **Environment:** Google **Colab free tier + Google Drive**. The runtime is ephemeral, so **persistence is designed in** — every notebook mounts Drive and saves the corpus and outputs to a project folder that survives resets and carries week to week (the Week-1 ritual). **Kaggle** is the documented fallback for students Colab keeps disconnecting.
- **Cost:** **$0 per student.** In-notebook code help is **Colab's built-in Gemini** (keeps code visible); Claude/ChatGPT work the same for students who prefer them. A free **Gemini API key** is needed only for the Week-7 annotation pipeline. Full autonomous agents are for *building this course*, not for students.
- **Audience:** curious adults, most with little or no coding. Notebook code is **read by non-coders**, so optimize it for being *explained*, not for being short; every code cell gets a plain-language Markdown cell above it.
- **Notebook pedagogy:** Act 1 (Weeks 1–3) ships fully-worked notebooks; Act 2 (Weeks 4–7) ships **completion problems** in two parallel versions (fuller-guidance and skeleton). This is required.

---

## How to use this project

**In Claude Cowork:** extract this folder into your workspace, open `BUILD-PLAN.md`, and follow the build order in §5. Work artifact-by-artifact — build a notebook, run it for real, read the traceback, fix, re-run, commit, then move on. The notebooks can only be verified by execution; do not assume code is correct because it looks correct (that's the course's whole thesis). For the compatibility harness, use the published Colab Docker image rather than a clean local Python, so the test matches the environment students actually get.

**In a Claude Project:** add these files to the project's knowledge. `BUILD-PLAN.md` is the document to point any new session at first.

---

## Current status

- **Design docs:** final and internally consistent (four-tool spine; images co-equal; networks and Syuzhet sentiment arcs optional; no transformer week; data-ethics-of-training-data promoted into Week 7's annotator thread and Week 8; persistence and tooling decided and written in; born-digital fiction corpora for the narrative projects).
- **Notebooks:** not yet built — this is the highest-leverage next step. The core notebooks are Week 2 (counting + pixels), Week 3 (classifier), Week 4 (data-collection cookbook), Week 5 (embeddings, text + images — the heaviest, and the compatibility hot spot), and Week 7 (the annotator), plus the Act-2 guided/skeleton variants and the optional `cool-methods/` starters (character networks, sentiment arcs). Per-notebook outlines are in `BUILD-PLAN.md` §4a.
- **Site:** an earlier `site/` exists but is several design generations stale (it still carries an old title). `BUILD-PLAN.md` §2 says to **rebuild from the current markdown, not patch.** That stale site is not included here to avoid any temptation to edit it; it can be supplied separately as reference if wanted.
