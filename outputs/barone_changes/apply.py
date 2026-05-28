#!/usr/bin/env python3
"""
apply.py — Apply the Barone Discovery Workflow Audit deliverables to the D&W skill suite.

Per memory/dw_skills_layout.md the firm maintains three identical skill locations:
    1. GitHub repo                 — path set by DW_GITHUB_REPO
    2. ~/.claude/skills/           — path set by DW_CLAUDE_SKILLS (default: $HOME/.claude/skills)
    3. iCloud Claude Skills folder — path set by DW_ICLOUD_SKILLS

This script sequences the 10 audit deliverables in dependency order, copies the
new skills and reference file automatically, and walks you through the five
textual edit-specs with backup + post-apply verification.

Run order is mandatory:
    09  verification-protocol.md             ← referenced by everything below
    02  timeline Certainty column            ← pure addition, no deps
    08  discovery-compliance Bucket column   ← pure addition, no deps
    03  DMAR 6-category matrix               ← affects 4 skills + data contracts
    05  Report 4 / 4a revision               ← load-bearing for new skills below
    01  dw-neutral-inventory                 ← new skill
    04  dw-theory-deconstructor              ← new skill
    06  dw-theory-to-workplan                ← new skill (depends on 05's Report 4a)
    07  dw-adversarial-stress-test           ← new skill (depends on 05's Report 4a)
    10  dw-skill-index updates               ← last; references everything above

Usage examples:
    python3 apply.py --check                       # validate config, no changes
    python3 apply.py --dry-run                      # show every action, no changes
    python3 apply.py --apply                       # apply everything
    python3 apply.py --apply --only 02             # apply just recommendation #02
    python3 apply.py --apply --skip 05             # apply everything except #05
    python3 apply.py --verify                      # post-apply verification only

Environment variables (set these in your shell before running):
    DW_GITHUB_REPO     Path to GitHub repo skills/ root            (REQUIRED)
    DW_CLAUDE_SKILLS   Path to ~/.claude/skills root               (default: $HOME/.claude/skills)
    DW_ICLOUD_SKILLS   Path to iCloud Claude Skills root           (REQUIRED)

Safety guarantees:
    - Every modified file is backed up to <file>.bak.<timestamp> before edit.
    - guided_edit waits for explicit user confirmation and verifies the file
      changed before recording success.
    - Any failure halts the run; partial progress is reported.
    - --dry-run never writes to disk in any location.
"""

from __future__ import annotations

import argparse
import datetime as dt
import filecmp
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

STAGING_DIR = Path(__file__).resolve().parent
DEFAULT_CLAUDE_SKILLS = Path.home() / ".claude" / "skills"
TIMESTAMP = dt.datetime.now().strftime("%Y%m%d-%H%M%S")

APPLY_ORDER = ["09", "02", "08", "03", "05", "01", "04", "06", "07", "10"]


@dataclass
class Recommendation:
    rec_id: str
    name: str
    rec_type: str
    source: str | None = None
    target_path: str | None = None
    skill_name: str | None = None
    integration_notes: str | None = None
    spec_file: str | None = None
    target_files: list[str] = field(default_factory=list)


