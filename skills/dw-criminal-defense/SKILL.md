---
name: dw-criminal-defense
description: >
  Master 3-phase criminal defense workflow. ALWAYS invoke for "case intake," "new case,"
  "run Phase 1/2/3," or initial case setup. Do NOT use for loading existing case state —
  use dw-case-brain. Do NOT use for case status checks — use dw-case-dashboard.
---

# Daniels & Washington — Criminal Defense Cowork Skill
**Version 5.0 | Internal Use Only**

This skill governs all Claude Cowork operations for criminal defense case management at Daniels & Washington. Follow this skill for every task involving a client case file. The 3-phase workflow below is the single source of truth.

---

## Core Rules (Always Apply)

- **Never create new spreadsheets.** All tabular data goes into the sheets that already exist in `Case Tables.xlsx` at the root of the case folder.
- **Never create new folders** unless a standard subfolder is confirmed missing.
- **Naming convention:** All documents use `[3-digit prefix] - [Document Name].docx` format (e.g., `010 - Incident Report`).
- **Cowork drafts; attorney approves.** Claude prepopulates templates and drafts documents. Attorneys make final decisions and send all external communications.
- **Quality Gates must be confirmed** before advancing to the next phase. Do not proceed if any gate item is unresolved.
- **Louisiana law applies** unless otherwise indicated. Use Louisiana statutes for all charge research, discovery obligations, and citations.

---

## PHASE 1 — Case Intake & Matter Setup

*Triggered the moment a new client engagement is confirmed. This phase covers everything from folder creation through a fully organized, Bate-stamped, searchable case file with a complete Case Profile — the foundation for all analysis in Phase 2.*

### Step 1: Folder Setup
- Confirm all standard subfolders exist: `01 - Trial Notebook` (all sub-tabs) and `02 - Pretrial Notebook` (all sub-tabs).
- Locate `Case Tables.xlsx` at the root of the case folder.
- Do not create new folders unless a standard subfolder is missing.

**✓ Step 1 Check:** Folder structure confirmed, `Case Tables.xlsx` located.

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
- Apply naming convention: `[3-digit prefix] - [Document Name]` (e.g., `010 - Incident Report`).
- Create subfolders for multi-file audio/video (e.g., `025 - Body Camera Footage/`).
- Output a **Separation Checklist**: expected document count (from State index) vs. actual file count.
- Flag any document in the State's index with no corresponding file — log in Report 7 queue.

**2e — Transcribe Interviews & Digital Media**
Route to **casedev:transcription** skill for audio/video processing with speaker diarization.
- Staff uploads all audio/video files to casedev vault; skill handles transcription automatically.
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

This single document replaces the former Initial Case Profile and Criminal Defense Cover. It is organized to follow the lifecycle of a criminal case — from identification through disposition — so the attorney can use it as a living reference from intake through trial.

**Section 1 — Case Identification**
- Client Name | DOB | SS# | Address | Phone | Email
- Docket # | Court | Division | Judge
- Date of Offense | Date of Arrest | Date of Hire
- Co-Defendant(s) (if any)
- **Cowork populates** from Clio intake and court filings where available. **Staff/Attorney completes** remaining client demographic fields.

**Section 2 — Charges & Exposure**
- All charges with Louisiana statutory citations
- Maximum penalty for each count
- Elements the prosecution must prove for each count
- Any mandatory minimums flagged
- Habitual offender exposure (if applicable)
- Responsive verdicts for each charge (reference `Art 814 Responsive Verdicts`)

**Section 3 — Arraignment & Bail**
- Arraignment: Date | Charges Read | Prosecutor | Judge
- Plea entered
- Bail status: ROR / REMAND / BAIL SET — record bond amounts
- Conditions of release
- **Populate from court filings when available; leave blank fields for attorney completion.**

**Section 4 — Case-Specific Defenses**
Review all available case file materials — arrest reports, police narratives, witness statements, evidence logs, bodycam summaries, transcripts, and any other intake documents. Identify defenses grounded in what the case file actually contains. This is not a list of generic defenses.

For each potential defense, include:
- The defense theory
- The specific evidence or document supporting it (with Bate stamp reference)
- Constitutional issues flagged (unlawful stop, Miranda violations, warrant defects)
- Factual weaknesses in the State's case (inconsistent accounts, evidence gaps, timeline conflicts)
- Affirmative defenses supported by the facts
- Recommendation for attorney investigation

**Section 5 — Client Background** *(Attorney completes after client interview)*
- Prior Criminal History
- Family / Home Life
- Educational History
- Employment History
- Medical / Mental Health
- Military Service (if applicable)

**Section 6 — Key Dates & Next Steps**
- Next Court Date (from Clio / Google Calendar)
- Bill/Indictment Date
- Discovery deadlines
- Motion filing deadlines
- Clio tasks created for attorney/staff completion of all open fields

**✓ Step 3 Check:**
- [ ] `000 - Case Profile.docx` saved to correct location
- [ ] All auto-populated fields completed from available sources
- [ ] Clio tasks created for attorney/staff completion of open fields

