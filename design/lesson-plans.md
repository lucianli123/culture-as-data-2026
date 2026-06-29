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

The thread that ties them together — the course's actual signature — is **moving a question beyond counting, on your own data.** Count adjectives near *she* vs. *he* in Week 2; in Week 5, *embed* those descriptions and watch the gendered clusters counting couldn't show. Same question, two tools, the richer one visibly seeing more. That before-and-after, run on the student's own corpus two or three times across the term, is what teaches "beyond counting" — far better than any amount of how-it-works exposition. Each beat is taught **experience-first, name-second, scale-up-third**: see it in a browser tool, name it, then "this is what the big models do — just more of it." Depth is conceptual-visual throughout — no linear algebra, no calculus. The repeated sentence: ***it's all turning culture into vectors and learning the weights, and the leap past counting is letting the machine place things by meaning instead of just tallying them.***

**Images are a co-equal kind of culture, taught through the same four tools — because the capability is identical.** Counting works on color, brightness, and composition; classification sorts album covers or posters and tells you which visual features it learned; embeddings place *paintings* near each other by style the catalog never tagged. A student can run their whole project on visual culture and never be a second-class case: image corpora are in the starter library, the data-collection cookbook pulls the museum image APIs, the embeddings lab runs on their pictures, the essay shows image clusters. The "beyond counting" contrast is, if anything, sharper on images — count a museum's tags, then embed the paintings themselves and watch them cluster by a visual style no one labeled. What images do *not* get is a tour of vision architectures: a student who clusters album covers doesn't need the CNN underneath any more than the lyrics student needs attention math to cluster songs. The capability is what matters; the architecture is appreciation. (The one genuinely thrilling visual *capability*, CLIP — search images by typing words — survives as a single optional spotlight for visual projects, offered the way stylometry is offered to text projects.)

**The critical-reading ritual.** "Look at This, then Question It" opens most weeks: admire a famous study, then name one interpretive choice its authors made and one way it could be wrong. From Week 5 onward, **flip it** — show the study and let the room name the choice before you do. That flip is how competency 8 becomes theirs rather than a performance you do for them. **Hard cap: five to seven minutes, one piece, one named choice.** The moment it needs a second slide, it has become a lecture; multi-item galleries are banned.

**When minutes run out — and they will:** Act 1 protects the mechanism block, Act 2 protects project lab time (a 45-minute floor), Act 3 protects writing and building. The ritual shrinks before the lab does. Garnish dies first.

**The anchor tools** (all free, browser-based, no install): the OpenAI Tokenizer / Tiktokenizer (Week 2), Google Teachable Machine (Week 3), and the TensorFlow Embedding Projector — which plots text *and* images (Week 5). The embedding models themselves come from **Hugging Face**, the public hub where open models live (named again in Weeks 7–8). Week 7's tool is the AI assistant itself, used as an annotator. A CLIP text-to-image search demo is the one optional add, for visual projects. A small kit, reused all term.

**Misconceptions are the real curriculum risk.** Novices reliably believe the model "understands," "looks things up in a database," or "is magic." Each week's mechanism beat targets one of these directly.

**Data sense, compressed.** One Data Biography (written at commit, Week 4), one licensing conversation with a one-page rubric (same week): CC0 museum data and public-domain books are always safe; academic-only data gets analyzed, not redistributed; lyrics/review text/charts are metadata-only; fan-fiction archives are sampled with care, not datamined; shadow-library piracy (LibGen) is off the table. When a source dies or gets gated, the deprecation itself is a reproducibility lesson.

---

# ACT ONE — THE TOUR (Weeks 1–3)

Full worked notebooks. Participatory live coding. Exposure and a hook, not mastery.

---

## Week 1 — Your First Investigation

**Focus:** culture-as-data itself — no tool yet; the four tools start next week.
**Competencies seeded:** 1 (read code), 8 (read work critically).
**Promise:** by the break you've loaded real cultural data, asked it a question, and made a chart. A complete investigation, end to end, on day one.

**Featured study — *Pockets* (The Pudding, 2018).** Women's jeans pockets are measurably smaller; they measured pockets and one chart lands the argument. **Interrogate:** 80 pairs, a handful of brands — is that "women's pockets," or a slice? And look at the *chart* itself, not just the data: what does it put front and center, what scale does it use, what would a different choice emphasize instead? A chart is an argument with choices baked in, the same as a count. Great piece, arguable scope; both true. That's how we read all term — the numbers *and* the pictures.

