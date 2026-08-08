#!/usr/bin/env python3
"""Figures for the Week 4 lecture draft deck (neural networks, word embeddings, APIs).

Nothing here is a stock illustration. The spiral is a real fit, the word vectors are
trained on the two novels in notebooks/data/texts, the nearest neighbours are computed
from them, and the API panel calls a live endpoint (falling back to a saved response).

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
    "figure.dpi": 200, "savefig.dpi": 200, "savefig.bbox": "tight",
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

# ------------------------------------------------------------- 2. a network
fig, ax = plt.subplots(figsize=(6.6, 4.0)); blank(ax)
ax.set_xlim(0, 10); ax.set_ylim(0, 6)
inp = [(1.4, y) for y in (4.8, 3.8, 2.8, 1.8, 0.8)]
hid = [(5.0, y) for y in (4.4, 3.4, 2.4, 1.4)]
out = [(8.4, 2.9)]
for a in inp:
    for b in hid:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=GRID, lw=0.8, zorder=1)
for b in hid:
    for c in out:
        ax.plot([b[0], c[0]], [b[1], c[1]], color=MUTED, lw=0.9, alpha=0.6, zorder=1)
for (x, y) in inp:
    ax.add_patch(Circle((x, y), 0.26, fc="white", ec=MUTED, lw=1.2, zorder=2))
for (x, y) in hid:
    ax.add_patch(Circle((x, y), 0.30, fc=TINT, ec=GOLD, lw=1.6, zorder=2))
for (x, y) in out:
    ax.add_patch(Circle((x, y), 0.32, fc="white", ec=WARM, lw=1.8, zorder=2))
ax.text(1.4, 5.5, "one per word", ha="center", fontsize=11, color=MUTED)
ax.text(5.0, 5.5, "a hidden layer", ha="center", fontsize=11, color=GOLD)
ax.text(8.4, 5.5, "the answer", ha="center", fontsize=11, color=WARM)
ax.text(5.0, 0.62, "each of these is its own neuron, and what it detects\n"
                   "is not a word you chose — it is a combination the model invented",
        ha="center", fontsize=11.5, color=INK, linespacing=1.5)
fig.savefig(os.path.join(FIG_DIR, "w4_network.png")); plt.close(fig)

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

# --------------------------------------- 4. the spiral: one line vs a network
rng = np.random.default_rng(0)
n = 220
t = np.sqrt(rng.random(n)) * 3.2 * np.pi
x1 = np.c_[t * np.cos(t), t * np.sin(t)] + rng.normal(0, 0.55, (n, 2))
x2 = np.c_[t * np.cos(t + np.pi), t * np.sin(t + np.pi)] + rng.normal(0, 0.55, (n, 2))
X = np.vstack([x1, x2]); y = np.r_[np.ones(n), np.zeros(n)]
lin = LogisticRegression().fit(X, y)
net = MLPClassifier(hidden_layer_sizes=(24, 24), max_iter=4000, random_state=0).fit(X, y)
xx, yy = np.meshgrid(np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 300),
                     np.linspace(X[:, 1].min() - 1, X[:, 1].max() + 1, 300))
fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.4))
for ax, model, name in ((axes[0], lin, "one neuron"), (axes[1], net, "a network")):
    zz = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1].reshape(xx.shape)
    ax.contourf(xx, yy, zz, levels=[0, 0.5, 1], colors=[COOL, WARM], alpha=0.10)
    ax.contour(xx, yy, zz, levels=[0.5], colors=[MUTED], linewidths=1.4)
    ax.scatter(X[y == 1, 0], X[y == 1, 1], s=9, color=WARM, alpha=0.85, lw=0)
    ax.scatter(X[y == 0, 0], X[y == 0, 1], s=9, color=COOL, alpha=0.85, lw=0)
    blank(ax)
    ax.set_title(f"{name}: {model.score(X, y):.0%} right", fontsize=13, pad=8, loc="left")
axes[0].set_xlabel("a straight line, wherever you put it", color=MUTED, fontsize=10.5)
axes[1].set_xlabel("stacked neurons bend the boundary", color=MUTED, fontsize=10.5)
fig.savefig(os.path.join(FIG_DIR, "w4_spiral.png")); plt.close(fig)
facts["spiral_linear"] = round(float(lin.score(X, y)), 3)
facts["spiral_net"] = round(float(net.score(X, y)), 3)

# ----------------------------------------- 5. one-hot columns vs dense vectors
fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.6),
                         gridspec_kw={"width_ratios": [1.55, 1]})
vocab = ["happy", "joyful", "glad", "oakland", "berkeley", "bart"]
onehot = np.eye(6)[[0, 1, 3, 4]]
axes[0].imshow(onehot, cmap="binary", vmin=0, vmax=1.6, aspect="auto")
axes[0].set_xticks(range(6)); axes[0].set_xticklabels(vocab, rotation=35, ha="right", fontsize=10)
axes[0].set_yticks(range(4))
axes[0].set_yticklabels(["happy", "joyful", "oakland", "berkeley"], fontsize=10)
axes[0].grid(False); axes[0].tick_params(length=0)
axes[0].set_title("one column per word: every pair is equally unrelated",
                  fontsize=12, loc="left", pad=8)
dense = np.array([[0.82, 0.31, -0.44, 0.12], [0.79, 0.28, -0.39, 0.18],
                  [-0.35, 0.71, 0.22, -0.51], [-0.31, 0.68, 0.27, -0.47]])
im = axes[1].imshow(dense, cmap="RdBu_r", vmin=-1, vmax=1, aspect="auto")
axes[1].set_xticks(range(4)); axes[1].set_xticklabels([f"d{i+1}" for i in range(4)], fontsize=10)
axes[1].set_yticks(range(4))
axes[1].set_yticklabels(["happy", "joyful", "oakland", "berkeley"], fontsize=10)
axes[1].grid(False); axes[1].tick_params(length=0)
axes[1].set_title("a few dozen numbers: near means alike", fontsize=12, loc="left", pad=8)
fig.savefig(os.path.join(FIG_DIR, "w4_onehot_vs_dense.png")); plt.close(fig)

# ------------------------------------------------- 6. the fake training task
fig, ax = plt.subplots(figsize=(6.8, 3.5)); blank(ax)
ax.set_xlim(0, 10); ax.set_ylim(0, 5)
sent = ["the", "tide", "came", "in", "over", "the", "cold", "sand"]
centre = 4
for i, tok in enumerate(sent):
    x = 0.35 + i * 1.2
    inside = abs(i - centre) <= 2 and i != centre
    fc = TINT if inside else "white"
    ec = GOLD if i == centre else (MUTED if inside else GRID)
    ax.add_patch(FancyBboxPatch((x, 3.3), 1.05, 0.66, boxstyle="round,pad=0.05",
                                fc=fc, ec=ec, lw=1.8 if i == centre else 1.0))
    ax.text(x + 0.52, 3.63, tok, ha="center", va="center", fontsize=11.5,
            color=INK if (inside or i == centre) else MUTED)
ax.text(0.35 + centre * 1.2 + 0.52, 4.3, "given this word", ha="center", fontsize=11, color=GOLD)
ax.text(0.35 + centre * 1.2 + 0.52, 2.85, "guess these", ha="center", fontsize=11, color=MUTED)
pairs = "(over, came)   (over, in)   (over, the)   (over, cold)"
ax.text(0.35, 2.05, "training pairs:  " + pairs, fontsize=12, color=INK)
ax.text(0.35, 1.25, "Nobody wants the guesses. The by-product is the point:", fontsize=12.5)
ax.text(0.35, 0.65, "the hidden layer becomes one vector per word.", fontsize=12.5,
        style="italic", color=WARM)
fig.savefig(os.path.join(FIG_DIR, "w4_skipgram.png")); plt.close(fig)

# ---------------------------- 7 + 8. vectors trained on the two repo novels
def load_words():
    text = ""
    for fn in ("frankenstein.txt", "dracula.txt"):
        text += open(os.path.join(REPO, "notebooks", "data", "texts", fn),
                     encoding="utf-8", errors="ignore").read().lower() + "\n"
    return re.findall(r"[a-z']{2,}", text)

toks = load_words()
counts = Counter(toks)
vocab = [w for w, c in counts.most_common(4000)]
index = {w: i for i, w in enumerate(vocab)}
V, WIN = len(vocab), 5
co = np.zeros((V, V), dtype=np.float32)
ids = [index.get(t, -1) for t in toks]
for i, a in enumerate(ids):
    if a < 0:
        continue
    for j in range(max(0, i - WIN), min(len(ids), i + WIN + 1)):
        b = ids[j]
        if b >= 0 and j != i:
            co[a, b] += 1
# PPMI, then a small SVD: the honest classroom version of word2vec
tot = co.sum()
row, col = co.sum(1, keepdims=True), co.sum(0, keepdims=True)
with np.errstate(divide="ignore", invalid="ignore"):
    pmi = np.log((co * tot) / (row * col))
pmi[~np.isfinite(pmi)] = 0
pmi[pmi < 0] = 0
vecs = TruncatedSVD(n_components=80, random_state=0).fit_transform(pmi)
vecs /= (np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-9)

def neighbours(word, k=5):
    if word not in index:
        return []
    sims = vecs @ vecs[index[word]]
    order = np.argsort(-sims)
    return [vocab[i] for i in order if vocab[i] != word][:k]

QUERIES = ["night", "father", "blood", "door", "sea"]
rows = [(q, neighbours(q)) for q in QUERIES if neighbours(q)]
facts["neighbours"] = {q: ns for q, ns in rows}
facts["corpus_tokens"] = len(toks)
facts["corpus_vocab"] = V

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
ax.text(0.2, 0.28, f"{len(toks):,} words of Frankenstein and Dracula. No labels, no supervision: "
                   "just who keeps company with whom.", fontsize=10.5, color=MUTED)
fig.savefig(os.path.join(FIG_DIR, "w4_neighbours.png")); plt.close(fig)

# the same vectors, squashed to two dimensions
show = [w for w in ["night", "day", "morning", "evening", "blood", "death", "life",
                    "father", "mother", "friend", "brother", "sister", "door", "window",
                    "room", "house", "sea", "ice", "ship", "letter", "hand", "eyes",
                    "count", "professor", "coffin", "castle"] if w in index]
pts = TruncatedSVD(n_components=2, random_state=0).fit_transform(vecs[[index[w] for w in show]])
fig, ax = plt.subplots(figsize=(6.6, 4.6))
ax.scatter(pts[:, 0], pts[:, 1], s=26, color=WARM, alpha=0.8, lw=0)
# crude label repel: alternate the offset so neighbouring labels do not stack
offsets = [(6, 4, "left"), (6, -10, "left"), (-6, 4, "right"), (-6, -10, "right")]
order = np.argsort(pts[:, 0])
for rank, idx in enumerate(order):
    x, y = pts[idx]
    dx, dy, ha = offsets[rank % 4]
    ax.annotate(show[idx], (x, y), xytext=(dx, dy), textcoords="offset points",
                fontsize=10.5, ha=ha)
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
cols = ["title", "artist_title", "date_display"]
axes[1].set_xlim(0, 10); axes[1].set_ylim(0, len(data) + 1.5)
for j, c in enumerate(cols):
    axes[1].text(0.2 + j * 3.3, len(data) + 0.7, c, fontsize=10.5, color=MUTED)
for i, row_ in enumerate(data):
    yy_ = len(data) - i - 0.2
    axes[1].add_patch(FancyBboxPatch((0.1, yy_ - 0.3), 9.8, 0.6, boxstyle="round,pad=0.04",
                                     fc=TINT if i % 2 == 0 else "white", ec="none"))
    for j, c in enumerate(cols):
        axes[1].text(0.2 + j * 3.3, yy_, str(row_.get(c, ""))[:26], fontsize=10.5)
axes[1].set_title("three lines later: a table", fontsize=12, loc="left", pad=10)
fig.savefig(os.path.join(FIG_DIR, "w4_api.png")); plt.close(fig)

with open(os.path.join(FIG_DIR, "week04_figs.json"), "w") as f:
    json.dump(facts, f, indent=1)
print(json.dumps(facts, indent=1)[:700])
print("figures written to", FIG_DIR)
