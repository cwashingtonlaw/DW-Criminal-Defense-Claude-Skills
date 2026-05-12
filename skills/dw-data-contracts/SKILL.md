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
| Page | Reference page in source documents | Yes |
| Witness | Full name of the witness | Yes |
| Goals | What this chapter aims to establish | Yes |
| Source | Bate stamp or document reference | Yes |
| Questions | Specific questions in non-leading form (Who/What/When/Where/Why/How/Describe/Tell) | Yes |
| Anticipated Cross-Attack Vectors | Predicted state cross attacks on this material with rebuttal preparation | Yes |
| Notes | Attorney notes, evidentiary flags, foundation requirements | Optional |

### Output Location
`01 - Trial Notebook/03 - Witnesses/Defense Witnesses/`

---

## Contract 3B: Trial Narrative Deliverables (Opening + Closing)

**Producer:** `dw-trial-narrative-builder`
**Consumers:** `dw-trial-notebook-builder`, `dw-case-brain`, `dw-appellate-error-monitor`

### Four Deliverables (built in pairs — opening and closing built together for theme coherence)

| # | Deliverable | Format | Filename Pattern |
|---|------------|--------|-----------------|
| 1 | Opening Statement | .docx | `Opening Statement — [Client Last Name] [YYYY-MM-DD].docx` |
| 2 | Closing Argument | .docx | `Closing Argument — [Client Last Name] [YYYY-MM-DD].docx` |
| 3 | Theme Tracker | .xlsx | `Theme Tracker — [Client Last Name] [YYYY-MM-DD].xlsx` |
| 4 | Rebuttal Anticipation Memo | .docx | `Rebuttal Anticipation Memo — [Client Last Name] [YYYY-MM-DD].docx` |

### Opening Statement Required Sections
1. Hook / Opening Line — memorable first sentence
2. Defense Story-Arc Preview (situation → conflict → defense theory) — preview, not argument (La. C.Cr.P. Art. 765/774)
3. Burden Framing — what the State must prove and the reasonable-doubt anchor
4. Theme Registration (3-5 themes, verbatim phrases) — these are tagged in the Theme Tracker for callback in closing
5. Exhibit Foreshadowing — 3-5 exhibits the jury will see
6. Closing Line — memorable image the jury carries into the State's case

### Closing Argument Required Sections
1. Theme Callback to Opening — verbatim phrase repetition from opening themes
2. Burden Hammer — reasonable doubt, presumption of innocence, State's burden
3. Jury Instruction Walk-Through — reasonable doubt definition (Cage v. Louisiana / In re Winship), lesser-included responsive verdicts, affirmative-defense burden if applicable
4. Evidence-Keyed Defense Story — each piece of defense evidence mapped to its supporting theme
5. State Rebuttal Anticipation Block — predicted state rebuttal points with woven pre-rebuttal lines (see Rebuttal Anticipation Memo)
6. Closing Line — defense theme final image

### Theme Tracker (.xlsx) Required Columns

| Column | Type | Required |
|--------|------|----------|
| Theme # | Integer | Yes |
| Theme Text | Text (3-7 words, verbatim phrase) | Yes |
| Opening Registration | Text (page/section reference in opening) | Yes |
| Mid-Trial Reinforcement | Text (witness/exhibit/cross moment) | Optional |
| Closing Callback | Text (section reference in closing) | Yes |
| Status | Dropdown (Registered / Reinforced / Dropped) | Yes |
| Notes | Text | No |

### Rebuttal Anticipation Memo Required Sections
For each predicted state rebuttal point:
1. What the State will likely say (predicted language)
2. Why it's wrong (legal or factual rebuttal)
3. Pre-rebuttal line woven into defense closing (verbatim)
4. Fallback objection if state rebuttal exceeds scope (La. C.Cr.P. Art. 774 grounds)

### Output Location
`01 - Trial Notebook/02 - Opening & Closing/`

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
| Direct-Exam Outlines (3A) | 1.0 | May 2026 | Initial — mirrors Cross-Exam with 8-column structure; "Impeachment Hooks" → "Anticipated Cross-Attack Vectors" |
| Trial Narrative Deliverables (3B) | 1.0 | May 2026 | Initial — Opening Statement, Closing Argument, Theme Tracker, Rebuttal Anticipation Memo |
| Case Tables Sheets | 1.0 | April 2026 | Initial |
| Case Brain Registration | 1.0 | April 2026 | Initial |
| Discovery Compliance Ledger | 1.0 | April 2026 | Initial |

---

*Version 1.1 — May 2026. Added Contracts 3A (Direct-Exam Outlines from `dw-direct-exam-architect`) and 3B (Trial Narrative Deliverables from `dw-trial-narrative-builder`). Updated Contract 2 producer list to include the new `dw-dna-forensic-biology-auditor` and `dw-crime-lab-auditor` skills.*
*Version 1.0 — April 2026. Created as part of the D&W skill architecture consolidation.*