# Integration Map — What This Skill Reads and Feeds

`dw-data-contracts-crim` is the binding contract layer. This skill is a declared **consumer** of the DMAR and Auditor Report contracts and the **producer** of Contract 3 (Cross-Examination Outlines). Read that skill before changing any filename or output path here.

---

## Reads from

| Source | Contract / output | Used at |
|---|---|---|
| `dw-transcript-pipeline-calcasieu-crim` (JusticeText, Calcasieu) · `dw-transcript-pipeline-rev-crim` (Rev, all other parishes) | **DMAR** — §4 Inconsistency Matrix, §7 Key Event Timeline, §9 Cross-Examination Seeds, §10 Report-vs-Recording Matrix (Barone 6-category, with CRITICAL/SIGNIFICANT/MINOR severity) | 0.58 |
| `dw-transcript-router-crim` | Routes untranscribed proceedings to the correct pipeline by parish | 0.58 |
| The `dw-evidence-audit` skills | **Auditor Report** §6 Key Findings for Cross-Examination — each with finding, source reference, and suggested line of questioning | 0.58 |
| `dw-witness-statement-analyzer-crim` | Witness Analysis Cards; Conflict Matrix | 0.58, 5 |
| `dw-brady-giglio-auditor-crim` | Disclosure gaps, cooperator benefits, officer credibility material. **Mandatory** before any cooperator or officer-credibility cross | 0.58, 3 |
| `dw-crime-lab-auditor-crim` | Analyst file, accreditation, SOP, calibration, proficiency. Required before any forensic cross | 3 |
| `dw-dmar-synthesizer-crim` | Cross-case witness comparison — multi-case, co-defendant, or joined matters only | 0.58 |
| `dw-theory-deconstructor-crim` · `dw-trial-narrative-builder-crim` | Case theme (the chapter spine) and theory vulnerabilities | 0.58, 1 |
| `dw-adversarial-stress-test-crim` | Theory stress-test findings — the cross must not open a door the theory cannot survive | 0.58, 8.5 |
| `dw-case-brain-crim` | `CASE_ROOT`, parish, court, docket, and every caption variable | 0.5, 0.55 |
| `dw-witness-threat-matrix-crim` | Ranked witness damage/vulnerability scores, where already built | 0.6 |

## Hands off to

| Consumer | What it takes |
|---|---|
| `dw-appellate-error-monitor-crim` | The completed **Preservation Log** — rulings, grounds stated, proffers made, and anything marked UNPRESERVED |
| `dw-issue-code-tracker-crim` | Issue codes from the Preservation Log |
| `dw-trial-notebook-builder-crim` | The outline, by its Contract 3 filename |
| `dw-case-brain-crim` | Output registration — skill name, filenames, date, location |
| `dw-trial-day-assistant-crim` | The outline itself, used at counsel table; its witness scorecard feeds tomorrow's cross back into this skill |

## Direction warning

`dw-adversarial-stress-test-crim` runs **into** this skill, not out of it. It tests the defense theory (gated on the Theory Selection Memo and Theory Deconstruction) and its cross module simulates the *State* crossing *defense* witnesses. Its own routing table sends witness-preparation work here. Never hand it a finished cross outline — run the Step 8.5 self-check instead.

## Not covered

**Criminal only.** No civil or PI cross-examination: La. C.E. art. 611(B) carries a narrower proviso for civil cases where an adverse party calls a witness for specific matters, and these modules do not map to treating physicians, defense IME examiners, or accident reconstructionists. Defense-witness direct examination goes to `dw-direct-exam-architect-crim` (Contract 3A).
