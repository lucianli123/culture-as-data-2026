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
- **PowerPoint / Google Slides:** `pandoc slides/week-05.md -o week-05.pptx` converts to PPTX.

## Note

These are **drafts** generated from the course data. Refine each against `design/lesson-plans.md`,
which has the full minute-by-minute flow with the [Lecture]/[Workshop]/[Discussion] tags and the
per-week mode balance. Add screenshots of the featured study to the Look-at-This slide before teaching.

## PowerPoint versions

Pre-rendered `.pptx` decks live in `slides/pptx/` (open in PowerPoint, Keynote, or Google
Slides). To regenerate them after editing a Markdown deck, run `bash slides/render_pptx.sh`
(needs pandoc). The Markdown files stay the source of truth; the `.pptx` files are generated.
