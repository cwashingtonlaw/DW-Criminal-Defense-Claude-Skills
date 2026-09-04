---
name: dw-criminal-defense-crim
category: core
description: >
  Master 3-phase criminal defense workflow. ALWAYS invoke for "case intake," "new case,"
  "run Phase 1/2/3," initial case setup, "fill out the LWOP sheet," "LWOP review,"
  "District Defender review," "life without parole worksheet," or "refresh the Case Profile."
  Do NOT use for loading existing case state — use dw-case-brain-crim. Do NOT use for case
  status checks — use dw-case-dashboard-crim. Do NOT use for the client-facing first meeting
  / intake interview — use dw-client-intake-interview-crim (this skill handles the case file
  side; the intake interview skill handles the live client meeting and feeds into Phase 1).
---

# Daniels & Washington — Criminal Defense Cowork Skill
**Version 6.2 | Internal Use Only**

This skill governs all Claude Cowork operations for criminal defense case management at Daniels & Washington. Follow this skill for every task involving a client case file. The 3-phase workflow below is the single source of truth.

For version history, see `CHANGELOG.md` at the skill root.

---
## Bundled Resources

This skill bundles `references/`, `assets/` (`CASE PROFILE.docx`, `Case Tables.xlsx`, `Evidence_Placeholder_Template.md`), and `scripts/generate_placeholders.py`. Read `references/bundled-resources-map.md` now for the directory tree and when-to-load schedule; each step below repeats its own load instruction.

---
## Core Rules (Always Apply)

- **Never create new spreadsheets.** All tabular data goes into the sheets that already exist in `Case Tables.xlsx` at the root of the case folder.
- **Never create new folders** unless a standard subfolder is confirmed missing. See `references/folder-structure-and-naming.md` for the standard structure.
- **Naming convention:** All documents use `[3-digit prefix] - [Document Name].docx` format with **sequential numbering starting at 001** (e.g., `001 - Bill of Information`, `002 - Incident Report`, `003 - Arrest Warrant`). Number documents consecutively with no gaps — do not skip numbers or leave room between entries.
- **Cowork drafts; attorney approves.** Claude prepopulates templates and drafts documents. Attorneys make final decisions and send all external communications.
- **Quality Gates must be confirmed** before advancing to the next phase. Do not proceed if any gate item is unresolved.
- **Louisiana law applies** unless otherwise indicated. Use Louisiana statutes for all charge research, discovery obligations, and citations.
- **Attorney-only fields are sacred.** Any field marked `[ATTORNEY]` in red font must be preserved blank for attorney completion. Cowork never fills these. In Refresh Mode, Cowork never overwrites them.
- **Case Tables write protocol is mandatory.** Before any write to `Case Tables.xlsx`, follow the protocol in `references/case-tables-write-protocol.md` (warn → confirm → write → verify) to prevent Google Drive sync overwrites.

---
## PHASE 1 — Case Intake & Matter Setup

*Triggered the moment a new client engagement is confirmed. This phase covers everything from folder creation through a fully organized, Bate-stamped, searchable case file with a complete Case Profile — the foundation for all analysis in Phase 2.*

### Step 1: Folder Setup

- Read `references/output-path-convention.md` to resolve `CASE_ROOT` (checks Case Brain session → attorney prompt → Cowork project mapping → asks attorney).
- Read `references/folder-structure-and-naming.md` for the full standard folder layout (including Exhibit List, Billing, and Case Closing locations) and the master document/audio/video naming conventions.
- Confirm all standard subfolders exist: `01 - Trial Notebook` (all sub-tabs) and `02 - Pretrial Notebook` (all sub-tabs).
- Locate `Case Tables.xlsx` at the root of the case folder. If this is a new case and no `Case Tables.xlsx` exists, copy the master template from `assets/Case Tables.xlsx` into the case root.
- Do not create new folders unless a standard subfolder is missing.

**✓ Step 1 Check:** Folder structure confirmed, `CASE_ROOT` resolved, `Case Tables.xlsx` located.

### Step 2: Prepare Discovery for Review

*Converts raw discovery into organized, Bate-stamped, searchable files. Folder sorting runs in parallel with OCR — do not wait for OCR to begin sorting.*

Sub-steps in order: **2a** Download & Organize (Download Log) → **2b** Bate-Stamp (`Bate Stamp Master Log.xlsx`) → **2c** Duplicate to `05 - Evidence` (verified copy) → **2d** Separate into numbered documents (Separation Checklist) → **2e** Transcribe via **dw-transcript-router-crim** → **2f** Generate placeholders with `scripts/generate_placeholders.py` (or **dw-evidence-placeholder-crim**).

