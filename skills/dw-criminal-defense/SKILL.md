---
name: dw-criminal-defense
description: >
  Master 4-phase criminal defense workflow. ALWAYS invoke for "case intake," "new case,"
  "run Phase 1/2/3/4," or initial case setup. Do NOT use for loading existing case state —
  use dw-case-brain. Do NOT use for case status checks — use dw-case-dashboard.
---

# Daniels & Washington — Criminal Defense Cowork Skill
**Version 4.0 | Internal Use Only**

This skill governs all Claude Cowork operations for criminal defense case management at Daniels & Washington. Follow this skill for every task involving a client case file. The 4-phase workflow below is the single source of truth.

---

## Core Rules (Always Apply)

- **Never create new spreadsheets.** All tabular data goes into the sheets that already exist in `Case Tables.xlsx` at the root of the case folder.
- **Never create new folders** unless a standard subfolder is confirmed missing.
- **Naming convention:** All documents use `[3-digit prefix] - [Document Name].docx` format (e.g., `010 - Incident Report`).
- **Cowork drafts; attorney approves.** Claude prepopulates templates and drafts documents. Attorneys make final decisions and send all external communications.
- **Quality Gates must be confirmed** before advancing to the next phase. Do not proceed if any gate item is unresolved.
- **Louisiana law applies** unless otherwise indicated. Use Louisiana statutes for all charge research, discovery obligations, and citations.

---

## PHASE 0 — Case Intake & Matter Setup

*Triggered the moment a new client engagement is confirmed — before any discovery arrives.*

### Step 1: Folder Setup
- Confirm all standard subfolders exist: `01 - Trial Notebook` (all sub-tabs) and `02 - Pretrial Notebook` (all sub-tabs).
- Locate `Case Tables.xlsx` at the root of the case folder.
- Do not create new folders unless a standard subfolder is missing.

### Step 2: Generate Initial Case Profile
**Output:** `000 - Initial Case Profile.docx` → save to `Pretrial Notebook → 03 - Case Analysis & Notes`

Include:
- All charges with Louisiana statutory citations and maximum penalties
- Elements the prosecution must prove for each count
- Common defenses associated with each charge type
- Any mandatory minimums or habitual offender exposure flagged

### Step 3: Criminal Defense Cover
**Output:** `002 - Criminal Defense Cover.docx` → save to `Pretrial Notebook → 03 - Case Analysis & Notes`

- Use the `CRIMINAL DEFENSE COVER.docx` template from the root folder.
- **Cowork populates:** Charges, Docket #, Bill/Indictment Date, Next Court Date (from Clio intake).
- **Staff/Attorney completes:** Client Name, DOB, SS#, Address, Phone, Email, Date of Offense, Date of Arrest, Date of Hire.
- **Arraignment:** Date, Charges, Prosecutor, Judge — populate from court filings when available.
- **Bail:** Check appropriate box (ROR / REMAND / BAIL SET), record bond amounts.
- **Client Info:** Prior Criminal History, Family/Home Life, Educational History, Employment, Medical/Mental Health — Attorney completes after client interview.
- Create a Clio task for attorney/staff completion of all open fields.

### Step 4: LWOP Assessment (If Applicable)
**Output:** `001 - LWOP Worksheet.docx` → save to `Pretrial Notebook → 03 - Case Analysis & Notes`

- Review charges to determine if LWOP exposure exists.
- **Homicide charges:** use `LWOP Homicide Review Sheet - FOR TYPING.docx` template.
- **Sex offense charges:** use `LWOP Sex Offense Review Sheet - FOR TYPING.docx` template.
- **Prepopulate:** Docket No., Date of Offense, Charges, Aggravating Factors, Indictment status.
- **Leave blank (attorney completes):** Theory of the Case, Prior Convictions, Witnesses, Defense(s).
- Create a Clio task: *"LWOP Worksheet requires review and completion after discovery."*

**LWOP Homicide Sheet fields:** State v. [Name], Docket No., Date of Offense, Age at Time of Offense, Co-Defendant(s), Alleged Victim(s) (asterisk deceased), Charges & Aggravating Factors, Indictment Attached (Yes/Not Received/Amended), Theory of Case, Prior Convictions, Witnesses/Statements, Police Report, Defenses/Possible Defense Witnesses, Defendant Statements, Motion to Suppress, Motions section (Discovery, Bill of Particulars, Suppression, In Limine, Reveal the Deal, Bond Reduction, Speedy Trial, Prescription), Investigation section, Discovery Checklist (Police Reports, Video, Photos, Autopsy, Labs, Forensics, Witness Statements, Client Statements, Co-Defendant Statements, HIPAA, School Records).