RECS: dict[str, Recommendation] = {
    "01": Recommendation(
        rec_id="01",
        name="NEW SKILL: dw-neutral-inventory (Report 0 — pre-strategic inventory)",
        rec_type="copy_new_skill",
        skill_name="dw-neutral-inventory",
        source="01-dw-neutral-inventory/SKILL.md",
        integration_notes="01-dw-neutral-inventory/integration-notes.md",
    ),
    "02": Recommendation(
        rec_id="02",
        name="ENHANCEMENT: dw-timeline-builder — add Certainty column (HIGHEST VALUE)",
        rec_type="guided_edit",
        spec_file="02-timeline-builder-edits.md",
        target_files=[
            "dw-timeline-builder/SKILL.md",
            "dw-criminal-defense/SKILL.md",
            "dw-criminal-defense/references/color-coding.md",
            "dw-data-contracts/SKILL.md",
        ],
    ),
    "03": Recommendation(
        rec_id="03",
        name="ENHANCEMENT: DMAR 6-category Report-vs-Recording matrix across 4 skills + data contracts",
        rec_type="guided_edit",
        spec_file="03-dmar-schema-edits.md",
        target_files=[
            "dw-data-contracts/SKILL.md",
            "dw-video-evidence-auditor/SKILL.md",
            "dw-transcript-pipeline-calcasieu/SKILL.md",
            "dw-transcript-pipeline-rev/SKILL.md",
            "dw-dmar-synthesizer/SKILL.md",
        ],
    ),
    "04": Recommendation(
        rec_id="04",
        name="NEW SKILL: dw-theory-deconstructor (Report 2a — facts/inferences/assumptions)",
        rec_type="copy_new_skill",
        skill_name="dw-theory-deconstructor",
        source="04-dw-theory-deconstructor/SKILL.md",
        integration_notes="04-dw-theory-deconstructor/integration-notes.md",
    ),
    "05": Recommendation(
        rec_id="05",
        name="REVISION: dw-criminal-defense Report 4 → Competing Theories + new Report 4a Theory Selection Memo",
        rec_type="guided_edit",
        spec_file="05-criminal-defense-report4-revision.md",
        target_files=[
            "dw-criminal-defense/SKILL.md",
            "dw-criminal-defense/references/case-analysis-prompts.md",
            "dw-criminal-defense/references/defense-shield-procedure.md",
        ],
    ),
    "06": Recommendation(
        rec_id="06",
        name="NEW SKILL: dw-theory-to-workplan (orchestrator — explodes selected theory into 7-stream plan)",
        rec_type="copy_new_skill",
        skill_name="dw-theory-to-workplan",
        source="06-dw-theory-to-workplan/SKILL.md",
        integration_notes="06-dw-theory-to-workplan/integration-notes.md",
    ),
    "07": Recommendation(
        rec_id="07",
        name="NEW SKILL: dw-adversarial-stress-test (prosecutor red-team + defense response)",
        rec_type="copy_new_skill",
        skill_name="dw-adversarial-stress-test",
        source="07-dw-adversarial-stress-test/SKILL.md",
        integration_notes="07-dw-adversarial-stress-test/integration-notes.md",
    ),
    "08": Recommendation(
        rec_id="08",
        name="ENHANCEMENT: dw-discovery-compliance-monitor — add Discovery Bucket column (Barone 7 buckets)",
        rec_type="guided_edit",
        spec_file="08-discovery-compliance-monitor-edits.md",
        target_files=[
            "dw-discovery-compliance-monitor/SKILL.md",
            "dw-criminal-defense/references/case-analysis-prompts.md",
        ],
    ),
    "09": Recommendation(
        rec_id="09",
        name="NEW REFERENCE: dw-shared-protocols/references/verification-protocol.md ([VERIFIED]/[UNVERIFIED] flags)",
        rec_type="copy_reference",
        source="09-verification-protocol.md",
        target_path="dw-shared-protocols/references/verification-protocol.md",
        integration_notes="09-integration-notes.md",
    ),
    "10": Recommendation(
        rec_id="10",
        name="UPDATE: dw-skill-index — add new skill rows + Barone 9-Step Workflow section + Phase 2 table updates",
        rec_type="guided_edit",
        spec_file="10-skill-index-updates.md",
        target_files=[
            "dw-skill-index/SKILL.md",
            "dw-criminal-defense/SKILL.md",
        ],
    ),
}


