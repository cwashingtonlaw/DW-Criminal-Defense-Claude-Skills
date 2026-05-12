---
name: dw-criminal-defense
description: >
  Master 3-phase criminal defense workflow. ALWAYS invoke for "case intake," "new case,"
  "run Phase 1/2/3," initial case setup, "fill out the LWOP sheet," "LWOP review,"
  "District Defender review," "life without parole worksheet," or "refresh the Case Profile."
  Do NOT use for loading existing case state — use dw-case-brain. Do NOT use for case
  status checks — use dw-case-dashboard.
---

# Daniels & Washington — Criminal Defense Cowork Skill
**Version 5.8 | Internal Use Only**

This skill governs all Claude Cowork operations for criminal defense case management at Daniels & Washington. Follow this skill for every task involving a client case file. The 3-phase workflow below is the single source of truth.

For version history, see `CHANGELOG.md` at the skill root.

---

## Bundled Resources

This skill includes bundled files organized into three directories. Load them as needed — they are not all required at once.

```
dw-criminal-defense/
├── SKILL.md                              ← You are here
├── CHANGELOG.md                          ← Version history
├── references/
│   ├── case-profile-procedure.md         ← Phase 1 Step 3 detailed procedure (operating modes, Part 1/2A/2B/2C field detail, LWOP population, Refresh Mode, XML edit)
│   ├── case-tables-write-protocol.md     ← Mandatory write protocol for Case Tables.xlsx (sync-conflict prevention)
│   ├── case-analysis-prompts.md          ← Phase 2 Step 2: all 8 report prompt templates
│   ├── defense-shield-procedure.md       ← Phase 3 Step 3 detailed procedure (Defense Shield + Defense Matrix + Running List)
│   ├── output-path-convention.md         ← CASE_ROOT resolution, phase folders, file naming
│   ├── lwop-field-maps.md                ← Field schema for Part 2A (Homicide) and Part 2B (Sex Offense) of Case Profile
│   ├── lwop-extraction-patterns.md       ← How to extract each LWOP field from discovery
│   ├── color-coding.md                   ← Spreadsheet color specs for all Case Tables sheets
│   ├── folder-structure-and-naming.md    ← Standard case folder structure + document naming conventions
│   ├── quick-reference.md                ← Cowork action types, sheet index, phase quick map, specialist skill routing
│   └── Evidence_Placeholder_Template.md  ← Layout spec for digital evidence placeholder PDFs (read by Claude; script hardcodes layout)
├── assets/
│   ├── CASE PROFILE.docx                 ← Master Case Profile template (Part 1 + case-type Parts 2A/2B/2C)
│   └── Case Tables.xlsx                  ← Master spreadsheet template (copy to new case roots)
└── scripts/
    └── generate_placeholders.py          ← Generates one-page placeholder PDFs for media evidence folders
```

**When to load each resource:**
- **Phase 1 Step 1 (new case):** Read `references/output-path-convention.md` to resolve `CASE_ROOT`. Copy `assets/Case Tables.xlsx` to the case root if not already present.
- **Phase 1 Step 2f:** Run `scripts/generate_placeholders.py` against the evidence directory.
- **Phase 1 Step 3 (Case Profile):** Read `references/case-profile-procedure.md`. For LWOP cases (Part 2A or 2B), also read `references/lwop-field-maps.md` and `references/lwop-extraction-patterns.md`.
- **Phase 1 Step 4 / Phase 3 Step 1 (Case Tables population):** Read `references/case-tables-write-protocol.md` before any write. Read `references/color-coding.md` for formatting specs.
- **Phase 2 Step 2 (8 reports):** Read `references/case-analysis-prompts.md` for the exact prompt templates.
- **Phase 3 Step 3 (Defense Shield):** Read `references/defense-shield-procedure.md`.
- **Any file-write step:** Consult `references/output-path-convention.md` for the canonical save path and `references/folder-structure-and-naming.md` for folder/naming standards.
- **For sheet index, action-type symbols, or specialist skill routing:** see `references/quick-reference.md`.

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
- Confirm all standard subfolders exist per `references/folder-structure-and-naming.md` — `01 - Trial Notebook` (all sub-tabs) and `02 - Pretrial Notebook` (all sub-tabs).
- Locate `Case Tables.xlsx` at the root of the case folder. If this is a new case and no `Case Tables.xlsx` exists, copy the master template from `assets/Case Tables.xlsx` into the case root.
- Do not create new folders unless a standard subfolder is missing.

