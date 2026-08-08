---
title: "Week 4: How Machines Learn to Read: Neural Networks and Word Embeddings"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 4 · How Machines Learn to Read: Neural Networks and Word Embeddings

> See what your Week 3 classifier becomes when you stack it, learn where word vectors come from and what they can and cannot do, and leave with your own corpus collected, saved and committed to.

*Tool / method: Neural networks and word embeddings, plus getting data off the web · Competencies: 2, 6*

## Look at This

Garg, Schiebinger, Jurafsky and Zou, "Word embeddings quantify 100 years of gender and ethnic stereotypes" (PNAS 2018): train word vectors on each decade of American text from 1910 onward, measure how far occupation words sit from woman-words versus man-words, and read a century of stereotype change off the geometry. The embedding stops being a gadget and becomes a measuring instrument.

## Question It

The measurement tracks the corpus, not the country: Google Books and COHA are what got printed and digitised, so a shift may be a shift in publishing. The word lists (which words count as "female", which occupations count) are the authors' choices, and the bias they find is the bias in the text, which is the same geometry that makes the king-queen analogy work. What the vectors know, they learned from us.

## A century of stereotypes, measured as distance

- Garg et al. (PNAS 2018) trained word vectors on each decade of American text from 1910 on.
- The measure: how far do occupation words sit from woman-words versus man-words, decade by decade?
- The curve tracks the century - and matches independent census and survey data, which is what makes it evidence rather than a demo.
- Question it: is that the country changing, or what got printed and digitised? And who chose which words count as female?

## Your classifier, redrawn as a neuron

- Inputs (word counts), one weight each, add them up, squash to a probability. That is Week 3, and it is one neuron.
- A network stacks them: a hidden layer between the words and the answer.
- What stacking buys: features nobody hand-wrote. Combinations of words the model invents because they help.
- What it costs: the weights stop being readable. That is the trade Week 7 asks you to accept knowingly.

## How it learns: downhill, in small steps

- A loss is one number saying how wrong the model currently is.
- Gradient descent: nudge every weight in the direction that lowers the loss, then repeat.
- No calculus today. Rolling downhill in fog, feeling for the slope, is the honest picture.
- TensorFlow Playground, live on the spiral: watch the hidden units carve the space into pieces.

## The problem embeddings solve

- In a bag of words, happy and joyful share nothing. Neither do Oakland and Berkeley.
- Counting has no notion of meaning. That is its honest floor, and you have lived with it since Week 2.
- The distributional idea: a word is known by the company it keeps.
- So put every word in a space where words that keep similar company land near each other.

## Where word vectors come from

- word2vec is a small neural net trained on a fake task: given a word, guess its neighbours.
- Nobody wants the predictions. The by-product is the point: the hidden layer becomes one vector per word.
- Similarity is the angle between two vectors, the same cosine as Week 2's vector space.
- king - man + woman lands near queen. Directions in the space carry relationships nobody labelled.

## The analogy, with its caveats attached

- The arithmetic is nudged: the query words are excluded, or king comes back as its own nearest neighbour.
- Most analogies fail. The famous four are the ones that worked.
- The same geometry gives doctor - man + woman = nurse (Bolukbasi 2016). Week 5 argues about what that means.
- Static vectors: one per word. Contextual models: one per occurrence. Week 5 embeds whole sentences.

## Where a corpus comes from

- Route 1, and most projects should stop here: a prepared file. pd.read_csv(url), gdown, load_dataset().
- Route 2, an API: a documented URL returning JSON. Endpoint, key, pagination, rate limit - all four on screen as we call the Met.
- Route 3, a small scrape, only when there is no file and no API. BeautifulSoup, slowly.
- The check that comes with route 3: robots.txt and the terms, request slowly, take only what you need, never republish.

## The licensing line, in three sentences

