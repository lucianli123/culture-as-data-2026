#!/usr/bin/env python3
"""Figures for the Week 4 lecture draft deck (neural networks, word embeddings, APIs).

Nothing here is a stock illustration. The models are really fitted, the word vectors are
trained on the two novels in notebooks/data/texts, the nearest neighbours are computed
from them, and the API panels call live endpoints.

    python3 slides/week04_figs.py      # then: node slides/week04_deck_build.js

Writes PNGs plus week04_figs.json into $FIG_DIR (default /tmp/figs). Same palette as
Week 3: the categorical pair passes the CVD-separation and chroma checks.
"""
import json, os, re, sys
from collections import Counter

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, FancyBboxPatch
from sklearn.decomposition import TruncatedSVD
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

FIG_DIR = os.environ.get("FIG_DIR", "/tmp/figs")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(FIG_DIR, exist_ok=True)

WARM, COOL, GOLD = "#A34526", "#1F5FA8", "#B9852F"
MUTED, GRID, INK, TINT = "#9A9A90", "#E5E1DA", "#1A1A1A", "#F4EEE8"

plt.rcParams.update({
    "figure.dpi": 300, "savefig.dpi": 300, "savefig.bbox": "tight",
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.edgecolor": GRID, "axes.labelcolor": INK, "text.color": INK,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
})
facts = {}


def blank(ax):
    ax.set_xticks([]); ax.set_yticks([]); ax.grid(False)
    for sp in ax.spines.values():
        sp.set_visible(False)
    return ax


def arrow(ax, xy1, xy2, color=MUTED, lw=1.4, alpha=1.0):
    ax.add_patch(FancyArrowPatch(xy1, xy2, arrowstyle="-|>", mutation_scale=11,
                                 color=color, lw=lw, alpha=alpha,
                                 shrinkA=2, shrinkB=2))


TEXTS = ("frankenstein.txt", "dracula.txt")


def read_text(fn):
    """The novel only: Project Gutenberg's licence wrapper is not Mary Shelley."""
    raw = open(os.path.join(REPO, "notebooks", "data", "texts", fn),
               encoding="utf-8", errors="ignore").read()
    start = raw.find("*** START OF")
    end = raw.find("*** END OF")
    body = raw[raw.find("\n", start) + 1:end] if start >= 0 and end > start else raw
    return body.lower()


def load_words():
    return re.findall(r"[a-z']{2,}", "\n".join(read_text(fn) for fn in TEXTS))


toks = load_words()


# ------------------------------------------------------------------ 1. a neuron
fig, ax = plt.subplots(figsize=(6.6, 4.0)); blank(ax)
ax.set_xlim(0, 10); ax.set_ylim(0, 6)
words = [("beach", 2, "+1.4"), ("rent", 1, "+0.9"), ("the", 3, "-0.2"), ("bart", 0, "-1.6")]
for i, (w, c, wt) in enumerate(words):
    y = 5.1 - i * 1.15
    ax.add_patch(FancyBboxPatch((0.2, y - 0.32), 2.5, 0.64, boxstyle="round,pad=0.06",
                                fc=TINT, ec="none"))
    ax.text(0.45, y, w, va="center", fontsize=12)
    ax.text(2.45, y, f"×{c}", va="center", ha="right", fontsize=12, color=MUTED)
    arrow(ax, (2.8, y), (5.3, 3.0), color=WARM if float(wt) > 0 else COOL,
          lw=1.1 + 1.6 * abs(float(wt)), alpha=0.75)
    ax.text(3.95, (y + 3.0) / 2 + 0.16, wt, fontsize=10.5, ha="center",
            color=WARM if float(wt) > 0 else COOL)
ax.add_patch(Circle((5.9, 3.0), 0.62, fc="white", ec=INK, lw=1.4))
ax.text(5.9, 3.0, "Σ", ha="center", va="center", fontsize=22)
arrow(ax, (6.6, 3.0), (7.5, 3.0))
xs = np.linspace(-6, 6, 120)
ax.plot(7.7 + xs * 0.13, 3.0 + (1 / (1 + np.exp(-xs)) - 0.5) * 1.5, color=WARM, lw=2)
arrow(ax, (9.0, 3.0), (9.7, 3.0))
ax.text(9.85, 3.0, "p", va="center", fontsize=15)
ax.text(0.2, 5.85, "counts", fontsize=11, color=MUTED)
ax.text(3.4, 5.85, "weights", fontsize=11, color=MUTED)
ax.text(5.35, 5.85, "add them up", fontsize=11, color=MUTED)
ax.text(7.6, 5.85, "squash", fontsize=11, color=MUTED)
ax.text(0.2, 0.35, "This is Week 3's classifier. It is also one neuron.", fontsize=13.5,
        style="italic")
fig.savefig(os.path.join(FIG_DIR, "w4_neuron.png")); plt.close(fig)

# ------------------------------------------------------- 2. a network, and its cost
# Two figures from one real fit: the same passages classified by Week 3's model and by
# a four-unit network. Both get it right; only one of them can be read afterwards.
from sklearn.feature_extraction.text import CountVectorizer


def novel_chunks(size=400):
    docs, labs = [], []
    for lab, fn in enumerate(TEXTS):
        ws = re.findall(r"[a-z']{2,}", read_text(fn))
        for i in range(0, len(ws) - size, size):
            docs.append(" ".join(ws[i:i + size])); labs.append(lab)
    return docs, labs


docs_, labs_ = novel_chunks()
vec_ = CountVectorizer(max_features=1500, min_df=5, stop_words="english")
Xd = vec_.fit_transform(docs_).toarray().astype(float)
Xd = 100 * Xd / (Xd.sum(1, keepdims=True) + 1e-9)      # words per hundred
names_ = np.array(vec_.get_feature_names_out())
from sklearn.model_selection import train_test_split
Xtr, Xte, ytr, yte = train_test_split(Xd, labs_, test_size=0.3, stratify=labs_,
                                      random_state=0)
lr_ = LogisticRegression(max_iter=2000).fit(Xtr, ytr)
net_ = MLPClassifier(hidden_layer_sizes=(4,), max_iter=900, random_state=0).fit(Xtr, ytr)
facts["novel_lr_acc"] = round(float(lr_.score(Xte, yte)), 3)
facts["novel_net_acc"] = round(float(net_.score(Xte, yte)), 3)
facts["novel_chunks"] = len(docs_)

fig, ax = plt.subplots(figsize=(6.8, 4.0)); blank(ax)
ax.set_xlim(0, 10); ax.set_ylim(0, 6.4)
inp_words = ["ice", "count", "blood", "sledge", "night"]
inp = [(1.7, y) for y in np.linspace(5.3, 1.9, len(inp_words))]
hid = [(5.0, y) for y in np.linspace(5.0, 2.2, 4)]
out = (8.4, 3.6)
for a in inp:
    for b in hid:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=GRID, lw=0.8, zorder=1)
for b in hid:
    ax.plot([b[0], out[0]], [b[1], out[1]], color=MUTED, lw=0.9, alpha=0.6, zorder=1)
