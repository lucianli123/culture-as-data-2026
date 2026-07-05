---
title: "Week 3: Classification: Counting with Weights"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 3 · Classification: Counting with Weights

> Teach a machine a bias in ten minutes, build a classifier and read its mind, and preview the full methods menu before next week's commitment.

*Tool / method: Classification. Train a reader and read what it learned · Competencies: 2, 4, 5*

## Look at This

Ted Underwood's genre prediction (Distant Horizons, 2019): a logistic regression, the exact tool of today's lab, trained to recognize detective fiction and science fiction across a century of novels.

## Question It

What counts as science fiction is a choice built into the training labels. And the model's most famous error, misreading Pynchon's The Crying of Lot 49, a detective-fiction spoof, shows genre boundaries are real but fuzzy. A classifier's mistakes teach as much as its successes; yours will too.

## Underwood's classifier, in particulars

- A logistic regression, the exact tool of today's lab, trained on a century of novels to recognize detective fiction and science fiction.
- Its most famous error is the lesson: it misreads Pynchon's The Crying of Lot 49, a novel critics call a detective-fiction spoof.
- Genre boundaries are real but fuzzy, and the classifier's mistake is what shows it.
- Ask of every classifier, including yours: where does it fail, and what does the failure teach?

## A classifier is counting with weights

- Every word casts a vote, for or against. The model adds the votes.
- Training means learning the weights from labeled examples.
- Read the signed weights: the most positive and most negative words are the model's mind on the table.
- Spam filters have worked exactly this way for twenty years.

## You taught it that

- Teachable Machine, live: a cat/dog model trained only on orange cats and brown dogs.
- The room predicts what a black cat will do. Then watches it happen.
- Bias is not a ghost in the machine. It is the training set, and you assembled it.
- One line to carry out: today's classifier is one neuron; stack many and you have Week 7's model.

## The methods menu (before you commit)

- Counting and keyness: differences and trends. Classification: sort and label at scale. Embeddings (W5): a map of meaning. Annotation (W7): the AI reads for you.
- Optional add-ons where they fit: character networks, sentiment arcs, CLIP image search, a fine-tuned ModernBERT.
- The corpus-existence rule: bring a screenshot of 50 loadable rows of your data to Week 4. No proof, no pitch.

## Three modes today (about a third each)

- **Lecture / demo:** Classification. Train a reader and read what it learned
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Warm-up + Look at This: Underwood's genre prediction.
- **0:10**  Teachable Machine, instructor demo: a two-class image model trained live, then the reveal that it learned from only orange cats and brown dogs. The room predicts what a black cat will do, then sees it.
- **0:22**  Counting with weights, the lab: each word casts a weighted vote; a logistic regression adds them up. Train it on a pop corpus, then read the signed coefficients, its mind on the table.
- **0:52**  For fun: the words that most predict "breakup song" or "this reviewer hated it."
- **0:57**  One-line bridge: that classifier is a neuron; stack many for a neural net, which is what's inside the Week 7 model. A quick TensorFlow Playground glance.
- **1:00**  Break
- **1:10**  Methods menu preview, so Week 4's choice is informed: counting, classification, embeddings (Week 5), and optional approaches (character networks for fiction; sentiment arcs for story projects, Jockers's Syuzhet reproducible in Python, whose own smoothing controversy is the built-in lesson to doubt the shape; CLIP image search for visual projects; and, for the technically comfortable, fine-tuning a small open model, ModernBERT, on your own labels).
- **1:25**  Pitch prep: what makes a tractable question, and the corpus-existence rule.
- **1:45**  Gemini-free check and check-out.

## Reading & homework

- **Reading:** [Mullen, America's Public Bible](https://americaspublicbible.org/) (intro + a verse)
- **Supplement:** [Underwood on GPT-4 and fictional time](https://tedunderwood.com/2023/03/19/using-gpt-4-to-measure-the-passage-of-time-in-fiction/); [Juola's Rowling unmasking](https://www.scientificamerican.com/article/how-a-computer-program-helped-show-jk-rowling-write-a-cuckoos-calling/)
- **Sketch:** Train a quick logistic regression on a labeled set; screenshot its five most positive and negative words.
- **Check (AI closed):** Explain it: read your classifier's top weights aloud, and name one input where it would fail and why. (Competencies 4, 5.)
