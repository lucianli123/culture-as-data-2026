---
title: "Week 2: Counting Is Already a Model"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 2 · Counting Is Already a Model

> Put a famous PNAS paper on trial, build a word-counter by hand, watch the same sentence get counted three ways, and find an artist's signature vocabulary with nothing but counting.

*Tool / method: Counting, and every count hides a choice · Competencies: 3, 5, 8*

## Look at This

The Bollen/Schmidt trial: a hockey stick of societal distress, found by counting.

## Question It

The rising words are fiction-words, and Google scanned more fiction after 2000. The rebuttal and the move to steal: the authors removed the entire fiction corpus and re-ran it, and the pattern largely held. The answer to "your corpus is biased" is a test, not an argument.

## Three modes today (about a third each)

- **Lecture / demo:** Counting, and every count hides a choice
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Warm-up retrieval.
- **0:05**  The trial: claim, objection, re-run-without-fiction rebuttal, "interpret with care." One named choice is the chart: the hockey-stick shape depends on its y-axis and smoothing.
- **0:25**  Delight beat: an artist's signature vocabulary, the words they use far more than a pop baseline. No caveats.
- **0:30**  Hand-built bag-of-words: two authors, highlighters, argue about merging run/running. Counting requires defining.
- **0:55**  What counts as a word? Paste a sentence into two tokenizer playgrounds and watch it shatter differently. Models see tokens, not words.
- **1:05**  Break
- **1:15**  tf-idf: the AI scales your hand count; stop-words dominate, which motivates "common here, rare overall."
- **1:30**  Cross-corpus counting: the same counter on a lyrics slice, a subreddit, and a novel. The corpus choice changes what "common" means.
- **1:50**  Gemini-free check and check-out.

## Reading & homework

- **Reading:** [Wolfram, What Is ChatGPT Doing](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/) (opening sections only)
- **Supplement:** [Zipf's law](https://en.wikipedia.org/wiki/Zipf%27s_law), the straight line in every text
- **Sketch:** Count something in a text you love; one chart; one sentence naming a choice you made.
- **Check (AI closed):** Explain it: why two tokenizers split a sentence differently, and what your stemming choice changed. (Competencies 3, 5.)
