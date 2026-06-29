#!/usr/bin/env python3
"""Export per-week slide content to slides/slides.json from the site data (build_site.py)."""
import sys, re, json, os
HERE=os.path.dirname(os.path.abspath(__file__)); REPO=os.path.dirname(HERE)
sys.path.insert(0, os.path.join(REPO,"tools")); import build_site as B

def plain(h):
    t=re.sub(r"<a href='([^']+)'>(.*?)</a>", r"\2", h); return re.sub(r"<[^>]+>","",t)

SKETCH={1:"One question from your life answerable with text or image data; three sentences.",
2:"Count something in a text you love; one chart; one sentence naming a choice you made.",
3:"Train a quick logistic regression on a labeled set; screenshot its five most positive and negative words.",
4:"Write your Data Biography (~400 words) and actually collect your corpus with the cookbook.",
5:"Toggle PCA vs. t-SNE and screenshot how the map changes; name one cluster you believe and one you don't.",
6:"One disagreement between your labels and the AI's where you were right, and why.",
7:"Show one label the AI got confidently wrong and one it nailed; say how you knew.",
8:"Expand to 600 to 1,000 words; write your show-your-work appendix and which checks survived.",
9:"Title your essay; write the headline finding in one sentence.",
10:"Within a week after: a private one-page reflection."}

THREADS={
1:[("Read work critically","Pockets is great and its choices are arguable. We admire and interrogate at once, the habit the whole course turns on."),
   ("Make something real","A complete investigation by the first break, before any theory."),
   ("Beyond counting (preview)","You load and chart real culture today; the ladder past counting starts next week.")],
2:[("Beyond counting","Counting is the honest floor, with no notion of meaning. This sets up the Week 5 payoff."),
   ("Every count is a choice","Tokens, stemming, the corpus, the chart's axis, each hides a decision you made."),
   ("Images are culture too","Count a painting's color and brightness, the same skill as words.")],
3:[("The reader you can see","The transparent classifier: read its signed weights, its mind on the table. Week 7 brings the opaque one."),
   ("You taught it the bias","The Teachable Machine reveal, a training set teaches a machine its prejudice."),
   ("Every choice is a choice","What counts as a label, and which words you hand it, decide what it learns.")],
4:[("Whose data","The Data Biography: where it came from, who is missing, what it cannot say."),
   ("The licensing line","CC0, to scrape-with-care, to never (LibGen). Judgment, not a rulebook."),
   ("Make something real","You leave with a real corpus in hand and a project repo born.")],
5:[("Beyond counting (the payoff)","The same she/he question from Week 2, now embedded, clusters counting could not see."),
   ("Every chart is a choice","PCA vs t-SNE rearranges the same data; the picture made a decision."),
   ("Whose data","Embeddings mirror the corpus, discovery (Soni/Klein) or laundered bias (Caliskan)?")],
6:[("Images are culture too","Their deepest day: pictures cluster by a visual style nobody tagged."),
   ("Where the AI fails on your data","Hand-label 30 the AI also labels; study every disagreement."),
   ("The two readers (calibration)","This hand-check is the bridge between the cheap reader and the powerful one.")],
7:[("The reader you can't see","The powerful, opaque annotator: trust the labels it is sure of, check the rest."),
   ("Whose judgment are you renting","Its reading was learned from creative work scraped largely without permission."),
   ("The third reader (go further)","Fine-tune a model you own, transparent, powerful, now yours.")],
8:[("Whose data, at full scale","A model is its corpus: bound the corpus and you bound the mind."),
   ("Memorization isn't reading","A model may recite your corpus rather than read it, a validity problem, not just ethics."),
   ("Kill it, then keep it","The Week 2 trial move, now turned on your own finding.")],
9:[("Interrogate your own chart","Ten weeks on other people's charts; now the ten minutes on yours."),
   ("No single right way","Three published essays, three defensible sets of choices."),
   ("Make something real","You leave with a deployed URL.")],
10:[("Whose data, whose authorship","The art triptych, de Belamy to Ridler to Anadol: who decided what went in?"),
   ("Understand, not commission","The oral walkthrough an AI cannot do for you."),
   ("All threads converge","You started loading a museum's data; you end watching it become the art.")],
}

reading={wk:(m,s) for wk,m,s in B.READING_LIST}
out=[]
for w in B.WEEKS:
    n=w["n"]; m,s=reading.get(str(n),("None","None"))
    out.append(dict(n=n,title=w["title"],promise=w["promise"],tool=w["tool"],comps=w["comps"],
        admire=w["admire"],interrogate=w["interrogate"],flow=[{"t":t,"a":a} for t,a in w["flow"]],
        reading=plain(m),supplement=plain(s),sketch=SKETCH[n],check=w["check"],
        threads=[{"name":nm,"note":nt} for nm,nt in THREADS[n]]))
json.dump(out, open(os.path.join(HERE,"slides.json"),"w"), indent=1)
print("wrote slides/slides.json")
