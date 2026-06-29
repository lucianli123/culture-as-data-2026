# Culture as Data — Planning Document
## Instructor's Companion to the Syllabus

*A 10-week community course in computational cultural analysis. This document is the design rationale, pedagogical notes, tool research, prep checklist, and reference library that sit behind the student-facing syllabus.*

---

## Audience and Stance

The course is built for **curious adults**: librarians, journalists, retired teachers, museum educators, hobbyists, working professionals, grad students from non-technical fields. Mixed coding backgrounds — some have light Python, most don't. Humanities and social-science interest assumed. Project-based, not survey.

The instructor's discipline is computational social science. The course leans interdisciplinary by design — Pudding-style data journalism is the dominant register; digital humanities and computational sociology supply the methodological backbone; critical data studies threads through every week as the ethics spine.

The **pedagogical posture** is curiosity-first, not compliance-first. Every "rigor" moment in the course is reframed as detective work. The AI is treated as an instrument with known failure modes, not an oracle. The deliverable is public, not academic. Cookies in Week 10.

---

## Design Principles

### 1. Lead with destinations, then interrogate them
Every week opens with a five-minute "Look at This, then Question It" — a finished study or article that did something interesting with the week's method. Students see *what success looks like* before they're asked to attempt it. This is the single biggest structural decision in the course. It changes the affect from "we will now study a technique" to "look what this technique can do; how would you use it?"

The ritual has a second beat that is as important as the first: after admiring the piece, the room names *what the authors chose and what they could have chosen instead.* The featured work is never presented as settled truth — it is presented as a set of defensible decisions, some of them arguable. See Principle 5a for the full rationale; the short version is that seeing destinations and learning to second-guess them are the same five minutes, and the course refuses to teach the first without the second.

