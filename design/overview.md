# Culture as Data — Central Overview
## Computational Cultural Analysis for the Curious

*The front door to the course. This summarizes the whole design; `syllabus.md` and `planning-doc.md` carry the detail.*

---

## What the course is

### One sentence
A 10-week, project-based community course that teaches curious adults to investigate cultural data at scale using AI-assisted coding — and to understand how the machine itself works, from counting to LLMs — ending in a published web essay.

### The shape
- **Weeks 1–3 — Tour.** Shared toy datasets, the first mechanism rungs (counting, classification), and all four project methods previewed before anyone commits.
- **Weeks 4–7 — Project.** Commit to a corpus and methods by Week 4 — where students also learn to collect data via APIs and careful scraping — then guided iteration, each week pairing a short tool beat (embeddings, the heart of the course, W5; deeper application and images, W6; the AI as a reader at scale, W7) with a long project lab. Every session has a pop-culture hook or hands-on slot, most carry a low-stakes "delight" moment, and a bank of fallback projects backs up anyone whose corpus or question doesn't pan out. Mid-course one-on-ones in Weeks 5–6.
- **Weeks 8–10 — Publish.** Week 8 opens with models trained on single historical periods (and what a famous model has memorized), then tries to kill each finding before settling it and drafting prose; Week 9 builds the page; Week 10 is a public showcase, closing on a neural network trained on MoMA's own collection.

### The four core methods (pick two)
Counting and comparison · classification (the AI as a reader you train and check) · embeddings (text and image, the heart of the course) · character networks as an optional method — so choosing a method and understanding how it works are one thread, with embeddings the biggest leap past counting. Short spotlights (how recommenders see you; CLIP image search for visual projects; the emotion-arcs smoothing fight) and starter notebooks (stylometry, color, diachronic meaning, reception) cover what didn't fit.

### What students make
Two things, separated on purpose. The **reproducible notebook** is the primary evidence of analysis — code, data, and prose cells that someone else can run top to bottom. The **web essay**, built on top of the finished notebook in Act 3, is the communication layer: an opening question, two to four visualizations, at least one image-based finding, ~800–1,500 words of prose, a corpus note, a "show your work" appendix, and a "what surprised me" closing. Static HTML and SVG by default; JavaScript is opt-in and triggers a code-review step. The essay is what students show; the notebook is where the thinking lives.

### How learning is checked (no grades, but standards)
Standards are made legible through eight named competencies: read a block of analysis code and say what it does; ask a tractable question of cultural data; name what a method assumes and hides; read an embedding map, a classifier's labels, or a character network skeptically; judge what counting, classification, embeddings, and AI annotation each reveal and hide, read an AI's confidence to know which labels to trust, and recognize the same machinery in the recommender feeds around them; write a Data Biography; judge AI-generated code rather than just run it; and read a published study, data essay, or chart for the choices behind it (and turn that eye on one's own visualizations before publishing). Evidence is gathered continuously and in AI-free conditions — weekly low-stakes competency checks (code-tracing, "explain your last result" aloud, debug-a-planted-bug) during the Gemini-free block; a process portfolio ("workbench"); an oral walkthrough mid-course and at the showcase; and a mid-course hand-labeling comparison against the AI's labels (Week 6: label thirty items the AI also labels, study every disagreement). Peer feedback is formative only.

### The audience
Curious adults outside formal education — librarians, journalists, retired teachers, museum educators, hobbyists. Mixed coding backgrounds; most have little or none.

---

## The ideas that define it

1. **Lead with destinations, then interrogate them.** Every week opens with a five-minute "Look at This, then Question It" — a finished study or article students first admire, then take apart: *what did the authors choose, what could they have chosen, where might this be wrong?* From Week 5 the interrogation beat is room-led: students name the choice before the instructor does. Productive failure runs through it — predict-before-you-test in Week 3, and in Week 7 trusting the AI's labels until a gold-set check reveals where it was confidently wrong.

2. **Published work is made of choices, not handed-down truth.** A through-line and its own competency: students learn to read research and data journalism the way the field's own practitioners do — with admiration and skepticism at once — and to see that celebrated work rests on interpretative decisions, some arguable, that its authors sometimes get wrong. It's carried by the weekly ritual, a standing three-question reading lens, the Week 2 trial of a famous study — a real published fight, assigned in Week 1, that ends with the authors answering "your corpus is biased" by re-running the analysis without the suspect data — and finally the student's "show your work" appendix, where they name the choices in their *own* project. Visualization rides this thread rather than getting its own unit: a chart is an argument with choices baked in (axis, scale, what's shown and dropped), interrogated in the ritual and, in Week 9, turned on the student's own chart before publishing — the making-side mirror of the Week 6 hand-labeling. The guardrail is calibrated respect, not cynical debunking: good work survives scrutiny and is more impressive for it.