class Log:
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    BLUE = "\033[34m"
    DIM = "\033[2m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    @staticmethod
    def info(msg: str) -> None:
        print(f"{Log.BLUE}[INFO]{Log.RESET} {msg}")

    @staticmethod
    def ok(msg: str) -> None:
        print(f"{Log.GREEN}[ OK ]{Log.RESET} {msg}")

    @staticmethod
    def warn(msg: str) -> None:
        print(f"{Log.YELLOW}[WARN]{Log.RESET} {msg}")

    @staticmethod
    def err(msg: str) -> None:
        print(f"{Log.RED}[FAIL]{Log.RESET} {msg}", file=sys.stderr)

    @staticmethod
    def section(msg: str) -> None:
        print(f"\n{Log.BOLD}═══ {msg} ═══{Log.RESET}")

    @staticmethod
    def dim(msg: str) -> None:
        print(f"{Log.DIM}{msg}{Log.RESET}")


@dataclass
class Locations:
    github: Path
    claude: Path
    icloud: Path

    def all(self) -> list[Path]:
        return [self.github, self.claude, self.icloud]

    def labels(self) -> list[tuple[str, Path]]:
        return [
            ("GitHub repo", self.github),
            ("~/.claude/skills", self.claude),
            ("iCloud Claude Skills", self.icloud),
        ]


def resolve_locations() -> Locations:
    github = os.environ.get("DW_GITHUB_REPO")
    claude = os.environ.get("DW_CLAUDE_SKILLS", str(DEFAULT_CLAUDE_SKILLS))
    icloud = os.environ.get("DW_ICLOUD_SKILLS")

    missing = []
    if not github:
        missing.append("DW_GITHUB_REPO")
    if not icloud:
        missing.append("DW_ICLOUD_SKILLS")
    if missing:
        Log.err(f"Required environment variables not set: {', '.join(missing)}")
        Log.dim("  Example:")
        Log.dim('    export DW_GITHUB_REPO="$HOME/dev/dw-skills"')
        Log.dim('    export DW_ICLOUD_SKILLS="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Claude Skills"')
        Log.dim('    export DW_CLAUDE_SKILLS="$HOME/.claude/skills"  # optional, has default')
        sys.exit(2)

    return Locations(
        github=Path(github).expanduser().resolve(),
        claude=Path(claude).expanduser().resolve(),
        icloud=Path(icloud).expanduser().resolve(),
    )


def check_locations(locs: Locations) -> bool:
    ok = True
    for label, path in locs.labels():
        if not path.exists():
            Log.err(f"{label}: {path} does not exist")
            ok = False
        elif not path.is_dir():
            Log.err(f"{label}: {path} is not a directory")
            ok = False
        elif not os.access(path, os.W_OK):
            Log.err(f"{label}: {path} is not writable")
            ok = False
        else:
            Log.ok(f"{label}: {path}")
    return ok


def backup_file(path: Path, dry_run: bool) -> Path | None:
    if not path.exists():
        return None
    bak = path.with_suffix(path.suffix + f".bak.{TIMESTAMP}")
    if dry_run:
        Log.dim(f"        (dry-run) would back up: {path} → {bak.name}")
        return bak
    shutil.copy2(path, bak)
    Log.dim(f"        backup: {bak.name}")
    return bak


def action_copy_new_skill(rec: Recommendation, locs: Locations, dry_run: bool) -> bool:
    assert rec.skill_name and rec.source
    src = STAGING_DIR / rec.source
    if not src.exists():
        Log.err(f"  source missing: {src}")
        return False

    Log.dim(f"  source: {src.relative_to(STAGING_DIR)}")
    for label, root in locs.labels():
        dest_dir = root / rec.skill_name
        dest_file = dest_dir / "SKILL.md"
        if dest_file.exists():
            Log.warn(f"  {label}: {dest_file.relative_to(root)} already exists — overwriting (backup created)")
            backup_file(dest_file, dry_run)
        else:
            Log.dim(f"  {label}: will create {dest_file.relative_to(root)}")
        if not dry_run:
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest_file)
            Log.ok(f"  {label}: wrote {dest_file.relative_to(root)}")
    return True


