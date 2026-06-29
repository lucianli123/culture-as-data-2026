---
title: "Week 7: The AI as a Reader, at Scale"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 7 · The AI as a Reader, at Scale

> Use the AI to read your whole corpus at once, learn to trust the labels it's sure of and catch the ones it isn't, and reckon with whose judgment you're renting.

*Tool / method: LLM-as-annotator, the most common operation in the field · Competencies: 2, 4, 5*

## Look at This

Gilardi, Alizadeh & Kubli (2023): ChatGPT outperformed crowd workers on several text-labeling tasks, cheaper, faster, more consistent.

## Question It

The prompt is the codebook; agreement with humans isn't ground truth; and the model fails silently, confident wrong answers a human's disagreement would have caught. Its "judgment" is a compression of scraped creative work, whose reading are you renting?

## Three modes today (about a third each)

- **Lecture / demo:** LLM-as-annotator, the most common operation in the field
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Warm-up + Look at This, room names the choice first: the AI as a cheaper coder, and where it fails silently.
- **0:10**  The annotator move, on your corpus: write a labeling prompt for your categories, run it on a slice, read the labels back. Tighten the definition and watch the labels shift, the prompt is your codebook.
- **0:35**  Confidence, and when to trust it: ask the model not just what but how sure. Sort by confidence, trust the sure labels, hand-check the unsure ones, which is exactly which 30 to pull for Week 6.
- **0:50**  Break
- **1:00**  Accuracy check, then project workshop: run your prompt against a small hand-labeled gold set. Where does the AI disagree, and is it wrong or are you? Then build time on your corpus. Go further (optional, technically comfortable): instead of the closed API model, run an open model from Hugging Face, or fine-tune your own small classifier (ModernBERT) on the labels you just made, the third reader you own.
- **1:50**  Gemini-free check and check-out.

## Reading & homework

- **Reading:** [NYT v. OpenAI](https://www.npr.org/2025/03/26/nx-s1-5288157/new-york-times-openai-copyright-case-goes-forward), read against your Week 4 licensing conversation
- **Supplement:** [Gilardi et al., full](https://www.pnas.org/doi/10.1073/pnas.2305016120); [Bamman et al., LLM classification in cultural analytics (CHR 2024)](https://arxiv.org/abs/2410.12029)
- **Sketch:** Show one label the AI got confidently wrong and one it nailed; say how you knew.
- **Check (AI closed):** Explain it: what is your labeling prompt deciding on your behalf, and how would you check whether to trust a given label? (Competencies 2, 5.)
