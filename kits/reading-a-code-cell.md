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
   `weddings.groupby("year")["name_status"].count()` reads: take the table → bundle rows
   by year → keep one column → count each bundle. Each dot passes the result along.
4. **The loop — `for item in pile:`** means *for each*. Everything indented below it
   happens once per item.
5. **Import — `import pandas as pd`.** Bring in a toolbox and give it a short name.
   Cells that are all imports do nothing visible; they stock the workshop.

## One real cell, annotated

```python
weddings["year"] = weddings["url"].str.extract(r"nytimes\.com/(\d{4})/").astype(float)
#  ^ new column      ^ take the url column, pull out the four digits after the site name,
#                      treat them as numbers  (pattern 1 wrapping pattern 3)

by_year = (weddings[weddings["name_status"].isin(["keeping", "taking"])]
           .groupby("year")["name_status"]
           .apply(lambda s: (s == "keeping").mean()))
#  keep only rows with a clear answer → bundle by year → for each year's bundle,
#  the share that says "keeping"  (one long pipeline: pattern 3)
```

If you can say what each arrow-comment says, in your own words, you have read the cell.

## Three things to ask the AI about any cell it writes

1. *"Explain this line by line."* Then check the explanation against the patterns above.
2. *"Where would this break?"* The answer teaches you what the cell assumes.
3. *"What is the smallest test that this did what I wanted?"* Run that test.

Reading is the skill. You never have to write `groupby` from memory — you have to catch
it counting the wrong thing.
