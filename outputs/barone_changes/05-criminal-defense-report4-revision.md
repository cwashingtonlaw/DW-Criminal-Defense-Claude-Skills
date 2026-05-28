# Rec 05 — Criminal Defense Report 4 Revision + New Report 4a

## Summary
Rename Report 4 from "Core Defense Narrative" to **"Competing Defense Theories"** and add a new **Report 4a: Theory Selection Memo**. This is the architectural change that enables the downstream Barone skills (stress test, workplan).

## Rationale
Premature commitment to a single defense narrative creates confirmation bias. By presenting multiple competing theories, the attorney makes an informed strategic choice and the team remains open to pivoting as new evidence arrives.

## Files Modified

### 1. `dw-criminal-defense/SKILL.md`
- Version bumped to 5.9
- Phase 2 Step 2 report table: Report 4 renamed, Report 4a added with skill routing
- Added Step 1E (Barone Discovery Workflow Pre-Analysis) — routes to dw-neutral-inventory and dw-theory-deconstructor
- Added Step 2A (Post-Report 4 — Theory Selection & Stress Test) — documents Report 4a workflow and downstream routing
- Phase 3 Step 9: Updated to reference Competing Theories and attorney-selected theory
- Changelog: Added v5.9 entry documenting all Barone changes

### 2. `dw-criminal-defense/references/case-analysis-prompts.md`
- Table of Contents: Report 4 renamed, Report 4a added
- Report 4 prompt: Completely rewritten for competing theories (theory name, summary, evidence, weaknesses, prosecution counter-arguments, viability, compatible defenses, comparative matrix)
- Report 4a prompt: New section — attorney-driven Theory Selection Memo (selected theory, rationale, key evidence, vulnerabilities, critical assumptions, pivot triggers, abandoned theories)

### 3. `dw-criminal-defense/references/defense-shield-procedure.md`
- No structural changes needed — Defense Shield consumes the attorney-selected theory from Report 4a (the selected theory replaces the former "core narrative" as the anchor)