**LWOP Sex Offense Sheet differences:** Include ages & birth dates for alleged victims. Discovery Checklist substitutes: SANE Exam (instead of Autopsy), CAC Video (instead of Photos), Labs with Accuser/Client/Co-Defendant/Witness columns. Submit to District Defender every 30 days after appointment.

### ✓ Phase 0 Quality Gate
Before proceeding to Phase 1, confirm:
- [ ] Full folder structure confirmed — all standard subfolders exist
- [ ] `Case Tables.xlsx` located at root of case folder
- [ ] `000 - Initial Case Profile.docx` saved to correct location
- [ ] `001 - LWOP Worksheet.docx` saved (if applicable) — Clio task created
- [ ] `002 - Criminal Defense Cover.docx` saved — Clio task created

---

## PHASE 1 — Prepare Discovery for Review

*Converts raw discovery into a fully organized, Bate-stamped, searchable case file. Folder sorting runs in parallel with OCR — do not wait for OCR to begin sorting.*

### Step 1: Download & Organize Discovery
- Sort all downloaded files into `01 - Pleadings` and `02 - Discovery` subfolders in the Pretrial Notebook.
- Move audio/video files to `05 - Evidence` in the Trial Notebook only — no duplicates.
- Generate a **Download Log**: date received, production set name, file count, total pages (estimated).
- Flag image-only PDFs (need OCR) vs. text-searchable PDFs.
- **Staff action (parallel):** Run OCR on all flagged image-only PDFs using Adobe Acrobat Professional, PDF Expert, or ScanSnap.

### Step 2: Bate-Stamp Documents
**Maintain:** `Bate Stamp Master Log.xlsx` as the single source of truth.

Log columns: Production Set | Date Received | Start Number | End Number | Staff Member | Date Stamped

Rules:
- Sequential numbering in order received. Never restart mid-case. Continuous across all production dates.
- Before any new stamping: check log for current highest number, output the next available.
- After stamping: update log immediately — no batch updates.
- Flag any numbering gap — alert staff before proceeding.
- Flag any overlap (duplicate numbers) — halt Phase 1 until resolved.

### Step 3: Duplicate Discovery to Evidence Folder
- Copy all Bate-stamped, OCR'd documents to `05 - Evidence` in the Trial Notebook.
- Run file count and size comparison between source and destination.
- Flag any file that failed to copy or shows a size mismatch.
- Do not proceed to Step 4 until copy is 100% verified.

### Step 4: Separate Discovery into Individual Documents
- Review the State's index to identify document divisions and names.
- Split the combined PDF into individual files at the State's document boundaries.
- Apply naming convention: `[3-digit prefix] - [Document Name]` (e.g., `010 - Incident Report`).
- Create subfolders for multi-file audio/video (e.g., `025 - Body Camera Footage/`).
- Output a **Separation Checklist**: expected document count (from State index) vs. actual file count.
- Flag any document in the State's index with no corresponding file — log in Report 7 queue.

### Step 5: Transcribe Interviews & Digital Media
Route to **casedev:transcription** skill for audio/video processing with speaker diarization.
- Staff uploads all audio/video files to casedev vault; skill handles transcription automatically.
- When transcripts return: name each transcript PDF identically to its audio/video file, save in the same folder.
- Add transcript as a separate row in the Master Evidence Table (Evidence Type: Transcript).
- Confirm every audio/video file has a corresponding transcript before Phase 2.

### Step 6: Digital Evidence Handling — Generate Placeholders
Media folders (photos, videos, audio, surveillance, body cam footage) cannot be Bate-stamped like documents. Each media folder needs a **Digital Evidence Placeholder** — a one-page PDF that sits in the evidence sequence and describes the folder's contents. Optionally route complex media analysis to **dw-evidence-placeholder** skill for full inventory generation.

**Run the bundled generator script:**
```bash
python3 <skill-directory>/scripts/generate_placeholders.py \
  --evidence-dir "<path-to-05-Evidence>" \
  [--folders "folder1" "folder2" ...]  # optional: specific folders only
```

If `--folders` is omitted, the script processes all subfolders automatically.