**✓ Step 1 Check:** Folder structure confirmed, `CASE_ROOT` resolved, `Case Tables.xlsx` located.

### Step 2: Prepare Discovery for Review

*Converts raw discovery into organized, Bate-stamped, searchable files. Folder sorting runs in parallel with OCR — do not wait for OCR to begin sorting.*

**2a — Download & Organize Discovery**
- Sort all downloaded files into `01 - Pleadings` and `02 - Discovery` subfolders in the Pretrial Notebook.
- Move audio/video files to `05 - Evidence` in the Trial Notebook only — no duplicates.
- Generate a **Download Log**: date received, production set name, file count, total pages (estimated).
- Flag image-only PDFs (need OCR) vs. text-searchable PDFs.
- **Staff action (parallel):** Run OCR on all flagged image-only PDFs using Adobe Acrobat Professional, PDF Expert, or ScanSnap.

**2b — Bate-Stamp Documents**
**Maintain:** `Bate Stamp Master Log.xlsx` as the single source of truth.

Log columns: Production Set | Date Received | Start Number | End Number | Staff Member | Date Stamped

Rules:
- Sequential numbering in order received. Never restart mid-case. Continuous across all production dates.
- Before any new stamping: check log for current highest number, output the next available.
- After stamping: update log immediately — no batch updates.
- Flag any numbering gap — alert staff before proceeding.
- Flag any overlap (duplicate numbers) — halt until resolved.

**2c — Duplicate Discovery to Evidence Folder**
- Copy all Bate-stamped, OCR'd documents to `05 - Evidence` in the Trial Notebook.
- Run file count and size comparison between source and destination.
- Flag any file that failed to copy or shows a size mismatch.
- Do not proceed to 2d until copy is 100% verified.

**2d — Separate Discovery into Individual Documents**
- Review the State's index to identify document divisions and names.
- Split the combined PDF into individual files at the State's document boundaries.
- Apply naming convention: `[3-digit prefix] - [Document Name]` with sequential numbering starting at `001` (e.g., `001 - Bill of Information`, `002 - Incident Report`). Assign the next consecutive number to each document — never skip numbers.
- Create subfolders for multi-file audio/video using the same sequential number (e.g., `008 - Body Camera Footage/`).
- Output a **Separation Checklist**: expected document count (from State index) vs. actual file count.
- Flag any document in the State's index with no corresponding file — log in Report 7 queue.

**2e — Transcribe Interviews & Digital Media**
Route to **dw-transcript-router** for parish-based pipeline selection (JusticeText for Calcasieu, Rev for all other parishes). The router handles upload, transcription, TranscriptPad import, and Defense Media Analysis Report generation.
- When transcripts return: name each transcript PDF identically to its audio/video file, save in the same folder.
- Add transcript as a separate row in the Evidence Table (Evidence Type: Transcript).
- Confirm every audio/video file has a corresponding transcript before proceeding.

**2f — Digital Evidence Handling — Generate Placeholders**
Media folders (photos, videos, audio, surveillance, body cam footage) cannot be Bate-stamped like documents. Each media folder needs a **Digital Evidence Placeholder** — a one-page PDF that sits in the evidence sequence and describes the folder's contents. Optionally route complex media analysis to **dw-evidence-placeholder** skill for full inventory generation.

**Run the bundled generator script:**
```bash
python3 <skill-directory>/scripts/generate_placeholders.py \
  --evidence-dir "<path-to-05-Evidence>" \
  [--folders "folder1" "folder2" ...]  # optional: specific folders only
```

If `--folders` is omitted, the script processes all subfolders automatically. The script scans each subfolder for file counts, types, and size; classifies contents by media type (Audio, Photo/Image, Video, Other Data); generates a one-page PDF placeholder matching the firm's template layout (defined in `references/Evidence_Placeholder_Template.md`); and names each PDF identically to its source folder.

**Workflow:**
- Identify every subfolder in `05 - Evidence` that contains media files
- Confirm scope with user — default to processing all folders unless told otherwise
- Skip folders that already have a corresponding placeholder PDF (use `--force` to regenerate)
- After running, report: total placeholders created, any folders skipped, breakdown by media type

