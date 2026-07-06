---
title: "Week 2: Counting Is Already a Model"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 2 · Counting Is Already a Model

> Put a famous PNAS paper on trial, find the words that make a voice distinctive (the method behind Week 1's featured study), and learn the one statistical method the course requires: the shuffle test, which checks whether a difference is real.

*Tool / method: Advanced counting: baselines, keyness, and the shuffle test · Competencies: 3, 5, 8*

## Look at This

The Bollen/Schmidt trial: a hockey stick of societal distress, found by counting.

## Question It

The rising words are fiction-words, and Google scanned more fiction after 2000. The rebuttal, and the method worth adopting: the authors removed the entire fiction corpus and re-ran it, and the pattern largely held. The answer to "your corpus is biased" is a test, not an argument.

## The trial: Bollen et al. v. Schmidt

- The claim (PNAS 2021): phrases of distorted thinking ("I am a failure," "everyone hates me") surge in Google Books after 2000. A hockey stick.
- The objection: Google scanned more fiction after 2000. Maybe the surge is novels, not distress.
- The rebuttal: the authors deleted the entire fiction corpus and re-ran the analysis. The pattern largely held.
- The method worth adopting: answer "your corpus is biased" with a test rather than an argument.

## What counts as a word?

- Two tokenizers shatter the same sentence differently: "don't" becomes one chip, two, or three.
- Models never see words. They see tokens, and the split is a design decision.
- Your hand-count argument about run/running is the same decision, made with highlighters.
- tf-idf: down-weight what is common everywhere. "Common here, rare overall" is what characterizes a text.

## Keyness: what makes a voice distinctive

- For every word: how much likelier is it in corpus A than corpus B? A log-odds ratio, smoothed so rare words don't explode.
- Strongly positive = distinctively A. Strongly negative = distinctively B. The middle is shared language.
- She Giggles, He Gallops is exactly this method: verbs after "she" vs. "he" in 2,000 screenplays. Women snuggle, giggle, squeal; men gallop, strap, shoot.
- The corpus pair is a choice: this artist against pop, this subreddit against a novel. Different pair, different "distinctive."

## The shuffle test: is the gap real?

- The question: could randomly dealt labels produce a gap this large?
- Shuffle the labels, recount, 1,000 times. Mark where the real gap lands in that pile.
- Chance rarely matches it: a finding. Chance matches it often: a coincidence.
- It says "probably not chance." It never says "big enough to matter." Effect size is your argument to make.

## Three modes today (about a third each)

- **Lecture / demo:** Advanced counting: baselines, keyness, and the shuffle test
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Warm-up retrieval.
- **0:05**  The trial: claim, objection, re-run-without-fiction rebuttal, "interpret with care." One named choice is the chart: the hockey-stick shape depends on its y-axis and smoothing.
- **0:25**  A brief demonstration before the complications: the words one artist uses far more than everyone else, a signature vocabulary measured against a pop baseline.
- **0:30**  Hand-built bag-of-words: two authors, highlighters, argue about merging run/running. Counting requires defining.
- **0:55**  What counts as a word? Paste a sentence into two tokenizer playgrounds and watch it shatter differently. Models see tokens, not words.
- **1:05**  Break
- **1:15**  tf-idf: the AI scales your hand count; stop-words dominate, which motivates "common here, rare overall."
- **1:30**  Keyness, the She Giggles, He Gallops move: a log-odds ratio between two corpora finds the words one voice uses far more than a baseline, exactly the method behind Week 1's featured piece. The corpus pair is a choice too: artist vs. pop, lyrics vs. subreddit vs. novel.
- **1:42**  Is the difference real? The shuffle test: shuffle the labels and recount, one thousand times. If chance alone frequently produces a gap this large, the difference should not be trusted; if it almost never does, the finding stands. A difference can be real and still small.
- **1:50**  Gemini-free check and check-out.

## Reading & homework

- **Reading:** [Wolfram, What Is ChatGPT Doing](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/) (opening sections only)
- **Supplement:** [Zipf's law](https://en.wikipedia.org/wiki/Zipf%27s_law), the straight line in every text
- **Sketch:** Count something in a text you care about; one chart; one sentence naming a choice. If the count compares two things, shuffle-test the gap.
- **Check (AI closed):** Explain it: why two tokenizers split a sentence differently, and what your stemming choice changed. (Competencies 3, 5.)
