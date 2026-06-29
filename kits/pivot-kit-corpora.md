# Pivot Kit, fallback corpus + question bank

If your project stalls, a corpus that won't cooperate, a question with no findable answer, 
that is expected, not failure. Adopt one of these pre-vetted pairs in Week 5 and still finish.
Each is **(PK)**: a corpus plus a question known to yield a finding in the time available,
pop-weighted, spanning text and image, tagged with which of the four tools it suits. A null
result honestly shown ("I expected X, the data doesn't show it, here's how I know") is a
complete project.

The four tools: **counting** (W2) · **classification** (W3) · **embeddings** (W5) ·
**AI annotation** (W7).

---

**(PK) 1, Eurovision lyrics, 1956–2023** · *text*
*Access:* `Spijkervet/eurovision-dataset` on GitHub (CSV, no key).
*Question:* Do winning entries use more love/unity vocabulary than non-winners, and has that
shifted by decade?
*Tool:* counting + tf-idf (or embeddings to cluster by theme).
*Why it's safe:* Clean licensed dataset, reachable in one cell, the question is answerable at
this scale, and language shift across decades gives a visible result.

**(PK) 2, /r/AmItheAsshole judgments** · *text*
*Access:* Pushshift mirror on HuggingFace (historical dump; live API is closed).
*Question:* Which words most predict a "You're the Asshole" verdict versus "Not the Asshole"?
*Tool:* classification (read the signed weights) → AI annotation to re-judge a slice.
*Why it's safe:* Pre-labeled at scale, a ~1,000-row slice trains a classifier in seconds, and
the signed-weight reveal is reliably fun and legible. Aggregate only; don't quote individuals.

**(PK) 3, TMDb movie posters of one genre** · *image*
*Access:* TMDb API, free key.
*Question:* Do horror posters cluster by color/visual style in a way the genre tag alone
doesn't capture?
*Tool:* counting (average color/brightness, W2) → image embeddings (W5/W6).
*Why it's safe:* Images are reachable via a documented API, a few hundred posters embed on a
CPU/T4 in minutes, and "covers cluster by untagged style" is the sharpest beyond-counting beat.

**(PK) 4, Met Museum Open Access objects** · *image + text*
*Access:* official Met API (~500K objects with images, CC0, go anywhere).
*Question:* How has the cataloging language for one department (e.g. "Costume") changed across
acquisition decades, and do the objects' images cluster the same way the labels do?
*Tool:* counting (catalog text) + image embeddings; the "count the labels, then let the images
sort themselves" contrast.
*Why it's safe:* CC0, zero licensing risk, a flagship API, and both a text and image path.

**(PK) 5, NYT Wedding Announcements, 1985–2014** · *text*
*Access:* `TheUpshot/nyt_weddings` on GitHub (CSV).
*Question:* What adjectives sit near "she" versus "he" in the announcements, and do they
cluster differently when embedded?
*Tool:* counting (W2) → embeddings (W5); the course's signature before/after.
*Why it's safe:* Small provided CSV, the gendered-adjective question is the canonical
count-then-embed demo, and it reliably produces a finding.

