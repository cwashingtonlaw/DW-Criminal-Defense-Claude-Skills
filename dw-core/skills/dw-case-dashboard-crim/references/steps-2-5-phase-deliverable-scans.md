# Steps 2–5 — Phase Deliverable Scan Tables

Read from SKILL.md **Steps 2, 3, 4, 4B, 4C and 5** — the deliverable tables, file-name patterns, auditor-output patterns, living-monitor checks, and the status logic for Phases 0–3.

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
| 4 | Competing Defense Theories | Scan for `04 - Competing Theories...` or `04 - Defense Narrative...` | Standard |
| 4a | Theory Selection Memo | Scan for `Theory Selection Memo` (attorney-selected) | **HIGH** |
| 5 | Viable Legal Defenses | Scan for `05 - Legal Defenses...` | Standard |
| 6 | Memorable Theme | Scan for `06 - Memorable Theme...` | Standard |
| 7 | Missing Discovery Demand | Check for auto-generated demand letter | **HIGH** |
| 8 | Key Witness Impeachment Plan | Scan for `09 - Impeachment...` or witness worksheets | **HIGH** |

Also check:
- `02 - Pretrial Notebook → 03 - Case Analysis & Notes → Cowork Analysis/` folder for Constitutional, Brady, Witness Cross-Reference, Timeline, Chain of Custody analyses
- `02 - Pretrial Notebook → 06 - Law & Research/` for Missing Discovery Demand Letter
- `01 - Trial Notebook → 03 - Witnesses/` for Impeachment Worksheets

### Step 4B: Scan for Auditor Skill Outputs (Phase 2)

Scan the `Cowork Analysis/` folder for deliverables from specialist auditor skills. These are evidence-specific and vary by case:

| Auditor Skill | Output Pattern (filename keywords) | Present? |
|---|---|---|
| `dw-mobile-forensic-auditor-crim` | "Forensic Extraction Audit", "Mobile Forensic" | ✓ or N/A |
| `dw-forensic-dump-analyzer-crim` | "Defense Intelligence Report", "Phone Dump Analysis" | ✓ or N/A |
| `dw-video-evidence-auditor-crim` | "Video Audit", "BWC Audit", "Body Cam" | ✓ or N/A |
| `dw-cell-site-geolocation-auditor-crim` | "CSLI Audit", "Cell Site", "Geolocation" | ✓ or N/A |
| `dw-child-forensic-interview-auditor-crim` | "Forensic Interview Audit", "Child Interview" | ✓ or N/A |
| `dw-confession-interrogation-auditor-crim` | "Interrogation Audit", "Confession", "Miranda" | ✓ or N/A |
| `dw-eyewitness-identification-auditor-crim` | "Identification Audit", "Photo Array", "Lineup" | ✓ or N/A |
| `dw-crime-scene-auditor-crim` | "Crime Scene Audit", "Evidence Audit" | ✓ or N/A |
| `dw-chain-of-custody-auditor-crim` | "Chain of Custody Audit" | ✓ or N/A |
| `dw-expert-witness-evaluator-crim` | "Expert Evaluation", "Daubert", "Expert Report" | ✓ or N/A |
| `dw-social-media-auditor-crim` | "Social Media Audit" | ✓ or N/A |
| `dw-sex-offense-specialist-crim` | "Sex Offense Analysis", "SANE Audit" | ✓ or N/A |

**Mark as N/A** if the case has no evidence of that type. **Mark as missing** if evidence exists (e.g., phone extraction in discovery) but no corresponding audit has been run.

### Step 4C: Scan for Living Monitors & Pre-Trial Motions

Check for the following case-level documents:

| Document | Location | Status |
|---|---|---|
| **Case Brain** | Check DEVONthink via `dw-case-brain-crim` or scan for `CASE BRAIN —` file | ✓ or ✗ |
| **Discovery Compliance Ledger** | `Cowork Analysis/` — look for "Discovery Ledger" or "Compliance Monitor" | ✓ or ✗ |
| **Appellate Error Log** | `Cowork Analysis/` — look for "Error Log" or "Appellate Monitor" | ✓ or ✗ |
| **Pre-Trial Motions Filed** | `02 - Pretrial Notebook → 01 - Pleadings/` — count motion filings | Count |
| **Suppression Motions** | Look for "Motion to Suppress" in Pleadings | ✓ or ✗ |
| **Bond Motions** | Look for "Bond" or "Pretrial Release" in Pleadings | ✓ or ✗ |
| **404(b) Opposition** | Look for "404" or "Prieur" in Pleadings | ✓ or ✗ (only if Prieur notice received) |

**Status Logic:**
- All 8 reports present (Reports 1–8, plus the attorney-selected Report 4a Theory Selection Memo) + all auto-action documents (Missing Discovery Demand, Impeachment Worksheets) + parallel analysis → **Phase 2 Complete** ✓
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
