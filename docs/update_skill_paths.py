#!/usr/bin/env python3
"""
Update SKILL.md files for Daniels & Washington skills.
Changes save/output location paths to match new trial notebook structure.
"""

import os
import sys
import shutil
from pathlib import Path


def backup_file(filepath):
    """Create a backup of the file before editing."""
    backup_path = str(filepath) + ".bak"
    shutil.copy2(str(filepath), backup_path)
    return backup_path


def read_file(filepath):
    """Read file content."""
    with open(str(filepath), 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filepath, content):
    """Write file content."""
    with open(str(filepath), 'w', encoding='utf-8') as f:
        f.write(content)


def find_and_replace(content, old_text, new_text, skill_name):
    """
    Find and replace text, with validation.
    Returns tuple: (success, modified_content, message)
    """
    if old_text not in content:
        return False, content, f"  ❌ Pattern not found"

    if content.count(old_text) > 1:
        return False, content, f"  ⚠️  Pattern found {content.count(old_text)} times (expected 1)"

    modified = content.replace(old_text, new_text)
    return True, modified, f"  ✓ Replaced successfully"


def add_save_path_after_anchor(content, anchor_text, new_path_text, skill_name):
    """
    Find anchor text and add save path after it.
    Looks for the anchor and inserts the new text on the next paragraph.
    Returns tuple: (success, modified_content, message)
    """
    if anchor_text not in content:
        return False, content, f"  ❌ Anchor text not found"

    # Find the position of the anchor
    pos = content.find(anchor_text)

    # Look for the next double newline or end of section
    insert_pos = content.find('\n\n', pos)
    if insert_pos == -1:
        insert_pos = len(content)
    else:
        insert_pos += 1  # Insert after first newline, before second

    # Insert the new path text
    modified = content[:insert_pos] + '\n' + new_path_text + content[insert_pos:]
    return True, modified, f"  ✓ Added save path after anchor text"


# ============================================================================
# DEFINE ALL REPLACEMENTS
# ============================================================================

