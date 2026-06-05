# Trial Notebook Deliverable Map

This is the complete reference of every deliverable the Trial Notebook Builder scans for,
organized by Trial Notebook tab. Each entry includes the expected file location, the upstream
skill that produces it, the phase it's created in, and whether it's critical for trial.

Read this file before every scan to ensure nothing is missed.

---

## Tab 1 — Jury Instructions & Selection

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| Proposed Jury Charges (defense) | `01 - Jury Instructions & Selection/` | `dw-jury-instructions-builder-crim` | 3 | YES |
| Verdict Form with Responsive Verdicts | `01 - Jury Instructions & Selection/` | `dw-jury-instructions-builder-crim` | 3 | YES |
| Art 814 Responsive Verdicts Analysis | `01 - Jury Instructions & Selection/` | `dw-jury-instructions-builder-crim` | 3 | YES |
| Self-Defense / Justification Instructions | `01 - Jury Instructions & Selection/` | `dw-jury-instructions-builder-crim` | 3 | Conditional |
| Ramos Instruction (unanimity) | `01 - Jury Instructions & Selection/` | `dw-jury-instructions-builder-crim` | 3 | YES |
| Voir Dire Question Outline | `01 - Jury Instructions & Selection/` | `dw-voir-dire-assistant-crim` | 3 | Recommended |
| Juror Questionnaire (if court permits) | `01 - Jury Instructions & Selection/` | `dw-voir-dire-assistant-crim` | 3 | Recommended |
| Strike List / Tracking Sheet | `01 - Jury Instructions & Selection/` | `dw-voir-dire-assistant-crim` | 3-4 | Recommended |
| Batson Compliance Documentation | `01 - Jury Instructions & Selection/` | `dw-voir-dire-assistant-crim` | 4 | Recommended |
| Juror Analysis Cards | `01 - Jury Instructions & Selection/` | `dw-voir-dire-assistant-crim` | 4 | Recommended |

## Tab 2 — Opening & Closing

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| Opening Statement Outline | `02 - Opening & Closing/` | `dw-criminal-defense-crim` (Phase 3, Step 9) | 3 | YES |
| Closing Argument Outline | `02 - Opening & Closing/` | `dw-criminal-defense-crim` (Phase 3, Step 9) | 3 | Recommended |
| Mapping the Story — Opening | `02 - Opening & Closing/` | `dw-criminal-defense-crim` (Phase 3, Step 9) | 3 | Recommended |
| Mapping the Story — Closing | `02 - Opening & Closing/` | `dw-criminal-defense-crim` (Phase 3, Step 9) | 3 | Recommended |
| Memorable Theme Document (Report 6) | `09 - Case Analysis/` (cross-ref) | `dw-criminal-defense-crim` (Phase 2) | 2 | Recommended |

## Tab 3 — Witnesses

### Prosecution Witnesses

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| Cross-Examination Outline (.docx) — per key witness | `03 - Witnesses/Prosecution Witnesses/` | `dw-cross-exam-architect-crim` | 3 | YES |
| Source/Exhibit Document Catalog (.pdf) — per witness | `03 - Witnesses/Prosecution Witnesses/` | `dw-cross-exam-architect-crim` | 3 | YES |
| Combined Source Documents (.pdf) — per witness | `03 - Witnesses/Prosecution Witnesses/` | `dw-cross-exam-architect-crim` | 3 | Recommended |
| Impeachment Worksheet — per key witness | `03 - Witnesses/` | `dw-criminal-defense-crim` (Phase 2, Step 4) | 2 | YES |
| Witness Battle Card — per key witness | `03 - Witnesses/Prosecution Witnesses/` | `dw-criminal-defense-crim` (Phase 3, Step 7A) | 3 | Recommended |
| Mapping the Cross Worksheet | `03 - Witnesses/Prosecution Witnesses/` | `dw-criminal-defense-crim` (Phase 3, Step 7B) | 3 | Recommended |

### Defense Witnesses

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| Direct Exam Template — per defense witness | `03 - Witnesses/Defense Witnesses/` | `dw-criminal-defense-crim` (Phase 3, Step 8) | 3 | Recommended |
| Mapping the Direct Worksheet | `03 - Witnesses/Defense Witnesses/` | `dw-criminal-defense-crim` (Phase 3, Step 8A) | 3 | Recommended |

### Expert Witnesses

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| Expert Witness Evaluation (Art. 702) | `03 - Witnesses/` or separate Expert subfolder | `dw-expert-witness-evaluator-crim` | 2-3 | Conditional |
| Daubert/Foret Challenge Brief | `03 - Witnesses/` | `dw-expert-witness-evaluator-crim` | 3 | Conditional |

