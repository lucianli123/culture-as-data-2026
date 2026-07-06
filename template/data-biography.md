# Data Biography

*Written at commit (Week 4), about 400 words across six prompts. Its distilled form
becomes your essay's corpus note in Week 8. The framework follows Heather Krause's
"Data Biographies: Getting to Know Your Data" (We All Count).*

## The six prompts

1. **What is this data, exactly?** Rows, fields, size, span. Name the file and where a
   reader can get it.
2. **Who made it, and why?** The people and institutions, and the purpose it was
   collected for — which is rarely your purpose.
3. **How was it collected?** The instrument, the pipeline, the selection step. What had
   to be true of an item for it to end up in the data?
4. **Who is in it — and who is missing?** The population the data actually covers,
   named precisely, and the people or works the collection process excluded.
5. **What licensing tier does it sit in?** (See `kits/licensing-one-pager.md`.) What may
   you publish: the text, the counts, or only the findings?
6. **What can it not tell you?** The questions this data cannot answer no matter how
   carefully you count — including your own question's weak flank.

## A worked example: the NYT wedding announcements

**What.** 5,562 wedding announcements published in the New York Times, 1985–2014,
compiled by The Upshot as a CSV (`TheUpshot/nyt_weddings` on GitHub): article URL,
whether the bride kept or took a name, and both ages.

**Who made it, and why.** Two layers of makers. The Style desk decided, for thirty
years, whose weddings were worth announcing — an editorial judgment, not a sample. Then
Upshot journalists extracted the fields in 2015 to report on name-keeping trends.

**How.** Parsed from published announcement pages; the date lives in the URL. The
selection step is the crucial one: couples submit announcements and editors choose among
them.

**Who is in it, and who is missing.** Couples wealthy or prominent enough to be
selected, overwhelmingly East Coast, and — for most of the period — almost exclusively
heterosexual. Missing: nearly everyone who married in America in those years.

**Licensing tier.** Published journalism, compiled for analysis; metadata-level fields.
Analyze and publish findings; link to the compilation rather than redistributing it.

**What it cannot tell you.** Whether American brides kept their names at these rates —
only whether announced-in-the-Times brides did. It supports questions about elite
self-presentation, not national behavior; and nothing after 2014.