for (x, y), w in zip(inp, inp_words):
    ax.add_patch(Circle((x, y), 0.22, fc="white", ec=MUTED, lw=1.2, zorder=2))
    ax.text(x - 0.38, y, w, ha="right", va="center", fontsize=11.5)
for (x, y) in hid:
    ax.add_patch(Circle((x, y), 0.28, fc=TINT, ec=GOLD, lw=1.6, zorder=2))
ax.add_patch(Circle(out, 0.32, fc="white", ec=WARM, lw=1.8, zorder=2))
ax.text(1.7, 6.0, "one per word", ha="center", fontsize=11, color=MUTED)
ax.text(5.0, 6.0, "four neurons in between", ha="center", fontsize=11, color=GOLD)
ax.text(8.4, 6.0, "which novel?", ha="center", fontsize=11, color=WARM)
ax.text(5.0, 0.7, "Every line is a weight. Each middle neuron adds up all the words in its\n"
                  "own way, and the output neuron adds up the four of them.",
        ha="center", va="center", fontsize=11.5, color=INK, linespacing=1.5)
fig.savefig(os.path.join(FIG_DIR, "w4_network.png")); plt.close(fig)

# 2b. what the extra layer costs: readable weights
fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.0),
                         gridspec_kw={"width_ratios": [1, 1.15], "wspace": 0.45})
coef = lr_.coef_[0]
top = np.r_[np.argsort(coef)[:6][::-1], np.argsort(-coef)[:6][::-1]]
axes[0].barh(range(len(top)), coef[top],
             color=[COOL if coef[i] < 0 else WARM for i in top])
axes[0].set_yticks(range(len(top))); axes[0].set_yticklabels(names_[top], fontsize=10.5)
axes[0].axvline(0, color=MUTED, lw=1)
axes[0].set_title(f"Week 3's model: {facts['novel_lr_acc']:.0%} on held-out passages",
                  fontsize=12.5, loc="left", pad=8)
axes[0].set_xlabel("one weight per word — and you can read them", color=MUTED, fontsize=10.5)
axes[0].grid(axis="y", visible=False)

W1 = net_.coefs_[0]
busiest = W1[np.argsort(-np.abs(W1).sum(1))[:60]].T
lim = np.percentile(np.abs(busiest), 97)
axes[1].imshow(busiest, cmap="RdBu_r", aspect="auto", vmin=-lim, vmax=lim)
axes[1].set_yticks(range(4)); axes[1].set_yticklabels([f"unit {i+1}" for i in range(4)],
                                                      fontsize=10.5)
axes[1].set_xticks([]); axes[1].grid(False); axes[1].tick_params(length=0)
axes[1].set_title(f"the network: {facts['novel_net_acc']:.0%} on the same passages",
                  fontsize=12.5, loc="left", pad=8)
axes[1].set_xlabel("the 60 busiest words × 4 units — and now nothing reads as an answer",
                   color=MUTED, fontsize=10.5)
fig.savefig(os.path.join(FIG_DIR, "w4_readability.png")); plt.close(fig)

# --------------------------------------------------------- 3. rolling downhill
fig, ax = plt.subplots(figsize=(6.2, 4.0))
w = np.linspace(-3, 3, 300)
loss = 0.6 * (w ** 2) + 0.35 * np.sin(3 * w) + 1.2
ax.plot(w, loss, color=MUTED, lw=2)
pos, steps = -2.6, []
for _ in range(7):
    grad = 1.2 * pos + 1.05 * np.cos(3 * pos)
    steps.append(pos)
    pos = pos - 0.28 * grad
ys = 0.6 * np.array(steps) ** 2 + 0.35 * np.sin(3 * np.array(steps)) + 1.2
ax.plot(steps, ys, "o", color=WARM, ms=8, zorder=3)
for i in range(len(steps) - 1):
    arrow(ax, (steps[i], ys[i]), (steps[i + 1], ys[i + 1]), color=WARM, lw=1.3)
ax.annotate("start anywhere", xy=(steps[0], ys[0]), xytext=(-2.9, 5.2), color=MUTED,
            fontsize=11, arrowprops=dict(arrowstyle="->", color=MUTED))
ax.annotate("each step: which way is down?\nnudge every weight that way",
            xy=(steps[3], ys[3]), xytext=(0.15, 4.6), color=INK, fontsize=11,
            linespacing=1.5, arrowprops=dict(arrowstyle="->", color=MUTED))
ax.set_xlabel("one weight (there are thousands of these)", color=MUTED, fontsize=10)
ax.set_ylabel("loss: how wrong the model is", color=MUTED, fontsize=10)
ax.set_xticks([]); ax.set_yticks([]); ax.tick_params(length=0)
fig.savefig(os.path.join(FIG_DIR, "w4_gradient.png")); plt.close(fig)

# ------------------ 4. two questions about meaning: one linear, one not
# Osgood's semantic differential found three dimensions behind how people rate words:
# evaluation, potency, activity. Warriner et al. re-measured them on 13,915 words, and
# the modern names are valence, dominance, arousal. Fetched at build time, not stored here.
def meaning_figure():
    import csv, io, requests
    url = "https://raw.githubusercontent.com/JULIELab/XANEW/master/Ratings_Warriner_et_al.csv"
    rows = list(csv.DictReader(io.StringIO(requests.get(url, timeout=60).text)))
    word = np.array([r["Word"] for r in rows])
    val = np.array([float(r["V.Mean.Sum"]) for r in rows])     # unpleasant 1 - pleasant 9
    aro = np.array([float(r["A.Mean.Sum"]) for r in rows])     # calm 1 - excited 9
    X = np.c_[val, aro]

    mid = np.median(val)
    pleasant = (val > mid).astype(int)
    swing = np.abs(val - mid)
    quiet, loud = np.percentile(swing, [35, 65])
    keep = (swing <= quiet) | (swing >= loud)
    Xc, charged = X[keep], (swing[keep] >= loud).astype(int)

    lin_a = LogisticRegression(max_iter=2000).fit(X, pleasant)
    lin_b = LogisticRegression(max_iter=2000).fit(Xc, charged)
    net_b = MLPClassifier((16, 16), max_iter=3000, random_state=0).fit(Xc, charged)

    rng_ = np.random.default_rng(0)
    show_a = rng_.choice(len(X), 2200, replace=False)
    show_b = rng_.choice(len(Xc), 2200, replace=False)
    xx, yy = np.meshgrid(np.linspace(1, 9, 300), np.linspace(1, 9, 300))
    grid = np.c_[xx.ravel(), yy.ravel()]

    fig, axes = plt.subplots(1, 3, figsize=(12.8, 4.2))
    panels = [(axes[0], X[show_a], pleasant[show_a], lin_a,
               "Is it pleasant?", f"one line: {lin_a.score(X, pleasant):.0%}"),
              (axes[1], Xc[show_b], charged[show_b], lin_b,
               "Is it emotionally charged, either way?", f"one line: {lin_b.score(Xc, charged):.0%}"),
              (axes[2], Xc[show_b], charged[show_b], net_b,
               "Is it emotionally charged, either way?", f"a network: {net_b.score(Xc, charged):.0%}")]
    for ax, pts, lab, model, title, score in panels:
        zz = model.predict(grid).reshape(xx.shape)
        ax.contourf(xx, yy, zz, levels=[-0.5, 0.5, 1.5], colors=[COOL, WARM], alpha=0.10)
        ax.contour(xx, yy, zz, levels=[0.5], colors=[MUTED], linewidths=1.6)
        ax.scatter(pts[lab == 1, 0], pts[lab == 1, 1], s=4, color=WARM, alpha=0.55, lw=0)
        ax.scatter(pts[lab == 0, 0], pts[lab == 0, 1], s=4, color=COOL, alpha=0.55, lw=0)
        ax.set_title(title, fontsize=11.5, loc="left", pad=8)
        ax.set_xlabel(score, color=MUTED, fontsize=11)
        ax.set_xlim(1, 9); ax.set_ylim(1, 9)
        ax.set_xticks([2, 5, 8]); ax.set_yticks([2, 5, 8])
        ax.grid(False)
    axes[0].set_ylabel("arousal: calm to excited", color=MUTED, fontsize=10)
    for ax in axes:
        ax.set_xticklabels(["unpleasant", "neutral", "pleasant"], fontsize=9.5)

    at = {w: i for i, w in enumerate(word)}
    for w, dx, dy in (("murder", 5, 4), ("torture", 5, -10), ("love", 6, 5),
                      ("joy", -6, -12), ("chair", 5, -10), ("habit", 5, 5)):
        if w in at:
            axes[1].annotate(w, (val[at[w]], aro[at[w]]), xytext=(dx, dy),
                             textcoords="offset points", fontsize=9.5, color=INK,
                             ha="right" if dx < 0 else "left")
    fig.savefig(os.path.join(FIG_DIR, "w4_meaning.png")); plt.close(fig)
    facts["meaning_words"] = len(word)
    facts["meaning_lin_pleasant"] = round(float(lin_a.score(X, pleasant)), 3)
    facts["meaning_lin_charged"] = round(float(lin_b.score(Xc, charged)), 3)
    facts["meaning_net_charged"] = round(float(net_b.score(Xc, charged)), 3)