## Tab 4 — Exhibit List

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| Master Exhibit List | `04 - Exhibit List/` | Manual / `dw-criminal-defense-crim` | 3-4 | YES |
| Exhibit Authentication Notes | `04 - Exhibit List/` | Manual | 3-4 | Recommended |
| Stipulated Exhibits List | `04 - Exhibit List/` | Manual / negotiation with State | 4 | Recommended |

## Tab 5 — Evidence

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| All Bate-Stamped Discovery Documents | `05 - Evidence/` | `dw-criminal-defense-crim` (Phase 1) | 1 | YES |
| Digital Evidence Placeholder PDFs | `05 - Evidence/` | `dw-evidence-placeholder-crim` | 1 | YES |
| Transcripts (all A/V) | `05 - Evidence/` | `dw-transcript-router-crim` | 1 | YES |

## Tab 6 — Motions in Limine

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| Motion to Suppress (if applicable) | `06 - Motions in Limine/` or Pretrial Pleadings | `dw-suppression-motion-crim` | 2-3 | Conditional |
| 404(b) Opposition (if Prieur notice filed) | `06 - Motions in Limine/` or Pretrial Pleadings | `dw-404b-opposition-crim` | 3 | Conditional |
| Other Motions in Limine | `06 - Motions in Limine/` | `dw-pretrial-motion-library-crim` | 3 | Conditional |

## Tab 7 — Legal Research

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| Legal Memoranda | `07 - Legal Research/` | Various | 2-3 | Recommended |
| Statutory Compilations | `07 - Legal Research/` | Various | 2-3 | Recommended |

## Tab 8 — Jury Selection Notes

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| Juror Analysis Cards | `08 - Jury Selection Notes/` | `dw-voir-dire-assistant-crim` | 4 | Recommended |
| Panel Composition Tracking | `08 - Jury Selection Notes/` | `dw-voir-dire-assistant-crim` | 4 | Recommended |
| Cause Challenge Documentation | `08 - Jury Selection Notes/` | `dw-voir-dire-assistant-crim` | 4 | Recommended |

## Tab 9 — Case Analysis

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| Report 1: Comprehensive Case Timeline | `Case Tables.xlsx — Timeline Sheet` | `dw-criminal-defense-crim` (Phase 2) | 2 | YES |
| Report 2: Prosecution's Case Summary | `09 - Case Analysis/` | `dw-criminal-defense-crim` (Phase 2) | 2 | Recommended |
| Report 3: Immediate Red Flags | `09 - Case Analysis/` | `dw-criminal-defense-crim` (Phase 2) | 2 | YES |
| Report 4: Core Defense Narrative | `09 - Case Analysis/` | `dw-criminal-defense-crim` (Phase 2) | 2 | YES |
| Report 5: Viable Legal Defenses | `09 - Case Analysis/` | `dw-criminal-defense-crim` (Phase 2) | 2 | Recommended |
| Report 6: Memorable Theme | `09 - Case Analysis/` | `dw-criminal-defense-crim` (Phase 2) | 2 | Recommended |
| Report 7: Table of Missing Discovery | `09 - Case Analysis/` | `dw-criminal-defense-crim` (Phase 2) | 2 | YES |
| Report 8: Witness Table | `Case Tables.xlsx — Witness List` | `dw-criminal-defense-crim` (Phase 2) | 2 | Recommended |
| Report 9: Key Witness Impeachment Plan | `09 - Case Analysis/` | `dw-criminal-defense-crim` (Phase 2) | 2 | YES |
| Missing Discovery Demand Letter | `09 - Case Analysis/Cowork Analysis/` | `dw-criminal-defense-crim` (Phase 2, Auto) | 2 | YES |
| Constitutional Issues Scan | `09 - Case Analysis/Cowork Analysis/` | `dw-criminal-defense-crim` (Phase 2) | 2 | Recommended |
| Brady/Giglio Checklist | `09 - Case Analysis/Cowork Analysis/` | `dw-brady-giglio-auditor-crim` | 2 | YES |
| Witness Cross-Reference Map | `09 - Case Analysis/Cowork Analysis/` | `dw-criminal-defense-crim` (Phase 2) | 2 | Recommended |
| Chain of Custody Audit | `09 - Case Analysis/Cowork Analysis/` | `dw-chain-of-custody-auditor-crim` | 2 | Recommended |

## Case Root — Supporting Documents

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| Case Tables.xlsx | Case root | `dw-criminal-defense-crim` (all phases) | 0+ | YES |
| Case Readiness Memo | Case root or Tab 9 | `dw-criminal-defense-crim` (Phase 3, Step 5) | 3 | Recommended |
| Discover the Story Worksheet | Case root or Tab 9 | `dw-criminal-defense-crim` (Phase 3, Step 6) | 3 | Recommended |
| Attorney Review Checklist | Case root | `dw-criminal-defense-crim` (Phase 2, Step 6) | 2 | Recommended |

