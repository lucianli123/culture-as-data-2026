#!/usr/bin/env python3
"""check_sync.py — fail loudly when the site/slides generator drifts from the design docs.

The weekly content in tools/build_site.py is a curated copy of design/lesson-plans.md.
That copy is hand-synced, which is exactly how the featured-study swap once reached the
notebooks but not the site and decks. This check makes that drift a red test instead of
a silent inconsistency.

Checks:
  1. The default featured study of each week in the planning doc's "Look at This" Library
     table appears in that week's `admire` text in build_site.py.
  2. Retired studies do not appear as a week's featured study in the generator.
  3. The generated artifacts (docs/, slides/slides.json, slides/week-NN.md) are what the
     generators currently produce (re-run and byte-compare, in a temp copy).

Run:  python tools/check_sync.py        (exit 0 = in sync)
"""
from __future__ import annotations
import re, sys, json, subprocess, tempfile, filecmp, shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))
import build_site as B

FAIL = []

# --- 1. featured studies: planning-doc library table vs. generator `admire` ---------
# Keyed on stable, distinctive tokens of each week's *default* featured piece.
EXPECTED = {
    1: ["She Giggles, He Gallops"],
    2: ["Bollen"],
    3: ["Underwood"],
    5: ["Kozlowski", "Bolukbasi"],
    6: ["Arnold"],
    7: ["Gilardi"],
    8: ["TimeCapsule"],
}
# Studies that must NOT be a week's default featured study anymore (swaps are fine
# elsewhere: readings, swap lists, supplements).
RETIRED_DEFAULTS = {
    1: ["Pockets"],
    3: ["Public Bible", "Mullen"],
    5: ["Caliskan", "Soni"],
}

weeks = {w["n"]: w for w in B.WEEKS}
for n, tokens in EXPECTED.items():
    blob = weeks[n]["admire"] + " " + weeks[n]["interrogate"]
    for tok in tokens:
        if tok.lower() not in blob.lower():
            FAIL.append(f"week {n}: expected featured-study token {tok!r} missing from build_site.py admire/interrogate")
for n, tokens in RETIRED_DEFAULTS.items():
    blob = weeks[n]["admire"]
    for tok in tokens:
        if tok.lower() in blob.lower():
            FAIL.append(f"week {n}: retired study {tok!r} still the featured study in build_site.py")

# Cross-check EXPECTED against the design docs themselves, so this table can't rot:
lesson_plans = (REPO / "design" / "lesson-plans.md").read_text(encoding="utf-8")
for n, tokens in EXPECTED.items():
    for tok in tokens:
        if tok.lower() not in lesson_plans.lower():
            FAIL.append(f"week {n}: token {tok!r} not found in design/lesson-plans.md — update EXPECTED in check_sync.py")

# --- 2. generated artifacts match the generators --------------------------------
with tempfile.TemporaryDirectory() as td:
    tmp = Path(td) / "repo"
    shutil.copytree(REPO, tmp, ignore=shutil.ignore_patterns(".git", "node_modules", "__pycache__", "_executed", "*.pptx"))
    subprocess.run([sys.executable, "tools/build_site.py"], cwd=tmp, check=True, capture_output=True)
    subprocess.run([sys.executable, "slides/export_slides.py"], cwd=tmp, check=True, capture_output=True)
    stale = []
    for rel in ["docs", "slides/slides.json"] + [f"slides/week-{i:02d}.md" for i in range(1, 11)]:
        a, b = REPO / rel, tmp / rel
        if a.is_dir():
            cmp = filecmp.dircmp(a, b)
            def walk(c):
                bad = c.diff_files + c.left_only + c.right_only
                stale.extend(str(Path(c.left).relative_to(REPO) / f) for f in bad)
                for sub in c.subdirs.values():
                    walk(sub)
            walk(cmp)
        elif not filecmp.cmp(a, b, shallow=False):
            stale.append(rel)
    for f in stale:
        FAIL.append(f"generated file out of date (re-run the generators): {f}")

if FAIL:
    print("check_sync: FAIL")
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print("check_sync: OK — generators match the design docs and generated files are current")