**✓ Step 2 Check:**
- [ ] File count in Evidence Folder matches downloaded discovery
- [ ] Bate Stamp Log shows no gaps or overlaps
- [ ] All image-only PDFs have been OCR'd and confirmed text-searchable
- [ ] No documents in the State's index are absent from the Evidence Folder
- [ ] Separation Checklist: expected count = actual count
- [ ] Every audio/video file has a corresponding transcript entry
- [ ] Digital Evidence Placeholder PDF exists for every media folder in `05 - Evidence`

### Step 3: Generate Case Profile

**Output:** `000 - Case Profile.docx` → save to `Pretrial Notebook → 03 - Case Analysis & Notes`
**Source template:** `assets/CASE PROFILE.docx`

Read **`references/case-profile-procedure.md`** for the full operating manual. That file covers:
- The two operating modes (Initial Generation vs. Refresh)
- Part 1 (always populated) — six sections of Case Identification, Charges, Arraignment, Defenses, Background, Key Dates
- Part 2 (case-type specific) — 2A LWOP Homicide, 2B LWOP Sex Offense, or 2C Other Felony
- LWOP population workflow with extraction priority order, sourcing rules, and formatting conventions
- Attorney-only field handling (red font preservation)
- Refresh Mode merge rules
- Field-completeness checklist and completion notes
- Generation procedure (XML edit using the docx skill)

For LWOP cases (Part 2A or 2B in scope), also read `references/lwop-field-maps.md` (field schema) and `references/lwop-extraction-patterns.md` (extraction rules from discovery).

**✓ Step 3 Check:**
- [ ] Operating mode selected (Initial Generation or Refresh)
- [ ] `000 - Case Profile.docx` saved to `Pretrial Notebook → 03 - Case Analysis & Notes`
- [ ] Part 1 sections 1–6 populated (Initial Generation) OR existing Part 1 preserved (Refresh)
- [ ] Exactly one of Part 2A, 2B, or 2C selected based on charges
- [ ] If LWOP: every field in `lwop-field-maps.md` for the active branch is present (field-completeness checklist run)
- [ ] All `[ATTORNEY]` fields preserved in red
- [ ] Refresh Mode only: attorney-entered content untouched, Refresh Log appended
- [ ] Completion notes generated

### Step 4: Build Case Tables

⚠ **Follow the Case Tables Write Protocol before modifying this file.** See `references/case-tables-write-protocol.md`.

Populate three sheets in `Case Tables.xlsx`. Do not create new sheets — use the existing ones. Maintain all existing color coding, dropdown lists, and formatting per `references/color-coding.md`. The Case Profile (Step 3) provides the charge and defense context needed for accurate assessment of all columns.

**4a — Evidence Table**
Populate the **Evidence Table Sheet** with the full discovery catalog, including analysis columns.

| # | Column | How Populated |
|---|--------|---------------|
| 1 | Doc # | Auto — file name prefix (3-digit) |
| 2 | Evidence Type | Auto — file type + content; Transcript listed separately from A/V |
| 3 | Name | Auto — file name (must match 3-digit convention) |
| 4 | Description | Staff — brief content summary |
| 5 | Bate Stamp | Auto — cross-referenced to Bate Stamp Log |
| 6 | Reviewed (Y/N) | Staff / Attorney — updated after document review |
| 7 | Notes | Staff / Attorney — key observations and flags |
| 8 | Discovery Set | Auto — from Download Log |
| 9 | Date of Delivery | Auto — from Download Log |
| 10 | Review Priority ★ | **Cowork** — AI assessment: HIGH / MED / LOW |
| 11 | Defense Relevance ★ | **Cowork** — AI preliminary, attorney confirms: FAVORABLE / NEUTRAL / FLAG |

**Review Priority rules:**
- HIGH: all audio/video, all interviews, incident reports, lab reports, prior bad acts
- MED: supplemental reports, witness statements, photographs
- LOW: administrative documents, chain of custody logs, return of service

**Defense Relevance rules:**
- FAVORABLE: documents suggesting innocence, inconsistency, or constitutional violation
- FLAG: documents suggesting suppression issues, Brady material, or missing items
- NEUTRAL: all other documents

*Attorney must review all FAVORABLE and FLAG items before Phase 2. Cowork's assessment is preliminary — attorney confirmation required on all AI assessments.*

