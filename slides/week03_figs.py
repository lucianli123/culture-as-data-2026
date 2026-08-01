#!/usr/bin/env python3
"""Figures for the Week 3 lecture draft deck (logistic regression + classification).

Every figure comes from a model fitted here, on the same corpus the group-work
notebook loads: two subreddits pulled live from the Arctic Shift archive, falling
back to sentences from two novels when the archive is unreachable. Nothing is drawn
by hand, so the numbers on the slides are the numbers the code produced.

Writes PNGs plus week03_figs.json (the numbers the deck prints as text) into
$FIG_DIR, default /tmp/figs.

    python3 slides/week03_figs.py      # then: node slides/week03_deck_build.js

Colors are the course palette, stepped up in chroma so the categorical pairs clear
the CVD-separation and chroma floors (validated: normal ΔE 25.4, protan 20.0).
"""
import json, os, re, sys

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from sklearn.decomposition import TruncatedSVD
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split

FIG_DIR = os.environ.get("FIG_DIR", "/tmp/figs")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(FIG_DIR, exist_ok=True)

WARM, COOL = "#A34526", "#1F5FA8"     # the two piles; validated as a categorical pair
MUTED, GRID, INK = "#9A9A90", "#E5E1DA", "#1A1A1A"
SEQ = LinearSegmentedColormap.from_list("terra", ["#FBF6F2", WARM])

plt.rcParams.update({
    "figure.dpi": 200, "savefig.dpi": 200, "savefig.bbox": "tight",
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.edgecolor": GRID, "axes.labelcolor": INK, "text.color": INK,
    "xtick.color": MUTED, "ytick.color": MUTED, "axes.titlecolor": INK,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
})

PAIR = ("sandiego", "bayarea")
N_PER_SIDE = 400


def tidy(ax, xlabel="", ylabel="", title=""):
    ax.set_xlabel(xlabel, color=MUTED, fontsize=10)
    ax.set_ylabel(ylabel, color=MUTED, fontsize=10)
    if title:
        ax.set_title(title, fontsize=12, pad=10, loc="left")
    ax.tick_params(length=0)
    return ax


# --------------------------------------------------------------- the corpus
ARCHIVE = os.environ.get("ARCHIVE_URL",
                        "https://arctic-shift.photon-reddit.com/api/comments/search")
MIN_PER_SIDE = 60


def fetch_comments(sub, n=N_PER_SIDE, max_pages=12, tries=4):
    """One subreddit, analyze-only. Returns (texts, note); keeps partial results
    across retries. Same loader as the group-work notebook, so the deck's numbers
    come from the same pull the room will make."""
    import random, time
    import requests
    got, before, pages, attempt, dead = [], None, 0, 0, 0
    time.sleep(random.uniform(0, 2.0))
    while len(got) < n and pages < max_pages and attempt < tries:
        params = {"subreddit": sub, "limit": 100, "fields": "body,created_utc"}
        if before:
            params["before"] = before
        try:
            resp = requests.get(ARCHIVE, params=params, timeout=30)
        except Exception as e:
            attempt += 1
            dead += 1
            if dead >= 2:
                return got, "unreachable"
            print(f"  r/{sub}: {type(e).__name__}, retry {attempt}/{tries}", file=sys.stderr)
            time.sleep(min(8, 2 ** attempt) + random.uniform(0, 1))
            continue
        dead = 0
        if resp.status_code == 200:
            rows = resp.json().get("data") or []
            pages += 1
            if not rows:
                return got, ("empty" if not got else "ok")
            before = int(min(r["created_utc"] for r in rows))
            got += [r["body"] for r in rows if isinstance(r.get("body"), str)
                    and 80 < len(r["body"]) < 800
                    and "[removed]" not in r["body"] and "[deleted]" not in r["body"]
                    and "moderator" not in r["body"].lower()
                    and "has been removed" not in r["body"].lower()]
            continue
        if resp.status_code == 400:
            return got, f"rejected: {resp.text[:80]}"
        attempt += 1
        wait = float(resp.headers.get("Retry-After") or min(8, 2 ** attempt))
        print(f"  r/{sub}: HTTP {resp.status_code}, waiting {wait:.0f}s "
              f"(retry {attempt}/{tries})", file=sys.stderr)
        time.sleep(wait + random.uniform(0, 1))
    return got, ("ok" if got else "failed")


