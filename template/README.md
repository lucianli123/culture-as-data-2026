# Publishing template

The web-essay template every project forks in Week 4 and fills in Week 9. It renders a
single-page essay with Quarto and deploys to GitHub Pages. Static by default: no
JavaScript unless you opt in at the Week 9 code-review checkpoint.

## Fork it (Week 4, five minutes)

1. Create a new GitHub repository for your project (public).
2. Copy the two files in this folder (`_quarto.yml`, `index.qmd`) into it.
3. Commit. Your project repository now exists; leave it until Week 9.

## Fill and deploy (Week 9)

1. Replace every bracketed placeholder in `index.qmd` with your material.
2. Render locally or in Colab: `quarto render` (output lands in `docs/`).
3. Commit `docs/`, then in your repository's Settings → Pages choose
   **Deploy from a branch**, branch `main`, folder `/docs`.
4. Your essay is live at `https://<username>.github.io/<repository>/` within minutes.

The essay is the communication layer; the analysis lives in your notebook. The course
standard for the notebook is Mullen's: *the instructor must be able to run it.* Link the
notebook prominently; the essay's claims are only as good as the notebook behind them.
