# Week 1 data (all offline-safe)

Everything the Week 1 notebook needs, snapshotted so the session never depends on the
network. The notebook looks here first, then the live sources, then its built-in samples.

| File | What it is | License |
|---|---|---|
| `shakespeare_sonnets.txt` | Gutenberg #1041: the 154 sonnets of 1609, the word corpus | public domain |
| `sonnet_word_counts.csv` | Derived: top 200 sonnet words after stop-word removal | derived |
| `met/*.jpg` + `met_manifest.csv` | 18 public-domain Met paintings (200px thumbnails) with titles, artists, source URLs | CC0 |
| `met_brightness_palette.csv` | Derived: per-painting brightness and color-range shares | derived |

The derived files are catch-up points: a student who falls behind can load the result of
a step and keep moving. Regenerate them by running the notebook top to bottom.
