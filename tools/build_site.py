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
TAGLINE = "Ask your own questions about the stories, lyrics, art, and online communities you care about."

NAV = [
    ("index.html", "Home"),
    ("syllabus.html", "Syllabus"),
    ("schedule.html", "Schedule"),
    ("notebooks.html", "Materials"),
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
    ("NYT Wedding Announcements 1985–2014 ⭐", "TheUpshot/nyt_weddings, a CSV", "counting across time, gender, class signaling"),
    ("Pantheon famous people ⭐", "pantheon.world, a CSV of 11,000+ figures", "how a culture decides who matters; status and prestige"),
    ("Billboard Hot 100 + audio features ⭐", "Kaggle CSV (Spotify's audio API closed in 2024)", "did hit music get more homogeneous over time?"),
    ("Met / MoMA Open Access ⭐", "CC0 spreadsheet, ~500K objects with images", "image embeddings, who gets collected, cataloging language"),
    ("/r/AmITheAsshole judgments", "Pushshift mirror on HuggingFace", "AI-as-reader (moral classification), reception analysis"),
    ("Eurovision lyrics 1956–2023", "Spijkervet/eurovision-dataset on GitHub", "counting across languages, sentiment, diachronic shift"),
    ("TMDb movie posters of one genre", "TMDb API, free key", "image embeddings, color analysis, CLIP search"),
    ("Bluesky one-hour firehose slice", "Jetstream, no API key, atproto SDK", "any of the four methods, social-media work"),
    ("LinCE code-switching corpora", "Hugging Face datasets, one-line load", "how bilinguals switch languages; mixed-language identity"),
    ("CLICS colexifications", "clics.clld.org, browse in-browser", "do languages carve up meaning the same way? (networks)"),
]

ANCHOR_TOOLS = [
    ("OpenAI Tokenizer / Tiktokenizer", "https://platform.openai.com/tokenizer", "Week 2, what counts as a word"),
    ("Google Teachable Machine", "https://teachablemachine.withgoogle.com/", "Week 3. Train a classifier in minutes"),
    ("Hugging Face", "https://huggingface.co/", "Weeks 5–8, the public hub where open models live"),
    ("TensorFlow Embedding Projector", "https://projector.tensorflow.org/", "Week 5, plots text and images"),
    ("CLIP image-search demo (optional)", "https://huggingface.co/spaces", "Week 6, search images by typing words"),
]


# Notebooks: Colab/GitHub links surfaced on the site --------------------------------
GH_REPO = "https://github.com/lucianli123/culture-as-data-2026"
COLAB = "https://colab.research.google.com/github/lucianli123/culture-as-data-2026/blob/main/"

NOTEBOOKS = [
    ("notebooks/week01_first_investigation.ipynb", 1, "Your first investigation", "Load the wedding data, make your first chart, learn to read an error and recover, count words and pixels."),
    ("notebooks/week02_counting.ipynb", 2, "Counting", "Bag-of-words by hand-logic, tf-idf, keyness (the She Giggles, He Gallops method), and the shuffle test."),
    ("notebooks/week03_classification.ipynb", 3, "Classification", "Train a logistic regression and read its signed weights, the model's mind on the table."),
    ("notebooks/week04_data_cookbook.ipynb", 4, "The data cookbook", "Three routes to a corpus: load a file, call an API, scrape politely. Saves your corpus to Drive."),
    ("notebooks/week05_embeddings.ipynb", 5, "Embeddings", "Embed your own corpus (text or images), look for unexpected clusters, and compare PCA against t-SNE."),
    ("notebooks/week07_annotator.ipynb", 7, "The AI as annotator", "Gemini labels your corpus at scale; you audit it by confidence and a hand-labeled gold set."),
]
NOTEBOOK_VARIANTS = {
    5: [("GUIDED", "notebooks/week05_embeddings_GUIDED.ipynb"), ("SKELETON", "notebooks/week05_embeddings_SKELETON.ipynb")],
    7: [("GUIDED", "notebooks/week07_annotator_GUIDED.ipynb"), ("SKELETON", "notebooks/week07_annotator_SKELETON.ipynb")],
}
SOCIAL_STARTERS = [
    ("notebooks/social-media-starters/reddit_starter.ipynb", "Reddit, three routes", "Historical archives on Hugging Face, the official API via PRAW, and a fiction loader for r/nosleep and r/HFY."),
    ("notebooks/social-media-starters/bluesky_jetstream.ipynb", "Bluesky firehose", "The most open social corpus: no key, hundreds of thousands of public posts an hour."),
    ("notebooks/social-media-starters/mastodon_api.ipynb", "Mastodon", "Per-instance public timelines; the server you choose is a corpus choice."),
    ("notebooks/social-media-starters/gutenberg_fiction.ipynb", "Project Gutenberg", "Public-domain genre fiction by ID: full text, zero legal risk."),
    ("notebooks/social-media-starters/letterboxd_scraper_template.ipynb", "Polite scraper template", "The Letterboxd pattern with the delay and checklist built in; Goodreads via the UCSD Book Graph instead."),
]

COOL_METHODS = [
    ("notebooks/cool-methods/character_networks.ipynb", "Character networks", "Who shares a scene with whom: a network from any fiction corpus."),
    ("notebooks/cool-methods/sentiment_arcs.ipynb", "Sentiment arcs", "The Syuzhet move in Python, smoothing controversy included."),
    ("notebooks/cool-methods/stylometry_starter.ipynb", "Stylometry", "Authorship by function words, the Rowling-unmasking method."),
    ("notebooks/cool-methods/finetune_modernbert.ipynb", "Fine-tune ModernBERT", "Train a classifier you own on the labels from Week 7."),
]

def nb_buttons(path, primary=True):
    cls = "button" if primary else "button ghost"
    return (f"<a class='{cls}' href='{COLAB}{path}'>Open in Colab</a> "
            f"<a class='button ghost' href='{GH_REPO}/blob/main/{path}'>View on GitHub</a>")

