# Weekly slide decks (drafts)

One draft deck per week, in Markdown. They open as plain outlines anywhere, and render to
real slides with no extra work.

## What's here

`week-01.md` to `week-10.md`, each deck: the promise, the Look-at-This study (admire +
interrogate), the three-mode split for the session, the minute-by-minute flow, and the
reading + homework + AI-closed check.

## Present them

- **Quarto (matches the course toolchain):** `quarto render slides/week-05.md` produces a
  reveal.js HTML deck. `quarto preview` for live editing.
- **VS Code:** the "vscode-reveal" extension previews these directly.
- **PowerPoint / Google Slides:** styled `.pptx` decks are pre-built in `slides/pptx/` (see below).

## Note

These are **drafts** generated from the course data. Refine each against `design/lesson-plans.md`,
which has the full minute-by-minute flow with the [Lecture]/[Workshop]/[Discussion] tags and the
per-week mode balance. Add screenshots of the featured study to the Look-at-This slide before teaching.

## PowerPoint versions

Styled `.pptx` decks live in `slides/pptx/` (open in PowerPoint, Keynote, or Google Slides).
They use the site's palette (terracotta, forest, gold), a repeated dot motif, a three-card
"three modes" slide, and a timeline, built with pptxgenjs rather than a plain converter.

Regenerate after editing the course content:

```bash
npm install pptxgenjs        # once
bash slides/render_pptx.sh   # refreshes slides.json from the site data, then renders pptx/
```

`slides.json` (the deck content) is exported from `tools/build_site.py` by
`slides/export_slides.py`, so the decks, the site, and the design docs stay in step.
The Markdown decks remain the lightweight outline; `slides/styled_pptx.js` builds the styled
PowerPoint from the same content.

## The hand-built lecture drafts

Two weeks have a fuller, hand-written teaching deck alongside the generated one, with figures
drawn from live data rather than bullets alone:

| Deck | Built by | Figures |
|---|---|---|
| `week-02-lecture-draft.pptx` | `week02_deck_build.js` | the Bollen trial, shuffle test, bootstrap, replication |
| `week-03-lecture-draft.pptx` | `week03_figs.py` → `week03_deck_build.js` | logistic regression: the sigmoid, the overlap in 2-D, baseline vs. model, the confusion matrix, over-fitting as C rises, the learning curve, the signed weights |

Week 3 is a two-step build, because the deck prints the numbers the figures were made from:

```bash
python3 slides/week03_figs.py       # fits the models, writes PNGs + week03_figs.json to $FIG_DIR (default /tmp/figs)
node slides/week03_deck_build.js    # reads both, writes slides/week-03-lecture-draft.pptx
```

The corpus is pulled live (two subreddits, falling back to two novels offline), so the committed
`.pptx` is a snapshot of one run and the accuracies move a point or two when you re-run it.
**Re-run both before teaching** so the slides match what the room will see in the notebook.
Figure colors are the course palette stepped up in chroma, so the two-series pairs clear the
colorblind-separation and chroma floors.