Read `references/phase1-step2-discovery-prep.md` now for the full 2a–2f procedure, log columns, Bate rules, script invocation, and the 7-item Step 2 Check.

**✓ Step 2 Check:** all seven items in the reference confirmed.

### Step 3: Generate Case Profile

**Output:** `000 - Case Profile.docx` → save to `Pretrial Notebook → 03 - Case Analysis & Notes`
**Source template:** `assets/CASE PROFILE.docx`

Read **`references/case-profile-procedure.md`** now — the full operating manual (both operating modes, JusticeWorks ingest, Part 1 §§ 1–11, Part 2A/2B/2C, LWOP population, Refresh merge rules, roll-up block, XML generation); its appendix holds the scope list and Step 3 Check formerly here.

For the § 4 Responsive Verdicts cell, read `references/art814-responsive-verdict-map.md` and emit the verdict set verbatim (never hand-type). For LWOP cases (Part 2A or 2B in scope), also read `references/lwop-field-maps.md` (field schema) and `references/lwop-extraction-patterns.md` (extraction rules from discovery).

**✓ Step 3 Check:** run the 13-item Step 3 Check in the appendix of `references/case-profile-procedure.md`.

### Step 4: Build Case Tables

⚠ **Follow the Case Tables Write Protocol before modifying this file.** See `references/case-tables-write-protocol.md`.

**Reference:** Read `references/color-coding.md` for the firm's full header and dropdown color specs (hex values for every column, authentication route, witness priority, and timeline tag). Use the `xlsx` skill to apply formatting per those specs.

Populate **4a — Evidence Table** (7 columns; Cowork proposes Sponsoring Witness, Authentication Route, and Anticipated Objections ★, attorney confirms each) and **4b — Witness List** (4 columns, alphabetical, every witness ranked 1–5 per `references/witness-priority-rubric.md`). Column lists and legends are in the reference.

Read `references/phase1-step4-case-tables-population.md` now for the column table, the authentication-route and objection-code legends, Witness List columns, and the Step 4 Check.

**✓ Step 4 Check:** all four items in the reference confirmed.

### ✓ Phase 1 Quality Gate
Read `references/phase-quality-gates.md` now and confirm every Phase 1 item (including case state saved to **dw-case-brain-crim**) before Phase 2.

---

## PHASE 2 — Case Processing & Analysis

*Runs parallel analysis before attorney review. Auto-action loops triggered by Reports 7 and 8 eliminate rework in Phase 3.*

### Step 1: Rapid Triage & Specialist Routing
Scan all documents to produce a **Triage Routing Memo** and early **specialist dispatches** — this step flags and routes; Step 2 analyzes. **1A** Triage Routing Memo (constitutional, Brady/Giglio, witness-inconsistency, timeline-conflict flags) · **1B** Chain of Custody Audit (substantive → **dw-chain-of-custody-auditor-crim**) · **1C** Specialist Evidence Routing (evidence type, read from the file and Download Log → auditor skill) · **1D** Charge-Type Specialist Routing (charge category → offense specialist; multi-domain cases dispatch to all).

Read `references/phase2-step1-triage-and-specialist-routing.md` now for flag-by-flag destinations and the full 1C/1D dispatch lists.

Save all Step 1 outputs to: `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/` subfolder.

### Step 1E — Barone Discovery Workflow Pre-Analysis (New — v5.9)
After Step 1A–1D and before Step 2: **dw-neutral-inventory-crim** (Report 0 — Neutral Inventory), then **dw-theory-deconstructor-crim** (Report 2a — Theory Deconstruction, after Report 2; feeds Report 4). Sequencing detail is in the Step 1 reference.

### Step 2: Generate the 8 Case Analysis Reports
Read `references/case-analysis-prompts.md` for the exact prompt template for each report. That file contains the common analytical framework ("Dream Team" lens), the source citation standard, and per-report instructions. Name each report exactly as shown below. For each report, identify and route specific issues to specialist skills.

