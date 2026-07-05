# Culture as Data — Lesson Plans

*The teach-from document. For each of the ten weeks: the mechanism topic, the featured study with its paired critique, the dataset(s), a minute-by-minute 2-hour session flow, the homework, and the week's competency check. It assumes the design in `syllabus.md` and the rationale in `planning-doc.md`.*

Sessions are **2 hours**. The course is **10 weeks**, three acts: Tour (1–3), Project (4–7), Publish (8–10). The eight competencies are the spine; each plan notes which it serves.

---

## The spine: four tools, and moving beyond counting

The course teaches four ways to turn culture into something a machine can analyze, ordered so each one expands what a student can *do* with their own corpus past the tool before it. The test for every mechanism beat is simple: **does understanding this change what you can do, or what you'll trust?** If yes, it's in, at the depth that changes your hands. If it's intellectual appreciation — beautiful but inert for your project — it's an optional spotlight or it's cut.

- **Counting** (Week 2) — frequencies and distinctive features. Powerful, and the honest floor: it has no notion of meaning, treating *happy* and *joyful* as unrelated columns.
- **Classification** (Week 3) — train the machine to sort your corpus and *read what it learned*. A logistic regression scoring weighted evidence; its signed weights are its mind on the table. This is the cheap, transparent reader; Week 7's annotator is the powerful, opaque one — the same job, scaled up.
- **Embeddings** (Week 5) — **the heart of the course.** Turn each item into a vector so similar things land near each other and meaning becomes geometry. This is the single biggest leap past counting: the day you can ask "what clusters together in my corpus" and "what's near what," your range expands more than from any other idea.
- **The AI as a reader, at scale** (Week 7) — have the model *judge* every item in your corpus (sarcastic or sincere, which of five themes), the most common real operation in the field and the natural deepening of classification. The skill is trusting the labels it's sure of and hand-checking the rest; the reckoning is whose judgment you borrow, since the model learned to read from scraped creative work.

The thread that ties them together — the course's actual signature — is **moving a question beyond counting, on your own data.** In Week 2 you *count* the words that gather around an axis you care about — the adjectives near *she* vs. *he*, say, or the words one artist uses far more than others, or the vocabulary that separates two genres; in Week 5 you *embed* those same words and watch clusters appear that counting couldn't show, because the machine places them by meaning. Same question, two tools, the richer one visibly seeing more. (Pick the example that matches the room — the before-and-after is the lesson, not the topic.) That before-and-after, run on the student's own corpus two or three times across the term, is what teaches "beyond counting" — far better than any amount of how-it-works exposition. Each beat is taught **experience-first, name-second, scale-up-third**: see it in a browser tool, name it, then "this is what the big models do — just more of it." Depth is conceptual-visual throughout — no linear algebra, no calculus. The repeated sentence: ***it's all turning culture into vectors and learning the weights, and the leap past counting is letting the machine place things by meaning instead of just tallying them.***

**Images are a co-equal kind of culture, taught through the same four tools — because the capability is identical.** Counting works on color, brightness, and composition; classification sorts album covers or posters and tells you which visual features it learned; embeddings place *paintings* near each other by style the catalog never tagged. A student can run their whole project on visual culture and never be a second-class case: image corpora are in the starter library, the data-collection cookbook pulls the museum image APIs, the embeddings lab runs on their pictures, the essay shows image clusters. The "beyond counting" contrast is, if anything, sharper on images — count a museum's tags, then embed the paintings themselves and watch them cluster by a visual style no one labeled. What images do *not* get is a tour of vision architectures: a student who clusters album covers doesn't need the CNN underneath any more than the lyrics student needs attention math to cluster songs. The capability is what matters; the architecture is appreciation. (The one genuinely thrilling visual *capability*, CLIP — search images by typing words — survives as a single optional spotlight for visual projects, offered the way stylometry is offered to text projects.)

**The three modes, balanced (~⅓ each).** Each core session runs in three roughly equal parts: about a third **lecture/demo** (the instructor teaches the week's tool or concept and live-codes it), a third **workshop** (students build hands-on, alone or in pairs), and a third **discussion** (the room interrogates a study, debates an interpretation, or critiques each other's work in progress). None is garnish; the three are co-equal, and each weekly plan opens with its rough split. The bookend weeks skew by function and don't force a rigid third: **Week 1** leans demo-and-workshop (no project yet to discuss), **Week 4** leans discussion-and-workshop (pitches, then collection), **Week 9** leans workshop-and-discussion (build, then critique), and **Week 10** is almost entirely discussion (the showcase).

**The critical-reading ritual — the anchor of the discussion third.** "Look at This, then Question It" opens most weeks: admire a famous study, then name one interpretive choice its authors made and one way it could be wrong. From Week 5 onward, **flip it** — show the study and let the room name the choice before you do. That flip is how competency 8 becomes theirs rather than a performance you do for them. It runs as a real discussion — often the trial or debate format (claim, objection, rebuttal) — and in the project weeks it's joined by **peer critique** of students' own work in progress. Keep it one piece, well-chosen (depth over a gallery), and give it real time.

**When minutes run out — and they will:** trim *proportionally* so the three-mode balance holds, rather than sacrificing one mode to rescue another. All three modes are load-bearing, so a tight session shaves a few minutes off each. The one floor that spans modes: every student should *build* something hands-on and *say* something in discussion — never a session that is all talk or all silent building.

**The anchor tools** (all free, browser-based, no install): the OpenAI Tokenizer / Tiktokenizer (Week 2), Google Teachable Machine (Week 3), and the TensorFlow Embedding Projector — which plots text *and* images (Week 5). The embedding models themselves come from **Hugging Face**, the public hub where open models live (named again in Weeks 7–8). Week 7's tool is the AI assistant itself, used as an annotator. A CLIP text-to-image search demo is the one optional add, for visual projects. A small kit, reused all term.

**Misconceptions are the real curriculum risk.** Novices reliably believe the model "understands," "looks things up in a database," or "is magic." Each week's mechanism beat targets one of these directly.

**Data sense, compressed.** One Data Biography (written at commit, Week 4), one licensing conversation with a one-page rubric (same week): CC0 museum data and public-domain books are always safe; academic-only data gets analyzed, not redistributed; lyrics/review text/charts are metadata-only; fan-fiction archives are sampled with care, not datamined; shadow-library piracy (LibGen) is off the table. When a source dies or gets gated, the deprecation itself is a reproducibility lesson.

---

# ACT ONE — THE TOUR (Weeks 1–3)

Full worked notebooks. Participatory live coding. Exposure and a hook, not mastery.

---

## Week 1 — Your First Investigation

**Focus:** culture as data, through the first tool met on day one: counting — rows, words, pixels.
**Competencies seeded:** 1 (read code), 8 (read work critically).
**Promise:** by the break you've loaded real cultural data, asked it a question, and made a chart — and by the end you've counted culture in all three shapes it comes in: rows, words, and pixels.