try:
    meaning_figure()
except Exception as e:
    print("meaning figure skipped:", type(e).__name__, e, file=sys.stderr)


# ---------- 7 + 8. vectors trained on the two repo novels, the contrastive way
counts = Counter(toks)
vocab = [w for w, c in counts.most_common(4000)]
index = {w: i for i, w in enumerate(vocab)}
V = len(vocab)
facts["corpus_tokens"] = len(toks)
facts["corpus_vocab"] = V


def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -8, 8)))


def contrastive_vectors(dims=60, epochs=8, lr=0.03, neg=5, batch=2048, win=4, seed=0):
    """Skip-gram with negative sampling, which is contrastive learning: for every pair
    of words that really did occur near each other, pull those two vectors together;
    for a handful of randomly drawn words, push them apart. Nothing else."""
    rng = np.random.default_rng(seed)
    ids_ = np.array([index.get(w, -1) for w in toks])
    ids_ = ids_[ids_ >= 0]
    pairs = np.concatenate([np.stack([ids_[:-o], ids_[o:]], 1) for o in range(1, win + 1)])
    rng.shuffle(pairs)
    E = rng.normal(0, 0.1, (V, dims))
    before = E.copy()
    freq = np.bincount(ids_, minlength=V).astype(float) ** 0.75
    freq /= freq.sum()
    for _ in range(epochs):
        for s_ in range(0, len(pairs), batch):
            p = pairs[s_:s_ + batch]
            a, b = p[:, 0], p[:, 1]
            g = 1 - sigmoid((E[a] * E[b]).sum(1, keepdims=True))     # pull
            np.add.at(E, a, lr * g * E[b])
            np.add.at(E, b, lr * g * E[a])
            for nk in rng.choice(V, size=(len(p), neg), p=freq).T:   # push
                g = sigmoid((E[a] * E[nk]).sum(1, keepdims=True))
                np.add.at(E, a, -lr * g * E[nk])
                np.add.at(E, nk, -lr * g * E[a])
    return before, E, len(pairs)


before, after, n_pairs = contrastive_vectors()
after_n = after / (np.linalg.norm(after, axis=1, keepdims=True) + 1e-9)
facts["contrastive_pairs"] = n_pairs

# 7a. one step of that training, drawn — with words taken from the corpus itself
ANCHOR = "door"
STOP = set("the a an and of to in it is was that he she his her i you we they for on at "
           "as with but not be had have been so all my me him them this there which "
           "from by or if no do did are were what when who will would could".split())
near = Counter()
for i, t in enumerate(toks):
    if t == ANCHOR:
        for u in toks[max(0, i - 4):i + 5]:
            if u != ANCHOR and u not in STOP:
                near[u] += 1
positive = near.most_common(1)[0][0]
rng_fig = np.random.default_rng(3)
negatives = [w for w in rng_fig.choice(vocab[:1200], 12, replace=False)
             if w not in near and w != ANCHOR and w not in STOP][:3]
facts["contrastive_example"] = {"anchor": ANCHOR, "positive": positive,
                                "negatives": negatives}

fig, ax = plt.subplots(figsize=(7.4, 4.2)); blank(ax)
ax.set_xlim(0, 10); ax.set_ylim(0, 7)
A = np.array([5.0, 3.2])
ax.add_patch(Circle(A, 0.30, fc=WARM, ec="white", lw=1.5, zorder=3))
ax.text(A[0], A[1] - 0.75, ANCHOR, ha="center", fontsize=13, color=WARM, weight="bold")
P = np.array([7.5, 4.5])
ax.add_patch(Circle(P, 0.26, fc=GOLD, ec="white", lw=1.5, zorder=3))
ax.text(P[0], P[1] + 0.42, positive, ha="center", fontsize=12.5, color=GOLD)
arrow(ax, P - 0.3, A + 0.3, color=GOLD, lw=2.4)
ax.text(9.9, 5.85, f"really did appear beside “{ANCHOR}”  →  PULL TOGETHER",
        fontsize=11.5, color=GOLD, ha="right")
for (x, y), w in zip([(2.4, 5.0), (1.9, 3.1), (3.0, 1.5)], negatives):
    D = np.array([x, y])
    ax.add_patch(Circle(D, 0.24, fc=COOL, ec="white", lw=1.4, zorder=3))
    ax.text(x, y + 0.40, w, ha="center", fontsize=12, color=COOL)
    away = (D - A) / np.linalg.norm(D - A)
    arrow(ax, D + away * 0.32, D + away * 1.15, color=COOL, lw=2.0)
ax.text(0.1, 6.55, "three words drawn at random  →  PUSH APART", fontsize=11.5, color=COOL)
ax.text(0.1, 0.1, f"One step. Repeat it {n_pairs:,} times and the space arranges itself.",
        fontsize=12.5, style="italic")