### Step 4: Build Case Tables
Populate three sheets in `Case Tables.xlsx`. Do not create new sheets — use the existing ones. Maintain all existing color coding, dropdown lists, and formatting. The Case Profile (Step 3) provides the charge and defense context needed for accurate assessment of all columns.

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
- [ ] `000 - Case Profile.docx` complete with all auto-populated fields (Step 3)
- [ ] All Case Tables populated — Evidence Table (all 11 columns), Witness Tables (Priority and Alpha) (Step 4)

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

Save all outputs to: `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/` subfolder.

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
| 2 | Prosecution's Case Summary | `01 - Trial Notebook/09 - Case Analysis/` | Standard | - |
| 3 | Immediate Red Flags | `01 - Trial Notebook/09 - Case Analysis/` | **HIGH ★** | **dw-suppression-motion** (for warrant/search issues); **dw-expert-witness-evaluator** (for expert issues) |
| 4 | Core Defense Narrative | `01 - Trial Notebook/09 - Case Analysis/` | Standard | - |
| 5 | Viable Legal Defenses | `01 - Trial Notebook/09 - Case Analysis/` | Standard | **dw-404b-opposition** (for bad acts); **dw-sentencing-mitigation-specialist** (for sentencing exposure); **dw-habitual-offender-auditor** (for habitual claims) |
| 6 | Memorable Theme | `01 - Trial Notebook/09 - Case Analysis/` | Standard | - |
| 7 | Table of Missing Discovery | `01 - Trial Notebook/09 - Case Analysis/` | **HIGH ★ → Auto-Action** | **dw-brady-giglio-auditor** |
| 8 | Witness Table | `Case Tables.xlsx — Witness Sheet` | Standard | - |
| 9 | Key Witness Impeachment Plan | `01 - Trial Notebook/09 - Case Analysis/` | **HIGH ★ → Auto-Action** | **dw-cross-exam-architect** |

**Bond/Release Issues:** If Report 3 or 5 identifies bond concerns → route to **dw-bond-and-release-motion**
**Plea Negotiations:** If prosecution indicates negotiation interest → route to **dw-plea-negotiation-analyzer**

### Step 3: Auto-Action — Report 7 → Missing Discovery Demand Letter
*Triggered immediately upon filing Report 7.*

**Output:** `Missing Discovery Demand — [Date].docx` → save to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

- Extract every item listed in Report 7's data table.
- Draft a formal demand letter addressed to the prosecution citing Brady/Giglio obligations.
- List each missing item with description and why it is material to the defense.
- Include Louisiana statutory citations for discovery disclosure requirements.
- Create a Clio task: *"Review and Send Missing Discovery Demand Letter"* — assigned to attorney.
- **Attorney must approve before letter is sent.**

### Step 4: Auto-Action — Report 9 → Impeachment Worksheets
*Triggered immediately upon filing Report 9.*

Create one Impeachment Worksheet per key witness in `Trial Notebook → 03 - Witnesses`:
- **Prepopulate:** witness name, role, all document references (Bate stamps) from Evidence Table
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

### Step 2: Update Witness Tables
The Witness Tables (Priority and Alpha) were initially populated in Phase 1 Step 4. Now update them with intelligence from Phase 2's case analysis:

- Incorporate Report 8 (Witness Table) data — merge any new witnesses or details
- Incorporate Report 9 (Key Witness Impeachment Plan) — bold-mark any witness with an Impeachment Plan as **KEY WITNESS** in both tables
- Re-rank Priority table: Key Witness (Report 9) > Eyewitnesses > Law Enforcement > Character Witnesses > Others
- Update the `Trial Exam Prepared (Y/N)` column as preparation progresses

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
- **Save location:** `01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/`

**7B — Mapping the Cross Worksheet:** prepopulate from impeachment materials, Report 9, and all prior statements. Route to **dw-cross-exam-architect** for strategic question mapping.

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
    │   ├── 000 - Case Profile.docx
    │   └── Cowork Analysis/            ← Parallel analysis outputs
    └── 06 - Law & Research/            ← Missing Discovery Demand Letters
```

### Case Tables.xlsx — Sheet Reference
| Sheet Name | Contents | Phase Populated |
|------------|----------|-----------------|
| Evidence Table | Master discovery index | Phase 1 Step 4 |
| Timeline Sheet | Chronological case events | Phase 2 Report 1 / Phase 3 Step 1 |
| Witness Sheet | Witness data table | Phase 2 Report 8 |
| Witness List - Alpha | Alphabetical witness list | Phase 1 Step 4 → Phase 3 Step 2 |
| Witness List - Priority | Priority-ranked witness list | Phase 1 Step 4 → Phase 3 Step 2 |
| Defense Matrix | Charges, responsive verdicts, defenses | Phase 3 Step 3 |

### Document Naming Convention
- All documents: `[3-digit prefix] - [Document Name].docx`
- Audio/video folders: `[3-digit prefix] - [Name]/`
- Transcripts: named identically to their corresponding A/V file
- Missing Discovery Demand Letters: `Missing Discovery Demand — [Date].docx`
- Impeachment Worksheets: one per key witness, filed in `Trial Notebook → 03 - Witnesses`

---

*This skill reflects Daniels & Washington Cowork Workflow Version 5.0 (April 2026). Update this file whenever the master workflow document is revised.*
