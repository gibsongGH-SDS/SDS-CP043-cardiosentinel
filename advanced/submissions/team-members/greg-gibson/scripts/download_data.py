#!/usr/bin/env python
"""
download_data.py — Reproducible Kaggle dataset fetch

Usage:
  python scripts/download_data.py --dataset <owner/slug> --outdir data/raw --unzip
  Env overrides:
    KAGGLE_DATASET (owner/slug), DATA_OUTDIR (path)

Prereqs:
  1) pip install kaggle
  2) Place kaggle.json in:
      - Windows: %USERPROFILE%\.kaggle\kaggle.json
      - macOS/Linux: ~/.kaggle/kaggle.json
  3) (Optional) keep this token out of git and set chmod 600 on *nix.
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

def check_kaggle_token() -> Path:
    user_home = Path.home()
    if os.name == "nt":
        # Windows
        token_path = user_home / ".kaggle" / "kaggle.json"
    else:
        token_path = user_home / ".kaggle" / "kaggle.json"

    if not token_path.exists():
        raise FileNotFoundError(
            f"Kaggle token not found at {token_path}\n"
            "Create one at https://www.kaggle.com/settings/account "
            "and place 'kaggle.json' in the path above."
        )
    return token_path

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def run(cmd: list[str]):
    print(">", " ".join(cmd))
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise RuntimeError(f"Command failed (exit {result.returncode})")
    return result.stdout

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default=os.getenv("KAGGLE_DATASET", "iamsouravbanerjee/heart-attack-prediction-dataset"),
                        help="Kaggle dataset slug: owner/slug")
    parser.add_argument("--outdir", default=os.getenv("DATA_OUTDIR", "data/raw"),
                        help="Output directory to save files")
    parser.add_argument("--unzip", action="store_true", help="Unzip after download (recommended)")
    args = parser.parse_args()

    dataset = args.dataset
    outdir = Path(args.outdir)
    ensure_dir(outdir)

    print(f"Dataset: {dataset}")
    print(f"Output : {outdir.resolve()}")

    # 1) Validate Kaggle token
    token_path = check_kaggle_token()
    print(f"Found Kaggle token at: {token_path}")

    # 2) Check kaggle CLI availability
    try:
        run(["kaggle", "-v"])
    except Exception:
        raise RuntimeError(
            "The 'kaggle' CLI isn't available. Install it with 'pip install kaggle' "
            "and ensure your shell can find the 'kaggle' command (restart terminal if needed)."
        )

    # 3) Download
    # If a previous zip exists, remove it to avoid confusion
    zip_candidates = list(outdir.glob("*.zip"))
    for z in zip_candidates:
        print(f"Removing old archive: {z}")
        z.unlink(missing_ok=True)

    print("Downloading from Kaggle ...")
    run(["kaggle", "datasets", "download", "-d", dataset, "-p", str(outdir)])

    # 4) Unzip (optional)
    if args.unzip:
        print("Unzipping ...")
        # unzip all zips (some datasets contain multiple zips)
        for z in outdir.glob("*.zip"):
            run(["python", "-m", "zipfile", "-e", str(z), str(outdir)])
            # optional: remove zip to keep folder clean
            z.unlink(missing_ok=True)

    # 5) Summary
    files = [str(p) for p in outdir.rglob("*") if p.is_file()]
    if not files:
        print("Warning: no files found after download.", file=sys.stderr)
    else:
        print("\nFiles fetched:")
        for f in files:
            print(" -", f)

    print("\n✅ Done.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