fig.savefig(os.path.join(FIG_DIR, "w4_contrastive_idea.png")); plt.close(fig)


def neighbours(word, k=5):
    if word not in index:
        return []
    order = np.argsort(-(after_n @ after_n[index[word]]))
    return [vocab[i] for i in order if vocab[i] != word][:k]


QUERIES = ["door", "hand", "eyes", "letter", "count"]
rows = [(q, neighbours(q, 4)) for q in QUERIES if neighbours(q)]
facts["neighbours"] = {q: ns for q, ns in rows}

fig, ax = plt.subplots(figsize=(6.6, 3.8)); blank(ax)
ax.set_xlim(0, 10); ax.set_ylim(0, len(rows) + 1.6)
for i, (q, ns) in enumerate(rows):
    y = len(rows) - i
    ax.add_patch(FancyBboxPatch((0.2, y - 0.34), 9.6, 0.68, boxstyle="round,pad=0.05",
                                fc=TINT if i % 2 == 0 else "white", ec="none"))
    ax.text(0.5, y, q, fontsize=13, va="center", color=WARM, weight="bold")
    ax.text(2.4, y, "   ".join(ns), fontsize=12.5, va="center", color=INK)
ax.text(0.2, len(rows) + 1.1, "nearest neighbours, from vectors trained on two novels",
        fontsize=11.5, color=MUTED)
ax.text(0.2, 0.28, f"{len(toks):,} words, {n_pairs:,} pulls, and five pushes for each one. "
                   "Nobody labelled anything.", fontsize=10.5, color=MUTED)
fig.savefig(os.path.join(FIG_DIR, "w4_neighbours.png")); plt.close(fig)

# 8b. before and after: how alike every pair is, at the start and at the end of training
pick = [w for w in ["night", "day", "morning", "evening",
                    "father", "mother", "sister", "brother",
                    "door", "room", "window", "house"] if w in index]
rows_i = [index[w] for w in pick]


def sim_matrix(mat):
    v = mat[rows_i]
    v = v / (np.linalg.norm(v, axis=1, keepdims=True) + 1e-9)
    return v @ v.T


fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.4))
for ax, mat, name in ((axes[0], before, "before training: nothing is like anything"),
                      (axes[1], after, "after: three blocks nobody labelled")):
    S = sim_matrix(mat)
    np.fill_diagonal(S, np.nan)
    ax.imshow(S, cmap="RdBu_r", vmin=-0.6, vmax=0.6)
    ax.set_xticks(range(len(pick)))
    ax.set_xticklabels(pick, rotation=55, ha="right", fontsize=9.5)
    ax.set_yticks(range(len(pick))); ax.set_yticklabels(pick, fontsize=9.5)
    ax.grid(False); ax.tick_params(length=0)
    ax.set_title(name, fontsize=12.5, loc="left", pad=8)
axes[0].set_xlabel("every square: how alike two words are", color=MUTED, fontsize=10.5)
axes[1].set_xlabel("red = alike. times of day, family, rooms", color=MUTED, fontsize=10.5)
fig.savefig(os.path.join(FIG_DIR, "w4_contrastive_result.png")); plt.close(fig)

# --------------------- 8c. one-hot columns vs the dense vectors we just trained
DENSE_WORDS = [w for w in ("night", "morning", "ship", "sea") if w in index]
DIMS_SHOWN = 8
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.5),
                         gridspec_kw={"width_ratios": [1.15, 1]})
onehot = np.eye(len(DENSE_WORDS))
axes[0].imshow(onehot, cmap="binary", vmin=0, vmax=1.6, aspect="auto")
for i in range(len(DENSE_WORDS)):
    for j in range(len(DENSE_WORDS)):
        axes[0].text(j, i, "1" if i == j else "0", ha="center", va="center",
                     fontsize=11, color="white" if i == j else MUTED)
axes[0].set_xticks(range(len(DENSE_WORDS)))
axes[0].set_xticklabels(DENSE_WORDS, rotation=30, ha="right", fontsize=10.5)
axes[0].set_title("counting: one column per word", fontsize=12.5, loc="left", pad=8)
axes[0].set_xlabel("every pair overlaps in nothing — all equally unrelated",
                   color=MUTED, fontsize=10.5)
dense = after_n[[index[w] for w in DENSE_WORDS], :DIMS_SHOWN]
axes[1].imshow(dense, cmap="RdBu_r", vmin=-np.abs(dense).max(), vmax=np.abs(dense).max(),
               aspect="auto")
for i in range(dense.shape[0]):
    for j in range(DIMS_SHOWN):
        axes[1].text(j, i, f"{dense[i, j]:+.2f}", ha="center", va="center", fontsize=8,
                     color=INK)
axes[1].set_xticks(range(DIMS_SHOWN))
axes[1].set_xticklabels([f"d{i+1}" for i in range(DIMS_SHOWN)], fontsize=9)
sim = lambda a, b: float(after_n[index[a]] @ after_n[index[b]])
axes[1].set_title("training: a few dozen numbers instead", fontsize=12.5, loc="left", pad=8)
axes[1].set_xlabel(f"night · morning = {sim('night','morning'):+.2f}      "
                   f"night · ship = {sim('night','ship'):+.2f}",
                   color=MUTED, fontsize=10.5)
for ax in axes:
    ax.set_yticks(range(len(DENSE_WORDS)))
    ax.set_yticklabels(DENSE_WORDS, fontsize=10.5)
    ax.grid(False); ax.tick_params(length=0)
fig.savefig(os.path.join(FIG_DIR, "w4_onehot_vs_dense.png")); plt.close(fig)
facts["dense_dims_shown"] = DIMS_SHOWN
facts["sim_night_morning"] = round(sim("night", "morning"), 2)
facts["sim_night_ship"] = round(sim("night", "ship"), 2)

# the same vectors, squashed to two dimensions
show = [w for w in ["night", "day", "morning", "evening", "blood", "death", "life",
                    "father", "mother", "friend", "brother", "sister", "door", "window",
                    "room", "house", "sea", "ice", "ship", "letter", "hand", "eyes",
                    "count", "professor", "coffin", "castle"] if w in index]
pts = TruncatedSVD(n_components=2, random_state=0).fit_transform(after_n[[index[w] for w in show]])
fig, ax = plt.subplots(figsize=(6.6, 4.6))
ax.scatter(pts[:, 0], pts[:, 1], s=26, color=WARM, alpha=0.8, lw=0)
# label placement: try four corners per point, keep the first that hits nothing already placed
fx = (pts[:, 0] - pts[:, 0].min()) / np.ptp(pts[:, 0])
fy = (pts[:, 1] - pts[:, 1].min()) / np.ptp(pts[:, 1])
placed = []
for i, w in enumerate(show):
    wid, hgt = 0.021 * len(w), 0.052
    for dx, dy, ha, va in ((0.012, 0.012, "left", "bottom"),
                           (-0.012, 0.012, "right", "bottom"),
                           (0.012, -0.012, "left", "top"),
                           (-0.012, -0.012, "right", "top")):
        x0 = fx[i] + dx - (wid if ha == "right" else 0)
        y0 = fy[i] + dy - (hgt if va == "top" else 0)
        box = (x0, y0, x0 + wid, y0 + hgt)
        if not any(box[0] < p[2] and p[0] < box[2] and box[1] < p[3] and p[1] < box[3]
                   for p in placed):
            break
    placed.append(box)
    ax.annotate(w, (pts[i, 0], pts[i, 1]),
                xytext=(4 if ha == "left" else -4, 3 if va == "bottom" else -3),
                textcoords="offset points", fontsize=10.5, ha=ha, va=va)
