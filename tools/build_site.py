#!/usr/bin/env python3
"""
build_site.py, regenerate the Culture as Data course site (BUILD-PLAN §2).

Plain HTML + one CSS file, no framework, no server build step. The page text is curated
from the four design docs (overview / syllabus / lesson-plans / planning-doc) and held as
structured Python data below, so the site and the docs can't silently drift: when the docs
change, update the data here and re-run.

    python tools/build_site.py        # writes everything under site/

Every page reads fully with JavaScript disabled; the only JS is a progressive-enhancement
nav toggle.
"""
from __future__ import annotations
import html
from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / "docs"
WEEKS_DIR = SITE / "weeks"

TITLE = "Culture as Data"
TAGLINE = "Ask your own questions about the stories, lyrics, art, and online communities you love."

NAV = [
    ("index.html", "Home"),
    ("syllabus.html", "Syllabus"),
    ("schedule.html", "Schedule"),
    ("resources.html", "Resources"),
    ("about.html", "About"),
]

COMPETENCIES = [
    "Read a block of analysis code and say what it does, line by line, without running it.",
    "Ask a tractable question of a pile of cultural data, specific enough to answer and honest about what it leaves out.",
    "Name what a method assumes and what it hides.",
    "Read an embedding map, a classifier's labels, or a character network skeptically, telling a real pattern from a pretty accident.",
    "Judge what counting, classification, embeddings, and AI annotation each reveal and hide, read an AI's confidence to know which results to trust, and reckon with training data scraped from creative work.",
    "Write a Data Biography that accounts for where a dataset came from, who is in it, who is not, and what it cannot tell you.",
    "Judge AI-generated code instead of just running it.",
    "Read a published study, data essay, or chart and see the choices behind it, then turn the same eye on your own charts before publishing.",
]

STARTER_CORPORA = [
    ("NYT Wedding Announcements 1985–2014", "TheUpshot/nyt_weddings on GitHub", "counting comparisons across time, gender analysis, class signaling"),
    ("/r/AmITheAsshole judgments", "Pushshift mirrors on HuggingFace", "AI-as-reader (moral classification), reception analysis"),
    ("Eurovision lyrics 1956–2023", "Spijkervet/eurovision-dataset on GitHub", "counting across languages, sentiment, diachronic shift"),
    ("TMDb movie posters of one genre", "TMDb API, free", "image embeddings, color analysis, CLIP search"),
    ("Met Museum Open Access", "official API, ~500K objects with images", "image embeddings, distant viewing, cataloging-language change"),
    ("Bluesky one-hour firehose slice", "Jetstream, no API key, atproto SDK", "any of the four methods, social-media-specific work"),
]

ANCHOR_TOOLS = [
    ("OpenAI Tokenizer / Tiktokenizer", "https://platform.openai.com/tokenizer", "Week 2, what counts as a word"),
    ("Google Teachable Machine", "https://teachablemachine.withgoogle.com/", "Week 3. Train a classifier in minutes"),
    ("Hugging Face", "https://huggingface.co/", "Weeks 5–8, the public hub where open models live"),
    ("TensorFlow Embedding Projector", "https://projector.tensorflow.org/", "Week 5, plots text and images"),
    ("CLIP image-search demo (optional)", "https://huggingface.co/spaces", "Week 6, search images by typing words"),
]

READING_LIST = [
    ("1", "Bollen et al. (PNAS 2021) abstract + the hockey-stick figure, plus the one-page Schmidt/Piantadosi/Mahowald critique", "Robin Sloan, \"Writing with the machine\""),
    ("2", "Wolfram, \"What Is ChatGPT Doing…\" opening sections only", "Zipf's law, the straight line in every text"),
    ("3", "Browse America's Public Bible (americaspublicbible.org), intro + a verse", "Underwood on GPT-4 and fictional time; Juola's Rowling unmasking"),
    ("4", "Krause, \"Data Biographies: Getting to Know Your Data\" (We All Count)", "Freelon, \"Post-API Age\""),
    ("5", "Alammar, \"The Illustrated Word2Vec\" + the Soni/Klein vs. Caliskan debate pair", "Garg et al. (PNAS 2018); Anderson et al. (Spotify, 2020)"),
    ("6", "Gilardi et al. (2023) abstract, the AI as a cheaper coder", "The Reagan/Swafford smoothing fight"),
    ("7", "NYT v. OpenAI complaint summary, or a Books3 explainer, read against your Week 4 licensing conversation", "Gilardi et al. (2023), full"),
    ("8", "None required", "MonadGPT and MacBERTh model pages, two more time capsules"),
    ("9", "None", "A Pudding \"how we made it\" post"),
    ("10", "None", "The de Belamy authorship story; Ridler's Mosaic Virus; Anadol's Unsupervised and its critics"),
]

