---
title: "Week 1: Your First Investigation"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 1 · Your First Investigation

> By the mid-session break you will have loaded a real dataset, asked a question of it, and produced a chart. By the end you will have counted culture in three forms: rows, words, and pixels.

*Tool / method: Counting: rows, words, pixels · Competencies: 1, 8*

## Look at This

The Pudding, "She Giggles, He Gallops" (2017): across ~2,000 film screenplays, the stage-direction verbs split by gender, women snuggle and giggle, men gallop and stride. The interactive presentation makes the pattern unmistakable.

## Question It

The 2,000 screenplays skew toward what was produced and digitized: is that "film," or a sample of it? Whose choice is a gendered verb: the writer's, the character's, or the genre's? Counting shows the split, not the cause. The visualization's own choices deserve the same scrutiny as the data.

## Why this course: the stakes

- Machines already read culture at scale: the feed ranking what you see, the moderation filter, the model trained on scraped art and prose. That reading shapes which culture reaches you, and it happens without you.
- Reading culture with machines produces real knowledge and real mistakes, and the two look identical until someone checks. Learning to check is the course.
- Ten weeks from now, you do the reading: a question you chose, a corpus you built, a published finding anyone can verify.
- The whole method in one sentence: it is all counting and weighting, and you can learn to read both.

## What counting culture has found

- In the stage directions of 2,000 film scripts: women snuggle, giggle, and sob; men strap, gallop, and kill. 85% of the screenwriters were men (The Pudding, 2017).
- Across 17,000 Hot 100 songs, the biggest revolution in American pop was not the Beatles in 1964; it was hip-hop in 1991 (Mauch et al., 2015).
- Counting small words like 'the' and 'of' unmasked Robert Galbraith as J.K. Rowling within days (Juola, 2013).
- A model trained on Google News completes 'man is to computer programmer as woman is to...' with 'homemaker' (Bolukbasi et al., 2016).
- An AI portrait sold at Christie's for $432,500; the training data was other people's paintings (2018). Every one of these is a count, and every one has arguable choices. Both halves are the course.

## Four words, used all term

- Corpus: the pile you study. 500 announcements, 2,000 screenplays, 10,000 album covers.
- Method: the counting or weighting you run on the corpus.
- Model: any simplification that turns culture into numbers. A word count is already one.
- Embedding: a few hundred numbers that place an item on a map of meaning. Week 5.

## The Drive routine (every week, without exception)

- Colab wipes its machine when you idle. Your mounted Drive folder is what survives.
- Copy the notebook to Drive, mount Drive, save everything to the one project folder.
- Your Week-4 corpus has to be alive in Week 5. This ritual is how.
- Gemini key goes in Colab Secrets. Never pasted into code.

## When code fails (it will, today, deliberately)

- Read the last line of the traceback first. It names the problem.
- Paste it to the AI: "this errored, fix it and tell me what went wrong."
- Try twice, then ask a human. In that order.
- Keep the cheat sheet at hand. No one memorizes error messages; everyone reads them.

## Defining a color, and what every bag loses

- What counts as red? A boundary you set on the hue wheel. Shift it twenty degrees and paintings change category without changing a pixel: defining the ranges is the analysis, the same decision as the stop-word list.
- Two sentences with identical word-bags can mean opposite things: "the critics loved it, the public did not" and its reversal count the same. Order, negation, and who-did-what are the casualties.
- A painting and its shuffled pixels share the brightness, the average color, and the palette. Composition is to images what word order is to sentences.
- The loss is the trade counting makes for scale. Name it on day one; Week 5's embeddings exist to recover some of it.

## Counting, three shapes

- Rows: what share of brides kept their name, year by year. One groupby, one chart.
- Words: the top words of a lyric are "the, and, you" until you remove stop-words. That removal is your first modeling choice.
- Pixels: rank 200 Met thumbnails darkest to brightest from average luminance.
- The same technique three times, each containing a decision.

## Three modes today (about a third each)

- **Lecture / demo:** Counting: rows, words, pixels
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Introductions and working agreements, demonstrated in practice. Today's live coding deliberately includes real mistakes.
- **0:10**  Lecture, the stakes: machines already read culture at scale, the feed ranking what you see, the moderation filter, the model trained on scraped art and prose, and that reading happens without you. Counting culture has produced real knowledge (the screenplay verb split, the Rowling unmasking, pop music's 1991 revolution) and real mistakes, and both look identical until someone checks. In ten weeks you do the reading yourself and publish something checkable.
- **0:28**  Look at This, then Question It: She Giggles, He Gallops.
- **0:35**  The vocabulary and the map (no code): corpus, method, model, embedding, in plain language with pictures. The deliverable, shown: a web essay on a runnable notebook.
- **0:47**  Lab 1 (worked, participatory): copy the notebook to Drive and mount Drive into the runtime (this is how your corpus and results survive Colab wiping the session, everything saving to one project folder), put a Gemini key in Colab Secrets, load NYT wedding data, make a first chart. Hand out the common-errors cheat sheet. Then solo with a partner: draft three questions, pick one, have the AI write the code, run it, chart it. Write one sentence predicting your cell before you run it.
- **1:20**  Break
- **1:30**  Lab 2 (worked): count words, then pixels. The real headlines' top words (stop-words dominate until removed, the first counting decision), then the Met image corpus: brightness ranking, defined color ranges and the corpus palette (what counts as red is a boundary you set), and the closing demonstration of what every bag throws away, identical word-bags with opposite meanings and a painting beside its shuffled pixels. Image projects begin here.
- **1:52**  Preview of the methods ahead; the weekly routines introduced. First check-out.

## Reading & homework

- **Reading:** [Bollen et al., the cognitive-distortions hockey stick (PNAS 2021)](https://www.pnas.org/doi/10.1073/pnas.2102061118), with the [Schmidt et al. critique](https://www.pnas.org/doi/10.1073/pnas.2115010118)
- **Supplement:** [Robin Sloan, Writing with the machine](https://www.robinsloan.com/notes/writing-with-the-machine/)
- **Deeper (optional):** [Moretti, Conjectures on World Literature (NLR 2000)](https://newleftreview.org/issues/ii1/articles/franco-moretti-conjectures-on-world-literature), the founding argument for reading culture at scale
- **Sketch:** One question from your life answerable with text or image data; three sentences.
- **Check (AI closed):** Trace it: one written sentence predicting what your cell does before you run it. (Competency 1.)