**What the script does:**
1. Scans each subfolder in the evidence directory for file counts, types, and size
2. Classifies contents by media type (Audio, Photo/Image, Video, Other Data)
3. Generates a one-page PDF placeholder for each folder matching the firm's template
4. Names each PDF identically to its source folder and saves it in the evidence directory

**Workflow:**
- Identify every subfolder in `05 - Evidence` that contains media files
- Confirm scope with user — default to processing all folders unless told otherwise
- Skip folders that already have a corresponding placeholder PDF (unless regenerating)
- After running, report: total placeholders created, any folders skipped, breakdown by media type

**Media type classification:**

| Category | Extensions |
|----------|-----------|
| Audio | .wav, .mp3, .aac, .flac, .ogg, .wma, .m4a, .wpl |
| Photo/Image | .jpg, .jpeg, .png, .bmp, .tiff, .gif, .raw, .cr2, .nef, .heic |
| Video | .mp4, .avi, .mov, .mkv, .wmv, .flv, .mts, .vob, .mpg, .mpeg, .m4v, .3gp, .dav, .264, .sec, .thm, .bup, .ifo |
| Other Data | .pdf, .docx, .doc, .txt, .xlsx, .csv, .exe, .dll, .db, .seclist |

Each placeholder PDF includes: Evidence ID/Name, file count, checked media type boxes, auto-generated description with file format breakdown, and storage path for retrieval.

### Step 7: Build the Master Evidence Table
Populate the **Evidence Table Sheet** in `Case Tables.xlsx`. Do not create a new sheet. Maintain all existing color coding, dropdown lists, and formatting.

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

### ✓ Phase 1 Quality Gate
Before proceeding to Phase 2, confirm:
- [ ] File count in Evidence Folder matches file count in Master Evidence Table
- [ ] Every audio/video file has a corresponding transcript entry
- [ ] Bate Stamp Log shows no gaps or overlaps
- [ ] All image-only PDFs have been OCR'd and confirmed text-searchable
- [ ] No documents in the State's index are absent from the Evidence Folder
- [ ] Separation Checklist: expected count = actual count
- [ ] Digital Evidence Placeholder PDF exists for every media folder in `05 - Evidence`

---

## PHASE 2 — Case Processing & Analysis

*Runs parallel analysis before attorney review. Auto-action loops triggered by Reports 7 and 9 eliminate rework in Phase 3.*

### Step 1: Parallel Analysis
Before attorney review begins, independently analyze all case documents and generate:
- **Constitutional Issues Scan:** flag any document suggesting 4th, 5th, or 6th Amendment concerns → route to **dw-suppression-motion**
- **Brady/Giglio Checklist:** identify material favorable to defense that may not have been disclosed → route to **dw-brady-giglio-auditor**
- **Witness Cross-Reference:** map every witness name across all documents and flag inconsistencies → route to **dw-cross-exam-architect**
- **Timeline Cross-Check:** build a preliminary chronology and flag any date/time conflicts in reports
- **Chain of Custody Audit:** verify each piece of physical evidence has an unbroken custody log → route to **dw-chain-of-custody-auditor**

Save all outputs to: `Pretrial Notebook → 03 - Case Analysis & Notes → Cowork Analysis` subfolder.

**Specialized Evidence Routing:** Identify and route based on evidence type:
- Eyewitness identification issues → **dw-eyewitness-identification-auditor**
- Confession/interrogation issues → **dw-confession-interrogation-auditor**
- Cell phone forensics → **dw-mobile-forensic-auditor** then **dw-forensic-dump-analyzer**
- Video evidence analysis → **dw-video-evidence-auditor**
- Cell site/location data → **dw-cell-site-geolocation-auditor**
- Social media evidence → **dw-social-media-auditor**
- Child forensic interviews → **dw-child-forensic-interview-auditor**
- Expert witness issues → **dw-expert-witness-evaluator**

### Step 2: Generate the 9 Case Analysis Reports
Use the **Case Analysis Prompts for Criminal Defense** document. Name each report exactly as shown. Run using the provided prompts. For each report, identify and route specific issues to specialist skills (suppress motions, Brady audits, bond reduction, sentencing, plea analysis, etc.).

