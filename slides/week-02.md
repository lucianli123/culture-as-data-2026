---
title: "Week 2: Counting, Compared: Is the Difference Real?"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 2 · Counting, Compared: Is the Difference Real?

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
- The notebook runs the trial live: the Ngram Viewer's JSON endpoint returns the paper's own data. "I am a failure" hockey-sticks in the mixed corpus and sits roughly flat inside fiction; "she whispered" hockey-sticks too. The evidence cuts both ways, which is why it is a trial.
- The method worth adopting: answer "your corpus is biased" with a test rather than an argument.

## What counts as a word?

- Two tokenizers shatter the same sentence differently: "don't" becomes one chip, two, or three.
- Models never see words. They see tokens, and the split is a design decision.
- Your hand-count argument about run/running is the same decision, made with highlighters. A stemmer makes it by rule (and produces "beauti"); a lemmatizer makes it by dictionary (and reads "was" as a noun unless told otherwise).
- Zipf's law: rank words by frequency and every corpus gives the same curve. The head is the stop list; the tail is too rare to count.
- tf-idf: down-weight what is common everywhere. "Common here, rare overall" is what characterizes a text.

## N-grams: counting phrases

- A bigram is two words in a row. Week 1 counted the sonnets' pairs; this week counts pairs across three corpora, and each book's top bigrams are already a fingerprint.
- Google Books n-grams are this method at civilizational scale: 500 billion words, one JSON request per query. Bollen et al. is an n-gram study.
- Longer n-grams buy context and pay in sparsity: the top word appears hundreds of times, the top pair dozens, the top triple six.
- "My love" is a different fact than "my" plus "love": pairs keep a sliver of the order the bag throws away.

## The statistics of counts

- Habit one: look at the distribution before the mean. Count data is skewed: most paragraphs of Dracula contain "night" zero times, a few contain many. Mean and median disagree, and the mean alone misleads.
- Habit two: divide by a denominator. The novels outweigh all 154 sonnets combined, so raw totals always vote for the novels. Rates per 1,000 words: "love" is 10.8 in the sonnets, 0.7 in Frankenstein.
- Habit three: a gap between rates can still be luck. That is the shuffle test's question, and it closes the session.
- A difference can be real and still small; a big difference can be an artifact of the denominator. Say which you have.

## Clustering: three communities, separable from counts alone

- 360 Reddit comments from r/buildapc, r/gardening, and r/relationship_advice, streamed live (analyze-only: counts and findings are published, the text and usernames never are). k-means gets no labels.
- Raw counts: one blob, the everywhere-words dominate. tf-idf: better, still smeared. tf-idf compressed to 60 dimensions: about six comments in seven land with their community.
- The algorithm never changed; the representation did. Same data, same k-means, three answers, which previews Week 5's whole move: replace word columns with learned dimensions.
- Read the stragglers: a gardening comment about a partner sorts with relationship_advice. The cluster found vocabulary; vocabulary mostly tracks community. Name what separated before you claim it.
- The hard version, in the go-further: r/sandiego against r/SanDiegan, one city, two communities. Clustering barely beats a coin flip, and even Week 3's supervised classifier reaches only about 60 percent. Topic is easy; community-within-topic is hard.
- And the same move for pictures: twenty Met paintings counted into 27 color buckets, k-means, no labels. Portraits sort from landscapes three in four, and the stragglers (a brown winter landscape counts like a portrait) are the discussion.

## Where counting fails

- Negation: "I am not happy" adds one to the happy count. Bigrams catch a little of this; most context is invisible to a counter.
- The stemmer is rules without a dictionary: universal, university, and universe all become "univers".
- The lemmatizer needs the part of speech: "saw" is a tool as a noun and the past of see as a verb; told nothing, it guesses.
- Polysemy: "sick beat" and "sick child" add to the same count. A word type is not a meaning. Week 5's embeddings exist for these holes, and bring their own.

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

- **0:00**  Warm-up: favorite Pudding pieces from the sketch, what did yours count, and one choice its makers made. Then retrieval.
- **0:05**  The trial: claim, objection, re-run-without-fiction rebuttal, "interpret with care." One named choice is the chart: the hockey-stick shape depends on its y-axis and smoothing. The notebook pulls the paper's own phrases live from Google Books and probes the fiction objection with fiction-marker phrases.
- **0:25**  A brief demonstration before the complications: the words one artist uses far more than everyone else, a signature vocabulary measured against a pop baseline.
- **0:30**  Hand-built bag-of-words: two authors, highlighters, argue about merging run/running. Counting requires defining.
- **0:55**  What counts as a word? Paste a sentence into two tokenizer playgrounds and watch it shatter differently. Models see tokens, not words. Then the standard tools for the run/running decision: NLTK stemming and lemmatization, a real stop list, and Zipf's law, the curve that explains why stop lists exist.
- **1:05**  Break
- **1:15**  N-grams and statistics, hands-on: bigrams across three corpora, distributions and mean-versus-median on real counts, rates per 1,000 words. Then tf-idf ("common here, rare overall") and k-means on 360 live Reddit comments from three subreddits: raw counts give a blob, tf-idf plus 60 dimensions sorts six in seven comments with their community. The representation, not the algorithm, does the work. Closer: the same k-means on twenty Met paintings counted into 27 color buckets sorts portraits from landscapes, three in four.
- **1:30**  Keyness, the She Giggles, He Gallops move: a log-odds ratio between two corpora finds the words one voice uses far more than a baseline, exactly the method behind Week 1's featured piece. The corpus pair is a choice too: artist vs. pop, lyrics vs. subreddit vs. novel.
- **1:42**  Is the difference real? The shuffle test: shuffle the labels and recount, one thousand times. If chance alone frequently produces a gap this large, the difference should not be trusted; if it almost never does, the finding stands. A difference can be real and still small.
- **1:50**  Gemini-free check and check-out.

## Reading & homework

- **Reading:** [Wolfram, What Is ChatGPT Doing](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/) (opening sections only)
- **Supplement:** [Zipf's law](https://en.wikipedia.org/wiki/Zipf%27s_law), the straight line in every text
- **Deeper (optional):** [Grimmer &amp; Stewart, Text as Data (2013)](https://web.stanford.edu/~jgrimmer/tad2.pdf), §1–4: all quantitative models of language are wrong, but some are useful
- **Sketch:** Count something in a text you care about; one chart; one sentence naming a choice. If the count compares two things, shuffle-test the gap.
- **Check (AI closed):** Explain it: why two tokenizers split a sentence differently, and what your stemming choice changed. (Competencies 3, 5.)