def action_copy_reference(rec: Recommendation, locs: Locations, dry_run: bool) -> bool:
    assert rec.source and rec.target_path
    src = STAGING_DIR / rec.source
    if not src.exists():
        Log.err(f"  source missing: {src}")
        return False

    Log.dim(f"  source: {src.relative_to(STAGING_DIR)}")
    for label, root in locs.labels():
        dest = root / rec.target_path
        if dest.exists():
            Log.warn(f"  {label}: {dest.relative_to(root)} already exists — overwriting (backup created)")
            backup_file(dest, dry_run)
        else:
            Log.dim(f"  {label}: will create {dest.relative_to(root)}")
        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            Log.ok(f"  {label}: wrote {dest.relative_to(root)}")
    return True


def action_guided_edit(rec: Recommendation, locs: Locations, dry_run: bool, non_interactive: bool) -> bool:
    assert rec.spec_file and rec.target_files
    spec = STAGING_DIR / rec.spec_file
    if not spec.exists():
        Log.err(f"  spec missing: {spec}")
        return False

    Log.dim(f"  spec: {spec}")
    Log.dim(f"  targets per location ({len(rec.target_files)} file(s)):")
    for tgt in rec.target_files:
        Log.dim(f"    - {tgt}")

    if dry_run:
        Log.info("  (dry-run) Would back up each target file and prompt for manual edit.")
        return True

    Log.section(f"BACKUP — rec {rec.rec_id}")
    for label, root in locs.labels():
        for tgt in rec.target_files:
            full = root / tgt
            if full.exists():
                backup_file(full, dry_run)
            else:
                Log.warn(f"  {label}: target {full.relative_to(root)} does not exist (skipping)")

    if non_interactive:
        Log.warn("  --non-interactive set; recording backups and skipping confirmation. Apply manually later.")
        return True

    editor = os.environ.get("EDITOR")
    print()
    Log.info(f"Open the edit spec and apply its BEFORE/AFTER blocks to the target files in all THREE locations:")
    Log.dim(f"    spec → {spec}")
    print()
    for label, root in locs.labels():
        print(f"    {Log.BOLD}{label}:{Log.RESET}")
        for tgt in rec.target_files:
            full = root / tgt
            marker = "" if full.exists() else " [does not exist — skip]"
            print(f"      → {full}{marker}")
        print()

    if editor:
        Log.dim(f"  Tip: '{editor} {spec}' to open the spec.")

    while True:
        ans = input(f"  Type 'applied' once you've applied rec {rec.rec_id} to all three locations (or 'skip' to defer): ").strip().lower()
        if ans in ("applied", "skip"):
            break
        Log.warn("  please type 'applied' or 'skip'")

    if ans == "skip":
        Log.warn(f"  rec {rec.rec_id} skipped; no verification performed.")
        return True

    Log.section(f"VERIFY — rec {rec.rec_id}")
    all_ok = True
    for label, root in locs.labels():
        for tgt in rec.target_files:
            full = root / tgt
            bak = full.with_suffix(full.suffix + f".bak.{TIMESTAMP}")
            if not full.exists() or not bak.exists():
                continue
            if filecmp.cmp(full, bak, shallow=False):
                Log.warn(f"  {label}: {full.relative_to(root)} IDENTICAL to backup — no edit detected")
                all_ok = False
            else:
                Log.ok(f"  {label}: {full.relative_to(root)} changed (verified)")
    if not all_ok:
        Log.warn(f"  Some targets show no change. Review and re-apply, or accept (e.g. if the spec didn't actually touch every listed file in this rec).")
    return True


