---
name: dw-case-dashboard
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

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

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

Check for presence of all Phase 0 documents in `02 - Pretrial Notebook → 03 - Case Analysis & Notes`:

| Deliverable | File Name | Status |
|-------------|-----------|--------|
| Initial Case Profile | `000 - Initial Case Profile.docx` | ✓ or ✗ |
| Criminal Defense Cover | `002 - Criminal Defense Cover.docx` | ✓ or ✗ |
| LWOP Assessment | `001 - LWOP Worksheet.docx` | ✓ or ✗ (only required if homicide/sex offense) |
| Folder Setup Complete | Verify all standard subfolders exist | ✓ or ✗ |

**Status Logic:**
- All 4 items present → **Phase 0 Complete** ✓
- 3 items present (LWOP not required) → **Phase 0 Complete** ✓
- 2 or fewer items → **Phase 0 In Progress**

### Step 3: Scan Phase 1 Deliverables

Check in `01 - Trial Notebook → 05 - Evidence/` and `Case Tables.xlsx`:

| Deliverable | Location | Status |
|-------------|----------|--------|
| Master Evidence Table | `Case Tables.xlsx — Evidence Table sheet` | Check row count > 0 |
| Evidence Folder Count | `05 - Evidence/` file count | Verify > 0 |
| Bate Stamp Log | `Bate Stamp Master Log.xlsx` at case root | ✓ or ✗ |
| Transcripts | Any `*_transcript.pdf` in media subfolders | Count present |
| Digital Placeholders | One `.pdf` per media subfolder | Count present |

**Status Logic:**
- Master Evidence Table populated (>10 rows), files in 05-Evidence folder, Bate Log exists, transcripts for A/V, placeholders for media folders → **Phase 1 Complete** ✓
- Some but not all items → **Phase 1 In Progress**
- None present → **Phase 1 Not Started**

### Step 4: Scan Phase 2 Deliverables

Check `01 - Trial Notebook → 09 - Case Analysis/` and `Case Tables.xlsx`:

| Report # | Report Name | Status | Priority |
|----------|-------------|--------|----------|
| 1 | Comprehensive Case Timeline | Check Timeline Sheet in xlsx | Standard |
| 2 | Prosecution's Case Summary | Scan for `02 - Prosecution...` or similar | Standard |
| 3 | Immediate Red Flags | Scan for `03 - Red Flags...` | **HIGH** |
| 4 | Core Defense Narrative | Scan for `04 - Defense Narrative...` | Standard |
| 5 | Viable Legal Defenses | Scan for `05 - Legal Defenses...` | Standard |
| 6 | Memorable Theme | Scan for `06 - Memorable Theme...` | Standard |
| 7 | Missing Discovery Demand | Check for auto-generated demand letter | **HIGH** |
| 8 | Witness Table | Check Witness Sheet in xlsx | Standard |
| 9 | Impeachment Plan | Scan for `09 - Impeachment...` or witness worksheets | **HIGH** |

Also check:
- `02 - Pretrial Notebook → 03 - Case Analysis & Notes → Cowork Analysis/` folder for Constitutional, Brady, Witness Cross-Reference, Timeline, Chain of Custody analyses
- `02 - Pretrial Notebook → 06 - Law & Research/` for Missing Discovery Demand Letter
- `01 - Trial Notebook → 03 - Witnesses/` for Impeachment Worksheets

### Step 4B: Scan for Auditor Skill Outputs (Phase 2)

Scan the `Cowork Analysis/` folder for deliverables from specialist auditor skills. These are evidence-specific and vary by case:

| Auditor Skill | Output Pattern (filename keywords) | Present? |
|---|---|---|
| `dw-mobile-forensic-auditor` | "Forensic Extraction Audit", "Mobile Forensic" | ✓ or N/A |
| `dw-forensic-dump-analyzer` | "Defense Intelligence Report", "Phone Dump Analysis" | ✓ or N/A |
| `dw-video-evidence-auditor` | "Video Audit", "BWC Audit", "Body Cam" | ✓ or N/A |
| `dw-cell-site-geolocation-auditor` | "CSLI Audit", "Cell Site", "Geolocation" | ✓ or N/A |
| `dw-child-forensic-interview-auditor` | "Forensic Interview Audit", "Child Interview" | ✓ or N/A |
| `dw-confession-interrogation-auditor` | "Interrogation Audit", "Confession", "Miranda" | ✓ or N/A |
| `dw-eyewitness-identification-auditor` | "Identification Audit", "Photo Array", "Lineup" | ✓ or N/A |
| `dw-crime-scene-auditor` | "Crime Scene Audit", "Evidence Audit" | ✓ or N/A |
| `dw-chain-of-custody-auditor` | "Chain of Custody Audit" | ✓ or N/A |
| `dw-expert-witness-evaluator` | "Expert Evaluation", "Daubert", "Expert Report" | ✓ or N/A |
| `dw-social-media-auditor` | "Social Media Audit" | ✓ or N/A |
| `dw-sex-offense-specialist` | "Sex Offense Analysis", "SANE Audit" | ✓ or N/A |