**4b — Witness Table – Priority** (`Witness List - Priority` sheet)
Extract every witness name encountered during discovery organization and transcription. Sort by witness impact on case outcome. Cross-reference against Case Profile defenses to identify which witnesses are central to the identified defense theories or the prosecution's burden of proof.

Importance ranking: Key Witness > Eyewitnesses > Law Enforcement > Character Witnesses > Others

Columns: Name | Witness Type | Association | Sources (Bate stamps) | Trial Exam Prepared (Y/N)

Bold-mark any witness who appears in multiple documents, gives conflicting statements, or is central to identified defense theories as **KEY WITNESS**.

**4c — Witness Table – Alpha** (`Witness List - Alpha` sheet)
Same data as 4b, sorted alphabetically. Standard reference list for quick lookup.

**✓ Step 4 Check:**
- [ ] Evidence Table row count matches file count in Evidence Folder
- [ ] Review Priority populated for every row in Evidence Table
- [ ] Defense Relevance populated for every row in Evidence Table
- [ ] Witness Table – Priority populated, ranked, and cross-referenced against Case Profile
- [ ] Witness Table – Alpha populated and sorted

### ✓ Phase 1 Quality Gate
Before proceeding to Phase 2, confirm all step checks are complete:
- [ ] Folder structure confirmed — all standard subfolders exist (Step 1)
- [ ] Discovery fully organized, Bate-stamped, OCR'd, transcribed, and placeholders generated (Step 2)
- [ ] `000 - Case Profile.docx` complete with all auto-populated fields (Step 3) — including Part 2A/2B for any LWOP case
- [ ] All Case Tables populated — Evidence Table (all 11 columns), Witness Tables (Priority and Alpha) (Step 4)
- [ ] Case state saved to **dw-case-brain** — Phase 1 complete, ready for Phase 2

---

## PHASE 2 — Case Processing & Analysis

*Runs parallel analysis before attorney review. Auto-action loops triggered by Reports 7 and 8 eliminate rework in Phase 3.*

### Step 1: Rapid Triage & Specialist Routing
Before the 8 Case Analysis Reports are generated, scan all case documents to produce two deliverables: a **Triage Routing Memo** and early **specialist skill dispatches**. The purpose of this step is speed — get routing decisions to specialist skills fast so they can begin working in parallel while the full reports are being written. This step flags and routes; the reports (Step 2) analyze in depth.

**1A — Triage Routing Memo**
Quickly scan all discovery documents and produce a short routing memo that identifies which documents need specialist attention. The memo is a working document for Cowork's internal use — not a deliverable to the attorney. It contains routing decisions, not analysis.

For each flag below, list the specific documents (by name and Bate stamp) and the routing destination. Do not write analysis — just identify and route:
- **Constitutional flags:** documents suggesting 4th, 5th, or 6th Amendment concerns → route to **dw-suppression-motion** *(Report 3 will provide the full analysis)*
- **Brady/Giglio flags:** material potentially favorable to the defense that may not have been disclosed → route to **dw-brady-giglio-auditor** *(Report 7 will provide the full table)*
- **Witness inconsistency flags:** witnesses who appear in multiple documents with conflicting accounts → flag for **Report 8** *(Report 8 will provide the full impeachment plan)*
- **Timeline conflict flags:** events with conflicting dates, times, or sequences across documents → flag for **Report 1** *(Report 1 will build the authoritative timeline)*

**1B — Chain of Custody Audit**
This is substantive analysis, not triage — no report covers this domain. Verify that each piece of physical evidence has an unbroken custody log from collection to present. Flag any gaps, undocumented transfers, or missing logs. Route findings to **dw-chain-of-custody-auditor**.

**1C — Specialist Evidence Routing**
Classify evidence by type and dispatch to the appropriate specialist skill for early analysis. Specialist skills can begin their work in parallel while the 8 reports are being generated in Step 2.

- Eyewitness identification issues → **dw-eyewitness-identification-auditor**
- Confession/interrogation issues → **dw-confession-interrogation-auditor**
- Cell phone forensics → **dw-mobile-forensic-auditor** then **dw-forensic-dump-analyzer**
- Video evidence analysis → **dw-video-evidence-auditor**
- Cell site/location data → **dw-cell-site-geolocation-auditor**
- Social media evidence → **dw-social-media-auditor**
- Child forensic interviews → **dw-child-forensic-interview-auditor**
- Expert witness issues → **dw-expert-witness-evaluator**