**(PK) 6, Pop-lyrics slice for one artist vs. a baseline** · *text*
*Access:* a provided lyrics slice (metadata/analysis only. Don't republish full lyrics).
*Question:* What is one artist's "signature vocabulary", the words they use far more than a big
pop baseline, and does it change across albums/eras?
*Tool:* counting / distinctive vocabulary (W2) → embeddings to cluster songs by mood/era.
*Why it's safe:* The signature-word fingerprint is a guaranteed delight beat, the slice is small,
and aggregate word counts avoid the lyrics-licensing problem.

**(PK) 7, Bluesky one-hour firehose slice** · *text*
*Access:* Jetstream, no API key; `atproto` Python SDK.
*Question:* Around one hashtag or topic, what distinct sub-conversations appear when posts are
embedded and clustered?
*Tool:* embeddings (W5) + AI annotation (W7) to label clusters.
*Why it's safe:* No key, a one-hour pull is plenty of data, and clustering yields visible
structure. Public-but-not-public: aggregate, anonymize, don't quote non-public individuals.

**(PK) 8, RuPaul's Drag Race contestant data + photos** · *image + text*
*Access:* `dragracer` R package / public episode data; contestant promo images.
*Question:* Do contestants' promo-look images cluster by season/era, and does the edit's
language (confessional text) predict placement?
*Tool:* image embeddings (W5/W6) + classification on text (W3).
*Why it's safe:* Beloved pop corpus, both a text and image path, small and tractable, and a
clear "does the data show what fans assume?" question.

---

### Born-digital fiction (for narrative projects)

**(PK) 9 - r/HFY sci-fi stories (born-digital fiction)** - *text*
*Access:* Reddit r/HFY via a Pushshift mirror / the born-digital fiction dump (aggregate, attributed).
*Question:* What is the "cause of victory" or cause of death across these stories, and does it shift by year?
*Tool:* AI annotation (W7) for narrative extraction, then counting/embeddings on the labels.
*Why it's safe:* A large, reachable born-digital corpus with a clear narrative question the annotator showcases; aggregate analysis, attribute the community, don't republish whole stories.

**(PK) 10 - r/nosleep horror (born-digital fiction)** - *text*
*Access:* Reddit r/nosleep via a Pushshift mirror (aggregate, attributed; small sample).
*Question:* Which horror subgenre is each story, and which subgenres rise and fall over time?
*Tool:* AI annotation (W7) to label subgenre; embeddings (W5) to find clusters the tags miss.
*Why it's safe:* Reachable, the subgenre question is answerable at scale, and the annotator's silent-failure lesson lands hard on ambiguous horror. Aggregate only.

**(PK) 11 - Public-domain genre fiction (Project Gutenberg) or Royal Road serials** - *text*
*Access:* Project Gutenberg (public domain, go anywhere) or a small, polite sample of Royal Road serials.
*Question:* What is the emotional arc of these stories, and do genres share a characteristic shape?
*Tool:* sentiment arcs (cool-methods) + character networks (cool-methods).
*Why it's safe:* Gutenberg is public domain with zero risk; Royal Road only as a small attributed sample. Both give long narratives the arc and network methods need.

---

### Expanded datasets (the wider applicant pool)

**(PK) 12 — Pantheon famous-people dataset** ⭐ · *text/structured*
*Access:* pantheon.world, a CSV of 11,000+ globally famous figures scored by fame. Loads with `read_csv`.
*Question:* How does a culture decide who is "famous", and how does that skew by era, place, and field?
*Tool:* counting/comparison (W2); embeddings (W5) on the bios.
*Why it's safe:* A real spreadsheet, no key, a clear status-and-prestige question.

**(PK) 13 — Music over time (Billboard Hot 100 + audio features)** ⭐ · *structured*
*Access:* a Billboard + audio-features **CSV** on Kaggle (flat, `read_csv`). *Spotify's audio API was deprecated Nov 2024, so do not call Spotify live;* the Million Song Dataset (millionsongdataset.com) has richer features but arrives as packed files the AI must unpack first.
*Question:* Did hit music get more homogeneous (tempo, energy, valence) over the decades?
*Tool:* counting/trends (W2); classification (W3) by decade.
*Why it's safe:* The CSV route needs no audio handling and no key; the question is answerable at scale.

**(PK) 14 — Met / MoMA Open Access (CC0 spreadsheet)** ⭐ · *image + text*
*Access:* the Met or MoMA CC0 collection **CSV** (loads with `read_csv`); images via the object IDs.
*Question:* Who gets collected, and how has the cataloging language changed across acquisition decades?
*Tool:* counting (catalog text) + image embeddings (W5/W6).
*Why it's safe:* CC0, zero licensing risk, both a text and image path, and a real spreadsheet to start from.

**(PK) 15 — LinCE code-switching corpora** · *text*
*Access:* Hugging Face `datasets` (one line: `load_dataset(...)`), word-level language tags.
*Question:* Where and how do bilingual speakers switch languages, and what does the switch mark?
*Tool:* counting/classification on the language tags (W2/W3).
*Why it's safe:* One-line load (the cookbook teaches it), labeled per word, a clear tagging-and-counting project.

---

*The pivot kit isn't a fallback-of-shame. It's insurance. The Week 5–6 one-on-ones are where
we reach for it if an idea wobbles. The three escape routes: narrow the question, swap the
corpus (keep the question), or swap the question (keep the corpus).*