**Featured study — *She Giggles, He Gallops* (The Pudding, 2017).** Across ~2,000 film screenplays, the *verbs* in stage directions split sharply by gender — women are written to "snuggle," "giggle," and "squeal"; men to "gallop," "stride," and "shoot." Counting the verbs attached to "she" versus "he" lands the pattern, and the interactive makes it impossible to unsee. **Interrogate:** ~2,000 screenplays skew toward what got produced and digitized — is that "film," or Hollywood's slice? And whose choice is a gendered verb — the screenwriter's, the character's, or the genre's? Counting shows the split, not the cause. And read the *visualization's* choices, not just the data: how it groups and ranks the verbs, what it foregrounds, what a different cut would surface — a chart is an argument with choices baked in, the same as a count. The icon of the form, and the cleanest "counting is already a model": every step (which verbs, near which pronoun, in which scripts) is a decision. That's how we read all term — the numbers *and* the choices behind them.

**Data:** NYT Wedding Announcements (~500 rows, provided CSV); a small pop-lyrics slice (provided); ~200 Met Museum objects with thumbnails (CC0).

| Time | Activity |
|---|---|
| 0:00 | **Setting the room.** Social rules demonstrated — instructor deliberately breaks one and is corrected. Announce today's live coding includes real mistakes on purpose. Two-sentence frame: algorithms already read culture at scale; in ten weeks you'll do it yourself *and understand how the machine does it.* |
| 0:12 | Look at This, then Question It: *She Giggles, He Gallops*. |
| 0:17 | **Pre-train the vocabulary** (no code): corpus, method, model, embedding — plain language, pictures. Course map; deliverable (notebook + web page). |
| 0:32 | **Lab 1 (worked, participatory):** copy the notebook to Drive and **mount Drive into the runtime** (this *is* setup — and it's how your corpus and results survive Colab wiping the session; everything saves to one project folder in your Drive), Gemini key into Colab Secrets, load wedding data from URL. Instructor narrates, plants one real bug, and recovers it *out loud using the unblocking kit* — read the last line of the error, paste it back to the AI with "this errored, fix it and tell me what went wrong," try twice, then ask a human. **Hand out the one-page "common errors" cheat sheet here**; the AI *will* hand them a traceback, and the move is to not panic. First chart. Then solo: with a partner, draft three questions this data could answer, pick one, have the assistant write the code, run it, chart it. **The Week 1 check lives here:** before running your solo cell, write one sentence saying what it will do. (Trace it; C1.) |
| 1:10 | Break |
| 1:20 | **Lab 2 (worked) — count words, then pixels, the same move twice.** First a text: top words of a small lyrics slice — watch stop-words drown the list, remove them, and notice you just made a *choice*. Then an image corpus: ~200 Met thumbnails (or album covers). A picture is numbers — red/green/blue per pixel — so the AI computes each image's average color and brightness and ranks the corpus darkest to brightest. Text and pictures, counted with the same skill; *what you choose to count* is a decision in both. Browse the catalog as you go and notice what it *doesn't* record (seeds Week 4's Data Biography). Image projects start here and run all the way through. |
| 1:50 | One-slide teaser of the ladder ahead; the standing rituals named. Check-out. |

**Reading (cliffhanger):** the Bollen/Schmidt fight, abstract-and-figure only — Bollen et al. 2021 (PNAS), the "hockey stick" of cognitive distortions counted in Google Books; then the one-page Schmidt/Piantadosi/Mahowald critique: the surge may be an artifact of *which books Google scanned*. Bring the three questions (what did they decide / load-bearing assumption / where's the gap). *Trial next week — including how the authors fought back.* (Population-level mental-health topic; keep the touch light.)
**Sketch:** one question from your life answerable with text or image data; three sentences.
**Check (trace it):** folded into Lab 1's solo turn — one written sentence predicting what your cell does before you run it. *(C1.)*

**Instructor notes.** Protect the wow; roving help catches the silently stuck before the break. The bored coder gets the "go further" cell. Most students arrive already using AI day to day (Claude, Gemini, ChatGPT), a few of them inefficiently — so the frame isn't "here is a new tool," it's "you already use these; this course makes you use them *well*, and read what they hand you." One week-one stance to hold all term: the assistant is plumbing — it writes code so the room can think about culture; it is not the subject.

**On the environment.** Colab's runtime is ephemeral — it wipes on idle or disconnect — so the Week-1 Drive mount is not housekeeping, it's what keeps a student's Week-4 corpus alive to Week 5. Make everyone save to their Drive project folder, and demo re-mounting after a reset once so it isn't scary later. For in-notebook help, Colab's **built-in Gemini** (the spark icon: generate a cell, or fix an error and read the diff) is the primary assistant and keeps the code visible; students already fluent in Claude or ChatGPT can use those instead — the workflow is identical. The Gemini *API key* is a separate thing, needed only for Week 7's annotation pipeline. If a student's Colab keeps disconnecting, **Kaggle Notebooks** is the fallback — its working directory persists with no mount. One thing to *steer away from*: letting a student turn a whole project over to an autonomous agent (Colab's Data Science Agent, or Claude Code) — the course works because they read and question the code, so keep them on cell-level help, not hands-off generation.

---

## Week 2 — Counting Is Already a Model

**Tool one, deepened — counting against a baseline.** Distinctive words (keyness) and the shuffle test for whether a difference is real. Every count still hides a choice (tokens, stemming, the corpus itself).
**Competencies:** 3, 5; 8 via the trial.
**Promise:** put a famous PNAS paper on trial, build a word-counter by hand, find the words that make a voice *distinctive* (and discover Week 1's featured study was exactly that method) — and learn the one statistics move this course needs: the shuffle test, which tells you whether a difference is real or just chance. (The one counting week: Week 1 gave counting's first taste on words and pixels; this is the deep dive.)
**Mode balance:** ~⅓ discussion (the trial, expanded into a real debate + what-to-trust), ~⅓ workshop (hand-built counting + keyness + the shuffle test), ~⅓ lecture/demo (tokenizers, tf-idf, the is-it-real idea).

**The set-piece — the Bollen/Schmidt trial.** (1) The claim: a hockey stick of societal distress, found by *counting*. (2) The objection: the rising words are fiction-words, and Google scanned more fiction after 2000 — the "surge in distress" might be a surge in novels. (3) The rebuttal, and the move to steal: Bollen et al. didn't argue — they **removed the entire fiction corpus and re-ran it**, and the pattern largely held. The answer to "your corpus is biased" is *test it and show the result.* Land Schmidt's line: the books are "a treasure trove when interpreted with care."

**Alternative trial — Mauch vs. Serrà (swap in for a music-leaning cohort).** Same structure, different subject: a change-over-time claim found by *measuring*, with two rigorous teams reaching opposite conclusions. Mauch et al. (2015) measure the Hot 100 and find *no* progressive homogenization; Serrà et al. (2012) measure the Million Song Dataset and find the opposite — a homogenized timbral palette, narrowed pitch transitions, and the rising "loudness war." The trial move is identical: which *operationalization* do you believe, and why does one question give two answers? It's a little harder to adjudicate than Bollen/Schmidt — it turns on two different audio-feature definitions rather than "fiction-words vs. all words" — so it's the swap for a room that came for music, not the default. Note this is a *reading*, not a build: the audio-data access problems that affect music *projects* (the HDF5 extraction, the dead Spotify API) don't touch the trial at all.

**Data:** two short author passages (printouts); a Gutenberg novel, the Met titles, and a Reddit slice for the cross-corpus counting lab.

| Time | Activity |
|---|---|
| 0:00 | Warm-up retrieval. |
| 0:05 | **[Discussion] The trial + what to trust (28 min):** claim → objection → re-run-without-fiction rebuttal → "interpret with care." Credit first, always. One named choice is the *chart*: the hockey-stick shape depends on the y-axis and the smoothing window — show how a different axis flattens the drama. Then open it to the room as a real discussion: what *would* you trust this kind of counting for, and where would you refuse? The picture is a choice too, and the first thing to interrogate. |
| 0:33 | **[Delight] The fingerprint (5 min, no caveats):** before we complicate counting, enjoy what it already does. The AI pulls the words one artist uses far more than everyone else — the signature vocabulary of a Taylor Swift or a Kendrick Lamar album against a big pop baseline. No interrogation yet; just "counting alone already shows you a voice." Don't qualify it — that's the point. |
| 0:38 | **[Workshop] Hand-built bag-of-words (22 min):** two authors, highlighters, tally the top words. Argue about merging run/running, casing, stop-words. The arguments *are* the lesson: counting requires defining. |
| 1:00 | Break |
| 1:10 | **[Lecture] Counting mechanics (20 min):** *what counts as a word* — paste a sentence into two tokenizer playgrounds and watch it shatter into different chips (models see tokens, not words; connect to the stemming argument). Then *tf-idf* — the AI scales your count, stop-words dominate, motivating "common here, rare overall" (Zipf's line is the take-home supplement). |
| 1:30 | **[Workshop] Keyness — the *She Giggles, He Gallops* move (12 min):** from "common here, rare overall" to "distinctively *hers*": a log-odds ratio between two corpora surfaces the words one voice uses far more than a baseline. **The reveal:** Week 1's featured piece is exactly this arithmetic, run on 2,000 screenplays — you now own the method behind the study you admired. Run it on the delight-beat artist against the pop baseline; run it on a lyrics slice vs. a subreddit vs. a novel — the corpus *pair* is a choice, and this doubles as the corpus sampler before Week 4. |
| 1:42 | **[Workshop] Is the difference real? The shuffle test (10 min):** light statistics with zero formulas. Shuffle the labels, recount, repeat a thousand times: if chance alone often produces a gap as big as yours, don't trust it; if it almost never does, you have something. One sentence on effect size — real-but-tiny is still tiny. This is the same move as Bollen's re-run-without-fiction: robustness is a *test you run*, not an argument you have — and it returns as Week 8's robustness arc. |
| 1:52 | **Gemini-free check + check-out.** |

**Reading:** Stephen Wolfram, "What Is ChatGPT Doing…" — the opening sections only, where even text generation turns out to be built from counting. *Proof that the humble tool you start with underlies the fanciest ones.*
**Sketch:** count something in a text you love; one chart; one sentence naming a choice you made. If your count compares two things, shuffle-test the gap.
**Check (explain it):** two tokenizers split the same sentence differently — explain why; and say in one sentence what your shuffle test can and cannot rule out. *(C3, C5.)*

---

## Week 3 — Classification: Counting with Weights

**Tool two — classification.** Train the machine to sort your corpus and *read what it learned*: a logistic regression scoring weighted evidence, its signed weights its mind on the table. A usable capability (sort my corpus, tell me what mattered) and an honest one (you can see and doubt what it leaned on). This is the cheap, transparent reader; Week 7's annotator is the powerful, opaque one — the same job, scaled up.
**Competencies:** 4, 5; 2 (pitch prep).
**Promise:** teach a machine a bias in ten minutes, build a classifier and read its mind — what words it leaned on, where it would fail — and preview the full methods menu before next week's commitment.
**Mode balance:** discussion ~40 (the bias reveal + pitch deliberation with peer feedback), workshop ~35 (build and read the classifier), lecture ~18 (where this goes + the methods menu) — classification is taught hands-on, so the lecture share is the smallest here.

**Featured study — Ted Underwood's genre prediction (*Distant Horizons*, 2019; "The Life Cycles of Genres," *Journal of Cultural Analytics* 2016).** Underwood trained a logistic regression — the exact tool of today's lab — to recognize detective fiction and science fiction across a century of novels, and used it to trace how those genres consolidated. **Interrogate (room first):** *what counts as science fiction?* The training labels are themselves a scholar's choice — and the model's best teaching moment is an error: it misreads Pynchon's *The Crying of Lot 49*, a novel scholars read as a detective-fiction spoof, so the "mistake" reveals that genre boundaries are real but fuzzy. Where would your classifier fail, and what would the failure teach you? (Open data and code on Zenodo.)

**Swap options (pick one, or keep the default).** The same lesson lands on other corpora: **Mullen's *America's Public Bible*** (2023) — a classifier finding biblical quotations in millions of newspaper pages, where *what counts as a quotation* is the choice; it remains the course's model deliverable either way (an openly-coded, runnable book). **Barré's "Operationalizing Canonicity"** for a hierarchy-leaning room; **moral-framing classification** for a discourse-leaning room. Full write-ups, prepared choices, and the swap rule: the "Look at This" Library in the planning doc.

**Data:** students' own faces/objects via webcam (Teachable Machine); a provided **pre-labeled** text dataset (~1,000 rows — e.g. r/AmItheAsshole posts tagged YTA/NTA, or movie reviews tagged pos/neg) for the classifier lab.

| Time | Activity |
|---|---|
| 0:00 | **[Discussion] Look at This + the bias reveal (20 min) — the discussion opens here.** First interrogate Underwood's genre classifier (detective fiction vs. science fiction across a century of novels) — what counts as science fiction, and what does the model's famous misread of Pynchon's detective-spoof reveal about genre boundaries? Then the live demo that becomes a discussion: train a two-class **Teachable Machine** image model in minutes, reveal it saw only orange cats and brown dogs, and have the *room predict and debate* what a black cat will do before you show it. The bias concept, planted by a training set, argued out loud. **For image projects:** this *is* a classifier on pictures — the same move you're about to do on text, on pixels. |
| 0:20 | **[Workshop] Counting with weights — the lab (35 min):** each word casts a weighted vote, *for* or *against*, and the model adds them up — a logistic regression (spam filters work this way). Code it on something the room cares about: a pre-labeled pop corpus (song lyrics tagged by genre or mood, AITA posts tagged YTA/NTA, or film reviews tagged pos/neg). Have the AI train the classifier on word counts, then **read the signed coefficients** — its most positive and most negative words are its mind on the table. Which did it lean on? Do you agree? Where would it fail — can you build it a "black cat"? Reading the weights *is* the lesson; the AI writing the code is plumbing. |
| 0:55 | Break |
| 1:05 | **[Lecture] Where this goes + methods menu (18 min):** first the matched pair the course turns on — the *transparent* reader you just built (cheap; you see exactly what it weighed) vs. the *powerful* reader in Week 7 (the big model as an annotator that catches subtler categories like sarcasm and tone, but hides how it decided). Then the project-eligible methods, so Week 4's choice is informed: counting (done), classification (today), **embeddings** (a map where similar things sit close — the heart of the course, in Week 5), and a short menu of **optional approaches** for specific projects (character networks for fiction with many characters; sentiment arcs for story projects — the emotional shape of a narrative, Jockers's Syuzhet reproducible in Python, whose own smoothing controversy is the built-in lesson to doubt the shape; CLIP image search for visual projects; and, for the technically comfortable, **fine-tuning a small open model — ModernBERT — on your own labels**, the advanced version of Week 3's classifier). Embeddings is where most projects find their richer-than-counting finding. |
| 1:23 | **[Discussion] Pitch prep + peer feedback (22 min):** what makes a tractable question, and the corpus-existence rule for next week — then students float a rough project idea to the room (or a pair) and get a first round of feedback on whether it's answerable at this scale. The discussion that de-risks Week 5. |
| 1:45 | **Gemini-free check + check-out.** |

**Reading:** browse *America's Public Bible* online (americaspublicbible.org) — read the introduction and click through one or two verses to see the classifier's findings in situ (~15 min). *The classification tool, shown as finished scholarship you can poke at.*
**Sketch:** point the AI at a labeled dataset you're curious about, train a quick logistic regression, and screenshot its five most positive and five most negative words — do they make sense? **And bring a corpus existence proof to Week 4: a screenshot showing you can load 50 rows of your proposed data** (use the data-collection cookbook notebook — Week 4 teaches the how, but the cookbook works now). No proof, no pitch — it converts the classic Week-5 wall into a Week-3 homework problem.
**Check (explain it):** read your classifier's top weights aloud — what did it learn — and name one input where it would fail and why. *(C4, C5.)*

---

# ACT TWO — THE PROJECT (Weeks 4–7)

Notebooks become **completion problems** in fuller-guidance and skeleton versions. One-on-ones run in Weeks 5–6. The tools keep expanding what the project can do: embeddings, the biggest leap past counting (W5); deeper application and images (W6); and the AI as a reader at scale (W7).

---

## Week 4 — Pick a Corpus. Pick Two Methods. Commit.

**Focus:** no new tool — this week belongs to the project.
**Competencies:** 2, 6.
**Promise:** leave with a pitched project, two chosen methods (one swappable in Week 6), your Data Biography drafted — and the one skill that makes "bring your own corpus" real: getting data into Colab, whether it's a prepared file you download, an API you call, or a page you carefully scrape.

**Featured study — a Pudding "How We Made…" process post.** The messy middle: pivots, dead ends, the question that took weeks. Every polished piece had a moment its maker thought it wouldn't work.

**The one data conversation (12 min, not a gate):** the licensing one-pager — CC0 museums and public-domain books: go anywhere; academic-only sets (MovieLens, IMDb, Goodreads scrapes): analyze, don't redistribute; lyrics, review text, chart data: metadata only; AO3 and other community-opposed archives: a small attributed sample at most, never a shared dataset — the community actively fights datamining; live social firehoses: we discuss, we don't scrape (Webis-TLDR-17 and Stack Exchange are the clean-license routes to messy social text); pirated full-text books (LibGen, Anna's Archive): never — the line the field's $1.5B settlement was about. Judgment, not a rulebook.

**Methods on offer:** counting/comparison · classification (the AI as a reader you train and check) · embeddings (text and image) · character networks.

| Time | Activity |
|---|---|
| 0:00 | Warm-up + Look at This: the process post. |
| 0:08 | **Pitches (40 min, 3-minute hard cap each):** my corpus (existence proof shown), my two methods, what would count as a finding. Instructor takes tractability notes for the one-on-ones — listen for vague questions, vibes-chosen methods, and the quiet scaling-down. |
| 0:48 | Break |
| 0:58 | **The data conversation (12 min):** licensing one-pager + the Data Biography introduced (Krause's who/how/where/why/when, plus what's missing). |
| 1:10 | **Getting the data — three routes (20 min):** where does a corpus *come from*? Demoed live, the AI writing the code. **(1) Download a prepared file — the common case, taught first.** Most corpora (Pantheon, the Met/MoMA CSVs, the Billboard CSV, a HuggingFace dataset, a Reddit dump) are *already made*; the skill is getting the file into Colab and open: `pd.read_csv(url)` for a direct link, `gdown`/`wget` to pull a file into your Drive folder, `load_dataset(...)` for HuggingFace, `unzip` for an archive. This is the route a beginner most needs — and "I can find a file on GitHub but don't know how to use it" stops being a wall. **(2) API (the polite front door):** hit an endpoint students met — the Met or Art Institute, no key — and watch the AI turn a documented URL into a table; name what an endpoint, a key, and rate-limiting are. **(3) Scrape (the back door, used with care):** no file and no API — a small BeautifulSoup scrape, plus the four-line check: read `robots.txt` and terms, scrape slowly, take only what you need, never re-publish copyrighted text. The licensing one-pager tells you which route is even allowed. |
| 1:30 | **Collect-and-build lab (25 min):** point the cookbook notebook at *your* corpus — pull it via API or load the file you've got — reshape it with the AI, and **save it to your Drive project folder so it's there next week** (the cookbook writes it out for you — this is the moment the Week-1 Drive mount pays off). **Fork the publishing template** here too: your project repo is born with your project. The AI wrangles; you judge whether what came back is what you wanted. |
| 1:55 | **Commit — with a safety net named.** Point the room to the **pivot kit**: a bank of pre-tested fallback corpus-and-question pairs (each known to yield a finding in the time we have), and the reframe that matters — *a null result, honestly shown, is a complete project.* "I expected X, the data doesn't show it, here's how I know" is a real essay. The kit isn't a fallback-of-shame; it's insurance, and the Week 5–6 one-on-ones are where we'll use it if your idea wobbles. Check-out. |

**Reading:** Heather Krause, "Data Biographies" (We All Count).
**Sketch:** write **the Data Biography** (~400 words) for your chosen corpus — and *actually collect it* using the cookbook notebook (the API or scrape you saw in class), so you arrive at Week 5 with real data in hand. If collection fails or the corpus turns out thin, that's exactly what the pivot kit is for — adopt a fallback pair rather than arriving empty. The Data Biography is the one full pass; its distilled form becomes your essay's corpus note in Week 8.
**Check (explain it):** your question aloud — what it omits, and where your data actually comes from. *(C2, C6.)*

---

## Week 5 — Embeddings: A Map of Meaning

**Tool three — embeddings. The heart of the course, and the leap past counting.** Turn each item — a word, a passage, a painting — into a vector so similar things land near each other and meaning becomes geometry. The day a student can ask "what clusters together in my corpus" and "what's near what," their range expands more than from any other idea. This is the week the course's whole promise — *move your project beyond counting* — pays off.
**Competencies:** 4, 5. **(One-on-ones begin: 20-minute slots, Zimmerman structure — forethought / performance / reflection, one written goal.)**
**Promise:** watch your own corpus — text or images — sort itself by meaning, see the finding counting couldn't give you, and learn the same trick is how "For You" feeds place you.
**Mode balance:** discussion ~30 (the embeddings debate, now a full block), lecture ~20 (the idea + the beyond-counting contrast), workshop ~40 (embed your own corpus — the heart, the largest single share). The debate carries the discussion third. **Build floor (project weeks):** protect ≥35 min of hands-on building; if a project-week session runs short, lecture gives first, discussion second, the build last — finishing the artifact is the point of these weeks.

**Featured debate — Kozlowski vs. Bolukbasi: two readings of a direction in embedding space.** **Kozlowski, Taddy & Evans, "The Geometry of Culture" (*ASR* 2019)** find *directions* in embedding space — a rich–poor axis, an education axis — and read them as the cultural structure of social class, tracking how the meaning of affluence shifted across a century. **Bolukbasi et al. (2016)** find the same kind of direction — a gender axis — and read it as encoded prejudice to be removed. Identical technique, opposite verdicts, so the room decides: when you find a "status dimension" in a corpus, is it a discovery about how a society codes importance, or laundered ideology? (A prepared caveat that doubles as a gift: Bolukbasi's famous analogy result is itself contested — even the bias paper carries an arguable choice; see the Library.) It seeds the Weeks 7–8 training-data thread: the model absorbs the corpus, structure and prejudice alike.

**Swap debate (for a bias-and-recovery-leaning room) — two readings of the same fact.** Embeddings encode the associations latent in a corpus. That single fact is a *warning* to one set of researchers and a *method* to another:

- **The warning — Caliskan, Bryson & Narayanan (2017), "Semantics derived automatically from language corpora contain human-like biases."** Their WEAT test shows embeddings reliably reproduce human stereotypes: not just flowers-pleasant/insects-unpleasant, but European-American names paired with "pleasant" over African-American names, and "woman" pulled toward domestic words. The point: an embedding is a mirror of its corpus, so a model trained on human text *launders human prejudice* — deploy it in résumé screening or search and you propagate the bias invisibly.
- **The method — Soni, Klein & Eisenstein, "Abolitionist Networks" (2021),** via the authors' general-audience *Public Books* essay "How Words Lead to Justice." The *same* mirror, used to recover history: embeddings trained on nineteenth-century abolitionist newspapers decade by decade reveal which papers *led* new uses of words, and two papers edited by women led much of the movement's language — quantitative weight behind the argument that a multiracial coalition of women stood in abolition's vanguard. (It also shows the optional **networks** method live: aggregate "who led whom" into a leader/follower graph.)

**Language-leaning rooms:** swap in **Youn et al. (2016)** on whether languages partition meaning the same way. All write-ups and prepared choices: the "Look at This" Library.

**Interrogate (room first):** these aren't opposite claims — they're the *same* claim ("embeddings reflect the corpus") aimed at opposite goals. So the choice the room has to name: **when is reading a corpus's associations a discovery, and when is it laundering bias?** What makes Soni/Klein scholarship and a biased résumé-screener harm — the data, the purpose, the human in the loop, what gets *done* with the output? (This is the course's deepest lesson in miniature: a method isn't good or bad, it's good or bad *for a purpose*.) The thread runs forward, too: Caliskan's "the model absorbs what's in the corpus, including the ugly parts" is the Week 7–8 training-data-ethics question, already on the table.

**Data:** the project corpus (main event); 100 lyrics/posts from class corpora prepared as TSV for the Projector.

| Time | Activity |
|---|---|
| 0:00 | **[Discussion] The embeddings debate (30 min) — the discussion third.** Kozlowski's *directions in meaning-space* (a rich–poor axis read as the cultural structure of class) vs. Bolukbasi's *same kind of direction* (a gender axis read as encoded prejudice): one technique, opposite verdicts. Run it structured — claim, objection, rebuttal, then open floor — on the question the course turns on: when is a dimension found in a corpus a *discovery about culture*, and when is it *ideology read back*? The room names the choices first. This is the deepest lesson in the course (a method is good or bad for a purpose) and it seeds the Week 7–8 training-data thread. |
| 0:30 | **[Lecture] The embeddings idea + the beyond-counting moment (20 min):** put Week 2 and today side by side. Run it on something the room enjoys — cluster a beloved artist's songs by mood and era, or cluster characters in a franchise — and watch groupings appear that *counting* couldn't see, because the machine placed them by meaning, not by shared words. (The gendered-adjectives version from Week 2 still works and ties to today's debate; lead with the fun one.) Same question, two tools, the second visibly richer. Name the idea: a word, passage, or picture becomes a vector — a few hundred numbers — with position learned from the company it keeps. The Projector gives two minutes of intuition (neighbors are context-mates, *not* dictionary synonyms — kill that misconception). |
| 0:50 | Break |
| 1:00 | **[Workshop] Embed your own corpus — text or images (40 min):** the real event, on the student's own data, and the largest single block of the week. Text projects embed passages and hunt a surprise cluster; **image projects embed their pictures** — album covers, paintings — and watch them group by style nobody tagged (the same Projector plots both; this is image projects' first deep payoff). The model doing the embedding is an open one from **Hugging Face**, the hub where open models live (named again in Weeks 7–8). **[Delight] — let the find land, no caveats yet:** your own corpus just sorted itself by *meaning*, which counting never could — sit in that win for a moment before anything complicates it. *Then* the turn: **this is where charts stop being neutral —** switch PCA to t-SNE and the same data rearranges — clusters tighten, distances shift, a grouping you trusted may dissolve. A visualization is an argument with decisions baked in (axis, projection, what's shown, what's dropped); reading one means finding them. Near means probably similar; exact distances mean little. *Five-minute recommender aside:* "For You" is this same map plus your history — you're a point in taste-space, the feed is your nearest neighbors, and Spotify's own researchers found algorithmic listening *less* diverse than organic. One-on-ones at the side; pairs and go-further cards cover the floor. |
| 1:45 | **Gemini-free check + check-out.** |

**Reading:** Jay Alammar, "The Illustrated Word2Vec" — through the personality-vectors and king/queen sections (~15 min).
**Sketch:** on your map from class, toggle PCA vs. t-SNE and screenshot how the picture changes; then name one neighbor (or, for images, one cluster) that surprised you and say whether you believe it — real pattern, or projection artifact?
**Check (explain it):** on your map, name one cluster you believe is real and one that's probably a projection artifact — and how you'd tell. *(C4.)*

---

## Week 6 — Deepen the Project: Images, and Where the AI Fails

**Focus:** push the project past first findings — apply the tools (embeddings especially) harder on the student's own corpus, give image projects their deepest day, and calibrate exactly where the AI's reading of *your* data is wrong.
**Competencies:** 1, 4, 7. **(One-on-ones continue.)**
**Promise:** get your richer-than-counting finding working on your own corpus — including images, if that's your project — and find exactly where the AI fails on your data.
**Mode balance:** discussion ~33 (the visual-study interrogation + studying the AI's disagreements together + peer share), lecture ~17 (image embeddings), workshop ~48 (project lab + hand-labeling — a project-deepening week, so workshop is the largest share). **Build floor:** workshop already clears the ≥35-min project-week minimum (lab + hand-labeling); protect it if short.

**Featured work — Arnold, Tilton & Berke, "Visual Style in Two Network-Era Sitcoms" (2019).** Using computer vision on every shot of *Bewitched* and *I Dream of Jeannie*, they read the *visual grammar* of the shows — how often each character is on screen, how the camera frames them, where it sits — and show the camera itself encoding gender and domestic space differently for each lead. Images as data, done by humanists, with an open toolkit (Distant Viewing) you could run yourself. **Interrogate (room first):** *what counts as a "character-centered shot"?* — the operationalization is the argument, and a different definition tells a different story; two sitcoms is a slice, not "television." It's the perfect companion to your own image embeddings: the same move (turn pictures into measurable features), aimed at a question about culture. (Supplements: Lev Manovich's *Selfiecity*, the same idea at the scale of thousands of selfies; for sentiment projects, the Reagan/Swafford smoothing fight.)
**Lead, decided:** the contemporary opener is the genre-film piece (The Pudding's frame-by-frame film color work, or movie-poster trends by genre and decade) — it matches this cohort's media diet and puts the genre-fiction crowd's world on screen. An art-leaning room swaps in a museum-collection visual piece. Arnold/Tilton/Berke stays the rigor case to interrogate.

**Data:** project corpus (text or image); an image set (album covers or WikiArt) for the live image-embedding demo.

| Time | Activity |
|---|---|
| 0:00 | **[Discussion] Look at This, then Question It — a pair (18 min):** a *contemporary* visual study leads (The Pudding's frame-by-frame film color work, or movie-poster trends by genre and decade — this-decade culture the room watches), then Arnold, Tilton & Berke's sitcom camerawork as the rigor case to interrogate. Lead with what they recognize, interrogate with what's cleanest, and give the room time to argue the choices — this is part of the discussion third. |
| 0:18 | **[Lecture] Images on the same map, for real (17 min):** the embedding move from Week 5, now on pictures. Embed an image set live — album covers, movie posters — and watch them cluster by visual style nobody tagged. **[Delight]** Let this *land* before any critique — no caveats in this moment: it's a genuinely cool thing the room can now do, and that's the point of showing it. (It's also the "beyond counting" contrast at its sharpest — count a museum's labels, then let the images sort *themselves*.) Image-project students run it on their own corpus; text-project students watch, then push their own embeddings harder in the lab. *(Optional take-home spotlights for visual projects: CLIP image search — find images by typing words; and "find the visual echo," embedding-based visual-link retrieval in the spirit of Ommer's art-history work — tracing a repeated pose or composition across a corpus.)* |
| 0:35 | **[Workshop] Project lab + fix-it check (30 min):** apply your method harder on your own data — embeddings clustered and interpreted, or your classifier's labels interrogated; somewhere in here, the planted-bug fix-it check, found AI-closed. Instructor floats; one-on-ones at the side. *If catch-up time is needed, this lab flexes; the hand-labeling set-piece does not.* |
| 1:05 | Break |
| 1:15 | **[Workshop] The hand-labeling set-piece, part 1 — label by hand (Gemini-free, 18 min):** label 30 items from *your* corpus by hand; the AI labels the same 30. *(This stays hand-work on purpose — the one beat coding can't teach.)* Nobody skips it. |
| 1:33 | **[Discussion] Study the disagreements together + peer share (15 min):** where did you and the AI differ, and on each, is *it* wrong or are *you*? Walk a few aloud as a room, then pairs share the find of the day. "The AI read it for me" becomes "I know exactly where the AI is wrong on my data" — said out loud, to each other. |
| 1:48 | Check-out. |

**Reading:** a short piece on the AI-as-annotator question to prime Week 7 — Gilardi et al.'s abstract (ChatGPT vs. crowd workers) is enough. *Supplement, for sentiment projects:* the Reagan/Swafford smoothing fight.
**Sketch:** one disagreement between your labels and the AI's where you were right — why? Could it be a moment in your essay? (Image projects: instead, swap the image set or the number of clusters and screenshot how the grouping shifts.)
**Check (fix it):** the planted bug. *(C1, C7.)*

---

## Week 7 — The AI as a Reader, at Scale

**Tool four — LLM-as-annotator.** The single most common operation in computational cultural analysis: hand the model 5,000 items and have it *judge* each one — sarcastic or sincere, which of five themes, feminist-coded or not — categories too subtle for word-counting. It's the natural deepening of Week 3's classifier: there you built a cheap reader whose mind you could see (signed weights); here you borrow an expensive reader far more capable but far more opaque, and the week is about using it without being fooled by it. This is also where the course's pitch lands hardest — the model reads your corpus using judgment it learned from training data nobody audited, much of it scraped creative work — so whose reading are you actually borrowing?
**Competencies:** 2, 4, 5.
**Promise:** use the AI to read your whole corpus at once, learn to trust the labels it's sure of and catch the ones it isn't — and reckon with whose judgment you're renting when you do.
**Mode balance:** ~⅓ discussion (the annotator's-dilemma debate + the training-data-ethics discussion with peer share), ~⅓ lecture/demo (the annotator move + confidence), ~⅓ workshop (accuracy check + build). **Build floor:** the build holds at ≥35 min; lecture gives first when short, discussion second.

**Featured study — the annotator's dilemma, two papers.** **Gilardi, Alizadeh & Kubli (2023)** found ChatGPT *outperformed* crowd workers on several text-labeling tasks — cheaper, faster, more consistent. Then the counterweight: **the reliability is task-dependent and the model fails silently** — confident wrong answers that a crowd worker's disagreement would have flagged. **Interrogate (room first):** the prompt *is* the codebook (you decide what "sarcastic" means, and a different prompt relabels the corpus); agreement with humans isn't ground truth; and the model's "judgment" is a compression of its training data — so when it labels fan fiction or song lyrics, it's applying patterns learned from *other people's* scraped creative work. Who consented to be the standard? **Co-featured — the field's own account:** **Bamman, Chang, Lucy & Zhou (CHR 2024)** test LLM labelers on cultural-analytics tasks and land on the tradeoff this course is built around — the readable Week-3 classifier vs. the powerful, opaque LLM — plus the unsettling wrinkle that GPT-4o partly "wins" a folktale task by having memorized the answers. Gilardi opens the debate; Bamman carries the interrogation, and the memorization question opens Week 8.

**Data:** project corpus (the main event); a small labeled gold set per student for the accuracy check; the licensing/training-data reading.

| Time | Activity |
|---|---|
| 0:00 | **[Discussion] The annotator's dilemma (18 min):** Gilardi et al. (the AI labels as well as crowd workers, cheaper and faster) set against the silent-failure counterweight — it's confidently wrong in ways a human coder wouldn't be. Room names the choices first, then the debate: would you trust an AI to code your data, and under what checks? This opens the discussion third and sets up everything that follows. |
| 0:18 | **[Lecture] The annotator move, on your corpus (20 min):** write a labeling prompt for *your* categories, run it on a slice, read the labels back — the categories being exactly the ones word-counting was too blunt for (cause of death in each sci-fi story; horror subgenre; sincere or sarcastic; does this comment blame a broken system or one person's luck). **[Delight] — before any caveat:** read the labels back and enjoy it — the AI just read your *entire* corpus the way you asked, in minutes; sit with that before confidence complicates it. The craft: the prompt is your codebook — tighten the definition, add an example, watch labels shift. The same subjective call as stemming (Week 2) and weights (Week 3), now in plain English. |
| 0:38 | Break |
| 0:48 | **[Lecture] Confidence, and when to trust it (12 min):** ask not just *what* but *how sure* — the probability behind each label (logits in plain terms: strength-of-evidence, the Week 3 weights idea exposed for the big model). Sort by confidence, trust the sure labels, **hand-check the unsure ones** — exactly which 30 to pull for Week 6, not a random 30. A model can be confidently wrong, which is why the gold-set check comes next. |
| 1:00 | **[Workshop] Accuracy check + build (35 min — the build floor):** run your prompt against your small hand-labeled gold set — where does the AI disagree, and is *it* wrong or are *you*? Then real build time on your own corpus, instructor roving. This is the protected hands-on block; it does not shrink below 35 minutes. |
| 1:35 | **[Discussion] Whose judgment are you renting? + peer share (13 min):** the training-data reckoning, as a room — you spent a whole session getting your corpus ethically; the model reading it did not (the Week 8 thread, opened here). Then pairs share one label the AI nailed and one it got confidently wrong, and how they knew. |
| 1:48 | **Gemini-free check + check-out.** |

**Reading:** one short piece on the training-data fight — the *New York Times* v. OpenAI complaint summary, or a plain-language explainer on the Books3 / pirated-books corpus — paired with the reminder of *your own* Week 4 licensing conversation. The question for class: you spent a whole session getting your corpus ethically; the models reading it for you did not. *(Supplement: Underwood's GPT-4 narrative-time study — the literary-history version of the same move.)*
**Sketch:** show one label the AI got confidently wrong on your data and one it nailed; for each, say how you knew. *(Competency 4 in its rawest form.)*
**Check (explain it):** what is your labeling prompt deciding on your behalf, and how would you check whether to trust a given label? In your own words. *(C2, C5.)*
**Go further (optional, for the technically comfortable).** The annotator here is a *closed* model behind an API. Two open alternatives, both on **Hugging Face**, for anyone who wants them: run an **open model** in Colab instead of calling Gemini (free, private, and its training data is more knowable — the Week 8 point — but weaker, and it needs the GPU); or the bigger step, **fine-tune your own small classifier** on the labels you just made — train `ModernBERT` (a modern, faster BERT) on your hand-labeled plus AI-labeled examples, and end with a model that is *yours*, free to run, and far quicker than prompting for a narrow repeated task. This is the **third reader**: Week 3's classifier was transparent, Week 7's annotator is powerful, and a fine-tune is the one you *own*. It's a real jump in complexity, so it lives strictly as a go-further in the optional `cool-methods` notebook, never a required beat.

---

# ACT THREE — PUBLISH (Weeks 8–10)

The toolchain has been familiar since the Week 4 fork. The analysis is the evidence; the page is the communication layer.

---

## Week 8 — Models as Time Capsules + Settle the Finding

**Focus:** what a trained model *is* — a compression of its corpus. Bound the corpus to a time or a collection and the model's whole worldview is the corpus's worldview: the Week 2 lesson, at its largest scale.
**Competencies:** 3, 4, 5.
**Promise:** you meet models that live entirely inside one historical period, learn what a famous model has secretly memorized, kill your own finding to see what survives — and leave with a prose draft.

**Featured work — models as time capsules, one pair.** **TimeCapsuleLLM**: a small GPT trained from scratch on nothing but 1800s London publications — ask it about today and it answers from a Victorian mind, because the corpus *is* its world. Then the inversion, **"Speak, Memory" (Chang, Cramer, Soni & Bamman, 2023)**: instead of choosing a model's diet, probe what a famous model already ate — name-cloze tests revealed which books GPT-4 has effectively memorized, heavy on sci-fi, fantasy, and a familiar canon: a training "canon" nobody curated on purpose. And it's not just an ethics problem — it's a *validity* problem for last week's annotator work: the authors show models score far higher on memorized books than unmemorized ones, so an LLM that seems to "read" your corpus may partly be reciting it (the case for open models whose training data is known). This is the ad's hook made concrete: the books and art fed into commercial models, largely without permission and out of sight, and here you get to actually probe it. **Interrogate (room first):** a period model speaks only for the period's *published, surviving, digitized* voices — who got printed in 1850s London? — and memorization isn't reading. The loop back to Week 2 closes: corpus composition isn't a bias to apologize for; bounded deliberately, it's the instrument. (MonadGPT, the 17th-century model, and MacBERTh, the scholars' historical-English workhorse, are this week's supplements — all on **Hugging Face**, the public hub where open models live. That's the concrete other side of the case for open models: you can not only critique closed ones, you can download and run open ones, and even fine-tune your own — see Week 7's go-further.)

| Time | Activity |
|---|---|
| 0:00 | Warm-up + Look at This, then Question It (7 min): TimeCapsuleLLM and "Speak, Memory" — screenshots ready; small hosted demos are flaky. |
| 0:07 | **Kill it, then keep what survives (45 min, one continuous arc):** the robustness habits, run live on *your own* results — shuffle the labels and re-run (does the pattern survive randomization?); split the corpus in half (does it hold in both?); ask "compared to what?" (every claim needs a baseline). This is the Bollen rebuttal move from Week 2, done to your own work. Then, in the same sitting, compress whatever survived into one headline sentence, with the room's help. Killing and settling are one motion: what's left standing *is* the finding. *If projects need the time to settle, reduce this to a single robustness check — the one that most threatens the finding — plus the compression step.* |
| 0:52 | Break |
| 1:02 | **Gemini-free writing block (20 min):** write your one-sentence interpretation yourself, AI closed. Yours goes in the essay. |
| 1:22 | **Writing workshop (28 min):** opening question → what you found → what it does *not* show → the choices you made. Distill the Data Biography into the corpus note. |
| 1:50 | **Check + check-out.** |

**Reading:** none required. *Supplements:* the MonadGPT and MacBERTh model pages — two more time capsules, one playful, one scholarly. (Deeper cuts: the "Speak, Memory" paper; 3Blue1Brown's "But what is a GPT?"; Bycroft's 3D LLM walkthrough.)
**Sketch (important):** expand to 600–1,000 words before Week 9. Write the **show-your-work appendix**: what you cut, what surprised you, what the AI got wrong, the choices you made and where a reader could disagree — plus which robustness checks your finding survived.
**Check (explain it):** your headline finding, and what it does **not** show. *(C3, C4.)*

---

## Week 9 — Build the Page

**Competencies:** 1, 7 (code-review for any JS), 8 (comparative reading).
**Promise:** leave with a deployed draft at a public URL.

**Featured comparison — three published essays side by side** (a Pudding piece, an Observable notebook, a Quarto site). Same goal, three defensible-but-different sets of choices. There's no single right way — only choices you can defend. Yours will be choices too.

| Time | Activity |
|---|---|
| 0:00 | Look at This, then Question It: the three essays (15 min) — common structure, divergent choices. |
| 0:15 | **Structured critique (Critical Response Process, 35 min)** in trios: statements of meaning → maker's questions → neutral questions → permissioned opinions. |
| 0:50 | Break |
| 1:00 | **Interrogate your own chart (15 min) — the making-side mirror of Week 6's hand-labeling:** put your main visualization on the screen and turn the term's skepticism on *it*. Does the y-axis start at zero, or is the AI's default manufacturing a trend? Is the eye pulled toward a pattern the data won't support? What did this chart choice hide that another would show? You spent ten weeks interrogating other people's charts; this is the ten minutes you interrogate your own before strangers see it. Fix one thing. |
| 1:15 | **Build lab (35 min):** open the template you forked in Week 4; paste outline, charts, code; render; deploy to Pages. Static by default; JS opt-ins hit the **code-review checkpoint** — read the AI's JavaScript before you ship it. |
| 1:50 | Phone test in pairs; check-out. |

**Reading:** none. **Sketch:** title the essay; headline finding in one sentence.
**Check (fix it):** a planted bug in publishing/layout code (or in opted-in JS). *(C1, C7.)*

---

## Week 10 — The Showcase

**Competencies assessed:** all eight, via the two capstone moments.
**Promise:** a public celebration. Cookies.

**Closing Look at This — neural networks meet the art world, a triptych.** The market: *Edmond de Belamy* (2018), a blurry GAN portrait sold at Christie's for $432,500 — built largely on Robbie Barrat's openly shared code, so who is the author? The labor: Anna Ridler's *Mosaic Virus*, a network trained on 10,000 tulips she photographed and labeled herself, the dataset hung on the wall as part of the work — training data made visible as authorship. The museum: Refik Anadol's *Unsupervised* (MoMA, 2022–23), a network trained on MoMA's own collection, dreaming wall-sized inside the building that supplied the data, while critics fought over whether it was a screensaver or the collection seeing itself. Three rooms, one question the course has asked all term: when a machine reads a culture's archive, what is it showing us — and who decided what went in? You started Week 1 loading a museum's data. You end watching a museum's data become the art.

| Time | Activity |
|---|---|
| 0:00 | Welcome. A show, not an exam. The closing Look at This. |
| 0:10 | Presentations — 4–5 min each: corpus, headline finding, one surprise, live URL. |
| 1:30 | Reception; everyone's URLs loaded for browsing. |

**The two capstone moments:**
- **The oral walkthrough** — walk one person through how you got the headline result, what it does *not* show, and (new) **how the tools that got you there actually work.** The AI-resistant capstone; the natural home of competencies 5 and 8.
- **The workbench intro** — open the portfolio (notebook, the Data Biography, one revised-after-feedback artifact, check-out notes) with one paragraph: *here's what I can do now that I couldn't in Week 1,* mapped to the eight competencies.

**Within one week after:** a private one-page reflection.

---

## Appendix — The Admire/Interrogate Pairings at a Glance

| Week | Topic | Admire | Interrogate (and rebuttal) |
|---|---|---|---|
| 1 | Counting / data journalism | *She Giggles, He Gallops* (The Pudding) | Sample scope (~2,000 screenplays); whose choice is the verb? |
| 1→2 | Counting | Bollen et al. 2021 (PNAS) | Schmidt/Piantadosi/Mahowald critique → **Bollen's re-run-without-fiction rebuttal** |
| 3 | Classification | Underwood, genre prediction (*Distant Horizons*, 2019) | What counts as science fiction is in the training labels; the Pynchon misread shows the boundary is real but fuzzy (Mullen, *America's Public Bible*, is the prepared swap and stays the model deliverable) |
| 3 | Networks (optional method) | Beveridge & Shan, "Network of Thrones" | A "tie" is a 15-word window; change it, change the protagonist |
| 5 | Embeddings | Kozlowski, "Geometry of Culture" (2019) vs. Bolukbasi (2016) | A found dimension: discovery about culture, or ideology read back? (Caliskan vs. Soni/Klein is the swap pairing; Soni/Klein also shows the optional networks method) |
| 5 | Recommenders (spotlight) | Anderson et al. 2020, Spotify diversity study | "Diversity" is a defined metric; satisfaction is a correlation |
| 6 | Images as data | Manovich, *Selfiecity* / *On Broadway* | Sampling ("selfies in five cities") becomes a claim about a whole city |
| 6 (supp.) | Sentiment / smoothing | Reagan et al., "Six Basic Shapes" | **Jockers *Syuzhet* → Swafford → Schmidt** (the smoothing fight) |
| 7 | The AI as a reader | Gilardi et al. (ChatGPT vs. crowd workers) | The prompt is the codebook; it fails silently; whose training data is the standard? |
| 8 | Period models / memorization | TimeCapsuleLLM + "Speak, Memory" (Bamman lab) | A period model speaks for who got published; name-cloze measures memorization, not reading |
| 2–6 | **Images, as a co-equal corpus** | counting pixels (W1) → classifier on images (W3) → image embeddings (W5) → image projects deepened (W6) | The same four tools, applied to pictures — a full project path, not a separate track; CLIP image search is the one optional add |
| 10 | AI art (send-off) | de Belamy → Ridler → Anadol (market, labor, museum) | Who is the author; whose labor is the data; who decided what went in |

*(Deeper cuts for the curious: Michel et al. culturomics vs. Pechenick's corpus-contamination critique; Juola's Rowling unmasking and its distractor-set caveat; the Netflix Prize and the Narayanan–Shmatikov de-anonymization; Gonen & Goldberg's "Lipstick on a Pig"; Anthropic's "Mapping the Mind" / Golden Gate Claude; Nan Z. Da vs. the Critical Inquiry forum as the field-level fight.)*

## Appendix — Data and Tools by Week

| Week | Primary data / tools | Notes |
|---|---|---|
| 1 | Wedding CSV · Met thumbnails (the day-one image corpus for pixel counting) | All provided; CC0; zero risk. |
| 2 | Author passages · tokenizer playgrounds · Gutenberg · Reddit slice | The cross-corpus counter doubles as the corpus sampler. |
| 3 | Teachable Machine · pre-labeled text dataset (~1,000 rows) | Bias reveal needs a planted skew; the LR lab needs the labeled set. |
| 4 | Bring-your-own from the starter library · a live API (Met/AIC) · the data-collection cookbook · the publishing template | The one licensing conversation; the APIs-then-scraping demo; existence proofs due; project repos born today. |
| 5 | Project corpora · Embedding Projector | Pre-test the embed-your-corpus notebook on every starter corpus; the projection toggle is the homework. |
| 6 | Project corpus (text or image) · an image set (album covers / WikiArt) for the live embed demo | Pre-test the image-embedding notebook; have a CLIP take-home ready for visual projects. |
| 7 | Project corpus · a small hand-labeled gold set per student | The annotator runs on their own data; the gold set is the accuracy check. Pre-test a labeling prompt on a sample corpus. |
| 8 | Student results · TimeCapsuleLLM page · the "Speak, Memory" figure | Screenshots ready as the default; live only if the network cooperates. |
| 9–10 | Student notebooks → pages | — |

**The anchor tools, one link page:** OpenAI Tokenizer / Tiktokenizer · Teachable Machine · Embedding Projector (text and images). Plus, for visual projects, an optional CLIP image-search demo. (Week 7 uses the AI assistant itself.) All free, browser-based, no install — students should leave with this page bookmarked.