ax.margins(0.10)
ax.set_xticks([]); ax.set_yticks([]); ax.tick_params(length=0)
ax.set_xlabel("the same vectors, squashed to two dimensions for looking at",
              color=MUTED, fontsize=10)
fig.savefig(os.path.join(FIG_DIR, "w4_map.png")); plt.close(fig)

# ------------------------------------------------------- 9. JSON becomes a table
def art_institute():
    import requests
    r = requests.get("https://api.artic.edu/api/v1/artworks",
                     params={"limit": 4, "fields": "title,artist_title,date_display"},
                     timeout=20)
    r.raise_for_status()
    return r.json()["data"], "live from api.artic.edu"

try:
    data, src = art_institute()
except Exception as e:
    print("API unavailable:", type(e).__name__, file=sys.stderr)
    data = [{"title": "The Bedroom", "artist_title": "Vincent van Gogh", "date_display": "1889"},
            {"title": "Nighthawks", "artist_title": "Edward Hopper", "date_display": "1942"},
            {"title": "A Sunday on La Grande Jatte", "artist_title": "Georges Seurat",
             "date_display": "1884"}]
    src = "recorded response (the API was unreachable)"
facts["api_source"] = src

fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.9))
for ax in axes:
    blank(ax)
snippet = json.dumps({"data": data[:2]}, indent=1)[:520]
axes[0].text(0, 1, snippet, family="monospace", fontsize=7.6, va="top", color=INK)
axes[0].set_title("what the endpoint returns: JSON", fontsize=12, loc="left", pad=10)
cols = [("title", 0.2, 4.6), ("artist_title", 5.0, 2.8), ("date_display", 8.0, 1.9)]
axes[1].set_xlim(0, 10); axes[1].set_ylim(0, len(data) + 1.5)


def fit_text(ax, x, y, s, room, size=10.5, **kw):
    """Draw s at x, trimming with an ellipsis until it fits `room` data units."""
    rend = fig.canvas.get_renderer()
    inv = ax.transData.inverted()
    t = ax.text(x, y, s, fontsize=size, **kw)
    while len(t.get_text()) > 1:
        bb = t.get_window_extent(renderer=rend)
        (x0, _), (x1, _) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
        if x1 - x0 <= room:
            break
        t.set_text(t.get_text()[:-2] + "\u2026")
    return t


for c, x, _ in cols:
    axes[1].text(x, len(data) + 0.7, c, fontsize=10.5, color=MUTED)
for i, row_ in enumerate(data):
    yy_ = len(data) - i - 0.2
    axes[1].add_patch(FancyBboxPatch((0.1, yy_ - 0.3), 9.8, 0.6, boxstyle="round,pad=0.04",
                                     fc=TINT if i % 2 == 0 else "white", ec="none"))
    for c, x, room in cols:
        fit_text(axes[1], x, yy_, str(row_.get(c, "") or ""), room)
axes[1].set_title("three lines later: a table", fontsize=12, loc="left", pad=10)
fig.savefig(os.path.join(FIG_DIR, "w4_api.png")); plt.close(fig)

# -------------------------------------- 9b. convolutions, spelled all the way out
from scipy.signal import convolve2d
from PIL import Image

MET = os.path.join(REPO, "notebooks", "data", "week01", "met")
SOBEL_V = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], float)
KERNELS = {
    "vertical edges":   SOBEL_V,
    "horizontal edges": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], float),
    "blur":             np.ones((5, 5)) / 25,
}


def met_grey(size=420):
    files = sorted(f for f in os.listdir(MET) if f.endswith(".jpg"))
    img = Image.open(os.path.join(MET, files[0])).convert("L")
    img.thumbnail((size, size))
    return np.asarray(img, float) / 255, files[0]