3. **The machine is not a black box, and the point is moving beyond counting.** Four tools, each expanding what a student can do with their own corpus past the one before, taught only to the depth that changes what they can do or trust: **counting** (the honest floor — no notion of meaning) → **classification** (train a transparent reader and see what it learned) → **embeddings** (the heart — items become positions on a map of meaning, so similar things cluster and patterns appear counting can't reach) → **AI annotation** (the powerful, opaque reader that judges your whole corpus — used with the discipline to trust its sure labels and check the rest). The signature move is taking a question first asked by counting and answering it again, more richly, by meaning — the same adjectives near *she* vs. *he*, counted in Week 2 and then embedded in Week 5 to reveal clusters counting missed. Depth is conceptual-visual — no math, browser tools, experience-first — and the thesis is: *it's all turning culture into vectors and learning the weights, and the leap past counting is letting the machine place things by meaning instead of tallying them.* Images are a co-equal corpus run through the same four tools — count pixels, classify album covers, embed paintings — so a visual project is as supported as a textual one; what they skip is the vision-architecture tour, since the capability, not the architecture, is the point. The destinations are cultural, not chatbot-shaped: the feeds the pitch indicts, and the central reckoning the ad promises — the models reading our culture were trained on creative work scraped largely without permission, which students confront directly in Week 7 when an AI annotates *their* corpus and in the period-model lesson where corpus-as-worldview becomes the instrument.

4. **The Data Biography carries the ethics, in one strong pass.** Written at commitment in Week 4 — where it can respond to a real corpus choice — on Heather Krause's framework, and distilled into the essay's corpus note in Week 8. The same week holds the one licensing conversation. The mechanism spine carries the rest of the ethical load by demonstration: the bias you taught the classifier, the count that depended on a definition, the model that generates plausible continuations rather than facts.

5. **The AI is an instrument with known failure modes, not an oracle.** The course explicitly teaches illusion of competence, the unconscious shrinking of a question to fit what the tool does easily, insecure code generation, and unreliability on non-English text. A "Gemini-free block" each session forces unaided work and hosts the weekly competency check.

6. **Assessment targets the thinking, not the artifact.** Because an AI can produce work a student doesn't understand, a polished result is not enough to show learning. The competency checks, oral walkthrough, weekly AI-closed blocks, and the Week 6 hand-labeling comparison exist to make the gap between "it ran" and "I understand it" visible — early, to the student first.

7. **Mechanics grounded in cognitive science.** Faded worked examples giving way to completion problems offered in parallel difficulty versions for the mixed cohort; cumulative retrieval warm-ups; interleaving across the ladder's rungs; participatory live coding; skill-matched pairing with rotating roles; the mid-course one-on-ones structured on a forethought–performance–reflection cycle; the Critical Response Process for critique.

8. **Curiosity-flavored framing.** Institutional language ("limitations," "validation," "AI use statement") is reworded into detective questions that do the same epistemic work. The assessment framework is itself in this voice: competencies as "things you'll be able to do," checks as rituals, the portfolio as a "workbench."

9. **Social rules, actively onboarded.** Four norms — no feigning surprise, no well-actually's, no backseat driving in pair sessions, no subtle -isms — demonstrated and modeled in Week 1 rather than merely posted, and paired with genuine standards so the room is both safe and rigorous.

---

## Tooling and cost
Python in Google Colab, Quarto, and GitHub Pages, with the Gemini API as the default free assistant. The course runs at $0 per student by default; the ceiling is a single $20 month of a chat subscription if a student wants one. The publishing toolchain is pre-built and introduced in Week 1, so Act 3 spends effort on the essay rather than on first contact with the tools.

---

## Open questions the first cohort will answer

The design is a careful, evidence-informed bet, not a proven protocol. A few things can only be learned by running it, and the instructor should watch for them and collect data:

- **Do the competency checks predict retained skill?** The checks are built to surface the run-vs-understand gap. Whether passing them means a student could redo the work months later is the central thing to verify.
- **Does the notebook/essay split keep time on the analysis?** The split moves the assessment weight onto the notebook; only watching where students actually spend Weeks 8–10 shows whether it also moved their time.
- **Is the cohort's range too wide for the differentiation built in?** Parallel-difficulty completion problems and the one-on-ones absorb some variance. A Week-1 read of coding backgrounds tells the instructor how much variance is left to manage by hand.
- **Do the social norms hold?** If corrections stop happening, the norms have gone decorative; if they start landing as policing, they've gone the other way. Either is a signal to intervene.
- **Do the tools land for the least technical students?** The Week 7 explain-it check (what is your labeling prompt deciding, and how would you check a label?) and the Week 10 oral walkthrough are the built-in measures. If a student still can't say what a tool hides by Week 10, the explain-it checks need more weight earlier.
- **Is ten weeks enough?** After one run, ask honestly whether students finished with room to spare or scrambled at the end. The answer shapes the next iteration.

---

## The documents
- `syllabus.md` — the student-facing document: schedule, weekly plans, readings, the split deliverable, the "how you'll know you're learning" section, and setup.
- `planning-doc.md` — the instructor's companion: design rationale, the full assessment framework with its competency-check calendar and workbench criteria, prep checklists, provider research, the corpus library, the annotated bibliography, and risk notes.
- `lesson-plans.md` — the teach-from document: minute-by-minute 2-hour flows for all ten weeks, each with its mechanism block, featured study and paired critique, datasets, and competency check.
- `site/` — a static multi-page website of the syllabus, ready to deploy to GitHub Pages. *(Currently two design generations behind the markdown documents; rebuild before sharing.)*