| # | Report Name | Output Location | Priority | Skill Routing |
|---|-------------|-----------------|----------|----------------|
| 1 | Comprehensive Case Timeline | `Case Tables.xlsx — Timeline Sheet` ⚠ | Standard | - |
| 2 | Prosecution's Case Summary | `01 - Trial Notebook/09 - Case Analysis/` | Standard | - |
| 3 | Immediate Red Flags | `01 - Trial Notebook/09 - Case Analysis/` | **HIGH ★** | **dw-suppression-motion-crim** (for warrant/search issues); **dw-expert-witness-evaluator-crim** (for expert issues) |
| 4 | Competing Defense Theories | `01 - Trial Notebook/09 - Case Analysis/` | Standard | **dw-theory-deconstructor-crim** (upstream: Report 2a feeds in) |
| 4a | Theory Selection Memo | `01 - Trial Notebook/09 - Case Analysis/` | **HIGH ★** | **dw-theory-to-workplan-crim** (downstream); **dw-adversarial-stress-test-crim** (downstream) |
| 5 | Viable Legal Defenses | `01 - Trial Notebook/09 - Case Analysis/` | Standard | **dw-404b-opposition-crim** (for bad acts); **dw-sentencing-mitigation-specialist-crim** (for sentencing exposure); **dw-habitual-offender-auditor-crim** (for habitual claims) |
| 6 | Memorable Theme | `01 - Trial Notebook/09 - Case Analysis/` | Standard | - |
| 7 | Table of Missing Discovery | `01 - Trial Notebook/09 - Case Analysis/` | **HIGH ★ → Auto-Action** | **dw-brady-giglio-auditor-crim** |
| 8 | Key Witness Impeachment Plan | `01 - Trial Notebook/09 - Case Analysis/` | **HIGH ★ → Auto-Action** | **dw-cross-exam-architect-crim** |

**Bond/Release Issues:** If Report 3 or 5 identifies bond concerns → route to **dw-bond-and-release-motion-crim**
**Plea Negotiations:** If prosecution indicates negotiation interest → route to **dw-plea-negotiation-analyzer-crim**

### Step 2A: Post-Report 4 — Theory Selection & Stress Test (Barone Workflow)
*Triggered after Reports 1-8 are complete. This step bridges analysis to action.*

Attorney selects the primary theory from Report 4; Cowork drafts **Report 4a — Theory Selection Memo** (attorney sign-off required) → `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`, then routes to **dw-adversarial-stress-test-crim** and **dw-theory-to-workplan-crim**. Read `references/phase2-post-report-procedures.md` now for memo contents.

### Step 3: Auto-Action — Report 7 → Missing Discovery Demand Letter
*Triggered immediately upon filing Report 7.*

**Output:** `Missing Discovery Demand — [Date].docx` → save to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

Use the exact boilerplate in `references/textexpander-snippets.md`; drafting steps are in `references/phase2-post-report-procedures.md`. **Attorney must approve before letter is sent.**

### Step 4: Auto-Action — Report 8 → Impeachment Worksheets
*Triggered immediately upon filing Report 8.*

One worksheet per key witness in `Trial Notebook → 03 - Witnesses`, prepopulated from the Evidence Table, Report 8, and transcripts, plus a Witness Dossier cover page; attorney completes Line of Attack, Question Sequence, Anticipated Responses. Fields: `references/phase2-post-report-procedures.md`.

### Step 5: Route Case Analysis to Attorney
Once all 8 reports and auto-actions are complete, email the attorney *"Case Analysis Ready for Review — [Client Name] / [Case Number]"* with the Case Analysis Index; confirm the demand letter awaits approval and all worksheets are filed. Detail: `references/phase2-post-report-procedures.md`.

### Step 6: Auto-Push Attorney Review Checklist to Apple Notes
*Triggered immediately after Step 5. The attorney needs actionable review items in their daily-driver app — not buried in the case folder.*

Generate the **Attorney Review Checklist** (5-business-day deadline, one checkbox per attorney-action deliverable) and push it to Apple Notes via Claude in Chrome; if unavailable, save `Attorney Review Checklist — [Date].md` at the case root and alert the attorney. Read `references/phase2-post-report-procedures.md` now for content, push, and fallback wording.

### ✓ Phase 2 Quality Gate
Read `references/phase-quality-gates.md` now and confirm every Phase 2 item (including case state saved to **dw-case-brain-crim**) before Phase 3.

---

## PHASE 3 — Trial Notebook & Attorney Preparation

*Converts case analysis into actionable trial preparation. Cowork pre-builds all templates; attorneys complete cross and direct exam preparation using the integrated templates.*

Read `references/phase3-trial-prep-procedures.md` now — the complete procedure for Steps 1–11; this skeleton gives order, outputs, and routing. ⚠ Steps 1–3 write to `Case Tables.xlsx`: follow `references/case-tables-write-protocol.md`.

### Step 1: Case Timeline Spreadsheet
From **Report 1** → `Case Tables.xlsx — Timeline Sheet`: 11 columns, strict chronological order, color coding per `references/color-coding.md`, hyperlinked sources, conflicts flagged.

### Step 2: Update Witness List
**Re-rank `Priority`** per `references/witness-priority-rubric.md` using Report 4a and Report 8; update `Key Evidence Sources` with that witness's Bate refs. Impeachment detail, exam-prep status, and rationale live in Report 8 and the witness worksheets. Route → **dw-witness-threat-matrix-crim**; the Report 4a theory drives **dw-jury-instructions-builder-crim** and **dw-voir-dire-assistant-crim** directly.