**Mark as N/A** if the case has no evidence of that type. **Mark as missing** if evidence exists (e.g., phone extraction in discovery) but no corresponding audit has been run.

### Step 4C: Scan for Living Monitors & Pre-Trial Motions

Check for the following case-level documents:

| Document | Location | Status |
|---|---|---|
| **Case Brain** | Check DEVONthink via `dw-case-brain` or scan for `CASE BRAIN —` file | ✓ or ✗ |
| **Discovery Compliance Ledger** | `Cowork Analysis/` — look for "Discovery Ledger" or "Compliance Monitor" | ✓ or ✗ |
| **Appellate Error Log** | `Cowork Analysis/` — look for "Error Log" or "Appellate Monitor" | ✓ or ✗ |
| **Pre-Trial Motions Filed** | `02 - Pretrial Notebook → 01 - Pleadings/` — count motion filings | Count |
| **Suppression Motions** | Look for "Motion to Suppress" in Pleadings | ✓ or ✗ |
| **Bond Motions** | Look for "Bond" or "Pretrial Release" in Pleadings | ✓ or ✗ |
| **404(b) Opposition** | Look for "404" or "Prieur" in Pleadings | ✓ or ✗ (only if Prieur notice received) |

**Status Logic:**
- All 9 reports present + all auto-action documents (Missing Discovery Demand, Impeachment Worksheets) + parallel analysis → **Phase 2 Complete** ✓
- 5-8 reports present → **Phase 2 In Progress**
- 0-4 reports present → **Phase 2 Not Started**

### Step 5: Scan Phase 3 Deliverables

Check `Case Tables.xlsx` and `01 - Trial Notebook/`:

| Deliverable | Location | Status |
|-------------|----------|--------|
| Timeline Spreadsheet | `Case Tables.xlsx — Timeline Sheet` (populated with color, links) | ✓ or ✗ |
| Witness Lists (Alpha & Priority) | `Case Tables.xlsx — Witness List - Alpha/Priority sheets` | Check for rows > 0 |
| Defense Matrix | `Case Tables.xlsx — Defense Matrix sheet` | Check for charges + verdicts + defenses |
| Cross-Exam Prep | `01 - Trial Notebook → 03 - Witnesses/` for battle cards, worksheets | Count files |
| Direct-Exam Prep | `01 - Trial Notebook → 03 - Witnesses/` | Count files |
| Case Readiness Memo | Scan root and Trial Notebook for one-page summary | ✓ or ✗ |
| Opening/Closing Prep | Check Trial Notebook for outline or template progress | ✓ or ✗ |

**Status Logic:**
- Timeline + Witness Lists + Defense Matrix populated, Cross/Direct prep docs present → **Phase 3 Complete** ✓
- Timeline + Witness Lists + Defense Matrix only → **Phase 3 Core Items Done** ⚠
- 1-2 items present → **Phase 3 In Progress**
- None present → **Phase 3 Not Started**

### Step 6: Determine Current Phase

Based on Phase 0–3 status:
- **Phase 0 not complete** → Case is in **Intake**
- **Phase 0 complete, Phase 1 not complete** → Case is in **Discovery Processing**
- **Phase 1 complete, Phase 2 not complete** → Case is in **Case Analysis**
- **Phase 2 complete, Phase 3 not complete** → Case is in **Trial Prep**
- **Phase 3 complete** → Case is **Trial-Ready**

### Step 6B: Scan Issue Code Status

Check `Case Tables.xlsx` for an `Issue Codes` sheet (maintained by `dw-issue-code-tracker`).

**If the sheet does NOT exist:**
- In the dashboard output, render this notice in place of the Issue Code Status block: "⚠️ Issue ledger not yet initialized. Run `dw-issue-code-tracker` to set up."
- Skip the rest of this step. Do not error out — graceful degradation.

