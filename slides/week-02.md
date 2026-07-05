---
title: "Week 2: Counting Is Already a Model"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 2 · Counting Is Already a Model

> Put a famous PNAS paper on trial, find the words that make a voice distinctive (the method behind Week 1's featured study), and learn the one statistics move the course needs: the shuffle test for whether a difference is real.

*Tool / method: Advanced counting: baselines, keyness, and the shuffle test · Competencies: 3, 5, 8*

## Look at This

The Bollen/Schmidt trial: a hockey stick of societal distress, found by counting.

## Question It

The rising words are fiction-words, and Google scanned more fiction after 2000. The rebuttal and the move to steal: the authors removed the entire fiction corpus and re-ran it, and the pattern largely held. The answer to "your corpus is biased" is a test, not an argument.

## Three modes today (about a third each)

- **Lecture / demo:** Advanced counting: baselines, keyness, and the shuffle test
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
- **1:30**  Keyness, the She Giggles, He Gallops move: a log-odds ratio between two corpora finds the words one voice uses far more than a baseline, exactly the method behind Week 1's featured piece. The corpus pair is a choice too: artist vs. pop, lyrics vs. subreddit vs. novel.
- **1:42**  Is the difference real? The shuffle test: shuffle the labels, recount, a thousand times. If chance alone often makes a gap this big, don't trust it; if it almost never does, you have a finding. Real-but-tiny is still tiny.
- **1:50**  Gemini-free check and check-out.

## Reading & homework

- **Reading:** [Wolfram, What Is ChatGPT Doing](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/) (opening sections only)
- **Supplement:** [Zipf's law](https://en.wikipedia.org/wiki/Zipf%27s_law), the straight line in every text
- **Sketch:** Count something in a text you love; one chart; one sentence naming a choice. Comparing two things? Shuffle-test it.
- **Check (AI closed):** Explain it: why two tokenizers split a sentence differently, and what your stemming choice changed. (Competencies 3, 5.)