### Step 3: Version Control — Amended & Superseded Documents
Keep a version control log; mark supersession in the `Evidence Name` cell (`— SUPERSEDED by [Evidence Number]`); never delete prior versions.

### Step 4: Case Readiness Memo
One-page attorney entry point built from all 8 reports, Cowork parallel analysis, and current status.

### Step 5: Discover the Story Worksheet (Case Story Development)
Complete before witness preparation — foundation of the defense narrative.

### Step 6: Cross Exam Preparation (Per Key Witness)
Cowork prepopulates **7A** Battle Card, **7B** Mapping the Cross Worksheet, **7C** Cross Exam Template for Report 8 and Top 10 witnesses; route by witness type → `01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/`.

### Step 7: Direct Exam Preparation (Per Defense Witness)
Cowork prepopulates **8A** Mapping the Direct Worksheet and **8B** Direct Exam Template → `01 - Trial Notebook/03 - Witnesses/Defense Witnesses/`.

### Step 8: Opening Statement & Closing Argument Preparation
Populate Mapping the Story templates from Report 4 (theory per Report 4a), Report 6, and the Discover the Story worksheet.

### Step 9: Appellate Readiness
**dw-appellate-error-monitor-crim** (preservation) → **dw-appellate-brief-builder-crim** (direct appeal) or **dw-post-conviction-relief-crim** (collateral relief).

### Step 10: Trial Day Support
Route in-court support (docket, objection log, scorecards, exhibit tracker, juror/Batson log, recap, issue spotter) to **dw-trial-day-assistant-crim**.

### Step 11: Assemble Trial Notebook
Route to **dw-trial-notebook-builder-crim** for assembly, master index, and Trial Readiness Gap Report.

---

*This skill reflects Daniels & Washington Cowork Workflow Version 6.2 (September 2026). Update this file whenever the master workflow document is revised.*

## Changelog

See `CHANGELOG.md` at the skill root; the condensed v5.2–v5.11 summary formerly here was moved there verbatim.

---

## Quick References

Reference materials in the `references/` subdirectory:

- **art814-responsive-verdict-map.md** — Phase 1 Step 3: all 71 art. 814(A) offenses with verbatim responsive-verdict sets
- **bundled-resources-map.md** — Bundled Resources: directory tree, when-to-load schedule, pointer list
- **case-analysis-prompts.md** — Phase 2 Step 2: the eight report prompt templates and analytical framework
- **case-profile-procedure.md** — Phase 1 Step 3: full Case Profile manual plus appended scope list and Step 3 Check
- **case-tables-write-protocol.md** — Any `Case Tables.xlsx` write: mandatory write protocol
- **color-coding.md** — Phase 1 Step 4, Phase 3 Step 1: color specs for every Case Tables sheet
- **folder-structure-and-naming.md** — Phase 1 Step 1 and any file write: folder tree and naming conventions
- **lwop-extraction-patterns.md** — Phase 1 Step 3 (LWOP): extracting each LWOP field from discovery
- **lwop-field-maps.md** — Phase 1 Step 3 (LWOP): Part 2A/2B field schema and completeness checklist
- **output-path-convention.md** — Phase 1 Step 1 and any file write: `CASE_ROOT` resolution and save paths
- **phase-quality-gates.md** — End of Phases 1 and 2: full quality-gate checklists
- **phase1-step2-discovery-prep.md** — Phase 1 Step 2: full 2a–2f procedure and Step 2 Check
- **phase1-step4-case-tables-population.md** — Phase 1 Step 4: Evidence Table columns, priority/relevance rules, Witness List
- **phase2-step1-triage-and-specialist-routing.md** — Phase 2 Steps 1/1E: triage flags, 1C/1D dispatch lists, Barone pre-analysis
- **phase2-post-report-procedures.md** — Phase 2 Steps 2A/3/4/5/6: theory memo, demand letter, worksheets, attorney email, Apple Notes push
- **phase3-trial-prep-procedures.md** — Phase 3 Steps 1–12: complete trial-prep procedure text
- **quick-reference.md** — Any time: action-type symbols, sheet index, phase map, specialist routing table
- **textexpander-snippets.md** — Phase 2 Step 3: firm boilerplate blocks
- **witness-priority-rubric.md** — Phase 1 Step 4, Phase 3 Step 2: 1–5 witness priority ranking rule

---

*This skill reflects Daniels & Washington Cowork Workflow Version 6.2 (September 2026). Update this file whenever the master workflow document is revised.*
