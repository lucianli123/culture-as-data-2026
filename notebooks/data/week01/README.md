# Week 1 data (all offline-safe)

Everything the Week 1 notebook needs, snapshotted so the session never depends on the
network. The notebook looks here first, then the live sources, then its built-in sample.

| File | What it is | License |
|---|---|---|
| `nyt_weddings.csv` | The Upshot's 7,835 NYT wedding announcements, 1985-2014 (5,562 with a clear name status) | MIT (see `LICENSE-nyt-weddings.txt`) |
| `met/*.jpg` + `met_manifest.csv` | 18 public-domain Met paintings (200px thumbnails) with titles, artists, source URLs | CC0 |
| `name_keeping_by_year.csv` | Derived: share of brides keeping their name, by year | derived |
| `headline_word_counts.csv` | Derived: top 200 headline words after stop-word removal | derived |
| `met_brightness_palette.csv` | Derived: per-painting brightness and color-range shares | derived |

The derived files are catch-up points: a student who falls behind can load the result of
any Week 1 step and keep moving. Regenerate them by running the notebook top to bottom.
