#!/usr/bin/env python3
"""
Tiny helper: ensure ~/.dw-tracker/config.json exists, copying assets/config.example.json
if not. Print the path. Used by SKILL.md Step 1 so Claude doesn't have to reimplement
the same logic each run.

Usage:
    python config.py --asset-dir /path/to/dw-court-jail-tracker/assets
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--asset-dir", required=True, type=Path)
    args = ap.parse_args()

    config_dir = Path.home() / ".dw-tracker"
    config_dir.mkdir(parents=True, exist_ok=True)
    config_path = config_dir / "config.json"
    example_path = args.asset_dir / "config.example.json"

    created = False
    if not config_path.exists():
        shutil.copy2(example_path, config_path)
        created = True

    cfg = json.loads(config_path.read_text())
    placeholders = [k for k, v in cfg.items() if v == "FILL_ME_IN"]

    print(json.dumps({
        "config_path": str(config_path),
        "created_from_template": created,
        "placeholders_remaining": placeholders,
    }, indent=2))


if __name__ == "__main__":
    main()
