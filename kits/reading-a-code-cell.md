# How to read a code cell

Handed out in Week 1 beside the common-errors cheat sheet. The AI writes the code in
this course; your job is to *read* it — and five patterns cover nearly every cell you
will meet. Competency 1 ("read a block of analysis code and say what it does") is built
from these.

## The five patterns

1. **Assignment — `name = thing`.** The right side runs first; the result gets a name.
   `weddings = pd.read_csv(URL)` means: fetch and parse the file, call the result
   `weddings`.
2. **Function call — `do(thing)`.** Parentheses mean *run this now*. `len(words)`,
   `print(df)`, `tokenize(text)`. What's inside the parentheses is the input.
3. **The method chain — read left to right, like a pipeline.**
   `manifest.groupby("artist")["title"].count()` reads: take the table → bundle rows
   by artist → keep one column → count each bundle. Each dot passes the result along.
4. **The loop — `for item in pile:`** means *for each*. Everything indented below it
   happens once per item.
5. **Import — `import pandas as pd`.** Bring in a toolbox and give it a short name.
   Cells that are all imports do nothing visible; they stock the workshop.

## What the names hold

Every name in a cell holds one of about six kinds of thing. Knowing which is half of
reading:

- **A string** — text in quotes: `"love"`. Code treats it as characters, not meaning.
- **A number** — `42` or `0.34`. No quotes.
- **A list** — an ordered pile: `["she", "giggles"]`. Loops eat these.
- **A dict** — labeled slots: `{"title": "...", "year": 1948}`. APIs return these.
- **A DataFrame** — the spreadsheet-like table `pd.read_csv` gives you; columns have
  names, rows have positions. Most course code is DataFrames in, DataFrames out.
- **A model** — an object you `fit` or `encode` with. You interrogate it, not read it.

Two values worth knowing by name: `NaN` means "missing," and it silently drops out of
counts — ask where it went. `None` means "nothing here," and it errors loudly when
touched — easier to catch.

## Colab words

A **cell** is one block that runs at once. The **runtime** (or *kernel*) is the machine
running them; when it restarts, every name is forgotten and you re-run from the top —
which is why the notebook must run top to bottom, and why your work lives in Drive. A
**traceback** is the error report; read its last line first.

## One real cell, annotated

```python
sonnet_words = [w for s in sonnets for w in re.findall(r"[a-z']+", s.lower())]
#  ^ new list        ^ for each sonnet, pull out its lowercase words and pool them
#                      (pattern 1 wrapping pattern 4, a loop inside a list)

per_sonnet = [len(re.findall(r"\blove\b", s.lower())) for s in sonnets]
rolling = pd.Series(per_sonnet).rolling(15, min_periods=1).mean()
#  count "love" in each sonnet → wrap the counts as a Series → smooth with a
#  15-sonnet rolling average  (pattern 1, then pattern 3's pipeline)
```

If you can say what each arrow-comment says, in your own words, you have read the cell.

## Three things to ask the AI about any cell it writes

1. *"Explain this line by line."* Then check the explanation against the patterns above.
2. *"Where would this break?"* The answer teaches you what the cell assumes.
3. *"What is the smallest test that this did what I wanted?"* Run that test.

Reading is the skill. You never have to write `groupby` from memory — you have to catch
it counting the wrong thing.
