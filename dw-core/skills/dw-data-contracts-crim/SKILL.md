---
name: dw-data-contracts-crim
category: core
description: >
  Shared data contracts defining output schemas between Daniels & Washington skills.
  This skill is NOT triggered directly — it is a reference document read by skills that
  produce or consume structured deliverables. It defines the exact filename patterns,
  required fields, and folder locations for DMARs, audit reports, cross-examination outlines,
  Case Tables sheets, and Case Brain entries. If you are building or modifying a D&W skill
  that produces output consumed by other skills, read this file first.
---

# Daniels & Washington — Data Contracts
**Version 1.0 | April 2026 | Internal Reference**

This document defines the output schemas that D&W skills must follow when producing deliverables consumed by other skills. It serves as the contract layer between producer and consumer skills.

**When to read this file:** Before modifying any skill's output format, or when building a new skill that produces deliverables consumed downstream.

This skill is read-only infrastructure — it does not produce attorney deliverables and does not need to load `dw-shared-protocols-crim` (work-product marking, output-path formula). Skills that **consume** these contracts to produce deliverables load shared protocols themselves at their own Step 0.5.

---

**How this file is organized:** each contract below is a one-paragraph summary — producers, consumers, filename pattern, output location. The complete schema (required sections, field tables, enums, consumer behavior) lives in `references/contract-*.md`; read the named file before producing or parsing that deliverable.

---

## Contract 1: Defense Media Analysis Report (DMAR)

**Producers:** `dw-transcript-pipeline-calcasieu-crim`, `dw-transcript-pipeline-rev-crim`
**Consumers:** `dw-confession-interrogation-auditor-crim`, `dw-video-evidence-auditor-crim`, `dw-forensic-dump-analyzer-crim`, `dw-cross-exam-architect-crim`, `dw-dmar-synthesizer-crim`, `dw-case-brain-crim`

Filename `Defense Media Analysis Report — [Client Last Name] [Date].docx`, saved to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`. Ten required sections in fixed order — Header Block (with `Schema Version`, `Date Generated`, `Pipeline`), Media Inventory, Transcript Summaries, Inconsistency Matrix, Miranda & Rights Analysis, Interrogation Technique Detection, Key Event Timeline, Defense Intelligence Brief, Cross-Examination Seeds, and the Barone 6-category Report-vs-Recording Matrix — plus required fields per transcript entry. Read `references/contract-1-dmar.md` now for the full schema.

---

## Contract 2: Auditor Skill Reports

**Producers:** All `dw-*-auditor` skills (mobile-forensic, video-evidence, crime-scene, chain-of-custody, cell-site-geolocation, social-media, eyewitness-identification, confession-interrogation, child-forensic-interview, expert-witness-evaluator, dna-forensic-biology, crime-lab)
**Consumers:** `dw-cross-exam-architect-crim`, `dw-trial-notebook-builder-crim`, `dw-case-dashboard-crim`, `dw-case-brain-crim`

Filename `[Audit Type] Report — [Client Last Name] [Date].docx`, saved to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`. Eight required sections (Executive Summary through Case Brain Registration, including "Key Findings for Cross-Examination") and the four-tier severity definitions (Critical / Significant / Minor / Informational). Read `references/contract-2-auditor-reports.md` now for the full schema.

---

## Contract 3: Cross-Examination Outlines

**Producer:** `dw-cross-exam-architect-crim`
**Consumers:** `dw-trial-notebook-builder-crim`, `dw-case-brain-crim`

Three deliverables per witness — `Cross-Examination — [Witness Name].docx`, `Source Catalog — [Witness Name].pdf`, `Combined Sources — [Witness Name].pdf` — saved to `01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/` or `Defense Witnesses/`. The outline follows the firm's chapter-based template (Chapter Title, Page, Witness, Goals, Source, Questions, Notes). Read `references/contract-3-cross-exam-outlines.md` now for the full schema.

---

## Contract 3A: Direct-Examination Outlines

**Producer:** `dw-direct-exam-architect-crim`
**Consumers:** `dw-trial-notebook-builder-crim`, `dw-case-brain-crim`

Three deliverables per defense witness — `Direct-Examination — [Witness Name].docx`, `Source Catalog — [Witness Name] Direct.pdf`, `Combined Sources — [Witness Name] Direct.pdf` — saved to `01 - Trial Notebook/03 - Witnesses/Defense Witnesses/`. Mirrors the cross-exam template with "Anticipated Cross-Attack Vectors" in place of "Impeachment Hooks" (Witness Role, Foundation Required, open-ended Questions, Anticipated Answers, Exhibits to Introduce, etc.). Read `references/contract-3a-direct-exam-outlines.md` now for the full schema.

---

## Contract 3B: Trial Narrative Deliverables