REPLACEMENTS = {
    # GROUP A: Auditor skills → `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

    "dw-brady-giglio-auditor": [
        {
            "type": "replace",
            "old": "- **Location:** Save to `Pretrial Notebook > 03 - Case Analysis & Notes` per D&W folder conventions",
            "new": "- **Location:** Save to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/` per D&W folder conventions",
            "description": "Change save location to trial notebook"
        }
    ],

    "dw-cell-site-geolocation-auditor": [
        {
            "type": "replace",
            "old": "- **Integrate with D&W workflow.** All audit outputs should reference the firm's standard document naming convention and file to appropriate case folder locations per the dw-criminal-defense skill.",
            "new": "- **Integrate with D&W workflow.** All audit outputs should save to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/` per D&W folder conventions.",
            "description": "Change to explicit save location"
        }
    ],

    "dw-chain-of-custody-auditor": [
        {
            "type": "replace",
            "old": "file to appropriate case folder locations per the dw-criminal-defense skill",
            "new": "save to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`",
            "description": "Change to explicit save location"
        }
    ],

    "dw-child-forensic-interview-auditor": [
        {
            "type": "add_anchor",
            "anchor": "## Using This Skill Effectively",
            "new_path": "**Save to:** `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`",
            "description": "Add save location before final section"
        }
    ],

    "dw-confession-interrogation-auditor": [
        {
            "type": "replace",
            "old": "file to appropriate case folder locations per the dw-criminal-defense skill",
            "new": "save to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`",
            "description": "Change to explicit save location"
        }
    ],

    "dw-crime-scene-auditor": [
        {
            "type": "replace",
            "old": "file to appropriate case folder locations per the dw-criminal-defense skill",
            "new": "save to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`",
            "description": "Change to explicit save location"
        }
    ],

    "dw-expert-witness-evaluator": [
        {
            "type": "replace",
            "old": "file to appropriate case folder locations per the dw-criminal-defense skill",
            "new": "save to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`",
            "description": "Change to explicit save location"
        }
    ],

    "dw-eyewitness-identification-auditor": [
        {
            "type": "replace",
            "old": "file to appropriate case folder locations per the dw-criminal-defense skill",
            "new": "save to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`",
            "description": "Change to explicit save location"
        }
    ],

    "dw-forensic-dump-analyzer": [
        {
            "type": "add_anchor",
            "anchor": "### Full Report",
            "new_path": "**Save to:** `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`",
            "description": "Add save location after full report section"
        }
    ],

    "dw-habitual-offender-auditor": [
        {
            "type": "add_anchor",
            "anchor": "### Output 2: Habitual Offender Bill Response / Challenge Motion (.docx)",
            "new_path": "**Save to:** `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`",
            "description": "Add save location near output section"
        }
    ],

    "dw-mobile-forensic-auditor": [
        {
            "type": "replace",
            "old": "file to appropriate case folder locations per the dw-criminal-defense skill",
            "new": "save to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`",
            "description": "Change to explicit save location"
        }
    ],

    "dw-sex-offense-specialist": [
        {
            "type": "add_anchor",
            "anchor": "## FINAL ANALYSIS FRAMEWORK",
            "new_path": "**Save to:** `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`",
            "description": "Add save location near final framework section"
        }
    ],

    "dw-social-media-auditor": [
        {
            "type": "add_anchor",
            "anchor": "## Guardrails",
            "new_path": "**Save to:** `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`\n",
            "description": "Add save location before guardrails section"
        }
    ],

    "dw-sqlite-recovery": [
        {
            "type": "add_anchor",
            "anchor": "## Guardrails",
            "new_path": "**Save to:** `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`\n",
            "description": "Add save location before guardrails section"
        }
    ],

    "dw-video-evidence-auditor": [
        {
            "type": "replace",
            "old": "file to appropriate case folder locations per the dw-criminal-defense skill",
            "new": "save to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`",
            "description": "Change to explicit save location"
        }
    ],

    "dw-appellate-error-monitor": [
        {
            "type": "add_anchor",
            "anchor": "## WORKFLOW SUMMARY",
            "new_path": "**Save to:** `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`\n",
            "description": "Add save location before workflow summary section"
        }
    ],

    "dw-plea-negotiation-analyzer": [
        {
            "type": "add_anchor",
            "anchor": "## OUTPUT FORMAT",
            "new_path": "**Save to:** `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`",
            "description": "Add save location near output format section"
        }
    ],

    "dw-defense-investigator-tasking": [
        {
            "type": "add_anchor",
            "anchor": "## OUTPUT FORMAT",
            "new_path": "**Save to:** `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`",
            "description": "Add save location near output format section"
        }
    ],

    # GROUP B: Other specific paths

    "dw-jury-instructions-builder": [
        {
            "type": "add_anchor",
            "anchor": "## OUTPUT",
            "new_path": "**Save to:** `01 - Trial Notebook/01 - Jury Instructions & Selection/`",
            "description": "Add save location near output section"
        }
    ],

    "dw-voir-dire-assistant": [
        {
            "type": "add_anchor",
            "anchor": "## Guardrails",
            "new_path": "**Save to:** `01 - Trial Notebook/01 - Jury Instructions & Selection/`\n",
            "description": "Add save location before guardrails section"
        }
    ],

    "dw-sentencing-mitigation-specialist": [
        {
            "type": "add_anchor",
            "anchor": "## OUTPUT",
            "new_path": "**Save to:** `01 - Trial Notebook/08 - Verdict_Sentencing/`",
            "description": "Add save location near output section"
        }
    ],

    "dw-discovery-orchestrator": [
        {
            "type": "replace",
            "old": "OUTPUT LOCATION:\n  [Case Root] / 02 - Pretrial Notebook / 03 - Case Analysis & Notes / Cowork Analysis",
            "new": "OUTPUT LOCATION:\n  [Case Root] / 01 - Trial Notebook / 09 - Case Analysis",
            "description": "Change primary save location to trial notebook"
        },
        {
            "type": "replace",
            "old": "- **Specify output location** (e.g., `Case Root / 02 - Pretrial Notebook / 03 - Case Analysis & Notes / Cowork Analysis`)",
            "new": "- **Specify output location** (e.g., `Case Root / 01 - Trial Notebook / 09 - Case Analysis / Cowork Analysis`)",
            "description": "Update example output location in handoff instructions"
        },
        {
            "type": "replace",
            "old": "Output location for all auditor findings: `[Case Root] / 02 - Pretrial Notebook / 03 - Case Analysis & Notes / Cowork Analysis/`",
            "new": "Output location for all auditor findings: `[Case Root] / 01 - Trial Notebook / 09 - Case Analysis / Cowork Analysis/`",
            "description": "Update auditor findings output location reference"
        }
    ],

    "dw-discovery-compliance-monitor": [
        {
            "type": "add_anchor",
            "anchor": "## Guardrails",
            "new_path": "**Save to:** `01 - Trial Notebook/09 - Case Analysis/`\n",
            "description": "Add explicit save location before guardrails"
        }
    ],

    "dw-evidence-placeholder": [
        {
            "type": "add_anchor",
            "anchor": "## Notes",
            "new_path": "**Save to:** `01 - Trial Notebook/05 - Evidence/`\n",
            "description": "Add save location before final notes section"
        }
    ],

    "dw-cross-exam-architect": [
        {
            "type": "replace",
            "old": "- **Location:** Same folder as the cross-examination outline (typically `Trial Notebook → 03 - Witnesses`)",
            "new": "- **Location:** Same folder as the cross-examination outline (typically `01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/`)",
            "description": "Change to explicit path with prosecution witnesses subfolder"
        }
    ],

    # GROUP C: dw-criminal-defense — SKIPPED (already has correct paths)
}