# Weekly data, curated from lesson-plans.md ---------------------------------
WEEKS = [
 dict(n=1, title="Your First Investigation", tool="Culture as data itself (the ladder starts next week)",
   promise="By the break you'll have loaded a real dataset, asked it a question, and produced your first chart. A complete investigation, end to end, on day one.",
   admire="The Pudding, \"Pockets\" (2018), women's jeans pockets are measurably smaller, and one chart lands the argument.",
   interrogate="80 pairs from a handful of brands: is that \"women's pockets,\" or a slice? And look at the chart itself, not just the data, what does it put front and center?",
   flow=[("0:00","Setting the room: the social rules, demonstrated by the instructor breaking one and being corrected. Today's live coding includes real mistakes on purpose."),
         ("0:12","Look at This, then Question It: Pockets."),
         ("0:17","Pre-train the vocabulary (no code): corpus, method, model, embedding, in plain language with pictures. The course map and the deliverable."),
         ("0:32","Lab 1 (worked, participatory): copy the notebook to Drive and mount Drive into the runtime (this is how your corpus and results survive Colab wiping the session, everything saving to one project folder), put a Gemini key in Colab Secrets, load NYT wedding data, make a first chart. Hand out the common-errors cheat sheet. Then solo with a partner: draft three questions, pick one, have the AI write the code, run it, chart it. Write one sentence predicting your cell before you run it."),
         ("1:10","Break"),
         ("1:20","Lab 2 (worked): ~200 Met Museum objects with thumbnails. Plot the collection by century; notice what the catalog does not record."),
         ("1:50","Teaser of the ladder ahead; the standing rituals named. First check-out.")],
   reading="The Bollen/Schmidt fight, abstract-and-figure only: the Google Books \"hockey stick\" of cognitive distortions, then the critique that it may be an artifact of which books Google scanned. Trial next week.",
   sketch="One question from your life answerable with text or image data; three sentences.",
   check="Trace it: one written sentence predicting what your cell does before you run it. (Competency 1.)",
   comps="1, 8"),
 dict(n=2, title="Counting Is Already a Model", tool="Counting, and every count hides a choice",
   promise="Put a famous PNAS paper on trial, build a word-counter by hand, watch the same sentence get counted three ways, and count an image too.",
   admire="The Bollen/Schmidt trial: a hockey stick of societal distress, found by counting.",
   interrogate="The rising words are fiction-words, and Google scanned more fiction after 2000. The rebuttal and the move to steal: the authors removed the entire fiction corpus and re-ran it, and the pattern largely held. The answer to \"your corpus is biased\" is a test, not an argument.",
   flow=[("0:00","Warm-up retrieval."),
         ("0:05","The trial: claim, objection, re-run-without-fiction rebuttal, \"interpret with care.\" One named choice is the chart: the hockey-stick shape depends on its y-axis and smoothing."),
         ("0:25","Delight beat: an artist's signature vocabulary, the words they use far more than a pop baseline. No caveats."),
         ("0:30","Hand-built bag-of-words: two authors, highlighters, argue about merging run/running. Counting requires defining."),
         ("0:55","What counts as a word? Paste a sentence into two tokenizer playgrounds and watch it shatter differently. Models see tokens, not words."),
         ("1:05","Break"),
         ("1:15","tf-idf: the AI scales your hand count; stop-words dominate, which motivates \"common here, rare overall.\""),
         ("1:30","Cross-corpus counting: the same counter on a lyrics slice, a subreddit, and a novel. The corpus choice changes what \"common\" means."),
         ("1:45","Counting images: average color, a brightness histogram, a \"darkest album cover\" ranking. What you choose to count is the same kind of decision as stop-words."),
         ("1:50","Gemini-free check and check-out.")],
   reading="Stephen Wolfram, \"What Is ChatGPT Doing…\", opening sections only, where even text generation turns out to be built from counting.",
   sketch="Count something in a text you love; one chart; one sentence naming a choice you made.",
   check="Explain it: why two tokenizers split a sentence differently, and what your stemming choice changed. (Competencies 3, 5.)",
   comps="3, 5, 8"),
 dict(n=3, title="Classification: Counting with Weights", tool="Classification. Train a reader and read what it learned",
   promise="Teach a machine a bias in ten minutes, build a classifier and read its mind, and preview the full methods menu before next week's commitment.",
   admire="Lincoln Mullen, America's Public Bible (2023), a classifier that finds biblical quotations across millions of newspaper pages.",
   interrogate="What counts as a quotation, a four-word echo, a loose paraphrase?, is a definition the scholar chose, and it shapes every result. The model reads the same messy digitized text your own project will.",
   flow=[("0:00","Warm-up + Look at This: Mullen's America's Public Bible."),
         ("0:10","Teachable Machine, instructor demo: a two-class image model trained live, then the reveal that it learned from only orange cats and brown dogs. The room predicts what a black cat will do, then sees it."),
         ("0:22","Counting with weights, the lab: each word casts a weighted vote; a logistic regression adds them up. Train it on a pop corpus, then read the signed coefficients, its mind on the table."),
         ("0:52","Delight beat: the words that most predict \"breakup song\" or \"this reviewer hated it.\""),
         ("0:57","One-line bridge: that classifier is a neuron; stack many for a neural net, which is what's inside the Week 7 model. A quick TensorFlow Playground glance."),
         ("1:00","Break"),
         ("1:10","Methods menu preview, so Week 4's choice is informed: counting, classification, embeddings (Week 5), and optional approaches (character networks for fiction; sentiment arcs for story projects, Jockers's Syuzhet reproducible in Python, whose own smoothing controversy is the built-in lesson to doubt the shape; CLIP image search for visual projects; and, for the technically comfortable, fine-tuning a small open model, ModernBERT, on your own labels)."),
         ("1:25","Pitch prep: what makes a tractable question, and the corpus-existence rule."),
         ("1:45","Gemini-free check and check-out.")],
   reading="Browse America's Public Bible online: read the introduction and click through one or two verses.",
   sketch="Train a quick logistic regression on a labeled dataset and screenshot its five most positive and five most negative words. And bring a corpus existence proof to Week 4: a screenshot of 50 rows of your proposed data.",
   check="Explain it: read your classifier's top weights aloud, and name one input where it would fail and why. (Competencies 4, 5.)",
   comps="2, 4, 5"),
 dict(n=4, title="Pick a Corpus. Pick Two Methods. Commit.", tool="The project (no new mechanism this week)",
   promise="Leave with a pitched project, two chosen methods, your Data Biography drafted, and the skill that makes \"bring your own corpus\" real: getting data off the web.",
   admire="A Pudding \"How We Made…\" process post, the messy middle, where every polished piece had a moment its maker thought it wouldn't work.",
   interrogate="Listen across the pitches for questions too vague to answer, corpora that don't exist as accessible data, methods chosen for vibes, and the quiet scaling-down of ambition.",
   flow=[("0:00","Warm-up + Look at This: the process post."),
         ("0:08","Pitches, three-minute hard cap each: your corpus (existence proof shown), your two methods, what would count as a finding."),
         ("0:48","Break"),
         ("0:58","The data conversation: the licensing one-pager (CC0 museums and public-domain books go anywhere; academic-only sets analyze-don't-redistribute; lyrics and review text metadata-only; AO3 and other community-opposed archives a small attributed sample at most, never a shared dataset; live firehoses we discuss, don't scrape; pirated full-text books from shadow libraries like LibGen never, the line the field's $1.5B settlement was about), and the Data Biography introduced."),
         ("1:10","Getting the data, APIs and scraping, demoed live with the AI writing the code. API first (the Met or Art Institute, no key); scraping second, with the robots.txt / ToS / rate-limit / anti-republish check."),
         ("1:30","Collect-and-build lab: point the cookbook notebook at your corpus, reshape it, and save it to your Drive project folder so it's there next week (when the Week 1 Drive mount pays off), and fork the publishing template. Your project repo is born today."),
         ("1:55","Commit, with the pivot kit named as insurance. A null result honestly shown is a complete project. Check-out.")],
   reading="Heather Krause, \"Data Biographies: Getting to Know Your Data\" (We All Count).",
   sketch="Write the Data Biography (~400 words) for your corpus, and actually collect it with the cookbook notebook so you reach Week 5 with real data in hand.",
   check="Explain it: your question aloud, what it omits, and where your data actually comes from. (Competencies 2, 6.)",
   comps="2, 6"),
 dict(n=5, title="Embeddings: A Map of Meaning", tool="Embeddings, the heart of the course, the leap past counting",
   promise="Watch your own corpus, text or images, sort itself by meaning, see the finding counting couldn't give you, and learn the same trick is how \"For You\" feeds place you.",
   admire="A debate, two readings of one fact: embeddings encode the associations in a corpus.",
   interrogate="To Caliskan et al. (2017) that's a warning, a model trained on human text launders human prejudice. To Soni, Klein & Eisenstein (2021) the same mirror is a method, embeddings on abolitionist newspapers reveal which papers led the movement's language. The room decides: when is reading a corpus's associations a discovery, and when is it laundering bias?",
   flow=[("0:00","Warm-up + Look at This, room names the choice first: the embeddings debate."),
         ("0:10","The beyond-counting moment: put Week 2 beside today. There you counted adjectives near she vs. he; now embed those descriptions and watch them cluster. Same question, two tools, the second visibly richer. Name the idea: an item becomes a vector, position learned from the company it keeps."),
         ("0:25","Embed your own corpus, text or images. Image projects embed their pictures and watch them group by untagged style. The embedding model is an open one from Hugging Face, the hub where open models live (the same place Week 8's period models come from). And here charts stop being neutral: switch PCA to t-SNE and the same data rearranges. A visualization is an argument with decisions baked in."),
         ("0:55","Break"),
         ("1:05","Project lab: push your embeddings, hunt the surprise cluster. A five-minute recommenders aside: \"For You\" is this same map plus your history. One-on-ones begin at the side."),
         ("1:50","Gemini-free check and check-out.")],
   reading="Jay Alammar, \"The Illustrated Word2Vec,\" through the personality-vectors and king/queen sections.",
   sketch="On your map, toggle PCA vs. t-SNE and screenshot how the picture changes. Name one neighbor or cluster that surprised you, and say whether you believe it.",
   check="Explain it: on your map, name one cluster you believe is real and one that's probably a projection artifact, and how you'd tell. (Competency 4.)",
   comps="4, 5"),
 dict(n=6, title="Deepen the Project: Images, and Where the AI Fails", tool="Apply the tools harder; image projects' deepest day; calibrate the AI on your data",
   promise="Push your project past first findings, give image projects their deepest day, and find exactly where the AI's reading of your data goes wrong.",
   admire="Arnold, Tilton & Berke, \"Visual Style in Two Network-Era Sitcoms\" (2019), computer vision on every shot of Bewitched and I Dream of Jeannie, reading how the camera frames each lead.",
   interrogate="What counts as a \"character-centered shot\" is an operational definition, and a different one tells a different story; two shows is a slice, not \"television.\"",
   flow=[("0:00","Warm-up + Look at This, a pair: a contemporary visual study leads, then the sitcom camerawork as the rigor case to interrogate."),
         ("0:07","Images on the same map, for real: embed an image set live and watch it cluster by visual style nobody tagged. The beyond-counting contrast at its sharpest."),
         ("0:25","Project lab: apply your method harder on your own data. Instructor floats; one-on-ones at the side."),
         ("1:05","Break"),
         ("1:15","The hand-labeling set-piece (Gemini-free): label 30 items from your corpus by hand; the AI labels the same 30; study every disagreement. Nobody skips this."),
         ("1:40","Fix-it check: a planted bug in the data pipeline, found AI-closed."),
         ("1:48","Check-out.")],
   reading="Gilardi et al. (2023) abstract, the AI as a cheaper coder, to prime Week 7. Supplement for sentiment projects: the Reagan/Swafford smoothing fight.",
   sketch="One disagreement between your labels and the AI's where you were right, and why. (Image projects: swap the image set or cluster count and screenshot how the grouping shifts.)",
   check="Fix it: the planted bug. (Competencies 1, 7.)",
   comps="1, 4, 7"),
 dict(n=7, title="The AI as a Reader, at Scale", tool="LLM-as-annotator, the most common operation in the field",
   promise="Use the AI to read your whole corpus at once, learn to trust the labels it's sure of and catch the ones it isn't, and reckon with whose judgment you're renting.",
   admire="Gilardi, Alizadeh & Kubli (2023): ChatGPT outperformed crowd workers on several text-labeling tasks, cheaper, faster, more consistent.",
   interrogate="The prompt is the codebook; agreement with humans isn't ground truth; and the model fails silently, confident wrong answers a human's disagreement would have caught. Its \"judgment\" is a compression of scraped creative work, whose reading are you renting?",
   flow=[("0:00","Warm-up + Look at This, room names the choice first: the AI as a cheaper coder, and where it fails silently."),
         ("0:10","The annotator move, on your corpus: write a labeling prompt for your categories, run it on a slice, read the labels back. Tighten the definition and watch the labels shift, the prompt is your codebook."),
         ("0:35","Confidence, and when to trust it: ask the model not just what but how sure. Sort by confidence, trust the sure labels, hand-check the unsure ones, which is exactly which 30 to pull for Week 6."),
         ("0:50","Break"),
         ("1:00","Accuracy check, then project workshop: run your prompt against a small hand-labeled gold set. Where does the AI disagree, and is it wrong or are you? Then build time on your corpus. Go further (optional, technically comfortable): instead of the closed API model, run an open model from Hugging Face, or fine-tune your own small classifier (ModernBERT) on the labels you just made, the third reader you own."),
         ("1:50","Gemini-free check and check-out.")],
   reading="One short piece on the training-data fight (the NYT v. OpenAI complaint summary, or a Books3 explainer), read against your own Week 4 licensing conversation.",
   sketch="Show one label the AI got confidently wrong and one it nailed; for each, say how you knew.",
   check="Explain it: what is your labeling prompt deciding on your behalf, and how would you check whether to trust a given label? (Competencies 2, 5.)",
   comps="2, 4, 5"),
 dict(n=8, title="Models as Time Capsules + Settle the Finding", tool="What a trained model is: a compression of its corpus",
   promise="Meet models that live entirely inside one historical period, learn what a famous model has secretly memorized, kill your own finding to see what survives, and leave with a prose draft.",
   admire="TimeCapsuleLLM, a small GPT trained from scratch on nothing but 1800s London publications, and \"Speak, Memory\" (Bamman's lab), which probes which books GPT-4 has effectively memorized.",
   interrogate="A period model speaks only for the period's published, surviving, digitized voices. And memorization isn't reading: models score higher on memorized books, so an LLM that seems to read your corpus may be partly reciting it, a validity problem, not just an ethics one.",
   flow=[("0:00","Warm-up + Look at This: TimeCapsuleLLM and \"Speak, Memory,\" screenshots ready. (These period models, and supplements like MonadGPT and MacBERTh, live on Hugging Face, where you can download and run open models, or fine-tune your own.)"),
         ("0:07","Kill it, then keep what survives, one continuous arc on your own results: shuffle the labels and re-run; split the corpus in half; ask \"compared to what?\". Then compress whatever survived into one headline sentence."),
         ("0:52","Break"),
         ("1:02","Gemini-free writing block: write your one-sentence interpretation yourself."),
         ("1:22","Writing workshop: opening question, what you found, what it does not show, the choices you made. Distill the Data Biography into the corpus note."),
         ("1:50","Check and check-out.")],
   reading="None required. Supplements: the MonadGPT and MacBERTh model pages, two more time capsules.",
   sketch="Expand to 600–1,000 words. Write your \"show your work\" appendix: what you cut, what surprised you, what the AI got wrong, and which robustness checks your finding survived.",
   check="Explain it: your headline finding, and what it does not show. (Competencies 3, 4.)",
   comps="3, 4, 5"),
 dict(n=9, title="Build the Page", tool="Publishing, Quarto to GitHub Pages, static by default",
   promise="Leave today with a deployed draft of your web essay at a public URL.",
   admire="Three published essays side by side: a Pudding piece, an Observable notebook, a Quarto site. The same goal, three defensible-but-different sets of choices.",
   interrogate="There's no single right way, only choices you can defend. Yours will be choices too.",
   flow=[("0:00","Look at This: the three essays, common structure, divergent choices."),
         ("0:15","Structured critique (Critical Response Process) in trios: statements of meaning, maker's questions, neutral questions, permissioned opinions."),
         ("0:50","Break"),
         ("1:00","Interrogate your own chart, the making-side mirror of Week 6's hand-labeling. Does the y-axis start at zero? Is the eye pulled toward a pattern the data won't support? Fix one thing."),
         ("1:15","Build lab: open the template you forked in Week 4; paste outline, charts, code; render; deploy. Static by default; JS opt-ins hit the code-review checkpoint."),
         ("1:50","Phone test in pairs. Check-out.")],
   reading="None.",
   sketch="Title your essay. Write the headline finding in one sentence.",
   check="Fix it: a planted bug in publishing/layout code (or in opted-in JS). (Competencies 1, 7.)",
   comps="1, 7, 8"),
 dict(n=10, title="The Showcase", tool="A public celebration; the two capstone assessments",
   promise="A 90-minute public event followed by a reception. Snacks. Music. Friends and family invited. Printed program with everyone's titles and URLs.",
   admire="The closing triptych, neural networks meet the art world: Edmond de Belamy (the market), Anna Ridler's Mosaic Virus (the labor), Refik Anadol's Unsupervised at MoMA (the museum).",
   interrogate="When a machine reads a culture's archive, what is it showing us, and who decided what went in? You started Week 1 loading a museum's data; you end watching a museum's data become the art.",
   flow=[("0:00","Welcome. This is a show, not a defense. The closing Look at This."),
         ("0:10","Presentations, 4–5 min each: corpus, headline finding, one surprise. Live URL projected."),
         ("1:30","Reception. Laptops at every seat with everyone's URLs loaded.")],
   reading="None.",
   sketch="Within one week after: a private one-page reflection summing up the term.",
   check="The oral walkthrough (the capstone): how you got your headline result, what it does not show, and how the tools actually work. Plus the workbench intro. (All eight competencies.)",
   comps="all eight"),
]

