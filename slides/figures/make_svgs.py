#!/usr/bin/env python3
"""Teaching diagrams for the vector / clustering beats, written as plain SVG.

Three figures, each making one argument:

  vector-from-text.svg     a document becomes a row of numbers (and most of it is zeros)
  vectors-in-space.svg     rows of numbers become points; near means "worded alike"
  clustering-motivation.svg  the same points, twice: sorted into your labels, then
                             grouped without them - and the groups disagree

The two panels of the third figure share one list of points, computed once here,
which is the whole argument: nothing is redrawn to flatter the story.

    python3 slides/figures/make_svgs.py

Colors are the course palette stepped up in chroma; the categorical trio passes the
CVD-separation, chroma and contrast checks (worst adjacent pair, normal vision, dE 25.4).
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

WARM, COOL, GOLD = "#A34526", "#1F5FA8", "#B9852F"
INK, MUTED, RULE, TINT = "#1A1A1A", "#6B6B63", "#D9D4CC", "#F4EEE8"
SERIF = "Georgia, 'Times New Roman', serif"
SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'SF Mono', 'Courier New', monospace"


def svg(w, h, body, title, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
            f'height="{h}" role="img" aria-labelledby="t d" font-family="{SANS}">\n'
            f'<title id="t">{title}</title>\n<desc id="d">{desc}</desc>\n{body}\n</svg>\n')


def text(x, y, s, size=13, fill=INK, family=SANS, anchor="start", weight="normal",
         style="normal", spacing=0):
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-family="{family}" '
            f'text-anchor="{anchor}" font-weight="{weight}" font-style="{style}"{ls}>{s}</text>')


def rect(x, y, w, h, fill="none", stroke="none", r=6, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


def line(x1, y1, x2, y2, stroke=RULE, sw=1.5, dash=None, cap="round"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}" stroke-linecap="{cap}"{d}/>')


def circle(cx, cy, r, fill, stroke="#FFFFFF", sw=1.2):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


ARROW = ('<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
         f'markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{MUTED}"/>'
         '</marker></defs>')


def arrow(x1, y1, x2, y2, stroke=MUTED, sw=1.6):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}" marker-end="url(#a)"/>')


# ---------------------------------------------------------------------------
# 1. a document becomes a row of numbers
# ---------------------------------------------------------------------------
SENTENCE = "the tide came in over the cold sand"
VOCAB = ["butter", "came", "cold", "in", "over", "pasta", "sand", "the", "tide", "…"]
COUNTS = ["0", "1", "1", "1", "1", "0", "1", "2", "1", ""]

b = [ARROW]
b.append(text(28, 40, "ONE DOCUMENT, ONE ROW OF NUMBERS", 12, MUTED, SANS, weight="bold", spacing=2))

b.append(rect(28, 62, 300, 78, TINT, r=8))
b.append(text(44, 96, "“the tide came in over", 17, INK, SERIF))
b.append(text(44, 120, "the cold sand”", 17, INK, SERIF))
b.append(text(28, 162, "a comment, a sentence, a novel — one item of your corpus", 12, MUTED))

b.append(arrow(346, 100, 396, 100))
b.append(text(371, 84, "count", 11, MUTED, anchor="middle"))

x0, cw = 416, 52
for i, (w, c) in enumerate(zip(VOCAB, COUNTS)):
    x = x0 + i * cw
    zero = c == "0"
    b.append(rect(x, 62, cw - 6, 78, "#FFFFFF" if zero else TINT, RULE, r=6))
    b.append(text(x + (cw - 6) / 2, 88, w, 10.5, MUTED if zero else INK, anchor="middle"))
    b.append(text(x + (cw - 6) / 2, 122, c, 20, RULE if zero else WARM, MONO, anchor="middle",
                  weight="bold"))
b.append(text(416, 162, "one column per word in the whole corpus — thousands of them —", 12, MUTED))
b.append(text(416, 180, "and for any single document, nearly all of them are zero", 12, MUTED))
b.append(text(28, 218, "The model never sees the sentence. It sees this row.", 15, INK, SERIF,
              style="italic"))

open(os.path.join(OUT, "vector-from-text.svg"), "w").write(svg(
    960, 246, "\n".join(b), "A document becomes a row of word counts",
    "The sentence 'the tide came in over the cold sand' is turned into a row of counts, "
    "one column per word in the corpus vocabulary, mostly zeros."))

# ---------------------------------------------------------------------------
# 2. rows of numbers become points in a space
# ---------------------------------------------------------------------------
SEA = [(3.0, 1.0), (4.1, 1.5), (2.3, 0.6)]
KITCHEN = [(0.8, 3.2), (1.5, 4.3), (0.7, 2.5)]

W, H = 820, 500
PX, PY, PW, PH = 120, 66, 450, 310          # plot box
sx = lambda v: PX + v * (PW / 5)
sy = lambda v: PY + PH - v * (PH / 5)

b = [ARROW]
b.append(text(28, 36, "EVERY DOCUMENT IS A POINT", 12, MUTED, SANS, weight="bold", spacing=2))
for g in range(1, 6):
    b.append(line(sx(g), PY, sx(g), PY + PH, RULE, 1))
    b.append(line(PX, sy(g), PX + PW, sy(g), RULE, 1))
b.append(line(PX, PY + PH, PX + PW, PY + PH, MUTED, 1.5))
b.append(line(PX, PY, PX, PY + PH, MUTED, 1.5))
b.append(text(PX + PW / 2, PY + PH + 38, "how many times “tide” appears  \u2192", 13, MUTED,
              anchor="middle"))
b.append(f'<g transform="translate({PX - 46},{PY + PH / 2}) rotate(-90)">'
         + text(0, 0, "how many times “butter” appears  \u2192", 13, MUTED, anchor="middle") + "</g>")

# two vectors from the origin, drawn before the points so the dots sit on top
b.append(f'<line x1="{PX}" y1="{PY + PH}" x2="{sx(3.0)}" y2="{sy(1.0)}" stroke="{WARM}" '
         f'stroke-width="1.8" opacity="0.5"/>')
b.append(f'<line x1="{PX}" y1="{PY + PH}" x2="{sx(0.8)}" y2="{sy(3.2)}" stroke="{COOL}" '
         f'stroke-width="1.8" opacity="0.5"/>')
b.append(f'<path d="M {sx(1.05)} {sy(0.35)} A 105 105 0 0 0 {sx(0.28)} {sy(1.12)}" '
         f'fill="none" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="3 3"/>')

for (x, y) in SEA:
    b.append(circle(sx(x), sy(y), 7.5, WARM))
for (x, y) in KITCHEN:
    b.append(circle(sx(x), sy(y), 7.5, COOL))

b.append(text(sx(3.0) + 4, sy(1.0) + 26, "“the tide came in…”", 12.5, WARM, SERIF, style="italic"))
b.append(text(sx(1.5) + 16, sy(4.3) + 4, "“he chopped onions…”", 12.5, COOL, SERIF, style="italic"))

# the angle annotation sits in the empty wedge between the two vectors
b.append(text(sx(1.35), sy(2.35), "the angle between two vectors", 11.5, MUTED))
b.append(text(sx(1.35), sy(2.13), "is how alike their wording is", 11.5, MUTED))

b.append(rect(PX + PW + 26, PY, 178, 124, TINT, r=8))
b.append(text(PX + PW + 44, PY + 30, "two words here.", 12.5, INK, SANS, weight="bold"))
b.append(text(PX + PW + 44, PY + 54, "a real corpus has", 12.5, INK))
b.append(text(PX + PW + 44, PY + 72, "thousands of axes,", 12.5, INK))
b.append(text(PX + PW + 44, PY + 90, "one per word — the", 12.5, INK))
b.append(text(PX + PW + 44, PY + 108, "arithmetic is the same.", 12.5, INK))

b.append(text(28, H - 30, "Near each other means worded alike, not “about the same thing”. "
                          "Closing that gap is the whole argument of Week 5.",
              14, INK, SERIF, style="italic"))

open(os.path.join(OUT, "vectors-in-space.svg"), "w").write(svg(
    W, H, "\n".join(b), "Documents as points in a space of word counts",
    "Six documents plotted by how often two words appear; sea sentences and kitchen "
    "sentences land in different regions, and the angle between two vectors is their similarity."))

# ---------------------------------------------------------------------------
# 3. why cluster at all: the same points, labelled and unlabelled
# ---------------------------------------------------------------------------
# ONE list of points, used by BOTH panels - that is the argument. Your labels split
# left from right (a classifier can draw that line). The corpus's own dense groups are
# three, and the third one straddles the line: a way of writing that both piles share.
PTS = [
    (0.9, 3.9), (1.4, 4.3), (0.7, 4.6), (1.6, 3.6), (1.1, 3.2), (1.9, 4.1),   # group 1
    (4.0, 4.4), (4.5, 3.9), (4.2, 4.8), (4.8, 4.5), (3.7, 4.0), (4.6, 3.3),   # group 2
    (2.4, 1.2), (2.9, 0.8), (3.4, 1.5), (2.6, 1.8), (3.1, 2.0), (3.6, 1.1),   # group 3
]
BOUNDARY_X = 3.25                    # your two labels: left of this vs. right of it
GROUP_RING = {1: (1.27, 3.95, 1.25), 2: (4.30, 4.15, 1.15), 3: (3.00, 1.40, 1.20)}

W, H = 1000, 620
PW = PH = 290
PANELS = {"A": 74, "B": 560}
PY = 150
gx = lambda v, left: left + v * (PW / 5.4)
gy = lambda v: PY + PH - v * (PH / 5.4)

b = [ARROW]
b.append(text(28, 34, "TWO WAYS TO LOOK AT ONE CORPUS", 12, MUTED, SANS, weight="bold", spacing=2))

for panel, left in PANELS.items():
    b.append(rect(left - 26, PY - 22, PW + 52, PH + 44, "#FFFFFF", RULE, r=10))
    for g in range(1, 6):
        b.append(line(gx(g, left), PY, gx(g, left), PY + PH, RULE, 1))
        b.append(line(left, gy(g), left + PW, gy(g), RULE, 1))

# --- panel A: you brought the labels, so a classifier can draw the line
left = PANELS["A"]
b.append(text(left - 26, 84, "You brought two labels", 20, INK, SERIF, weight="bold"))
b.append(text(left - 26, 108, "CLASSIFICATION  ·  supervised", 11, WARM, SANS, weight="bold",
              spacing=1.5))
b.append(f'<line x1="{gx(BOUNDARY_X, left)}" y1="{PY}" x2="{gx(BOUNDARY_X, left)}" '
         f'y2="{PY + PH}" stroke="{MUTED}" stroke-width="1.8" stroke-dasharray="6 5"/>')
for (x, y) in PTS:
    b.append(circle(gx(x, left), gy(y), 7, WARM if x < BOUNDARY_X else COOL))
b.append(circle(left + 4, PY + PH + 46, 6, WARM))
b.append(text(left + 18, PY + PH + 51, "pile A", 12, INK))
b.append(circle(left + 92, PY + PH + 46, 6, COOL))
b.append(text(left + 106, PY + PH + 51, "pile B", 12, INK))
b.append(text(left - 26, PY + PH + 84, "The dashed line is the model. It answers the one", 12.5, INK))
b.append(text(left - 26, PY + PH + 102, "question you brought, and only that one.", 12.5, INK))

# --- panel B: no labels, so the corpus reports its own groups
left = PANELS["B"]
b.append(text(left - 26, 84, "Now take the labels away", 20, INK, SERIF, weight="bold"))
b.append(text(left - 26, 108, "CLUSTERING  ·  unsupervised", 11, GOLD, SANS, weight="bold",
              spacing=1.5))
b.append(f'<line x1="{gx(BOUNDARY_X, left)}" y1="{PY}" x2="{gx(BOUNDARY_X, left)}" '
         f'y2="{PY + PH}" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="6 5" '
         f'opacity="0.35"/>')          # the same line, ghosted: group 3 straddles it
for g, (cx, cy, r) in GROUP_RING.items():
    b.append(f'<ellipse cx="{gx(cx, left):.1f}" cy="{gy(cy):.1f}" rx="{r * (PW / 5.4):.1f}" '
             f'ry="{r * (PH / 5.4):.1f}" fill="{GOLD}" fill-opacity="0.08" stroke="{GOLD}" '
             f'stroke-width="1.6" stroke-dasharray="5 4"/>')
for (x, y) in PTS:
    b.append(circle(gx(x, left), gy(y), 7, MUTED))
b.append(text(gx(1.27, left), gy(5.46), "group 1", 12, GOLD, anchor="middle", weight="bold"))
b.append(text(gx(4.30, left), gy(5.46), "group 2", 12, GOLD, anchor="middle", weight="bold"))
b.append(text(gx(3.00, left), gy(2.86), "group 3", 12, GOLD, anchor="middle", weight="bold"))
b.append(text(left - 26, PY + PH + 51, "Same points, no labels. The machine reports where the",
              12.5, INK))
b.append(text(left - 26, PY + PH + 69, "corpus is dense: three groups, not two.", 12.5, INK))
b.append(text(left - 26, PY + PH + 95, "And group 3 sits astride the line — a way of writing", 12.5, INK))
b.append(text(left - 26, PY + PH + 113, "that both of your piles share.", 12.5, INK))

b.append(arrow(PANELS["A"] + PW + 44, PY + PH / 2, PANELS["B"] - 60, PY + PH / 2))
mid = (PANELS["A"] + PW + PANELS["B"]) / 2 - 8
b.append(text(mid, PY + PH / 2 - 16, "drop the", 11, MUTED, anchor="middle"))
b.append(text(mid, PY + PH / 2 + 30, "labels", 11, MUTED, anchor="middle"))

b.append(text(28, H - 26, "Classification can only answer the question you brought. Clustering "
                          "can hand you one you didn’t think to ask — which is why the course "
                          "goes there next.", 14, INK, SERIF, style="italic"))

open(os.path.join(OUT, "clustering-motivation.svg"), "w").write(svg(
    W, H, "\n".join(b), "Classification versus clustering on the same points",
    "The same eighteen documents shown twice: on the left coloured by the two labels you "
    "brought, with a classifier's boundary; on the right unlabelled, where three dense "
    "groups appear and the third straddles the boundary."))

print("wrote:", ", ".join(sorted(f for f in os.listdir(OUT) if f.endswith(".svg"))))