READING_LIST = [
 ("1", "<a href='https://www.pnas.org/doi/10.1073/pnas.2102061118'>Bollen et al., the cognitive-distortions hockey stick (PNAS 2021)</a>, with the <a href='https://www.pnas.org/doi/10.1073/pnas.2115010118'>Schmidt et al. critique</a>", "<a href='https://www.robinsloan.com/notes/writing-with-the-machine/'>Robin Sloan, Writing with the machine</a>", "<a href='https://newleftreview.org/issues/ii1/articles/franco-moretti-conjectures-on-world-literature'>Moretti, Conjectures on World Literature (NLR 2000)</a>, the founding argument for reading culture at scale"),
 ("2", "<a href='https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/'>Wolfram, What Is ChatGPT Doing</a> (opening sections only)", "<a href='https://en.wikipedia.org/wiki/Zipf%27s_law'>Zipf's law</a>, the straight line in every text", "<a href='https://web.stanford.edu/~jgrimmer/tad2.pdf'>Grimmer &amp; Stewart, Text as Data (2013)</a>, §1–4: all quantitative models of language are wrong, but some are useful"),
 ("3", "<a href='https://americaspublicbible.org/'>Mullen, America's Public Bible</a> (intro + a verse)", "<a href='https://tedunderwood.com/2023/03/19/using-gpt-4-to-measure-the-passage-of-time-in-fiction/'>Underwood on GPT-4 and fictional time</a>; <a href='https://www.scientificamerican.com/article/how-a-computer-program-helped-show-jk-rowling-write-a-cuckoos-calling/'>Juola's Rowling unmasking</a>", "<a href='https://doi.org/10.22148/16.005'>Underwood, The Life Cycles of Genres (2016)</a>, the full paper behind today's featured study"),
 ("4", "<a href='https://gijn.org/stories/data-biographies-getting-to-know-your-data/'>Krause, Data Biographies</a> (We All Count)", "<a href='https://dfreelon.org/publications/2018_Computational_research_in_the_postAPI_age.pdf'>Freelon, Post-API Age</a>", "<a href='https://doi.org/10.1080/1369118X.2012.678878'>boyd &amp; Crawford, Critical Questions for Big Data (2012)</a>, the canonical statement of what large datasets cannot tell you"),
 ("5", "<a href='https://jalammar.github.io/illustrated-word2vec/'>Alammar, The Illustrated Word2Vec</a>, plus the debate: <a href='https://journals.sagepub.com/doi/10.1177/0003122419877135'>Kozlowski/Taddy/Evans, The Geometry of Culture (ASR 2019)</a> vs. <a href='https://arxiv.org/abs/1607.06520'>Bolukbasi et al. (2016)</a>", "The second pairing: <a href='https://arxiv.org/abs/1608.07187'>Caliskan et al. (2017)</a> vs. <a href='https://www.publicbooks.org/how-words-lead-to-justice/'>Soni/Klein, How Words Lead to Justice</a>; <a href='https://research.atspotify.com/algorithmic-effects-on-the-diversity-of-consumption-on-spotify/'>Anderson et al., Spotify diversity</a>", "<a href='https://doi.org/10.1177/0003122419877135'>Kozlowski et al., The Geometry of Culture (2019)</a> in full; <a href='https://distill.pub/2016/misread-tsne/'>Wattenberg, Viégas &amp; Johnson, How to Use t-SNE Effectively (Distill 2016)</a>"),
 ("6", "<a href='https://www.pnas.org/doi/10.1073/pnas.2305016120'>Gilardi et al. (2023)</a>, the AI as a cheaper coder", "<a href='https://link.springer.com/article/10.1140/epjds/s13688-016-0093-1'>Reagan et al., Six Basic Shapes</a> (the smoothing fight); <a href='https://selfiecity.net/'>Manovich, Selfiecity</a>", "<a href='https://doi.org/10.1093/llc/fqz013'>Arnold &amp; Tilton, Distant Viewing (DSH 2019)</a>, the theory behind treating images as data"),
 ("7", "<a href='https://www.npr.org/2025/03/26/nx-s1-5288157/new-york-times-openai-copyright-case-goes-forward'>NYT v. OpenAI</a>, read against your Week 4 licensing conversation", "<a href='https://www.pnas.org/doi/10.1073/pnas.2305016120'>Gilardi et al., full</a>; <a href='https://arxiv.org/abs/2410.12029'>Bamman et al., LLM classification in cultural analytics (CHR 2024)</a>", "<a href='https://doi.org/10.1162/coli_a_00502'>Ziems et al., Can LLMs Transform Computational Social Science? (CL 2024)</a>, the systematic evaluation behind this week's method"),
 ("8", "<a href='https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web'>Ted Chiang, ChatGPT Is a Blurry JPEG of the Web (2023)</a>, the compression idea this week is built on", "<a href='https://github.com/haykgrigo3/TimeCapsuleLLM'>TimeCapsuleLLM</a> and <a href='https://aclanthology.org/2023.emnlp-main.453/'>Speak, Memory</a>; period models <a href='https://huggingface.co/Pclanglais/MonadGPT'>MonadGPT</a> and <a href='https://huggingface.co/emanjavacas/MacBERTh'>MacBERTh</a>", "<a href='https://doi.org/10.1086/702594'>Da, The Computational Case Against Computational Literary Studies (2019)</a>, the field's sharpest critique, read against your own robustness checks"),
 ("9", "None", "<a href='https://pudding.cool/process/pivot-continue-down/'>A Pudding process post</a>", "<a href='https://critinq.wordpress.com/2019/03/31/computational-literary-studies-a-critical-inquiry-online-forum/'>the Critical Inquiry online forum</a>: Underwood and others answer Da, a discipline arguing about itself in public"),
 ("10", "None", "<a href='https://en.wikipedia.org/wiki/Edmond_de_Belamy'>Edmond de Belamy</a>; <a href='https://annaridler.com/works/myriad-tulips'>Ridler's Mosaic Virus</a>; <a href='https://www.moma.org/calendar/exhibitions/5535'>Anadol's Unsupervised</a>", "<a href='https://arxiv.org/abs/1706.07068'>Elgammal et al., CAN: Creative Adversarial Networks (2017)</a>, the paper behind the de Belamy generation of AI art"),
]

# Slide-deck data (one-line sketch + the three per-deck through-lines), consumed by
# slides/export_slides.py so the decks and the site share one content source. -----
SLIDES_SKETCH={1:"One question from your life answerable with text or image data; three sentences.",
2:"Count something in a text you care about; one chart; one sentence naming a choice. If the count compares two things, shuffle-test the gap.",
3:"Train a quick logistic regression on a labeled set; screenshot its five most positive and negative words.",
4:"Write your Data Biography (~400 words) and actually collect your corpus with the cookbook.",
5:"Toggle PCA vs. t-SNE and screenshot how the map changes; name one cluster you believe and one you don't.",
6:"One disagreement between your labels and the AI's where you were right, and why.",
7:"Show one label the AI got confidently wrong and one it nailed; say how you knew.",
8:"Expand to 600 to 1,000 words; write your show-your-work appendix and which checks survived.",
9:"Title your essay; write the headline finding in one sentence.",
10:"Within a week after: a private one-page reflection."}