# ---------------------------------------------------------------------------
def esc(s: str) -> str:
    return html.escape(s, quote=False)

def page(title: str, body: str, depth: int = 0, active: str = "") -> str:
    base = "../" * depth
    def nav_link(href, label):
        cls = ' class="active"' if href == active else ''
        return f'<a href="{base}{href}"{cls}>{esc(label)}</a>'
    nav = "".join(nav_link(href, label) for href, label in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}, {esc(TITLE)}</title>
<meta name="description" content="{esc(TAGLINE)}">
<link rel="stylesheet" href="{base}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="{base}index.html">{esc(TITLE)}</a>
    <nav class="nav" aria-label="Primary">{nav}</nav>
  </div>
</header>
<main id="main" class="wrap">
{body}
</main>
<footer class="site-foot"><div class="wrap">
  <p>{esc(TITLE)}: a 10-week, project-based community course. $0 per student. Built to run on Google Colab's free tier.</p>
</div></footer>
</body>
</html>
"""

def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", path.relative_to(SITE.parent))

def ol(items): return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"
def ul(items): return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

# Pages ---------------------------------------------------------------------
def build_index():
    body = f"""
<section class="hero">
  <p class="eyebrow">A 10-week project-based course for curious adults</p>
  <h1>{esc(TITLE)}</h1>
  <p class="lede">{esc(TAGLINE)}</p>
  <p>Investigate cultural data at scale with an AI as your coding partner. You publish a web essay on a question only you would ask. No math, no coding to start, $0 to take part.</p>
  <p class="cta"><a class="button" href="syllabus.html">Read the syllabus</a> <a class="button ghost" href="schedule.html">See the ten weeks</a></p>
