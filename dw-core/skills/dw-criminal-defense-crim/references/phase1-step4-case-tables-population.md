# Phase 1 Step 4 — Build Case Tables (Population Detail)

Read from SKILL.md **Phase 1 Step 4** — Evidence Table column-by-column population, Review Priority and Defense Relevance rules, Witness List columns and 1–5 ranking, and the Step 4 Check.

⚠ **Follow the Case Tables Write Protocol before modifying this file.** See "Case Tables Write Protocol" section above.

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

**4b — Witness List** (`Witness List` sheet — single consolidated sheet)
Extract every witness name encountered during discovery organization and transcription. Enter each on the one `Witness List` sheet, sorted **alphabetically by Last, First**. `Priority (1–5)` is a sortable column — do not keep separate alpha/priority sheets.

Columns: Witness Name (Last, First) | Address | Role | Type | Priority (1–5) | Priority Rationale | Bate Ref (Statement) | Bate Ref (Other) | Connection to Case | Key Testimony Expected | Impeachment Issues | Exam Prep (Y/N) | Notes

**Rank every witness 1–5** using the first-match decision rule in `references/witness-priority-rubric.md` (1 – Critical … 5 – Peripheral). Read the selected defense theory from the Case Profile FIRST, then rank each witness by importance to that theory and to the State's burden. Write the rank as `N – Label` and record the defense-theory-specific justification in **Priority Rationale**. Flag unconfirmed roles as `5 (prov.)` and re-rank as discovery arrives.

**✓ Step 4 Check:**
- [ ] Evidence Table row count matches file count in Evidence Folder
- [ ] Review Priority populated for every row in Evidence Table
- [ ] Defense Relevance populated for every row in Evidence Table
- [ ] Witness List populated, sorted alphabetically, and ranked 1–5 per witness-priority-rubric.md (Priority Rationale completed for each)
