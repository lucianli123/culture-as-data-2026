---
title: "Week 3: Classification: Counting with Weights"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 3 · Classification: Counting with Weights

> Argue out the genre article that made this method famous, watch a model get built in practice (and mis-built), then build your own in a group: a logistic regression you can read, doubt, and defend.

*Tool / method: Modelling in practice. Fit a logistic regression, read it, break it · Competencies: 2, 4, 5*

## Look at This

Ted Underwood's genre prediction (Distant Horizons, 2019; "The Life Cycles of Genres," 2016): a logistic regression, the exact tool of today's group work, trained to recognize detective fiction and science fiction across a century of novels.

## Question It

What counts as science fiction is a choice built into the training labels. And the model's most famous error, misreading Pynchon's The Crying of Lot 49, a detective-fiction spoof, shows genre boundaries are real but fuzzy. A classifier's mistakes teach as much as its successes; yours will too.

## Discussion: The Life Cycles of Genres

- You read the article. The room argues it, not the instructor. Four questions on the board, thirty-five minutes.
- What did Underwood actually count, and who decided which novels were detective fiction?
- The Pynchon misread (The Crying of Lot 49, a detective-fiction spoof) is the best thing in the paper: genre boundaries are real but fuzzy, and the error is what shows it.
- Carry this into the second hour: where would YOUR classifier fail, and what would the failure teach?

## Modelling in practice, built live

- Features, weights, a fit, and a score you would believe. That is the whole object.
- Every word casts a vote, for or against; the model adds the votes and learns the weights from labeled examples.
- Held out or it doesn't count. Score against a baseline that always guesses the bigger pile, or the number means nothing.
- Read the signed weights: the most positive and most negative words are the model's mind on the table.

## What goes wrong in practice

- Scoring on the training rows: that measures memory, not reading.
- An imbalanced pair flattering itself, and a leaked giveaway feature you never meant to hand it.
- No 'neither' box: hand it Shakespeare and it answers confidently anyway.
- Teachable Machine, sixty seconds: orange cats and brown dogs. Bias is not a ghost in the machine, it is the training set, and you assembled it.

## Group work: your model, your call

- Threes, one screen, rotating driver / reader / skeptic. The notebook has stations, not answers.
- Pick two piles, build features, fit, judge against the baseline, read the weights, break it.
- Then change ONE decision (min_df, tf-idf, bigrams, C, class_weight) and fit again: several models side by side is the point.
- Does the accuracy move, and do the top words change more than the accuracy does?

## Report back, then Week 4

- Ninety seconds a group: your pair, baseline vs. best, your two word lists, one caveat you would put in writing.
- Sort your top words into topic, register, and community habit. That sort is the finding; the accuracy is not.
- The methods menu in one slide: counting, classification, embeddings (W5), annotation (W7), plus optional add-ons.
- The corpus-existence rule: bring a screenshot of 50 loadable rows of your data to Week 4. No proof, no pitch.

## Three modes today (about a third each)

- **Lecture / demo:** Modelling in practice. Fit a logistic regression, read it, break it
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Warm-up and retrieval: last week's shuffle test in one sentence, and one thing you still don't trust about it.
- **0:05**  Discussion, Underwood's "The Life Cycles of Genres," read for today. The room argues it out, not the instructor: what exactly did he count, who decided which novels were detective fiction, and what does the model's misread of Pynchon's The Crying of Lot 49 show about genre boundaries? Then the transfer question every group carries into the second hour: where would YOUR classifier fail, and what would that failure teach?
- **0:40**  Lecture, modelling in practice: a model is features, weights, a fit, and a score you would believe. Built live on screen, mistakes included, in this order, turn text into a matrix, split off data the model never sees, fit it, compare the score against a baseline that always guesses the bigger pile, then read the signed weights. Then what goes wrong in practice: scoring on the training rows, an imbalanced pair flattering itself, a leaked giveaway feature, and the model with no "neither" box. Teachable Machine's orange cats and brown dogs is the sixty-second version of all of it; the bias is the training set, and you assembled it.
- **1:05**  Break
- **1:15**  Group work in Colab, threes, one screen, rotating driver / reader / skeptic. The notebook (week03_modeling_TOGETHER) is guided but blank, a worked six-sentence warm-up and then stations, not answers: pick your two piles, build the features, fit it, judge it against the baseline, read its mind, break it with something from neither pile. Then the workbench, where the plumbing is provided so the minutes go on choices: fit_model() sweeps min_df, tf-idf, bigrams, C, class_weight and stop words into one comparison table (sliders for the groups who prefer them), why() interrogates a single weight (which pile, how many documents, how many different people, the word in use), contributions() shows how any typed sentence was decided, and use_pair() swaps in two communities of your own so you can ask which findings survive a change of corpus rather than a change of model.
- **1:47**  Report-backs, ninety seconds a group: the pair you chose, baseline against best, your two word lists sorted into topic / register / habit, and the one caveat you would put in writing. Then the two things Week 4 needs, the methods menu in one slide (counting, classification, embeddings in Week 5, annotation in Week 7, plus the optional add-ons) and the corpus-existence rule, no proof no pitch. Gemini-free check and check-out.

## Reading & homework

- **Reading:** [Underwood, The Life Cycles of Genres (2016)](https://doi.org/10.22148/16.005), the article the session discusses: read the argument and the figures, skim the model tables
- **Supplement:** [Mullen, America's Public Bible](https://americaspublicbible.org/) (intro + a verse), the same tool as finished scholarship you can poke at; [Robinson, Trump's tweets: the Android/iPhone split (2016)](http://varianceexplained.org/r/trump-tweets/), distinctive words unmasking who typed; [Juola's Rowling unmasking](https://www.scientificamerican.com/article/how-a-computer-program-helped-show-jk-rowling-write-a-cuckoos-calling/)
- **Deeper (optional):** [Underwood, Distant Horizons (2019)](https://press.uchicago.edu/ucp/books/book/chicago/D/bo35853783.html), chapter 2, the book-length version of today's article, with the Pynchon misread in context
- **Sketch:** Take one of the group-work models to a labeled set you care about; screenshot its five most positive and negative words.
- **Check (AI closed):** Explain it: read your classifier's top weights aloud, and name one input where it would fail and why. (Competencies 4, 5.)
