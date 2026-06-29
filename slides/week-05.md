---
title: "Week 5: Embeddings: A Map of Meaning"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 5 · Embeddings: A Map of Meaning

> Watch your own corpus, text or images, sort itself by meaning, see the finding counting couldn't give you, and learn the same trick is how "For You" feeds place you.

*Tool / method: Embeddings, the heart of the course, the leap past counting · Competencies: 4, 5*

## Look at This

A debate, two readings of one fact: embeddings encode the associations in a corpus.

## Question It

To Caliskan et al. (2017) that's a warning, a model trained on human text launders human prejudice. To Soni, Klein & Eisenstein (2021) the same mirror is a method, embeddings on abolitionist newspapers reveal which papers led the movement's language. The room decides: when is reading a corpus's associations a discovery, and when is it laundering bias?

## Three modes today (about a third each)

- **Lecture / demo:** Embeddings, the heart of the course, the leap past counting
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Warm-up + Look at This, room names the choice first: the embeddings debate.
- **0:10**  The beyond-counting moment: put Week 2 beside today. There you counted adjectives near she vs. he; now embed those descriptions and watch them cluster. Same question, two tools, the second visibly richer. Name the idea: an item becomes a vector, position learned from the company it keeps.
- **0:25**  Embed your own corpus, text or images. Image projects embed their pictures and watch them group by untagged style. The embedding model is an open one from Hugging Face, the hub where open models live (the same place Week 8's period models come from). And here charts stop being neutral: switch PCA to t-SNE and the same data rearranges. A visualization is an argument with decisions baked in.
- **0:55**  Break
- **1:05**  Project lab: push your embeddings, hunt the surprise cluster. A five-minute recommenders aside: "For You" is this same map plus your history. One-on-ones begin at the side.
- **1:50**  Gemini-free check and check-out.

## Reading & homework

- **Reading:** [Alammar, The Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/), plus the debate: [Soni/Klein, How Words Lead to Justice](https://www.publicbooks.org/how-words-lead-to-justice/) vs. [Caliskan et al. (2017)](https://arxiv.org/abs/1608.07187)
- **Supplement:** [Garg et al. (PNAS 2018)](https://www.pnas.org/doi/10.1073/pnas.1720347115); [Anderson et al., Spotify diversity](https://research.atspotify.com/algorithmic-effects-on-the-diversity-of-consumption-on-spotify/)
- **Sketch:** Toggle PCA vs. t-SNE and screenshot how the map changes; name one cluster you believe and one you don't.
- **Check (AI closed):** Explain it: on your map, name one cluster you believe is real and one that's probably a projection artifact, and how you'd tell. (Competency 4.)
