#!/usr/bin/env python3
"""
lint-skills.py — Daniels & Washington Skill-Pattern Linter

Validates each `skills/dw-*/SKILL.md` against the established D&W skill pattern.
Hard errors flag structural breakage (missing frontmatter, broken cross-references).
Warnings flag pattern drift (missing standard sections) — useful but not fatal.

Usage:
    bin/lint-skills.py                 # lint all skills, print issues, exit 1 on errors
    bin/lint-skills.py --skill dw-foo  # lint just one skill
    bin/lint-skills.py --errors-only   # suppress warnings
    bin/lint-skills.py --strict        # warnings become errors
    bin/lint-skills.py --quiet         # only print summary line

Exit codes:
    0 — no errors (and, with --strict, no warnings)
    1 — errors present
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# ── Repo layout ─────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

# ── Exemptions ──────────────────────────────────────────────────────────────
# Some skills legitimately diverge from the standard pattern. List the warning
# codes a given skill is exempt from. Errors (E*) are never exempted — those
# represent real structural problems.

EXEMPT: dict[str, set[str]] = {
    "dw-skill-index":         {"W1", "W3", "W4"},                       # index/lookup, no file output
    "dw-template-selector":   {"W1", "W2", "W3", "W4", "W5", "W6"},     # shared protocol, not direct-trigger
    "dw-shared-protocols":    {"W1", "W2", "W3", "W4", "W5", "W6"},     # library other skills load specific files from
    "dw-data-contracts":      {"W1", "W3", "W4", "W6"},                 # schema definitions
    "dw-criminal-defense":    {"W1", "W2", "W3"},                       # master orchestrator; downstream skills enforce hard stops + citations
    "dw-evidence-placeholder":{"W1", "W3"},                             # utility skill
    "dw-image-filename-stamp":{"W1", "W3", "W4"},                       # utility
    "dw-case-brain":          {"W1", "W2", "W3", "W4"},                 # session persistence — internal brain.md, no attorney deliverables
    "dw-criminal-defense.skill": {"W1", "W2", "W3", "W4", "W5", "W6"},  # legacy plugin shape
}

# ── Issue codes ─────────────────────────────────────────────────────────────

ISSUE_DESCRIPTIONS = {
    "E1": "Missing or unparseable YAML frontmatter",
    "E2": "Frontmatter `name` does not match directory name",
    "E3": "Referenced file does not exist on disk",
    "E4": "Referenced dw-* skill does not exist as a directory",
    "W1": "No 'Step 0' / file intake hard stop section found",
    "W2": "No 'Step 0.5' / shared protocols load section found",
    "W3": "No 'Source Citation Mandate' (or equivalent) section found",
    "W4": "No output-path reference ({{CASE_ROOT}} or output-path-formula) found",
    "W5": "Reference file in references/ not mentioned in SKILL.md (orphaned)",
    "W6": "Frontmatter description has no explicit trigger keywords (e.g., 'ALWAYS invoke')",
}

# ── Issue model ─────────────────────────────────────────────────────────────


@dataclass
class Issue:
    code: str
    message: str

    @property
    def is_error(self) -> bool:
        return self.code.startswith("E")


@dataclass
class SkillReport:
    name: str
    path: Path
    issues: list[Issue] = field(default_factory=list)

    def add(self, code: str, detail: str = "") -> None:
        msg = ISSUE_DESCRIPTIONS[code]
        if detail:
            msg = f"{msg} — {detail}"
        self.issues.append(Issue(code=code, message=msg))

    def filtered_issues(self, errors_only: bool, strict: bool) -> list[Issue]:
        skill_exempt = EXEMPT.get(self.name, set())
        out = []
        for i in self.issues:
            if i.code in skill_exempt:
                continue
            if errors_only and not (i.is_error or strict):
                continue
            out.append(i)
        return out


# ── Frontmatter parsing (no PyYAML dependency) ──────────────────────────────

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Lightweight YAML-frontmatter parser. Returns name + description only."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    body = m.group(1)
    out: dict[str, str] = {}
    current_key: str | None = None
    buf: list[str] = []
    for raw in body.splitlines():
        line = raw.rstrip()
        # Top-level key: `key:` or `key: value` (must be unindented)
        m2 = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$", line)
        if m2 and not raw.startswith((" ", "\t")):
            if current_key is not None:
                out[current_key] = " ".join(s.strip() for s in buf).strip()
            current_key = m2.group(1)
            value = m2.group(2).strip()
            buf = [value] if value and value != ">" else []
            continue
        if current_key is not None:
            buf.append(line.strip())
    if current_key is not None:
        out[current_key] = " ".join(s.strip() for s in buf).strip()
    return out


# ── Pattern checks ──────────────────────────────────────────────────────────

# Section detectors — generous regex so minor formatting variations still match.
RE_STEP_0 = re.compile(
    r"step\s*0\b.*(file\s*intake|hard\s*stop)|file\s*intake\s*hard\s*stop",
    re.IGNORECASE,
)
RE_STEP_05 = re.compile(
    r"step\s*0\.5\b.*shared\s*protocols|load\s*shared\s*protocols",
    re.IGNORECASE,
)
RE_CITATION = re.compile(
    r"source\s*citation\s*mandate|citation\s*mandate|every\s+factual\s+\w+\s+must\s+(trace|cite)",
    re.IGNORECASE,
)
RE_OUTPUT_PATH = re.compile(
    r"\{\{\s*CASE_ROOT\s*\}\}|\bCASE_ROOT\b|output-path-formula|output-path-convention",
    re.IGNORECASE,
)
RE_TRIGGERS = re.compile(
    r"ALWAYS\s+invoke|invoke\s+for|trigger\s+(?:phrase|keyword)",
    re.IGNORECASE,
)

# Find file references like `references/foo.md`, `dw-foo/references/bar.md`.
RE_REF_FILE = re.compile(r"`?(?:[\w./-]*?/)?references/([\w.-]+\.md)`?")
# Find skill cross-references like `dw-foo`. Captures preceding char to filter
# out email/domain matches (e.g., billing@dw-criminal.local).
RE_SKILL_REF = re.compile(r"(.?)\b(dw-[a-z][a-z0-9-]*)\b(\.[a-z]+)?")

# Markers indicating a dw- mention is historical (deprecated/merged/renamed),
# not an active routing reference. If any of these appear on the same line,
# the dw- token is skipped.
HISTORICAL_MARKERS = re.compile(
    r"\b(former|deprecated|replaced\s+by|replaces\s+the\s+former|"
    r"incorporates|integrates\s+\S+\s+(?:and\s+\S+\s+)?into|"
    r"consolidates|absorbs|merged\s+into|retired|superseded|"
    r"now\s+part\s+of|legacy|removed|renamed|original\s+dw-|identical\s+to\s+the)\b",
    re.IGNORECASE,
)

# Template placeholders like `dw-foo-[platform]` or `dw-foo[suffix]` are not
# real skill names; skip when the captured token is followed by these.
RE_TEMPLATE_FOLLOWUP = re.compile(r"^[-]?\[")


def lint_skill(skill_dir: Path, all_skill_names: set[str]) -> SkillReport:
    rpt = SkillReport(name=skill_dir.name, path=skill_dir / "SKILL.md")

    if not rpt.path.exists():
        rpt.add("E1", f"{rpt.path.relative_to(REPO_ROOT)} not found")
        return rpt

    text = rpt.path.read_text(encoding="utf-8")

    # E1 / E2 — frontmatter
    fm = parse_frontmatter(text)
    if fm is None:
        rpt.add("E1")
        # Continue with other checks anyway — they may still surface useful info.
    else:
        name_in_fm = fm.get("name", "").strip()
        if name_in_fm and name_in_fm != skill_dir.name:
            rpt.add("E2", f"frontmatter name='{name_in_fm}' but directory='{skill_dir.name}'")
        if not RE_TRIGGERS.search(fm.get("description", "")):
            rpt.add("W6")

    # W1-W4 — standard sections
    if not RE_STEP_0.search(text):
        rpt.add("W1")
    if not RE_STEP_05.search(text):
        rpt.add("W2")
    if not RE_CITATION.search(text):
        rpt.add("W3")
    if not RE_OUTPUT_PATH.search(text):
        rpt.add("W4")

    # E3 — reference files mentioned in SKILL.md must exist
    refs_dir = skill_dir / "references"
    referenced_files = {m.group(1) for m in RE_REF_FILE.finditer(text)}
    for ref in referenced_files:
        if not (refs_dir / ref).exists():
            # Skip cross-skill refs handled below; only flag local refs.
            # If the line that mentioned the ref includes a `dw-` prefix, treat
            # it as cross-skill and skip the local-existence check.
            line_with_ref = next(
                (line for line in text.splitlines() if f"references/{ref}" in line),
                "",
            )
            cross_skill = re.search(r"dw-[a-z0-9-]+/references/" + re.escape(ref), line_with_ref)
            if cross_skill:
                continue
            rpt.add("E3", f"references/{ref}")

    # W5 — orphaned reference files. A file counts as referenced if its full
    # path (`references/X.md`) appears OR its bare filename appears in any
    # markdown-emphasis or code-span style (e.g., `**X.md**`, `\`X.md\``,
    # bullet-list filename mentions in a Quick References section).
    if refs_dir.exists():
        for f in refs_dir.iterdir():
            if not f.is_file() or f.suffix != ".md":
                continue
            if f.name == "README.md":
                continue
            if f.name in referenced_files:
                continue
            # Fallback: bare filename appears anywhere in the SKILL.md
            if f.name in text:
                continue
            rpt.add("W5", f"references/{f.name}")

    # E4 — cross-skill references must resolve. Skip:
    #   - Self-references
    #   - Email/domain matches ('@dw-foo', 'dw-foo.local')
    #   - Hidden directory paths ('.dw-foo' or '~/.dw-foo')
    #   - Template placeholders ('dw-foo-[platform]')
    #   - Historical mentions (line contains "former", "merged into", etc.)
    skill_refs: set[str] = set()
    for line in text.splitlines():
        if HISTORICAL_MARKERS.search(line):
            continue
        for m in RE_SKILL_REF.finditer(line):
            preceding, ref, suffix = m.group(1), m.group(2), m.group(3)
            if preceding in ("@", ".") or suffix:
                continue
            following = line[m.end(2):m.end(2) + 4]
            if RE_TEMPLATE_FOLLOWUP.match(following):
                continue
            skill_refs.add(ref)
    skill_refs.discard(skill_dir.name)
    for ref in sorted(skill_refs):
        # Allow the `.skill` legacy variant to map to the base name.
        if ref in all_skill_names or f"{ref}.skill" in all_skill_names:
            continue
        rpt.add("E4", ref)

    return rpt


# ── Reporting ───────────────────────────────────────────────────────────────


def render_report(reports: list[SkillReport], errors_only: bool, strict: bool, quiet: bool) -> tuple[int, int]:
    total_errors = 0
    total_warnings = 0
    for rpt in reports:
        issues = rpt.filtered_issues(errors_only=errors_only, strict=strict)
        if not issues:
            continue
        if not quiet:
            print(f"\n=== {rpt.name} ({rpt.path.relative_to(REPO_ROOT)}) ===")
        for i in issues:
            severity = "ERROR" if i.is_error else "WARN "
            if i.is_error:
                total_errors += 1
            else:
                total_warnings += 1
            if not quiet:
                print(f"  {severity} {i.code}: {i.message}")
    return total_errors, total_warnings


# ── Entry point ─────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", help="Lint just this skill (directory name).")
    parser.add_argument("--all", action="store_true", help="Lint all skills, not just dw-* (includes 3rd-party utility skills).")
    parser.add_argument("--errors-only", action="store_true", help="Suppress warnings.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors.")
    parser.add_argument("--quiet", action="store_true", help="Only print the summary line.")
    args = parser.parse_args()

    if not SKILLS_DIR.is_dir():
        print(f"skills/ not found at {SKILLS_DIR}", file=sys.stderr)
        return 2

    if args.skill:
        targets = [SKILLS_DIR / args.skill]
        if not targets[0].is_dir():
            print(f"Skill not found: {args.skill}", file=sys.stderr)
            return 2
    else:
        all_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
        if args.all:
            targets = all_dirs
        else:
            targets = [p for p in all_dirs if p.name.startswith("dw-")]

    all_skill_names = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}

    reports = [lint_skill(t, all_skill_names) for t in targets]
    errors, warnings = render_report(reports, args.errors_only, args.strict, args.quiet)

    print(f"\n{len(reports)} skill(s) checked — {errors} error(s), {warnings} warning(s).")

    if errors > 0:
        return 1
    if args.strict and warnings > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