### 2. Project-based, with the artifact and the analysis separated
Every student produces two things: a **reproducible notebook** (the evidence of analysis — "I must be able to run it," per Mullen's standard) and a **web essay** built on top of it in Act 3 (the communication layer). The form is consistent across the class (so the instructor can teach the build once); the content is each student's own. Drawing the destination clearly in Week 1 — projecting *Pockets* and saying "you will publish something shaped like this" — is more pedagogically powerful than any methods rationale.

The separation is deliberate. The project-based-learning and cognitive-load literature warns that a polished-artifact requirement can teach a *different* skill (front-end and visual design) than the intended one (analysis), and that asking novices to learn analysis methods *and* a publishing toolchain at once overloads working memory (Mayer's segmenting and pre-training principles). The notebook is the analytical record and a short essay is the communication, evaluated separately — the way Walsh, Underwood, and Mullen assess. The essay is the thing students *show*; the notebook is the proof of the thinking. See Principle 12.

### 3. Three acts, with rebalanced weight
- **Weeks 1–3 (Tour):** Shared toy datasets, all four methods sampled, no commitments. Goal: students learn what's possible before they pick anything.
- **Weeks 4–7 (Project):** Commit by Week 4, then four weeks of guided iteration. Method deep-dives in 5 and 6; spotlights and workshop in 7.
- **Weeks 8–10 (Publish):** Three weeks of scaffolded delivery. Week 8 settles findings and drafts prose; Week 9 builds; Week 10 shows.

**Three weeks of publish scaffolding is the minimum that's realistic for a non-technical cohort building their first interactive web page.** Compressing publishing into a single working week does not work; the build reliably takes longer than expected. The publishing toolchain is also pre-built and named in Week 1 (pre-training principle), so Act 3 spends working memory on the essay, not on first contact with Quarto.

### 4. Methods buffet, honestly described
Four core methods, met in the Tour and chosen at commitment: **counting and comparison**, **classification** (a transparent classifier you train and read — Week 3), **embeddings** (text and image — the heart of the course), and **AI annotation** (the big model as a reader you direct and verify — Week 7, the most-used operation in the field). The two reading-tools are a matched pair: the cheap reader whose mind you can see (W3) and the powerful, opaque one whose mind you must probe (W7), with the hand-labeling set-piece (W6) the calibration check between them. Two-to-three methods in ten weeks is sampling, not mastery, and the syllabus says so. The tools map to weeks — counting (W2), classification (W3), embeddings (W5), AI annotation (W7) — so picking a method and understanding it are the same thread; embeddings is where most projects find their richer-than-counting finding. **Character networks** stays an optional method for fiction with many characters, and **narrative sentiment arcs** (Matthew Jockers's *Syuzhet* in R; trivially reproducible in Python — score emotion across a story, then read its shape) is the optional method for the genre-fiction projects, both offered like stylometry. The Syuzhet arc carries its own caveat for free: the Jockers–Swafford–Schmidt smoothing fight, over whether the Fourier smoothing *manufactures* the arc, is the course's cleanest "interrogate your own output" lesson — landing on the very tool the student is holding. **Fine-tuning a small open model is the optional advanced method, and it completes the reader theme.** The two reading-tools are a *pair* for the general student — the transparent W3 classifier and the powerful, opaque W7 annotator — but for the technically comfortable there is a **third reader**: fine-tune an open encoder (`ModernBERT`, a modern faster BERT, on Hugging Face) on the student's own labels, ending with a classifier that is theirs, free to run, private, and far faster than prompting for a narrow repeated task. It slots in naturally after the annotator week, because the training data is exactly the labels the student just made (hand-labeled in W6, AI-labeled at scale in W7). It is also the concrete payoff of the open-vs-closed thread the ethics weeks build: not just critiquing closed models, but running and training open ones whose data is more knowable. It is **deliberately not core** — fine-tuning is the single biggest complexity jump available to this audience (datasets, tokenization, the Trainer loop, GPU memory, checkpoints) and the most fragile thing to run on free Colab's ephemeral runtime, so half the cohort would stall on it. It lives as a `cool-methods` notebook and a Week-7 "go further," serving the technical students (the software engineers, the comfortable scripters) without burdening the beginners. Spotlights (recommender systems as a five-minute Week 5 aside answering the pitch's Netflix/Spotify hook; CLIP image search for visual projects; running an open model in place of the closed annotator API) give tastes of what didn't fit; stylometry, color analysis, diachronic meaning, and reception live as starter notebooks for independent pursuit.

Topic modeling is deliberately absent. Its outputs are the hardest for novices to read responsibly — the interpretability critique is a literature of its own — and the mechanism ladder doesn't need it: classification and embeddings carry the same conceptual load with better-behaved outputs. Networks take its seat: visual, intuitive, and home to one of the best admire/interrogate examples in the field (the *Game of Thrones* co-occurrence window).

### 5. Examples paired to every method
Each main method gets a paired study in Week 3 (when introduced) and a paired *Look at This* in each subsequent week. The bibliography is organized by method, not by author. Students don't have to read most of these — they see them projected, react to the charts, and the references are there if they want more.

### 5a. Read the masters critically — authors make choices, not truth
A distinct learning goal, and the basis for the seventh competency: students should leave able to read a published study or data essay and *see the choices behind it* — and to internalize that finished, celebrated work is made by people who decide what to count, what to exclude, where to draw lines, and what to claim, and who sometimes get it wrong. The target affect is calibrated: admiration and skepticism held at once. The non-goals are equally important — this is **not** cynical debunking, and **not** "all research is just opinion." A study can be rigorous *and* contestable; teaching students to see the contestability without losing respect for the rigor is the whole skill.

**Visualization is folded into this, not taught as a separate unit.** A chart is the same interpretive-choice problem as a count, applied to a picture: a truncated axis, a binning decision, a projection (PCA vs. t-SNE), a color scale, and what's left off all shape the reading the way the *Syuzhet* smoothing manufactured arc shapes. The course threads it three ways rather than adding a charting curriculum a general audience doesn't need: (1) **reading** — "Look at This" already uses charts (the *Pockets* chart, the hockey-stick axis), so the room names the chart's choices alongside the data's, at no added time; (2) **the concept lands in Week 5** — the embedding scatter is the first visualization-as-argument, and the PCA/t-SNE toggle (already the Sketch) is the live demonstration that the picture is a choice; (3) **making** — a Week 9 "interrogate your own chart" beat, the making-side mirror of Week 6's hand-labeling, turns the term's skepticism on the student's own visualization before publishing (zero-baseline axis, manufactured trend, what the chart hides). The principle: students who spend ten weeks interrogating others' charts must interrogate their own — otherwise the course drops its central move at the exact moment it matters most.

How it is built into the course, so it's a through-line rather than a slogan:
- **The weekly ritual carries it.** "Look at This, then Question It" appends an interrogation beat to every featured piece: *what did they choose, what could they have chosen, where might this be wrong?* (Principle 1.)
- **A reading lens carries it.** Every assigned reading comes with three standing questions — what did the authors decide, what's the load-bearing assumption, where's the gap — and these are opened up in class.
- **A hands-on set-piece carries it.** Week 2 puts a famous study on trial — claim, published objection, and the authors' test-it-and-show-the-result rebuttal — so students rehearse the skill on a real scholarly fight, and meet the robustness move they'll later use on their own work.
- **It comes home to their own work.** The "show your work" appendix and the Data Biography are explicitly framed as doing to one's own project what the term has done to the professionals' — naming your own choices and where a reader could disagree. The arc runs from interrogating others to owning the same kind of choices yourself, which both demystifies expertise and raises the student's own honesty.

**Instructor caution.** The failure mode is a room that learns to sneer. Guard against it actively: pair every critique with genuine credit for what the work achieved, model disagreeing-with-respect, and intervene if "what did they choose?" curdles into "so it's all garbage." The point is that good work survives scrutiny and is more impressive for it — not that scrutiny destroys it.

### 6. Social media as cultural data
Three of the six Week 2 tour stations are social-media corpora. The corpus library has a substantial post-API-era section. The Week 4 lab includes specific walkthroughs for Bluesky, Mastodon, Reddit, and Pushshift mirrors. This is where most curious adults live now; the course meets them there.

### 7. Four tools, taught to the depth that changes what a student can do
The course teaches four ways to turn culture into something a machine can analyze, and the ordering principle is *capability*, not architecture: each tool expands what a student can do with their own corpus past the one before. The test for every mechanism beat is one question — **does understanding this change what you can do, or what you'll trust?** If yes, it's in, at the depth that changes the student's hands. If it's intellectual appreciation — real but inert for their project — it's an optional spotlight or it's cut. This test is what keeps the course teachable for a librarian rather than calibrated for someone who finds the architectures intrinsically fascinating.

- **Counting** (Week 2) — frequencies, distinctive features; powerful, and the honest floor (no notion of meaning).
- **Classification** (Week 3) — train the machine to sort the corpus and *read what it learned*; a logistic regression whose signed weights are inspectable. A real capability and an honest one. It is the cheap, transparent reader of the matched pair the course turns on; Week 7's annotator is the powerful, opaque one — the same job scaled up. No neural-network mechanism is taught: it would change nothing the student can do.
- **Embeddings** (Week 5) — **the heart.** Items become vectors; similar things land near each other; "what clusters in my corpus" becomes askable. The single biggest leap past counting, and the week the course's whole promise pays off.
- **The AI as a reader, at scale** (Week 7) — have the model *judge* every item in the corpus (which of five themes, sarcastic or sincere), the most common real operation in the field and the natural deepening of classification. Capability = label at scale and trust it appropriately (read the confidence, hand-check the unsure); the reckoning = whose judgment you borrow, since the model learned to read from scraped creative work. A little mechanism earns its place here — confidence/logits as a usable trust signal — because it changes what the student does next.

The through-line — the course's actual signature — is **moving a question beyond counting on the student's own data**: count adjectives near *she* vs. *he* in Week 2, then *embed* them in Week 5 and see the gendered clusters counting couldn't. Run that before-and-after two or three times across the term; it teaches "beyond counting" far better than exposition. Depth is conceptual-visual throughout — no linear algebra, no calculus. Each beat is **experience-first, name-second, scale-up-third**. The repeated sentence: *it's all turning culture into vectors and learning the weights, and the leap past counting is letting the machine place things by meaning instead of just tallying them.*

**Images are a co-equal corpus, taught through the same four tools — because the capability is identical**, not because the course tours vision architectures. Counting works on color and brightness (W2); classification sorts album covers and reports its visual features (W3, Teachable Machine, already live); embeddings place paintings near each other by untagged style (W5–6, the same Projector plots both). A student can run an entire project on visual culture as a first-class case: image corpora in the starter library, the cookbook pulls museum image APIs, the embeddings lab runs on their pictures, the essay shows image clusters. What images do *not* get is the CNN's internals or a vision-transformer tour — a student clustering album covers needs that no more than the lyrics student needs attention math. The one genuinely thrilling visual *capability*, CLIP (search images by typing words), survives as a single optional spotlight for visual projects, offered the way stylometry is offered to text projects. The discipline to hold: keep image work to capability, never let it grow into an architecture lecture.

**Anchor tools** (free, browser-based, no install), reused all term: a tokenizer playground (W2), Google Teachable Machine (W3), and the TensorFlow Embedding Projector — which plots text and images (W5). Week 7's tool is the AI assistant itself, used as an annotator. The embedding models come from **Hugging Face**, the open-model hub — named in Weeks 5, 7, and 8 so students know where open models (and the optional fine-tuning method) live. A CLIP image-search demo is the one optional add, for visual projects. A small familiar kit beats a parade of novelties.

**Misconceptions are the real target.** Novices reliably believe the model *understands*, *looks things up in a database*, or *is magic* — and each belief is corrected by demonstration, not lecture: tokenizer surprises kill "it reads words"; the Teachable Machine bias reveal kills "it just knows"; the Playground spiral kills "someone wrote the rules" (the net learns features no one coded); and Week 7's gold-set check kills "the AI just knows" — the model is confidently wrong on a measurable fraction, which is why you verify it. The shift shows up where it's used: the Week 7 explain-it check (what is your prompt deciding, and how would you know whether to trust a label?) and the Week 10 oral walkthrough, which asks what each tool shows and hides alongside the result.

**Coding vs. hand-work, deliberately split.** Mechanism is learned by *coding* it with the AI and then reading the result — Week 3's logistic-regression lab is the model: the AI writes the training code (plumbing), the student reads the signed weights (the lesson). Hand-labeling is reserved for the one place it teaches something code can't: Week 6, where labeling 30 items the AI also labels, by hand, is the only way to feel *where the AI's reading of your data is wrong*. That set-piece stays manual on purpose; every other place a method is learned, the student codes it with the AI and reads the result.

**Recommenders close a promise-gap, briefly.** The pitch indicts the Netflix/Spotify feeds, so the embeddings week owes an answer: a recommender is the same map plus your history — "For You" is your nearest neighbors in taste-space. A five-minute Week 5 aside (not a matrix-factorization lesson — students don't need the mechanism, only the idea that they're a point on a map of meaning), with Anderson et al.'s Spotify finding as the admire/interrogate study. The deeper "machines trained on our culture" stakes the ad leads with are paid off in Week 8's "Speak, Memory" beat, where students actually probe what a model memorized.

**Period-trained models are the spine's cultural payoff.** Week 8 reframes "what is a trained model" as *a compression of its corpus* — then shows models whose corpora were bounded on purpose: TimeCapsuleLLM (1800s London only) and, inverted, "Speak, Memory" (probing which books GPT-4 memorized) — with MonadGPT (17th-century) and MacBERTh (the scholars' historical English) as supplements. This loops the Week 2 trial at full scale — corpus composition isn't a bias to apologize for; bounded deliberately, it's the instrument — and it gives the diachronic thread a modern home. It also keeps the LLM weeks from collapsing into chat-assistant literacy: the destination is culture, not the chatbot.

**On framing the annotator:** lead with the capability (it reads thousands of items the way a human coder would, in minutes), then immediately the discipline (the prompt is the codebook; it fails *silently*, so confidence-sorting and a gold-set check are not optional). Resist letting it drift into "how the transformer works" — that's a different course's subject and doesn't change what the student can do. The "What Surprised You?" check-outs keep building use-based intuition for where the AI fails.

### 8. Curiosity-flavored, not compliance-flavored framing
Standard academic and professional courses borrow institutional language ("limitations," "ethics protocol," "AI use statement") that signals seriousness but kills curiosity. This course reframes those moments as detective questions. The epistemic work is the same; the affect is different. See the "Reframing Language" table at the end of this document.

### 9. Data Biography as the ethics carrier, in one strong pass
The course's data ethics live in a single, serious Data Biography (Krause's framework: who collected it, how, where, why, when — and who's missing), written at commitment in Week 4, where it can respond to a real corpus choice, and distilled into the essay's corpus note in Week 8. One pass, not a recurring unit. The licensing one-pager (CC0 → academic-only → metadata-only → community-opposed → never-pirate) is delivered in the same Week 4 conversation — judgment students can carry, not a compliance gate.

The mechanism spine now carries much of the ethical load through demonstration: the Week 3 bias reveal (*you* taught the machine that bias, with your training set), Week 2's "what counts is a choice," Week 8's "plausible continuations, not facts." Ethics through mechanism tends to stick better than ethics as paperwork; the tradeoff — less iterative reflection across the term — is accepted deliberately, and the easiest re-expansion if a cohort wants more is restoring a mid-course Biography revision.

### 10. Honest about AI failure modes
The AI is treated as an instrument with documented failure modes, not an oracle. The course explicitly teaches:
- **Illusion of competence** (Prather et al., ICER 2024): code that runs is not code that's right.
- **Shifting goalposts** (Prather et al., 2024): students unconsciously scale down their question to match what the LLM can produce. The Week 5–6 one-on-ones are partly there to catch this.
- **Cognitive offloading and skill atrophy** (Kosmyna et al., MIT EEG study, 2025): students who never work without an AI assistant cannot later reproduce their own work.
- **Insecure code generation** (Veracode 2025): ~45% of LLM-generated code contains exploitable security weaknesses.
- **Low-resource language failure** (Jadhav et al., 2024): LLMs underperform fine-tuned baselines on non-English text.

Two structural responses are built in:
- **The Gemini-free block.** Every weekly session includes a ~20-minute block where the AI is closed (see *How Each Week Actually Works*). The research evidence on cognitive debt makes this non-negotiable.
- **Static HTML + SVG as the default final-essay format**, with JavaScript as an opt-in that triggers an additional code-review step. This is the responsible default given current LLM front-end security findings.

**The unblocking kit (the practical-survival layer).** The above teaches students to *distrust* the AI; this teaches them to *recover* when it fails them — the single biggest practical risk to the course, since the whole edifice rests on Gemini writing runnable code for non-coders, and the lived failure mode is code that runs but is subtly wrong, or a traceback a non-coder can't parse, with one instructor for the room. Three parts, introduced Week 1 at the first AI-writes-code moment and referenced in every lab:
1. *Self-rescue protocol (student-facing, on the wall):* (a) read the **last line** of the error aloud — it usually names the problem; (b) paste the **full traceback** back to the AI with "this errored, fix it and tell me what went wrong"; (c) if still stuck after two tries, flag the instructor and move to your partner's screen meanwhile. The protocol matters as much as any fix: it keeps a stuck student *moving* instead of frozen.
2. *The "common errors" cheat sheet:* the 6–8 errors a non-coder will actually hit — missing/blank API key, rate-limit message, wrong file path, empty dataframe, package-not-installed, malformed output from the AI, quota exceeded, notebook disconnected — each with the exact paste-back phrasing. Pre-built, printed, and committed to the repo. This is a build task on the prep checklist.
3. *Classroom escalation path:* pairs first, cheat sheet second, instructor last — so one instructor is never the bottleneck for a room of stuck people. The Recurse "no backseat driving" rule still applies; helping a stuck partner read an error is not backseat driving.

### 11. Recurse Center social rules, with onboarding
Four norms borrowed from a programming retreat for adults who don't have a CS degree: no feigning surprise, no well-actually's, no backseat driving in pair sessions, no subtle -isms. These do more pedagogical work for a mixed-experience adult cohort than any other single design choice.

A practitioner-blog warning (Chopra 2020, "Misunderstanding What It Takes To Make Recurse Center's Social Rules Work") is direct: the rules don't work by being posted. They require active onboarding. The Week 1 opening therefore includes 20 minutes where the instructor deliberately breaks each rule and demonstrates the correction — including the rule that the instructor isn't exempt. The rules are protective, not policing. The evidence base is Edmondson's psychological-safety research: safety is established behaviorally (leaders model fallibility, frame work as uncertain, respond appreciatively to candor), and safety must be paired with genuine standards — the "learning zone" needs both. The competency checks (Principle 12) are those standards; without them, a safe room drifts to apathy.

### 12. Assessment without grades: competencies, checks, and a portfolio
The course is built around a real risk: that a student can finish, publish a good essay, and have learned to *direct* an AI without learning to *do* the analysis. The cognitive-offloading literature (Kosmyna et al. 2025; the "illusion of competence" and "metacognitive laziness" findings) makes that risk concrete — fluency-on-demand produces a feeling of understanding that outruns the real thing, especially in novices with weak self-regulation. A polished artifact therefore cannot be the evidence of learning. The assessment design responds, mirroring how comparable courses assess and grounded in the assessment-*for*-learning literature:

- **Eight named competencies** are the spine (read code, ask a tractable question, name what a method hides, read results skeptically, explain how the AI works and when to trust it, write a Data Biography, judge AI-generated code, and read a finished study or data essay for the choices behind it). They are stated to students on day one and are the criteria for everything below.
- **Weekly AI-free competency checks** in the Gemini-free block: code-tracing ("predict the output / what does this cell do"), oral "explain your last result," and debug-a-planted-bug. These are the most AI-resistant instruments available — tracing and oral explanation cannot be outsourced in real time (the 2025 ICER tracing study; the oral-assessment literature). Ungraded; their purpose is to surface the run-vs-understand gap early. (Two competencies live partly outside the Gemini-free checks: critical reading of others' work sits in the weekly "Look at This, then Question It" beat, the Week 2 trial, and the "show your work" appendix — see Principle 5a; and judging-what-the-tools-show-and-hide is built across the weeks and measured by the explain-it checks — tokenizers in Week 2, the classifier's weights in Week 3, the annotator's confidence and gold-set check in Week 7 — and the oral walkthrough; see Principle 7.)
- **A process portfolio ("workbench") with criteria fixed in advance**: the reproducible notebook, the Data Biography, one revised-after-feedback artifact, and a reflective intro. Fixed explicit criteria are necessary because the competency-portfolio validity literature shows assessors anchor on holistic gestalt judgments and resist disconfirming evidence (Oudkerk Pool et al.). The portfolio is the backbone; the essay is one artifact in it, not the whole.
- **An oral walkthrough** (mid-course and at the showcase): "walk me through how you got this and what it does NOT show." The AI-resistant capstone.
- **AI-closed work as a standing condition**: the weekly Gemini-free block, plus the Week 6 hand-labeling set-piece (students label 30 items the AI also labels, then study every disagreement), turns the central risk into a learning instrument by making the gap visible to the student.
- **Peer feedback is formative only.** The meta-analytic evidence is that peer assessment helps *learning* (Double et al. 2020, g ≈ 0.31) but is unreliable as *measurement* (self-assessment especially; peers tend to over-mark). So it is never scoring — and where a judgment needs to be reliable, peers compare two works rather than rate one in isolation (the Adaptive Comparative Judgement finding).

No-grades is not no-standards. The course simply puts the standards in competencies and checks rather than in marks — appropriate for a non-credit community course, and consistent with the Carpentries' ungraded-but-formative model.

### 13. Pedagogy mechanics grounded in cognitive science
The weekly structure is engineered, not improvised. The load-bearing mechanics and their evidence:

- **Faded worked examples → completion problems (expertise reversal).** Act 1 gives full worked notebooks; Act 2 shifts to completion problems (blanked notebooks) offered in parallel *fuller-guidance* and *skeleton* versions. The worked-example effect is one of the best-replicated findings in instructional psychology, but it reverses with expertise (Kalyuga; Renkl & Atkinson) — so a single worked example mistargets a mixed cohort. Parallel versions and fading are how one room serves a first-timer and a software engineer at once. This directly addresses the "is the audience coherent enough to teach as one?" risk.
- **Productive failure with a consolidation step.** The "Look at This" / try-before-told move is well-founded (Kapur; Sinha & Kapur 2021 meta-analysis, g ≈ 0.36) — *but only with the contrast-and-consolidate step* (compare students' flawed attempts before revealing the canonical method). Without it the effect disappears ("When Productive Failure Fails"). The course implements it twice: Week 3's bias reveal (students predict the black-cat outcome before testing, then compare predictions) and, most fully, Week 7's annotator — students trust the AI's labels, then the gold-set check reveals where it was confidently wrong, and the consolidation is the move from "the AI read it for me" to "I know which labels to trust and why."
- **Retrieval and spaced practice.** Each session opens with a 5-minute AI-free, ungraded retrieval warm-up, made *cumulative* so early methods stay live in later weeks. Distributed practice and practice testing are the two highest-utility techniques in Dunlosky et al.'s review; the once-weekly project structure otherwise risks each week becoming an island.
- **Interleaving across rungs, blocking within one.** The cumulative warm-ups and the ladder's own design keep earlier rungs live inside later ones (tokens reappear in Week 8; counting reappears in classification), and the Week 3 methods preview lets students discriminate which method fits which question before committing — but within a single rung's first exposure, practice is blocked (beginners benefit from blocking first, interleaving once competent).
- **Participatory live coding** (the Carpentries' core method): instructor types and narrates, students follow, with explain-then-type to avoid split-attention, and deliberate mistake-and-recovery (which also models the fallibility psychological safety needs). Experienced learners get optional extension prompts so they're not pinned below their level.
- **Skill-matched pair programming with timed role rotation.** The pair-programming evidence is genuinely mixed and moderated; the documented failure mode is a large skill gap disengaging the novice. So pairs are matched by rough level where possible, roles rotate on a timer (enforcing the no-backseat-driving rule), and large gaps use the expert as a rover rather than a fixed partner.
- **Self-regulated-learning structure for the one-on-ones** (Zimmerman's forethought → performance → reflection cycle). Detailed in *Mid-Course One-on-Ones*, below — the course's highest-leverage tutoring lever.
- **Structured critique (Critical Response Process).** Week 9 critique uses Liz Lerman's four-step process (statements of meaning → maker questions → neutral questions → permissioned opinion), which protects the maker's agency and forces specificity, countering the studio-critique failure mode where critique turns performative or authority-dominated.

---

### 14. A joy budget, protected on purpose
The course's pedagogical spine is "admire, then attack" — interrogate every study, kill your own finding, find where the AI fails. That rigor is correct and it is also, unrelieved, exhausting for a volunteer audience attending by choice after a workday. So delight is **budgeted and structurally protected**, not left to chance: roughly every other week carries a **Delight beat** — one finding or capability shown *just because it's cool, with no caveat attached.* It is the one moment the critical-reading reflex is switched off on purpose, and the instructor must resist the trained urge to qualify it. The ledger: Week 1 (the day-one investigation itself), Week 2 (an artist's signature-word fingerprint), Week 3 (the words that most say "breakup song"), Week 5 (the surprise-cluster hunt on your own corpus), Week 6 (album covers clustering by untagged visual style), Week 9 (your own work live at a public URL), Week 10 (the showcase). Weeks 4, 7, and 8 are the working/serious weeks where the delight is the *doing* — the pop hands-on slot carries the relatability there instead. The pleasure-to-rigor ratio is a design variable; this is the course tending it deliberately.

### 15. Pop culture in the hook and the hands, scholarship in the interrogation
The featured academic studies (Mullen, the Caliskan/Soni-Klein debate, Arnold/Tilton/Berke, the time-capsule models) are best-in-class *as objects of interrogation* — their operationalization lessons ("what counts as a quotation," "what counts as a character-centered shot") are cleaner than most pop-culture studies, which are often methodologically loose. So they hold the **interrogation slot**, where rigor is the asset. But the field's center of gravity is historical text scholarship, and left unchecked it pulls the whole course toward a digital-humanities seminar the target audience didn't sign up for. The correction is a ratio rule: **every week also shows the student their kind of culture, from their decade, in the hook or the hands-on slot.** Target — at least half the "Look at This" warm-ups and the majority of lab/worked examples are contemporary popular culture (streaming, pop music, fan communities, social media, this-decade film and TV). The academic paper is what the room *critiques*; the pop corpus is what they *build on*. The discipline is to watch the cumulative ratio, not the individual choice: optimizing each anchor for "best scholarship" quietly optimizes the whole course away from "speaks to this audience," because the field's strongest work skews historical and textual.

### 16. Making over reading, on balance
A diffuse correction that the pop hands-on slots, the joy budget, and the pivot kit all serve: the course can over-index on the critical-reading competency and produce a skeptical *reader* of cultural analytics better than a confident *maker* of it — which is likely inverted from what this audience wants (they came to make a cool thing, not mainly to doubt things). The critical-reading ritual stays — it is the spine, and naming choices is the whole intellectual move — but the *weight* of each session should land on the student building and finding, not only doubting. In practice: protect the lab floor over the ritual when minutes are short (already the priority rule), keep the Delight beats uncaveated, and ensure the assessment portfolio rewards a finished, defensible artifact at least as much as a sharp critique.

### 17. Slack in the arc, and a pivot kit for projects that fail
Ten weeks produces ~12 weeks of work, and real cohorts fall behind early; some projects will also fail outright. Two mechanisms absorb both, neither adding to the calendar:

**Slack (the pacing valve).** Created by marking what is *droppable*, per the "garnish dies first" priority rule, not by adding time. The floating catch-up valve lives in Weeks 5–7: each has a named compressible element (Week 5's recommender aside and back-half lab; Week 6's project lab and fix-it check; Week 7's workshop half) that a cohort running behind borrows from — while the protected floors (the hand-labeling set-piece, the accuracy check, the embeddings demo) stay. And **Week 8's robustness arc is explicitly reducible to a single pass** — one robustness check that most threatens the finding, plus compression — when projects need the session to settle. The full sweep is the ideal, not the floor.

**The pivot kit (the contingency).** For the student whose corpus turns out unusable or whose question has no findable answer. Three parts, surfaced at Week 4 commitment and used in the Week 5–6 one-on-ones where stalls first appear:
1. *Fallback corpus-and-question bank:* 6–8 pre-vetted pairs (corpus + question known to yield a finding in the time available), spanning text and image, pop-weighted. Cover the recurring interest-types so a pivot feels lateral rather than a defeat: a **genre-fiction** corpus with a trope-or-feature question (causes of death across sci-fi stories, how horror subgenres trap their characters — a natural showcase for the Week 7 annotator); a **self-improvement / advice forum** with a behavior question (what a community like r/getdisciplined treats as within a person's control); an **argument forum** with a stance question (what actually moves a position on r/changemyview); **song lyrics** with a change-over-time question (has vocabulary converged across a decade); an **image set** (album covers or posters by visual style); and a **structured-records** set with a trend question (restaurant openings and closures by type and city). Each is a project a stalled student can adopt in Week 5 and still finish. Tagged in the corpus library so they're findable; building/testing them is a prep-checklist task.
2. *The "stuck project" protocol:* three escape routes — narrow the question, swap the corpus (keep the question), or swap the question (keep the corpus) — with the one-on-one as the decision point.
3. *The null-result reframe:* "I expected X and the data doesn't show it, and here's how I know" is a complete, honest, publishable project. Stated at Week 4, reinforced whenever a project wobbles. It removes the failure stigma that makes students cling to a dying idea past the point of rescue.
4. *Two mismatches to catch at the pitch, before they cost a student three weeks.* First, **audio-feature music questions** — "did music get more homogeneous" in the well-known studies means timbre and loudness measured from the audio signal, which the course's text-and-image tools don't reach. Redirect to what the tools *do* serve well: lyrical convergence (vocabulary diversity over a decade), metadata and genre patterns over time, or a pre-computed audio-feature table treated as plain rows for counting and embeddings. Second, **politically fraught or data-blocked topics** — influence-operations detection, the X/Twitter firehose, "foreign actors" — are both inflammatory and largely inaccessible now that the platform API is paywalled. Redirect to the tractable version of the same curiosity: how a topic is *framed* across different public communities (subreddits, forums), or sentiment toward a specific policy in open text. The aim is to move the student to a finishable question inside their own interest, not to talk them out of the interest.

## How Each Week Actually Works

The week-by-week script — minute-by-minute flows, featured studies with their paired critiques, datasets, and checks — lives in `lesson-plans.md`. The notes below are the instructor-judgment layer: the why, and the what-to-watch-for.

**The priority rule, when minutes run out (they will):** Act 1 protects the mechanism block, Act 2 protects project lab time (a 45-minute floor), Act 3 protects writing and building. The Look-at-This ritual is hard-capped at five to seven minutes — one piece, one named choice, never a gallery — and it shrinks before the lab does. Garnish dies first.

**Pacing and the Gemini-free block.** Run each session as 5–6 segments of ~20–25 minutes (ritual, mechanism block, lab, break, lab, wrap), not monolithic blocks — working memory can't take it (Cognitive Load Theory; Sweller 2023). One of those segments, ~20 minutes, is AI-closed and non-negotiable (Kosmyna et al. 2025; Prather et al. 2024): announce it ("AI tabs closed"), place it where the week needs it (Week 6's hand-labeling, Week 8's writing block), and name the resistance — "it feels worse without the assistant; that's the learning."

### Weeks 1–3 (Tour)
- **Week 1**'s job is unchanged: lower the barrier and create a "moment" by the first break — one complete tiny investigation, end to end. Two things get set that pay off later: the social-rules-by-modeling-fallibility opening and the vocabulary pre-training. Full worked notebooks, participatory live coding. The stance to hold from day one: the assistant is plumbing, not the subject — it writes code so the room can think about culture. (The template fork lives in Week 4, where the project repo is born.)
- **Week 2** carries the trial — credit first, then the objection, then the test; if the room tips toward "so it's all fake," you've mis-run it — and the hand-built bag-of-words, where the arguments about stemming and casing *are* the lesson. The tokenizer playgrounds turn that same argument into a design choice you can watch: "what counts as a word" is the week's whole thesis. The cross-corpus counter doubles as the corpus sampler before Week 4. Land the spine sentence for the first time here. (Zipf is a take-home supplement; don't spend class time on it.)
- **Week 3**'s Teachable Machine is a twelve-minute *instructor demo*, not a lab — planted skew prepared in advance (orange cats, brown dogs, one black cat), explicit predict-before-you-test beat. The lab is a single coding build — the AI trains a logistic regression on a *provided pre-labeled* dataset and the students read its signed weights (resist running two classifier builds in one session). The weight-reading is the learning; don't let it slide into hand-labeling. The methods-menu preview must be just enough to choose by — say out loud that the embeddings mechanism arrives in Week 5, and put the Thrones 15-word-window catch on the table during the networks taste, so the interrogation travels with the method. Assign the corpus existence proof.

### Week 4 (Commit)
- The pitches remain the most important hour of the term: 3-minute hard cap, existence proofs enforced (no proof, no pitch). Listen for questions too vague to answer, corpora that don't exist as accessible data, methods chosen for vibes, and the quiet scaling-down of ambition to what the AI does easily; address these privately in the one-on-ones.
- The data conversation is one pass, judgment not rulebook: the licensing one-pager plus the Data Biography assignment. **Data collection lands here too** — a 20-minute APIs-then-scraping demo (the AI writes the `requests`/BeautifulSoup code; students learn what an endpoint, a key, rate-limiting, and `robots.txt` are, and when scraping is and isn't allowed), then the cookbook notebook becomes the collect-it homework that *is* the corpus-existence proof. Placed in Week 4 because that's where bring-your-own-corpus bites; it costs no mechanism rung and Week 4 has no lab floor to defend. Notebooks switch from fully-worked to completion problems — have both guidance levels ready.

### Weeks 5–7 (Project)
- Working weeks: a short mechanism block, a long project lab, the instructor floats. Completion problems, skill-matched pairing with timed role rotation, and cumulative warm-ups are the standing mechanics.
- **Week 5 is the heart of the course** — embeddings, the biggest leap past counting. Lead with the *problem* (counting can't relate *happy* and *joyful*), then the beyond-counting contrast on the student's own data (count adjectives near she/he in Week 2, embed them now). The block runs on students' *own* corpora — that merge protects the lab floor. Kill the dictionary misconception explicitly (neighbors are context-mates, not synonyms); the projection caveat is one spoken sentence plus the homework toggle. Images embed on the same map (the Projector plots both) — image projects get their deep day in Week 6, but the parallel is named here. The recommender close is a five-minute aside (you're a point on a map of meaning), strictly boxed. **The critical-reading beat is a debate, not a single study:** Caliskan (embeddings launder bias — a warning) vs. Soni/Klein (embeddings recover history — a method), same mirror aimed at opposite goals. Run it as the interrogation — the room decides *when reading a corpus's associations is discovery and when it's laundering bias* — capped at the usual 5–7 minutes; it's the cleanest "a method is good or bad for a purpose" lesson in the course, and it seeds the Week 7–8 training-data thread (Caliskan's "the model absorbs the corpus, ugly parts included"). First-wall week, and one-on-ones begin — run them at the side while pairs and go-further cards cover the floor.
- **Week 6** deepens the project rather than teaching a new architecture: apply the tools (embeddings especially) harder on the student's own corpus, and give image projects their deepest day — embed an image set live and watch it cluster by untagged style, the "beyond counting" contrast at its sharpest. The Manovich opening (*Selfiecity*) is the critique rep — sampling becomes a claim about a whole city — capped at seven minutes. The hand-labeling set-piece stays and is non-negotiable — the one beat where coding can't teach the lesson. CLIP is an optional take-home for visual projects; Reagan/Swafford a supplement for sentiment projects.
- **Week 7** teaches the most-used operation in the field — the AI as a reader at scale — as the fourth tool and the deepening of Week 3. Hold the discipline: the prompt is the codebook (tighten it, watch labels move); confidence-sorting tells you which 30 to hand-check in Week 6; the gold-set check catches silent errors. This is also the anchor for the training-data-ethics thread — whose scraped creative work taught this reader — so pair it with the Week 4 licensing callback. Do *not* let it drift into transformer mechanics; that's a different course. The back half is project build time.

### Weeks 8–10 (Publish)
- **Week 8**: the opening is two items only — TimeCapsuleLLM and "Speak, Memory," screenshots as the default (small hosted demos are flaky); MonadGPT and MacBERTh are supplements, not class time. Kill-your-finding and settling are *one continuous arc* on the students' own results: shuffle, split, "compared to what?", then compress what survived into one sentence in the same sitting. No new methods; resist the temptation.
- **Week 9** is the build session. With prose drafted and the toolchain familiar since the Week 4 fork, the lab focuses on the essay. The comparative reading of three published essays lands "no single right way, only choices you can defend." Critique uses the Critical Response Process, not generic draft-trading. Students leave with a deployed URL.
- **Week 10** is the showcase, with the two highest-value assessment moments: the **oral walkthrough** (now "how did you get this, what does it NOT show — and how do the tools actually work?") and the **workbench intro**. Run the closing triptych credit-first — three artworks, one question — and keep it to the opening minutes; the day belongs to the students' work. The room is the validation; these two moments are how you and the student confirm the eight competencies landed.

---

## Mid-Course One-on-Ones (Weeks 5 and 6)

Each student gets a 20-minute slot, outside class; schedule the calendar block before Week 1. This is the course's tutoring lever — the highest-leverage individual intervention available (on the order of VanLehn's ~0.79σ for human tutoring, not the mythical 2σ), so protect it.

Structure each session on Zimmerman's three-phase self-regulation cycle rather than a loose chat:

**Forethought (looking forward).**
- What's your question, and what would count as a finding worth reporting?
- Which two methods, and why those?
- What's your success criterion for the next week?

**Performance (looking at now).**
- What are you tracking week to week? Show me.
- Where are you stuck? (Watch here for the quiet scaling-down — the unconscious shrinking of the question to fit what the AI does easily. This is the documented "shifting goalposts" failure mode; the one-on-one is where you catch it.)

**Self-reflection (looking back).**
- What will you change next week?
- Set one concrete, checkable goal. You'll review it at the next session.

End every one-on-one with that single written goal. Self-recording against a goal is the mechanism Zimmerman's own studies show drives skill gains. This is also the moment to flag any student who's drowning — far better to surface in Week 6 than Week 9.

---

## The Assessment Framework (Instructor Detail)

The course has no grades, but it has standards, and they are legible. This section is the operational detail behind Principle 12.

### The eight competencies (the criteria for everything)
Stated to students on day one; they are the rubric for the portfolio and the target of the weekly checks.
1. Read a block of analysis code and say what it does, line by line, without running it.
2. Ask a tractable question of a pile of cultural data — specific enough to answer, honest about what it omits.
3. Name what a method assumes and what it hides.
4. Read an embedding map, a classifier's labels, or a character network skeptically — real pattern vs. pretty accident.
5. Judge what each tool shows and hides, and the ethics of the data behind them — explain in plain language what counting, classification, embeddings, and AI annotation reveal and conceal; read an AI's confidence to know which results to trust; and reckon with training data scraped from creative work. (See Principle 7.)
6. Write a Data Biography.
7. Judge AI-generated code instead of just running it.
8. Read a published study, data essay, or chart and see the choices behind it — name the interpretative decisions its authors made (including how a visualization frames its case: axis, scale, what's shown and dropped), where it could have gone differently, where it might be wrong, and turn the same eye on the student's own charts before publishing. (Distinct from #3: that one is method-level and abstract; this one is about a specific finished work and its authors' decisions.)

### The weekly check calendar (in the Gemini-free block)
Rotate the three instrument types so every competency gets touched more than once:

| Week | Check type | Targets competency |
|---|---|---|
| 1 | Trace it (predict output of a demo cell) | 1 |
| 2 | Explain it (why two tokenizers split a sentence differently; what your stemming choice changed) | 3, 5 |
| 3 | Explain it (read your classifier's top weights — what it learned; one input where it would fail) | 4, 5 |
| 4 | Explain it (your question, what it omits, where the data comes from) | 2, 6 |
| 5 | Explain it (one real cluster vs. one projection artifact on your map) | 4 |
| 6 | Fix it (planted bug in the data pipeline) | 1, 7 |
| 7 | Explain it (what your labeling prompt decides; how you'd check whether to trust a label) | 2, 5 |
| 8 | Explain it (your headline finding + what it doesn't show) | 3, 4 |
| 9 | Fix it (a planted bug in publishing/layout code) | 1, 7 |
| 10 | Oral walkthrough (the capstone) | all eight |

These are diagnostic, not graded. Their value is that the run-vs-understand gap surfaces to the student early. If a student consistently can't trace or explain their own code, that is the signal to intervene — gently, in a one-on-one — long before the showcase.

**Competency 8 (critical reading) is tracked outside this calendar,** because it isn't an AI-free code task. Its touchpoints are the weekly "Look at This, then Question It" beat (room-led from Week 5 on), the Week 2 trial, the comparative reading of three published essays (Week 9), and — as the student's own demonstration — the "show your work" appendix. **Competency 5's other evidence** is the run of explain-it checks (tokenizers in Week 2, the classifier's weights in Week 3, the annotator's confidence and gold-set check in Week 7) and the oral walkthrough, which asks "what does each tool show and hide?" alongside "what does your result not show?"

### The workbench (process portfolio) — fixed criteria
Collected as a single folder/repo. Criteria are fixed in advance (necessary because the validity literature shows assessors anchor on holistic impressions otherwise):

- **Reproducible notebook** — runs top to bottom on the instructor's machine; prose cells explain each step. (Competencies 1, 2, 3, 4.)
- **The Data Biography** — one full pass (Week 4), visibly engaged with the student's actual corpus rather than generic; its distilled form is the essay's corpus note. (Competency 6.)
- **One revised-after-feedback artifact** — a before/after showing a change made in response to a critique or one-on-one. (Evidence of the feedback loop working.)
- **Reflective intro** — one paragraph at the showcase: "what I can do now that I couldn't in Week 1," mapped to the eight competencies. (Metacognition; assessment-as-learning.)

The web essay is *one artifact in the workbench,* not the whole portfolio and not the measure of learning.

### What "good" looks like without grades
For each competency, the instructor can hold a simple three-level internal read — *not yet / getting there / solid* — used only to decide where to spend one-on-one time, never reported as a mark. Mastery-learning logic applies: the point is to catch "not yet" early and provide a corrective loop, not to rank.

### Reliability guardrails
- Peer feedback is formative only; never a score. Where a peer judgment should be reliable, have peers compare two works rather than rate one in isolation.
- Self-assessment is for reflection, never measurement (the reliability evidence is poor).
- The oral walkthrough is the most trustworthy single signal, because it is the one an AI cannot fake on the student's behalf.

---

## Affording the AI: Provider Research

As of May 2026, the realistic options for getting students cheap or free AI access. The instructor should pick a primary, document it in the syllabus, and surface the alternatives.

**Default recommendation: Google AI Studio + Gemini API.**
- aistudio.google.com. 1,500 requests/day on Gemini 2.5 Flash. No credit card. Vision included on the free tier.
- 1M-token context window.
- Trade-off: free-tier prompts may be used for training. Fine for this course's public corpora; don't paste sensitive data.
- This is the strongest free option of any provider as of May 2026.

**Backup: Groq free tier.**
- console.groq.com. LPU-accelerated inference, very fast.
- ~30 RPM, ~14,400 RPD on Llama 3.1 8B (the workhorse model).
- No vision on most free models — pair with Gemini for image work.
- Useful for the Week 6 annotation pipeline (high request count, small batches).

**OpenRouter free models.**
- openrouter.ai. ~28 models with `:free` suffix including DeepSeek V3 and Qwen3 variants.
- 50 RPD, 20 RPM per model.
- Useful for a Week 6 "robustness check" comparing two open models.

**Paid options if you want them:**
- Anthropic Claude API direct — $5 starter credit, then ~$1–$5 per million tokens on smaller models.
- OpenAI API — similar tiers.
- $20/month chat subscriptions (Claude Pro, ChatGPT Plus, Gemini Advanced) — polished web interface, no API for batch work.

**Truly free, fully local: Ollama.**
- ollama.com. Install, pull a model (`ollama pull llama3.2`), run as HTTP server.
- Works on Macs with M-series chips, Windows/Linux with 16GB+ RAM.
- No internet required after initial download. No data leaves the machine.
- Performance slightly behind hosted models but adequate.

**Compute:** Google Colab's free tier (intermittent T4 GPU) handles every method in this course — BERTopic, sentence-transformers, CLIP. Colab Pro at $10/month is optional.

### Suggested cohort default
Gemini API free as primary, Groq free as backup, one paid provider's $5 starter credit as an optional taste. Total student spend: $0 by default, up to $20 if someone wants a month of a chat subscription. Document the choice in the syllabus before Week 1.

### Tools for chat and coding
Practical recommendation for the typical student:
1. Open **Google AI Studio** in a browser tab for general chat. Free.
2. Use **built-in Colab AI (Gemini in Colab)** for code inside notebooks. Free, zero setup, already integrated.
3. Get a **Gemini API key** when Week 7 arrives, for the annotation pipeline. Free, paste into a Colab secret.

For students who want more polished tooling:
- **GitHub Copilot Free** — 2,000 completions + 50 chats/month, requires GitHub account.
- **Continue.dev** — open-source VS Code extension, bring your own key.
- **Cursor**, **Windsurf** — polished AI-native IDEs ($15–$20/month with free tiers).

For terminal-comfortable students:
- **Aider**, **OpenCode**, **Gemini CLI** — all open-source, free if BYOK.

### Privacy note
Free tiers from Gemini, OpenRouter, and Groq reserve the right to log requests for training. The course's corpora are public; this is fine. If a student's project involves sensitive data, switch to a paid API or run locally with Ollama.

---

## Instructor Prep Checklist

### Before Term 1 (one-time)
- [ ] **Read the "AI in the Classroom" required-background section** of the bibliography. The course's pedagogical decisions about AI follow from this literature; teaching the course without internalizing it will produce a different, worse course.
- [ ] **Decide on the AI access plan.** Default: Gemini API free + Groq backup. Document it.
- [ ] **Build the "Look at This, then Question It" slide deck** — 10 slides, screenshot + paragraph each, *plus* one prepared "arguable choice" per featured piece (the credit, then the decision a reasonable person could contest). Update each term.
- [ ] **Prepare the Week 2 trial packet** — the Bollen hockey-stick figure, the Schmidt critique's fiction-frequency figure, and the rebuttal's re-run-without-fiction result, staged as claim → objection → test. Rehearse landing "a treasure trove when interpreted with care" without tipping the room into "it's all fake."
- [ ] **Build a `cool-methods/` folder** with starter notebooks for stylometry, emotion arcs, color analysis, diachronic meaning, reception. (Character networks now live in the main completion-problem bank as a core method.)
- [ ] **Build a `social-media-starters/` folder** with working examples for Bluesky firehose, Mastodon API, PRAW Reddit (including a Reddit-fiction loader for r/nosleep and r/HFY), HuggingFace Pushshift loader, a Project Gutenberg public-domain genre-fiction loader, and a Letterboxd/Goodreads scraper template.
- [ ] **Build a Data Biography template.** ~400 words across the six prompts. Provide as a Quarto template students fork. Include one fully-worked example using a starter corpus.
- [ ] **Build the static-HTML Quarto template** that is the default Week 9 deliverable. The template should require zero JavaScript and produce a complete essay layout. Students fork it in **Week 4**, the day their projects commit — the repo is born with the project — and push a live URL that day. Students who opt into JS modify from there.
- [ ] **Build a completion-problem bank.** For each core method (counting, classification, embeddings, networks), a fully-worked notebook *and* two Act-2 versions — fuller-guidance and skeleton. This is the expertise-reversal mechanism; it's the most labor-intensive prep item and the most important for the mixed cohort.
- [ ] **Build a competency-check bank.** For each week, a "trace it" cell, a planted-bug "fix it" snippet, and an "explain it" prompt, mapped to the check calendar in the Assessment Framework section.
- [ ] **Build the workbench/portfolio template** — a repo skeleton with slots for the notebook, the Data Biography, the revised-after-feedback artifact, and the reflective intro.
- [ ] **Prepare the Critical Response Process one-pager** for Week 9 critique, and rehearse facilitating it.
- [ ] **Pre-write the Week 1 social-rules onboarding script** — the four micro-demos where you deliberately break each rule and demonstrate the correction. ~15 minutes total. Rehearse it.
- [ ] **Prepare the Week 7 annotator kit** — a worked labeling-prompt notebook (write prompt → run on a slice → read labels → request per-label confidence → sort and spot-check), a small hand-labeled gold set per starter corpus for the accuracy check, and the training-data reading (NYT v. OpenAI summary or a Books3 explainer). Rehearse the prompt-is-codebook beat: tighten one definition live and show labels shift.
- [ ] **Build the anchor-tools link page** — tokenizer playground, Teachable Machine, Embedding Projector — and dry-run each on the classroom network. (Week 7 uses the AI assistant itself; rehearse a labeling prompt that yields a clean confidence spread on a sample corpus.)
- [ ] **Rehearse the Week-1 Drive-mount ritual** — every notebook's first cell mounts Drive and sets a project-folder path; confirm the cookbook and outputs write there, and practice re-mounting after a forced runtime reset so it can be demoed calmly. Confirm Colab's built-in Gemini is visible on the teaching account (18+/locale); have Google AI Studio ready as the fallback, and a Kaggle notebook ready for any student Colab keeps disconnecting.
- [ ] Pilot Week 6's annotation lab on a sample corpus. Pilot Week 9's Quarto-publish flow end-to-end.

### Before Week 1 (each term)
- [ ] Set up class GitHub organization. Provision starter Colab and Quarto repos.
- [ ] Pre-build the Week 2 notebooks: the hand-count scale-up, the tokenizer comparison, the tf-idf demo (Zipf is a take-home supplement), and the cross-corpus counter (a novel, museum titles, a Reddit slice).
- [ ] Pre-build Week 3: the Teachable Machine image sets (including the planted skew), a provided pre-labeled text dataset (~1,000 rows) with a logistic-regression-and-read-the-weights notebook, and the two methods-preview notebooks (Projector with preloaded words; the *Thrones* graph).
- [ ] **Build the "common errors" cheat sheet** (the unblocking kit): the 6–8 errors a non-coder will actually hit, each with exact paste-back phrasing; print it and commit it to the repo. Pre-test by deliberately triggering each error in Colab.
- [ ] **Build and test the pivot-kit fallback bank:** 6–8 corpus-and-question pairs, each verified to yield a finding in the time available, pop-weighted, spanning text and image. Tag them in the corpus library.
- [ ] **Build the data-collection cookbook notebook** (Week 4, also the Week-3 existence-proof tool): a worked API pull (Met/AIC, no key) and a small, polite BeautifulSoup scrape, each with the AI writing the code and a `robots.txt`/ToS/rate-limit/anti-republish checklist inline. Pre-test both on the classroom network.
- [ ] Refresh the starter corpora list (verify access still works for each).
- [ ] Confirm showcase venue and snacks for Week 10. Tell students Week 1 that strangers will be there.
- [ ] Print social rules card for every student.
- [ ] Mirror all online readings to a course folder (in case anything goes offline mid-term).
- [ ] Schedule the mid-course one-on-ones (Weeks 5 and 6) in your own calendar — 20 minutes per student.

### Ongoing during the term
- [ ] Walk students through the chosen AI provider in the Week 1 lab — API key, Colab secret, quota check.
- [ ] **Run the weekly competency check** in the Gemini-free block, following the check calendar. Keep a private not-yet / getting-there / solid read per student to decide where one-on-one time goes. Never report it as a mark.
- [ ] **Enforce the Gemini-free block every session.** Announce it. Watch for students secretly tabbing back to the assistant. The whole point is the discomfort.
- [ ] **Read each student's Data Biography (after Week 4)** and write a short response. This is the ethics intervention; it cannot be skipped. Check that it engages the actual corpus — who's missing, what it can't say — rather than generic boilerplate.
- [ ] **Open each session with the cumulative retrieval warm-up** — 5 minutes, from memory, AI closed, reaching back to earlier weeks, not just last week.
- [ ] Maintain the fallback corpora list; share with any student whose project collapses by Week 4.
- [ ] Update the "Look at This" deck if a relevant new piece is published.
- [ ] **For any student whose corpus is not in English:** ensure they hand-label a small validation sample for the AI-as-reader method. LLMs underperform on low-resource languages by measurable margins; without validation the annotation step is unreliable.

---

## Reframing Language

This is the operating principle. Throughout the course, institutional language gets replaced with curiosity-flavored equivalents that do the same epistemic work without killing affect.

| Compliance flavor | Curiosity flavor |
|---|---|
| Limitations paragraph | What your AI helper would have to be told to know |
| Ethics checkpoint | Who's not in your dataset, and what would they say if they could see it? |
| Validation requirement | Where did the AI make a confident mistake, and what does that tell us? |
| AI Use Statement | What surprised you? |
| Reproducibility | Could a friend run this on Tuesday after one coffee? |
| Project proposal | Pitch the essay you'd want to read |

---

## Models We're Borrowing From

The course's pedagogical DNA traces back to:

- **The Pudding** — visual essay as the deliverable form. The single most influential reference; students see Pudding pieces every week.
- **NYT Graphics, Reuters Graphics, FiveThirtyEight** — long-form data-journalism craft.
- **Mike Bostock & Observable** — interactive notebooks as a publishing format.
- **Lev Manovich's Cultural Analytics Lab** — image-based cultural analysis at scale (Selfiecity is the model).
- **Mona Chalabi** — hand-drawn lines as epistemic humility.
- **Recurse Center** — social rules; the "I don't know" culture for adult learners.
- **Programming Historian** — lesson-as-recipe pedagogy.

---

# The "Look at This" Library

Every featured example, by week. Update the deck each term as new pieces are published.

| Week | Featured | Type |
|---|---|---|
| 1 | The Pudding, "Pockets" (Diehm & Thomas 2018) | The genre itself |
| 6 | Manovich et al., *Selfiecity* (2014) | Images as vectors / cultural analytics at scale |
| 3 | The Pudding, "She Giggles, He Gallops" (Daniels 2017) | Counting |
| 4 | A Pudding "how we made it" process post | Project pivots |
| 5 | Juola identifies Rowling as Galbraith (2013) | Stylometry |
| 6 | Reagan et al., "Six Basic Shapes" (2016) | Emotion arcs |
| 7 | Beveridge & Shan, "Network of Thrones" (2016) | Character networks |
| 8 | Garg et al., "100 Years of Stereotypes" (2018) | Embeddings, diachronic |
| 9 | Three published web essays (Pudding + Observable + Quarto) | The publication form |
| 10 | (Showcase — no Look at This) | — |

---

# Annotated Bibliography of Cool Studies

Organized by method. Students don't have to read these — they see the headline finding projected and react to the chart. The references are here for the curious, the curriculum-revisers, and the instructor. Each one is also material for "Look at This, then Question It" and the Week 2 trial: for any piece you feature, come prepared with one interpretative choice its authors made that a reasonable person could argue with (corpus boundary, unit of analysis, what got operationalized as what, what's claimed vs. shown). Credit first, then the choice.

### Counting
- **The Pudding, "She Giggles, He Gallops"** (Daniels, April 2017) — gendered verbs in 2,000 screenplays. The icon of the form. pudding.cool/2017/08/screen-direction/
- **The Pudding, "Plain Language"** (Daniels 2016) — SOTU reading-level decline
- **The Pudding, "Pockets"** (Diehm & Thomas, August 2018) — measured pockets in 80 pairs of jeans
- **Bamman, Underwood & Smith, "The Transformation of Gender in English-Language Fiction"** (*Cultural Analytics* 2014) — gendered character description in 100,000 novels
- **Andrew Piper, "Fictionality"** (*Journal of Cultural Analytics* 2016) — linguistic features distinguishing fiction from non-fiction

### Classification & LLM-as-Reader
- **Lincoln Mullen, *America's Public Bible*** (Stanford University Press, 2023; americaspublicbible.org) — **the Week 3 classification anchor.** A classifier detecting biblical quotation across millions of newspaper pages; "what counts as a quotation" is the interpretive choice, and the open code + reproducible-book form is the model deliverable
- **Bamman, Chang, Lucy & Zhou, "On Classification with Large Language Models in Cultural Analytics"** (CHR 2024) — **the Week 7 anchor.** Field-specific account of the interpretable-vs-accurate tradeoff (ties W3's readable logistic regression to W7's powerful-but-opaque LLM) and the memorization/contamination problem (GPT-4o "wins" folktale ID by having seen the labels — Googleable)
- **Ted Underwood, "Using GPT-4 to measure the passage of time in fiction"** (2023) — the literary-history version: GPT-4 as coder tracks human coders on fictional-time; prompt-is-codebook, agreement-isn't-truth, trained-on-these-novels. A Week 7 paired example
- **Gilardi, Alizadeh & Kubli, "ChatGPT outperforms crowd workers for text-annotation tasks"** (PNAS 2023) — the foundation paper
- **Törnberg, "Best Practices for Text Annotation with Large Language Models"** (*Sociologica* 2024) — practical guide
- **Ziems, Held, Shaikh, Chen, Zhang & Yang, "Can Large Language Models Transform Computational Social Science?"** (*Computational Linguistics* 2024) — rigorous benchmark across 25 tasks
- **Bail, "Can Generative AI Improve Social Science?"** (PNAS 2024) — synthesis with caveats
- **Argyle, Busby, Fulda, Gubler, Rytting & Wingate, "Out of One, Many"** (*Political Analysis* 2023) — silicon sampling, controversial
- **Ollion, Shen, Macanovic & Chatelain, "The Dangers of Using Proprietary LLMs for Research"** (*Nature Machine Intelligence* 2024) — the critical counterpoint

### Embeddings
- **Soni, Klein & Eisenstein, "Abolitionist Networks"** (*Journal of Cultural Analytics* 2021) — **the Week 5 featured study.** Diachronic embeddings identify which abolitionist newspapers led semantic change (two women-edited papers led the vanguard); read via the authors' general-audience *Public Books* essay "How Words Lead to Justice." Doubles as the live demo of the optional networks method. Open code + Dataverse embeddings
- **Vicinanza, Goldberg & Srivastava, "A deep-learning model of prescient ideas"** (*PNAS Nexus* 2023) — a **deeper cut**: contextual-embedding "surprise" that drops over time marks prescient ideas, which emerge from a field's periphery (the Stennis/Eastland civil-rights example is gripping). Show the *finding*, not the perplexity machinery, given the no-math audience
- **Kozlowski, Taddy & Evans, "The Geometry of Culture"** (*ASR* 2019) — class meaning shift over a century
- **Garg, Schiebinger, Jurafsky & Zou, "Word embeddings quantify 100 years of gender and ethnic stereotypes"** (PNAS 2018)
- **Caliskan, Bryson & Narayanan, "Semantics derived automatically from language corpora contain human-like biases"** (*Science* 2017) — the WEAT paper, and **the Week 5 debate foil to Soni/Klein**: the *same* fact (embeddings mirror the corpus) read as a warning (laundered prejudice) rather than a method (historical recovery). The interrogation is the tension between the two, not either alone
- **Bolukbasi, Chang, Zou, Saligrama & Kalai, "Man is to Computer Programmer as Woman is to Homemaker?"** (NeurIPS 2016) — founding bias-in-embeddings paper
- **Allison Parrish, *Articulations*** (2018) — generated poetry from phonetic embedding walks

### Image Analysis
- **Arnold, Tilton & Berke, "Visual Style in Two Network-Era Sitcoms"** (*Journal of Cultural Analytics* 2019) — **the Week 6 featured study.** Computer vision reads gender in the camerawork of *Bewitched* and *I Dream of Jeannie*; "what counts as a character-centered shot" is the operational choice. Accessible, humanist, reproducible via the open Distant Viewing Toolkit
- **Ommer et al., visual-link retrieval in art history** (e.g. "Unsupervised Learning of Visual Links" / Heidelberg HCI work) — a **deeper cut + optional image-project spotlight**: embedding-based "find the visual echo," tracing a repeated pose or composition across paintings; connects to intellectual-influence detection
- **Manovich et al., *Selfiecity***  (selfiecity.net, 2014) — 3,200 selfies from five cities
- **Manovich, *Cultural Analytics*** (MIT Press 2020) — textbook of the field
- **Arnold & Tilton, "Distant Viewing"** (*DSH* 2019) — film stills, news photos, museum collections
- **The Pudding, "Colors of Motion"** (Clark 2017) — average color frame-by-frame in films
- **Saleh & Elgammal, "Large-scale Classification of Fine-Art Paintings"** (2015) — 81,000 paintings classified

### Stylometry
- **Burrows, "Delta: A Measure of Stylistic Difference"** (*LLC* 2002)
- **Juola, "Rowling and 'Galbraith': An Authorial Analysis"** (*Language Log*, July 2013)
- **Mosteller & Wallace, *Inference and Disputed Authorship: The Federalist*** (1964) — founding case
- **Eder, Rybicki & Kestemont, "Stylometry with R"** (*RJ* 2016) — practical guide

### Emotion Arcs
- **Reagan, Mitchell, Kiley, Danforth & Dodds, "The emotional arcs of stories are dominated by six basic shapes"** (*EPJ Data Science* 2016)
- **Dodds & Danforth, Hedonometer** (hedonometer.org) — Twitter happiness over time
- **Jockers, *Syuzhet*** R package (2014) — sentiment-arc analysis for novels
- **Vonnegut's "Shapes of Stories"** lecture (YouTube) — the conjecture that started it

### Character Networks
- **Beveridge & Shan, "Network of Thrones"** (*Math Horizons* 2016)
- **Moretti, "Network Theory, Plot Analysis"** (*New Left Review* 2011) — Hamlet's network
- **Elson, Dames & McKeown, "Extracting Social Networks from Literary Fiction"** (ACL 2010)

### Diachronic
- **Hamilton, Leskovec & Jurafsky, "Diachronic Word Embeddings Reveal Statistical Laws of Semantic Change"** (ACL 2016)
- **Michel et al., "Quantitative Analysis of Culture Using Millions of Digitized Books"** (*Science* 2011) — the Google Ngram paper, plus the Pechenick critique

### Social Media as Cultural Data
- **Baumgartner, Zannettou, Keegan, Squire & Blackburn, "The Pushshift Reddit Dataset"** (ICWSM 2020) — foundational corpus paper
- **Botzer, Gu & Weninger, "Analysis of Moral Judgment on Reddit"** (IEEE TCSS 2022) — AITA as a moral-judgment corpus
- **Salganik, *Bit by Bit: Social Research in the Digital Age*** (Princeton 2018, open access at bitbybitbook.com) — the textbook for ethical social-media research
- **Fiesler, Beard & Keegan, "No Robots, Spiders, or Scrapers"** (ICWSM 2020) — what scraping is actually allowed
- **Freelon, "Computational Research in the Post-API Age"** (*Political Communication* 2018) — prophetic essay on API closures
- **Massanari, "#Gamergate and The Fappening"** (*New Media & Society* 2017) — classic mixed-methods Reddit study
- **Counting Feminicide / Data + Feminism Lab** (Catherine D'Ignazio et al., MIT) — model for community-facing data work accountable to the people in the data

### Deeper Cuts (optional, never required)
Available for students who want to go further:
- Moretti, *Distant Reading* (2013)
- Underwood, *Distant Horizons: Digital Evidence and Literary Change* (2019)
- D'Ignazio & Klein, *Data Feminism* (2020, open access at data-feminism.mitpress.mit.edu)
- Bender, Gebru, McMillan-Major & Shmitchell, "On the Dangers of Stochastic Parrots" (FAccT 2021)
- Crawford, *Atlas of AI* (2021)
- Risam, *New Digital Worlds: Postcolonial Digital Humanities* (2018)
- McQuillan, *Resisting AI* (2022)

### Field Self-Critique (optional — scholars turning the lens on their own field)
- **Underwood, "How Not to Do Things with Words"** (*Journal of Cultural Analytics* 2019) — the architect of distant reading on his own missteps
- **Klein, "Distant Reading after Moretti"** (lklein.com 2018) — reframing the lineage in light of who got to read
- **Crawford & Paglen, "Excavating AI"** (excavating.ai, 2019) — what's in the training data of the models students will use

### Methodological Critique (optional, for the curious)
- **Da, "The Computational Case against Computational Literary Studies"** (*Critical Inquiry* 45(3), 2019) — the polemic against CLS
- **Bode, "What's the Matter with Computational Literary Studies?"** (*Critical Inquiry* 49(4), 2023) — the more productive successor critique
- **Piper, *Enumerations: Data and Literary Study*** (Chicago, 2018) — depth-on-one-question as constructive counterpoint
- **Nguyen, Liakata, DeDeo et al., "How We Do Things With Words"** (*Frontiers in AI* 2020) — cross-disciplinary survey of methodological tensions

### AI in the Classroom — Required Background for Instructors
The course's posture toward AI is informed by:
- **Prather, Reeves, Leinonen et al., "The Widening Gap: The Benefits and Harms of Generative AI for Novice Programmers"** (ICER 2024) — direct empirical observation of the illusion-of-competence and shifting-goalposts failure modes in 21 novices
- **Kosmyna, Hauptmann, Yuan et al., "Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task"** (MIT Media Lab, arXiv:2506.08872, 2025) — EEG evidence of cognitive debt; structural foundation for the Gemini-free block
- **MDPI *Information*, "Fluency Illusion: A Review on Influence of ChatGPT in Classroom Settings"** (17(3), 299, 2026) — synthesis review of 41 publications introducing "fluency illusion" as the central explanatory construct
- **Veracode, "2025 GenAI Code Security Report"** — industry-wide testing finding ~45% of AI-generated code contains exploitable security weaknesses; foundation for the static-HTML default
- **Shahid et al., "The Hidden Risks of LLM-Generated Web Application Code"** (arXiv:2504.20612, 2025) — security evaluation across major LLMs including Gemini
- **Jadhav et al., "On Limitations of LLM as Annotator for Low Resource Languages"** (arXiv:2411.17637, 2024) — LLMs underperform fine-tuned baselines by 10–14% on Marathi annotation; basis for the non-English validation requirement

### The Mechanism Spine — Teaching Resources (basis for Principle 7)
- **Financial Times, "Generative AI exists because of the transformer"** (ig.ft.com, free) — the best single lay walkthrough of how an LLM works; an optional deeper-cut for the curious, outside the taught curriculum
- **Gilardi, Alizadeh & Kubli, "ChatGPT outperforms crowd workers for text-annotation tasks"** (PNAS 2023) — the Week 7 featured study; pair with the caveat that reliability is task-dependent and failures are silent
- **The training-data fight (Week 7 reading cluster):** the *New York Times* v. OpenAI complaint (and reporting summaries); the Getty Images v. Stability AI suits; reporting on the **Books3** corpus of pirated books inside the Pile; and the **Bartz v. Anthropic** settlement — the $1.5 billion class settlement over training Claude on ~7 million books pirated from LibGen and PiLiMi, where the court held training on lawfully-acquired books to be fair use but the pirated downloads not. The most concrete teaching case in the cluster, and pointedly about the maker of the model writing students' code. Plain-language explainers are fine — the point is that the models reading students' corpora were trained on creative work scraped largely without permission, in direct contrast to the Week 4 licensing conversation. Verify current status before teaching; these cases move
- **Stephen Wolfram, "What Is ChatGPT Doing… and Why Does It Work?"** — the opening sections build generation up from counting; the Week 2 reading
- **Jay Alammar, "The Illustrated Word2Vec"** (jalammar.github.io) — the personality-vectors framing; the Week 5 reading. His "Illustrated Transformer" is the denser go-deeper.
- **3Blue1Brown, neural-network series + "But what is a GPT?"** — unmatched visuals; use curated clips only (the backpropagation/calculus chapters are out of scope for this audience)
- **Andrej Karpathy, "[1hr Talk] Intro to Large Language Models"** — the first ~40 minutes are genuinely general-audience; a deeper cut for the curious
- **Transformer Explainer** (poloclub.github.io/transformer-explainer; Cho, Kim, Karpekov et al., arXiv:2408.04619) — a live GPT-2 in the browser; an optional deeper-cut for students curious how the assistant works, outside the taught curriculum
- **LLMs Unplugged** (llmsunplugged.org; ANU Cybernetic Studio; CC BY-NC-SA, Zenodo doi:10.5281/zenodo.17403824) — a dice-built bigram activity; a deeper-cut if a student wants to feel how next-token prediction works, outside the taught curriculum
- **TensorFlow Embedding Projector** (projector.tensorflow.org) — Week 5; prepare the class TSV and the PCA/t-SNE toggle
- **A CLIP image-search demo** (e.g. a Hugging Face Space) — the one optional visual-capability spotlight (Week 6 take-home): type words, rank a folder of images; the engine under image search. Verify a current no-install demo before teaching
- **Google Teachable Machine** (teachablemachine.withgoogle.com) — Week 3; minutes to a working model; prepare the bias-reveal image sets
- **Tokenizer playgrounds** (OpenAI Tokenizer; Tiktokenizer) — Week 2's what-counts-as-a-word demo
- **Anthropic, "Mapping the Mind of a Large Language Model" / Golden Gate Claude** — a deeper cut: the Week 5 map of meaning, found real inside a production model; use the blog posts, not the technical paper
- *Optional deeper:* Brendan Bycroft's 3D LLM visualization (bbycroft.net/llm); "Spreadsheets Are All You Need" (use the browser version; the Excel file can crash on Macs)

### Recommenders, AI Art, and Period-Trained Models (Look at This material, Weeks 5–10)
- **Anderson et al., "Algorithmic Effects on the Diversity of Consumption on Spotify"** (WWW 2020) — algorithm-driven listening is less diverse than organic; more-diverse listeners retain better; the Week 5 recommender study
- **Ted Underwood, "Using GPT-4 to measure the passage of time in fiction"** (blog, 2023) — replicates his hand-coded narrative-time study with GPT-4 as annotator; the Week 3 featured piece
- **Chang, Cramer, Soni & Bamman, "Speak, Memory: An Archaeology of Books Known to ChatGPT/GPT-4"** (EMNLP 2023) — name-cloze probes of what GPT-4 memorized; skews sci-fi/fantasy and canon; the Week 8 inversion
- **TimeCapsuleLLM** (open project; GPT trained from scratch on 1800s London publications) — *verify the project page and details each term; it's a fast-moving independent effort*
- **Pierre-Carl Langlais, MonadGPT** (Hugging Face, 2023) — a model fine-tuned on thousands of 17th-century texts; answers in period worldview; a Week 8 supplement
- **Manjavacas & Fonteyn, MacBERTh** (2022) — BERT pre-trained from scratch on historical English (c. 1450–1950); the scholars' period model; a Week 8 supplement
- **Obvious, *Edmond de Belamy*** (Christie's, 2018; $432,500) — plus the Robbie Barrat authorship coverage; first panel of the Week 10 closing triptych
- **Anna Ridler, *Mosaic Virus* / *Myriad (Tulips)*** — a GAN trained on 10,000 tulips she photographed and labeled; the dataset exhibited as the artwork's labor; second panel of the Week 10 triptych
- **Refik Anadol, *Unsupervised*** (MoMA, 2022–23) — a network trained on MoMA's collection, shown at MoMA; pair with Ben Davis's Artnet critique; third panel of the Week 10 triptych
- *Deeper cuts:* the Netflix Prize and Narayanan & Shmatikov's de-anonymization (2008); Sims & Bamman on literary social networks (2020)

### Pedagogy Foundations
- **Krause, Heather, "Data Biographies: Getting to Know Your Data"** (We All Count, 2019) — the framework adopted as the course's ethics backbone
- **D'Ignazio & Klein, *Data Feminism*** (MIT Press 2020, open access) — Ch. 7 "Show Your Work" is the basis for the deliverable's appendix requirement
- **Knowles, Holton & Swanson, *The Adult Learner*** (9th ed., Routledge 2020) — andragogy; explains why a methods-buffet structure violates problem-centered orientation
- **Chopra, "Misunderstanding What It Takes To Make Recurse Center's Social Rules Work"** (harihareswara.net, 2020) — practitioner warning that posted-but-not-enacted rules fail; basis for Week 1 active onboarding

### Assessment (basis for Principle 12 and the Assessment Framework)
- **Kosmyna et al., "Your Brain on ChatGPT: Accumulation of Cognitive Debt..."** (MIT Media Lab, arXiv:2506.08872, 2025) — EEG evidence of cognitive debt; the central case that a finished artifact cannot prove learning
- **Fan et al. (2024), "metacognitive laziness"** and the "illusion of competence" literature (Rojas-Galeano 2025) — why fluency-on-demand outruns real understanding, especially for novices with weak self-regulation
- **Hassan et al., "How Do Novice Programmers Solve Code-Tracing Problems When ChatGPT Is Available?"** (ICER 2025) — tracing remains a task the AI can't fake on the learner's behalf; basis for the trace-it check
- **Lister et al. (2004, ITiCSE) / BRACElet**; **Stankov et al. (2023), *Computer Applications in Engineering Education*** — reading/tracing precedes and predicts writing; code-tracing assesses semantics
- **Oral/interview assessment in data science** (*Journal of Statistics and Data Science Education*, 2025) — orals are "primary drivers of learning," not just measurement; basis for the oral walkthrough
- **Oudkerk Pool et al., *Advances in Health Sciences Education*** — competency-portfolio assessors anchor on holistic judgments; basis for fixing portfolio criteria in advance
- **Double, McGrane & Hopfenbeck (2020), *Educational Psychology Review*** (g ≈ 0.31) and **Falchikov & Goldfinch (2000)** — peer assessment helps learning but is unreliable as measurement; basis for "peer feedback is formative only"
- **VanLehn (2011), *Educational Psychologist*** — human tutoring ≈ 0.79σ (not Bloom's 2σ); calibrates the realistic value of the one-on-ones
- **Bloom (1984), "The 2 Sigma Problem"** — the mastery-learning logic (feedback + correction + threshold) the competency checks borrow
- **How comparable courses actually assess:** Underwood (IS 417 — notebooks + paper + low-stakes quizzes), Mullen (completion-graded worksheets + reproducible-code standard), Walsh (separate notebook + paper), the Carpentries (ungraded, red/green sticky notes, minute cards)

### Teaching Mechanics (basis for Principle 13)
- **Worked-example effect & expertise reversal:** Sweller & Cooper (1985); Kalyuga (2007); Renkl & Atkinson (2003); Renkl, Atkinson & Große (2004) on fading — basis for full worked notebooks → completion problems with parallel difficulty versions
- **Productive failure:** Kapur (2008, 2014); Sinha & Kapur (2021) meta-analysis (g ≈ 0.36); "When Productive Failure Fails" (Baumgartner et al.) on the necessary consolidation step
- **Mayer's multimedia principles** (segmenting, pre-training, modality; Cambridge Handbook) — basis for session segmentation and pre-building/naming the toolchain in Week 1
- **Dunlosky et al. (2013); Hattie & Donoghue (2021)** — distributed practice and practice testing are highest-utility; basis for cumulative retrieval warm-ups and interleaving
- **Participatory live coding:** the Carpentries instructor training; "Ten quick tips for teaching with participatory live coding" (PLOS Comp Bio) — explain-then-type, deliberate mistake-and-recovery
- **Pair programming:** Hannay et al. (2009) meta-analysis (mixed, moderated effects); Lui & Chan (novice–novice gains); Chong & Hurlbutt (large-gap failure mode) — basis for skill-matched pairing with role rotation
- **Zimmerman's self-regulated-learning cycle** (forethought / performance / reflection); Kitsantas & Zimmerman on goal-setting + self-recording — basis for the one-on-one structure
- **Liz Lerman, *Critique Is Creative* / Critical Response Process** (Wesleyan UP, 2022); Stanford d.school "I Like / I Wish / What If"; Adaptive Comparative Judgement (Bartholomew et al.) — basis for Week 9 structured critique and pairwise peer comparison
- **Edmondson (1999), *Administrative Science Quarterly*** on psychological safety; Edmondson & Bransby — safety is behavioral and must be paired with standards; basis for the safety/standards pairing in Principles 11–12

---

# The Full Corpus Library

Mixed-media collections marked **(M)**. Pivot-kit fallback pairs — pre-tested to yield a finding in the time available — marked **(PK)**; these are what a stalled student adopts in Week 5 (see Principle 17). The student-facing syllabus lists a starter shortlist of 6; this is the full library for the instructor to consult and recommend from.

### Cultural Heritage
- Smithsonian Open Access (M, ~5M items, CC0, api.si.edu)
- Metropolitan Museum of Art Open Access API (M, ~500K objects)
- Cooper Hewitt Smithsonian Design Museum API (M)
- Library of Congress photographs and prints
- New York Public Library Digital Collections
- Europeana API — European cultural heritage
- DPLA (Digital Public Library of America) API
- Chronicling America (Library of Congress, US historical newspapers)

### Film, TV, Music (M for posters/covers)
- TMDb (The Movie Database) API — posters, metadata, cast, plot
- MusicBrainz + Cover Art Archive
- OMDb
- Million Song Dataset + musiXmatch — bag-of-words lyrics
- Genius API — full lyrics, rate-limited
- Spotify audio features API

### Fashion, Design, Visual Culture
- Public Domain Review collections
- Magazine cover archives at archive.org
- Behance / Dribbble (light scrape, ethical caveats)

### Fandom & Identity
- AO3 fanfiction tag dump (selective, aggregate-only)
- RuPaul's Drag Race contestant data + photos (M) — `dragracer` R package
- Eurovision lyrics + performance photos (M) — `Spijkervet/eurovision-dataset`
- LiveJournal academic dumps

### Food, Drink, Domestic Life
- Internet Archive Cookbook Collection (M, ~13,000 books)
- TheMealDB / TheCocktailDB APIs (M)
- Yelp Open Dataset
- BeerAdvocate / RateBeer reviews (Stanford SNAP dump)
- NYT Cooking (light scrape, ethical)

### Love, Death, Life-Stage Rituals
- NYT Wedding Announcements 1985–2014 (`TheUpshot/nyt_weddings`)
- Obituaries — Legacy.com light scrape; published academic corpora
- Missed connections — LoC historical newspapers; Craigslist (light)
- Tarot card descriptions (Rider-Waite is public domain)

### Politics
- Congressional Record / Hansard
- Campaign poster archives (LoC, archive.org)
- Trump Twitter Archive (thetrumparchive.com) — closed historical
- Dril tweets (`dril-archive` GitHub mirrors) — closed historical

### Books & Reading
- Open Library API (M, covers + metadata)
- Project Gutenberg / Standard Ebooks
- UCSD Book Graph (Goodreads reviews, Wan & McAuley, ~10M reviews)
- Allison Parrish's "Gutenberg, dammit" corpus

### Lists, Lore, Weirdness
- Wikipedia "List of unusual..." pages (often with images)
- Wikipedia edit wars / talk pages (MediaWiki API)
- Internet Archive zines and diaries

### Narrative & Born-Digital Fiction

Where the genre-fiction projects (horror, sci-fi, LitRPG) actually find text. The move is born-digital and publicly posted over pirated published novels: more accessible, far cleaner legally, and the native habitat of the genres students love.

- **Reddit fiction** *(cleanest path)* — r/nosleep, r/shortscarystories, r/libraryofshadows (horror); r/HFY, r/WritingPrompts (sci-fi and general). Contemporary, publicly posted, reachable via PRAW or the Pushshift dumps the social-media section covers.
- **Web serials** — Royal Road, Scribble Hub: the home of LitRPG and progression fantasy. Light, polite scraping at small scale; check each site's terms.
- **Public-domain genre fiction** — Project Gutenberg, Standard Ebooks: full text, zero risk, the classic end of the genres (Shelley, Poe, Wells, Verne, early Lovecraft). Use when a historical-genre framing fits.
- **AO3 — a consent case, not a clean source.** Vast contemporary narrative, but the archive rate-limits, opposes dataset creation, and scraped AO3 datasets were pulled from HuggingFace in 2025. A small, hand-collected, non-redistributed sample with attribution is defensible; building or sharing a dataset is not. For the right student the consent question *is* the project — the training-data-ethics debate on a corpus they care about.
- **Published-fiction reception (not the text)** — Goodreads and Amazon reviews: how readers talk about books, abundant and reachable, but no fiction inside. The reception angle, not the narrative one.
- **In-copyright text, legally** — HathiTrust Research Center's non-consumptive access and Extracted Features give per-page word counts you can compute on without ever reading the text out. Heavy for a community cohort; the advanced path.

**The line not to cross:** shadow libraries (LibGen, Anna's Archive, the Books3 corpus) for full-text in-copyright novels. Full-text contemporary *published* fiction is the genuinely hard case — which is the course's lesson, not a gap to route around. See the licensing one-pager and the Bartz v. Anthropic note in the training-data cluster: the maker of the very model writing students' code paid $1.5 billion for downloading exactly this kind of corpus.

### Social Media (the post-API era)

The messy, vital corpus space. Most students will use one of these.

- **Bluesky / ATProto** *(easiest, most open)* — Jetstream firehose, no API key needed. `atproto` Python SDK. A one-hour pull is hundreds of thousands of posts.
- **Mastodon** — per-instance API. Each server (mastodon.social, hachyderm.io, fosstodon.org, etc.) has its own public-timeline endpoint. Good for community-specific corpora.
- **Reddit historical (Pushshift archives)** — live API closed in 2023, but historical monthly dumps (2005–2022) remain on HuggingFace mirrors and academic torrents. For new data: PRAW with OAuth, small-scale only (~1k post listing cap, 100 queries/min).
- **Letterboxd** — no official API, light scraping with delays feasible at small scale.
- **Goodreads** — UCSD Book Graph is the standard academic dump.
- **AO3** — see *Narrative & Born-Digital Fiction* above: a consent case, small attributed samples only, never a redistributed dataset.
- **Tumblr** — public posts only, light scrape; rich for fandom and early-2000s sociolinguistics.
- **TikTok metadata** — third-party tools (Apify, scraping libraries) provide descriptions, hashtags, sounds. Hard, ethically fraught.
- **Twitch chat** — TwitchChatDownloader and academic dumps. Volume is the challenge.
- **YouTube comments** — YouTube Data API, free tier with quota. Great for reception analysis.
- **Wikipedia talk pages and edit histories** — MediaWiki API. Edit wars are a kind of social-media artifact: argument with timestamps. Highly underused.
- **Trump Twitter Archive, dril tweets, LiveJournal dumps** — closed historical corpora.
- **Discord (research access only)** — public servers can be archived with the user's permission; not generally recommended for student projects.

**Social-media ethics:** Public-but-not-public is the central tension. A post on Bluesky is technically public, but the user didn't anticipate being a row in your CSV. Aggregate analysis is broadly defensible. Quoting individuals — especially non-public figures — requires care; quoting them in a published web essay requires more. The Data Biography's "People" prompt applies twice as hard here. When in doubt, anonymize, aggregate, or ask.

**General ethics rule for all corpora:** Aggregate analysis is broadly accepted. Quoting individuals or training models on identifiable personal text/images is not. Face recognition and age/gender prediction on real people are off-limits.

---

## Environment, Persistence, and Tooling (the $0 stack)

The default stack is **Google Colab free tier + Google Drive**, chosen so the code-writing AI is built into the notebook and the whole thing costs nothing. Two facts about Colab drive the design:

- **The runtime is ephemeral.** Free Colab wipes the session on idle or disconnect (roughly 90 minutes idle, ~12-hour cap), taking every in-memory variable and every file written to `/content` with it. For a ten-week project course this is the single biggest practical hazard: a student collects a corpus in Week 4 and finds it gone in Week 5. **The fix is designed in, not left to chance** — Week 1 establishes a Drive-mount ritual, and every notebook saves the corpus and outputs to a Drive project folder so they survive resets and carry week to week. The cookbook notebook writes the collected corpus straight to Drive (Week 4). Mounting Drive has a small auth friction for non-coders, which is exactly why it's taught once, early, with a re-mount-after-reset demo so it isn't frightening later.
- **The free AI is now good and built in.** Colab ships an integrated, free, Gemini-powered assistant (generate a cell from plain language; fix an error and review the change as a diff) — capable enough for this course's plumbing code and, crucially, it writes into cells the student can *read*. That visibility is why it's the primary in-notebook helper rather than a separate chat window. Students already fluent in Claude or ChatGPT use those instead; the workflow is identical. The Gemini *API key* is a distinct thing, needed only for Week 7's annotation pipeline (programmatic labeling at scale).

**Fallback:** Kaggle Notebooks — a persistent working directory with no mount, more reliable free GPU (30 hrs/week, predictable), and frozen runtime versions for reproducibility. Worse built-in AI than Colab's, so it's the documented escape hatch for students Colab keeps disconnecting, not the default.

**The tooling line to hold (and why):** full coding agents — Colab's Data Science Agent generating whole notebooks, or an autonomous tool like Claude Code — are for *building* this course's materials, not for students. The course's entire learning architecture (the AI-closed blocks, "read the AI's code," the planted bugs, the hand-labeling calibration) rests on the student seeing and questioning the code. A tool that turns "investigate this and understand the tools" into "describe what you want and receive a result" is exactly the cognitive-offloading failure the Gemini-free blocks exist to counter. So: cell-level help for learners, agents for the build. A more technical course could choose differently; this one shouldn't.

**Two gotchas to flag before each term:** Colab's built-in AI requires an 18+ account in a supported locale, so a few students may not see the spark icon — Google AI Studio is the universal fallback there. And free Gemini quotas have been cut more than once (see below), so re-verify limits before teaching.

## Caveats, Risks, and Things to Watch For

- **AI provider quotas shift.** Google cut Gemini free quotas 50–80% in December 2025 and again in April 2026. Re-check ai.google.dev/gemini-api/docs/rate-limits before each term. What's free this term may not be free next term.
- **Social-media API access changes.** Pushshift's live API closed in 2023. X/Twitter has been hostile to research since 2023. Reddit's terms tightened in 2024. The "post-API era" framing is now structural; budget for it.
- **Week 9 can collapse.** Even with three weeks of publish scaffolding, Week 9's build session is the place where projects most commonly stall — Quarto installation issues, GitHub Pages deployment failures, custom JavaScript breaking. Pilot the entire flow before the term. Have backup deployment options (QuartoPub, Observable, Replit) ready.
- **AI-as-reader is unreliable on non-English text.** The corpus library leans Anglosphere, and LLMs underperform fine-tuned baselines by 10–14% on low-resource-language annotation (Jadhav et al. 2024). Require inter-annotator agreement against a small hand-labeled sample for all non-English work, and flag the limitation explicitly.
- **Week 9 can collapse, and the one-on-ones are what prevent it.** The build session is where projects stall (Quarto, Pages, JS); pilot the whole flow and keep backup deployment ready (QuartoPub, Observable, Replit). The mid-course one-on-ones (see that section) are the non-negotiable upstream hedge — skip them and the wheels come off in Week 9.
- **Pudding-grade output isn't achievable in 10 weeks**, and the deliverable says so ("an essay *shaped like* a Pudding piece"). Don't let students compare drafts to professional pieces without that caveat. Archive the "Look at This" pieces you feature — Pudding URLs move.
- **The "What Surprised You?" check-out is load-bearing.** If students stop doing it, the AI-as-instrument thread quietly collapses. Read them, respond, refer back in class.
- **The illusion-of-competence risk is real and structural.** The Gemini-free block and weekly checks are the main response; the Week 6 hand-labeling is the highest-leverage moment to surface a student who can run code but can't trace or explain it.
- **The whole design is evidence-informed but unproven *in this combination*.** Each piece has a base — but the assessment stack, the Recurse social rules (built for a daily-contact residency, not a weekly class), and the published-essay deliverable have not been validated together for mixed-experience adults. And the effect sizes behind the mechanics are modest and moderated (productive failure g ≈ 0.36 *with* consolidation; peer assessment g ≈ 0.31 and unreliable as measurement; tutoring ≈ 0.79σ not 2σ; PBL d⁺ ≈ 0.44–0.65, and this course sits at the low end of the duration window). Treat the not-yet/getting-there/solid reads as judgment aids, not measurements; run the course as an experiment and collect data.
- **The mechanics assume instructor skill.** Live coding, the Critical Response Process, productive failure *with* its consolidation step, and the SRL-structured one-on-ones are skills — the form without them gives none of the benefit, so the prep checklist's "rehearse it" items aren't optional. Pair programming is the weakest-evidenced mechanic; skill-matched pairing and role rotation are the hedges, but let people work solo if it isn't helping.
- **The course produces ~12 weeks of work in 10**, run as ~2-hour sessions of mixed-format instruction that will tire the instructor by Week 6. Slack is built into the structure (see Principle 17): the Weeks 5–7 floating catch-up valve and the cuttable Week 8 robustness arc. Surface the workload in Week 1, and when behind, compress the marked elements rather than the protected floors.

---

## Honest Status of the Evidence

So the citations aren't mistaken for certainty: the strongest evidence behind this design is for the *individual mechanics* (worked examples, retrieval practice, segmenting, code-tracing as assessment) — among the better-replicated findings in instructional psychology. The evidence is *moderate* for productive failure, project-based learning, and peer assessment — real effects, but moderated and sometimes contested. The evidence is *weakest, and partly preliminary,* for the AI-and-cognition claims (several key 2025–2026 sources are non-peer-reviewed preprints, directionally consistent with the broader offloading literature but early) and for the *whole-system* claim that this particular combination produces durable competence in this particular audience. That last claim is untested. The course is a well-reasoned bet, not a proven protocol; run it with data collection and revise against what the first cohort shows.

---

## What This Document Is For

Two audiences:
1. **The instructor running the course** — the *why* behind every design choice, the prep that's needed, and the failure modes to watch for.
2. **Anyone adapting the course** — the design rationale, so changes can be made knowingly rather than blindly.

The syllabus is what students see. This document is what makes the syllabus possible.