**If the sheet exists:**
1. **Count rows by `Status`** column: Open, Addressed, N/A, and total.
2. **Group all rows where `Status = Open`** by category (the prefix of the `Code` column):
   - **Universal** — codes prefixed `U-` (always render this category)
   - **Homicide** — codes prefixed `H-` (render only if at least one homicide code is Open)
   - **Rape/Sexual Assault** — codes prefixed `R-` (render only if at least one R-code is Open)
3. **Within each category, sort Open codes ascending by code number** (so `U-01, U-02, U-03...` reads naturally).
4. **Compute the stale flag for each Open code:**
   - Stale = `Status = Open` AND `(today − Last Updated) > 30 days`
   - Use the user's local timezone.
   - Append `⚠️ STALE` to stale codes in the Open list.
5. **If any stale codes exist**, also render a "Stale Issues Summary" sub-block listing each stale code with its `Last Updated` date and the day count since.
6. **If no Open codes are stale**, omit the stale summary entirely.

**Read-only.** This step never modifies the `Issue Codes` sheet. Updates to the ledger are the job of `dw-issue-code-tracker` exclusively.

**No auto-routing.** Do not auto-suggest running a code's linked skill, even for stale codes. Surface the data; the attorney decides.

### Step 7: Flag Workflow Gaps

Check for and flag any of the following:
- Phase 2 reports exist but Phase 1 Master Evidence Table is missing (discovery not properly organized)
- Phase 3 Defense Matrix populated but Phase 2 Red Flags report missing (risks not assessed)
- Impeachment Worksheets exist but no corresponding witnesses in Master Evidence Table (inconsistency)
- Evidence folder has files but Bate Stamp Log is missing (discovery not stamped)
- Case Tables.xlsx missing entirely (critical blocker)

### Step 8: Identify Recommended Next Steps

Based on current phase and gaps, recommend the exact next skill to invoke:

**From Phase 0:**
- If Phase 0 incomplete: "Run **dw-criminal-defense** skill — Phase 0 (Case Intake & Matter Setup)"

**From Phase 1:**
- If Phase 1 incomplete: "Run **dw-criminal-defense** skill — Phase 1 (Prepare Discovery for Review)"
- If Master Evidence Table missing: "Run **dw-criminal-defense** skill — Phase 1 Step 7 (Build the Master Evidence Table)"

**From Phase 2:**
- If Phase 2 incomplete: "Run **dw-criminal-defense** skill — Phase 2 (Case Processing & Analysis)"
- If specific reports missing: "Run **dw-criminal-defense** skill — Phase 2 to generate missing reports (specify which ones)"
- If Constitutional Issues Scan missing: "Run **dw-suppression-motion** for constitutional issues audit"
- If Brady/Giglio Audit missing: "Run **dw-brady-giglio-auditor** across all discovery"
- If Chain of Custody Audit missing: "Run **dw-chain-of-custody-auditor** on evidence logs and lab reports"
- If Impeachment Worksheets missing: "Run **dw-cross-exam-architect** to build cross-exam outlines for key State witnesses"

**From Phase 3:**
- If Phase 3 incomplete: "Run **dw-criminal-defense** skill — Phase 3 (Trial Notebook & Attorney Preparation)"
- If witness prep incomplete: "Run **dw-cross-exam-architect** to generate cross-exam outlines for remaining witnesses"
- If jury selection prep missing: "Run **dw-voir-dire-assistant** for juror analysis and voir dire questions"
- If jury instructions missing: "Run **dw-jury-instructions-builder** for proposed charges and verdict forms"

---

## Dashboard Output Format

**Always produce the dashboard in this exact markdown structure.** Render to console. Optionally save to a `.docx` file if the user requests a written summary.