def arithmetic_figure():
    """One patch, one kernel, one output number, with every multiplication printed.
    The whole of a convolution is on this slide; everything after it is repetition."""
    img, fname = met_grey(size=900)
    h, w = img.shape
    patch = np.asarray(Image.fromarray((img[h // 3:h // 3 + 96, w // 3:w // 3 + 96] * 255)
                                       .astype(np.uint8)).resize((7, 7)), float)
    out = convolve2d(patch, SOBEL_V[::-1, ::-1], mode="valid")     # true convolution
    r, c = 2, 2                                                     # the window we show
    win = patch[r:r + 3, c:c + 3]

    fig = plt.figure(figsize=(11.6, 3.5))
    gs = fig.add_gridspec(1, 4, width_ratios=[1.1, 0.5, 1.7, 0.9], wspace=0.4)
    ax0, ax1, ax2, ax3 = [fig.add_subplot(gs[0, i]) for i in range(4)]

    ax0.imshow(patch, cmap="gray", vmin=0, vmax=255)
    for i in range(7):
        for j in range(7):
            ax0.text(j, i, int(patch[i, j]), ha="center", va="center", fontsize=7.5,
                     color="white" if patch[i, j] < 128 else INK)
    ax0.add_patch(plt.Rectangle((c - .5, r - .5), 3, 3, fill=False, ec=WARM, lw=2.4))
    ax0.set_title("1. the picture is numbers", fontsize=12, loc="left", pad=8)
    ax0.set_xlabel("brightness, 0 = black", color=MUTED, fontsize=10)

    ax1.imshow(SOBEL_V, cmap="RdBu_r", vmin=-2.5, vmax=2.5)
    for i in range(3):
        for j in range(3):
            ax1.text(j, i, f"{SOBEL_V[i, j]:+.0f}", ha="center", va="center", fontsize=13)
    ax1.set_title("2. the filter", fontsize=12, loc="left", pad=8)
    ax1.set_xlabel("nine numbers", color=MUTED, fontsize=10)

    blank(ax2)
    ax2.set_xlim(0, 1); ax2.set_ylim(0, 1)
    rows_txt = [" ".join(f"({SOBEL_V[i, j]:+.0f}×{int(win[i, j]):>3d})" for j in range(3))
                for i in range(3)]
    ax2.set_title("3. multiply, then add up", fontsize=12, loc="left", pad=8)
    ax2.text(0.02, 0.78, "\n".join(rows_txt), family="monospace", fontsize=10.5,
             va="top", linespacing=1.9)
    ax2.text(0.02, 0.20, f"=  {out[r, c]:+.0f}", fontsize=17, color=WARM, weight="bold")
    ax2.text(0.02, 0.02, "one number, for that one spot", fontsize=10.5, color=MUTED)

    ax3.imshow(out, cmap="gray")
    ax3.add_patch(plt.Rectangle((c - .5, r - .5), 1, 1, fill=False, ec=WARM, lw=2.4))
    ax3.set_title("4. slide it, everywhere", fontsize=12, loc="left", pad=8)
    ax3.set_xlabel("the answers make a new picture", color=MUTED, fontsize=10)
    for ax in (ax0, ax1, ax3):
        ax.set_xticks([]); ax.set_yticks([]); ax.grid(False); ax.tick_params(length=0)
    fig.savefig(os.path.join(FIG_DIR, "w4_conv_arith.png")); plt.close(fig)
    facts["conv_one_output"] = round(float(out[r, c]), 1)
    return fname


def convolution_figure():
    a, fname = met_grey()
    fig, axes = plt.subplots(1, 4, figsize=(11.2, 3.2))
    axes[0].imshow(a, cmap="gray"); axes[0].set_title("the painting", fontsize=12, loc="left")
    for ax, (name, k) in zip(axes[1:], KERNELS.items()):
        out = convolve2d(a, k, mode="same", boundary="symm")
        ax.imshow(np.abs(out), cmap="gray")
        ax.set_title(name, fontsize=12, loc="left")
    for ax in axes:
        blank(ax)
    axes[0].set_xlabel("one Met painting, in grey", color=MUTED, fontsize=10.5)
    axes[2].set_xlabel("three different filters, each slid over every pixel",
                       color=MUTED, fontsize=10.5)
    fig.savefig(os.path.join(FIG_DIR, "w4_convolution.png")); plt.close(fig)
    return fname


def stack_figure():
    """Why depth. Each panel is the previous panel convolved again and shrunk, so the
    numbers behind panel 3 are combinations of combinations of raw pixels."""
    a, _ = met_grey(size=480)

    def pool(x, k=2):
        h, w = (x.shape[0] // k) * k, (x.shape[1] // k) * k
        return x[:h, :w].reshape(h // k, k, w // k, k).max((1, 3))

    def layer(x, kern):
        return pool(np.maximum(convolve2d(x, kern, mode="same", boundary="symm"), 0))

    l1 = layer(a, SOBEL_V)
    l2 = layer(l1, np.array([[0, 1, 0], [1, -3, 1], [0, 1, 0]], float))
    l3 = layer(l2, np.ones((3, 3)) / 9)
    panels = [(a, "the pixels", "what you gave it"),
              (l1, "layer 1", "edges"),
              (l2, "layer 2", "corners, texture"),
              (l3, "layer 3", "whole regions")]
    fig, axes = plt.subplots(1, 4, figsize=(11.4, 3.3))
    for ax, (m, t, sub) in zip(axes, panels):
        ax.imshow(m, cmap="gray", vmin=0, vmax=np.percentile(m, 99.5)); blank(ax)
        ax.set_title(f"{t}   ({m.shape[0]}×{m.shape[1]})", fontsize=12, loc="left", pad=6)
        ax.set_xlabel(sub, color=MUTED, fontsize=11)
    fig.savefig(os.path.join(FIG_DIR, "w4_conv_stack.png")); plt.close(fig)


def clip_figure():
    """The two halves of the lecture meeting: the contrastive move from the word-vector
    section, run on (painting, caption) pairs instead of (word, neighbour) pairs."""
    import csv
    rows_ = list(csv.DictReader(open(os.path.join(REPO, "notebooks", "data", "week01",
                                                  "met_manifest.csv"), encoding="utf-8")))
    def short(t):
        return t.split(" (")[0][:44]

    me = rows_[0]
    img = Image.open(os.path.join(REPO, "notebooks", "data", "week01", me["file"]))
    img.thumbnail((300, 300))
    first = short(me["title"]).split()[0].lower()
    others = [short(r["title"]) for r in rows_[1:]
              if short(r["title"]).split()[0].lower() != first][:2]

    fig = plt.figure(figsize=(10.6, 3.9))
    gs = fig.add_gridspec(1, 2, width_ratios=[1, 2.1], wspace=0.05)
    axi = fig.add_subplot(gs[0, 0]); axi.imshow(img); blank(axi)
    axi.set_title("a CNN reads the picture", fontsize=12, loc="left", pad=8)
    ax = fig.add_subplot(gs[0, 1]); blank(ax)
    ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.set_title("a language model reads the captions", fontsize=12, loc="left", pad=8)
    caps = [(short(me["title"]), GOLD, "its own caption — PULL TOGETHER", -1),
            (others[0], COOL, "another painting's — PUSH APART", 1),
            (others[1], COOL, "another painting's — PUSH APART", 1)]
    for i, (t, col, tag, direction) in enumerate(caps):
        y = 4.9 - i * 1.45
        ax.add_patch(FancyBboxPatch((2.0, y - 0.34), 6.6, 0.68, boxstyle="round,pad=0.06",
                                    fc=TINT, ec="none"))
        ax.text(2.25, y, t, fontsize=11.5, va="center")
        # the arrow leaves from the caption and moves it: left is toward the painting
        if direction < 0:
            arrow(ax, (1.8, y), (0.25, y), color=col, lw=2.4)
        else:
            arrow(ax, (8.8, y), (10.0, y), color=col, lw=2.4)
        ax.text(2.25, y - 0.68, tag, fontsize=10, color=col)
    ax.text(0.0, 0.05, "Same move as the word vectors, on picture–caption pairs. That is CLIP, "
                       "and it is why you can search a museum in words.",
            fontsize=11.5, style="italic")
    fig.savefig(os.path.join(FIG_DIR, "w4_clip.png")); plt.close(fig)
    facts["clip_example"] = me["title"]


for name_, fn_ in (("conv_arith", arithmetic_figure), ("convolution", convolution_figure),
                   ("conv_stack", stack_figure), ("clip", clip_figure)):
    try:
        got = fn_()
        if got:
            facts["convolution_image"] = got
    except Exception as e:
        print(f"{name_} figure skipped:", type(e).__name__, e, file=sys.stderr)

# ------------------------------- 8d. the distributional hypothesis, as an exercise
# Real lines from the corpus with the target word blanked out. Everyone in the room can
# fill the gap, and the only evidence they have is the company the word keeps.
def distributional_figure(target="door", n=6, span=7, seed=1):
    rng_ = np.random.default_rng(seed)
    hits = [i for i, w in enumerate(toks) if w == target and span < i < len(toks) - span]
    picks = sorted(rng_.choice(hits, size=min(n, len(hits)), replace=False))
    lines = []
    for i in picks:
        left = " ".join(toks[i - span:i])
        right = " ".join(toks[i + 1:i + 1 + span])
        lines.append((left, right))

    fig, ax = plt.subplots(figsize=(10.6, 3.9)); blank(ax)
    ax.set_xlim(0, 10); ax.set_ylim(0, len(lines) + 2.2)
    for k, (left, right) in enumerate(lines):
        y = len(lines) - k + 0.6
        ax.add_patch(FancyBboxPatch((0.15, y - 0.32), 9.7, 0.64, boxstyle="round,pad=0.05",
                                    fc=TINT if k % 2 == 0 else "white", ec="none"))
        ax.text(4.45, y, left, fontsize=10.5, ha="right", va="center", family="monospace")
        ax.text(5.0, y, "?", fontsize=13, ha="center", va="center", color=WARM,
                weight="bold", family="monospace")
        ax.add_patch(FancyBboxPatch((4.62, y - 0.2), 0.76, 0.4, boxstyle="round,pad=0.03",
                                    fc="none", ec=WARM, lw=1.2))
        ax.text(5.6, y, right, fontsize=10.5, ha="left", va="center", family="monospace")
    ax.text(0.15, len(lines) + 1.6, "Six real lines from the two novels. What is the missing word?",
            fontsize=12.5)
    ax.text(0.15, 0.3, "You knew it, and the only evidence you had was the company it keeps.",
            fontsize=12, style="italic", color=MUTED)
    fig.savefig(os.path.join(FIG_DIR, "w4_distributional.png")); plt.close(fig)
    facts["distributional_word"] = target


try:
    distributional_figure()
except Exception as e:
    print("distributional figure skipped:", type(e).__name__, e, file=sys.stderr)

# ------------------------------------------- 9c. where a corpus comes from
# Four figures for the second half of the lecture. All of them call the real endpoints
# and fall back to recorded values if the network is unavailable at build time.
MONO = {"family": "monospace"}


def api_anatomy():
    """The request on the left, the reply on the right, with the two parts that matter
    labelled: pagination tells you how big the job is, data is the rows."""
    import requests
    url = "https://api.artic.edu/api/v1/artworks/search"
    r = requests.get(url, params={"q": "landscape", "limit": 2,
                                  "fields": "title,artist_title,date_start"}, timeout=25)
    j = r.json()
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 3.9),
                             gridspec_kw={"width_ratios": [1, 1.25], "wspace": 0.12})
    for ax in axes:
        blank(ax); ax.set_xlim(0, 10); ax.set_ylim(0, 10)

    axes[0].set_title("what you send", fontsize=12.5, loc="left", pad=10)
    req = ["GET api.artic.edu/api/v1/artworks/search",
           "        ?q=landscape",
           "        &limit=2",
           "        &fields=title,artist_title,date_start"]
    axes[0].add_patch(FancyBboxPatch((0.2, 5.6), 9.6, 3.4, boxstyle="round,pad=0.12",
                                     fc=TINT, ec="none"))
    axes[0].text(0.5, 8.5, "\n".join(req), fontsize=9.6, va="top", **MONO)
    for y, lab, col in ((4.6, "the endpoint: a URL that answers with data", INK),
                        (3.7, "the query: what you are asking for", WARM),
                        (2.8, "the page size: how much per request", COOL),
                        (1.9, "the fields: ask only for what you need", GOLD)):
        ax = axes[0]
        ax.add_patch(Circle((0.45, y + 0.08), 0.13, fc=col, ec="none"))
        ax.text(0.85, y, lab, fontsize=11, va="center", color=col if col != INK else INK)
    axes[0].text(0.2, 0.5, f"status {r.status_code} · {r.headers['Content-Type'].split(';')[0]}",
                 fontsize=11, color=MUTED)

    axes[1].set_title("what comes back", fontsize=12.5, loc="left", pad=10)
    short = lambda t: (t or "")[:30] + ("..." if len(t or "") > 30 else "")
    body = json.dumps({"pagination": j["pagination"],
                       "data": [{"title": short(d.get("title")),
                                 "artist_title": short(d.get("artist_title")),
                                 "date_start": d.get("date_start")}
                                for d in j["data"][:2]]},
                      indent=1, ensure_ascii=False).split("\n")
    axes[1].add_patch(FancyBboxPatch((0.2, 0.3), 6.6, 8.9, boxstyle="round,pad=0.12",
                                     fc=TINT, ec="none"))
    top_y, step = 8.9, 0.42
    for i, ln in enumerate(body[:21]):
        axes[1].text(0.45, top_y - i * step, ln, fontsize=7.6, va="center", **MONO)
    # brackets and labels down the right-hand side, so nothing crosses the code
    def bracket(i0, i1, col, label):
        y0, y1 = top_y - i1 * step - 0.15, top_y - i0 * step + 0.15
        axes[1].plot([7.0, 7.0], [y0, y1], color=col, lw=2.2)
        axes[1].text(7.25, (y0 + y1) / 2, label, fontsize=10, color=col, va="center",
                     linespacing=1.4)
    pag_end = next(i for i, ln in enumerate(body) if ln.startswith(" }"))
    bracket(1, pag_end, WARM, "read this first:\nhow many exist,\nhow many you got")
    bracket(pag_end + 1, min(len(body), 21) - 1, COOL, "the rows")
    fig.savefig(os.path.join(FIG_DIR, "w4_api_anatomy.png")); plt.close(fig)
    facts["api_total"] = j["pagination"]["total"]


def api_shapes():
    """Two museums, two designs. One hands you rows; the other hands you a phone book."""
    import requests
    artic = requests.get("https://api.artic.edu/api/v1/artworks/search",
                         params={"q": "storm", "limit": 100}, timeout=25).json()
    n_artic = len(artic["data"])
    met = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search",
                       params={"q": "storm", "hasImages": "true"}, timeout=25).json()
    n_met = met["total"]

    fig, axes = plt.subplots(2, 1, figsize=(10.6, 4.6), gridspec_kw={"hspace": 0.45})
    for ax in axes:
        blank(ax); ax.set_xlim(0, 12); ax.set_ylim(0, 3)

    ax = axes[0]
    ax.set_title("Art Institute: one request, and you have a table",
                 fontsize=12.5, loc="left", pad=6)
    ax.add_patch(FancyBboxPatch((0.2, 1.0), 3.0, 1.2, boxstyle="round,pad=0.08",
                                fc=TINT, ec="none"))
    ax.text(0.45, 1.6, "search?q=storm", fontsize=10.5, va="center", **MONO)
    arrow(ax, (3.4, 1.6), (4.6, 1.6), color=INK, lw=1.6)
    for i in range(5):
        ax.add_patch(FancyBboxPatch((4.9, 2.25 - i * 0.42), 6.6, 0.34,
                                    boxstyle="round,pad=0.03", fc=WARM, ec="none",
                                    alpha=0.85 - i * 0.12))
    ax.text(0.2, 0.25, f"one request, {n_artic} rows, and it is already a table.",
            fontsize=11, color=WARM)

    ax = axes[1]
    ax.set_title("The Met: one request for the ID numbers, then one request each",
                 fontsize=12.5, loc="left", pad=6)
    ax.add_patch(FancyBboxPatch((0.2, 1.0), 3.0, 1.2, boxstyle="round,pad=0.08",
                                fc=TINT, ec="none"))
    ax.text(0.45, 1.6, "search?q=storm", fontsize=10.5, va="center", **MONO)
    arrow(ax, (3.4, 1.6), (4.4, 1.6), color=INK, lw=1.6)
    ax.add_patch(FancyBboxPatch((4.6, 1.05), 2.6, 1.1, boxstyle="round,pad=0.06",
                                fc=COOL, ec="none", alpha=0.25))
    ax.text(5.9, 1.6, f"{n_met:,} ID\nnumbers", fontsize=11, ha="center", va="center",
            color=COOL, linespacing=1.3)
    for i in range(4):
        y = 2.55 - i * 0.55
        arrow(ax, (7.4, 1.6), (8.5, y), color=COOL, lw=1.2, alpha=0.8)
        ax.add_patch(FancyBboxPatch((8.7, y - 0.17), 2.6, 0.34, boxstyle="round,pad=0.03",
                                    fc=COOL, ec="none", alpha=0.8))
    ax.text(0.2, 0.25, f"one request for the IDs, then {n_met:,} more to get {n_met:,} rows.",
            fontsize=11, color=COOL)
    fig.savefig(os.path.join(FIG_DIR, "w4_api_shapes.png")); plt.close(fig)
    facts["artic_storm"] = n_artic
    facts["met_storm"] = n_met


def scrape_anatomy():
    """The HTML on the left with the three selectors marked, the row it becomes on the right."""
    import requests
    from bs4 import BeautifulSoup
    html = requests.get("https://quotes.toscrape.com/page/1/", timeout=25,
                        headers={"User-Agent": "culture-as-data course build"}).text
    block = BeautifulSoup(html, "html.parser").select_one("div.quote")
    lines = [ln for ln in block.prettify().split("\n") if ln.strip()][:20]

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.0),
                             gridspec_kw={"width_ratios": [1.55, 1], "wspace": 0.1})
    for ax in axes:
        blank(ax); ax.set_xlim(0, 10); ax.set_ylim(0, 10)

    axes[0].set_title("the page: find the data inside the markup",
                      fontsize=12.5, loc="left", pad=10)
    marks = {"span class=\"text\"": WARM, "small class=\"author\"": COOL,
             "a class=\"tag\"": GOLD}
    for i, ln in enumerate(lines):
        y = 9.4 - i * 0.47
        hit = next((c for k, c in marks.items() if k in ln), None)
        if hit:
            axes[0].add_patch(FancyBboxPatch((0.15, y - 0.17), 9.7, 0.36,
                                             boxstyle="round,pad=0.03", fc=hit, ec="none",
                                             alpha=0.16))
        axes[0].text(0.35, y, ln[:76].replace("\t", "  "), fontsize=7.4, va="center",
                     color=hit or INK, **MONO)

    axes[1].set_title("the row you wanted", fontsize=12.5, loc="left", pad=10)
    row = [("span.text", block.select_one("span.text").get_text(strip=True)[:38] + "...", WARM),
           ("small.author", block.select_one("small.author").get_text(strip=True), COOL),
           ("a.tag", ", ".join(t.get_text(strip=True)
                               for t in block.select("a.tag")[:3]), GOLD)]
    for i, (sel, val, col) in enumerate(row):
        y = 8.2 - i * 2.2
        axes[1].add_patch(FancyBboxPatch((0.2, y - 0.75), 9.5, 1.5,
                                         boxstyle="round,pad=0.08", fc=TINT, ec="none"))
        axes[1].text(0.5, y + 0.35, sel, fontsize=10, color=col, **MONO)
        axes[1].text(0.5, y - 0.3, val, fontsize=10.5, color=INK)
    axes[1].text(0.2, 0.6, "A selector that matches nothing returns None,\nwith no error at all.",
                 fontsize=10.5, color=MUTED, linespacing=1.5)
    fig.savefig(os.path.join(FIG_DIR, "w4_scrape_anatomy.png")); plt.close(fig)