def load_reddit(a, b, n=N_PER_SIDE):
    piles = {}
    for sub in (a, b):
        rows, note = fetch_comments(sub, n)
        print(f"  r/{sub}: {len(rows)} comments ({note})", file=sys.stderr)
        if note == "unreachable":
            raise ConnectionError("archive unreachable")
        if len(rows) < MIN_PER_SIDE:
            raise ValueError(f"r/{sub} returned {len(rows)} comments ({note})")
        piles[sub] = rows
    return pd.DataFrame({"text": piles[a] + piles[b],
                         "label": [a] * len(piles[a]) + [b] * len(piles[b])})


def load_novelists(n=N_PER_SIDE):
    def sents(text):
        return [s.strip().replace("\n", " ") for s in re.split(r"(?<=[.!?])\s+", text)
                if 40 < len(s) < 180][:n]
    def read_one(fname):
        return open(os.path.join(REPO, "notebooks", "data", "texts", fname),
                    encoding="utf-8", errors="ignore").read()
    a, b = sents(read_one("frankenstein.txt")), sents(read_one("dracula.txt"))
    return pd.DataFrame({"text": a + b, "label": ["shelley"] * len(a) + ["stoker"] * len(b)})


def load_pair():
    try:
        df = load_reddit(*PAIR)
        return df, PAIR[0], PAIR[1], "live Reddit comments (Arctic Shift archive)"
    except Exception as e:
        print("archive unavailable:", type(e).__name__, "- using the novelists", file=sys.stderr)
        return load_novelists(), "shelley", "stoker", "sentences from two novels"


df, LABEL_A, LABEL_B, SOURCE = load_pair()
print(f"corpus: {LABEL_A} vs {LABEL_B} ({SOURCE}), {len(df)} rows")

vec = CountVectorizer(min_df=2)
X = vec.fit_transform(df["text"])
y = (df["label"] == LABEL_A).astype(int).values
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)

clf = LogisticRegression(max_iter=2000).fit(Xtr, ytr)
clf_full = LogisticRegression(max_iter=2000).fit(X, y)
acc = clf.score(Xte, yte)
dummy = DummyClassifier(strategy="most_frequent").fit(Xtr, ytr)
base_acc = dummy.score(Xte, yte)
# Shuffle the folds: the rows arrive newest-first per pile, so contiguous folds
# would be comparing different weeks rather than different samples.
cv = cross_val_score(LogisticRegression(max_iter=2000), X, y,
                     cv=StratifiedKFold(5, shuffle=True, random_state=0))

facts = {
    "label_a": LABEL_A, "label_b": LABEL_B, "source": SOURCE,
    "n_rows": int(len(df)), "n_a": int((df["label"] == LABEL_A).sum()),
    "n_b": int((df["label"] == LABEL_B).sum()), "n_features": int(X.shape[1]),
    "accuracy": round(float(acc), 3), "baseline": round(float(base_acc), 3),
    "cv_mean": round(float(cv.mean()), 3), "cv_std": round(float(cv.std()), 3),
}

# --------------------------------------------------------- 1. the sigmoid
score = np.linspace(-6, 6, 400)
prob = 1 / (1 + np.exp(-score))
fig, ax = plt.subplots(figsize=(6.2, 4.3))
ax.plot(score, prob, color=WARM, lw=2.2)
ax.axhline(0.5, color=MUTED, lw=1.2, ls=(0, (4, 4)))
ax.axvline(0, color=GRID, lw=1.2)
ax.text(-5.7, 0.88, f"above the line,\nthe model says {LABEL_A}", color=WARM, fontsize=10.5,
        ha="left", va="top", linespacing=1.4)
ax.text(5.8, 0.10, f"below the line,\nit says {LABEL_B}", color=COOL, fontsize=10.5,
        ha="right", va="top", linespacing=1.4)
ax.annotate("threshold 0.5\n(yours to move)", xy=(0.15, 0.5), xytext=(-5.7, 0.28),
            color=MUTED, fontsize=9.5,
            arrowprops=dict(arrowstyle="->", color=MUTED, lw=1))
ax.set_ylim(-0.05, 1.08)
tidy(ax, "sum of the weights of the words in the document", "probability of " + LABEL_A)
fig.savefig(os.path.join(FIG_DIR, "w3_sigmoid.png"))
plt.close(fig)

# ------------------------------------------------- 2. the boundary, in 2D
svd = TruncatedSVD(n_components=2, random_state=0).fit(X)
P = svd.transform(X)
flat = LogisticRegression(max_iter=2000).fit(P, y)
xx, yy = np.meshgrid(np.linspace(P[:, 0].min(), P[:, 0].max(), 300),
                     np.linspace(P[:, 1].min(), P[:, 1].max(), 300))