**Data:** NYT Wedding Announcements (~500 rows, provided CSV); ~200 Met Museum objects with thumbnails (CC0).

| Time | Activity |
|---|---|
| 0:00 | **Setting the room.** Social rules demonstrated — instructor deliberately breaks one and is corrected. Announce today's live coding includes real mistakes on purpose. Two-sentence frame: algorithms already read culture at scale; in ten weeks you'll do it yourself *and understand how the machine does it.* |
| 0:12 | Look at This, then Question It: *Pockets*. |
| 0:17 | **Pre-train the vocabulary** (no code): corpus, method, model, embedding — plain language, pictures. Course map; deliverable (notebook + web page). |
| 0:32 | **Lab 1 (worked, participatory):** copy the notebook to Drive and **mount Drive into the runtime** (this *is* setup — and it's how your corpus and results survive Colab wiping the session; everything saves to one project folder in your Drive), Gemini key into Colab Secrets, load wedding data from URL. Instructor narrates, plants one real bug, and recovers it *out loud using the unblocking kit* — read the last line of the error, paste it back to the AI with "this errored, fix it and tell me what went wrong," try twice, then ask a human. **Hand out the one-page "common errors" cheat sheet here**; the AI *will* hand them a traceback, and the move is to not panic. First chart. Then solo: with a partner, draft three questions this data could answer, pick one, have the assistant write the code, run it, chart it. **The Week 1 check lives here:** before running your solo cell, write one sentence saying what it will do. (Trace it; C1.) |
| 1:10 | Break |
| 1:20 | **Lab 2 (worked):** ~200 Met museum objects with thumbnails. Plot the collection by century; browse what a museum's data looks like — and notice what the catalog *doesn't* record. (That noticing seeds Week 4's Data Biography.) |
| 1:50 | One-slide teaser of the ladder ahead; the standing rituals named. Check-out. |

**Reading (cliffhanger):** the Bollen/Schmidt fight, abstract-and-figure only — Bollen et al. 2021 (PNAS), the "hockey stick" of cognitive distortions counted in Google Books; then the one-page Schmidt/Piantadosi/Mahowald critique: the surge may be an artifact of *which books Google scanned*. Bring the three questions (what did they decide / load-bearing assumption / where's the gap). *Trial next week — including how the authors fought back.* (Population-level mental-health topic; keep the touch light.)
**Sketch:** one question from your life answerable with text or image data; three sentences.
**Check (trace it):** folded into Lab 1's solo turn — one written sentence predicting what your cell does before you run it. *(C1.)*

**Instructor notes.** Protect the wow; roving help catches the silently stuck before the break. The bored coder gets the "go further" cell. Most students arrive already using AI day to day (Claude, Gemini, ChatGPT), a few of them inefficiently — so the frame isn't "here is a new tool," it's "you already use these; this course makes you use them *well*, and read what they hand you." One week-one stance to hold all term: the assistant is plumbing — it writes code so the room can think about culture; it is not the subject.

**On the environment.** Colab's runtime is ephemeral — it wipes on idle or disconnect — so the Week-1 Drive mount is not housekeeping, it's what keeps a student's Week-4 corpus alive to Week 5. Make everyone save to their Drive project folder, and demo re-mounting after a reset once so it isn't scary later. For in-notebook help, Colab's **built-in Gemini** (the spark icon: generate a cell, or fix an error and read the diff) is the primary assistant and keeps the code visible; students already fluent in Claude or ChatGPT can use those instead — the workflow is identical. The Gemini *API key* is a separate thing, needed only for Week 7's annotation pipeline. If a student's Colab keeps disconnecting, **Kaggle Notebooks** is the fallback — its working directory persists with no mount. One thing to *steer away from*: letting a student turn a whole project over to an autonomous agent (Colab's Data Science Agent, or Claude Code) — the course works because they read and question the code, so keep them on cell-level help, not hands-off generation.

---

## Week 2 — Counting Is Already a Model

**Tool one — counting.** Every count hides a choice (tokens, stemming, the corpus itself).
**Competencies:** 3, 5; 8 via the trial.
**Promise:** put a famous PNAS paper on trial, build a word-counter by hand, watch the same sentence get counted three ways — and count an image, too, since pictures are data the same way words are.

**The set-piece — the Bollen/Schmidt trial.** (1) The claim: a hockey stick of societal distress, found by *counting*. (2) The objection: the rising words are fiction-words, and Google scanned more fiction after 2000 — the "surge in distress" might be a surge in novels. (3) The rebuttal, and the move to steal: Bollen et al. didn't argue — they **removed the entire fiction corpus and re-ran it**, and the pattern largely held. The answer to "your corpus is biased" is *test it and show the result.* Land Schmidt's line: the books are "a treasure trove when interpreted with care."

**Data:** two short author passages (printouts); a Gutenberg novel, the Met titles, and a Reddit slice for the cross-corpus counting lab.

| Time | Activity |
|---|---|
| 0:00 | Warm-up retrieval. |
| 0:05 | **The trial (20 min):** claim → objection → re-run-without-fiction rebuttal → "interpret with care." Credit first, always. One named choice is the *chart*: the hockey-stick shape depends on the y-axis and the smoothing window — show how a different axis flattens the drama. The picture is a choice too, and it's the first thing to interrogate. |
| 0:25 | **Delight beat — the fingerprint (5 min, no caveats):** before we complicate counting, enjoy what it already does. The AI pulls the words one artist uses far more than everyone else — the signature vocabulary of a Taylor Swift or a Kendrick Lamar album against a big pop baseline. No interrogation yet; just "counting alone already shows you a voice." Don't qualify it — that's the point. |
| 0:30 | **Hand-built bag-of-words (25 min):** two authors, highlighters, tally the top words. Argue about merging run/running, casing, stop-words. The arguments *are* the lesson: counting requires defining. |
| 0:55 | **What counts as a word? (12 min):** paste the same sentence into two tokenizer playgrounds and watch it shatter differently into colored chips — models never see words, they see tokens, and *which* tokens is a design choice. Connect straight back to the stemming argument you just had: run/running was your version of the same decision. |
| 1:05 | Break |
| 1:15 | **tf-idf (15 min):** the AI scales your hand count; stop-words dominate, which motivates tf-idf — "common here, rare overall." (Zipf's eerie straight line is this week's five-minute supplement to try at home.) |
| 1:30 | **Cross-corpus counting (15 min):** run the same counter on a pop-lyrics slice, a subreddit, and a novel — start with the corpus the room actually lives in. Same code, three corpora; notice how the *corpus choice* changes what "common" means. (Doubles as the corpus sampler before Week 4.) |
| 1:45 | **Counting images (5 min):** pictures are data too. The AI computes a painting's average color and brightness histogram — Rothko vs. a bright pop poster — and a "darkest album cover" ranking. Counting is the same skill on images, and *what you choose to count* (hue? brightness? saturation?) is the same kind of decision as stop-words. Image projects start here and go all the way through. |
| 1:50 | **Gemini-free check + check-out.** |

**Reading:** Stephen Wolfram, "What Is ChatGPT Doing…" — the opening sections only, where even text generation turns out to be built from counting. *Proof that the humble tool you start with underlies the fanciest ones.*
**Sketch:** count something in a text you love; one chart; one sentence naming a choice you made.
**Check (explain it):** two tokenizers split the same sentence differently — explain why, and what your stemming decision changed in the hand count. *(C3, C5.)*

---

## Week 3 — Classification: Counting with Weights

**Tool two — classification.** Train the machine to sort your corpus and *read what it learned*: a logistic regression scoring weighted evidence, its signed weights its mind on the table. A usable capability (sort my corpus, tell me what mattered) and an honest one (you can see and doubt what it leaned on). This is the cheap, transparent reader; Week 7's annotator is the powerful, opaque one — the same job, scaled up.
**Competencies:** 4, 5; 2 (pitch prep).
**Promise:** teach a machine a bias in ten minutes, build a classifier and read its mind — what words it leaned on, where it would fail — and preview the full methods menu before next week's commitment.

**Featured study — Lincoln Mullen, *America's Public Bible* (Stanford University Press, 2023).** Mullen trained a classifier to find biblical quotations across millions of pages of historical American newspapers — a machine that decides, page after page, "is this a quotation of this verse, or not?" You can't just search for the words: the wording drifts (paraphrase, archaic spelling, OCR errors), so the model has to learn the *pattern* of a quotation, exactly the step up from counting that classification is. **Interrogate (room first):** *what counts as a quotation?* — a four-word echo, a loose paraphrase? — is a definition the scholar had to make, and it shapes every number that follows. The model is also reading the same kind of messy digitized text your own project will, so its errors are the errors you'll meet. (An openly-coded, reproducible digital book — the gold standard for "a real scholar doing the thing you're about to do.")

**Data:** students' own faces/objects via webcam (Teachable Machine); a provided **pre-labeled** text dataset (~1,000 rows — e.g. r/AmItheAsshole posts tagged YTA/NTA, or movie reviews tagged pos/neg) for the classifier lab.

| Time | Activity |
|---|---|
| 0:00 | Warm-up + Look at This, then Question It: Mullen's *America's Public Bible* — a classifier finding scripture across millions of newspaper pages. |
| 0:10 | **Teachable Machine — instructor demo (12 min):** train a two-class image model live in minutes. Then the reveal: it was trained on only orange cats and brown dogs; the room *predicts* what a black cat will do; show it. The entire bias concept, planted by a training set, in one beat. **For image projects:** this *is* a classifier on pictures — the same train-it-and-read-what-it-learned move you're about to do on text, on pixels instead of words. Sort album covers, posters, paintings the same way. |
| 0:22 | **Counting with weights — the lab (30 min):** each word casts a weighted vote, *for* or *against*, and the model adds them up — a logistic regression (spam filters work this way). Code it on something the room cares about: a pre-labeled pop corpus (song lyrics tagged by genre or mood, AITA posts tagged YTA/NTA, or film reviews tagged pos/neg). Have the AI train the classifier on word counts, then **read the signed coefficients** — its most positive and most negative words are its mind on the table. Which did it lean on? Do you agree? Where would it fail — can you build it a "black cat"? Reading the weights *is* the lesson; the AI writing the code is plumbing. |
| 0:52 | **Delight beat — what says "breakup song"? (5 min, no caveats):** ask the trained classifier for the words that most predict each class — the vocabulary that most screams "this is a breakup song," or "this reviewer hated it." Just enjoy it; the machine learned a little cultural fingerprint and it's a kick to read. |
| 0:57 | **Where this goes (3 min):** you just built the *transparent* reader — cheap, and you can see exactly what it weighed. Its limit: it only knows the words you gave it, so subtler categories (sarcasm, theme, tone) slip past. Week 7 brings the *powerful* reader — the big model as an annotator you direct and check — which catches what word-counts miss but hides how it decided. The two readers are the matched pair the course turns on. |
| 1:00 | Break |
| 1:10 | **Methods menu preview (15 min)** — the project-eligible methods, so Week 4's choice is informed: counting (done), classification (today), **embeddings** (a map where similar things sit close — the heart of the course, in Week 5), and a short menu of **optional approaches** for specific projects (character networks for fiction with many characters; sentiment arcs for story projects — the emotional shape of a narrative, Jockers's Syuzhet reproducible in Python, whose own smoothing controversy is the built-in lesson to doubt the shape; CLIP image search for visual projects; and, for the technically comfortable, **fine-tuning a small open model — ModernBERT — on your own labels**, the advanced version of Week 3's classifier). Embeddings is where most projects find their richer-than-counting finding. |
| 1:25 | **Pitch prep (20 min):** what makes a tractable question; the corpus-existence rule for next week. |
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
**Promise:** leave with a pitched project, two chosen methods (one swappable in Week 6), your Data Biography drafted — and the one skill that makes "bring your own corpus" real: getting data off the web, from an API or a careful scrape.

**Featured study — a Pudding "How We Made…" process post.** The messy middle: pivots, dead ends, the question that took weeks. Every polished piece had a moment its maker thought it wouldn't work.

**The one data conversation (12 min, not a gate):** the licensing one-pager — CC0 museums and public-domain books: go anywhere; academic-only sets (MovieLens, IMDb, Goodreads scrapes): analyze, don't redistribute; lyrics, review text, chart data: metadata only; AO3 and other community-opposed archives: a small attributed sample at most, never a shared dataset — the community actively fights datamining; live social firehoses: we discuss, we don't scrape (Webis-TLDR-17 and Stack Exchange are the clean-license routes to messy social text); pirated full-text books (LibGen, Anna's Archive): never — the line the field's $1.5B settlement was about. Judgment, not a rulebook.

**Methods on offer:** counting/comparison · classification (the AI as a reader you train and check) · embeddings (text and image) · character networks.

| Time | Activity |
|---|---|
| 0:00 | Warm-up + Look at This: the process post. |
| 0:08 | **Pitches (40 min, 3-minute hard cap each):** my corpus (existence proof shown), my two methods, what would count as a finding. Instructor takes tractability notes for the one-on-ones — listen for vague questions, vibes-chosen methods, and the quiet scaling-down. |
| 0:48 | Break |
| 0:58 | **The data conversation (12 min):** licensing one-pager + the Data Biography introduced (Krause's who/how/where/why/when, plus what's missing). |
| 1:10 | **Getting the data — APIs and scraping (20 min):** where does a corpus *come from*? Two routes, demoed live with the AI writing the code. **API first (the polite front door):** hit an endpoint students already met — the Met or Art Institute, no key — and watch the AI turn a documented URL into a table; name what an endpoint, a key, and rate-limiting are. **Scraping second (the back door, used with care):** when there's no API, the AI writes a small BeautifulSoup scrape of a simple page — and the same breath teaches the four-line check: read the site's `robots.txt` and terms, scrape slowly, take only what you need, never re-publish copyrighted text. The licensing one-pager from ten minutes ago tells you which route is even allowed. |
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

**Featured debate — two readings of the same fact about embeddings.** Embeddings encode the associations latent in a corpus. That single fact is a *warning* to one set of researchers and a *method* to another, and Week 5's critical-reading beat is to hold both and decide what follows.

- **The warning — Caliskan, Bryson & Narayanan (2017), "Semantics derived automatically from language corpora contain human-like biases."** Their WEAT test shows embeddings reliably reproduce human stereotypes: not just flowers-pleasant/insects-unpleasant, but European-American names paired with "pleasant" over African-American names, and "woman" pulled toward domestic words. The point: an embedding is a mirror of its corpus, so a model trained on human text *launders human prejudice* — deploy it in résumé screening or search and you propagate the bias invisibly.
- **The method — Soni, Klein & Eisenstein, "Abolitionist Networks" (2021),** via the authors' general-audience *Public Books* essay "How Words Lead to Justice." The *same* mirror, used to recover history: embeddings trained on nineteenth-century abolitionist newspapers decade by decade reveal which papers *led* new uses of words, and two papers edited by women led much of the movement's language — quantitative weight behind the argument that a multiracial coalition of women stood in abolition's vanguard. (It also shows the optional **networks** method live: aggregate "who led whom" into a leader/follower graph.)

**Interrogate (room first):** these aren't opposite claims — they're the *same* claim ("embeddings reflect the corpus") aimed at opposite goals. So the choice the room has to name: **when is reading a corpus's associations a discovery, and when is it laundering bias?** What makes Soni/Klein scholarship and a biased résumé-screener harm — the data, the purpose, the human in the loop, what gets *done* with the output? (This is the course's deepest lesson in miniature: a method isn't good or bad, it's good or bad *for a purpose*.) The thread runs forward, too: Caliskan's "the model absorbs what's in the corpus, including the ugly parts" is the Week 7–8 training-data-ethics question, already on the table.

**Data:** the project corpus (main event); 100 lyrics/posts from class corpora prepared as TSV for the Projector.

| Time | Activity |
|---|---|
| 0:00 | Warm-up + Look at This, then Question It (room names the choice first): the embeddings debate — Caliskan's bias warning vs. Soni/Klein's historical recovery, same mirror, opposite use. |
| 0:10 | **The beyond-counting moment (15 min):** put Week 2 and today side by side. Run it on something the room enjoys — cluster a beloved artist's songs by mood and era, or cluster characters in a franchise — and watch groupings appear that *counting* couldn't see, because the machine placed them by meaning, not by shared words. (The gendered-adjectives version from Week 2 still works and ties to today's debate; lead with the fun one.) Same question, two tools, the second visibly richer. Name the idea: a word, passage, or picture becomes a vector — a few hundred numbers — with position learned from the company it keeps. The Projector gives two minutes of intuition (neighbors are context-mates, *not* dictionary synonyms — kill that misconception). |
| 0:25 | **Embed your own corpus — text or images (30 min):** the real event, on the student's own data. Text projects embed passages and hunt a surprise cluster; **image projects embed their pictures** — album covers, paintings — and watch them group by style nobody tagged (the same Projector plots both; this is image projects' first deep payoff, not a footnote). The model doing the embedding is an open one from **Hugging Face**, the hub where open models live — worth a nod, since it's where Week 8's period models and the optional fine-tuning method come from too. **And this is where charts stop being neutral.** The scatter you're looking at is a *choice*: switch PCA to t-SNE and the same data rearranges — clusters tighten, distances shift, a grouping you trusted may dissolve. The picture didn't lie; it just made a choice, and so will every chart you publish. The rule lands here, on their own map: a visualization is an argument with decisions baked in (axis, projection, what's shown, what's dropped), and reading one — yours or anyone's — means finding those decisions. Near means probably similar; exact distances mean little. |
| 0:55 | Break |
| 1:05 | **Project lab (40 min):** push your embeddings — more of the corpus, different slices, hunt the surprise cluster — let people *enjoy* the find before the caveats land. **Five-minute aside, recommenders:** "For You" is this same map plus your history — you're a point in taste-space, and the feed is your nearest neighbors. Spotify's own researchers found algorithmic listening is *less* diverse than organic ("diversity" being a metric somebody defined). The instructor runs one-on-ones at the side; pairs and go-further cards cover the floor. *If the cohort is behind, compress the recommender aside and the back half of the lab first; protect the embed-your-own-corpus demo.* |
| 1:45 | **Gemini-free check + check-out.** |

**Reading:** Jay Alammar, "The Illustrated Word2Vec" — through the personality-vectors and king/queen sections (~15 min).
**Sketch:** on your map from class, toggle PCA vs. t-SNE and screenshot how the picture changes; then name one neighbor (or, for images, one cluster) that surprised you and say whether you believe it — real pattern, or projection artifact?
**Check (explain it):** on your map, name one cluster you believe is real and one that's probably a projection artifact — and how you'd tell. *(C4.)*

---

## Week 6 — Deepen the Project: Images, and Where the AI Fails

**Focus:** push the project past first findings — apply the tools (embeddings especially) harder on the student's own corpus, give image projects their deepest day, and calibrate exactly where the AI's reading of *your* data is wrong.
**Competencies:** 1, 4, 7. **(One-on-ones continue.)**
**Promise:** get your richer-than-counting finding working on your own corpus — including images, if that's your project — and find exactly where the AI fails on your data.

**Featured work — Arnold, Tilton & Berke, "Visual Style in Two Network-Era Sitcoms" (2019).** Using computer vision on every shot of *Bewitched* and *I Dream of Jeannie*, they read the *visual grammar* of the shows — how often each character is on screen, how the camera frames them, where it sits — and show the camera itself encoding gender and domestic space differently for each lead. Images as data, done by humanists, with an open toolkit (Distant Viewing) you could run yourself. **Interrogate (room first):** *what counts as a "character-centered shot"?* — the operationalization is the argument, and a different definition tells a different story; two sitcoms is a slice, not "television." It's the perfect companion to your own image embeddings: the same move (turn pictures into measurable features), aimed at a question about culture. (Supplements: Lev Manovich's *Selfiecity*, the same idea at the scale of thousands of selfies; for sentiment projects, the Reagan/Swafford smoothing fight.)

**Data:** project corpus (text or image); an image set (album covers or WikiArt) for the live image-embedding demo.

| Time | Activity |
|---|---|
| 0:00 | Warm-up + Look at This, then Question It — a pair: a *contemporary* visual study leads (e.g. The Pudding's frame-by-frame film color work, or movie-poster trends by genre and decade — this-decade culture the room watches), then Arnold, Tilton & Berke's sitcom camerawork as the rigor case to interrogate. Lead with what they recognize; interrogate with what's cleanest. |
| 0:07 | **Images on the same map, for real (18 min):** the embedding move from Week 5, now on pictures. Embed an image set live — album covers, movie posters — and watch them cluster by visual style nobody tagged. Let this *land* before any critique: it's a genuinely cool thing the room can now do, and that's the point of showing it. (It's also the "beyond counting" contrast at its sharpest — count a museum's labels, then let the images sort *themselves*.) Image-project students run it on their own corpus; text-project students watch, then push their own embeddings harder in the lab. *(Optional take-home spotlights for visual projects: CLIP image search — find images by typing words; and "find the visual echo," embedding-based visual-link retrieval in the spirit of Ommer's art-history work — tracing a repeated pose or composition across a corpus.)* |
| 0:25 | **Project lab (40 min):** apply your method harder on your own data — embeddings clustered and interpreted, or your classifier's labels interrogated. Instructor floats; one-on-ones at the side. *If catch-up time is needed, this lab and the fix-it check flex; the hand-labeling set-piece does not.* |
| 1:05 | Break |
| 1:15 | **The hand-labeling set-piece (Gemini-free, 25 min):** label 30 items from *your* corpus by hand; the AI labels the same 30; study every disagreement. "The AI read it for me" becomes "I know exactly where the AI is wrong on my data." Nobody skips it. *(This stays hand-work on purpose — it's the one beat where coding can't teach the lesson.)* |
| 1:40 | **Fix-it check (8 min):** a planted bug in the data pipeline; find it AI-closed. |
| 1:48 | Check-out. |

**Reading:** a short piece on the AI-as-annotator question to prime Week 7 — Gilardi et al.'s abstract (ChatGPT vs. crowd workers) is enough. *Supplement, for sentiment projects:* the Reagan/Swafford smoothing fight.
**Sketch:** one disagreement between your labels and the AI's where you were right — why? Could it be a moment in your essay? (Image projects: instead, swap the image set or the number of clusters and screenshot how the grouping shifts.)
**Check (fix it):** the planted bug. *(C1, C7.)*

---

## Week 7 — The AI as a Reader, at Scale

**Tool four — LLM-as-annotator.** The single most common operation in computational cultural analysis: hand the model 5,000 items and have it *judge* each one — sarcastic or sincere, which of five themes, feminist-coded or not — categories too subtle for word-counting. It's the natural deepening of Week 3's classifier: there you built a cheap reader whose mind you could see (signed weights); here you borrow an expensive reader far more capable but far more opaque, and the week is about using it without being fooled by it. This is also where the course's pitch lands hardest — the model reads your corpus using judgment it learned from training data nobody audited, much of it scraped creative work — so whose reading are you actually borrowing?
**Competencies:** 2, 4, 5.
**Promise:** use the AI to read your whole corpus at once, learn to trust the labels it's sure of and catch the ones it isn't — and reckon with whose judgment you're renting when you do.

**Featured study — the annotator's dilemma, two papers.** **Gilardi, Alizadeh & Kubli (2023)** found ChatGPT *outperformed* crowd workers on several text-labeling tasks — cheaper, faster, more consistent. Then the counterweight: **the reliability is task-dependent and the model fails silently** — confident wrong answers that a crowd worker's disagreement would have flagged. **Interrogate (room first):** the prompt *is* the codebook (you decide what "sarcastic" means, and a different prompt relabels the corpus); agreement with humans isn't ground truth; and the model's "judgment" is a compression of its training data — so when it labels fan fiction or song lyrics, it's applying patterns learned from *other people's* scraped creative work. Who consented to be the standard?

**Data:** project corpus (the main event); a small labeled gold set per student for the accuracy check; the licensing/training-data reading.

| Time | Activity |
|---|---|
| 0:00 | Warm-up + Look at This, then Question It (room names the choice first): Gilardi — the AI as a cheaper coder, and where it fails silently. |
| 0:10 | **The annotator move, on your corpus (25 min):** write a labeling prompt for *your* categories, run it on a slice, read the labels back. The categories are yours and they're exactly the ones word-counting was too blunt for: does this comment blame a broken system or one person's bad luck; what's the cause of death in each of these sci-fi stories; which horror subgenre is this; is this review sincere or sarcastic. Then the craft: the prompt is your codebook — tighten the definition, add an example, and watch labels shift. The same subjective call you made about stemming in Week 2 and weights in Week 3, now in plain English, and just as consequential. |
| 0:35 | **Confidence, and when to trust it (15 min):** ask the model not just *what* but *how sure* — the probability behind each label (logits, in plain terms: the model's strength-of-evidence, the same idea as Week 3's signed weights, now exposed for the big model). The move that matters: sort by confidence, trust the 95%-sure labels, and **hand-check the unsure ones** — which is exactly which 30 to pull for Week 6's hand-labeling, not a random 30. Confidence is a usable signal, not a guarantee; a model can be confidently wrong, which is why the gold-set check comes next. |
| 0:50 | Break |
| 1:00 | **Accuracy check + project workshop (50 min):** run your prompt against your small hand-labeled gold set — where does the AI disagree with you, and is *it* wrong or are *you*? Then build time on your own corpus, instructor roving, a station for each method. *The workshop half absorbs catch-up time for a cohort running behind; the accuracy check stays.* |
| 1:50 | **Gemini-free check + check-out.** |

**Reading:** one short piece on the training-data fight — the *New York Times* v. OpenAI complaint summary, or a plain-language explainer on the Books3 / pirated-books corpus — paired with the reminder of *your own* Week 4 licensing conversation. The question for class: you spent a whole session getting your corpus ethically; the models reading it for you did not. *(Supplements: Bamman, Chang, Lucy & Zhou, "On Classification with Large Language Models in Cultural Analytics" (CHR 2024) — the field's own account of when to trust an LLM labeler, including the unsettling finding that GPT-4o "succeeds" on a folktale task partly by having memorized the answers, which are Googleable; Underwood's GPT-4 narrative-time study, the literary-history version of the same move; and Gilardi et al. on LLMs vs. crowd workers.)*
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
| 1 | Counting / data journalism | *Pockets* (The Pudding) | Sample scope (80 pairs, few brands) |
| 1→2 | Counting | Bollen et al. 2021 (PNAS) | Schmidt/Piantadosi/Mahowald critique → **Bollen's re-run-without-fiction rebuttal** |
| 3 | Classification | Mullen, *America's Public Bible* (2023) | What counts as a quotation is a definition; the model reads the same messy OCR you will |
| 3 | Networks (optional method) | Beveridge & Shan, "Network of Thrones" | A "tie" is a 15-word window; change it, change the protagonist |
| 5 | Embeddings (+ optional networks) | Soni, Klein & Eisenstein, "Abolitionist Networks" (2021) | "Leading a word" is operationalized; embeddings mirror what survived; ties are a choice |
| 5 | Recommenders (spotlight) | Anderson et al. 2020, Spotify diversity study | "Diversity" is a defined metric; satisfaction is a correlation |
| 6 | Images as data | Manovich, *Selfiecity* / *On Broadway* | Sampling ("selfies in five cities") becomes a claim about a whole city |
| 6 (supp.) | Sentiment / smoothing | Reagan et al., "Six Basic Shapes" | **Jockers *Syuzhet* → Swafford → Schmidt** (the smoothing fight) |
| 7 | The AI as a reader | Gilardi et al. (ChatGPT vs. crowd workers) | The prompt is the codebook; it fails silently; whose training data is the standard? |
| 8 | Period models / memorization | TimeCapsuleLLM + "Speak, Memory" (Bamman lab) | A period model speaks for who got published; name-cloze measures memorization, not reading |
| 2–6 | **Images, as a co-equal corpus** | counting pixels (W2) → classifier on images (W3) → image embeddings (W5) → image projects deepened (W6) | The same four tools, applied to pictures — a full project path, not a separate track; CLIP image search is the one optional add |
| 10 | AI art (send-off) | de Belamy → Ridler → Anadol (market, labor, museum) | Who is the author; whose labor is the data; who decided what went in |

*(Deeper cuts for the curious: Michel et al. culturomics vs. Pechenick's corpus-contamination critique; Juola's Rowling unmasking and its distractor-set caveat; the Netflix Prize and the Narayanan–Shmatikov de-anonymization; Gonen & Goldberg's "Lipstick on a Pig"; Anthropic's "Mapping the Mind" / Golden Gate Claude; Nan Z. Da vs. the Critical Inquiry forum as the field-level fight.)*

## Appendix — Data and Tools by Week

| Week | Primary data / tools | Notes |
|---|---|---|
| 1 | Wedding CSV · Met objects | All provided; CC0; zero risk. |
| 2 | Author passages · tokenizer playgrounds · Gutenberg · Met · Reddit slice · a few images (paintings/album covers) | The cross-corpus counter doubles as the corpus sampler; the pixel-counting beat needs 3–4 images on hand. |
| 3 | Teachable Machine · pre-labeled text dataset (~1,000 rows) | Bias reveal needs a planted skew; the LR lab needs the labeled set. |
| 4 | Bring-your-own from the starter library · a live API (Met/AIC) · the data-collection cookbook · the publishing template | The one licensing conversation; the APIs-then-scraping demo; existence proofs due; project repos born today. |
| 5 | Project corpora · Embedding Projector | Pre-test the embed-your-corpus notebook on every starter corpus; the projection toggle is the homework. |
| 6 | Project corpus (text or image) · an image set (album covers / WikiArt) for the live embed demo | Pre-test the image-embedding notebook; have a CLIP take-home ready for visual projects. |
| 7 | Project corpus · a small hand-labeled gold set per student | The annotator runs on their own data; the gold set is the accuracy check. Pre-test a labeling prompt on a sample corpus. |
| 8 | Student results · TimeCapsuleLLM page · the "Speak, Memory" figure | Screenshots ready as the default; live only if the network cooperates. |
| 9–10 | Student notebooks → pages | — |

**The anchor tools, one link page:** OpenAI Tokenizer / Tiktokenizer · Teachable Machine · Embedding Projector (text and images). Plus, for visual projects, an optional CLIP image-search demo. (Week 7 uses the AI assistant itself.) All free, browser-based, no install — students should leave with this page bookmarked.
