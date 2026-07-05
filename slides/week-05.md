---
title: "Week 5: Embeddings: A Map of Meaning"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 5 · Embeddings: A Map of Meaning

> Watch your own corpus, text or images, sort itself by meaning, see the finding counting couldn't give you, and learn the same trick is how "For You" feeds place you.

*Tool / method: Embeddings, the heart of the course, the leap past counting · Competencies: 4, 5*

## Look at This

A debate, two readings of one discovery: embedding space contains directions.

## Question It

Kozlowski, Taddy & Evans (2019) find a rich–poor axis in embedding space and read it as the cultural structure of social class, measurable across a century. Bolukbasi et al. (2016) find the same kind of direction, a gender axis pairing men with "programmer" and women with "homemaker," and read it as prejudice to remove. Identical technique, opposite verdicts. The room decides: when is a dimension found in a corpus a discovery about culture, and when is it the corpus's own bias read back?

## The problem counting cannot solve

- To a counter, "happy" and "joyful" are unrelated strings. Zero overlap.
- An embedding turns each item into a vector, a few hundred numbers, positioned by the company the item keeps.
- Near in that space means similar in learned context: happy and joyful end up neighbors because they appear in the same company.
- Neighbors are context-mates, NOT dictionary synonyms. Kill that misconception today, out loud.

## The debate: discovery, or bias read back?

- Kozlowski, Taddy & Evans (2019): a rich-poor direction in embedding space tracks the cultural structure of class across a century. Culture made measurable.
- Bolukbasi et al. (2016): the same kind of direction pairs man:programmer :: woman:homemaker. Prejudice the model absorbed, to be removed.
- Identical technique. Opposite verdicts.
- The room settles it: what makes a found dimension a discovery vs. the corpus's own bias, the data, the purpose, or what you do with the result?

## The chart is a choice

- PCA and t-SNE flatten the same vectors two ways: clusters tighten, distances shift, a grouping you trusted can dissolve.
- "Near" means probably similar. Exact distances on the flattened map mean little.
- A visualization is an argument with decisions baked in: projection, axes, what's dropped.
- Tonight's toggle: PCA vs. t-SNE on your own map. Name one cluster you believe and one you don't.

## The recommender aside (five minutes, boxed)

- "For You" is this same map plus your history: you are a point in taste-space, the feed is your nearest neighbors.
- Spotify's own researchers found algorithmic listening less diverse than organic listening (Anderson et al., 2020).
- You built the same machinery today.

## Three modes today (about a third each)

- **Lecture / demo:** Embeddings, the heart of the course, the leap past counting
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Warm-up + Look at This, room names the choice first: the embeddings debate.
- **0:10**  The beyond-counting moment: put Week 2 beside today. There you counted the words around an axis you care about; now embed them and watch them cluster. Run it on something the room enjoys, a beloved artist's songs sorted by mood and era, and groupings appear that counting couldn't see. Same question, two tools, the second visibly richer. Name the idea: an item becomes a vector, position learned from the company it keeps.
- **0:25**  Embed your own corpus, text or images. Image projects embed their pictures and watch them group by untagged style. The embedding model is an open one from Hugging Face, the hub where open models live (the same place Week 8's period models come from). And here charts stop being neutral: switch PCA to t-SNE and the same data rearranges. A visualization is an argument with decisions baked in.
- **0:55**  Break
- **1:05**  Project lab: push your embeddings, hunt the surprise cluster. A five-minute recommenders aside: "For You" is this same map plus your history. One-on-ones begin at the side.
- **1:50**  Gemini-free check and check-out.

## Reading & homework

- **Reading:** [Alammar, The Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/), plus the debate: [Kozlowski/Taddy/Evans, The Geometry of Culture (ASR 2019)](https://journals.sagepub.com/doi/10.1177/0003122419877135) vs. [Bolukbasi et al. (2016)](https://arxiv.org/abs/1607.06520)
- **Supplement:** The second pairing: [Caliskan et al. (2017)](https://arxiv.org/abs/1608.07187) vs. [Soni/Klein, How Words Lead to Justice](https://www.publicbooks.org/how-words-lead-to-justice/); [Anderson et al., Spotify diversity](https://research.atspotify.com/algorithmic-effects-on-the-diversity-of-consumption-on-spotify/)
- **Sketch:** Toggle PCA vs. t-SNE and screenshot how the map changes; name one cluster you believe and one you don't.
- **Check (AI closed):** Explain it: on your map, name one cluster you believe is real and one that's probably a projection artifact, and how you'd tell. (Competency 4.)
