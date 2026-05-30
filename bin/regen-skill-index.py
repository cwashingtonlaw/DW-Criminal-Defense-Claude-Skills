#!/usr/bin/env python3
"""
regen-skill-index.py — Regenerate dw-skill-index-crim/SKILL.md routing tables.

Eliminates drift between the index's routing tables and the actual contents
of `skills/dw-*/`. Walks every skill directory, parses its YAML frontmatter,
and emits the markdown tables in `skills/dw-skill-index-crim/SKILL.md` from the
config in `bin/skill-index-categories.yml`.

The non-table content of SKILL.md (header, intro, "Quick Lookup" lead, footer
including the changelog) is preserved verbatim — only the table sections are
regenerated, between marker comments the script writes on first run.

Out of scope: regenerating dw-template-selector or dw-criminal-defense-crim — those
have more contextual routing and are still maintained by hand.

Usage:
    bin/regen-skill-index.py            # regenerate in place
    bin/regen-skill-index.py --check    # CI mode: print diff, exit 1 if dirty
    bin/regen-skill-index.py --write    # explicit write (default behavior)

Exit codes:
    0 — index is up to date (or was successfully written)
    1 — --check found differences, OR a config-vs-disk mismatch errored
    2 — usage / IO error
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# Reuse the lint-skills frontmatter parser (no new dependency). The script's
# filename uses a hyphen, so we load it via importlib rather than `import`.
import importlib.util as _importlib_util

_LINT_PATH = Path(__file__).resolve().parent / "lint-skills.py"
_spec = _importlib_util.spec_from_file_location("lint_skills", _LINT_PATH)
if _spec is None or _spec.loader is None:  # pragma: no cover
    raise SystemExit(f"Could not load {_LINT_PATH}")
_lint_skills = _importlib_util.module_from_spec(_spec)
sys.modules["lint_skills"] = _lint_skills  # required for @dataclass to find ns
_spec.loader.exec_module(_lint_skills)
parse_frontmatter = _lint_skills.parse_frontmatter

# Map bare skill name -> plugin namespace, derived from the on-disk layout.
# Only includes plugin-housed skills (plugin is not None); flat skills are absent.
PLUGIN_OF = {d.name: plugin for plugin, d in _lint_skills.discover_skills() if plugin is not None}

def ns(skill_name: str) -> str:
    """Namespaced display name, e.g. dw-pleadings:dw-suppression-motion-crim."""
    p = PLUGIN_OF.get(skill_name)
    return f"{p}:{skill_name}" if p else skill_name

REPO_ROOT = Path(__file__).resolve().parent.parent
_SKILL_DIRS_BY_NAME = {d.name: d for d in _lint_skills.discover_skill_dirs()}
INDEX_PATH = _SKILL_DIRS_BY_NAME["dw-skill-index-crim"] / "SKILL.md"
CONFIG_PATH = Path(__file__).resolve().parent / "skill-index-categories.yml"

# ── Section definitions ─────────────────────────────────────────────────────
# Each section maps a config-key to:
#   - markdown_heading: the heading text on the page (`## ...`)
#   - intro: optional paragraph(s) emitted between the heading and the table
#   - columns: 3 column headings — varies by section
#   - format: which row template to use (most use ("X","Skill","Trigger"))


@dataclass
class SectionSpec:
    key: str
    heading: str
    columns: tuple[str, str, str]
    intro: str = ""
    outro: str = ""
    # If set, the section is emitted verbatim from this string (heading
    # included) instead of being generated from config rows. Used for
    # hand-authored narrative sections like the Barone Discovery Workflow,
    # whose table/structure isn't derived from per-skill frontmatter. The
    # skills it references are still listed in skill-index-categories.yml
    # (Quick Lookup) so the orphan check sees them.
    raw: str = ""


# Hand-authored narrative section emitted verbatim (see SectionSpec.raw). Its
# table/structure isn't derived from per-skill frontmatter, so it lives here as
# a literal block. The skills it references appear in Quick Lookup config rows,
# so the orphan check still sees them.
BARONE_RAW = """## Barone Discovery Workflow — "Run the Barone workflow..."

