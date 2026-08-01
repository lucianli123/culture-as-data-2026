# Teaching diagrams (SVG)

Hand-built vector diagrams for the beats that a chart of real data can't carry — the ones
where the point is the *idea*, not the numbers. Plain SVG: they scale to any projector, open in
a browser, drop into the site with an `<img>` tag, and insert into PowerPoint 2016+ or Google
Slides as vectors.

Regenerate after editing:

```bash
python3 slides/figures/make_svgs.py
```

The geometry lives in that one script, so the figures stay consistent with each other. Colors
are the course palette stepped up in chroma; the categorical trio (terracotta / blue / gold)
passes the colorblind-separation, chroma and contrast checks.

| File | What it argues | Where it belongs |
|---|---|---|
| `vector-from-text.svg` | A document becomes one row of numbers, one column per word in the corpus — and for any single document nearly all of them are zero. **The model never sees the sentence; it sees the row.** | Week 2's vectorization beat; Week 3's "counting with weights" slide |
| `vectors-in-space.svg` | Rows of numbers are points, so a corpus is a cloud. Two words make a plane you can draw; a real corpus has thousands of axes and the arithmetic is unchanged. The angle between two documents is how alike their wording is. | Week 2 (vector space); the setup for Week 5 |
| `clustering-motivation.svg` | The same eighteen documents twice. Left: coloured by the two labels you brought, with the boundary a classifier can draw. Right: unlabelled, where the corpus's own dense groups turn out to be **three**, and the third straddles your boundary. **Classification can only answer the question you brought; clustering can hand you one you didn't think to ask.** | Week 3's closing bridge; Week 5's opening |

Both panels of the clustering figure are drawn from one list of points defined once in the
script. Nothing is nudged between panels — the disagreement between the labels and the groups
is in the coordinates, not in the drawing.