## Pretrial Notebook — Trial-Relevant Items

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| Initial Case Profile | `02 - Pretrial/03 - Case Analysis & Notes/` | `dw-criminal-defense-crim` (Phase 0) | 0 | Reference |
| LWOP Worksheet (if applicable) | `02 - Pretrial/03 - Case Analysis & Notes/` | `dw-lwop-populator` | 0 | Conditional |
| Criminal Defense Cover | `02 - Pretrial/03 - Case Analysis & Notes/` | `dw-criminal-defense-crim` (Phase 0) | 0 | Reference |
| Suppression Motion (filed) | `02 - Pretrial/01 - Pleadings/` | `dw-suppression-motion-crim` | 2-3 | Conditional |
| Bond Reduction Motion | `02 - Pretrial/01 - Pleadings/` | `dw-bond-and-release-motion-crim` | 1-2 | Reference |
| Pretrial Motions (various) | `02 - Pretrial/01 - Pleadings/` | `dw-pretrial-motion-library-crim` | 2-3 | Reference |
| Discovery Compliance Ledger | `02 - Pretrial/02 - Discovery/` | `dw-discovery-compliance-monitor-crim` | 1+ | Reference |
| Habitual Offender Audit | `02 - Pretrial/03 - Case Analysis & Notes/` | `dw-habitual-offender-auditor-crim` | 2-3 | Conditional |
| Plea Analysis | `02 - Pretrial/03 - Case Analysis & Notes/` | `dw-plea-negotiation-analyzer-crim` | 2-3 | Conditional |
| Sentencing Mitigation Package | `01 - Trial/` or `02 - Pretrial/` (varies) | `dw-sentencing-mitigation-specialist-crim` | 3-4 | Conditional |

## Specialist Audit Reports (May Be in Case Analysis or Pretrial)

| Deliverable | Expected Location | Producing Skill | Phase | Critical? |
|------------|-------------------|-----------------|-------|-----------|
| Eyewitness ID Audit | `09 - Case Analysis/Cowork Analysis/` | `dw-eyewitness-identification-auditor-crim` | 2-3 | Conditional |
| Confession/Interrogation Audit | `09 - Case Analysis/Cowork Analysis/` | `dw-confession-interrogation-auditor-crim` | 2-3 | Conditional |
| Child Forensic Interview Audit | `09 - Case Analysis/Cowork Analysis/` | `dw-child-forensic-interview-auditor-crim` | 2-3 | Conditional |
| Cell Site / CSLI Audit | `09 - Case Analysis/Cowork Analysis/` | `dw-cell-site-geolocation-auditor-crim` | 2-3 | Conditional |
| Mobile Forensic (Methodology) Audit | `09 - Case Analysis/Cowork Analysis/` | `dw-mobile-forensic-auditor-crim` | 2-3 | Conditional |
| Phone Dump Content Analysis | `09 - Case Analysis/Cowork Analysis/` | `dw-forensic-dump-analyzer-crim` | 2-3 | Conditional |
| Video Evidence Audit | `09 - Case Analysis/Cowork Analysis/` | `dw-video-evidence-auditor-crim` | 2-3 | Conditional |
| Social Media Audit | `09 - Case Analysis/Cowork Analysis/` | `dw-social-media-auditor-crim` | 2-3 | Conditional |
| Crime Scene Audit | `09 - Case Analysis/Cowork Analysis/` | `dw-crime-scene-auditor-crim` | 2-3 | Conditional |
| Appellate Error Preservation Log | Case root or `09 - Case Analysis/` | `dw-appellate-error-monitor-crim` | 3-4 | Recommended |
| Defense Media Analysis Report | `09 - Case Analysis/Cowork Analysis/` | `dw-transcript-router-crim` | 1-2 | Conditional |

---

## Criticality Legend

- **YES** — Must exist before trial. If missing, listed as a Critical Gap.
- **Recommended** — Valuable for trial preparation but trial can proceed without it. Listed as Non-Critical Gap.
- **Conditional** — Only relevant if the case involves that issue (e.g., LWOP worksheet only if LWOP exposure exists, 404(b) opposition only if Prieur notice was filed). If the issue exists and the deliverable is missing, treat as Critical.
- **Reference** — Background document that informs trial preparation but isn't used directly in trial. Not listed as a gap.

---

## How to Use This Map

1. **Before scanning:** Read this file to know what to look for.
2. **During scanning:** Check each deliverable against the case folder.
3. **After scanning:** Any deliverable marked YES or Conditional (where the condition applies) that is MISSING goes into the Critical Gaps section of the Trial Readiness Gap Report. Any Recommended deliverable that is missing goes into Non-Critical Gaps.
4. **For gap remediation:** The "Producing Skill" column tells the attorney exactly which skill to invoke to create the missing deliverable.
