---
title: "Week 8: Models as Time Capsules + Settle the Finding"
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 8 · Models as Time Capsules + Settle the Finding

> Meet models that live entirely inside one historical period, learn what a famous model has secretly memorized, stress-test your own finding to see what survives, and leave with a prose draft.

*Tool / method: What a trained model is: a compression of its corpus · Competencies: 3, 4, 5*

## Look at This

TimeCapsuleLLM, a small GPT trained from scratch on nothing but 1800s London publications, and "Speak, Memory" (Bamman's lab), which probes which books GPT-4 has effectively memorized.

## Question It

A period model speaks only for the period's published, surviving, digitized voices. And memorization isn't reading: models score higher on memorized books, so an LLM that seems to read your corpus may be partly reciting it, a validity problem, not just an ethics one.

## Stress-test the finding

- Bollen's method, applied to your own finding: remove the slice that most concerns you and re-run.
- If the pattern survives, report it with the check shown. If it does not, you have learned what the finding depended on.
- Minimum bar: ONE robustness check, the one that most threatens your result.
- "I expected X, the data doesn't show it, here's how I know" is a complete, publishable result.

## Memorization isn't reading

- Speak, Memory (Chang et al., 2023): name-cloze tests show GPT-4 has memorized many novels; it fills in "___ Bennet" without reading anything.
- A model may be reciting your corpus rather than analyzing it: a validity problem, not only an ethics one.
- TimeCapsuleLLM: train only on 1800s London text and the model speaks its era. A model is bounded by its corpus.
- Ask of every model you used: what was in its training data, and does that undercut MY claim?

## The show-your-work appendix

- Your method choices, your moments of doubt, what you cut, what the AI got wrong.
- Name where a reader could reasonably disagree with you, before they do.
- The honesty you demanded of published work all term, turned on yourself. (Data Feminism's practice, run quietly all course.)

## Three modes today (about a third each)

- **Lecture / demo:** What a trained model is: a compression of its corpus
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Warm-up + Look at This: TimeCapsuleLLM and "Speak, Memory," screenshots ready. (These period models, and supplements like MonadGPT and MacBERTh, live on Hugging Face, where you can download and run open models, or fine-tune your own.)
- **0:07**  Stress-test the finding, one continuous arc on your own results: shuffle the labels and re-run; split the corpus in half; ask "compared to what?". Then compress whatever survived into one headline sentence.
- **0:52**  Break
- **1:02**  Gemini-free writing block: write your one-sentence interpretation yourself.
- **1:22**  Writing workshop: opening question, what you found, what it does not show, the choices you made. Distill the Data Biography into the corpus note.
- **1:50**  Check and check-out.

## Reading & homework

- **Reading:** [Ted Chiang, ChatGPT Is a Blurry JPEG of the Web (2023)](https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web), the compression idea this week is built on
- **Supplement:** [TimeCapsuleLLM](https://github.com/haykgrigo3/TimeCapsuleLLM) and [Speak, Memory](https://aclanthology.org/2023.emnlp-main.453/); period models [MonadGPT](https://huggingface.co/Pclanglais/MonadGPT) and [MacBERTh](https://huggingface.co/emanjavacas/MacBERTh)
- **Deeper (optional):** [Da, The Computational Case Against Computational Literary Studies (2019)](https://doi.org/10.1086/702594), the field's sharpest critique, read against your own robustness checks
- **Sketch:** Expand to 600 to 1,000 words; write your show-your-work appendix and which checks survived.
- **Check (AI closed):** Explain it: your headline finding, and what it does not show. (Competencies 3, 4.)