def verify_run(locs: Locations) -> bool:
    Log.section("POST-APPLY VERIFICATION")
    expected_skills = [
        "dw-neutral-inventory/SKILL.md",
        "dw-theory-deconstructor/SKILL.md",
        "dw-theory-to-workplan/SKILL.md",
        "dw-adversarial-stress-test/SKILL.md",
        "dw-shared-protocols/references/verification-protocol.md",
    ]
    all_ok = True
    for label, root in locs.labels():
        Log.info(f"{label}: {root}")
        for rel in expected_skills:
            full = root / rel
            if full.exists():
                Log.ok(f"  {rel}")
            else:
                Log.err(f"  MISSING: {rel}")
                all_ok = False
    return all_ok


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Validate config (env vars + locations) and exit.")
    mode.add_argument("--dry-run", action="store_true", help="Print every planned action without writing anything.")
    mode.add_argument("--apply", action="store_true", help="Apply changes (with backups + verification).")
    mode.add_argument("--verify", action="store_true", help="Run post-apply verification only.")

    p.add_argument("--only", action="append", default=[], help="Apply only the listed recommendation(s).")
    p.add_argument("--skip", action="append", default=[], help="Skip the listed recommendation(s).")
    p.add_argument("--non-interactive", action="store_true", help="In --apply mode, perform backups for guided_edit recs but skip the manual-edit prompt.")

    args = p.parse_args()

    Log.section("CONFIG")
    locs = resolve_locations()
    if not check_locations(locs):
        return 2

    if args.check:
        Log.ok("Config valid. Locations all reachable.")
        return 0

    if args.verify:
        return 0 if verify_run(locs) else 1

    plan = [r for r in APPLY_ORDER if (not args.only or r in args.only) and r not in args.skip]
    if not plan:
        Log.err("Nothing to do (--only / --skip filter excluded everything).")
        return 2

    Log.section(f"PLAN — {len(plan)} recommendation(s), dependency-ordered")
    for rid in plan:
        Log.info(f"  {rid}  {RECS[rid].name}")
    if args.dry_run:
        Log.warn("DRY-RUN mode — nothing will be written.")

    fail_count = 0
    for rid in plan:
        rec = RECS[rid]
        Log.section(f"REC {rid} — {rec.rec_type}")
        Log.info(rec.name)
        try:
            if rec.rec_type == "copy_new_skill":
                ok = action_copy_new_skill(rec, locs, args.dry_run)
            elif rec.rec_type == "copy_reference":
                ok = action_copy_reference(rec, locs, args.dry_run)
            elif rec.rec_type == "guided_edit":
                ok = action_guided_edit(rec, locs, args.dry_run, args.non_interactive)
            else:
                Log.err(f"  unknown rec_type: {rec.rec_type}")
                ok = False
            if rec.integration_notes:
                notes_path = STAGING_DIR / rec.integration_notes
                if notes_path.exists():
                    Log.dim(f"  integration notes: {notes_path}")
            if not ok:
                fail_count += 1
                Log.err(f"  rec {rid} reported failure; halting.")
                break
        except Exception as e:
            fail_count += 1
            Log.err(f"  rec {rid} raised {type(e).__name__}: {e}")
            break

    Log.section("SUMMARY")
    completed = plan[: len(plan) - fail_count] if fail_count else plan
    Log.info(f"Completed: {len(completed)} / {len(plan)}")
    for rid in completed:
        Log.ok(f"  {rid}  {RECS[rid].name}")
    if fail_count:
        skipped = plan[len(completed):]
        for rid in skipped:
            Log.err(f"  {rid}  NOT APPLIED  {RECS[rid].name}")
        return 1

    if not args.dry_run:
        Log.section("NEXT STEPS")
        print("  1. Run final verification:")
        print(f"       python3 {Path(__file__).name} --verify")
        print("  2. Commit the GitHub repo location:")
        print(f"       cd '{locs.github}' && git add -A && git commit -m 'Barone Discovery Workflow Audit — apply v5.9 (2026-05-28)'")
        print("  3. Smoke-test by invoking one of the new trigger phrases in a fresh Cowork session, e.g.:")
        print("       \"neutral inventory\"          (rec 01)")
        print("       \"deconstruct the state's theory\"  (rec 04)")
        print("       \"stress test the theory\"     (rec 07)")
        print("  4. Backups are tagged .bak.{}; delete after a clean week of usage.".format(TIMESTAMP))

    return 0


if __name__ == "__main__":
    sys.exit(main())