</section>

<section>
  <h2>The four tools</h2>
  {ul([
    "<strong>Counting</strong>: the honest floor, with no notion of meaning.",
    "<strong>Classification</strong>: train a transparent reader and see what it learned.",
    "<strong>Embeddings</strong>: items become positions on a map of meaning. The heart of the course.",
    "<strong>AI annotation</strong>: a powerful model reads your whole corpus; you decide which labels to trust.",
  ])}
  <p>Images count too. You count, classify, and embed pictures the same way as text.</p>
</section>

<section>
  <h2>What you make</h2>
  {ul([
    "A reproducible notebook: the record of your analysis, runnable top to bottom.",
    "A web essay built on it: an opening question, a few charts, an image finding, a corpus note, about 800 to 1,500 words.",
  ])}
</section>

<section>
  <h2>Who it's for</h2>
  <p>Curious adults, mixed coding backgrounds, most with little or none. The AI writes code; you think about culture.</p>
</section>
"""
    write(SITE / "index.html", page("Home", body, depth=0, active="index.html"))

def build_syllabus():
    comps = ol([esc(c) for c in COMPETENCIES])
    corpora = "".join(
        f"<tr><td><strong>{esc(name)}</strong></td><td>{esc(src)}</td><td>{esc(use)}</td></tr>"
        for name, src, use in STARTER_CORPORA
    )
    body = f"""