zz = flat.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1].reshape(xx.shape)
fig, ax = plt.subplots(figsize=(6.2, 4.3))
ax.contour(xx, yy, zz, levels=[0.5], colors=[MUTED], linewidths=1.6, linestyles="dashed")
ax.scatter(P[y == 1, 0], P[y == 1, 1], s=13, color=WARM, alpha=0.75,
           edgecolors="white", linewidths=0.4, label=LABEL_A)
ax.scatter(P[y == 0, 0], P[y == 0, 1], s=13, color=COOL, alpha=0.75,
           edgecolors="white", linewidths=0.4, label=LABEL_B)
ax.legend(frameon=False, loc="upper right", fontsize=10, labelcolor=INK)
ax.set_xticklabels([]); ax.set_yticklabels([])
ax.text(0.5, -0.16, f"the best straight line in this 2-D view gets {flat.score(P, y):.0%} right; "
        f"with all {X.shape[1]:,} columns the model gets {acc:.0%}",
        transform=ax.transAxes, ha="center", fontsize=9.5, color=MUTED)
tidy(ax, f"the same {X.shape[1]:,} word-columns, squashed down to two", "")
fig.savefig(os.path.join(FIG_DIR, "w3_boundary.png"))
plt.close(fig)
facts["boundary_accuracy_2d"] = round(float(flat.score(P, y)), 3)

# ------------------------------------------------------ 3. signed weights
words = np.array(vec.get_feature_names_out())
w = clf_full.coef_.ravel()
order = w.argsort()
k = 8
idx = np.concatenate([order[:k], order[-k:]])
fig, ax = plt.subplots(figsize=(6.2, 4.6))
colors = [COOL if w[i] < 0 else WARM for i in idx]
ax.barh(range(len(idx)), w[idx], color=colors, height=0.72)
ax.set_yticks(range(len(idx)))
ax.set_yticklabels(words[idx], fontsize=10.5)
ax.axvline(0, color=MUTED, lw=1)
ax.text(0.02, 0.965, f"→ {LABEL_A}", transform=ax.transAxes, color=WARM, fontsize=11, ha="left")
ax.text(0.98, 0.03, f"← {LABEL_B}", transform=ax.transAxes, color=COOL, fontsize=11, ha="right")
ax.grid(axis="y", visible=False)
tidy(ax, "weight (the size of the word's vote)", "")
fig.savefig(os.path.join(FIG_DIR, "w3_weights.png"))
plt.close(fig)
facts["top_a"] = [str(t) for t in words[order[-6:][::-1]]]
facts["top_b"] = [str(t) for t in words[order[:6]]]

# ------------------------------------------------- 4. baseline vs. model
fig, ax = plt.subplots(figsize=(6.2, 4.3))
ax.set_axisbelow(True)
bars = ax.bar([0, 1], [base_acc, acc], width=0.5, color=[MUTED, WARM])
ax.errorbar([1], [cv.mean()], yerr=[cv.std()], fmt="none", ecolor=INK, elinewidth=1.4, capsize=6)
for b, v in zip(bars, [base_acc, acc]):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.015, f"{v:.2f}",
            ha="center", fontsize=13, color=INK)
ax.text(1.0, 0.90, f"the same model on five different\nsplits: {cv.mean():.2f} ± {cv.std():.2f}",
        ha="center", va="top", fontsize=10, color=MUTED, linespacing=1.4)
ax.set_xticks([0, 1])
ax.set_xticklabels(["always guess\nthe bigger pile", "logistic\nregression"], fontsize=11)
ax.set_ylim(0, 1.0)
ax.grid(visible=False)
tidy(ax, "", "accuracy on rows the model never saw")
fig.savefig(os.path.join(FIG_DIR, "w3_baseline.png"))
plt.close(fig)

# ---------------------------------------------------- 5. the C dial (fit)
Cs = [0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100]
tr_acc, te_acc = [], []
for C in Cs:
    m = LogisticRegression(C=C, max_iter=3000).fit(Xtr, ytr)
    tr_acc.append(m.score(Xtr, ytr))
    te_acc.append(m.score(Xte, yte))