def scrape_cost():
    """What a polite pause costs, so the number is decided before the loop runs."""
    pages = np.arange(0, 5001)
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    for pause, col, lab in ((0.0, MUTED, "no pause: you are a load test"),
                            (1.0, WARM, "1 second between pages"),
                            (2.0, COOL, "2 seconds between pages")):
        ax.plot(pages, pages * (pause + 0.15) / 60, color=col, lw=2.2,
                ls="--" if pause == 0 else "-")
        ax.text(5050, 5000 * (pause + 0.15) / 60, lab, fontsize=10.5, color=col, va="center")
    ax.set_xlabel("pages requested", color=MUTED, fontsize=10.5)
    ax.set_ylabel("minutes", color=MUTED, fontsize=10.5)
    ax.set_xlim(0, 5000)
    ax.set_title("Decide this before you write the loop", fontsize=13, loc="left", pad=10)
    fig.savefig(os.path.join(FIG_DIR, "w4_scrape_cost.png")); plt.close(fig)


for name_, fn_ in (("api_anatomy", api_anatomy), ("api_shapes", api_shapes),
                   ("scrape_anatomy", scrape_anatomy), ("scrape_cost", scrape_cost)):
    try:
        fn_()
    except Exception as e:
        print(f"{name_} figure skipped:", type(e).__name__, e, file=sys.stderr)