Save all Step 1 outputs to: `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/` subfolder.

### Step 2: Generate the 8 Case Analysis Reports
Read `references/case-analysis-prompts.md` for the exact prompt template for each report. That file contains the common analytical framework ("Dream Team" lens), the source citation standard, and per-report instructions. Name each report exactly as shown below. For each report, identify and route specific issues to specialist skills.

| # | Report Name | Output Location | Priority | Skill Routing |
|---|-------------|-----------------|----------|----------------|
| 1 | Comprehensive Case Timeline | `Case Tables.xlsx — Timeline Sheet` ⚠ | Standard | - |
| 2 | Prosecution's Case Summary | `01 - Trial Notebook/09 - Case Analysis/` | Standard | - |
| 3 | Immediate Red Flags | `01 - Trial Notebook/09 - Case Analysis/` | **HIGH ★** | **dw-suppression-motion** (for warrant/search issues); **dw-expert-witness-evaluator** (for expert issues) |
| 4 | Core Defense Narrative | `01 - Trial Notebook/09 - Case Analysis/` | Standard | - |
| 5 | Viable Legal Defenses | `01 - Trial Notebook/09 - Case Analysis/` | Standard | **dw-404b-opposition** (for bad acts); **dw-sentencing-mitigation-specialist** (for sentencing exposure); **dw-habitual-offender-auditor** (for habitual claims) |
| 6 | Memorable Theme | `01 - Trial Notebook/09 - Case Analysis/` | Standard | - |
| 7 | Table of Missing Discovery | `01 - Trial Notebook/09 - Case Analysis/` | **HIGH ★ → Auto-Action** | **dw-brady-giglio-auditor** |
| 8 | Key Witness Impeachment Plan | `01 - Trial Notebook/09 - Case Analysis/` | **HIGH ★ → Auto-Action** | **dw-cross-exam-architect** |

**Bond/Release Issues:** If Report 3 or 5 identifies bond concerns → route to **dw-bond-and-release-motion**
**Plea Negotiations:** If prosecution indicates negotiation interest → route to **dw-plea-negotiation-analyzer**

### Step 3: Auto-Action — Report 7 → Missing Discovery Demand Letter
*Triggered immediately upon filing Report 7.*

**Output:** `Missing Discovery Demand — [Date].docx` → save to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

- Extract every item listed in Report 7's data table.
- Draft a formal demand letter addressed to the prosecution citing Brady/Giglio obligations.
- List each missing item with description and why it is material to the defense.
- Include Louisiana statutory citations for discovery disclosure requirements.
- **Attorney must approve before letter is sent.**

### Step 4: Auto-Action — Report 8 → Impeachment Worksheets
*Triggered immediately upon filing Report 8.*

Create one Impeachment Worksheet per key witness in `Trial Notebook → 03 - Witnesses`:
- **Prepopulate:** witness name, role, all document references (Bate stamps) from Evidence Table
- **Prepopulate:** all impeachment material from Report 8 for that witness
- **Prepopulate:** all prior statements from transcripts with Bate stamp references
- **Add:** Witness Dossier cover page consolidating everything known about this witness
- **Leave blank (attorney completes):** Line of Attack, Question Sequence, Anticipated Responses

### Step 5: Route Case Analysis to Attorney
Once all 8 reports and auto-action documents are complete:
- Draft attorney email: *"Case Analysis Ready for Review — [Client Name] / [Case Number]"*
- Attach Case Analysis Index listing all 8 reports + Cowork Analysis findings
- Confirm Missing Discovery Demand Letter is ready for attorney approval
- Confirm all Impeachment Worksheets are filed and ready for Phase 3

### Step 6: Auto-Push Attorney Review Checklist to Apple Notes
*Triggered immediately after Step 5. The attorney needs actionable review items in their daily-driver app — not buried in the case folder.*

After completing all 8 reports and auto-actions, Cowork generates an **Attorney Review Checklist** and pushes it to Apple Notes. This ensures the attorney sees the checklist where they actually work, with a clear deadline.

