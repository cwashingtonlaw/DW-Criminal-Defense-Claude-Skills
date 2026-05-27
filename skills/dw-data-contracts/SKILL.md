---
name: dw-data-contracts
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

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## Contract 1: Defense Media Analysis Report (DMAR)

**Producers:** `dw-transcript-pipeline-calcasieu`, `dw-transcript-pipeline-rev`
**Consumers:** `dw-confession-interrogation-auditor`, `dw-video-evidence-auditor`, `dw-forensic-dump-analyzer`, `dw-cross-exam-architect`, `dw-dmar-synthesizer`, `dw-case-brain`

### Filename Pattern
`Defense Media Analysis Report — [Client Last Name] [Date].docx`

### Required Sections (in order)
1. **Header Block** — Client name, docket number, date generated, parish, platform used
2. **Media Inventory** — Table of all media files processed with: filename, duration, file type, speaker count, transcription status
3. **Transcript Summaries** — Per-file summary with: key statements (with timestamps), speakers identified, topics covered
4. **Inconsistency Matrix** — Cross-file contradictions: who said what, where it conflicts, timestamp references for both
5. **Miranda & Rights Analysis** — Whether rights were administered, timing, waiver status, any issues (applies to interrogation recordings only — mark N/A for other media types)
6. **Interrogation Technique Detection** — Reid technique markers, leading questions, coercion indicators, minimization/maximization (applies to interrogation recordings only — mark N/A for other media types)
7. **Key Event Timeline** — Chronological timeline of significant events across all media files with timestamps and source file references
8. **Defense Intelligence Brief** — Actionable findings organized by: favorable to defense, unfavorable to defense, requires further investigation
9. **Cross-Examination Seeds** — Specific contradictions, omissions, or procedural issues that can be used in cross-examination, with source references

### Required Fields per Transcript Entry
- Source filename (must match filename in evidence folder)
- Duration (HH:MM:SS)
- Speaker labels (consistent across all entries)
- Transcript text with timestamps at minimum 30-second intervals
- Confidence flags for uncertain transcription segments

### Output Location
`01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

---

## Contract 2: Auditor Skill Reports

**Producers:** All `dw-*-auditor` skills (mobile-forensic, video-evidence, crime-scene, chain-of-custody, cell-site-geolocation, social-media, eyewitness-identification, confession-interrogation, child-forensic-interview, expert-witness-evaluator, dna-forensic-biology, crime-lab)
**Consumers:** `dw-cross-exam-architect`, `dw-trial-notebook-builder`, `dw-case-dashboard`, `dw-case-brain`

### Filename Pattern
`[Audit Type] Report — [Client Last Name] [Date].docx`

Examples:
- `Mobile Forensic Extraction Audit — Cole 2026-04-01.docx`
- `Video Evidence Audit — Tezeno 2026-03-15.docx`
- `Chain of Custody Audit — Nicholas 2026-03-20.docx`
- `DNA Audit Report — Cole 2026-05-10.docx`
- `Crime Lab Audit Report — Cole 2026-05-10.docx`

### Required Sections (all auditor reports must include)
1. **Executive Summary** — 2-3 paragraph overview of findings and significance
2. **Evidence Examined** — List of specific items audited with Bate stamp references
3. **Methodology** — What standards/protocols were applied (SWGDE, NIST, agency policy, etc.)
4. **Findings** — Detailed findings organized by severity: Critical, Significant, Minor, Informational
5. **Defense Implications** — How each finding affects the defense case
6. **Key Findings for Cross-Examination** — Bullet list of specific points that can be used to challenge evidence or impeach witnesses. Each point must include: the finding, the source reference (Bate stamp or document), and a suggested line of questioning.
7. **Recommendations** — Suggested next steps (motions to file, experts to retain, additional investigation)
8. **Case Brain Registration** — Skill name, output filename, date, location (per the Register Output with Case Brain protocol)

### Severity Definitions
- **Critical**: Evidence should be excluded or case outcome materially affected
- **Significant**: Weakens prosecution's case or supports defense theory
- **Minor**: Procedural deficiency that may not affect admissibility but can be raised
- **Informational**: Noted for completeness but unlikely to affect case

### Output Location
`01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

---

## Contract 3: Cross-Examination Outlines