**Producer:** `dw-trial-narrative-builder-crim`
**Consumers:** `dw-trial-notebook-builder-crim`, `dw-voir-dire-assistant-crim`, `dw-cross-exam-architect-crim`, `dw-direct-exam-architect-crim`, `dw-jury-focus-group-crim`, `dw-case-brain-crim`

Four interlocking deliverables sharing one case theme — Opening Statement Outline, Closing Argument Outline, Theme Tracker, Rebuttal Anticipation Memo (`[Deliverable] — [Client Last Name] [Date].docx`) — canonical copy in `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`, with Opening/Closing optionally mirrored to `01 - Trial Notebook/02 - Opening & Closing/`. Read `references/contract-3b-trial-narrative-deliverables.md` now for each deliverable's required sections and the Theme Tracker columns.

---

## Contract 3C: DNA / Forensic Biology Audit Report

**Producer:** `dw-dna-forensic-biology-auditor-crim`
**Consumers:** `dw-cross-exam-architect-crim`, `dw-trial-notebook-builder-crim`, `dw-expert-witness-evaluator-crim`, `dw-brady-giglio-auditor-crim`, `dw-case-brain-crim`

Filename `DNA Forensic Biology Audit — [Client Last Name] [Date].docx`, saved to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`. Inherits the Contract 2 structure and adds nine DNA-specific sections (evidence inventory, testing methodology, mixture interpretation, statistics, CODIS hit audit, standards compliance, chain-of-custody and analyst cross-references, cross-exam seeds). Read `references/contract-3c-dna-forensic-biology-audit.md` now for the full schema.

---

## Contract 3D: Crime Lab Audit Report (Drug Lab / Toxicology / R.S. 15:499)

**Producer:** `dw-crime-lab-auditor-crim`
**Consumers:** `dw-cross-exam-architect-crim`, `dw-trial-notebook-builder-crim`, `dw-expert-witness-evaluator-crim`, `dw-suppression-motion-crim`, `dw-drug-offense-specialist-crim`, `dw-dwi-specialist-crim`, `dw-brady-giglio-auditor-crim`, `dw-case-brain-crim`

Filename `Crime Lab Audit — [Client Last Name] [Date].docx`, saved to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`. Inherits the Contract 2 structure and adds ten crime-lab sections, including the R.S. 15:499 / 15:501 certificate-and-demand audit, methodology, QC, weight audit, Confrontation Clause posture, and cross-exam seeds. Read `references/contract-3d-crime-lab-audit.md` now for the full schema.

---

## Contract 4: Case Tables.xlsx Sheet Schemas

**Shared Resource:** `Case Tables.xlsx` at case root
**Writers:** `dw-criminal-defense-crim` (creates), Phase 2 and 3 skills (populate)
**Readers:** `dw-case-dashboard-crim`, `dw-trial-notebook-builder-crim`, `dw-cross-exam-architect-crim`

Column schemas for the 7-column Evidence Table (an admissibility worksheet as of v6.1), the Timeline Sheet, and the 4-column Witness List, each with type, populator, and required flag. `Case Tables.xlsx` carries three sheets as of v6.0. Read `references/contract-4-case-tables-sheets.md` now for the column tables.

---

## Contract 5: Case Brain Registration Entry

**Producer:** Any skill that generates a deliverable
**Consumer:** `dw-case-brain-crim` (writes to Obsidian), `dw-trial-notebook-builder-crim` (reads), `dw-case-dashboard-crim` (reads)

Defines the one-line COMPANION SKILL OUTPUTS entry format (date | skill-name | output filename | folder path relative to case root) and the OPEN ISSUES checkbox format for attorney action items. Read `references/contract-5-case-brain-registration.md` now for the exact formats and example.

---

## Contract 6: Discovery Compliance Ledger

**Producer:** `dw-discovery-compliance-monitor-crim`
**Consumers:** `dw-brady-giglio-auditor-crim`, `dw-criminal-defense-crim` (Phase 2 Report 7), `dw-case-dashboard-crim`

Ten required columns (Item, Category, Discovery Bucket 1–7, Demanded Date, Demanded In, Produced Date, Production Set, Bate Range, Notes, Brady Flag), saved to `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`. Read `references/contract-6-discovery-compliance-ledger.md` now for the column table.

---

## How to Use This Document

**If you are a PRODUCING skill:**
1. Read the contract for your output type before generating any deliverable
2. Ensure your output matches the filename pattern, required sections, and field requirements
3. Save to the specified output location
4. Register with Case Brain per Contract 5

**If you are a CONSUMING skill:**
1. Read the contract for the input you expect
2. Validate that the file exists at the expected location with the expected filename pattern
3. If the input is missing or malformed, report the specific contract violation rather than failing silently
4. Never assume fields exist — check for them and handle missing data gracefully