fig, ax = plt.subplots(figsize=(6.2, 4.3))
ax.plot(Cs, tr_acc, color=COOL, lw=2.2, marker="o", ms=4.5)
ax.plot(Cs, te_acc, color=WARM, lw=2.2, marker="o", ms=4.5)
ax.set_xscale("log")
ax.text(Cs[-1] * 1.15, tr_acc[-1], "on rows it\ntrained on", color=COOL, fontsize=10, va="center")
ax.text(Cs[-1] * 1.15, te_acc[-1], "on held-out\nrows", color=WARM, fontsize=10, va="center")
ax.axhline(base_acc, color=MUTED, lw=1.2, ls=(0, (4, 4)))
ax.text(Cs[0], base_acc + 0.012, "baseline", color=MUTED, fontsize=9.5)
ax.set_xlim(Cs[0] / 1.6, Cs[-1] * 4.2)
ax.set_ylim(min(base_acc, min(te_acc)) - 0.06, 1.04)
tidy(ax, "C  (low = kept simple · high = trusts the training data)", "accuracy")
fig.savefig(os.path.join(FIG_DIR, "w3_regularisation.png"))
plt.close(fig)
facts["c_low"] = {"C": Cs[0], "train": round(tr_acc[0], 3), "test": round(te_acc[0], 3)}
facts["c_high"] = {"C": Cs[-1], "train": round(tr_acc[-1], 3), "test": round(te_acc[-1], 3)}
facts["c_best"] = {"C": Cs[int(np.argmax(te_acc))], "test": round(max(te_acc), 3)}

# ------------------------------------------------------ 6. confusion matrix
cm = confusion_matrix(yte, clf.predict(Xte))          # rows: true (0=B, 1=A)
fig, ax = plt.subplots(figsize=(5.6, 4.3))
im = ax.imshow(cm, cmap=SEQ)
for i in range(2):
    for j in range(2):
        ax.text(j, i, cm[i, j], ha="center", va="center", fontsize=20,
                color="white" if cm[i, j] > cm.max() * 0.6 else INK)
ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
ax.set_xticklabels([f"said {LABEL_B}", f"said {LABEL_A}"], fontsize=11)
ax.set_yticklabels([f"really {LABEL_B}", f"really {LABEL_A}"], fontsize=11, rotation=90, va="center")
ax.grid(visible=False)
ax.tick_params(length=0)
ax.set_xlabel("the two cells off the diagonal are the mistakes", color=MUTED, fontsize=10)
fig.savefig(os.path.join(FIG_DIR, "w3_confusion.png"))
plt.close(fig)
facts["confusion"] = {"true_b_said_b": int(cm[0, 0]), "true_b_said_a": int(cm[0, 1]),
                      "true_a_said_b": int(cm[1, 0]), "true_a_said_a": int(cm[1, 1])}

# ------------------------------------------------------- 7. learning curve
sizes, curve, lo, hi = [], [], [], []
rng = np.random.default_rng(0)
for frac in (0.1, 0.2, 0.35, 0.5, 0.75, 1.0):
    n = int(Xtr.shape[0] * frac)
    runs = []
    for _ in range(5):                      # five draws per size: one run is luck
        take = rng.permutation(Xtr.shape[0])[:n]
        if len(set(ytr[take])) < 2:
            continue
        runs.append(LogisticRegression(max_iter=3000).fit(Xtr[take], ytr[take]).score(Xte, yte))
    if not runs:
        continue
    sizes.append(n); curve.append(float(np.mean(runs)))
    lo.append(min(runs)); hi.append(max(runs))
fig, ax = plt.subplots(figsize=(6.2, 4.3))
ax.fill_between(sizes, lo, hi, color=WARM, alpha=0.13, linewidth=0)
ax.plot(sizes, curve, color=WARM, lw=2.2, marker="o", ms=5)
ax.text(sizes[1], hi[1] + 0.012, "five draws at each size;\nthe band is best-to-worst",
        fontsize=9.5, color=MUTED, linespacing=1.4)
ax.axhline(base_acc, color=MUTED, lw=1.2, ls=(0, (4, 4)))
ax.text(sizes[-1], base_acc + 0.012, "baseline", color=MUTED, fontsize=9.5, ha="right")
ax.set_ylim(min(base_acc, min(lo)) - 0.05, max(hi) + 0.09)
tidy(ax, "training documents", "accuracy on held-out rows")
fig.savefig(os.path.join(FIG_DIR, "w3_learning.png"))
plt.close(fig)
facts["learning"] = [[int(s), round(float(c), 3)] for s, c in zip(sizes, curve)]

with open(os.path.join(FIG_DIR, "week03_figs.json"), "w") as f:
    json.dump(facts, f, indent=1)
print(json.dumps(facts, indent=1))
print("figures written to", FIG_DIR)