- CC0 museum data and public-domain books: use freely, republish freely.
- Academic corpora and community text: analyze, do not redistribute. Lyrics and reviews: metadata and counts only.
- Shadow-library books: never. That line is what the field's $1.5B settlement was about.
- The Data Biography answers the rest: where it came from, who is missing, what it cannot say.

## Three modes today (about a third each)

- **Lecture / demo:** Neural networks and word embeddings, plus getting data off the web
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Warm-up: where Week 3 left off, and one sentence on where today goes. The classifier you built is one neuron; today it grows.
- **0:08**  Look at This, then Question It: the Garg paper's headline figure, a century of stereotype change measured as distance in an embedding space. Then the questions: is that a change in the country or in what got printed, and who chose the word lists?
- **0:15**  Lecture one, from one neuron to a network (20 min). Your logistic regression, redrawn: inputs, one weight each, a sum, a squash. Then stack it, hidden layer first, and what stacking buys you: features nobody hand-wrote. Training as rolling downhill, loss and gradient descent without the calculus. TensorFlow Playground live on the spiral, watching hidden units carve the space. What it costs: the weights stop being readable, which is exactly the trade Week 7 asks you to accept.
- **0:30**  Lecture two, word embeddings (30 min). The problem first: to a bag of words, happy and joyful are unrelated columns, which is counting's honest floor. The distributional idea, a word is known by the company it keeps. word2vec as a small neural net trained on a fake task, predict the neighbouring word, whose by-product is the vector. Then the geometry: nearest neighbours, cosine similarity, and the king - man + woman analogy with its caveats shown. The Embedding Projector live on a real vocabulary. Closing distinction, one line each: static vectors (one per word) versus contextual ones (one per occurrence), and the sentence embeddings Week 5 actually uses.
- **1:00**  Break
- **1:10**  Where a corpus comes from, APIs and scraping (20 min), demoed live with the AI writing the code. Route one, the prepared file most projects should use. Route two, an API: hit the Met or Art Institute endpoint, no key, and name what an endpoint, a key, pagination and a rate limit are as they appear on screen. Route three, a small scrape with BeautifulSoup, and the four-line check that comes with it: read robots.txt and the terms, request slowly, take only what you need, never republish. The licensing line in three sentences: CC0 and public domain go anywhere, academic sets are analyze-don't-redistribute, shadow libraries never.
- **1:30**  Collect-and-build lab (20 min): point the cookbook notebook at your corpus, reshape it, and save it to your Drive project folder so it is there next week. Fork the publishing template with GitHub Pages on, so a live placeholder URL exists from today.
- **1:50**  Pitch in pairs, two minutes each: your corpus, your two methods, what would count as a finding. Then commit, with the pivot kit named as insurance and a null result named as a real result. Check-out.

## Reading & homework

- **Reading:** [Garg, Schiebinger, Jurafsky &amp; Zou, Word embeddings quantify 100 years of gender and ethnic stereotypes (PNAS 2018)](https://www.pnas.org/doi/10.1073/pnas.1720347115): abstract, significance statement and figures, methods skimmed. What the lecture's machinery is for
- **Supplement:** [Alammar, The Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/), where the vectors in that paper come from, drawn one picture at a time; [Krause, Data Biographies](https://gijn.org/stories/data-biographies-getting-to-know-your-data/) (We All Count), the frame for this week's sketch
- **Deeper (optional):** [3Blue1Brown, Neural Networks](https://www.3blue1brown.com/topics/neural-networks), chapters 1 and 2; [Mikolov et al. (2013)](https://arxiv.org/abs/1301.3781), the four-page paper that started it; [Freelon, Post-API Age](https://dfreelon.org/publications/2018_Computational_research_in_the_postAPI_age.pdf), for when the front door closes
- **Sketch:** Data Biography (~400 words), collect your corpus with the cookbook, and one surprising neighbour from the Embedding Projector.
- **Check (AI closed):** Explain it: what a word vector is, in your own words, and one thing it cannot tell you. Plus your question aloud, what it omits, and where your data comes from. (Competencies 2, 6.)
