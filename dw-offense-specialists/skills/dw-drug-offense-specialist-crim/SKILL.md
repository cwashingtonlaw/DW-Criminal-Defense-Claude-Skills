---
name: dw-drug-offense-specialist-crim
category: offense-specialists
description: >
  Drug offense defense framework for Louisiana. ALWAYS invoke for "drug charge," "possession,"
  "distribution," "trafficking," "CDS," "controlled dangerous substance," "Schedule I/II/III/IV/V,"
  "constructive possession," "intent to distribute," "drug lab," "field test," "drug weight,"
  "893 diversion," "drug court," "marijuana," "cocaine," "methamphetamine," "fentanyl,"
  "heroin," "R.S. 40:966," "R.S. 40:967," "R.S. 40:968," "R.S. 40:969," or "R.S. 40:970."
  Do NOT use for DWI/DUI drug impairment (use dw-dwi-specialist-crim).
---

# D&W Drug Offense Specialist

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any lab reports, charging documents, search warrants, witness statements, defendant statements, or case discovery, do not analyze anything yet.**

Your only response must be:
> *"Before I begin — are you uploading any additional lab reports, field test reports, charging documents, search warrants, affidavits, body-worn camera footage, witness statements, defendant statements, or other case documents? I'll start analysis only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** Mid-analysis discovery of an additional confirmatory lab result, a missing search warrant affidavit, or a body camera recording showing the search would require complete re-evaluation of charge classification, possession theory, lab audit, and search & seizure analysis.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

### Source Citation Mandate

Every factual assertion in the drug-offense analysis — substance identification, weight, possession theory, search circumstances, intent indicators, and enhancement eligibility — must trace back to a specific source document. Drug cases are fact-driven: the lab result establishes the substance, the police report establishes the arrest circumstances, and the search warrant affidavit establishes constitutional posture. Unsourced claims about weight, schedule, or possession theory carry no weight at suppression hearings, plea negotiations, or trial.

**Citation format:** Cite the document title, page number, and paragraph or timestamp. Examples:
- `(Lab Report — LSP Crime Lab, Sample #2026-001, p. 1)`
- `(Field Test Report — LCPD Case #2026-00456, p. 1)`
- `(Search Warrant Affidavit, p. 2, para. 4)`
- `(Arrest Report — LCPD Case #2026-00456, p. 3, para. 2)`
- `(Officer Smith BWC — Vehicle Stop, Timestamp 00:05:32)`
- `(Bill of Information, Count 1, p. 1)`
- `(Discovery Production, Bates #00145-00148)`

**Multiple-source rule:** When more than one document confirms a fact about the substance, weight, or arrest, cite all of them — e.g., `(Lab Report, Sample #2026-001, p. 1; Arrest Report, p. 3, para. 2)`.

**Unsourced assertions:** If a factual claim cannot be tied to a specific document, mark it `[UNSOURCED — VERIFY WITH CLIENT/DISCOVERY]` so the attorney knows to confirm or remove it before relying on it.

**Where sourcing applies:** All factual content — substance identification, weight, possession location, search authority, intent indicators (cash, scales, packaging), prior conviction status, lab chain of custody. Legal standards, statutory citations (R.S. 40:966-970), and case law follow normal legal citation format.

---

**Date of offense governs every statute cite.** Before quoting any element, penalty range, enhancement, or parole-eligibility figure, confirm the date of offense per count and select the statute version in force on that date using `dw-shared-protocols-crim/references/sentencing-statute-versions.md` (15:529.1 / 15:571.3 / 15:574.4 and the offense statute itself). Never fabricate a prior-version value; flag `[VERIFY — Westlaw]` where that file does.

## ENTRY POINT: HARD STOP — CONFIRM DRUG OFFENSE CASE

Before proceeding, confirm the following elements are present:

**STEP 0.6 — CASE TYPE VERIFICATION:**

