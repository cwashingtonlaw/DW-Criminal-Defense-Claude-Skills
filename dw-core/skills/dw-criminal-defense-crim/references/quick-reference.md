# Quick Reference

This file consolidates lookup tables and convention references for the dw-criminal-defense-crim skill. SKILL.md points here from each phase rather than duplicating these tables inline.

For folder structure and document naming conventions, see `folder-structure-and-naming.md`.
For spreadsheet color coding specs, see `color-coding.md`.

---

## Cowork Action Types

| Symbol | Meaning |
|---|---|
| ⚡ **COWORK ACTION** | Claude executes this step |
| ⚠ **STAFF ACTION** | Human staff executes; Claude may assist or verify |
| ⚖ **ATTORNEY ACTION** | Attorney-only; Claude prepopulates supporting materials only |
| ✓ **QUALITY GATE** | Must be confirmed before advancing to next phase |
| 📋 **TEMPLATE GUIDE** | Reference for populating a specific document |

---

## Case Tables.xlsx — Sheet Reference

The master template in `assets/Case Tables.xlsx` contains all sheets below with pre-formatted headers, column structures, dropdowns, and color coding. Copy it to new case roots; never create sheets from scratch.

| Sheet Name | Contents | Phase Populated |
|------------|----------|-----------------|
| Evidence Table | Master discovery index (11 columns) | Phase 1 Step 4 |
| Timeline Sheet | Chronological case events (10 columns) | Phase 2 Report 1 / Phase 3 Step 1 |
| Witness List | Consolidated witness list (13 columns), alphabetical by Last, First, with sortable Priority (1–5) column — replaces the former Witness Sheet / Alpha / Priority sheets | Phase 1 Step 4 → Phase 3 Step 2 |
| Defense Matrix | Charges, responsive verdicts, defenses (7 columns) | Phase 3 Step 3B |
| Legal Defenses (Rape) | **Defense Shield template** — sex offense defense catalog (7 columns) | Phase 3 Step 3A (sex offense cases only) |
| Legal Defenses (Homicide) | **Defense Shield template** — homicide defense catalog (7 columns) | Phase 3 Step 3A (homicide cases only) |
| Legal Defenses ([Case Type]) | **Defense Shield template** — created for new case types as needed (7 columns) | Phase 3 Step 3A (when no template exists) |
| Dealing with States Narrative | Counter-narrative strategies — Rape & Homicide applications (6 columns) | Phase 3 Step 3A |
| Running List | Defenses discovered/refined during each litigation phase (3 columns) | Phase 3 Step 3C → ongoing through trial |

---

## Phase Quick Map

| Phase | Purpose | Capstone Output |
|---|---|---|
| Phase 1 | Case Intake & Matter Setup | `000 - Case Profile.docx` + populated Case Tables |
| Phase 2 | Case Processing & Analysis | 8 Case Analysis Reports + auto-actions (discovery demand, impeachment worksheets) |
| Phase 3 | Trial Notebook & Attorney Preparation | Trial-ready notebook (assembled by `dw-trial-notebook-builder-crim`) |
| Phase 4 | Final Trial Notebook Assembly | Handled by `dw-trial-notebook-builder-crim` (separate skill) |

---

## Routing — Specialist Skills Called from This Workflow

| Trigger | Skill |
|---|---|
| 4th/5th/6th Amendment issues, warrant defects | `dw-suppression-motion-crim` |
| Brady/Giglio audit, missing discovery | `dw-brady-giglio-auditor-crim` |
| Discovery received, classification | `dw-discovery-orchestrator-crim` |
| Eyewitness ID procedures | `dw-eyewitness-identification-auditor-crim` |
| Custodial interrogations, Miranda | `dw-confession-interrogation-auditor-crim` |
| Cell phone extraction methodology | `dw-mobile-forensic-auditor-crim` |
| Phone dump content analysis | `dw-forensic-dump-analyzer-crim` |
| Body cam, dash cam, surveillance video | `dw-video-evidence-auditor-crim` |
| Cell site, GPS, geofence, Stingray | `dw-cell-site-geolocation-auditor-crim` |
| Social media evidence | `dw-social-media-auditor-crim` |
| Child forensic interviews (CAC) | `dw-child-forensic-interview-auditor-crim` |
| Expert witness Daubert/Foret challenges | `dw-expert-witness-evaluator-crim` |
| Chain of custody | `dw-chain-of-custody-auditor-crim` |
| Investigator tasking, scene canvass, witness vetting | `dw-defense-investigator-tasking-crim` |
| Other crimes evidence (404(b), Prieur) | `dw-404b-opposition-crim` |
| Habitual offender bills, predicate convictions | `dw-habitual-offender-auditor-crim` |
| Sentencing memos, mitigation, PSI audit | `dw-sentencing-mitigation-specialist-crim` |
| Bond reduction, pretrial release | `dw-bond-and-release-motion-crim` |
| Plea offer evaluation | `dw-plea-negotiation-analyzer-crim` |
| Cross-examination outlines | `dw-cross-exam-architect-crim` |
| Witness threat ranking | `dw-witness-threat-matrix-crim` |
| Voir dire, jury selection | `dw-voir-dire-assistant-crim` |
| Jury instructions, verdict forms | `dw-jury-instructions-builder-crim` |
| Appellate error preservation | `dw-appellate-error-monitor-crim` |
| Final trial notebook assembly | `dw-trial-notebook-builder-crim` |
| Session start/end, case state persistence | `dw-case-brain-crim` |
| Case status, where do we stand | `dw-case-dashboard-crim` |
| Case closing, disposition recording | `dw-case-disposition-crim` |

For a complete searchable index of all D&W skills, see `dw-skill-index-crim`.
