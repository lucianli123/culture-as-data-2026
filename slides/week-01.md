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

## Course logistics

- Ten sessions, two hours each, in three parts every week: lecture and demonstration, hands-on workshop, and discussion, roughly a third each.
- Bring a laptop. You need a Google account (Colab and Drive, where all work lives) and a GitHub account (where your essay publishes); both are free, and the course costs nothing.
- The weekly rhythm: a short reading before each session, a small sketch after it, and a five-minute check with the AI closed. All materials live on the course site.
- Icebreaker, one fast round: your name, one piece of culture you kept returning to this year, and one number about it you wish you knew. Keep your answer; it is a first draft of a project question.
- The course ends in a public showcase, friends and family invited, your finding at a live URL.

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

## What is data? A CSV, and Drucker's caveat

- Data is anything made countable. The making is the part to watch.
- A CSV: one row per thing, one column per recorded fact. Ours: one row per painting, one column per fact the Met records.
- Drucker: data ("the given") is the wrong word. Capta, "the taken," is honest.
- The columns are choices: the artist's name but not the sitter's; a free-text date. Absence is a decision too.
- Pairs, two minutes: what did the catalogers take, and what did they leave?

## Quantification has a literature (the theory shelf, never required)

- Porter, Trust in Numbers (1995): quantification is a technology of distance - numbers travel where personal trust cannot, which is why institutions demand them.
- Bowker and Star, Sorting Things Out (1999): every classification makes some things visible and others invisible; categories have politics, including the columns of a museum catalog.
- Gitelman (ed.), 'Raw Data' Is an Oxymoron (2013): there is no raw data - collection, cleaning, and framing cook it before you arrive.
- Scott, Seeing Like a State (1998): counting makes the world legible to power, and the counting remakes the world to be more countable.
- Drucker's capta (the Week 1 supplement) is the door into this shelf; D'Ignazio and Klein's Data Feminism (open access) runs under the whole course. None of it is required; all of it is where the course's habits come from.

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

## Bags of words, bags of pixels, and what they miss

- What counts as red? A boundary you set on the hue wheel. Shift it twenty degrees and paintings change category without changing a pixel: defining the ranges is the analysis, the same decision as the stop-word list.
- Two sentences with identical word-bags can mean opposite things: "the critics loved it, the public did not" and its reversal count the same.
- The centerpiece: Sonnet 130's bag is a catalogue of praise - sun, coral, roses, snow, music, goddess. The poem negates every item ("my mistress' eyes are nothing like the sun"). The count reads a love poem; Shakespeare wrote a satire of love poems.
- The manifest's date column reads "ca. 1520" and "1530s". Force it to numbers and pandas quietly turns those into NaN, and mean() skips NaN without telling you: the average drops half the paintings, the older half. Count your NaN before you average.
- The loss is the trade counting makes for scale. Name it on day one; Week 5's embeddings exist to recover some of it.

## Deep-research tools: one role, four rules

- AI deep-research tools browse for an hour and return a long, cited report. In this course they have exactly one role: the scout, finding datasets and prior work before Week 4's commitment.
- Rule one: every citation is a lead, not a source. Reports cite real, wrong, and nonexistent works with identical confidence; nothing enters your work unread.
- Rule two: verify dataset access yourself. "Publicly available" in a report means someone once said so; the corpus-existence proof (50 loadable rows, Week 3's sketch) is the standard.
- Rule three: the report is never a source. Cite what you read, not the tool that found it.
- Rule four: scout, then close the tool. Your question, your reading, and your interpretation cannot be delegated - the same boundary as with code.

## Counting, three shapes

- Rows: a manifest of paintings, downloaded live and ranked in one pipeline.
- Words: the top words of 154 sonnets are thy and thou until the stop list learns Early Modern English; then love (195 times), beauty, and time surface. The stop list must fit the corpus, and it is your choice.
- Pixels: the paintings themselves, ranked darkest to brightest from average luminance.
- One technique, three shapes, a decision hiding in each.

## Three modes today (about a third each)

- **Lecture / demo:** Counting: rows, words, pixels
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Logistics, working agreements, and a one-round icebreaker: your name, one piece of culture you kept returning to this year, and one number about it you wish you knew. Today's live coding deliberately includes real mistakes.
- **0:10**  Lecture, the stakes: machines already read culture at scale, the feed ranking what you see, the moderation filter, the model trained on scraped art and prose, and that reading happens without you. Counting culture has produced real knowledge (the screenplay verb split, the gendered language in 14 million teaching reviews, the Rowling unmasking, pop music's 1991 revolution) and real mistakes, and both look identical until someone checks. In ten weeks you do the reading yourself and publish something checkable.
- **0:28**  Look at This, then Question It: She Giggles, He Gallops.
- **0:35**  The vocabulary and the map (no code): corpus, method, model, embedding, plus what data itself is. A CSV, anatomized on screen using the painting manifest (rows are paintings, columns are what the Met chose to record), and Drucker's correction: data is capta, taken not given. Two minutes in pairs: what did the catalogers take, and what did they leave out? The deliverable, shown: a web essay on a runnable notebook.
- **0:47**  Lab 1 (worked, participatory): copy the notebook to Drive and mount Drive (this is how work survives Colab wiping the session), Gemini key into Colab Secrets, then load the 154 sonnets and make a first chart: love across the sequence. Count the whole corpus three ways, one bar chart per stop list, and watch the answer change; then count word pairs, the first n-grams (She Giggles is a bigram count). Then the AI loop, solo: ask, predict, run, interrogate. The error drill lands here, cheat sheet in hand.
- **1:20**  Break
- **1:30**  Lab 2 (worked): count pixels. The manifest is the first CSV (rows are paintings, columns are the Met's choices); a dozen paintings download live from the Met API and rank darkest to brightest in a grid, and the corpus palette is a bar chart of defined color ranges. The manifest's messy dates set the missing-data trap: forced to numbers, half become NaN, and the average quietly drops the older half of the corpus. The after-class half, the boundary experiment and Sonnet 130's bag against the poem itself, is this week's guided homework. Image projects begin here.
- **1:52**  Preview of the methods ahead; the weekly routines introduced. First check-out.

## Reading & homework

- **Reading:** [Bollen et al., the cognitive-distortions hockey stick (PNAS 2021)](https://www.pnas.org/doi/10.1073/pnas.2102061118), with the [Schmidt et al. critique](https://www.pnas.org/doi/10.1073/pnas.2115010118)
- **Supplement:** [Robin Sloan, Writing with the machine](https://www.robinsloan.com/notes/writing-with-the-machine/); [Drucker, Humanities Approaches to Graphical Display (DHQ 2011)](http://www.digitalhumanities.org/dhq/vol/5/1/000091/000091.html), the case that all data is capta
- **Deeper (optional):** [Moretti, Conjectures on World Literature (NLR 2000)](https://newleftreview.org/issues/ii1/articles/franco-moretti-conjectures-on-world-literature), the founding argument for reading culture at scale
- **Sketch:** A favorite Pudding piece and what it counted; the question from your life it inspires; the notebook's after-class half (~20 minutes).
- **Check (AI closed):** Trace it: one written sentence predicting what your cell does before you run it. (Competency 1.)