**If you are MODIFYING a skill's output format:**
1. Update this data-contracts document FIRST
2. Then update the producing skill
3. Then verify all consuming skills still work with the new format
4. Log the change in the producing skill's changelog

---

## Contract 7: Jail-Call Tampering-Risk Cross-Feed

**Producer:** `dw-jail-call-analyzer-crim` (Module D)
**Consumer:** `dw-witness-threat-matrix-crim` (Post-Cross Refresh Mode and initial-build threat scoring)

Carries Module D witness-contact, threat, coaching, and coordination findings into the threat matrix so Vulnerability scores and Top 5 ranks reflect the tampering signal. Filename `Jail-Call Tampering Risk Cross-Feed — [Client Last Name] [Date].md`, saved alongside the jail-call audit at `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`. Defines the required header, the per-entry field schema (`witness_id`, `severity`, `pattern_type`, `recommended_action`, etc.), consumer scoring behavior, and the schema-drift policy. Read `references/contract-7-jail-call-tampering-cross-feed.md` now for the full schema.

---

## Contract Versioning

| Contract | Version | Last Updated | Breaking Changes |
|----------|---------|-------------|-----------------|
| DMAR | 1.0 | April 2026 | Initial — May 2026: required Schema Version + Date Generated + Pipeline fields in Header Block |
| Auditor Reports | 1.0 | April 2026 | Initial — added "Key Findings for Cross-Examination" section |
| Cross-Exam Outlines | 1.0 | April 2026 | Initial |
| Direct-Exam Outlines (3A) | 1.0 | May 2026 | Initial — added for `dw-direct-exam-architect-crim` |
| Trial Narrative Deliverables (3B) | 1.0 | May 2026 | Initial — Opening, Closing, Theme Tracker, Rebuttal Anticipation Memo for `dw-trial-narrative-builder-crim` |
| DNA / Forensic Biology Audit Report (3C) | 1.0 | May 2026 | Initial — added for `dw-dna-forensic-biology-auditor-crim` |
| Crime Lab Audit Report (3D) | 1.0 | May 2026 | Initial — added for `dw-crime-lab-auditor-crim` |
| Case Tables Sheets | 1.0 | April 2026 | Initial |
| Case Brain Registration | 1.0 | April 2026 | Initial |
| Discovery Compliance Ledger | 1.0 | April 2026 | Initial |
| Jail-Call Tampering Cross-Feed | 1.0 | May 2026 | Initial |

---

*Version 1.1 — May 2026. Added Contracts 3A (Direct-Exam Outlines from `dw-direct-exam-architect-crim`) and 3B (Trial Narrative Deliverables from `dw-trial-narrative-builder-crim`). Updated Contract 2 producer list to include the new `dw-dna-forensic-biology-auditor-crim` and `dw-crime-lab-auditor-crim` skills.*
*Version 1.0 — April 2026. Created as part of the D&W skill architecture consolidation.*
*Version 1.2 — May 2026 (Barone Discovery Workflow Audit). Added DMAR Section 10 (Report-vs-Recording Matrix, 6-category Barone). Added Certainty column to Timeline Sheet schema. Added Discovery Bucket column to Discovery Compliance Ledger.*
*Version 1.1 — May 2026. Added Contract 7 (jail-call tampering cross-feed) and DMAR Header Block schema-version metadata.*

---

## Quick References

Full schemas in the `references/` subdirectory (one file per contract):

- **contract-1-dmar.md** — Contract 1: DMAR header block, ten required sections, Barone 6-category matrix, per-transcript fields
- **contract-2-auditor-reports.md** — Contract 2: auditor report sections, filename examples, severity definitions
- **contract-3-cross-exam-outlines.md** — Contract 3: three cross-exam deliverables and chapter-template fields
- **contract-3a-direct-exam-outlines.md** — Contract 3A: three direct-exam deliverables and 8-column template
- **contract-3b-trial-narrative-deliverables.md** — Contract 3B: opening, closing, theme tracker, rebuttal memo schemas
- **contract-3c-dna-forensic-biology-audit.md** — Contract 3C: DNA-specific audit sections
- **contract-3d-crime-lab-audit.md** — Contract 3D: crime-lab audit sections incl. R.S. 15:499 certificate audit
- **contract-4-case-tables-sheets.md** — Contract 4: Evidence Table, Timeline, and Witness List column schemas
- **contract-5-case-brain-registration.md** — Contract 5: COMPANION SKILL OUTPUTS and OPEN ISSUES entry formats
- **contract-6-discovery-compliance-ledger.md** — Contract 6: ledger column schema
- **contract-7-jail-call-tampering-cross-feed.md** — Contract 7: cross-feed header, per-entry fields, consumer behavior, schema-drift policy
