#!/usr/bin/env python3
"""
add-category-frontmatter.py — add a `category:` field to each D&W skill's YAML frontmatter

The category is preparatory metadata for hypothetical future plugin packaging.
It maps each skill to one of the audit's proposed plugin buckets (core,
intake, discovery, evidence-audit, pleadings, trial-prep, transcription,
disposition, offense-specialists, ops). Claude Code does not validate
frontmatter beyond name + description, so adding this field is safe.

Source of truth: `bin/skill-index-categories.yml` section IDs + the
per-skill OVERRIDES in this script (for skills appearing in multiple
sections, in only quick_lookup, or in uncategorized:).

Usage:
    bin/add-category-frontmatter.py            # apply changes in place
    bin/add-category-frontmatter.py --check    # dry-run; exit 1 if any change needed
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
CONFIG_PATH = REPO_ROOT / "bin" / "skill-index-categories.yml"

# Section ID (in skill-index-categories.yml) -> plugin-aligned category name
SECTION_TO_CATEGORY: dict[str, str] = {
    "quick_lookup":         "",                      # never primary; use the other section
    "evidence_auditing":    "evidence-audit",
    "motions_pleadings":    "pleadings",
    "trial_preparation":    "trial-prep",
    "sentencing_appeal_pcr":"disposition",
    "charge_specialists":   "offense-specialists",
    "intake_setup":         "intake",
    "shared_references":    "core",
    "uncategorized":        "",                      # use override
}

# Per-skill overrides (applied when section mapping is empty or wrong)
OVERRIDES: dict[str, str] = {
    # Orchestrator + infrastructure -> core
    "dw-criminal-defense":              "core",
    "dw-case-brain":                    "core",
    "dw-case-dashboard":                "core",
    "dw-skill-index":                   "core",
    "dw-shared-protocols":              "core",
    "dw-template-selector":             "core",
    "dw-data-contracts":                "core",

    # Discovery
    "dw-discovery-orchestrator":        "discovery",
    "dw-discovery-compliance-monitor":  "discovery",
    "dw-brady-giglio-auditor":          "discovery",

    # Transcription pipeline
    "dw-transcript-router":             "transcription",
    "dw-transcript-pipeline-calcasieu": "transcription",
    "dw-transcript-pipeline-rev":       "transcription",
    "dw-dmar-synthesizer":              "transcription",

    # Trial prep (skills not naturally in trial_preparation routing section)
    "dw-trial-notebook-builder":        "trial-prep",
    "dw-witness-threat-matrix":         "trial-prep",
    "dw-jury-focus-group":              "trial-prep",
    "dw-exhibit-manager":               "trial-prep",
    "dw-timeline-builder":              "trial-prep",

    # Evidence audit (skill in uncategorized but functionally an audit)
    "dw-witness-statement-analyzer":    "evidence-audit",

    # Disposition / case-closing
    "dw-case-disposition":              "disposition",

    # Operational utilities
    "dw-billing-narrative-generator":   "ops",
    "dw-case-law-researcher":           "ops",
    "dw-client-communication-drafter":  "ops",
    "dw-court-jail-tracker":            "ops",
    "dw-image-filename-stamp":          "ops",
    "dw-evidence-placeholder":          "ops",
    "dw-pi-video-generator":            "ops",
}


# Minimal YAML reader for the skill-index-categories.yml file
def parse_categories_yml(text: str) -> dict[str, list[str]]:
    """Returns {section_id: [skill_name, ...]} from the YAML config."""
    sections: dict[str, list[str]] = {}
    current_section: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        # Section header (no indent, ends with ":")
        m = re.match(r"^([a-z_][a-z0-9_]*):\s*$", line)
        if m:
            current_section = m.group(1)
            sections.setdefault(current_section, [])
            continue
        # Skill row: '  - skill: dw-foo'
        m = re.match(r"^\s*-\s*skill:\s*(\S+)", line)
        if m and current_section is not None:
            sections[current_section].append(m.group(1))
    return sections


def determine_category(skill: str, sections: dict[str, list[str]]) -> str:
    """Pick the canonical category for a skill."""
    if skill in OVERRIDES:
        return OVERRIDES[skill]
    # Find every section the skill appears in (excluding quick_lookup)
    candidate_sections = [
        s for s, skills in sections.items()
        if skill in skills and SECTION_TO_CATEGORY.get(s)
    ]
    if candidate_sections:
        # Take first non-empty mapping
        for s in candidate_sections:
            cat = SECTION_TO_CATEGORY.get(s, "")
            if cat:
                return cat
    return ""  # could not determine


# Frontmatter rewriting
FRONTMATTER_RE = re.compile(r"^(---\s*\n)(.*?)(\n---\s*\n)", re.DOTALL)
CATEGORY_LINE_RE = re.compile(r"^category:\s*\S+\s*$", re.MULTILINE)


def upsert_category(skill_md: str, category: str) -> tuple[str, bool]:
    """Insert or update `category: <value>` in the frontmatter.

    Returns (new_text, changed). The line is inserted right after the
    `name:` line for visibility. If a category line already exists with
    the same value, no change. If it differs, update it.
    """
    m = FRONTMATTER_RE.match(skill_md)
    if not m:
        return skill_md, False
    fm_open, fm_body, fm_close = m.group(1), m.group(2), m.group(3)
    rest = skill_md[m.end():]

    # Already present?
    existing = CATEGORY_LINE_RE.search(fm_body)
    new_line = f"category: {category}"
    if existing:
        if existing.group(0).strip() == new_line:
            return skill_md, False
        new_body = CATEGORY_LINE_RE.sub(new_line, fm_body, count=1)
    else:
        # Insert after the `name:` line
        lines = fm_body.split("\n")
        out_lines: list[str] = []
        inserted = False
        for line in lines:
            out_lines.append(line)
            if not inserted and re.match(r"^name:\s*\S", line):
                out_lines.append(new_line)
                inserted = True
        if not inserted:
            # No name line found (shouldn't happen) — prepend
            out_lines.insert(0, new_line)
        new_body = "\n".join(out_lines)

    return fm_open + new_body + fm_close + rest, True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="Dry-run; exit 1 if any change would be made.")
    args = parser.parse_args()

    if not CONFIG_PATH.exists():
        print(f"Config not found: {CONFIG_PATH}", file=sys.stderr)
        return 2

    sections = parse_categories_yml(CONFIG_PATH.read_text(encoding="utf-8"))

    skills = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and p.name.startswith("dw-"))
    changed_count = 0
    skipped: list[str] = []

    for skill_dir in skills:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        category = determine_category(skill_dir.name, sections)
        if not category:
            skipped.append(skill_dir.name)
            continue
        text = skill_md.read_text(encoding="utf-8")
        new_text, changed = upsert_category(text, category)
        if changed:
            changed_count += 1
            if args.check:
                print(f"WOULD UPDATE {skill_dir.name} -> category: {category}")
            else:
                skill_md.write_text(new_text, encoding="utf-8")
                print(f"UPDATED {skill_dir.name} -> category: {category}")

    if skipped:
        print(f"\nSkipped (no category): {', '.join(skipped)}", file=sys.stderr)

    if args.check:
        if changed_count > 0:
            print(f"\n{changed_count} skill(s) would change. Run without --check to apply.", file=sys.stderr)
            return 1
        print(f"\nAll {len(skills)} skills have correct category frontmatter.")
        return 0

    print(f"\nUpdated {changed_count} skill(s); {len(skills) - changed_count - len(skipped)} already correct.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
