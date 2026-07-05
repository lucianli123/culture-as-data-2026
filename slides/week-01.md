---
title: "Week 1: Your First Investigation"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 1 · Your First Investigation

> By the break you'll have loaded a real dataset, asked it a question, and produced your first chart. By the end you'll have counted culture in all three shapes it comes in: rows, words, and pixels.

*Tool / method: Counting: rows, words, pixels · Competencies: 1, 8*

## Look at This

The Pudding, "She Giggles, He Gallops" (2017): across ~2,000 film screenplays, the stage-direction verbs split by gender, women snuggle and giggle, men gallop and stride, and the interactive makes it impossible to unsee.

## Question It

~2,000 screenplays skewed toward what got produced and digitized: is that "film," or a slice? Whose choice is a gendered verb, the writer's, the character's, the genre's? Counting shows the split, not the cause. And read the visualization's choices, not just the data.

## Culture is already data

- Spotify counts your listening; the For You feed is a model reading culture at scale; you are on the receiving end every day.
- In ten weeks you run the same kind of reading yourself, on culture you choose.
- Today's corpus: every NYT wedding announcement 1985-2014 (~500 rows): who married whom, and whether the bride kept her name.
- The deliverable, shown now: a published web essay on top of a notebook anyone can run.

## Four words, used all term

- Corpus: the pile you study. 500 announcements, 2,000 screenplays, 10,000 album covers.
- Method: the counting or weighting you run on the corpus.
- Model: any simplification that turns culture into numbers. A word count is already one.
- Embedding: a few hundred numbers that place an item on a map of meaning. Week 5.

## The Drive ritual (every week, no exceptions)

- Colab wipes its machine when you idle. Your mounted Drive folder is what survives.
- Copy the notebook to Drive, mount Drive, save everything to the one project folder.
- Your Week-4 corpus has to be alive in Week 5. This ritual is how.
- Gemini key goes in Colab Secrets. Never pasted into code.

## When code errors (it will, today, on purpose)

- Read the LAST line of the traceback first. It names the problem.
- Paste it to the AI: "this errored, fix it and tell me what went wrong."
- Try twice. Then ask a human. That order.
- Keep the cheat sheet out. Nobody memorizes error messages; everybody reads them.

## Counting, three shapes

- Rows: what share of brides kept their name, year by year. One groupby, one chart.
- Words: the top words of a lyric are "the, and, you" until you remove stop-words. That removal is your first modeling choice.
- Pixels: rank 200 Met thumbnails darkest to brightest from average luminance.
- Same move three times, and a decision hiding in each.

## Three modes today (about a third each)

- **Lecture / demo:** Counting: rows, words, pixels
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Setting the room: the social rules, demonstrated by the instructor breaking one and being corrected. Today's live coding includes real mistakes on purpose.
- **0:12**  Look at This, then Question It: She Giggles, He Gallops.
- **0:17**  Pre-train the vocabulary (no code): corpus, method, model, embedding, in plain language with pictures. The course map and the deliverable.
- **0:32**  Lab 1 (worked, participatory): copy the notebook to Drive and mount Drive into the runtime (this is how your corpus and results survive Colab wiping the session, everything saving to one project folder), put a Gemini key in Colab Secrets, load NYT wedding data, make a first chart. Hand out the common-errors cheat sheet. Then solo with a partner: draft three questions, pick one, have the AI write the code, run it, chart it. Write one sentence predicting your cell before you run it.
- **1:10**  Break
- **1:20**  Lab 2 (worked), count words, then pixels: first the top words of a small lyrics slice (stop-words drown the list until you remove them, your first counting choice), then an image corpus, ~200 Met thumbnails ranked darkest to brightest by average brightness. Text and pictures, counted with the same move; image projects start here.
- **1:50**  Teaser of the ladder ahead; the standing rituals named. First check-out.

## Reading & homework

- **Reading:** [Bollen et al., the cognitive-distortions hockey stick (PNAS 2021)](https://www.pnas.org/doi/10.1073/pnas.2102061118), with the [Schmidt et al. critique](https://www.pnas.org/doi/10.1073/pnas.2115010118)
- **Supplement:** [Robin Sloan, Writing with the machine](https://www.robinsloan.com/notes/writing-with-the-machine/)
- **Sketch:** One question from your life answerable with text or image data; three sentences.
- **Check (AI closed):** Trace it: one written sentence predicting what your cell does before you run it. (Competency 1.)