- Substance(s) involved (marijuana, cocaine, methamphetamine, fentanyl, heroin, synthetic opioid, ecstasy, LSD, prescription medications, etc.)
- Quantity/weight of substance seized (grams, ounces, pounds, or weight unknown)
- Charge type classification:
  - Simple possession (personal use quantity)
  - Possession with intent to distribute (PWID)
  - Distribution (actual distribution or intent)
  - Manufacturing (clandestine lab, cultivation)
  - Trafficking (large quantity with mandatory minimums)
- Schedule classification (I, II, III, IV, or V under R.S. 40:964-970)
- Arrest circumstances: vehicle stop, home search warrant, consent search, plain view, informant-driven, etc.
- Prior drug conviction history (critical for enhancement analysis)

**If any element is unclear, STOP and request clarification before proceeding.**

---

## WORKFLOW OVERVIEW

This skill executes 8 sequential analytical steps, each building on the previous:

1. Load case context from dw-case-brain-crim
2. Charge classification & penalty exposure
3. Possession analysis (actual vs. constructive)
4. Lab analysis audit (field vs. confirmatory testing)
5. Search & seizure challenges
6. Intent to distribute analysis
7. Diversionary options evaluation
8. Generate outputs and integrate with other D&W tools

---

## STEP 1: LOAD CASE CONTEXT

**Action:** Invoke `dw-case-brain-crim` to pull:
- Defendant demographics and prior criminal history
- Specific statutes charged (R.S. 40:966-970 citations)
- Substance name, street name, and Schedule classification
- Gross weight and net weight (if known)
- Prior drug felony convictions (critical for enhancement calculation)
- Arrest location and method (vehicle, residence, public place)
- Search warrant or consent basis
- Lab status (tested, pending, or field test only)

