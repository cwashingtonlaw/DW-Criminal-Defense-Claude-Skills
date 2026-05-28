# Rec 03 — DMAR 6-Category Report-vs-Recording Matrix

## Summary
Add a **Report-vs-Recording Matrix** to the DMAR schema. This is a systematic, 6-category comparison of what official reports say versus what recordings actually show. One matrix per officer/report-recording pair.

## The 6 Categories
1. **Narrative Match** — Does the report account match the recording?
2. **Omissions** — What does the report leave out that the recording shows?
3. **Additions** — What does the report claim that the recording doesn't show?
4. **Timing Discrepancies** — Do report timestamps match recording timestamps?
5. **Quote Accuracy** — Do reported quotes match what was actually said?
6. **Procedural Compliance** — Do procedures described match procedures shown?

Each discrepancy: Report citation | Recording citation | Discrepancy description | Severity (CRITICAL / SIGNIFICANT / MINOR)

## Files Modified

### 1. `dw-data-contracts/SKILL.md`
- Added Section 10 (Report-vs-Recording Matrix) to Contract 1 DMAR Required Sections
- Full 6-category table with comparison descriptions and defense significance

### 2. `dw-video-evidence-auditor/SKILL.md`
- Added new STEP 3A (Report-vs-Recording Matrix) between STEP 3 and STEP 4
- Updated STEP 4 audit report structure to include Report-vs-Recording Matrix section

### 3. `dw-transcript-pipeline-calcasieu/SKILL.md`
- Added SECTION 4A (Report-vs-Recording Matrix) to DMAR Structure in Phase 6
- Includes all 6 subcategories (4A.1 through 4A.6)

### 4. `dw-transcript-pipeline-rev/SKILL.md`
- Added Phase 4A (Report-vs-Recording Matrix) between Phase 4 and Phase 5
- Updated Phase 5 reference to include Section 4A in DMAR structure

### 5. `dw-dmar-synthesizer/SKILL.md`
- Added Module S4A (Report-vs-Recording Cross-Case Comparison) between S4 and S5
- Compares matrices across cases: same officer/different reports, same event/different officers, institutional patterns