**Checklist content** (auto-generated from Phase 2 outputs):
- Title: `Attorney Review Checklist — [Matter Name] ([YYYY-MM-DD])`
- Deadline: 5 business days from creation date
- One checkbox item per attorney-action deliverable:
  - Missing Discovery Demand Letter (review, sign, send)
  - Report 3 Red Flags (prioritize HIGH items for motion practice)
  - Report 5 Legal Defenses (decide which motions to file)
  - Report 6 Memorable Theme (confirm or select alternative)
  - Impeachment Worksheets (complete Line of Attack, Question Sequence, Anticipated Responses)
  - Expert Witness retention (child psych, SANE, forensic interview)
  - Any outstanding discovery demands from Report 7
- Footer: `Generated by Cowork — Daniels & Washington`

**Push procedure** (via Claude in Chrome):
1. Navigate to `https://www.icloud.com/notes/`
2. Wait for iCloud Notes to load (user must be logged into iCloud in Chrome)
3. Click the "New Note" button to create a new note
4. Type the same title and checklist content
5. Apple Notes on iCloud supports checklist formatting — use the checklist button in the toolbar

**Fallback behavior (important — Chrome may not always be connected):**
If Claude in Chrome is not available or Apple Notes is unreachable:
1. Save the checklist as `Attorney Review Checklist — [Date].md` at the case root
2. Log the failed push in the Quality Gate
3. Alert the attorney: *"Review checklist saved locally — Chrome automation was unavailable for Apple Notes. Connect Claude in Chrome and re-run Step 6 to push."*

The reason for the fallback is that Claude in Chrome requires the browser extension to be installed and connected, which isn't always the case. The local markdown file ensures the checklist is never lost, even if the push fails.

### ✓ Phase 2 Quality Gate
Before proceeding to Phase 3, confirm:
- [ ] All 8 reports named correctly and saved to correct locations
- [ ] Triage Routing Memo, Chain of Custody Audit, and Specialist Evidence Routing complete — all outputs saved to Cowork Analysis subfolder
- [ ] Missing Discovery Demand Letter drafted and ready for attorney approval
- [ ] Impeachment Worksheet exists for every witness named in Report 8
- [ ] Witness Dossier cover page exists for every key witness
- [ ] Attorney notified via email with Case Analysis Index
- [ ] Attorney Review Checklist pushed to Apple Notes (or fallback .md saved at case root)
- [ ] Case state saved to **dw-case-brain** — Phase 2 complete, ready for Phase 3

---

## PHASE 3 — Trial Notebook & Attorney Preparation

*Converts case analysis into actionable trial preparation. Cowork pre-builds all templates; attorneys complete cross and direct exam preparation using the integrated templates.*

### Step 1: Case Timeline Spreadsheet
Built from **Report 1** (Comprehensive Case Timeline) → `Case Tables.xlsx — Timeline Sheet`

⚠ **Follow the Case Tables Write Protocol.** See `references/case-tables-write-protocol.md`.

Columns to populate: Start Date | Start Time | End Date | End Time | Title | Subtitle | Description | Tags (Cowork Flags) | Bate Stamp | Notes

Rules:
- Sort all events in strict chronological order
- Apply color coding per `references/color-coding.md` (Timeline Sheet section): prosecution events (light red) | defense-favorable (light green) | neutral (white)
- Hyperlink Source Doc column to corresponding file in Evidence Folder where possible
- Flag any timeline event that conflicts with another document in the Cowork Flags column
- Maintain all existing color coding, dropdown lists, and formatting

### Step 2: Update Witness Tables
The Witness Tables (Priority and Alpha) were initially populated in Phase 1 Step 4. Now update them with intelligence from Phase 2's case analysis:

⚠ **Follow the Case Tables Write Protocol.** See `references/case-tables-write-protocol.md`.

- Incorporate Report 8 (Key Witness Impeachment Plan) — bold-mark any witness with an Impeachment Plan as **KEY WITNESS** in both tables
- Re-rank Priority table: Key Witness (Report 8) > Eyewitnesses > Law Enforcement > Character Witnesses > Others
- Update the `Trial Exam Prepared (Y/N)` column as preparation progresses

### Step 3: Defense Shield & Defense Matrix

⚠ **Follow the Case Tables Write Protocol.** See `references/case-tables-write-protocol.md`.