The Barone Discovery Workflow is a structured 9-step analytical pipeline that extends the standard Phase 2 analysis. It emphasizes theory-neutral initial assessment, structured theory development, and adversarial testing before committing to a defense strategy.

| Step | Report | Skill | Trigger Phrase |
|------|--------|-------|----------------|
| 1 | Report 0 — Neutral Inventory | `dw-neutral-inventory-crim` | "neutral inventory" or "Report 0" |
| 2 | Report 1 — Timeline (with Certainty) | `dw-timeline-builder-crim` | "build the timeline" |
| 3 | Report 2 — Prosecution's Case Summary | `dw-criminal-defense-crim` Phase 2 | "run Phase 2" |
| 4 | Report 2a — Theory Deconstruction | `dw-theory-deconstructor-crim` | "deconstruct the theory" |
| 5 | Report 3 — Red Flags | `dw-criminal-defense-crim` Phase 2 | (auto-generated) |
| 6 | Report 4 — Competing Defense Theories | `dw-criminal-defense-crim` Phase 2 | (auto-generated) |
| 7 | Report 4a — Theory Selection Memo | `dw-criminal-defense-crim` Phase 2 Step 2A | (attorney-driven) |
| 8 | Theory-to-Workplan (7 streams) | `dw-theory-to-workplan-crim` | "build a workplan" |
| 9 | Adversarial Stress Test | `dw-adversarial-stress-test-crim` | "stress test the theory" |