```markdown
# Case Dashboard
**Client:** [Name] | **Case Number:** [Docket] | **Generated:** [Date]

---

## Current Status
**Current Phase:** [Phase 0 / Phase 1 / Phase 2 / Phase 3 / Trial-Ready]
**Overall Progress:** [0-100%] | [Phase 0: X%, Phase 1: X%, Phase 2: X%, Phase 3: X%]

---

## Phase 0 — Case Intake & Matter Setup
**Status:** ✓ Complete | ⚠ In Progress | ✗ Not Started

### Completed Items ✓
- [x] Folder Setup Complete
- [x] Initial Case Profile
- [x] Criminal Defense Cover
- [x] LWOP Assessment

### Outstanding Items
- [ ] None — Phase 0 complete

### Notes
[Any observations about Phase 0 deliverables]

---

## Phase 1 — Prepare Discovery for Review
**Status:** ✓ Complete | ⚠ In Progress | ✗ Not Started

### Completed Items ✓
- [x] Master Evidence Table (N rows)
- [x] Evidence Folder Organized (N files)
- [x] Bate Stamp Log
- [x] Digital Evidence Placeholders
- [x] Transcripts (N audio/video files)

### Outstanding Items
- [ ] Master Evidence Table (not yet populated)
- [ ] Transcripts (3 of 5 pending)

### Notes
[File count discrepancies, flagged transcripts, etc.]

---

## Phase 2 — Case Processing & Analysis
**Status:** ✓ Complete | ⚠ In Progress | ✗ Not Started

### Completed Reports ✓
- [x] Report 1: Comprehensive Case Timeline
- [x] Report 2: Prosecution's Case Summary
- [x] Report 3: Immediate Red Flags **[HIGH]**
- [x] Report 4: Core Defense Narrative
- [x] Report 5: Viable Legal Defenses
- [x] Report 6: Memorable Theme
- [x] Report 7: Missing Discovery Demand **[HIGH]** + Demand Letter Generated
- [x] Report 8: Witness Table
- [x] Report 9: Impeachment Plan **[HIGH]** + Worksheets Generated

### Parallel Analysis ✓
- [x] Constitutional Issues Scan
- [x] Brady/Giglio Audit
- [x] Witness Cross-Reference
- [x] Timeline Cross-Check
- [x] Chain of Custody Audit

### Outstanding Items
- [ ] Report 3 (Red Flags) — pending review
- [ ] Impeachment Worksheets (6 of 9 key witnesses)

### Notes
[Key findings, flagged items, attorney action items]

---

## Phase 3 — Trial Notebook & Attorney Preparation
**Status:** ✓ Complete | ⚠ In Progress | ✗ Not Started

### Completed Items ✓
- [x] Timeline Spreadsheet (N events, color-coded)
- [x] Witness Lists (Alpha + Priority, N witnesses)
- [x] Defense Matrix (N charges, responsive verdicts, defenses)
- [x] Case Readiness Memo
- [x] Cross-Exam Prep (N witness battle cards)
- [x] Direct-Exam Prep (N defense witness templates)
- [x] Opening/Closing Prep (outlines started)

### Outstanding Items
- [ ] Cross-Exam Prep (3 witnesses remaining)
- [ ] Direct-Exam Prep (2 witnesses remaining)
- [ ] Final Opening Statement
- [ ] Final Closing Argument

### Notes
[Trial readiness summary]

---

## Issue Code Status

**Source:** `Case Tables.xlsx → Issue Codes` sheet (maintained by `dw-issue-code-tracker`)

> ⚠️ Issue ledger not yet initialized. Run `dw-issue-code-tracker` to set up.
> _(Render this notice instead of the block below if the `Issue Codes` sheet does not exist.)_

### Counts

| Status | Count |
|--------|-------|
| Open | [N] |
| Addressed | [N] |
| N/A | [N] |
| **Total** | **[N]** |

### Open Issues by Category

#### Universal ([N] open)
- [U-XX] Issue Name  _(append ⚠️ STALE if applicable)_
- ...

#### Homicide ([N] open) — _omit this category if zero open codes_
- [H-XX] Issue Name  _(append ⚠️ STALE if applicable)_
- ...

#### Rape/Sexual Assault ([N] open) — _omit this category if zero open codes_
- [R-XX] Issue Name  _(append ⚠️ STALE if applicable)_
- ...

### Stale Issues Summary
_(Render this sub-block only if at least one Open code has been Open more than 30 days. Otherwise omit entirely.)_

> ⚠️ **[N] issue(s) have been Open more than 30 days.** Review whether they are still actively being worked or should be reclassified.

- [U-XX] Issue Name — Open since YYYY-MM-DD ([X] days)
- ...

---

## Workflow Gaps & Flags ⚠
- ✗ [Gap description] — impacts [Phase] — recommend [action]
- ✗ [Gap description]

---

## Recommended Next Steps

### Immediate (Priority 1)
1. **Skill:** dw-criminal-defense | Phase 2
   **Action:** Generate missing Case Analysis Reports (specify: Reports 3, 7, 9)
   **Expected Output:** Red Flags doc, Missing Discovery Demand Letter, Impeachment Worksheets
   **Estimated Time:** 2-3 hours

### Next Steps (Priority 2)
2. **Skill:** dw-criminal-defense | Phase 3
   **Action:** Build Cross-Exam templates for key witnesses
   **Expected Output:** Battle Cards, Cross Worksheets
   **Estimated Time:** 1-2 hours

### Future Steps
3. [Subsequent phase work]

---

## Phase Completion Checklist

### Phase 0
- [ ] Folder structure complete
- [ ] Initial Case Profile ✓
- [ ] Criminal Defense Cover ✓
- [ ] LWOP Assessment ✓

**→ Ready for Phase 1:** YES / NO

### Phase 1
- [ ] Master Evidence Table ✓
- [ ] Bate Stamp Log ✓
- [ ] Digital Placeholders ✓
- [ ] Transcripts complete ✓

**→ Ready for Phase 2:** YES / NO

### Phase 2
- [ ] All 9 reports ✓
- [ ] Parallel analyses ✓
- [ ] Missing Discovery Demand ✓
- [ ] Impeachment Worksheets ✓

**→ Ready for Phase 3:** YES / NO

### Phase 3
- [ ] Timeline Spreadsheet ✓
- [ ] Witness Lists ✓
- [ ] Defense Matrix ✓
- [ ] Cross-Exam Prep ✓
- [ ] Direct-Exam Prep ✓
- [ ] Opening/Closing ✓

**→ Ready for Trial:** YES / NO

---

**Generated by Daniels & Washington Case Dashboard | [Timestamp]**
```