Read **`references/defense-shield-procedure.md`** for the full procedure. That file covers:
- **3A — Build the Case-Specific Defense Shield:** filter the Defense Shield template (Rape, Homicide, or build new for other case types) to defenses with factual support in this case; populate "Dealing with States Narrative" sheet
- **3B — Populate the Defense Matrix:** map charges and responsive verdicts to the defenses you'll actually run
- **3C — Initialize the Running List:** start tracking defenses as they emerge through trial

Specialist routing from this step:
- Jury instruction research and drafting → **dw-jury-instructions-builder**
- Voir dire strategy → **dw-voir-dire-assistant**
- Witness threat ranking (post-Defense Matrix) → **dw-witness-threat-matrix**

### Step 4: Version Control — Amended & Superseded Documents
When the prosecution sends corrected or supplemental productions:

⚠ **Follow the Case Tables Write Protocol.** See `references/case-tables-write-protocol.md`.

- Maintain a version control log to keep the Master Evidence Table accurate
- Mark superseded documents clearly in the Evidence Table
- Do not delete prior versions — archive with notation

### Step 5: Case Readiness Memo
The attorney's single entry point into the Trial Notebook — one-page summary of everything the attorney needs to know before diving into the file.

Inputs: all 8 case analysis reports, Cowork parallel analysis, current case status

### Step 6: Discover the Story Worksheet (Case Story Development)
Complete before witness preparation begins. This is the foundation of the defense narrative and informs all witness examination preparation.

### Step 7: Cross Exam Preparation (Per Key Witness)
*Attorney work — Cowork prepopulates templates with available intelligence. Route specialist witness types to appropriate skills. Complete for all Key Witness Impeachment Plan witnesses and Top 10 priority witnesses only.*

**7A — Witness Cross Battle Card:** one-page intelligence summary per witness
- **Eyewitness to crime** → route to **dw-eyewitness-identification-auditor** for ID weakness analysis
- **Law enforcement officer** → route to **dw-cross-exam-architect** for hostile witness strategy
- **Expert witness (prosecution)** → route to **dw-expert-witness-evaluator** for methodology challenges
- **Save location:** `01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/`

**7B — Mapping the Cross Worksheet:** prepopulate from impeachment materials, Report 8, and all prior statements. Route to **dw-cross-exam-architect** for strategic question mapping.

**7C — Cross Exam Template:** prepopulate structure and available impeachment points; leave question sequencing and line of attack to attorney. Route specialized witness cross (confessions, interrogation tactics, mobile forensics, video authentication) to appropriate specialist skills.

### Step 8: Direct Exam Preparation (Per Defense Witness)
*Attorney work — Cowork prepopulates templates with intelligence from Discover the Story worksheet and Witness Dossiers.*

**8A — Mapping the Direct Worksheet**

**8B — Direct Exam Template**
- **Save location:** `01 - Trial Notebook/03 - Witnesses/Defense Witnesses/`

### Step 9: Opening Statement & Closing Argument Preparation
*Attorney-driven — Cowork populates the framework from case analysis outputs.*

Populate the Mapping the Story templates (Opening and Closing) from: Report 4 (Core Defense Narrative), Report 6 (Memorable Theme), and the Discover the Story worksheet.

### Step 10: Appellate Readiness
*Post-conviction and during trial preparation — monitor for appealable issues.*

Route preservation of trial error, evidentiary challenges, and appellate strategy to **dw-appellate-error-monitor** to ensure all grounds for appeal are documented and preserved for post-conviction review.

### Step 11: Assemble Trial Notebook
*Final assembly — triggered when all Phase 3 deliverables are complete.*

Route to **dw-trial-notebook-builder** to assemble all Phase 2 and Phase 3 deliverables into the final Trial Notebook. The trial notebook builder scans the case folder for all upstream deliverables, organizes them into the Trial Notebook folder structure, generates a master index, and produces a Trial Readiness Gap Report identifying any missing items.

---

## Pointers

- **Action-type symbols, sheet index, phase quick map, specialist skill routing table:** `references/quick-reference.md`
- **Case folder structure & document naming:** `references/folder-structure-and-naming.md`
- **Spreadsheet color specs:** `references/color-coding.md`
- **Version history:** `CHANGELOG.md` at skill root

---

*This skill reflects Daniels & Washington Cowork Workflow Version 5.8 (May 2026). Update this file whenever the master workflow document is revised.*