<h1>Syllabus</h1>
<p class="lede">Use code, statistics, and AI to investigate cultural data at scale, and publish a web essay on a question only you would ask.</p>

<section>
  <h2>The shape of the course</h2>
  {ul([
    "<strong>Weeks 1–3, Tour.</strong> Toy datasets; counting, then classification; all four methods previewed before you commit.",
    "<strong>Weeks 4–7, Project.</strong> Commit to a corpus and two methods by Week 4. A short tool beat each week (embeddings, images, AI annotation) plus a long project lab. One-on-ones in Weeks 5 and 6.",
    "<strong>Weeks 8–10, Publish.</strong> Settle the finding, build the page, ship a URL, show it.",
  ])}
  <p>Plan about three hours a week outside class.</p>
</section>

<section>
  <h2>Eight things you'll be able to do</h2>
  {comps}
</section>

<section>
  <h2>How you'll know you're learning</h2>
  <p>No grades, but real standards. Because an AI can produce work you don't understand, the course checks the thinking directly: a weekly check with the assistant closed (trace a cell, explain a result, fix a planted bug), a portfolio, an oral walkthrough, and the Week 6 hand-labeling against the AI's labels. Peer feedback is formative only.</p>
</section>

<section>
  <h2>The Data Biography</h2>
  <p>Written in Week 4 when you commit to a corpus (Heather Krause's framework): where your data came from and what it can and cannot tell you. Its distilled form becomes the essay's corpus note.</p>
</section>

<section>
  <h2>Setup</h2>
  {ul([
    "A Google account (for Colab and Google AI Studio).",
    "A GitHub account (for hosting your final essay).",
    "An AI assistant. The default is the Gemini API via Google AI Studio: free, no credit card, vision included. Other providers work the same way.",
    "A laptop that can run a browser. Colab provides the GPU when you need one.",
  ])}
  <p>No required spend. A $20/month chat subscription is optional and never needed for any part of the course.</p>
</section>

<section>
  <h2>Starter corpora</h2>
  <p>Stuck for a corpus by Week 4? These six are vetted and small enough to move fast.</p>
  <table><thead><tr><th>Corpus</th><th>Access</th><th>Best for</th></tr></thead><tbody>{corpora}</tbody></table>
</section>
"""
    write(SITE / "syllabus.html", page("Syllabus", body, depth=0, active="syllabus.html"))

def build_schedule():
    rows = "".join(
        f'<tr><td><a href="weeks/week-{w["n"]:02d}.html">Week {w["n"]}</a></td>'
        f'<td><strong>{esc(w["title"])}</strong></td>'
        f'<td>{esc(w["tool"])}</td>'
        f'<td>{esc(w["promise"])}</td></tr>'
        for w in WEEKS
    )
    body = f"""
<h1>The Ten Weeks</h1>
<p class="lede">Three acts: Tour (1–3), Project (4–7), Publish (8–10). Each week opens with a finished study you first admire, then take apart, and lands on something you build.</p>
<table class="schedule"><thead><tr><th>Week</th><th>Title</th><th>Tool / method</th><th>The promise</th></tr></thead>
<tbody>{rows}</tbody></table>
"""
    write(SITE / "schedule.html", page("Schedule", body, depth=0, active="schedule.html"))

def build_resources():
    tools = "".join(
        f'<tr><td><a href="{esc(url)}">{esc(name)}</a></td><td>{esc(note)}</td></tr>'
        for name, url, note in ANCHOR_TOOLS
    )
    reading = "".join(
        f"<tr><td>{esc(wk)}</td><td>{esc(main)}</td><td>{esc(supp)}</td></tr>"
        for wk, main, supp in READING_LIST
    )
    body = f"""
<h1>Resources</h1>

<section>
  <h2>The notebooks</h2>
  <p>One Colab notebook per tool (counting, classification, data cookbook, embeddings, annotator), plus Act-2 completion versions and a smoke test. In <code>notebooks/</code>; open in Colab and start with <code>_smoke_test.ipynb</code>.</p>
</section>

<section>
  <h2>Anchor tools</h2>
  <p>All free, browser-based, no install.</p>
  <table><thead><tr><th>Tool</th><th>Used in</th></tr></thead><tbody>{tools}</tbody></table>
</section>

<section>
  <h2>Reading at a glance</h2>
  <p>One main reading a week, one optional supplement; papers are abstract-and-figures, never full. Bring three questions: what did the authors decide, what's the load-bearing assumption, where's the gap?</p>
  <table><thead><tr><th>Week</th><th>Main</th><th>Supplement</th></tr></thead><tbody>{reading}</tbody></table>
</section>

<section>
  <h2>When you get stuck</h2>
  <p>Two kits in <code>kits/</code>: a <strong>common-errors cheat sheet</strong> (the errors a non-coder hits in Colab, with the phrase to paste back to the AI) and a <strong>pivot kit</strong> of vetted corpus-and-question pairs for when a project stalls.</p>
</section>
"""
    write(SITE / "resources.html", page("Resources", body, depth=0, active="resources.html"))

def build_about():
    body = f"""
<h1>About</h1>
<section>
  <h2>Who it's for</h2>
  <p>Curious adults, mixed coding backgrounds, most with little or none. Project-based, not a survey.</p>
</section>
<section>
  <h2>Cost</h2>
  <p>$0 by default. The free Gemini tier covers it; a $20/month chat subscription is optional and never required.</p>
</section>
<section>
  <h2>The AI as a tool, not an oracle</h2>
  <p>The AI writes code and helps you build, but it has known failure modes: false confidence, shrinking your question to fit the tool, insecure code, weak non-English. Each session has a stretch with it closed, so you leave able to reproduce your own work.</p>
</section>
<section>
  <h2>The showcase</h2>
  <p>By Week 10 you'll have a URL you can send to your group chat. The page will load. There will be a chart. There will be an image. There will be an argument. Strangers will read it.</p>
</section>
"""
    write(SITE / "about.html", page("About", body, depth=0, active="about.html"))

def build_weeks():
    for i, w in enumerate(WEEKS):
        flow_rows = "".join(f'<tr><td class="time">{esc(t)}</td><td>{esc(a)}</td></tr>' for t, a in w["flow"])
        prev_link = f'<a href="week-{w["n"]-1:02d}.html">&larr; Week {w["n"]-1}</a>' if i > 0 else "<span></span>"
        next_link = f'<a href="week-{w["n"]+1:02d}.html">Week {w["n"]+1} &rarr;</a>' if i < len(WEEKS)-1 else "<span></span>"
        body = f"""
<p class="crumb"><a href="../schedule.html">&larr; All ten weeks</a></p>
<article>
  <p class="eyebrow">Week {w['n']}</p>
  <h1>{esc(w['title'])}</h1>
  <p class="lede">{esc(w['promise'])}</p>
  <p class="meta"><strong>Tool / method:</strong> {esc(w['tool'])} &nbsp;·&nbsp; <strong>Competencies:</strong> {esc(w['comps'])}</p>

  <section class="callout">
    <h2>Look at This, then Question It</h2>
    <p><strong>Admire:</strong> {esc(w['admire'])}</p>
    <p><strong>Interrogate:</strong> {esc(w['interrogate'])}</p>
  </section>

  <section>
    <h2>The session, minute by minute</h2>
    <table class="flow"><thead><tr><th>Time</th><th>Activity</th></tr></thead><tbody>{flow_rows}</tbody></table>
  </section>

  <section>
    <h2>Reading and homework</h2>
    <p><strong>Reading:</strong> {esc(w['reading'])}</p>
    <p><strong>Sketch:</strong> {esc(w['sketch'])}</p>
    <p><strong>Competency check:</strong> {esc(w['check'])}</p>
  </section>
</article>
<nav class="pager">{prev_link}{next_link}</nav>
"""
        write(WEEKS_DIR / f"week-{w['n']:02d}.html", page(f"Week {w['n']}: {w['title']}", body, depth=1))

CSS = """/* Culture as Data, one stylesheet. System fonts, high contrast, reads with JS off. */
:root{
  --ink:#1a1a1a; --muted:#5a5a52; --bg:#fbfaf7; --card:#fff; --line:#e3e0d8;
  --accent:#7a3b2e; --accent-soft:#f0e9e2; --max:46rem;
}
*{box-sizing:border-box}
html{font-size:18px;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  line-height:1.62}
.wrap{width:100%;max-width:var(--max);margin:0 auto;padding:0 1.25rem}
.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;background:var(--card);padding:.5rem 1rem;border:1px solid var(--line);z-index:10}
a{color:var(--accent)}
a:hover{text-decoration:none}
h1,h2,h3{line-height:1.2;letter-spacing:-0.01em}
h1{font-size:2.15rem;margin:.2em 0 .3em}
h2{font-size:1.4rem;margin:2em 0 .5em}
p{margin:.7em 0}
section{margin:1.5rem 0}
.eyebrow{text-transform:uppercase;letter-spacing:.12em;font-size:.72rem;color:var(--muted);font-weight:600;margin:0}
.lede{font-size:1.2rem;color:#333}
.meta{color:var(--muted);font-size:.92rem}
/* header / nav */
.site-head{background:var(--card);border-bottom:1px solid var(--line)}
.site-head .wrap{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:.5rem 1rem;padding-top:.8rem;padding-bottom:.8rem}
.brand{font-weight:700;font-size:1.1rem;text-decoration:none;color:var(--ink);letter-spacing:-0.01em}
.nav{display:flex;flex-wrap:wrap;gap:.1rem .4rem}
.nav a{padding:.25rem .55rem;border-radius:6px;text-decoration:none;color:var(--muted);font-size:.95rem}
.nav a:hover{background:var(--accent-soft);color:var(--accent)}
.nav a.active{color:var(--ink);font-weight:600}
/* hero */
.hero{padding:1.5rem 0 .5rem;border-bottom:1px solid var(--line)}
.cta{margin-top:1.1rem}
.button{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;padding:.55rem 1.1rem;border-radius:8px;font-weight:600;font-size:.98rem}
.button.ghost{background:transparent;color:var(--accent);border:1px solid var(--accent)}
.button:hover{opacity:.9}
/* tables */
table{border-collapse:collapse;width:100%;margin:1rem 0;font-size:.95rem;background:var(--card)}
th,td{text-align:left;vertical-align:top;padding:.55rem .7rem;border-bottom:1px solid var(--line)}
th{font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.flow .time,.schedule td:first-child{white-space:nowrap;color:var(--muted);font-variant-numeric:tabular-nums}
/* callout */
.callout{background:var(--accent-soft);border:1px solid var(--line);border-radius:10px;padding:.4rem 1.1rem}
.callout h2{margin-top:.7rem}
.crumb,.pager{font-size:.9rem}
.pager{display:flex;justify-content:space-between;margin:2rem 0 1rem;border-top:1px solid var(--line);padding-top:1rem}
ol,ul{padding-left:1.3rem}
li{margin:.35em 0}
code{background:var(--accent-soft);padding:.08em .35em;border-radius:4px;font-size:.9em}
/* footer */
.site-foot{border-top:1px solid var(--line);margin-top:3rem;color:var(--muted);font-size:.88rem}
.site-foot .wrap{padding-top:1.2rem;padding-bottom:2rem}
@media (max-width:560px){html{font-size:17px}h1{font-size:1.8rem}.lede{font-size:1.1rem}}
"""

def build_assets():
    write(SITE / "assets" / "style.css", CSS)
    write(SITE / ".nojekyll", "")

def build_buildnote():
    note = """# How the site is generated

This site is produced by `../../tools/build_site.py`, a small Python script with no
dependencies beyond the standard library. The page content is curated from the four design
docs (`overview.md`, `syllabus.md`, `lesson-plans.md`, `planning-doc.md`) and held as
structured data inside the script, so the site and the docs stay in step: when a doc changes,
update the matching data in `build_site.py` and re-run

    python tools/build_site.py

It emits plain HTML plus one CSS file. There is **no server build step**, deploy by pushing
`site/` to a `gh-pages` branch or serving it from `/docs`. Every page reads fully with
JavaScript disabled.

**Why a Python script and not Quarto?** BUILD-PLAN §2 allows either. The script was chosen for
trivially-reproducible regeneration and zero server build step. (Quarto would have the
pedagogical bonus of dogfooding the student toolchain; if you later prefer it, the structured
content here ports cleanly to `.qmd`.)
"""
    write(SITE / "_build" / "README.md", note)

def main():
    build_assets()
    build_index()
    build_syllabus()
    build_schedule()
    build_resources()
    build_about()
    build_weeks()
    print("Site built, docs/ ready for GitHub Pages.")


if __name__ == "__main__":
    main()