---

## Implementation Notes

### Scanning Methodology

Use these methods to check for file presence:

1. **Direct File Check:** Use `os.path.exists()` or equivalent to check for specific named files
2. **Row Count Check:** For Excel sheets, parse `Case Tables.xlsx` and count populated rows (> minimum threshold)
3. **Folder Scan:** List directory contents and look for file name patterns (e.g., files starting with `0[1-9]` for phase 2 reports)
4. **Substring Match:** For report names that may vary slightly, search for report type keywords (e.g., "Timeline", "Red Flags", "Impeachment")

### Error Handling

- **Missing Case Tables.xlsx:** Flag immediately and stop. This is a critical blocker.
- **Folder structure incomplete:** List missing subfolders and flag as workflow gap.
- **Mixed phase deliverables:** Flag inconsistency. Example: "Phase 2 reports exist but Phase 1 Master Evidence Table missing — discovery may not be properly organized."

### Excel Parsing

When reading `Case Tables.xlsx`, check these sheets for population:
- `Evidence Table`: Count rows with data (excluding headers)
- `Timeline Sheet`: Count rows with data
- `Witness Sheet`: Count rows with data
- `Witness List - Alpha` & `Witness List - Priority`: Count rows with data
- `Defense Matrix`: Count charge rows

If a sheet does not exist, note it as missing.

### LWOP Assessment

The LWOP Worksheet is **only required** if charges include:
- Homicide (First Degree, Second Degree, Manslaughter)
- Sex Offenses (Rape, Aggravated Rape, Molestation)

If the case has other charges only, note LWOP as "Not Applicable" in Phase 0 status.

---

## Tips for Accuracy

1. **Ask for the case path first.** Never assume the location — paths vary widely across user systems.
2. **Check for file naming variations.** D&W uses the `[3-digit] - [Name]` convention, but some files may have slight variations (spaces, dashes, underscores). Search for keywords instead of exact matches.
3. **Populate the % complete for each phase.** This gives the user a sense of progress. Formula: `(completed items / total expected items) × 100`
4. **Always include time estimates** for recommended next steps. Attorneys care about how long the work will take.
5. **Flag high-priority items clearly.** RED FLAGS, MISSING DISCOVERY DEMANDS, and IMPEACHMENT WORKSHEETS are attorney decision points — call them out.

---

## Related Skills

- **dw-criminal-defense** — Execute any phase of the 4-phase workflow
- **dw-case-brain** — Load/save persistent case context across sessions
- **dw-issue-code-tracker** — Maintain the case-level issue code ledger (Open/Addressed/N/A). The dashboard reads this ledger read-only; only the tracker writes to it.
- **dw-cross-exam-architect** — Generate cross-examination outlines for witnesses
- **dw-discovery-orchestrator** — Triage and route incoming discovery to auditor skills
- **dw-discovery-compliance-monitor** — Track prosecution disclosure obligations
- **dw-appellate-error-monitor** — Track error preservation throughout proceedings
- **dw-evidence-placeholder** — Generate placeholder PDFs for media evidence folders

---

## Version
Dashboard Skill v1.1 — Added Issue Code Status section reading from `dw-issue-code-tracker` ledger (May 2026)
Dashboard Skill v1.0 — Aligned with dw-criminal-defense SKILL.md (February 2026)


Follow shared protocols for output paths (see Step 0.5).