SLIDES_THREADS={
1:[("Read work critically","She Giggles, He Gallops is excellent and its choices are debatable. Admiring and questioning at once is the habit the course is built on."),
   ("Make something real","A complete investigation by the first break, before any theory."),
   ("Images are culture too","A picture is numbers: you counted pixels on day one, and images continue as a co-equal corpus through all ten weeks.")],
2:[("Beyond counting","Counting is the simplest tool and has no notion of meaning. Week 5 addresses that limit."),
   ("Every count is a choice","Tokens, stemming, the corpus, the chart's axis, each hides a decision you made."),
   ("Is the difference real?","Shuffle the labels and count again, one thousand times; if chance often matches your gap, do not trust it.")],
3:[("The reader you can see","The transparent classifier: read its signed weights and see exactly what it learned. Week 7 introduces the opaque counterpart."),
   ("Bias comes from the training set","The Teachable Machine demonstration: a machine learns the prejudice of the data it is given."),
   ("Every choice is a choice","What counts as a label, and which words you hand it, decide what it learns.")],
4:[("Whose data","The Data Biography: where it came from, who is missing, what it cannot say."),
   ("The licensing line","CC0, to scrape-with-care, to never (LibGen). Judgment, not a rulebook."),
   ("Make something real","You leave with a real corpus in hand and a project repo born.")],
5:[("Beyond counting (the payoff)","The same counting question from Week 2, now embedded: clusters counting could not see."),
   ("Every chart is a choice","PCA vs t-SNE rearranges the same data; the picture made a decision."),
   ("Whose data","A direction found in the corpus: cultural discovery (Kozlowski) or encoded prejudice (Bolukbasi)?")],
6:[("Images are culture too","Their deepest day: pictures cluster by a visual style nobody tagged."),
   ("Where the AI fails on your data","Hand-label 30 the AI also labels; study every disagreement."),
   ("The two readers (calibration)","This hand-check is the bridge between the cheap reader and the powerful one.")],
7:[("The reader you can't see","The powerful, opaque annotator: trust the labels it is sure of, check the rest."),
   ("Whose judgment are you renting","Its reading was learned from creative work scraped largely without permission."),
   ("The third reader (go further)","Fine-tune a model you own, transparent, powerful, now yours.")],
8:[("Whose data, at full scale","A model is its corpus: bound the corpus and you bound the mind."),
   ("Memorization isn't reading","A model may recite your corpus rather than read it, a validity problem, not just ethics."),
   ("Test it, then keep what survives","The Week 2 trial's method, now applied to your own finding.")],
9:[("Interrogate your own chart","Ten weeks on other people's charts; now the ten minutes on yours."),
   ("No single right way","Three published essays, three defensible sets of choices."),
   ("Make something real","You leave with a deployed URL.")],
10:[("Whose data, whose authorship","The art triptych, de Belamy to Ridler to Anadol: who decided what went in?"),
   ("Understand, not commission","The oral walkthrough an AI cannot do for you."),
   ("All threads converge","You started loading a museum's data; you end watching it become the art.")],
}