**Why this matters:** Penalty exposure, enhancement eligibility, and diversion eligibility all depend on precise substance identification and weight determination. Constructive possession defenses vary dramatically by location (defendant's home, vehicle passenger, etc.).

---

## STEP 2: CHARGE CLASSIFICATION & PENALTY EXPOSURE

**Action:** Read `references/drug-schedule-penalties.md` now for the substance → Schedule mapping under R.S. 40:964, the charge-tier → penalty matrix (simple possession / PWID / distribution / trafficking mandatory minimums), and the penalty enhancements to flag (drug-free zone R.S. 40:981.3, firearm, minor present, prior drug felony). The Step 2 quick map is appended at the end of that file.

**Critical question:** Is the charged weight GROSS or NET? Gross weight includes packaging, cutting agents, containers. Net weight = pure substance only. Penalty thresholds (especially for cocaine and trafficking charges) depend entirely on this distinction.

**Output:** Penalty exposure grid showing:
- Base sentence range
- Enhancement scenarios and cumulative exposure
- Mandatory minimums triggered by weight or prior convictions

---

## STEP 3: POSSESSION ANALYSIS

**Action:** Classify possession as actual or constructive, run the four-element *State v. Harris* test (awareness, knowledge, dominion and control, guilty knowledge), apply the location-based analysis (sole-occupied residence, multi-occupant residence, vehicle driver/owner, vehicle passenger), match the defense strategy to the scenario, and complete the documentation checklist. Read `references/constructive-possession-framework.md` now for the Harris framework, key case law (*Harris*, *Bell*, *Trahan*, *Cann*, *Mitchell*), scenario-by-scenario defense strategies, and the documentation checklist — the Step 3 operational guidance is appended at the end of that file.

---

## STEP 4: LAB ANALYSIS AUDIT

**Action:** Determine whether the State has confirmatory lab testing (GC-MS/HPLC) or field-test results only; if field test only, demand lab testing; if lab tested, audit the methodology, gross-vs-net weight determination, lab accreditation and analyst qualification, chain of custody, and re-testing options. Route to dw-expert-witness-evaluator-crim to vet the lab analyst. Read `references/drug-lab-methodology.md` now for the field-test vs. confirmatory distinction, GC-MS/HPLC challenge points, cocaine trafficking weight thresholds, and the audit checklists — the Step 4 operational guidance is appended at the end of that file.

---

## STEP 5: SEARCH & SEIZURE CHALLENGES

**Action:** Route to `dw-suppression-motion-crim` with drug-specific framing. Analyze vehicle searches (probable cause, plain view/plain smell, automobile exception, search incident to arrest, consent, inventory), residence searches (warrant requirement and particularity, knock-and-announce, scope, protective sweep), person searches (Terry, search incident to arrest), confidential-informant tips (Aguilar-Spinelli / Gates, corroboration), drug-dog alerts (handler and dog reliability), and cell-phone searches (*Riley v. California*). Read `references/search-seizure-drug-challenges.md` now for the full challenge framework under each search type.

---

## STEP 6: INTENT TO DISTRIBUTE ANALYSIS

**Action:** Evaluate each of the eight circumstantial intent factors the State relies on to elevate simple possession to PWID — quantity, packaging, scales, cash, cell phones and text messages, high-crime location, absence of paraphernalia, and conduct during arrest — and build the defense counter and counter-evidence for each. Route phone content to dw-forensic-dump-analyzer-crim and dw-mobile-forensic-auditor-crim. Read `references/intent-to-distribute-factors.md` now for the factor-by-factor prosecution argument, defense challenge, and evidence — the Step 6 operational guidance is appended at the end of that file.

---

## STEP 7: DIVERSIONARY OPTIONS EVALUATION

**Action:** Immediately assess Art. 893 first-offender diversion eligibility, then Art. 890 suspension/deferral, drug court, DA pre-trial diversion, marijuana-specific options (post-Act 274, 2024), and federal alternatives. Read `references/drug-diversion-programs.md` now for the eligibility criteria, procedure, completion effects, and program structure of each option — the Step 7 operational guidance is appended at the end of that file.

---

## STEP 8: OUTPUTS AND INTEGRATION

### Output Files to Generate

**1. Drug Case Analysis Report (.docx)**
Location: `<case-root>/02 - Pretrial Notebook/03 - Case Analysis & Notes/`

**2. Lab Methodology Challenge Memo (if applicable) (.docx)**
Location: `<case-root>/02 - Pretrial Notebook/04 - Expert Reports & Challenges/`

**3. Constructive Possession Defense Memo (if applicable) (.docx)**
Location: `<case-root>/02 - Pretrial Notebook/05 - Defense Strategy/`

**4. Diversionary Eligibility Assessment (.docx)**
Location: `<case-root>/02 - Pretrial Notebook/06 - Negotiations & Plea/`

Read `references/output-deliverable-specs.md` now for the required contents of each deliverable.

---

## INTEGRATION WITH OTHER D&W TOOLS

### Tools That Feed INTO This Skill

- **dw-case-brain-crim:** Pulls initial case facts, prior convictions, charges
- **dw-discovery-orchestrator-crim:** Routes drug evidence (lab reports, officer reports, CI documents)

### Tools to ROUTE TO After This Skill

- **dw-suppression-motion-crim:** Formulate search/seizure challenges with drug-specific probable cause analysis
- **dw-expert-witness-evaluator-crim:** Vet lab analysts, toxicologists, drug dog handlers, CI reliability experts
- **dw-brady-giglio-auditor-crim:** Audit CI deals and informant reliability in drug investigations
- **dw-plea-negotiation-analyzer-crim:** Evaluate plea offers against trial risk in light of PWID vs. simple possession distinction
- **dw-cross-exam-architect-crim:** Build cross-examination of officer (search legality), lab analyst (methodology), CI handler (reliability)
- **dw-sentencing-mitigation-specialist-crim:** If convicted, prepare mitigation materials (addiction history, treatment readiness, Art. 893 opportunity lost, etc.)
- **dw-habitual-offender-auditor-crim:** If prior drug felonies exist, audit mandatory minimum applicability
- **dw-trial-notebook-builder-crim:** Assemble final trial materials with drug evidence sections

### Tools for Specific Evidence

- **dw-forensic-dump-analyzer-crim:** Analyze phone dump for distribution indicators (text messages, call logs, contacts)
- **dw-mobile-forensic-auditor-crim:** Audit phone extraction methodology (was warrant obtained? proper chain of custody?)
- **dw-video-evidence-auditor-crim:** Audit body camera or surveillance video of search execution (was it lawful? scope complied?)

---

## CORE RULES — NEVER DEVIATE

1. **Never accept a field test as conclusive** — Always demand confirmatory lab testing (GC-MS or HPLC). Field tests have unacceptable false positive rates.

2. **Always distinguish gross weight from net weight** — Penalty thresholds (especially for cocaine and trafficking) depend entirely on this. A 30-gram error can mean 10+ years difference.

3. **Constructive possession requires more than proximity** — Must prove all four Harris elements (awareness, knowledge, dominion, guilty knowledge). Mere presence + knowledge is insufficient per *State v. Bell*.

4. **Always check Art. 893 eligibility immediately** — If defendant qualifies for first offender diversion, this is a game-changer. Evaluate before committing to trial strategy.

5. **Always audit the confidential informant chain** — If a CI was involved, route to dw-brady-giglio-auditor-crim. CI reliability, deals, track record of truthfulness are critical to suppression strategy.

6. **Drug-free zone enhancement requires proof defendant KNEW** — Prosecution must prove defendant knew they were within 2,000 feet of school, church, or public housing. Challenge this affirmatively.

7. **For distribution charges, State must prove actual distribution or intent** — Mere possession of large quantity is NOT automatic intent to distribute. PWID requires intent beyond reasonable doubt.

---

## CHECKLIST FOR CASE COMPLETION

- [ ] Charge type and statute confirmed (R.S. 40:966-970 section identified)
- [ ] Substance and Schedule classification verified
- [ ] Net vs. gross weight determined and documented
- [ ] Lab testing status confirmed (tested or field test only?)
- [ ] Lab methodology audit completed (if tested)
- [ ] Search and seizure analysis routed to dw-suppression-motion-crim
- [ ] Possession analysis (actual vs. constructive) documented
- [ ] Intent to distribute factor analysis completed (if PWID charged)
- [ ] Art. 893 eligibility assessed
- [ ] Prior drug convictions verified (enhancement risk)
- [ ] Drug-free zone distance verified (if charged with enhancement)
- [ ] Expert needs identified (lab analyst, toxicology, drug dog, CI reliability)
- [ ] Output files generated and filed in case notebook
- [ ] Integration tasks assigned (suppression motion, plea negotiation, trial prep)

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **constructive-possession-framework.md** — Step 3. Louisiana case-law analysis of constructive possession; the four-element *State v. Harris*, 472 So.2d 576 (La. 1985) test the State must prove beyond reasonable doubt; Step 3 operational guidance (Harris elements, location-based analysis, defense strategies by scenario, documentation checklist) appended
- **drug-diversion-programs.md** — Step 7. Louisiana Art. 893, Art. 890, drug court, and pre-trial diversion programs; eligibility assessment to be completed before committing to trial strategy; Step 7 operational summary (Art. 893/890, drug court, pre-trial diversion, Act 274 marijuana rules, federal) appended
- **drug-lab-methodology.md** — Step 4. Field testing vs. confirmatory laboratory analysis: distinguishing preliminary screening from conclusive evidence of drug identity; Step 4 audit guidance (GC-MS/HPLC, gross-vs-net weight thresholds, accreditation, chain of custody, re-testing) appended
- **drug-schedule-penalties.md** — Step 2. Louisiana Controlled Dangerous Substances Act (R.S. 40:964-970) schedule-by-schedule substances and penalties (including marijuana special rules); Step 2 quick map (Schedule mapping, penalty tiers, enhancements) appended
- **intent-to-distribute-factors.md** — Step 6. Intent-to-distribute analysis framework: prosecution factors and defense counters; possession of large quantity is not automatic intent to distribute; eight-factor operational analysis appended
- **output-deliverable-specs.md** — Step 8. Required contents of the four deliverables (Drug Case Analysis Report, Lab Methodology Challenge Memo, Constructive Possession Defense Memo, Diversionary Eligibility Assessment)
- **search-seizure-drug-challenges.md** — Step 5. Drug-specific search-and-seizure challenge framework: vehicle, residence, and person searches, confidential-informant tips, drug-dog alerts, cell-phone searches