The Barone workflow also adds:
- **Certainty column** to the Timeline Sheet (CONFIRMED / PROBABLE / DISPUTED / UNCONFIRMED / ALLEGED)
- **Discovery Bucket classification** (7 Barone buckets) to the Discovery Compliance Ledger
- **Report-vs-Recording Matrix** (6-category) to all DMARs
- **Verification Protocol** ([VERIFIED] / [UNVERIFIED] flags) across all analytical skills"""


SECTIONS: list[SectionSpec] = [
    SectionSpec(
        key="quick_lookup",
        heading="Quick Lookup — \"I need to...\"",
        columns=("I need to...", "Use this skill", "Say this"),
    ),
    SectionSpec(
        key="barone",
        heading="Barone Discovery Workflow",
        columns=("", "", ""),
        raw=BARONE_RAW,
    ),
    SectionSpec(
        key="evidence_auditing",
        heading="Evidence Auditing — \"Audit the...\"",
        columns=("Evidence Type", "Skill", "Trigger Phrase"),
    ),
    SectionSpec(
        key="motions_pleadings",
        heading="Motions & Pleadings — \"Draft a...\"",
        columns=("Motion Type", "Skill", "Trigger Phrase"),
        outro="All motion skills use the template selection protocol in `dw-shared-protocols-crim/references/` to search DEVONthink for firm templates before drafting.",
    ),
    SectionSpec(
        key="trial_preparation",
        heading="Trial Preparation — \"Prep for trial...\"",
        columns=("Task", "Skill", "Trigger Phrase"),
    ),
    SectionSpec(
        key="sentencing_appeal_pcr",
        heading="Sentencing, Appeal & Post-Conviction — \"After trial...\"",
        columns=("Task", "Skill", "Trigger Phrase"),
    ),
    SectionSpec(
        key="charge_specialists",
        heading="Charge-Type Specialists — \"What's the framework for [charge]...\"",
        columns=("Charge Type", "Skill", "Trigger Phrase"),
        intro=(
            "Each specialist provides charge-specific elements, defenses, "
            "sentencing exposure, motions, and discovery checklists. Routed "
            "to from `dw-criminal-defense-crim` Phase 2 or directly when the charge "
            "type is known."
        ),
    ),
    SectionSpec(
        key="intake_setup",
        heading="Intake & Setup — \"Set up...\"",
        columns=("Task", "Skill", "Trigger Phrase"),
        outro=(
            "*Note: `dw-lwop-populator` was retired in v5.3 — its functionality "
            "merged into `dw-criminal-defense-crim` Phase 1 Step 3.*"
        ),
    ),
    SectionSpec(
        key="shared_references",
        heading="Shared References (Not Direct-Trigger)",
        columns=("Skill", "What It Does", "Read By"),
        intro=(
            "These skills are read by other skills as reference protocols — "
            "you don't invoke them directly:"
        ),
    ),
]

# ── Markers that delimit the auto-generated block in SKILL.md ───────────────
BEGIN_MARKER = "<!-- BEGIN AUTOGEN: routing-tables (regen-skill-index.py) -->"
END_MARKER = "<!-- END AUTOGEN: routing-tables (regen-skill-index.py) -->"


# ── Tiny config parser (no PyYAML) ──────────────────────────────────────────


def parse_config(text: str) -> dict[str, list[dict[str, str]]]:
    """Parse the subset of YAML used by skill-index-categories.yml.

    Recognized shape:

        section_key:
          - skill: dw-foo
            label: "..."
            trigger: "..."
            ...

    Comments (#...) and blank lines are ignored. Strings may be quoted with
    "..." or unquoted (everything after the colon). Multi-line values are NOT
    supported — each key/value lives on one line.
    """
    sections: dict[str, list[dict[str, str]]] = {}
    current_section: str | None = None
    current_entry: dict[str, str] | None = None

    for raw_line in text.splitlines():
        # Strip inline comments only when the # is preceded by whitespace —
        # otherwise we'd mangle values like `mailto:foo#bar`. (None of our
        # values currently contain hashes, but safer this way.)
        line = re.sub(r"\s+#.*$", "", raw_line).rstrip()
        if not line.strip():
            continue
        if line.lstrip().startswith("#"):
            continue

        # New top-level section: `key:` at column 0, no value
        m = re.match(r"^([a-z_][a-z0-9_]*)\s*:\s*$", line)
        if m:
            if current_entry is not None and current_section is not None:
                sections[current_section].append(current_entry)
                current_entry = None
            current_section = m.group(1)
            sections.setdefault(current_section, [])
            continue

        # New list entry: `  - key: value` (the `-` opens a new dict)
        m = re.match(r"^\s+-\s+([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$", line)
        if m:
            if current_entry is not None and current_section is not None:
                sections[current_section].append(current_entry)
            current_entry = {}
            current_entry[m.group(1)] = _strip_quotes(m.group(2).strip())
            continue

        # Continuation key inside the current dict: `    key: value`
        m = re.match(r"^\s+([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$", line)
        if m and current_entry is not None:
            current_entry[m.group(1)] = _strip_quotes(m.group(2).strip())
            continue

    if current_entry is not None and current_section is not None:
        sections[current_section].append(current_entry)

    return sections


def _strip_quotes(s: str) -> str:
    if len(s) >= 2 and ((s[0] == '"' and s[-1] == '"') or (s[0] == "'" and s[-1] == "'")):
        return s[1:-1]
    return s


# ── Trigger-phrase extraction from a skill's frontmatter description ────────

# Match "ALWAYS invoke for ..." up through the run of quoted phrases. Captures
# the full quoted-phrase blob; we then pull individual quoted strings from it.
RE_INVOKE_BLOCK = re.compile(
    r"ALWAYS\s+invoke\s+for\s+(.+?)(?:\.\s|\.$|Do\s+NOT|Read\s|Produces?\s|Covers?\s|Returns?\s|Handles?\s)",
    re.IGNORECASE | re.DOTALL,
)
RE_QUOTED = re.compile(r'"([^"]+)"')


def extract_trigger_phrase(description: str, max_phrases: int = 2) -> str:
    """Extract a short trigger-phrase suggestion from a skill description.

    Strategy: find the "ALWAYS invoke for ..." run, pull the first 1-2 quoted
    phrases from it, join with " or ". Fallback to a placeholder if none found.
    """
    if not description:
        return "[no trigger phrase]"

    # Normalize whitespace so multi-line descriptions parse cleanly.
    normalized = re.sub(r"\s+", " ", description)
    m = RE_INVOKE_BLOCK.search(normalized)
    if not m:
        # Try a softer fallback: pull up to 2 quoted phrases anywhere.
        quotes = RE_QUOTED.findall(normalized)[:max_phrases]
        if quotes:
            return " or ".join(quotes)
        return "[no trigger phrase]"

    quotes = RE_QUOTED.findall(m.group(1))[:max_phrases]
    if not quotes:
        return "[no trigger phrase]"
    return " or ".join(quotes)


# ── Skill loading ───────────────────────────────────────────────────────────


@dataclass
class Skill:
    name: str
    description: str
    path: Path

    def trigger_phrase(self) -> str:
        return extract_trigger_phrase(self.description)


def load_skills() -> dict[str, Skill]:
    """Load name → Skill for every skill directory present (dw-* and others)."""
    out: dict[str, Skill] = {}
    for d in _lint_skills.discover_skill_dirs():
        skill_md = d / "SKILL.md"
        if not skill_md.exists():
            continue
        text = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text) or {}
        out[d.name] = Skill(
            name=d.name,
            description=fm.get("description", ""),
            path=d,
        )
    return out


# ── Markdown emission ───────────────────────────────────────────────────────


def render_table_row(left: str, skill_name: str, trigger: str) -> str:
    skill_cell = f"`{skill_name}`" if not skill_name.startswith("`") else skill_name
    return f"| {left} | {skill_cell} | {trigger} |"


def format_trigger(raw: str) -> str:
    """Render a trigger string in the existing index style: quoted phrases.

    Input may already be quoted (frontmatter pulled `"audit body cam"`) or
    unquoted (`audit body cam or BWC`). We split on " or " / "," at the top
    level and re-emit each phrase wrapped in straight quotes — matching the
    pattern in the existing hand-written index.
    """
    if not raw:
        return raw
    s = raw.strip()
    # If the whole thing is one quoted blob, just return it.
    if s.startswith('"') and s.endswith('"') and s.count('"') == 2:
        return s
    # Strip any pre-existing quotes for normalization.
    parts: list[str] = []
    # Use " or " as primary splitter; handle "X, Y, or Z" style.
    chunks = re.split(r"\s+or\s+", s)
    out_chunks: list[str] = []
    for c in chunks:
        # Sub-split on commas (unless the chunk is a single phrase like
        # "Securus/GTL/ViaPath" with no commas).
        sub = [p.strip() for p in c.split(",") if p.strip()]
        for p in sub:
            p = p.strip().strip('"').strip("'").strip()
            if p:
                out_chunks.append(f'"{p}"')
    return " or ".join(out_chunks)


def render_section(spec: SectionSpec, entries: list[dict[str, str]], skills: dict[str, Skill]) -> str:
    # Verbatim sections (e.g. Barone Discovery Workflow) emit their raw body.
    # Normalize to a single trailing newline so the splice spacing in
    # render_all_sections matches generated sections.
    if spec.raw:
        return spec.raw.rstrip("\n") + "\n"
    lines: list[str] = []
    lines.append(f"## {spec.heading}")
    lines.append("")
    if spec.intro:
        lines.append(spec.intro)
        lines.append("")
    # Header row
    lines.append(f"| {spec.columns[0]} | {spec.columns[1]} | {spec.columns[2]} |")
    lines.append("|" + "|".join("---" for _ in spec.columns) + "|")
    for entry in entries:
        skill_name = entry.get("skill", "")
        label = entry.get("label", skill_name)
        # Optional suffix that gets appended to the skill cell, e.g. " (Module I)".
        # Stored on the entry to avoid hardcoding in the script.
        suffix = entry.get("label_suffix", "")
        # For shared_references, columns are (Skill, What It Does, Read By).
        if spec.key == "shared_references":
            read_by = entry.get("read_by", "—")
            lines.append(f"| `{ns(skill_name)}` | {label} | {read_by} |")
            continue
        # Normal rows: derive trigger from config, falling back to frontmatter.
        trigger = entry.get("trigger")
        if not trigger:
            sk = skills.get(skill_name)
            trigger = sk.trigger_phrase() if sk else "[no trigger phrase]"
        formatted_trigger = format_trigger(trigger)
        # Skill cell: `name` plus any suffix kept OUTSIDE the backticks.
        if suffix:
            skill_cell = f"`{ns(skill_name)}`{suffix}"
        else:
            skill_cell = f"`{ns(skill_name)}`"
        lines.append(f"| {label} | {skill_cell} | {formatted_trigger} |")
    if spec.outro:
        lines.append("")
        lines.append(spec.outro)
    lines.append("")
    return "\n".join(lines)


def render_all_sections(config: dict[str, list[dict[str, str]]], skills: dict[str, Skill]) -> str:
    blocks = [BEGIN_MARKER, ""]
    for i, spec in enumerate(SECTIONS):
        entries = config.get(spec.key, [])
        blocks.append(render_section(spec, entries, skills))
        # Horizontal rule between sections (matches the existing file).
        if i < len(SECTIONS) - 1:
            blocks.append("---")
            blocks.append("")
    blocks.append(END_MARKER)
    return "\n".join(blocks).rstrip() + "\n"


# ── Index file rewriting ────────────────────────────────────────────────────

# The hand-written intro that lives ABOVE the autogen block. We re-inject this
# verbatim if the existing file doesn't already have markers — i.e., on first
# run. After the first run, the markers are present and we leave everything
# above BEGIN_MARKER untouched.
DEFAULT_HEADER = """---
name: dw-skill-index-crim
description: >
  Find the right D&W skill for any task. ALWAYS invoke for "what skills do we have,"
  "which skill handles X," "show me the skills," "skill list," "what can Cowork do,"
  "help me find the right tool," or any question about which D&W skill to use for a
  specific task. Returns a searchable routing table of all D&W skills with trigger
  phrases and use cases.
---

# D&W Skill Index — Find the Right Skill

When the attorney asks which skill to use, or wants to know what's available, present the relevant section of this routing table. Don't dump the entire table unless asked — match the attorney's question to the right category and show that section.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. Note: this is a reference/index skill with no file output — no output path applies.

---

"""

# The hand-written footer below the autogen block.
DEFAULT_FOOTER = """

---

## Can't Find What You Need?

If none of the above matches:
1. **General criminal defense work** → Start with `dw-criminal-defense-crim` — it routes to specialists
2. **New discovery just arrived** → Start with `dw-discovery-orchestrator-crim` — it triages to auditors
3. **Not sure what phase we're in** → Start with `dw-case-dashboard-crim` — it tells you where you are
4. **Something entirely new** → Use `skill-creator` to build a new skill

---

*D&W Skill Index v1.1 — May 2026*

*v1.1 changes: added `dw-client-intake-interview-crim`, `dw-jail-call-analyzer-crim`, `dw-trial-day-assistant-crim`, `dw-appellate-brief-builder-crim`, `dw-violent-crime-specialist-crim`; new "Charge-Type Specialists" section consolidating all five specialists; renamed "Sentencing & Post-Conviction" to "Sentencing, Appeal & Post-Conviction"; surfaced Daubert/Foret hearing day package (Module I) inside `dw-expert-witness-evaluator-crim`; removed retired `dw-lwop-populator` row.*
"""


def assemble_full_file(existing: str, body: str) -> str:
    """Splice the regenerated `body` into `existing`.

    If markers exist, we replace only the content between them (preserving
    everything outside). On first run (no markers) we substitute the default
    header + footer scaffolding so the file gets the markers planted.
    """
    if BEGIN_MARKER in existing and END_MARKER in existing:
        before = existing.split(BEGIN_MARKER, 1)[0]
        after = existing.split(END_MARKER, 1)[1]
        # Normalize spacing around the autogen block: exactly one blank line
        # before BEGIN_MARKER and exactly one blank line after END_MARKER.
        return (
            f"{before.rstrip()}\n\n"
            f"{body.rstrip()}"
            f"\n\n{after.lstrip()}"
        )
    # First run — establish the canonical scaffold.
    return DEFAULT_HEADER + body.rstrip() + "\n" + DEFAULT_FOOTER


# ── Validation ──────────────────────────────────────────────────────────────


def validate(config: dict[str, list[dict[str, str]]], skills: dict[str, Skill]) -> tuple[list[str], list[str]]:
    """Return (errors, warnings).

    Errors:
      - A skill referenced in the config does not exist in skills/ on disk.
    Warnings:
      - A dw-* skill exists on disk but is not referenced anywhere in config.
    """
    errors: list[str] = []
    warnings: list[str] = []

    referenced: set[str] = set()
    for section_key, entries in config.items():
        for entry in entries:
            skill_name = entry.get("skill", "")
            if not skill_name:
                continue
            referenced.add(skill_name)
            # External (non-dw) skills don't need to live in skills/.
            if entry.get("external"):
                continue
            # Skills under dw- must exist as a directory.
            if skill_name.startswith("dw-") and skill_name not in skills:
                errors.append(
                    f"Config section '{section_key}' references skill "
                    f"'{skill_name}', but skills/{skill_name}/ does not exist."
                )

    for skill_name in skills:
        if skill_name in referenced:
            continue
        # Skip non-dw third-party utility skills (file-organizer, etc.) — they
        # aren't part of the D&W index regardless.
        if not skill_name.startswith("dw-"):
            continue
        warnings.append(
            f"Skill '{skill_name}' exists on disk but is not in any section "
            f"of skill-index-categories.yml (orphan)."
        )

    return errors, warnings


# ── Entry point ─────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Print diff and exit 1 if changes would result.")
    mode.add_argument("--write", action="store_true", help="(default) Write regenerated file to disk.")
    args = parser.parse_args()

    # Default mode is --write.
    do_write = not args.check

    if not CONFIG_PATH.exists():
        print(f"Config not found: {CONFIG_PATH}", file=sys.stderr)
        return 2
    config = parse_config(CONFIG_PATH.read_text(encoding="utf-8"))

    skills = load_skills()

    errors, warnings = validate(config, skills)
    for w in warnings:
        print(f"WARN: {w}", file=sys.stderr)
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1

    body = render_all_sections(config, skills)
    if not INDEX_PATH.exists():
        print(f"Index path not found: {INDEX_PATH}", file=sys.stderr)
        return 2
    existing = INDEX_PATH.read_text(encoding="utf-8")
    new_text = assemble_full_file(existing, body)

    if existing == new_text:
        if not args.check:
            print(f"OK — {INDEX_PATH.relative_to(REPO_ROOT)} is already up to date.")
        return 0

    if args.check:
        diff = difflib.unified_diff(
            existing.splitlines(keepends=True),
            new_text.splitlines(keepends=True),
            fromfile=str(INDEX_PATH.relative_to(REPO_ROOT)) + " (current)",
            tofile=str(INDEX_PATH.relative_to(REPO_ROOT)) + " (regenerated)",
        )
        sys.stdout.writelines(diff)
        print(
            f"\nWould rewrite {INDEX_PATH.relative_to(REPO_ROOT)} "
            f"(run without --check to apply).",
            file=sys.stderr,
        )
        return 1

    if do_write:
        INDEX_PATH.write_text(new_text, encoding="utf-8")
        print(f"Wrote {INDEX_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