# Content slides (the substance of each deck): heading + concrete bullets. Rendered
# between "Question It" and "Three modes" in both the .md and .pptx decks. ----------
SLIDES_CONTENT={
1:[("Why this course: the stakes",
   ["Machines already read culture at scale: the feed ranking what you see, the moderation filter, the model trained on scraped art and prose. That reading shapes which culture reaches you, and it happens without you.",
    "Reading culture with machines produces real knowledge and real mistakes, and the two look identical until someone checks. Learning to check is the course.",
    "Ten weeks from now, you do the reading: a question you chose, a corpus you built, a published finding anyone can verify.",
    "The whole method in one sentence: it is all counting and weighting, and you can learn to read both."]),
  ("What counting culture has found",
   ["In the stage directions of 2,000 film scripts: women snuggle, giggle, and sob; men strap, gallop, and kill. 85% of the screenwriters were men (The Pudding, 2017).",
    "Across 17,000 Hot 100 songs, the biggest revolution in American pop was not the Beatles in 1964; it was hip-hop in 1991 (Mauch et al., 2015).",
    "Counting small words like 'the' and 'of' unmasked Robert Galbraith as J.K. Rowling within days (Juola, 2013).",
    "A model trained on Google News completes 'man is to computer programmer as woman is to...' with 'homemaker' (Bolukbasi et al., 2016).",
    "An AI portrait sold at Christie's for $432,500; the training data was other people's paintings (2018). Every one of these is a count, and every one has arguable choices. Both halves are the course."]),
  ("Four words, used all term",
   ["Corpus: the pile you study. 500 announcements, 2,000 screenplays, 10,000 album covers.",
    "Method: the counting or weighting you run on the corpus.",
    "Model: any simplification that turns culture into numbers. A word count is already one.",
    "Embedding: a few hundred numbers that place an item on a map of meaning. Week 5."]),
  ("The Drive routine (every week, without exception)",
   ["Colab wipes its machine when you idle. Your mounted Drive folder is what survives.",
    "Copy the notebook to Drive, mount Drive, save everything to the one project folder.",
    "Your Week-4 corpus has to be alive in Week 5. This ritual is how.",
    "Gemini key goes in Colab Secrets. Never pasted into code."]),
  ("When code fails (it will, today, deliberately)",
   ["Read the last line of the traceback first. It names the problem.",
    "Paste it to the AI: \"this errored, fix it and tell me what went wrong.\"",
    "Try twice, then ask a human. In that order.",
    "Keep the cheat sheet at hand. No one memorizes error messages; everyone reads them."]),
  ("Counting, three shapes",
   ["Rows: what share of brides kept their name, year by year. One groupby, one chart.",
    "Words: the top words of a lyric are \"the, and, you\" until you remove stop-words. That removal is your first modeling choice.",
    "Pixels: rank 200 Met thumbnails darkest to brightest from average luminance.",
    "The same technique three times, each containing a decision."])],
2:[("The trial: Bollen et al. v. Schmidt",
   ["The claim (PNAS 2021): phrases of distorted thinking (\"I am a failure,\" \"everyone hates me\") surge in Google Books after 2000. A hockey stick.",
    "The objection: Google scanned more fiction after 2000. Maybe the surge is novels, not distress.",
    "The rebuttal: the authors deleted the entire fiction corpus and re-ran the analysis. The pattern largely held.",
    "The method worth adopting: answer \"your corpus is biased\" with a test rather than an argument."]),
  ("What counts as a word?",
   ["Two tokenizers shatter the same sentence differently: \"don't\" becomes one chip, two, or three.",
    "Models never see words. They see tokens, and the split is a design decision.",
    "Your hand-count argument about run/running is the same decision, made with highlighters.",
    "tf-idf: down-weight what is common everywhere. \"Common here, rare overall\" is what characterizes a text."]),
  ("Keyness: what makes a voice distinctive",
   ["For every word: how much likelier is it in corpus A than corpus B? A log-odds ratio, smoothed so rare words don't explode.",
    "Strongly positive = distinctively A. Strongly negative = distinctively B. The middle is shared language.",
    "She Giggles, He Gallops is exactly this method: verbs after \"she\" vs. \"he\" in 2,000 screenplays. Women snuggle, giggle, squeal; men gallop, strap, shoot.",
    "The corpus pair is a choice: this artist against pop, this subreddit against a novel. Different pair, different \"distinctive.\""]),
  ("The shuffle test: is the gap real?",
   ["The question: could randomly dealt labels produce a gap this large?",
    "Shuffle the labels, recount, 1,000 times. Mark where the real gap lands in that pile.",
    "Chance rarely matches it: a finding. Chance matches it often: a coincidence.",
    "It says \"probably not chance.\" It never says \"big enough to matter.\" Effect size is your argument to make."])],
3:[("Underwood's classifier, in detail",
   ["A logistic regression, the exact tool of today's lab, trained on a century of novels to recognize detective fiction and science fiction.",
    "Its most famous error is the lesson: it misreads Pynchon's The Crying of Lot 49, a novel critics call a detective-fiction spoof.",
    "Genre boundaries are real but fuzzy, and the classifier's mistake is what shows it.",
    "Ask of every classifier, including yours: where does it fail, and what does the failure teach?"]),
  ("A classifier is counting with weights",
   ["Every word casts a vote, for or against. The model adds the votes.",
    "Training means learning the weights from labeled examples.",
    "Read the signed weights: the most positive and most negative words are the model's mind on the table.",
    "Spam filters have worked exactly this way for twenty years."]),
  ("The training set is the lesson",
   ["Teachable Machine, live: a cat/dog model trained only on orange cats and brown dogs.",
    "The room predicts what a black cat will do. Then watches it happen.",
    "Bias is not a ghost in the machine. It is the training set, and you assembled it.",
    "One connection to remember: today's classifier is one neuron; stack many and you have Week 7's model."]),
  ("The methods menu (before you commit)",
   ["Counting and keyness: differences and trends. Classification: sort and label at scale. Embeddings (W5): a map of meaning. Annotation (W7): the AI reads for you.",
    "Optional add-ons where they fit: character networks, sentiment arcs, CLIP image search, a fine-tuned ModernBERT.",
    "The corpus-existence rule: bring a screenshot of 50 loadable rows of your data to Week 4. No proof, no pitch."])],
4:[("What a viable pitch contains",
   ["Three minutes, hard cap: your corpus (existence proof on screen), your two methods, and what would count as a finding.",
    "\"Explore themes in music\" is not answerable. \"Did Billboard #1 lyrics narrow in vocabulary 1990-2020?\" is.",
    "A null result, honestly shown, is a complete project: \"I expected X, the data doesn't show it, here's how I know.\"",
    "The pivot kit exists because corpora fail. Adopting a fallback pair is normal, not a failure."]),
  ("Licensing rules, in one slide",
   ["CC0 museum data and public-domain books: use freely, republish freely.",
    "Academic corpora: analyze, don't redistribute. Lyrics and review text: metadata and counts only.",
    "AO3 and other community-opposed archives: a small attributed sample at most, never a shared dataset.",
    "Shadow-library books: never. That line is what the field's $1.5B settlement was about."]),
  ("Three routes to a corpus",
   ["Route 1, the common case: a prepared file. pd.read_csv(url), gdown for Drive links, load_dataset() for Hugging Face.",
    "Route 2: an API, the sanctioned route. The Met's endpoint returns JSON, no key required.",
    "Route 3, a last resort: scraping, done carefully. Read robots.txt and the terms of service, request slowly, take only what you need, never republish.",
    "Whatever the route: save the result to your Drive project folder today. Week 5 depends on it."]),
  ("The Data Biography (~400 words, due Week 5)",
   ["Where did this data come from, and who made it?",
    "Who is in it, and who is missing from it?",
    "What can it not tell you, no matter how cleverly you count?",
    "Its distilled form becomes your essay's corpus note in Week 8. Write it once, use it twice."])],
5:[("The problem counting cannot solve",
   ["To a counter, \"happy\" and \"joyful\" are unrelated strings. Zero overlap.",
    "An embedding turns each item into a vector, a few hundred numbers, positioned by the company the item keeps.",
    "Near in that space means similar in learned context: happy and joyful end up neighbors because they appear in the same company.",
    "Neighbors are context-mates, not dictionary synonyms. Correct this misconception explicitly."]),
  ("The debate: discovery, or bias read back?",
   ["Kozlowski, Taddy & Evans (2019): a rich-poor direction in embedding space tracks the cultural structure of class across a century. Culture made measurable.",
    "Bolukbasi et al. (2016): the same kind of direction pairs man:programmer :: woman:homemaker. Prejudice the model absorbed, to be removed.",
    "Identical technique. Opposite verdicts.",
    "The room settles it: what makes a found dimension a discovery vs. the corpus's own bias, the data, the purpose, or what you do with the result?"]),
  ("The chart is a choice",
   ["PCA and t-SNE flatten the same vectors two ways: clusters tighten, distances shift, a grouping you trusted can dissolve.",
    "\"Near\" means probably similar. Exact distances on the flattened map mean little.",
    "A visualization is an argument with decisions baked in: projection, axes, what's dropped.",
    "Homework: toggle PCA against t-SNE on your own map. Name one cluster you believe and one you do not."]),
  ("The recommender aside (five minutes, strictly limited)",
   ["\"For You\" is this same map plus your history: you are a point in taste-space, the feed is your nearest neighbors.",
    "Spotify's own researchers found algorithmic listening less diverse than organic listening (Anderson et al., 2020).",
    "You built the same machinery today."])],
6:[("The featured pair, in detail",
   ["Arnold, Tilton & Berke (2019): computer vision on every shot of Bewitched and I Dream of Jeannie, measuring how the camera frames each lead.",
    "\"Character-centered shot\" is an operational definition. Change the definition, change the story.",
    "Two network sitcoms is a slice, not \"television.\"",
    "Turn the same eye on your project: what did YOU operationalize this week, and what would a different definition show?"]),
  ("Images on the same map",
   ["CLIP embeds pictures into a shared space with words: your album covers, paintings, posters become vectors.",
    "Watch an image set cluster by visual style nobody tagged: the beyond-counting contrast at its sharpest.",
    "Week 1 ranked pixels by brightness; today style emerges unasked. Same corpus, two rungs of the ladder."]),
  ("The hand-labeling exercise (required of everyone)",
   ["Label 30 items from your own corpus, by hand, no AI.",
    "The AI labels the same 30. Study every disagreement: is it wrong, or are you?",
    "This is calibration: learning exactly where the machine's reading of YOUR data breaks.",
    "Deliberately done without the AI. It is the one exercise code cannot teach."])],
7:[("The powerful, opaque reader",
   ["Gilardi et al. (2023): ChatGPT out-labeled paid crowd workers on political-text tasks at roughly a twentieth of the cost.",
    "Your prompt IS the codebook: categories, definitions, edge-case rules. Write it like one.",
    "Change one line of the codebook and the same machine becomes a different reader.",
    "It fails silently. Confident-and-wrong looks identical to confident-and-right from the outside."]),
  ("Trust, by confidence",
   ["Ask for a confidence number with every label. Sort ascending. Hand-check the bottom.",
    "Gold set first: label ~30 items yourself before the machine sees them. Agreement against gold is your accuracy floor.",
    "Disagreements are data: sometimes the model is wrong, sometimes your codebook was vague.",
    "Whose reading are you renting? A model trained largely on scraped creative work. Week 8 takes that up."]),
  ("Three readers, one course",
   ["Week 3, the transparent reader: a logistic regression whose weights you can read.",
    "Week 7, the powerful reader: an API model you audit by confidence and gold set.",
    "Go-further, the reader you own: fine-tune ModernBERT on your own labels. Free to run, and it is yours."])],
8:[("Stress-test the finding",
   ["Bollen's method, applied to your own finding: remove the slice that most concerns you and re-run.",
    "If the pattern survives, report it with the check shown. If it does not, you have learned what the finding depended on.",
    "Minimum bar: ONE robustness check, the one that most threatens your result.",
    "\"I expected X, the data doesn't show it, here's how I know\" is a complete, publishable result."]),
  ("Memorization isn't reading",
   ["Speak, Memory (Chang et al., 2023): name-cloze tests show GPT-4 has memorized many novels; it fills in \"___ Bennet\" without reading anything.",
    "A model may be reciting your corpus rather than analyzing it: a validity problem, not only an ethics one.",
    "TimeCapsuleLLM: train only on 1800s London text and the model speaks its era. A model is bounded by its corpus.",
    "Ask of every model you used: what was in its training data, and does that undercut MY claim?"]),
  ("The show-your-work appendix",
   ["Your method choices, your moments of doubt, what you cut, what the AI got wrong.",
    "Name where a reader could reasonably disagree with you, before they do.",
    "The honesty you demanded of published work all term, turned on yourself. (Data Feminism's practice, run quietly all course.)"])],
9:[("Interrogate your own chart",
   ["Does the y-axis start at zero, or is the plotting default manufacturing your trend?",
    "Is the eye pulled toward a pattern the data won't support?",
    "What does this chart hide that a different one would show?",
    "Ten weeks interrogating other people's charts. These ten minutes are for yours. Fix one thing."]),
  ("No single right way",
   ["Three published essays, same goal, three defensible sets of choices: a Pudding piece, an Observable notebook, a Quarto site.",
    "A structure that works: hook, corpus note, finding, how-it-could-be-wrong, appendix.",
    "Write the headline finding in one sentence before you write anything else. If you can't, the essay isn't ready."]),
  ("Publish",
   ["Mullen's test, the course standard: \"I must be able to run it.\" The notebook works for someone who is not you.",
    "Every student leaves this session with a deployed URL.",
    "The essay shows the thinking. The notebook proves it happened."])],
10:[("The walkthrough, AI closed",
   ["Present the essay, then walk the room through your notebook, aloud, cell by cell.",
    "The oral walkthrough is the one deliverable an AI cannot produce for you.",
    "Expect three questions: what did you choose, what would you distrust, what would you do next?"]),
  ("The closing triptych",
   ["Edmond de Belamy, the AI portrait that sold for $432,500: who is the author?",
    "Anna Ridler's Mosaic Virus: she photographed 10,000 tulips herself to build the training set: whose labor is the data?",
    "Anadol's Unsupervised at MoMA: the museum's own collection becomes the art: who decided what went in?",
    "Week 1 began with loading a museum's catalog. The course ends watching a catalog become the art."]),
  ("What you can do now",
   ["Read a block of analysis code and say what it does, line by line.",
    "Ask a tractable question of cultural data and name what it leaves out.",
    "Run counting, classification, embeddings, and annotation, and say what each reveals and hides.",
    "Shuffle-test a gap. Interrogate a chart, including your own.",
    "The portfolio proves it: notebook, Data Biography, essay, walkthrough."])],
}

