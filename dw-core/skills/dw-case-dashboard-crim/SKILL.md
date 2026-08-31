---
name: dw-case-dashboard-crim
category: core
description: >
  Case status dashboard. ALWAYS invoke for "case status," "where do we stand," "what's
  next," "readiness check," or "what phase am I in." Scans client folder for deliverables
  and recommends next steps. Do NOT use for case intake or session loading.
---

# Case Dashboard — Daniels & Washington Criminal Defense

Quickly assess where a case stands in the 4-phase workflow, identify completed deliverables, flag missing items, and surface the exact next steps to move forward.

---

## When to Use This Skill

**Use this skill whenever anyone asks:**
- "What phase is this case in?"
- "What's been done so far?"
- "What's outstanding?"
- "What do we do next?"
- "Is the case ready for trial?"
- "Can we move to the next phase?"
- "Case status / readiness check"
- "What deliverables do we have?"

This skill is the **team status check** — attorneys use it before strategy calls, staff uses it to plan the next sprint, and the client-facing team uses it to track progress.

---

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any case files, status updates, deadline calendars, or new deliverables to be reflected in the dashboard, do not analyze anything yet.**

Your only response must be:
> *"Before I begin — are you uploading any additional case files, status updates, court orders setting new deadlines, or completed deliverables to factor into the dashboard? I'll start the readiness scan only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** Mid-scan discovery of a newly served motion, a recently issued scheduling order, or an updated deliverable would change phase completion logic and next-step recommendations.

---

### Source Citation Mandate

Every factual assertion in the dashboard must trace back to a specific file or folder in the case root. The dashboard guides decision-making about phase progression and next steps; unsourced or speculative status claims lead to missed deadlines and skipped deliverables.

**Citation format:** Cite the file path or location relative to `CASE_ROOT`. Examples:
- `(02 - Pretrial Notebook/03 - Case Analysis & Notes/000 - Initial Case Profile.docx)`
- `(Case Tables.xlsx — Evidence Table, row count: 47)`
- `(01 - Trial Notebook/05 - Evidence/, 12 files present)`
- `(Court Order — Scheduling Order, filed 03/15/2026, p. 1)`

**Multiple-source rule:** When more than one location confirms a status fact, cite all of them — e.g., `(Case Tables.xlsx — Witness Table; 01 - Trial Notebook/03 - Witnesses/, 8 files)`.

**Unsourced assertions:** If a status claim cannot be tied to a documented file or location, mark it `[UNSOURCED — VERIFY WITH ATTORNEY]` so the team knows the dashboard reflects an assumption rather than a confirmed deliverable.

**Where sourcing applies:** All factual content — phase status, deliverable completion, deadline tracking, gap identification. Strategic recommendations and procedural standards follow normal narrative format.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## Workflow

### Step 1: Locate and Scan the Case Folder

1. Ask the user for the **absolute path** to the case root folder (e.g., `/path/to/ClientName_CaseNumber/`)
2. Verify the folder exists and contains the standard D&W structure:
   - `01 - Trial Notebook/` (with subfolders: `01 - Jury Instructions...`, `03 - Witnesses/`, `05 - Evidence/`, `09 - Case Analysis/`)
   - `02 - Pretrial Notebook/` (with subfolders: `01 - Pleadings/`, `02 - Discovery/`, `03 - Case Analysis & Notes/`, `06 - Law & Research/`)
   - `Case Tables.xlsx` at the root

3. If the folder structure is incomplete or missing `Case Tables.xlsx`, **flag this immediately** in the dashboard under "⚠ Workflow Gaps."

### Step 2: Scan Phase 0 Deliverables

Check `02 - Pretrial Notebook → 03 - Case Analysis & Notes` for the Initial Case Profile, Criminal Defense Cover, LWOP Assessment (homicide/sex offense only), and complete folder setup. Read `references/steps-2-5-phase-deliverable-scans.md` now for the deliverable tables and status logic used in Steps 2–5.

### Step 3: Scan Phase 1 Deliverables

Check `01 - Trial Notebook → 05 - Evidence/` and `Case Tables.xlsx` for the Master Evidence Table, evidence folder count, Bate Stamp Log, transcripts, and digital placeholders. Apply the Phase 1 status logic in the Steps 2–5 reference.

### Step 4: Scan Phase 2 Deliverables

Check `01 - Trial Notebook → 09 - Case Analysis/` and `Case Tables.xlsx` for Reports 1–8 (plus 4a Theory Selection Memo), the `Cowork Analysis/` parallel analyses, the Missing Discovery Demand Letter, and Impeachment Worksheets. Table and priorities are in the Steps 2–5 reference.

### Step 4B: Scan for Auditor Skill Outputs (Phase 2)

Scan `Cowork Analysis/` for specialist auditor deliverables by filename keyword; mark N/A where the case has no evidence of that type, missing where evidence exists but no audit was run. Auditor-to-pattern table is in the Steps 2–5 reference.

### Step 4C: Scan for Living Monitors & Pre-Trial Motions

Check for the Case Brain, Discovery Compliance Ledger, Appellate Error Log, and filed motions (suppression, bond, 404(b)) in `01 - Pleadings/`, then apply the Phase 2 status logic from the Steps 2–5 reference.

### Step 5: Scan Phase 3 Deliverables