**Producer:** `dw-cross-exam-architect`
**Consumers:** `dw-trial-notebook-builder`, `dw-case-brain`

### Three Deliverables per Witness

| # | Deliverable | Format | Filename Pattern |
|---|------------|--------|-----------------|
| 1 | Cross-Examination Outline | .docx | `Cross-Examination — [Witness Name].docx` |
| 2 | Source/Exhibit Document Catalog | .pdf | `Source Catalog — [Witness Name].pdf` |
| 3 | Combined Source Documents | .pdf | `Combined Sources — [Witness Name].pdf` |

### Cross-Examination Outline Required Structure
The outline uses the firm's chapter-based template format:

| Field | Description | Required |
|-------|-------------|----------|
| Chapter Title | Topic area for this line of questioning | Yes |
| Page | Reference page in source documents | Yes |
| Witness | Full name of the witness | Yes |
| Goals | What this chapter aims to establish | Yes |
| Source | Bate stamp or document reference | Yes |
| Questions | Specific questions in leading format | Yes |
| Notes | Attorney notes, anticipated responses, follow-up strategy | Optional |

### Output Location
`01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/` or `Defense Witnesses/`

---

## Contract 3A: Direct-Examination Outlines

**Producer:** `dw-direct-exam-architect`
**Consumers:** `dw-trial-notebook-builder`, `dw-case-brain`

### Three Deliverables per Defense Witness

| # | Deliverable | Format | Filename Pattern |
|---|------------|--------|-----------------|
| 1 | Direct-Examination Outline | .docx | `Direct-Examination — [Witness Name].docx` |
| 2 | Source/Exhibit Document Catalog | .pdf | `Source Catalog — [Witness Name] Direct.pdf` |
| 3 | Combined Source Documents | .pdf | `Combined Sources — [Witness Name] Direct.pdf` |

### Direct-Examination Outline Required Structure
The outline uses the firm's chapter-based template format with an 8-column structure. The Direct-Exam template mirrors the Cross-Exam template with one substitution — "Impeachment Hooks" → "Anticipated Cross-Attack Vectors":

| Field | Description | Required |
|-------|-------------|----------|
| Chapter Title | Topic area for this line of questioning | Yes |
| Witness | Full name of the witness | Yes |
| Witness Role | Defense witness, character witness, alibi, expert, etc. | Yes |
| Goals | What this chapter aims to establish for the defense theory | Yes |
| Foundation Required | Predicate facts, qualifications, or admissibility predicates that must be laid first | Yes |
| Questions | Open-ended, non-leading questions (who/what/when/where/how/why/describe/explain) | Yes |
| Anticipated Answers | Expected substance of the witness's testimony, drawn from witness interviews | Yes |
| Exhibits to Introduce | Exhibit numbers and authentication method (cross-reference Exhibit List) | Optional |
| Source | Bate stamp, witness interview memo, or document reference | Yes |
| Anticipated Cross / Redirect Notes | Vulnerabilities to address on direct; topics to reserve for redirect | Optional |
| Notes | Attorney notes, witness preparation flags, demeanor cues | Optional |

### Output Location

`01 - Trial Notebook/03 - Witnesses/Defense Witnesses/`

---

## Contract 3B: Trial Narrative Deliverables

**Producer:** `dw-trial-narrative-builder`
**Consumers:** `dw-trial-notebook-builder`, `dw-voir-dire-assistant`, `dw-cross-exam-architect`, `dw-direct-exam-architect`, `dw-jury-focus-group`, `dw-case-brain`

The trial-narrative-builder produces four interlocking deliverables that share a common case theme.

### Four Deliverables

| # | Deliverable | Format | Filename Pattern |
|---|------------|--------|-----------------|
| 1 | Opening Statement Outline | .docx | `Opening Statement — [Client Last Name] [Date].docx` |
| 2 | Closing Argument Outline | .docx | `Closing Argument — [Client Last Name] [Date].docx` |
| 3 | Theme Tracker | .docx | `Theme Tracker — [Client Last Name] [Date].docx` |
| 4 | Rebuttal Anticipation Memo | .docx | `Rebuttal Anticipation Memo — [Client Last Name] [Date].docx` |

### Opening Statement Outline — Required Sections

