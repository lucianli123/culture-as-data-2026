#!/usr/bin/env python3
"""
check_compat.py - Layer 1 of the compatibility harness (BUILD-PLAN 4c).

Answers one cheap question in seconds, without running any notebook:
    "Do the pinned packages even have a solution together?"

It does NOT catch numpy-ABI / runtime-import problems - that is Layer 2
(tools/run_notebooks.sh, which executes the notebooks in a Colab-like image).

Usage:
    python tools/check_compat.py
    python tools/check_compat.py --requirements notebooks/requirements.txt \
                                 --constraints notebooks/constraints.txt

Exit code 0 = resolver found a solution. Non-zero = conflict (printed).
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEFAULT_REQ = REPO / "notebooks" / "requirements.txt"
DEFAULT_CON = REPO / "notebooks" / "constraints.txt"


def run(cmd: list[str], cwd: Path | None = None) -> tuple[int, str]:
    print("  $ " + " ".join(cmd) + (f"   (cwd={cwd})" if cwd else ""))
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    return proc.returncode, (proc.stdout + proc.stderr)


def _rel(p: Path) -> str:
    """Use a repo-relative path when possible (robust to spaces in absolute paths)."""
    try:
        return str(p.resolve().relative_to(REPO))
    except ValueError:
        return str(p)


def pip_dry_run(req: Path, con: Path) -> bool:
    """pip's resolver, no install. pip >= 23 supports --dry-run + --report."""
    with tempfile.NamedTemporaryFile("r", suffix=".json", delete=False) as tf:
        report_path = tf.name
    cmd = [
        sys.executable, "-m", "pip", "install",
        "--dry-run", "--ignore-installed",
        "--report", report_path,
        "-r", _rel(req), "-c", _rel(con),
    ]
    code, out = run(cmd, cwd=REPO)
    if code != 0:
        print("\n[pip] resolver FAILED:\n" + out)
        return False
    try:
        report = json.loads(Path(report_path).read_text())
        n = len(report.get("install", []))
        print(f"[pip] resolver OK - {n} packages in a consistent set.")
    except (ValueError, OSError, json.JSONDecodeError):
        print("[pip] resolver OK (exit was clean).")
    finally:
        Path(report_path).unlink(missing_ok=True)
    return True


def uv_compile(req: Path, con: Path):
    """Second opinion: uv's resolver names the exact conflicting pins. Optional."""
    if shutil.which("uv") is None:
        print("[uv] not installed - skipping the second-opinion resolve "
              "(`pip install uv` to enable).")
        return None
    cmd = ["uv", "pip", "compile", _rel(req),
           "--constraint", _rel(con), "--no-header"]
    code, out = run(cmd, cwd=REPO)
    if code != 0:
        print("\n[uv] resolver FAILED:\n" + out)
        return False
    print("[uv] resolver OK.")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--requirements", type=Path, default=DEFAULT_REQ)
    ap.add_argument("--constraints", type=Path, default=DEFAULT_CON)
    args = ap.parse_args()

    if not args.requirements.exists():
        print(f"ERROR: {args.requirements} not found.")
        return 2
    if not args.constraints.exists():
        print(f"ERROR: {args.constraints} not found.")
        return 2

    print(f"Resolving {args.requirements}  (constraints: {args.constraints})\n")

    pip_ok = pip_dry_run(args.requirements, args.constraints)
    print()
    uv_ok = uv_compile(args.requirements, args.constraints)

    print("\n" + "=" * 60)
    if pip_ok and uv_ok is not False:
        print("RESULT: resolver green. The pinned set has a solution.")
        print("Next: tools/run_notebooks.sh (Layer 2) to catch import-time breakage.")
        return 0
    print("RESULT: resolver conflict - fix the pins above before testing notebooks.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