# ---------------------------------------------- 10. figures from the paper itself
# Downloaded and cropped at build time from the arXiv preprint of the week's reading
# (arXiv:1711.08412 = PNAS 2018). Kept out of the repo: the build fetches them.
PAPER_CROPS = {                      # name: (page index, clip rect in PDF points)
    "w4_paper_time":       (2, (310, 74, 566, 212)),    # Fig 1b, bias vs occupation share
    "w4_paper_validation": (2, (62, 74, 305, 212)),     # Fig 1a, embedding bias vs census
    "w4_paper_ethnic":     (2, (75, 258, 292, 402)),    # Fig 1c, occupations by group
    "w4_paper_adjectives": (5, (98, 66, 270, 212)),     # Fig 2a, adjectives 1910/1950/1990
    "w4_paper_phaseshift": (5, (305, 62, 558, 205)),    # Fig 2b, decade correlation matrix
}

def paper_figures():
    import requests
    try:
        import pymupdf
    except ImportError:
        import fitz as pymupdf
    pdf = os.path.join(FIG_DIR, "garg2018.pdf")
    if not os.path.exists(pdf):
        r = requests.get("https://arxiv.org/pdf/1711.08412", timeout=60)
        r.raise_for_status()
        open(pdf, "wb").write(r.content)
    doc = pymupdf.open(pdf)
    for name, (page, box) in PAPER_CROPS.items():
        doc[page].get_pixmap(clip=pymupdf.Rect(*box), dpi=450).save(
            os.path.join(FIG_DIR, name + ".png"))
    return len(PAPER_CROPS)

try:
    facts["paper_figures"] = paper_figures()
    print(f"cropped {facts['paper_figures']} figures from the paper")
except Exception as e:
    facts["paper_figures"] = 0
    print("paper figures unavailable:", type(e).__name__, e, file=sys.stderr)
    print("  (the deck falls back to text-only versions of those slides)", file=sys.stderr)

with open(os.path.join(FIG_DIR, "week04_figs.json"), "w") as f:
    json.dump(facts, f, indent=1)
print(json.dumps(facts, indent=1)[:700])
print("figures written to", FIG_DIR)