| # | Report Name | Output Location | Priority | Skill Routing |
|---|-------------|-----------------|----------|----------------|
| 1 | Comprehensive Case Timeline | `Case Tables.xlsx — Timeline Sheet` | Standard | - |
| 2 | Prosecution's Case Summary | `09 - Case Analysis folder` | Standard | - |
| 3 | Immediate Red Flags | `09 - Case Analysis folder` | **HIGH ★** | **dw-suppression-motion** (for warrant/search issues); **dw-expert-witness-evaluator** (for expert issues) |
| 4 | Core Defense Narrative | `09 - Case Analysis folder` | Standard | - |
| 5 | Viable Legal Defenses | `09 - Case Analysis folder` | Standard | **dw-404b-opposition** (for bad acts); **dw-sentencing-mitigation-specialist** (for sentencing exposure); **dw-habitual-offender-auditor** (for habitual claims) |
| 6 | Memorable Theme | `09 - Case Analysis folder` | Standard | - |
| 7 | Table of Missing Discovery | `09 - Case Analysis folder` | **HIGH ★ → Auto-Action** | **dw-brady-giglio-auditor** |
| 8 | Witness Table | `Case Tables.xlsx — Witness Sheet` | Standard | - |
| 9 | Key Witness Impeachment Plan | `09 - Case Analysis folder` | **HIGH ★ → Auto-Action** | **dw-cross-exam-architect** |

**Bond/Release Issues:** If Report 3 or 5 identifies bond concerns → route to **dw-bond-and-release-motion**
**Plea Negotiations:** If prosecution indicates negotiation interest → route to **dw-plea-negotiation-analyzer**

### Step 3: Auto-Action — Report 7 → Missing Discovery Demand Letter
*Triggered immediately upon filing Report 7.*

**Output:** `Missing Discovery Demand — [Date].docx` → save to `Pretrial Notebook → 06 - Law & Research`

- Extract every item listed in Report 7's data table.
- Draft a formal demand letter addressed to the prosecution citing Brady/Giglio obligations.
- List each missing item with description and why it is material to the defense.
- Include Louisiana statutory citations for discovery disclosure requirements.
- Create a Clio task: *"Review and Send Missing Discovery Demand Letter"* — assigned to attorney.
- **Attorney must approve before letter is sent.**

### Step 4: Auto-Action — Report 9 → Impeachment Worksheets
*Triggered immediately upon filing Report 9.*

Create one Impeachment Worksheet per key witness in `Trial Notebook → 03 - Witnesses`:
- **Prepopulate:** witness name, role, all document references (Bate stamps) from Master Evidence Table
- **Prepopulate:** all impeachment material from Report 9 for that witness
- **Prepopulate:** all prior statements from transcripts with Bate stamp references
- **Add:** Witness Dossier cover page consolidating everything known about this witness
- **Leave blank (attorney completes):** Line of Attack, Question Sequence, Anticipated Responses

### Step 5: Route Case Analysis to Attorney
Once all 9 reports and auto-action documents are complete:
- Draft attorney email: *"Case Analysis Ready for Review — [Client Name] / [Case Number]"*
- Attach Case Analysis Index listing all 9 reports + Cowork Analysis findings
- Confirm Missing Discovery Demand Letter is ready for attorney approval
- Confirm all Impeachment Worksheets are filed and ready for Phase 3
- Create Clio task: *"Case Analysis Ready for Review"* — assigned to attorney

### Step 6: Auto-Push Attorney Review Checklist to Google Docs & Apple Notes
*Triggered immediately after Step 5. The attorney needs actionable review items in their daily-driver apps — not buried in the case folder.*

After completing all 9 reports and auto-actions, Cowork generates an **Attorney Review Checklist** and pushes it to both Google Docs and Apple Notes. This ensures the attorney sees the checklist where they actually work, with a clear deadline.

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

**6A — Push to Google Docs:**
1. Use Claude in Chrome (`mcp__Claude_in_Chrome`) to navigate to `https://docs.google.com/document/create`
2. Wait for the blank document to load
3. Set the document title using the `.docs-title-input` element
4. Click into the document body and type the full checklist content
5. For checkboxes: use Google Docs keyboard shortcut or menu to insert checklist items
6. The document auto-saves to the attorney's Google Drive — no manual save needed

**6B — Push to Apple Notes (via iCloud web):**
1. Use Claude in Chrome to navigate to `https://www.icloud.com/notes`
2. Wait for iCloud Notes to load (user must be logged into iCloud in Chrome)
3. Click the "New Note" button to create a new note
4. Type the same title and checklist content
5. Apple Notes on iCloud supports checklist formatting — use the checklist button in the toolbar

