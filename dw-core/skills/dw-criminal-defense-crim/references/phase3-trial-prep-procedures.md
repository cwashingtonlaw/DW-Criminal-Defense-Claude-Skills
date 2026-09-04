# Phase 3 — Trial Notebook & Attorney Preparation (Detailed Procedures)

Read from SKILL.md **Phase 3 Steps 1–11** — the complete per-step procedure text (Timeline columns and rules, Witness List update and strategy routing, version control, readiness memo, story worksheet, cross/direct exam prep 6A–6C and 7A–7B, opening/closing, appellate readiness, trial-day support, notebook assembly).

### Step 1: Case Timeline Spreadsheet
Built from **Report 1** (Comprehensive Case Timeline) → `Case Tables.xlsx — Timeline Sheet`

⚠ **Follow the Case Tables Write Protocol.** See `references/case-tables-write-protocol.md`.

Columns to populate: Start Date | Start Time | End Date | End Time | Title | Subtitle | Description | Tags (Cowork Flags) | Certainty | Bate Stamp | Notes

Rules:
- Sort all events in strict chronological order
- Apply color coding per `references/color-coding.md` (Timeline Sheet section): prosecution events (light red) | defense-favorable (light green) | neutral (white)
- Hyperlink Source Doc column to corresponding file in Evidence Folder where possible
- Flag any timeline event that conflicts with another document in the Cowork Flags column
- Maintain all existing color coding, dropdown lists, and formatting

### Step 2: Update Witness List
The `Witness List` sheet was initially populated in Phase 1 Step 4. Now update it with intelligence from Phase 2's case analysis:

⚠ **Follow the Case Tables Write Protocol.** See `references/case-tables-write-protocol.md`.

The sheet carries four columns — `Witness Name` | `Role in Case` | `Priority` | `Key Evidence Sources` — and nothing else. Keep it that way; depth belongs in the witness worksheets, not the spreadsheet.

- **Re-rank `Priority`** per `references/witness-priority-rubric.md` now that the defense theory (Report 4a) and impeachment plan (Report 8) are known. Apply the rubric's Brady/Giglio modifier (bump one step toward 1) where Report 8 identifies impeachment material.
- **Update `Key Evidence Sources`** with the Bate refs and file names of every statement, report, recording, and exhibit tied to that witness, comma-separated.
- **Refine `Role in Case`** where discovery has clarified a provisional role; drop the `(prov.)` flag once confirmed.
- Impeachment detail, ranking rationale, addresses, and exam-prep status are tracked in Report 8 and the per-witness worksheets in `01 - Trial Notebook/03 - Witnesses/` — **not** on this sheet.

Specialist routing from this step:
- Witness threat ranking (Damage × Vulnerability) → **dw-witness-threat-matrix-crim**
- Jury instruction research and drafting, driven by the Report 4a theory → **dw-jury-instructions-builder-crim**
- Voir dire strategy → **dw-voir-dire-assistant-crim**

### Step 3: Version Control — Amended & Superseded Documents
When the prosecution sends corrected or supplemental productions:

⚠ **Follow the Case Tables Write Protocol.** See `references/case-tables-write-protocol.md`.

- Maintain a version control log to keep the Master Evidence Table accurate
- Mark superseded documents clearly in the Evidence Table
- Do not delete prior versions — archive with notation

### Step 4: Case Readiness Memo
The attorney's single entry point into the Trial Notebook — one-page summary of everything the attorney needs to know before diving into the file.

Inputs: all 8 case analysis reports, Cowork parallel analysis, current case status

### Step 5: Discover the Story Worksheet (Case Story Development)
Complete before witness preparation begins. This is the foundation of the defense narrative and informs all witness examination preparation.

### Step 6: Cross Exam Preparation (Per Key Witness)
*Attorney work — Cowork prepopulates templates with available intelligence. Route specialist witness types to appropriate skills. Complete for all Key Witness Impeachment Plan witnesses and Top 10 priority witnesses only.*

**6A — Witness Cross Battle Card:** one-page intelligence summary per witness
- **Eyewitness to crime** → route to **dw-eyewitness-identification-auditor-crim** for ID weakness analysis
- **Law enforcement officer** → route to **dw-cross-exam-architect-crim** for hostile witness strategy
- **Expert witness (prosecution)** → route to **dw-expert-witness-evaluator-crim** for methodology challenges
- **Save location:** `01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/`

**6B — Mapping the Cross Worksheet:** prepopulate from impeachment materials, Report 8, and all prior statements. Route to **dw-cross-exam-architect-crim** for strategic question mapping.

**6C — Cross Exam Template:** prepopulate structure and available impeachment points; leave question sequencing and line of attack to attorney. Route specialized witness cross (confessions, interrogation tactics, mobile forensics, video authentication) to appropriate specialist skills.

### Step 7: Direct Exam Preparation (Per Defense Witness)
*Attorney work — Cowork prepopulates templates with intelligence from Discover the Story worksheet and Witness Dossiers.*

**7A — Mapping the Direct Worksheet**

**7B — Direct Exam Template**
- **Save location:** `01 - Trial Notebook/03 - Witnesses/Defense Witnesses/`

### Step 8: Opening Statement & Closing Argument Preparation
*Attorney-driven — Cowork populates the framework from case analysis outputs.*

Populate the Mapping the Story templates (Opening and Closing) from: Report 4 (Competing Defense Theories — use the attorney-selected theory from Report 4a), Report 6 (Memorable Theme), and the Discover the Story worksheet.

### Step 9: Appellate Readiness
*Post-conviction and during trial preparation — monitor for appealable issues.*

Route preservation of trial error, evidentiary challenges, and appellate strategy to **dw-appellate-error-monitor-crim** to ensure all grounds for appeal are documented and preserved for post-conviction review.

After verdict and sentence, when the appellate record is designated and the ranked-issue output from `dw-appellate-error-monitor-crim` is in hand, route brief drafting to **dw-appellate-brief-builder-crim** for the direct-appeal brief (assignments of error, statement of facts with record cites, per-assignment argument structured as standard of review → preservation → law → application → prejudice, and reply brief). For collateral relief (PCR, federal habeas, sentence modification) instead of direct appeal, route to **dw-post-conviction-relief-crim**.

### Step 10: Trial Day Support
*During trial — fast-cycle, in-court support.*

Route real-time trial-day support to **dw-trial-day-assistant-crim** for: daily docket, real-time objection log (which feeds upstream to **dw-appellate-error-monitor-crim**), witness scorecards (which feed **dw-cross-exam-architect-crim** for next-day prep), exhibit tracker, juror observation log including Batson tracking, end-of-day recap with overnight tasks, and mid-trial issue spotter (Brady, surprise testimony, mistrial triggers under La. C.Cr.P. Art. 770/771). The trial-day assistant produces short, scannable outputs designed for use during breaks and at counsel table — final polish rolls into the trial notebook via Step 12.

### Step 11: Assemble Trial Notebook
*Final assembly — triggered when all Phase 3 deliverables are complete.*

Route to **dw-trial-notebook-builder-crim** to assemble all Phase 2 and Phase 3 deliverables into the final Trial Notebook. The trial notebook builder scans the case folder for all upstream deliverables, organizes them into the Trial Notebook folder structure, generates a master index, and produces a Trial Readiness Gap Report identifying any missing items.
