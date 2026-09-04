# Dashboard Output Format — Markdown Template

Read from the SKILL.md **Dashboard Output Format** section — the exact markdown structure every dashboard must follow, including the Issue Code Status block and the Phase Completion Checklist.

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
- [x] Report 4: Competing Defense Theories
- [x] Report 4a: Theory Selection Memo **[HIGH]**
- [x] Report 5: Viable Legal Defenses
- [x] Report 6: Memorable Theme
- [x] Report 7: Missing Discovery Demand **[HIGH]** + Demand Letter Generated
- [x] Report 8: Key Witness Impeachment Plan **[HIGH]** + Worksheets Generated

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
- [x] Witness List (N witnesses)
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

**Source:** Case Tables.xlsx → `Issue Codes` sheet (maintained by `dw-issue-code-tracker-crim` v2.0)

If the `Issue Codes` sheet does not exist, display:
> ⚠️ Issue ledger not yet initialized. Run `dw-issue-code-tracker-crim` to set up.

Otherwise, render this block:

### Counts

| Status | Count |
|--------|-------|
| Open | {N_open} |
| Addressed | {N_addressed} |
| N/A | {N_na} |
| **Total** | **{N_total}** |

### Open Issues by Category

#### Universal ({N_open_universal} open)
- [U-XX] Issue Name {⚠️ if stale}
- ...

#### Homicide ({N_open_homicide} open)  _[only if applicable]_
- [H-XX] Issue Name {⚠️ if stale}
- ...

#### Rape/Sexual Assault ({N_open_rape} open)  _[only if applicable]_
- [R-XX] Issue Name {⚠️ if stale}
- ...

### Stale Flag Logic

For each row in the `Issue Codes` sheet:
- If `Status` = `Open` AND (today − `Last Updated`) > 30 days → append ⚠️ STALE marker
- If no Open codes are stale, omit the stale section entirely

### Stale Issues Summary

If any stale codes exist, display:
> ⚠️ **{N_stale} issue(s) have been Open more than 30 days.** Review whether they are still actively being worked or should be reclassified.

List each stale code with its `Last Updated` date:
- [U-07] Eyewitness Identification — Open since 2026-03-15 ({X} days)
- ...

---

## Workflow Gaps & Flags ⚠
- ✗ [Gap description] — impacts [Phase] — recommend [action]
- ✗ [Gap description]

---

## Recommended Next Steps

### Immediate (Priority 1)
1. **Skill:** dw-criminal-defense-crim | Phase 2
   **Action:** Generate missing Case Analysis Reports (specify: Reports 3, 7, 9)
   **Expected Output:** Red Flags doc, Missing Discovery Demand Letter, Impeachment Worksheets
   **Estimated Time:** 2-3 hours

### Next Steps (Priority 2)
2. **Skill:** dw-criminal-defense-crim | Phase 3
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
- [ ] All 8 reports ✓
- [ ] Parallel analyses ✓
- [ ] Missing Discovery Demand ✓
- [ ] Impeachment Worksheets ✓

**→ Ready for Phase 3:** YES / NO

### Phase 3
- [ ] Timeline Spreadsheet ✓
- [ ] Witness List ✓
- [ ] Cross-Exam Prep ✓
- [ ] Direct-Exam Prep ✓
- [ ] Opening/Closing ✓

**→ Ready for Trial:** YES / NO

---

**Generated by Daniels & Washington Case Dashboard | [Timestamp]**
```