**Fallback behavior (important — Chrome may not always be connected):**
If Claude in Chrome is not available or either service is unreachable:
1. Save the checklist as `Attorney Review Checklist — [Date].md` at the case root
2. Log which pushes failed in the Quality Gate
3. Alert the attorney: *"Review checklist saved locally — Chrome automation was unavailable for [Google Docs / Apple Notes]. Connect Claude in Chrome and re-run Step 6 to push."*

The reason for the fallback is that Claude in Chrome requires the browser extension to be installed and connected, which isn't always the case. The local markdown file ensures the checklist is never lost, even if the push fails.

### ✓ Phase 2 Quality Gate
Before proceeding to Phase 3, confirm:
- [ ] All 9 reports named correctly and saved to correct locations
- [ ] Cowork Parallel Analysis complete — all outputs saved to Cowork Analysis subfolder
- [ ] Missing Discovery Demand Letter drafted — Clio task assigned to attorney
- [ ] Impeachment Worksheet exists for every witness named in Report 9
- [ ] Witness Dossier cover page exists for every key witness
- [ ] Attorney notified via email AND Clio task
- [ ] Attorney Review Checklist pushed to Google Docs (or fallback .md saved at case root)
- [ ] Attorney Review Checklist pushed to Apple Notes (or fallback .md saved at case root)

---

## PHASE 3 — Trial Notebook & Attorney Preparation

*Converts case analysis into actionable trial preparation. Cowork pre-builds all templates; attorneys complete cross and direct exam preparation using the integrated templates.*

### Step 1: Case Timeline Spreadsheet
Built from **Report 1** (Comprehensive Case Timeline) → `Case Tables.xlsx — Timeline Sheet`

Columns to populate: Start Date | Start Time | End Date | End Time | Title | Subtitle | Description | Tags (Cowork Flags) | Bate Stamp | Notes

Rules:
- Sort all events in strict chronological order
- Color-code: prosecution events (light red) | defense-favorable (light green) | neutral (white)
- Hyperlink Source Doc column to corresponding file in Evidence Folder where possible
- Flag any timeline event that conflicts with another document in the Cowork Flags column
- Maintain all existing color coding, dropdown lists, and formatting

### Step 2: Witness Lists — Two Versions
Generate both versions simultaneously in `Case Tables.xlsx`. Use existing sheets — do not create separate files.

**Version A — Alpha** (`Witness List - Alpha` sheet): standard alphabetical reference list

**Version B — Priority** (`Witness List - Priority` sheet): sorted by witness impact on case outcome

Importance ranking: Key Witness (Report 9) > Eyewitnesses > Law Enforcement > Character Witnesses > Others

Both versions include: Name | Witness Type | Association | Sources (Bate stamps) | Trial Exam Prepared (Y/N)

Bold-mark any witness with a Report 9 Impeachment Plan as **KEY WITNESS** in both versions.

### Step 3: Defense Matrix
Populate the Defense Matrix sheet in `Case Tables.xlsx`. Complete all 6 columns.

- Charge column: list each offense charged AND all responsive verdicts on separate rows
- Review `Art 814 Responsive Verdicts` document in `Trial Notebook → 01 - Jury Instructions & Selection`
- After populating charges and responsive verdicts, identify applicable defenses
- Review `Legal Defenses (Rape)` OR `Legal Defenses (Homicide)` sheet — only the one applicable to this case
- Route jury instruction research and drafting to **dw-jury-instructions-builder** for comprehensive instruction set
- Route voir dire strategy to **dw-voir-dire-assistant** for juror challenge guidance

### Step 4: Version Control — Amended & Superseded Documents
When the prosecution sends corrected or supplemental productions:
- Maintain a version control log to keep the Master Evidence Table accurate
- Mark superseded documents clearly in the Evidence Table
- Do not delete prior versions — archive with notation

### Step 5: Case Readiness Memo
The attorney's single entry point into the Trial Notebook — one-page summary of everything the attorney needs to know before diving into the file.

Inputs: all 9 case analysis reports, Cowork parallel analysis, current case status

### Step 6: Discover the Story Worksheet (Case Story Development)
Complete before witness preparation begins. This is the foundation of the defense narrative and informs all witness examination preparation.