1. **Header Block** — Case caption, docket, charges, trial date, lead attorney, defense theme (one line)
2. **Hook / Primacy Opener** — First 60 seconds, theme-driven
3. **Story of the Case** — Defense narrative in chronological or thematic order, no argument
4. **Introduction of Defendant** — Humanizing facts admissible in opening
5. **Roadmap of the Evidence** — Witnesses the jury will hear, exhibits they will see
6. **Burden of Proof Reminder** — Reasonable doubt framing
7. **Promise to the Jury / Ask** — What the verdict should be and why
8. **Objection Risk Notes** — Argument vs. statement, vouching, future-evidence pledges
9. **Theme References** — Cross-reference to Theme Tracker entries

### Closing Argument Outline — Required Sections

1. **Header Block** — Same as Opening
2. **Theme Restatement** — Tie back to opening theme
3. **Burden and Reasonable Doubt** — Jury instruction quotations
4. **Element-by-Element Walk** — Each charged element, the State's proof, the gap, the defense response (cross-reference Defense Matrix)
5. **Witness Credibility** — Per-witness impeachment summary (cross-reference Cross-Examination outlines)
6. **Exhibit Highlights** — Key exhibits the jury should re-examine in deliberation
7. **Anticipated State Rebuttal Responses** — Cross-reference Rebuttal Anticipation Memo
8. **Verdict Form Walk-Through** — Walk the jury through the verdict form (cross-reference Jury Instructions / Verdict Form)
9. **Closing Ask** — Specific verdict requested, charge-by-charge

### Theme Tracker — Required Structure

A living document that records every place the case theme is reinforced across the trial file.

| Column | Type | Required |
|--------|------|----------|
| Theme Element | Text (short phrase, e.g., "Rushed investigation") | Yes |
| Source | Text (witness, exhibit, motion, voir dire question) | Yes |
| Bate Stamp / Reference | Text | Yes |
| Used In | Text (Opening / Cross of [Witness] / Direct of [Witness] / Closing / Voir Dire) | Yes |
| Notes | Text | No |

### Rebuttal Anticipation Memo — Required Sections

1. **Header Block** — Same as Opening
2. **Predicted State Themes** — What the prosecutor is likely to argue
3. **Predicted State Rebuttal Points** — Anticipated responses to defense closing
4. **Defense Counter-Points** — Pre-drafted responses, with sources and exhibit references
5. **Improper-Argument Triggers** — Golden Rule, vouching, burden-shifting, Bossier-style errors — and preserved-objection language
6. **Appellate Preservation Flags** — Cross-reference to `dw-appellate-error-monitor`

### Output Location

All four deliverables: `01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

The Opening Statement and Closing Argument outlines may also be mirrored to `01 - Trial Notebook/02 - Opening & Closing/` for courtroom-ready access; the Cowork Analysis copy is the canonical work-product version.

---

## Contract 3C: DNA / Forensic Biology Audit Report

**Producer:** `dw-dna-forensic-biology-auditor`
**Consumers:** `dw-cross-exam-architect`, `dw-trial-notebook-builder`, `dw-expert-witness-evaluator`, `dw-brady-giglio-auditor`, `dw-case-brain`

### Filename Pattern

`DNA Forensic Biology Audit — [Client Last Name] [Date].docx`

### Required Sections

Inherits the Contract 2 (Auditor Skill Reports) structure (Executive Summary, Evidence Examined, Methodology, Findings, Defense Implications, Key Findings for Cross-Examination, Recommendations, Case Brain Registration), with these DNA-specific additions:

1. **Evidence Inventory** — Per-item table: item number, source (swab/cutting/reference), collection date, collector, lab item number
2. **Testing Methodology Audit** — Extraction method, quantification platform, amplification kit (Identifiler/Fusion/GlobalFiler), capillary electrophoresis instrument, allele-calling thresholds
3. **Mixture Interpretation** — Number of contributors, deconvolution method, probabilistic genotyping software (STRmix / TrueAllele / EuroForMix), version, validation status, parameter set used
4. **Statistical Calculations** — Likelihood ratio or RMP, propositions tested, reference population database used, sub-population correction (theta)
5. **CODIS / Database Hit Audit** — If applicable: hit confirmation, moderate/high stringency, candidate match procedure
6. **Standards Compliance Check** — SWGDAM, ISO/IEC 17025, lab accreditation body (ANAB / A2LA), validation studies
7. **Chain of Custody Cross-Reference** — Cross-reference to `dw-chain-of-custody-auditor` findings for the same items
8. **Analyst Credentials & Discipline History** — Cross-reference to `dw-expert-witness-evaluator`
9. **Cross-Examination Seeds** — Mixture interpretation challenges, stochastic threshold issues, drop-in / drop-out assumptions, contamination indicators

### Output Location

`01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

