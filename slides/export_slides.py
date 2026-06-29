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
reading={wk:(m,s) for wk,m,s in B.READING_LIST}
out=[]
for w in B.WEEKS:
    n=w["n"]; m,s=reading.get(str(n),("None","None"))
    out.append(dict(n=n,title=w["title"],promise=w["promise"],tool=w["tool"],comps=w["comps"],
        admire=w["admire"],interrogate=w["interrogate"],flow=[{"t":t,"a":a} for t,a in w["flow"]],
        reading=plain(m),supplement=plain(s),sketch=SKETCH[n],check=w["check"]))
json.dump(out, open(os.path.join(HERE,"slides.json"),"w"), indent=1)
print("wrote slides/slides.json")
