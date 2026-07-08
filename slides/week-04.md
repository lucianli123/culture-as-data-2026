---
title: "Week 4: Pick a Corpus. Pick Two Methods. Commit."
subtitle: "Culture as Data · draft slides"
format: revealjs
---

# Week 4 · Pick a Corpus. Pick Two Methods. Commit.

> Leave with a pitched project, two chosen methods, your Data Biography drafted, and the skill that makes "bring your own corpus" real: getting data off the web.

*Tool / method: The project (no new mechanism this week) · Competencies: 2, 6*

## Look at This

A Pudding "How We Made…" process post, the messy middle, where every polished piece had a moment its maker thought it wouldn't work.

## Question It

Listen across the pitches for questions too vague to answer, corpora that don't exist as accessible data, methods chosen on instinct rather than fit, and the quiet scaling-down of ambition.

## What a viable pitch contains

- Three minutes, hard cap: your corpus (existence proof on screen), your two methods, and what would count as a finding.
- "Explore themes in music" is not answerable. "Did Billboard #1 lyrics narrow in vocabulary 1990-2020?" is.
- A null result, honestly shown, is a complete project: "I expected X, the data doesn't show it, here's how I know."
- The pivot kit exists because corpora fail. Adopting a fallback pair is normal, not a failure.

## Licensing rules, in one slide

- CC0 museum data and public-domain books: use freely, republish freely.
- Academic corpora: analyze, don't redistribute. Lyrics and review text: metadata and counts only.
- AO3 and other community-opposed archives: a small attributed sample at most, never a shared dataset.
- Shadow-library books: never. That line is what the field's $1.5B settlement was about.

## Three routes to a corpus

- Route 1, the common case: a prepared file. pd.read_csv(url), gdown for Drive links, load_dataset() for Hugging Face.
- Route 2: an API, the sanctioned route. The Met's endpoint returns JSON, no key required.
- Route 3, a last resort: scraping, done carefully. Read robots.txt and the terms of service, request slowly, take only what you need, never republish.
- Whatever the route: save the result to your Drive project folder today. Week 5 depends on it.

## The Data Biography (~400 words, due Week 5)

- Where did this data come from, and who made it?
- Who is in it, and who is missing from it?
- What can it not tell you, no matter how cleverly you count?
- Its distilled form becomes your essay's corpus note in Week 8. Write it once, use it twice.

## Three modes today (about a third each)

- **Lecture / demo:** The project (no new mechanism this week)
- **Workshop:** build hands-on on your own data
- **Discussion:** the study above, interrogate it, debate it, or critique each other's work

## The session

- **0:00**  Warm-up + Look at This: the process post.
- **0:08**  Pitches, three-minute hard cap each: your corpus (existence proof shown), your two methods, what would count as a finding.
- **0:48**  Break
- **0:58**  The data conversation: the licensing one-pager (CC0 museums and public-domain books go anywhere; academic-only sets analyze-don't-redistribute; lyrics and review text metadata-only; AO3 and other community-opposed archives a small attributed sample at most, never a shared dataset; live firehoses we discuss, don't scrape; pirated full-text books from shadow libraries like LibGen never, the line the field's $1.5B settlement was about), and the Data Biography introduced.
- **1:10**  Getting the data, APIs and scraping, demoed live with the AI writing the code. API first (the Met or Art Institute, no key); scraping second, with the robots.txt / ToS / rate-limit / anti-republish check.
- **1:30**  Collect-and-build lab: point the cookbook notebook at your corpus, reshape it, and save it to your Drive project folder so it's there next week (when the Week 1 Drive mount pays off), and fork the publishing template with GitHub Pages enabled, so a live placeholder URL exists from commit day. Your project repository starts today.
- **1:55**  Commit, with the pivot kit named as insurance. A null result honestly shown is a complete project. Check-out.

## Reading & homework

- **Reading:** [Krause, Data Biographies](https://gijn.org/stories/data-biographies-getting-to-know-your-data/) (We All Count)
- **Supplement:** [Freelon, Post-API Age](https://dfreelon.org/publications/2018_Computational_research_in_the_postAPI_age.pdf)
- **Deeper (optional):** [boyd &amp; Crawford, Critical Questions for Big Data (2012)](https://doi.org/10.1080/1369118X.2012.678878), the canonical statement of what large datasets cannot tell you
- **Sketch:** Write your Data Biography (~400 words) and actually collect your corpus with the cookbook.
- **Check (AI closed):** Explain it: your question aloud, what it omits, and where your data actually comes from. (Competencies 2, 6.)