# Weekly data, curated from lesson-plans.md ---------------------------------
WEEKS = [
 dict(n=1, title="Your First Investigation", tool="Counting: rows, words, pixels",
   promise="By the mid-session break you will have loaded a real dataset, asked a question of it, and produced a chart. By the end you will have counted culture in three forms: rows, words, and pixels.",
   admire="The Pudding, \"She Giggles, He Gallops\" (2017): across ~2,000 film screenplays, the stage-direction verbs split by gender, women snuggle and giggle, men gallop and stride. The interactive presentation makes the pattern unmistakable.",
   interrogate="The 2,000 screenplays skew toward what was produced and digitized: is that \"film,\" or a sample of it? Whose choice is a gendered verb: the writer's, the character's, or the genre's? Counting shows the split, not the cause. The visualization's own choices deserve the same scrutiny as the data.",
   flow=[("0:00","Introductions and working agreements, demonstrated in practice. Today's live coding deliberately includes real mistakes."),
         ("0:10","Lecture, the stakes: machines already read culture at scale, the feed ranking what you see, the moderation filter, the model trained on scraped art and prose, and that reading happens without you. Counting culture has produced real knowledge (the screenplay verb split, the Rowling unmasking, pop music's 1991 revolution) and real mistakes, and both look identical until someone checks. In ten weeks you do the reading yourself and publish something checkable."),
         ("0:28","Look at This, then Question It: She Giggles, He Gallops."),
         ("0:35","The vocabulary and the map (no code): corpus, method, model, embedding, in plain language with pictures. The deliverable, shown: a web essay on a runnable notebook."),
         ("0:47","Lab 1 (worked, participatory): copy the notebook to Drive and mount Drive into the runtime (this is how your corpus and results survive Colab wiping the session, everything saving to one project folder), put a Gemini key in Colab Secrets, load NYT wedding data, make a first chart. Hand out the common-errors cheat sheet. Then solo with a partner: draft three questions, pick one, have the AI write the code, run it, chart it. Write one sentence predicting your cell before you run it."),
         ("1:20","Break"),
         ("1:30","Lab 2 (worked): count words, then pixels. First the top words of a small lyrics sample (stop-words dominate the list until you remove them, the first counting decision), then an image corpus: ~200 Met thumbnails ranked darkest to brightest by average brightness. Text and images, counted with the same technique; image projects begin here."),
         ("1:52","Preview of the methods ahead; the weekly routines introduced. First check-out.")],
   reading="The Bollen/Schmidt exchange, abstract and figure only: the Google Books \"hockey stick\" of cognitive distortions, then the critique that it may be an artifact of which books Google scanned. The trial runs next week.",
   sketch="One question from your life answerable with text or image data; three sentences.",
   check="Trace it: one written sentence predicting what your cell does before you run it. (Competency 1.)",
   comps="1, 8"),
 dict(n=2, title="Counting Is Already a Model", tool="Advanced counting: baselines, keyness, and the shuffle test",
   promise="Put a famous PNAS paper on trial, find the words that make a voice distinctive (the method behind Week 1's featured study), and learn the one statistical method the course requires: the shuffle test, which checks whether a difference is real.",
   admire="The Bollen/Schmidt trial: a hockey stick of societal distress, found by counting.",
   interrogate="The rising words are fiction-words, and Google scanned more fiction after 2000. The rebuttal, and the method worth adopting: the authors removed the entire fiction corpus and re-ran it, and the pattern largely held. The answer to \"your corpus is biased\" is a test, not an argument.",
   flow=[("0:00","Warm-up retrieval."),
         ("0:05","The trial: claim, objection, re-run-without-fiction rebuttal, \"interpret with care.\" One named choice is the chart: the hockey-stick shape depends on its y-axis and smoothing."),
         ("0:25","A brief demonstration before the complications: the words one artist uses far more than everyone else, a signature vocabulary measured against a pop baseline."),
         ("0:30","Hand-built bag-of-words: two authors, highlighters, argue about merging run/running. Counting requires defining."),
         ("0:55","What counts as a word? Paste a sentence into two tokenizer playgrounds and watch it shatter differently. Models see tokens, not words."),
         ("1:05","Break"),
         ("1:15","tf-idf: the AI scales your hand count; stop-words dominate, which motivates \"common here, rare overall.\""),
         ("1:30","Keyness, the She Giggles, He Gallops move: a log-odds ratio between two corpora finds the words one voice uses far more than a baseline, exactly the method behind Week 1's featured piece. The corpus pair is a choice too: artist vs. pop, lyrics vs. subreddit vs. novel."),
         ("1:42","Is the difference real? The shuffle test: shuffle the labels and recount, one thousand times. If chance alone frequently produces a gap this large, the difference should not be trusted; if it almost never does, the finding stands. A difference can be real and still small."),
         ("1:50","Gemini-free check and check-out.")],
   reading="Stephen Wolfram, \"What Is ChatGPT Doing…\", opening sections only, where even text generation turns out to be built from counting.",
   sketch="Count something in a text you care about; one chart; one sentence naming a choice you made.",
   check="Explain it: why two tokenizers split a sentence differently, and what your stemming choice changed. (Competencies 3, 5.)",
   comps="3, 5, 8"),
 dict(n=3, title="Classification: Counting with Weights", tool="Classification. Train a reader and read what it learned",
   promise="Teach a machine a bias in ten minutes, build a classifier and read the weights it learned, and preview the full menu of methods before next week's commitment.",
   admire="Ted Underwood's genre prediction (Distant Horizons, 2019): a logistic regression, the exact tool of today's lab, trained to recognize detective fiction and science fiction across a century of novels.",
   interrogate="What counts as science fiction is a choice built into the training labels. And the model's most famous error, misreading Pynchon's The Crying of Lot 49, a detective-fiction spoof, shows genre boundaries are real but fuzzy. A classifier's mistakes teach as much as its successes; yours will too.",
   flow=[("0:00","Warm-up + Look at This: Underwood's genre prediction."),
         ("0:10","Teachable Machine, instructor demo: a two-class image model trained live, then the reveal that it learned from only orange cats and brown dogs. The room predicts what a black cat will do, then sees it."),
         ("0:22","Counting with weights, the lab: each word casts a weighted vote; a logistic regression adds them up. Train it on a pop corpus, then read the signed coefficients: the model's reasoning, laid out in full."),
         ("0:52","A short demonstration: the words that most predict \"breakup song\" or \"this reviewer hated it.\""),
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
   interrogate="Listen across the pitches for questions too vague to answer, corpora that don't exist as accessible data, methods chosen on instinct rather than fit, and the quiet scaling-down of ambition.",
   flow=[("0:00","Warm-up + Look at This: the process post."),
         ("0:08","Pitches, three-minute hard cap each: your corpus (existence proof shown), your two methods, what would count as a finding."),
         ("0:48","Break"),
         ("0:58","The data conversation: the licensing one-pager (CC0 museums and public-domain books go anywhere; academic-only sets analyze-don't-redistribute; lyrics and review text metadata-only; AO3 and other community-opposed archives a small attributed sample at most, never a shared dataset; live firehoses we discuss, don't scrape; pirated full-text books from shadow libraries like LibGen never, the line the field's $1.5B settlement was about), and the Data Biography introduced."),
         ("1:10","Getting the data, APIs and scraping, demoed live with the AI writing the code. API first (the Met or Art Institute, no key); scraping second, with the robots.txt / ToS / rate-limit / anti-republish check."),
         ("1:30","Collect-and-build lab: point the cookbook notebook at your corpus, reshape it, and save it to your Drive project folder so it's there next week (when the Week 1 Drive mount pays off), and fork the publishing template. Your project repository starts today."),
         ("1:55","Commit, with the pivot kit named as insurance. A null result honestly shown is a complete project. Check-out.")],
   reading="Heather Krause, \"Data Biographies: Getting to Know Your Data\" (We All Count).",
   sketch="Write the Data Biography (~400 words) for your corpus, and actually collect it with the cookbook notebook so you reach Week 5 with real data in hand.",
   check="Explain it: your question aloud, what it omits, and where your data actually comes from. (Competencies 2, 6.)",
   comps="2, 6"),
 dict(n=5, title="Embeddings: A Map of Meaning", tool="Embeddings, the heart of the course, the leap past counting",
   promise="Watch your own corpus, text or images, sort itself by meaning, see the finding counting could not give you, and learn that the same technique drives \"For You\" recommendation feeds.",
   admire="A debate, two readings of one discovery: embedding space contains directions.",
   interrogate="Kozlowski, Taddy & Evans (2019) find a rich\u2013poor axis in embedding space and read it as the cultural structure of social class, measurable across a century. Bolukbasi et al. (2016) find the same kind of direction, a gender axis pairing men with \"programmer\" and women with \"homemaker,\" and read it as prejudice to remove. Identical technique, opposite verdicts. The room decides: when is a dimension found in a corpus a discovery about culture, and when is it the corpus's own bias read back?",
   flow=[("0:00","Warm-up + Look at This, room names the choice first: the embeddings debate."),
         ("0:10","The beyond-counting moment: put Week 2 beside today. There you counted the words around an axis you care about; now embed them and watch them cluster. Run it on something the room enjoys, a beloved artist's songs sorted by mood and era, and groupings appear that counting couldn't see. Same question, two tools, the second visibly richer. Name the idea: an item becomes a vector, position learned from the company it keeps."),
         ("0:25","Embed your own corpus, text or images. Image projects embed their pictures and watch them group by untagged style. The embedding model is an open one from Hugging Face, the hub where open models live (the same place Week 8's period models come from). And here charts stop being neutral: switch PCA to t-SNE and the same data rearranges. A visualization is an argument with decisions baked in."),
         ("0:55","Break"),
         ("1:05","Project lab: extend your embeddings and look for unexpected clusters. A five-minute aside on recommenders: \"For You\" is this same map plus your history. One-on-ones begin at the side."),
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
         ("1:15","The hand-labeling set-piece (Gemini-free): label 30 items from your corpus by hand; the AI labels the same 30; study every disagreement. No one skips this."),
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
         ("0:35","Confidence, and when to trust it: ask the model not just what but how sure. Sort by confidence, trust the labels the model is sure of, and hand-check the unsure ones."),
         ("0:50","Break"),
         ("1:00","Accuracy check, then project workshop: run your prompt against a small hand-labeled gold set. Where does the AI disagree, and is it wrong or are you? Then build time on your corpus. Go further (optional, technically comfortable): instead of the closed API model, run an open model from Hugging Face, or fine-tune your own small classifier (ModernBERT) on the labels you just made, the third reader you own."),
         ("1:50","Gemini-free check and check-out.")],
   reading="One short piece on the training-data fight (the NYT v. OpenAI complaint summary, or a Books3 explainer), read against your own Week 4 licensing conversation.",
   sketch="Show one label the AI got confidently wrong and one it got exactly right; for each, say how you knew.",
   check="Explain it: what is your labeling prompt deciding on your behalf, and how would you check whether to trust a given label? (Competencies 2, 5.)",
   comps="2, 4, 5"),
 dict(n=8, title="Models as Time Capsules + Settle the Finding", tool="What a trained model is: a compression of its corpus",
   promise="Meet models that live entirely inside one historical period, learn what a famous model has secretly memorized, stress-test your own finding to see what survives, and leave with a prose draft.",
   admire="TimeCapsuleLLM, a small GPT trained from scratch on nothing but 1800s London publications, and \"Speak, Memory\" (Bamman's lab), which probes which books GPT-4 has effectively memorized.",
   interrogate="A period model speaks only for the period's published, surviving, digitized voices. And memorization isn't reading: models score higher on memorized books, so an LLM that seems to read your corpus may be partly reciting it, a validity problem, not just an ethics one.",
   flow=[("0:00","Warm-up + Look at This: TimeCapsuleLLM and \"Speak, Memory,\" screenshots ready. (These period models, and supplements like MonadGPT and MacBERTh, live on Hugging Face, where you can download and run open models, or fine-tune your own.)"),
         ("0:07","Stress-test the finding, one continuous arc on your own results: shuffle the labels and re-run; split the corpus in half; ask \"compared to what?\". Then compress whatever survived into one headline sentence."),
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
   promise="A 90-minute public event followed by a reception, with friends and family invited. A printed program lists every project's title and URL.",
   admire="The closing triptych, neural networks meet the art world: Edmond de Belamy (the market), Anna Ridler's Mosaic Virus (the labor), Refik Anadol's Unsupervised at MoMA (the museum).",
   interrogate="When a machine reads a culture's archive, what is it showing us, and who decided what went in? You started Week 1 loading a museum's data; you end watching a museum's data become the art.",
   flow=[("0:00","Welcome. This is a celebration, not a defense. The closing Look at This."),
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
<link rel="icon" href="{base}assets/favicon.svg">
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
FAVICON_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
               '<rect width="32" height="32" rx="6" fill="#7a3b2e"/>'
               '<rect x="7" y="17" width="5" height="8" rx="1" fill="#f0e9e2"/>'
               '<rect x="14" y="12" width="5" height="13" rx="1" fill="#b9852f"/>'
               '<rect x="21" y="7" width="5" height="18" rx="1" fill="#3f6f5f"/>'
               '</svg>')

def build_index():
    acts = {1: "Act 1 — The tools (Weeks 1–3)", 4: "Act 2 — The project (Weeks 4–7)", 8: "Act 3 — Publish (Weeks 8–10)"}
    outline_rows = "".join(
        (f'<tr class="act"><td colspan="2">{acts[w["n"]]}</td></tr>' if w["n"] in acts else "")
        + f'<tr><td class="time">Week {w["n"]}</td><td><a href="weeks/week-{w["n"]:02d}.html">{esc(w["title"])}</a> &mdash; {esc(w["tool"])}</td></tr>'
        for w in WEEKS)
    body = f"""
<section class="hero">
  <p class="eyebrow">A 10-week project-based course for curious adults</p>
  <h1>{esc(TITLE)}</h1>
  <p class="lede">{esc(TAGLINE)}</p>
  <p>Investigate cultural data at scale with an AI as your coding partner. You publish a web essay on a question only you would ask. No mathematics or programming background is required, and the course is free to take.</p>
  <p class="cta"><a class="button" href="syllabus.html">Read the syllabus</a> <a class="button" href="notebooks.html">Open the notebooks</a> <a class="button ghost" href="schedule.html">See the ten weeks</a></p>
</section>

<section>
  <h2>The four tools</h2>
  {ul([
    "<strong>Counting</strong>: the simplest tool; it has no notion of meaning.",
    "<strong>Classification</strong>: train a transparent reader and see what it learned.",
    "<strong>Embeddings</strong>: items become positions on a map of meaning. The heart of the course.",
    "<strong>AI annotation</strong>: a powerful model reads your whole corpus; you decide which labels to trust.",
  ])}
  <p>Images receive the same treatment: you count, classify, and embed pictures as well as text.</p>
</section>

<section>
  <h2>The ten weeks</h2>
  <table class="flow"><tbody>{outline_rows}</tbody></table>
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
  <p>Curious adults with mixed coding backgrounds, most with little or none. The AI writes the code; you supply the questions and the judgment.</p>
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
  <h2>How a session runs</h2>
  <p>Each core session balances three modes in roughly equal thirds: a short lecture and live-coded demo of the week's tool, hands-on workshop time on your own data, and a real discussion, interrogating a study, debating an interpretation, or critiquing each other's work in progress.</p>
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
  <p>Ten vetted pairs to start from; the full corpus library, organized by interest area with access notes for the post-API era, lives in <a href='https://github.com/lucianli123/culture-as-data-2026/blob/main/design/planning-doc.md'>the planning document</a>.</p>
  <p>Stuck for a corpus by Week 4? These are vetted and small enough to move fast. A star (⭐) means it opens straight in Colab with one line, the lowest-effort place to start if code feels new.</p>
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
        f"<tr><td>{esc(wk)}</td><td>{main}</td><td>{supp}</td><td>{deep}</td></tr>"
        for wk, main, supp, deep in READING_LIST
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
  <p>One required reading a week (under thirty minutes), one optional supplement, and a <em>deeper</em> option for those who want the full scholarship. Bring three questions to each: what did the authors decide, what is the load-bearing assumption, and where is the gap?</p>
  <table><thead><tr><th>Week</th><th>Required</th><th>Supplement</th><th>Deeper (optional)</th></tr></thead><tbody>{reading}</tbody></table>
</section>

<section>
  <h2>See the featured studies yourself</h2>
  <p>The work each week opens with. Linked, not embedded, so credit and context stay with the source.</p>
  {ul([
    "<a href='https://pudding.cool/2017/08/screen-direction/'>The Pudding, She Giggles, He Gallops</a> (Week 1)",
    "<a href='https://doi.org/10.22148/16.005'>Underwood, The Life Cycles of Genres</a> (Week 3)",
    "<a href='https://americaspublicbible.org/'>Mullen, America's Public Bible</a> (Week 3 reading, and the model for your final deliverable)",
    "<a href='https://selfiecity.net/'>Manovich, Selfiecity</a> (Week 6)",
    "<a href='https://www.moma.org/calendar/exhibitions/5535'>Anadol, Unsupervised at MoMA</a> (Week 10)",
  ])}
</section>

<section>
  <h2>Supplemental reading (deeper cuts, never required)</h2>
  {ul([
    "<a href='https://data-feminism.mitpress.mit.edu/'>D'Ignazio & Klein, Data Feminism</a> (open access)",
    "<a href='https://www.bitbybitbook.com/'>Salganik, Bit by Bit</a>, ethical social research (open access)",
    "<a href='https://excavating.ai/'>Crawford & Paglen, Excavating AI</a>",
    "<a href='https://dl.acm.org/doi/10.1145/3442188.3445922'>Bender et al., On the Dangers of Stochastic Parrots</a>",
    "<a href='https://github.com/bamman-group/gpt4-books'>Speak, Memory: code and data</a> for probing what a model memorized",
  ])}
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
  <h2>The through-lines</h2>
  <p>A few threads run through every week, and each session advances at least one:</p>
  {ul([
    "<strong>Beyond counting.</strong> Each tool reaches past the last; the signature move is re-asking a counting question by meaning.",
    "<strong>Every method and chart is a choice.</strong> We admire finished work and interrogate it, then turn the same eye on our own.",
    "<strong>The readers you can and can't see.</strong> The transparent classifier (Week 3), the powerful annotator (Week 7), and the model you fine-tune and own.",
    "<strong>Whose data, whose judgment.</strong> The Data Biography, the licensing line, and the scraped creative work the models learned from.",
    "<strong>The AI as an instrument, not an oracle.</strong> Known failure modes, and a stretch each session with the assistant closed.",
    "<strong>Images are co-equal culture.</strong> You count, classify, and embed pictures the same way as text.",
  ])}
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
        nbs = [n for n in NOTEBOOKS if n[1] == w["n"]]
        deck = (f"<a class='button ghost' href='{GH_REPO}/raw/main/slides/pptx/week-{w['n']:02d}.pptx'>Slides (.pptx)</a> "
                f"<a class='button ghost' href='{GH_REPO}/blob/main/slides/week-{w['n']:02d}.md'>Slide outline</a>")
        if nbs:
            path, _, name, _ = nbs[0]
            variants = "".join(f" &nbsp;<a href='{COLAB}{vp}'>{vl} version</a>" for vl, vp in NOTEBOOK_VARIANTS.get(w["n"], []))
            nb_block = ("<section class='callout notebook-callout'><h2>This week's materials</h2>"
                        f"<p class='cta'>{nb_buttons(path)} {deck}</p>"
                        + (f"<p class='meta'>Completion-problem versions:{variants}</p>" if variants else "")
                        + "</section>")
        else:
            extra = (" Week 6 deepens the project with the <a href='../notebooks.html'>Week 5 embeddings notebook</a>; "
                     "its image path (CLIP) is this week's tool. The hand-labeling exercise is deliberately code-free.") if w["n"] == 6 else ""
            nb_block = ("<section class='callout notebook-callout'><h2>This week's materials</h2>"
                        f"<p class='cta'>{deck}</p><p class='meta'>No new notebook this week.{extra}</p></section>")
        prev_link = f'<a href="week-{w["n"]-1:02d}.html">&larr; Week {w["n"]-1}</a>' if i > 0 else "<span></span>"
        next_link = f'<a href="week-{w["n"]+1:02d}.html">Week {w["n"]+1} &rarr;</a>' if i < len(WEEKS)-1 else "<span></span>"
        body = f"""
<p class="crumb"><a href="../schedule.html">&larr; All ten weeks</a></p>
<article>
  <p class="eyebrow">Week {w['n']}</p>
  <h1>{esc(w['title'])}</h1>
  <p class="lede">{esc(w['promise'])}</p>
  <p class="meta"><strong>Tool / method:</strong> {esc(w['tool'])} &nbsp;·&nbsp; <strong>Competencies:</strong> {esc(w['comps'])}</p>
{nb_block}

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
tr.act td{padding-top:1.1rem;font-weight:700;color:var(--accent);border-bottom:none;font-size:.95rem}
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
.figure{width:100%;height:auto;display:block;margin:1.2rem 0}
/* footer */
.site-foot{border-top:1px solid var(--line);margin-top:3rem;color:var(--muted);font-size:.88rem}
.site-foot .wrap{padding-top:1.2rem;padding-bottom:2rem}
@media (max-width:560px){html{font-size:17px}h1{font-size:1.8rem}.lede{font-size:1.1rem}}
"""

def build_assets():
    write(SITE / "assets" / "style.css", CSS)
    write(SITE / "assets" / "favicon.svg", FAVICON_SVG)
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


def build_notebooks():
    rows = "".join(
        f"<tr><td class='time'>Week {wk}</td><td><strong>{esc(name)}</strong><br>{esc(desc)}<br>"
        + nb_buttons(path)
        + "".join(f" &nbsp;<a href='{COLAB}{vp}'>{vl}</a>" for vl, vp in NOTEBOOK_VARIANTS.get(wk, []))
        + "</td></tr>"
        for path, wk, name, desc in NOTEBOOKS)
    deck_rows = "".join(
        f"<tr><td class='time'>Week {w['n']}</td><td>{esc(w['title'])} &nbsp; "
        f"<a href='{GH_REPO}/raw/main/slides/pptx/week-{w['n']:02d}.pptx'>Download .pptx</a> &nbsp; "
        f"<a href='{GH_REPO}/blob/main/slides/week-{w['n']:02d}.md'>Outline</a></td></tr>"
        for w in WEEKS)
    social = "".join(
        f"<li><strong>{esc(name)}</strong>, {esc(desc)} <a href='{COLAB}{path}'>Open in Colab</a></li>"
        for path, name, desc in SOCIAL_STARTERS)
    cool = "".join(
        f"<li><strong>{esc(name)}</strong>, {esc(desc)} <a href='{COLAB}{path}'>Open in Colab</a></li>"
        for path, name, desc in COOL_METHODS)
    body = f"""
<article>
  <h1>Notebooks &amp; slides</h1>
  <p class="lede">The labs the course teaches from. Every one runs on Colab's free tier, costs $0, and works without any API key.</p>
  <p class="cta"><a class="button" href="{COLAB}notebooks/_smoke_test.ipynb">Run the smoke test first</a> <a class="button ghost" href="{GH_REPO}/tree/main/notebooks">All notebooks on GitHub</a></p>

  <section>
    <h2>Before your first session</h2>
    {ul([
      "Open the smoke test above and run it top to bottom: a green report means your runtime is healthy.",
      f"Never coded at all? An optional twenty-minute <a href='{COLAB}notebooks/python_warmup.ipynb'>Python warm-up</a> covers names, lists, and a first table, predict-then-run. The course never quizzes syntax; this is only for those who want it.",
      "Each notebook's first cells mount your Google Drive (so work survives a Colab reset) and install the few pinned packages Colab doesn't ship.",
      "Week 7 wants a free Gemini API key in Colab Secrets; without one it runs end-to-end on a recorded response.",
      "Weeks 5 and 7 also come in GUIDED (fuller scaffolding) and SKELETON (more blanks) versions; choose the one that matches your experience.",
    ])}
  </section>

  <section>
    <h2>The weekly labs</h2>
    <table class="flow"><thead><tr><th>Week</th><th>Notebook</th></tr></thead><tbody>{rows}</tbody></table>
  </section>

  <section>
    <h2>Optional method starters</h2>
    <ul>{cool}</ul>
  </section>

  <section>
    <h2>Getting social-media and fiction data</h2>
    <p>Ready-made loaders for the post-API era, used from Week 4 on. Each runs offline on a built-in sample; live pulls are opt-in.</p>
    <ul>{social}</ul>
  </section>

  <section>
    <h2>Handouts and the publishing template</h2>
    {ul([
      f"<a href='{GH_REPO}/blob/main/kits/common-errors-cheatsheet.md'>Common-errors cheat sheet</a>: what to do when a cell fails, handed out in Week 1.",
      f"<a href='{GH_REPO}/blob/main/kits/reading-a-code-cell.md'>How to read a code cell</a>: the five patterns behind nearly every cell in the course, handed out beside it.",
      f"<a href='{GH_REPO}/blob/main/kits/licensing-one-pager.md'>Licensing one-pager</a>: which route to a corpus is allowed, used in Week 4's data conversation.",
      f"<a href='{GH_REPO}/blob/main/kits/pivot-kit-corpora.md'>Pivot kit</a>: pre-tested fallback corpus-and-question pairs, insurance for stalled projects.",
      f"<a href='{GH_REPO}/blob/main/kits/critical-response-process.md'>Critical Response Process one-pager</a>: the Week 9 critique protocol, meaning before questions, questions before opinions.",
      f"<a href='{GH_REPO}/blob/main/kits/competency-checks.md'>Competency-check bank</a>: the weekly trace/fix/explain items for the AI-closed block.",
      f"<a href='{GH_REPO}/tree/main/template'>Project template</a>: the Quarto essay skeleton, the Data Biography template with a worked example, and the workbench portfolio structure, forked in Week 4.",
    ])}
  </section>

  <section>
    <h2>The slide decks</h2>
    <p>One deck per week, matching the weekly pages: the featured study, the key points, the session plan, and the homework. The .pptx opens in PowerPoint, Keynote, or Google Slides; the outline is plain Markdown.</p>
    <table class="flow"><thead><tr><th>Week</th><th>Deck</th></tr></thead><tbody>{deck_rows}</tbody></table>
  </section>
</article>
"""
    write(SITE / "notebooks.html", page("Notebooks", body, depth=0, active="notebooks.html"))


def main():
    build_assets()
    build_index()
    build_syllabus()
    build_schedule()
    build_notebooks()
    build_resources()
    build_about()
    build_weeks()
    print("Site built, docs/ ready for GitHub Pages.")


if __name__ == "__main__":
    main()