Check `Case Tables.xlsx` and `01 - Trial Notebook/` for the Timeline Sheet, Witness Lists, Defense Matrix, cross/direct exam prep, Case Readiness Memo, and opening/closing prep; apply the Phase 3 status logic from the Steps 2–5 reference.

### Step 6: Determine Current Phase

Based on Phase 0–3 status:
- **Phase 0 not complete** → Case is in **Intake**
- **Phase 0 complete, Phase 1 not complete** → Case is in **Discovery Processing**
- **Phase 1 complete, Phase 2 not complete** → Case is in **Case Analysis**
- **Phase 2 complete, Phase 3 not complete** → Case is in **Trial Prep**
- **Phase 3 complete** → Case is **Trial-Ready**

### Step 6B: Scan Issue Code Status

Check `Case Tables.xlsx` for an `Issue Codes` sheet (maintained by `dw-issue-code-tracker-crim` v2.0 — 33 codes: 14 Universal + 8 Homicide + 11 Rape/Sexual Assault). If absent, render the "Issue ledger not yet initialized" notice and skip. If present, count rows by Status, group Open codes by category, sort ascending, flag codes Open more than 30 days as STALE. **Read-only; no auto-routing.** Read `references/step-6b-issue-code-scan.md` now for the exact procedure.

### Step 7: Flag Workflow Gaps

Check for and flag any of the following:
- Phase 2 reports exist but Phase 1 Master Evidence Table is missing (discovery not properly organized)
- Phase 3 Defense Matrix populated but Phase 2 Red Flags report missing (risks not assessed)
- Impeachment Worksheets exist but no corresponding witnesses in Master Evidence Table (inconsistency)
- Evidence folder has files but Bate Stamp Log is missing (discovery not stamped)
- Case Tables.xlsx missing entirely (critical blocker)

### Step 8: Identify Recommended Next Steps

Based on current phase and gaps, recommend the exact next skill to invoke (e.g., **dw-criminal-defense-crim** phase re-runs, **dw-suppression-motion-crim**, **dw-brady-giglio-auditor-crim**, **dw-chain-of-custody-auditor-crim**, **dw-cross-exam-architect-crim**, **dw-voir-dire-assistant-crim**, **dw-jury-instructions-builder-crim**). Read `references/step-8-next-step-recommendations.md` now for the phase-by-phase recommendation text.

---

## Dashboard Output Format

**Always produce the dashboard in this exact markdown structure.** Render to console. Optionally save to a `.docx` file if the user requests a written summary. Read `references/dashboard-output-template.md` now and reproduce its structure exactly — Current Status, Phase 0–3 blocks, Issue Code Status, Workflow Gaps & Flags, Recommended Next Steps (with time estimates), Phase Completion Checklist, footer.

---

## Implementation Notes

Read `references/implementation-notes-and-accuracy-tips.md` before scanning — scanning methodology (direct file check, row count, folder scan, substring match), error handling (missing `Case Tables.xlsx` is a critical blocker), Excel sheet parsing, LWOP applicability, and the five accuracy tips (ask for the path first, tolerate naming variations, populate % complete, include time estimates, call out attorney decision points).

---

## Related Skills

- **dw-criminal-defense-crim** — Execute any phase of the 4-phase workflow
- **dw-case-brain-crim** — Load/save persistent case context across sessions
- **dw-issue-code-tracker-crim** — Maintain the case-level issue code ledger (Open/Addressed/N/A). The dashboard reads this ledger read-only; only the tracker writes to it.
- **dw-cross-exam-architect-crim** — Generate cross-examination outlines for witnesses
- **dw-discovery-orchestrator-crim** — Triage and route incoming discovery to auditor skills
- **dw-discovery-compliance-monitor-crim** — Track prosecution disclosure obligations
- **dw-appellate-error-monitor-crim** — Track error preservation throughout proceedings
- **dw-evidence-placeholder-crim** — Generate placeholder PDFs for media evidence folders

---

## Quick References

Reference materials in the `references/` subdirectory:

- **steps-2-5-phase-deliverable-scans.md** — Steps 2, 3, 4, 4B, 4C, 5: deliverable tables, auditor output patterns, living monitors, status logic for Phases 0–3
- **step-6b-issue-code-scan.md** — Step 6B: Issue Codes sheet read procedure, grouping, stale-flag computation, read-only rules
- **step-8-next-step-recommendations.md** — Step 8: phase-by-phase next-skill recommendation text
- **dashboard-output-template.md** — Dashboard Output Format: the exact markdown template for every dashboard
- **implementation-notes-and-accuracy-tips.md** — Implementation Notes: scanning methodology, error handling, Excel parsing, LWOP applicability, accuracy tips

---

## Version
Dashboard Skill v1.2 — Aligned Issue Code Status section with `dw-issue-code-tracker-crim` v2.0 (taxonomy v2 — 14 Universal + 8 Homicide + 11 Rape/Sexual Assault, no code-number gaps) (May 2026)
Dashboard Skill v1.1 — Added Issue Code Status section reading from `dw-issue-code-tracker-crim` ledger (May 2026)
Dashboard Skill v1.0 — Aligned with dw-criminal-defense-crim SKILL.md (February 2026)


Follow shared protocols for output paths (see Step 0.5).
