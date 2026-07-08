# Competency-check bank

One item per mode per week, for the Gemini-free block: a **trace it** cell (predict
before running), a **fix it** snippet (a planted bug, with the bug named for the
instructor), and an **explain it** prompt. The weekly check named in the lesson plan is
the required one; the other two are alternates for re-checks and make-ups. Rotate
values; never reuse a fix-it on the same cohort twice.

## Week 1 — trace it (required)

- **Trace:** `sum(1 for s in sonnets if "summer" in s.lower())` — one sentence
  predicting what prints.
- **Fix:** `counts.most_comon(5)` — *AttributeError: a typo the traceback names almost
  verbatim (`most_common`).*
- **Explain:** why does the notebook save everything to the Drive project folder rather
  than `/content`?

## Week 2 — explain it (required)

- **Trace:** `len(tokenize("Don't stop believing", strip_punct=False))` — how many
  tokens, and why might another tokenizer disagree?
- **Fix:** `STOP = {"the", "and"}; kept = [w for w in words if w in STOP]` — *inverted
  condition: keeps stop-words instead of removing them.*
- **Explain:** two tokenizers split the same sentence differently — why? And what can
  your shuffle test rule out, and what can it not?

## Week 3 — explain it (required)

- **Trace:** a classifier's top weight is `("boring", -2.1)` — predict its vote on
  "a boring triumph."
- **Fix:** `model.fit(X_test, y_test)` — *trained on the test set; accuracy will be a
  lie.*
- **Explain:** read your five most positive weights aloud; name one input the classifier
  will get wrong and why.

## Week 4 — explain it (required)

- **Trace:** `pd.read_csv(url).head(50)` returns 50 rows and 3 columns — what does that
  prove for the corpus-existence rule, and what does it not prove?
- **Fix:** a scrape loop with `time.sleep(0.01)` — *the polite pause is missing; name
  the checklist line it violates.*
- **Explain:** your question aloud, what it omits, and where your data actually comes
  from.

## Week 5 — explain it (required)

- **Trace:** two sentences share no words; their cosine similarity is 0.81 — what does
  the model know that a counter does not?
- **Fix:** `TSNE(n_components=2).fit_transform(vecs[:3])` — *perplexity must be less
  than n_samples; three points cannot make this map.*
- **Explain:** on your map, one cluster you believe and one that is probably a
  projection artifact — and how you would tell.

## Week 6 — fix it (required)

- **Trace:** the AI labeled 30 items and agreed with you on 24 — what is your agreement
  rate, and is that good? (Compared to what?)
- **Fix:** the planted pipeline bug from the session (e.g., `df.dropna()` silently
  removing every row with an empty optional field before the count). Found AI-closed.
- **Explain:** one disagreement between your labels and the AI's where you were right —
  how do you know you were right?

## Week 7 — explain it (required)

- **Trace:** the annotator returns `{"label": "positive", "confidence": 0.51}` — what do
  you do with this row, and why?
- **Fix:** `PROMPT` asks for JSON but the parser does `raw.split(",")` — *fragile
  parsing; the recorded cassette shows why the JSON contract exists.*
- **Explain:** what is your labeling prompt deciding on your behalf, and how would you
  check whether to trust a given label?

## Week 8 — explain it (required)

- **Trace:** after shuffling labels 1,000 times, chance beat your gap 4 times — say the
  sentence you may now write, and the sentence you may not.
- **Fix:** a robustness re-run that removes the suspect slice but keeps using the
  *original* counts downstream — *the check ran; the finding never updated.*
- **Explain:** your headline finding, and what it does not show.

## Week 9 — fix it (required)

- **Trace:** `quarto render` succeeded but the deployed page shows no charts — where do
  you look first? (Hint: paths that worked locally.)
- **Fix:** the planted publishing bug from the session (e.g., an image path pointing at
  the Drive mount instead of the repo's `images/`).
- **Explain:** name one choice in your own main chart a skeptical reader would question,
  and your answer to them.

## Week 10 — the oral walkthrough (capstone)

No bank; the protocol: how you got your headline result, what it does not show, and how
the tools actually work — plus the workbench introduction. All eight competencies, out
loud, AI closed.