---

## Contract 3D: Crime Lab Audit Report (Drug Lab / Toxicology / R.S. 15:499)

**Producer:** `dw-crime-lab-auditor`
**Consumers:** `dw-cross-exam-architect`, `dw-trial-notebook-builder`, `dw-expert-witness-evaluator`, `dw-suppression-motion`, `dw-drug-offense-specialist`, `dw-dwi-specialist`, `dw-brady-giglio-auditor`, `dw-case-brain`

### Filename Pattern

`Crime Lab Audit — [Client Last Name] [Date].docx`

### Required Sections

Inherits the Contract 2 (Auditor Skill Reports) structure with these crime-lab-specific additions:

1. **Report Inventory** — Per-report table: lab name, report date, evidence item numbers, analyst, test type (controlled substance / blood alcohol / urine toxicology / breath alcohol)
2. **R.S. 15:499 Certificate Audit** — Whether a Certificate of Analysis under La. R.S. 15:499 was issued, whether the State filed a notice of intent to use it under La. R.S. 15:501, whether the defense filed a timely demand for the analyst to testify under La. R.S. 15:501(B), and the resulting confrontation posture under *Melendez-Diaz* / *Bullcoming*
3. **Testing Methodology Audit** — For controlled substances: presumptive vs. confirmatory testing, GC-MS / FTIR / Raman / microcrystalline; for toxicology: GC headspace, enzymatic, immunoassay vs. confirmatory; for breath: Intoxilyzer model, calibration interval, simulator solution lot
4. **Standards Compliance Check** — SWGDRUG (drugs), SOFT/ANSI (tox), NHTSA (DUI), ISO/IEC 17025 accreditation, lab accreditation body
5. **Quality Control Audit** — Blanks, positive controls, duplicates, calibration verification, batch QC review, instrument maintenance log
6. **Quantity / Weight Audit** — Net vs. gross weight, packaging weight subtracted, balance calibration, statutory threshold proximity (for tiered offenses)
7. **Chain of Custody Cross-Reference** — Cross-reference to `dw-chain-of-custody-auditor`
8. **Analyst Credentials & Discipline History** — Cross-reference to `dw-expert-witness-evaluator`; flag any *Brady*/*Giglio* impeachment material for routing to `dw-brady-giglio-auditor`
9. **Confrontation Clause Posture** — Sixth Amendment / La. Const. Art. I § 16 analysis of who must testify at trial
10. **Cross-Examination Seeds** — Methodology gaps, QC failures, R.S. 15:499 notice/demand timing, calibration / maintenance, analyst bias

### Output Location

`01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

---

## Contract 4: Case Tables.xlsx Sheet Schemas

**Shared Resource:** `Case Tables.xlsx` at case root
**Writers:** `dw-criminal-defense` (creates), Phase 2 and 3 skills (populate)
**Readers:** `dw-case-dashboard`, `dw-trial-notebook-builder`, `dw-cross-exam-architect`

### Evidence Table Sheet

| Column | Type | Populated By | Required |
|--------|------|-------------|----------|
| Doc # | Text (3-digit) | Auto from filename | Yes |
| Evidence Type | Text | Auto from file type | Yes |
| Name | Text | Auto from filename | Yes |
| Description | Text | Staff | Yes |
| Bate Stamp | Text | Auto from Bate Log | Yes |
| Reviewed (Y/N) | Dropdown | Staff/Attorney | Yes |
| Notes | Text | Staff/Attorney | No |
| Discovery Set | Text | Auto from Download Log | Yes |
| Date of Delivery | Date | Auto from Download Log | Yes |
| Review Priority | HIGH/MED/LOW | Cowork AI | Yes |
| Defense Relevance | FAVORABLE/NEUTRAL/FLAG | Cowork AI | Yes |

### Timeline Sheet

| Column | Type | Required |
|--------|------|----------|
| Start Date | Date | Yes |
| Start Time | Time | No |
| End Date | Date | No |
| End Time | Time | No |
| Title | Text | Yes |
| Subtitle | Text | No |
| Description | Text | Yes |
| Tags (Cowork Flags) | Text | No |
| Bate Stamp | Text | Yes |
| Notes | Text | No |

### Witness Sheet

| Column | Type | Required |
|--------|------|----------|
| Name | Text | Yes |
| Witness Type | Text (Prosecution/Defense/Expert) | Yes |
| Association | Text | Yes |
| Sources (Bate stamps) | Text | Yes |
| Trial Exam Prepared (Y/N) | Dropdown | Yes |

### Defense Matrix Sheet

| Column | Type | Required |
|--------|------|----------|
| Charge | Text (includes La. R.S. citation) | Yes |
| Elements | Text | Yes |
| Responsive Verdicts | Text | Yes |
| Defense(s) | Text | Yes |
| Evidence Supporting Defense | Text | Yes |
| Notes | Text | No |

---

## Contract 5: Case Brain Registration Entry

**Producer:** Any skill that generates a deliverable
**Consumer:** `dw-case-brain` (writes to Obsidian), `dw-trial-notebook-builder` (reads), `dw-case-dashboard` (reads)

### COMPANION SKILL OUTPUTS Entry Format

Each entry in the Case Brain's COMPANION SKILL OUTPUTS section must follow this format:

```
- **[Date]** | `[skill-name]` | [Output filename] | [folder path relative to case root]
```

Example:
```
- **2026-04-01** | `dw-mobile-forensic-auditor` | Mobile Forensic Extraction Audit — Cole 2026-04-01.docx | 01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/
```

### OPEN ISSUES Entry Format (when audit identifies attorney action items)

```
- [ ] [Brief description of issue] — from `[skill-name]` ([date])
```

---

## Contract 6: Discovery Compliance Ledger

**Producer:** `dw-discovery-compliance-monitor`
**Consumers:** `dw-brady-giglio-auditor`, `dw-criminal-defense` (Phase 2 Report 7), `dw-case-dashboard`

### Required Columns

| Column | Type | Required |
|--------|------|----------|
| Item | Text | Yes |
| Category | Text (Document/Physical/Digital/Witness) | Yes |
| Demanded Date | Date | Yes |
| Demanded In | Text (motion/letter reference) | Yes |
| Produced Date | Date or "OUTSTANDING" | Yes |
| Production Set | Text | If produced |
| Bate Range | Text | If produced |
| Notes | Text | No |
| Brady Flag | Yes/No | Yes |

### Output Location
`01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

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

## Contract Versioning

| Contract | Version | Last Updated | Breaking Changes |
|----------|---------|-------------|-----------------|
| DMAR | 1.0 | April 2026 | Initial |
| Auditor Reports | 1.1 | May 2026 | Producer list expanded to include `dw-dna-forensic-biology-auditor` and `dw-crime-lab-auditor` |
| Cross-Exam Outlines | 1.0 | April 2026 | Initial |
| Direct-Exam Outlines (3A) | 1.0 | May 2026 | Initial — added for `dw-direct-exam-architect` |
| Trial Narrative Deliverables (3B) | 1.0 | May 2026 | Initial — Opening, Closing, Theme Tracker, Rebuttal Anticipation Memo for `dw-trial-narrative-builder` |
| DNA / Forensic Biology Audit Report (3C) | 1.0 | May 2026 | Initial — added for `dw-dna-forensic-biology-auditor` |
| Crime Lab Audit Report (3D) | 1.0 | May 2026 | Initial — added for `dw-crime-lab-auditor` |
| Case Tables Sheets | 1.0 | April 2026 | Initial |
| Case Brain Registration | 1.0 | April 2026 | Initial |
| Discovery Compliance Ledger | 1.0 | April 2026 | Initial |

---

*Version 1.1 — May 2026. Added Contracts 3A (Direct-Exam Outlines from `dw-direct-exam-architect`) and 3B (Trial Narrative Deliverables from `dw-trial-narrative-builder`). Updated Contract 2 producer list to include the new `dw-dna-forensic-biology-auditor` and `dw-crime-lab-auditor` skills.*
*Version 1.0 — April 2026. Created as part of the D&W skill architecture consolidation.*