### Step 7: Cross Exam Preparation (Per Key Witness)
*Attorney work — Cowork prepopulates templates with available intelligence. Route specialist witness types to appropriate skills. Complete for all Key Witness Impeachment Plan witnesses and Top 10 priority witnesses only.*

**7A — Witness Cross Battle Card:** one-page intelligence summary per witness
- **Eyewitness to crime** → route to **dw-eyewitness-identification-auditor** for ID weakness analysis
- **Law enforcement officer** → route to **dw-cross-exam-architect** for hostile witness strategy
- **Expert witness (prosecution)** → route to **dw-expert-witness-evaluator** for methodology challenges

**7B — Mapping the Cross Worksheet:** prepopulate from impeachment materials, Report 9, and all prior statements. Route to **dw-cross-exam-architect** for strategic question mapping.

**7C — Cross Exam Template:** prepopulate structure and available impeachment points; leave question sequencing and line of attack to attorney. Route specialized witness cross (confessions, interrogation tactics, mobile forensics, video authentication) to appropriate specialist skills.

### Step 8: Direct Exam Preparation (Per Defense Witness)
*Attorney work — Cowork prepopulates templates with intelligence from Discover the Story worksheet and Witness Dossiers.*

**8A — Mapping the Direct Worksheet**

**8B — Direct Exam Template**

### Step 9: Opening Statement & Closing Argument Preparation
*Attorney-driven — Cowork populates the framework from case analysis outputs.*

Populate the Mapping the Story templates (Opening and Closing) from: Report 4 (Core Defense Narrative), Report 6 (Memorable Theme), and the Discover the Story worksheet.

### Step 10: Appellate Readiness
*Post-conviction and during trial preparation — monitor for appealable issues.*

Route preservation of trial error, evidentiary challenges, and appellate strategy to **dw-appellate-error-monitor** to ensure all grounds for appeal are documented and preserved for post-conviction review.

---

## Quick Reference

### Cowork Action Types
- ⚡ **COWORK ACTION** — Claude executes this step
- ⚠ **STAFF ACTION** — Human staff executes; Claude may assist or verify
- ⚖ **ATTORNEY ACTION** — Attorney-only; Claude prepopulates supporting materials only
- ✓ **QUALITY GATE** — Must be confirmed before advancing to next phase
- 📋 **TEMPLATE GUIDE** — Reference for populating a specific document

### Standard Folder Structure Reference
```
[Case Root]/
├── Case Tables.xlsx                    ← Master data file — never replace
├── 01 - Trial Notebook/
│   ├── 01 - Jury Instructions & Selection/
│   ├── 03 - Witnesses/                 ← Impeachment Worksheets filed here
│   ├── 05 - Evidence/                  ← Bate-stamped, OCR'd docs + A/V
│   └── 09 - Case Analysis/             ← Reports 2-7, 9
└── 02 - Pretrial Notebook/
    ├── 01 - Pleadings/
    ├── 02 - Discovery/
    ├── 03 - Case Analysis & Notes/
    │   ├── 000 - Initial Case Profile.docx
    │   ├── 001 - LWOP Worksheet.docx
    │   ├── 002 - Criminal Defense Cover.docx
    │   └── Cowork Analysis/            ← Parallel analysis outputs
    └── 06 - Law & Research/            ← Missing Discovery Demand Letters
```

### Case Tables.xlsx — Sheet Reference
| Sheet Name | Contents | Phase Populated |
|------------|----------|-----------------|
| Evidence Table | Master discovery index | Phase 1 |
| Timeline Sheet | Chronological case events | Phase 2 Report 1 / Phase 3 Step 1 |
| Witness Sheet | Witness data table | Phase 2 Report 8 |
| Witness List - Alpha | Alphabetical witness list | Phase 3 Step 2 |
| Witness List - Priority | Priority-ranked witness list | Phase 3 Step 2 |
| Defense Matrix | Charges, responsive verdicts, defenses | Phase 3 Step 3 |

### Document Naming Convention
- All documents: `[3-digit prefix] - [Document Name].docx`
- Audio/video folders: `[3-digit prefix] - [Name]/`
- Transcripts: named identically to their corresponding A/V file
- Missing Discovery Demand Letters: `Missing Discovery Demand — [Date].docx`
- Impeachment Worksheets: one per key witness, filed in `Trial Notebook → 03 - Witnesses`

---

*This skill reflects Daniels & Washington Cowork Workflow Version 4.0 (March 2026). Update this file whenever the master workflow document is revised.*