def main():
    """Main function to process all skills."""
    if len(sys.argv) > 1:
        skills_dir = sys.argv[1]
    else:
        skills_dir = os.path.expanduser("~/.claude/skills")

    skills_dir = Path(skills_dir)

    if not skills_dir.exists():
        print(f"Error: Skills directory not found: {skills_dir}")
        sys.exit(1)

    print(f"\n{'='*70}")
    print(f"Updating SKILL.md files for Daniels & Washington Skills")
    print(f"{'='*70}")
    print(f"Skills directory: {skills_dir}\n")

    results = {
        "success": [],
        "partial": [],
        "failed": []
    }

    for skill_name, changes in REPLACEMENTS.items():
        skill_path = skills_dir / skill_name / "SKILL.md"

        if not skill_path.exists():
            print(f"⚠️  {skill_name}: File not found at {skill_path}")
            results["failed"].append(skill_name)
            continue

        print(f"\n📝 Processing: {skill_name}")

        # Create backup
        backup_path = backup_file(skill_path)
        print(f"   Backup created: {backup_path}")

        # Read file
        content = read_file(skill_path)
        modified = False
        partial = False

        # Apply changes
        for i, change in enumerate(changes, 1):
            if change["type"] == "replace":
                success, content, msg = find_and_replace(
                    content,
                    change["old"],
                    change["new"],
                    skill_name
                )
                print(f"   [{i}/{len(changes)}] {change['description']}")
                print(f"       {msg}")
                if success:
                    modified = True
                else:
                    partial = True

            elif change["type"] == "add_anchor":
                success, content, msg = add_save_path_after_anchor(
                    content,
                    change["anchor"],
                    change["new_path"],
                    skill_name
                )
                print(f"   [{i}/{len(changes)}] {change['description']}")
                print(f"       {msg}")
                if success:
                    modified = True
                else:
                    partial = True

        # Write file if modified
        if modified:
            write_file(skill_path, content)
            if partial:
                print(f"   ⚠️  PARTIAL: Some changes applied with warnings")
                results["partial"].append(skill_name)
            else:
                print(f"   ✅ COMPLETE: All changes applied successfully")
                results["success"].append(skill_name)
        else:
            print(f"   ❌ FAILED: No changes could be applied")
            results["failed"].append(skill_name)

    # Summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    print(f"✅ Successful: {len(results['success'])} skills")
    for skill in results["success"]:
        print(f"   • {skill}")

    if results["partial"]:
        print(f"\n⚠️  Partial: {len(results['partial'])} skills (with warnings)")
        for skill in results["partial"]:
            print(f"   • {skill}")

    if results["failed"]:
        print(f"\n❌ Failed: {len(results['failed'])} skills")
        for skill in results["failed"]:
            print(f"   • {skill}")

    print(f"\n{'='*70}")
    total = len(results["success"]) + len(results["partial"])
    print(f"Total processed: {total}/{len(REPLACEMENTS)}")
    print(f"{'='*70}\n")

    return 0 if not results["failed"] else 1


if __name__ == "__main__":
    sys.exit(main())
