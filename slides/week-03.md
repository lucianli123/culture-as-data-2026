---
title: "Week 3: Classification: Counting with Weights"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 3 · Classification: Counting with Weights

> Teach a machine a bias in ten minutes, build a classifier and read its mind, and preview the full methods menu before next week's commitment.

*Tool / method: Classification. Train a reader and read what it learned · Competencies: 2, 4, 5*

## Look at This

Lincoln Mullen, America's Public Bible (2023), a classifier that finds biblical quotations across millions of newspaper pages.

## Question It

What counts as a quotation, a four-word echo, a loose paraphrase?, is a definition the scholar chose, and it shapes every result. The model reads the same messy digitized text your own project will.

## Three modes today (about a third each)

- **Lecture / demo:** Classification. Train a reader and read what it learned
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Warm-up + Look at This: Mullen's America's Public Bible.
- **0:10**  Teachable Machine, instructor demo: a two-class image model trained live, then the reveal that it learned from only orange cats and brown dogs. The room predicts what a black cat will do, then sees it.
- **0:22**  Counting with weights, the lab: each word casts a weighted vote; a logistic regression adds them up. Train it on a pop corpus, then read the signed coefficients, its mind on the table.
- **0:52**  Delight beat: the words that most predict "breakup song" or "this reviewer hated it."
- **0:57**  One-line bridge: that classifier is a neuron; stack many for a neural net, which is what's inside the Week 7 model. A quick TensorFlow Playground glance.
- **1:00**  Break
- **1:10**  Methods menu preview, so Week 4's choice is informed: counting, classification, embeddings (Week 5), and optional approaches (character networks for fiction; sentiment arcs for story projects, Jockers's Syuzhet reproducible in Python, whose own smoothing controversy is the built-in lesson to doubt the shape; CLIP image search for visual projects; and, for the technically comfortable, fine-tuning a small open model, ModernBERT, on your own labels).
- **1:25**  Pitch prep: what makes a tractable question, and the corpus-existence rule.
- **1:45**  Gemini-free check and check-out.

## Reading & homework

- **Reading:** [Mullen, America's Public Bible](https://americaspublicbible.org/) (intro + a verse)
- **Supplement:** [Underwood on GPT-4 and fictional time](https://tedunderwood.com/2023/03/19/using-gpt-4-to-measure-the-passage-of-time-in-fiction/); [Juola's Rowling unmasking](https://www.scientificamerican.com/article/how-a-computer-program-helped-show-jk-rowling-write-a-cuckoos-calling/)
- **Sketch:** Train a quick logistic regression on a labeled set; screenshot its five most positive and negative words. Bring a corpus existence proof to Week 4.
- **Check (AI closed):** Explain it: read your classifier's top weights aloud, and name one input where it would fail and why. (Competencies 4, 5.)
