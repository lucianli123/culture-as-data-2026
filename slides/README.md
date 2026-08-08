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
| `week-04-lecture-draft.pptx` | `week04_figs.py` → `week04_deck_build.js` | 23 figures on 32 slides: five cropped from the week's reading (Garg et al.), plus a neuron, a network beside the readable weights it costs you, gradient descent, the spiral fitted twice, one-hot against dense vectors, the contrastive pull-and-push and the similarity blocks it produces, neighbours and a 2-D map from vectors trained on the repo's two novels, a convolution worked out number by number, a filter bank and a three-layer stack on a Met painting, CLIP as the same pull and push on picture-caption pairs, and then the collecting half: a live request and reply with the pagination block called out, the same JSON beside the table it becomes, the Art Institute and the Met drawn side by side to show one API handing you rows and the other handing you ID numbers, one quote block of real HTML with its three selectors marked, and what a one-second pause costs across 5,000 pages |

Weeks 3 and 4 are two-step builds, because each deck prints the numbers its figures were made from:

```bash
python3 slides/week03_figs.py       # fits the models, writes PNGs + week03_figs.json to $FIG_DIR (default /tmp/figs)
node slides/week03_deck_build.js    # reads both, writes slides/week-03-lecture-draft.pptx

python3 slides/week04_figs.py       # ~2 min: fits the spiral, trains word vectors contrastively on the two novels, convolves a Met painting, and calls the Art Institute, Met and quotes.toscrape endpoints live
node slides/week04_deck_build.js    # writes slides/week-04-lecture-draft.pptx
```

**Figures from the reading.** `week04_figs.py` downloads the arXiv preprint of Garg et al. 2018
(arXiv:1711.08412) at build time and crops five figures out of it — the century curve, the
census validation, the adjectives by decade, the occupations by group, and the decade
correlation matrix. The images are not
stored in this repo; the build fetches them, and every slide that uses one carries the citation
and a "shown for teaching" line. If the download fails, those slides render without the picture
rather than breaking the build.

The corpus is pulled live (two subreddits, falling back to two novels offline), so the committed
`.pptx` is a snapshot of one run and the accuracies move a point or two when you re-run it.
**Re-run both before teaching** so the slides match what the room will see in the notebook.
Figure colors are the course palette stepped up in chroma, so the two-series pairs clear the
colorblind-separation and chroma floors.