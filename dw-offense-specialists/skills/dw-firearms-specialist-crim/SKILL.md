---
name: dw-firearms-specialist-crim
category: offense-specialists
description: >
  Firearms and weapons offense defense framework for Louisiana and federal law. ALWAYS invoke for
  "gun charge," "firearm," "weapon," "felon in possession," "illegal carrying," "concealed weapon,"
  "R.S. 14:95," "R.S. 14:95.1," "922(g)," "felon with a gun," "armed offender," "firearm enhancement,"
  "prohibited person," "gun found," "weapon seized," or "ballistics." Covers state illegal carrying,
  felon-in-possession (state and federal), concealed carry issues, firearm enhancements, dual jurisdiction
  exposure, and Second Amendment challenges post-Bruen. Do NOT use for homicide cases where the firearm
  is the murder weapon (use dw-criminal-defense-crim Phase 1) unless the gun charge is standalone or stacked.
---

# dw-Firearms Specialist

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

### Source Citation Mandate

Every factual assertion in the firearms-offense analysis — weapon identification, possession theory, search circumstances, predicate conviction details, ACCA exposure, and § 924(c) findings — must trace back to a specific source document. Firearms cases turn on the documented record: the seizure location, the chain of custody, and the predicate conviction certificates determine charge viability and exposure. Unsourced claims about possession, predicate offenses, or weapon characteristics carry no weight at suppression hearings or in plea negotiations.

**Citation format:** Cite the document title, page number, and paragraph or timestamp. Examples:
- `(Arrest Report — LCPD Case #2026-00456, p. 3, para. 2)`
- `(Search Warrant Affidavit, p. 2, para. 4)`
- `(Officer Smith BWC — Vehicle Stop, Timestamp 00:05:32)`
- `(ATF Trace Report — Serial #12345678, dated 03/15/2026, p. 1)`
- `(Predicate Conviction Minute Entry — Docket #2018-CR-0123, dated 06/12/2018)`
- `(NCIC/Pen Pack — Defendant Criminal History, p. 2)`
- `(Ballistics Report — LSP Crime Lab, Sample #2026-001, p. 1)`
- `(Discovery Production, Bates #00145-00148)`

**Multiple-source rule:** When more than one document confirms a fact about the weapon, predicate, or seizure, cite all of them — e.g., `(Arrest Report, p. 3; ATF Trace Report, p. 1)`.

**Unsourced assertions:** If a factual claim cannot be tied to a specific document, mark it `[UNSOURCED — VERIFY WITH CLIENT/DISCOVERY]` so the attorney knows to confirm or remove it before relying on it.

**Where sourcing applies:** All factual content — weapon type and serial, seizure location and method, predicate conviction details, ACCA classification, § 924(c) underlying offense, dual-jurisdiction posture. Statutory citations (R.S. 14:95.1, 18 U.S.C. § 922(g), § 924(c), § 924(e)) and case law (*Bruen*, *Rahimi*) follow normal legal citation format.

---

**Date of offense governs every statute cite.** Before quoting any element, penalty range, enhancement, or parole-eligibility figure, confirm the date of offense per count and select the statute version in force on that date using `dw-shared-protocols-crim/references/sentencing-statute-versions.md` (15:529.1 / 15:571.3 / 15:574.4 and the offense statute itself). Never fabricate a prior-version value; flag `[VERIFY — Westlaw]` where that file does.

## WORKFLOW OVERVIEW

This skill systematically analyzes firearms and weapons charges under Louisiana and federal law, with emphasis on:
- **Dual jurisdiction exposure** (state R.S. 14:95.1 vs. federal 18 U.S.C. § 922(g))
- **Predicate conviction audit** (felon-in-possession: is prior actually disqualifying?)
- **Second Amendment challenges post-Bruen** (evolving jurisprudence)
- **Possession analysis** (actual vs. constructive)
- **Search & seizure** (firearm-specific framing)
- **ACCA exposure** (15-year mandatory minimum if 3+ violent/drug felonies)
- **§ 924(c) mandatory consecutive sentences** (highest-stakes issue in any firearms case)

---

## STEP 0 — HARD STOP: CONFIRM FIREARMS CASE

Before proceeding, verify this is a firearms/weapons case and gather critical information:

**QUESTIONS TO ASK:**
1. What are the specific charges? (State statute or federal 18 U.S.C. section?)
2. What weapon? (handgun, rifle, shotgun, other?)
3. How was weapon discovered/seized? (stop, consent search, warrant, plain view, residence search?)
4. Does defendant have prior felony convictions? (How many? Type? Date? Jurisdiction?)
5. Is this state prosecution, federal, or both?
6. Is the firearm charge standalone or stacked with other charges (drugs, violence, other)?

**RED FLAG CASES REQUIRING IMMEDIATE FEDERAL EXPOSURE ANALYSIS:**
- Felon-in-possession charge (any state or federal)
- Federal § 924(c) allegation (using/carrying gun during drug/violence crime)
- ATF or FBI involvement indicated
- Multi-defendant case
- Prior federal convictions
- Drug nexus (gun + drugs = likely federal adoption)

---

## STEP 1 — LOAD CASE CONTEXT

Use **dw-case-brain-crim** to pull case data:
- Specific statute(s) charged (state and federal)
- Weapon description (type, caliber, condition, registration status if any)
- Prior felony convictions (type, date, jurisdiction, disposition)
- How weapon was located (stop, search, seizure method)
- Whether state or federal prosecution
- Status of federal grand jury (if any)
- Whether ATF/FBI is investigating
- Charging agency (local DA, federal prosecutor, both)

---

## STEP 2 — DUAL JURISDICTION EXPOSURE ANALYSIS (CRITICAL)

**READ: `references/state-federal-firearms-matrix.md`**

This is the highest-priority first step. Firearms charges uniquely carry dual jurisdiction risk:

Map the state charges (R.S. 14:95 illegal carrying; R.S. 14:95.1 felon in possession, 10-20 years hard labor, no probation/parole) against the federal charges (18 U.S.C. § 922(g), § 924(c) mandatory consecutive, § 924(e) ACCA 15-year minimum), assess federal adoption risk (ATF/FBI involvement, grand jury, drug nexus, prior federal convictions, multi-defendant, trafficking indicators), and run the forum-selection comparison. Read `references/state-federal-firearms-matrix.md` now for the state/federal charge and penalty summary, the federal-adoption risk indicators, the forum-selection questions, and the side-by-side R.S. 14:95.1 vs. § 922(g) comparison table — the Step 2 operational guidance is appended at the end of that file.

---

## STEP 3 — STATE CHARGE ANALYSIS

**READ: `references/louisiana-firearms-statutes.md`**

Analyze every charged Louisiana statute — R.S. 14:95 (illegal carrying: elements, penalties, permit defenses), R.S. 14:95.1 (felon in possession: five elements, mandatory 10-20 years hard labor without benefit, the MANDATORY predicate conviction audit, and the 10-year cleansing period under R.S. 14:95.1(C) running from completion of sentence), R.S. 14:95.2 (firearm-free zone), R.S. 14:95.5 and 14:95.10 (domestic abuse / protective order prohibitions overlapping § 922(g)(8)-(9)), concealed-carry permit exemptions (R.S. 40:1379.3), and Castle Doctrine / Stand Your Ground (R.S. 14:20). Read `references/louisiana-firearms-statutes.md` now for the elements, penalties, defenses, and predicate-audit checklist for each statute — the Step 3 operational guidance is appended at the end of that file.

---

## STEP 4 — FEDERAL CHARGE ANALYSIS

**READ: `references/federal-firearms-framework.md`**

Analyze federal exposure under 18 U.S.C. § 922(g) (nine prohibited-person categories; up to 15 years post-Bipartisan Safer Communities Act 2022; federal "punishable by imprisonment >1 year" predicate definition differs from state), § 924(c) (mandatory consecutive 5/7/10/25 years; "in furtherance" element; second conviction 25-year minimum), § 924(e) ACCA (15-year mandatory minimum on 3+ violent felonies or serious drug offenses; Taylor/Mathis categorical approach; *Johnson* residual-clause invalidation), and USSG § 2K2.1. Read `references/federal-firearms-framework.md` now for the category-by-category elements, penalties, predicate challenge strategy, and guideline notes — the Step 4 operational guidance is appended at the end of that file.

---

## STEP 5 — POSSESSION ANALYSIS

Classify possession as actual (on the body, direct physical control) or constructive (vehicle, residence, shared spaces); for constructive possession run the three Harris factors (awareness, dominion and control, guilty knowledge), the multi-occupant analysis, and the constructive-possession weaknesses; evaluate the temporary/innocent possession defense. Read `references/firearms-possession-analysis.md` now for the elements, defense considerations, and multi-occupant framework.

---

## STEP 6 — SECOND AMENDMENT CHALLENGES (POST-BRUEN)

**READ: `references/second-amendment-post-bruen.md`**

**THIS IS THE MOST RAPIDLY EVOLVING AREA OF FIREARMS LAW**

Apply the *Bruen* (2022) text-history-and-tradition test and *United States v. Rahimi* (2024) to the charged prohibitor; evaluate the § 922(g)(1) circuit split (*Range v. Attorney General*, 3rd Cir. 2023), 5th Circuit development (*United States v. Daniels*), good-candidate criteria (nonviolent predicate, weak historical tradition), and procedural requirements (standing, ripeness, as-applied vs. facial). ALWAYS verify current 5th Circuit precedent via casedev:search or WebSearch before filing. Read `references/second-amendment-post-bruen.md` now for the doctrinal framework, circuit-split status, and when-to-raise criteria — the Step 6 operational guidance is appended at the end of that file.

---

## STEP 7 — SEARCH & SEIZURE (FIREARM-SPECIFIC)

**ROUTE TO: `dw-suppression-motion-crim` with firearms-specific framing**

Analyze the Terry frisk (armed-and-dangerous justification, scope), vehicle-stop discovery (plain view, automobile exception, inventory), residence search (warrant scope for firearms, consent, third-party consent), consent (voluntariness, scope, withdrawal), informant-tip reliability, and ShotSpotter / gunshot-detection reliability. Read `references/firearms-search-seizure-issues.md` now for the firearm-specific challenge questions under each search type.

---

## STEP 8 — OUTPUTS AND DOCUMENTATION

### Primary Deliverable: Firearms Case Analysis Report

**Create a comprehensive .docx report (use `docx` skill)** with seven sections: (1) Case Summary; (2) Dual Jurisdiction Exposure Assessment; (3) Predicate Conviction Audit (if § 922(g) or ACCA exposure); (4) Possession Analysis; (5) Second Amendment Challenge Memo (if applicable); (6) Search & Seizure Issues; (7) Strategic Recommendations. Read `references/output-deliverable-specs.md` now for the required contents of each section.

**SAVE TO:**
```
<case-root>/02 - Pretrial Notebook/03 - Case Analysis & Notes/
Firearms_Case_Analysis_[DefendantName]_[Date].docx
```

### Secondary Deliverables

Predicate Conviction Audit Spreadsheet (if ACCA or R.S. 14:95.1 exposure), Second Amendment Challenge Memo (if filed), and Dual Jurisdiction Forum Analysis (if federal adoption likely) — required contents for each are in `references/output-deliverable-specs.md`.

---

## INTEGRATION WITH D&W ECOSYSTEM

### READS FROM:
- **dw-case-brain-crim** — Case context, charges, defendant history
- **dw-case-dashboard-crim** — Case status, filing deadlines, next steps

### ROUTES TO:
- **dw-suppression-motion-crim** — Firearm discovery/seizure issues
- **dw-habitual-offender-auditor-crim** — Predicate conviction analysis (overlapping expertise)
- **dw-expert-witness-evaluator-crim** — Ballistics experts, gunshot residue experts, trajectory analysis
- **dw-plea-negotiation-analyzer-crim** — State vs. federal exposure, plea strategy
- **dw-sentencing-mitigation-specialist-crim** — R.S. 14:95.1 mandatory minimum mitigation, ACCA litigation
- **dw-drug-offense-specialist-crim** — If stacked with drug charges (§ 924(c) analysis)

### FEEDS INTO:
- **dw-cross-exam-architect-crim** — Impeach prosecution witness re: possession, knowledge, control
- **dw-trial-notebook-builder-crim** — Jury instructions, cross-exam outlines, trial strategy

### USES:
- **docx** skill — Generate analysis report, memos
- **casedev:search** — Current case law (Bruen, Rahimi, 5th Cir. updates)
- **WebSearch** — Latest Second Amendment jurisprudence, circuit developments

---

## CORE RULES AND PRINCIPLES

### Rule 1: ALWAYS Assess Federal Adoption Risk Before State-Only Strategy

- Never assume prosecution will remain in state court
- Even small drug nexus can trigger federal interest
- ATF/FBI involvement = high federal adoption likelihood
- Build federal defense strategy in parallel with state case

### Rule 2: ALWAYS Audit Predicate Felony Convictions

- Many "felonies" don't actually qualify under § 922(g)
- 10-year cleansing period (R.S. 14:95.1(C)) is often overlooked
- Deferral under Art. 893 = NOT a conviction
- Expungement = conviction disappears
- Boykin violation = void conviction

### Rule 3: For § 922(g), Check BOTH State and Federal Predicate Definitions

- Federal: "crime punishable by imprisonment >1 year"
- State: Louisiana felony (broad category)
- A Louisiana misdemeanor with 2-year sentence may qualify federally
- A Louisiana felony with <1 year actual sentence may NOT qualify federally

### Rule 4: Constructive Possession Requires Full Harris Analysis

- Proximity + other factors ≠ automatic guilt
- Multi-occupant spaces create reasonable doubt
- Must prove awareness + dominion/control + guilty knowledge
- Circumstantial evidence must meet "clear and convincing" threshold

### Rule 5: Second Amendment Challenges Post-Bruen Are Evolving

- ALWAYS check current 5th Circuit precedent before filing
- Rahimi resolved DV restraining order; other categories in flux
- Nonviolent felon category = best bet for Bruen challenge
- Circuit split remains on Range-type cases (nonviolent felons)

### Rule 6: § 924(c) Mandatory Consecutive Sentences Are the Highest-Stakes Issue

- 5-25 years MANDATORY CONSECUTIVE (no guideline reduction)
- Makes total sentence calculation dramatically higher
- "In furtherance" element is fact-intensive — jury question
- Consider § 924(c) viability early in plea negotiation

### Rule 7: For ACCA Cases, Challenge Every Predicate Under Taylor/Mathis

- Categorical approach required (elements, not conduct)
- Johnson v. United States: residual clause void (elements-only test)
- Mathis: distinguish between elements and means
- Every predicate must categorically qualify (violent felony or serious drug)

### Rule 8: Compare State vs. Federal Sentencing to Inform Plea Strategy

- State: R.S. 14:95.1 mandatory 10-20 years hard labor
- Federal § 922(g): up to 15 years (or mandatory minimum 15 if ACCA applies)
- § 924(c): mandatory consecutive 5-25 years
- Stacking § 922(g) + § 924(c) + ACCA = 25+ years minimum
- Plea to state-only § 95.1 may be better than federal triple exposure

---

## QUICK REFERENCE: STATE VS. FEDERAL COMPARISON

The side-by-side R.S. 14:95.1 vs. § 922(g) comparison table (predicate, penalty range, parole/probation, cleansing, enhancements, § 924(c) exposure, forum, jury) is appended at the end of `references/state-federal-firearms-matrix.md` — read it when preparing the forum analysis and plea comparison.

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **federal-firearms-framework.md** — Step 4. 18 U.S.C. § 922(g) prohibited-persons categories, penalties (post-Bipartisan Safer Communities Act), and federal firearms-charge framework; Step 4 operational guidance (§ 922(g) nine categories, § 924(c), § 924(e) ACCA, USSG § 2K2.1) appended
- **firearms-possession-analysis.md** — Step 5. Actual vs. constructive possession of a firearm: Harris factors, multi-occupant analysis, constructive-possession weaknesses, temporary/innocent possession defense
- **firearms-search-seizure-issues.md** — Step 7. Firearm-specific search-and-seizure challenge questions: Terry frisk, vehicle stop, residence search, consent, informant tip, ShotSpotter
- **louisiana-firearms-statutes.md** — Step 3. Louisiana firearms statutes (R.S. 14:95 et seq.): definitions, prohibited conduct, and per-statute elements/penalties; Step 3 operational guidance (R.S. 14:95, 14:95.1 predicate audit and cleansing period, 14:95.2, 14:95.5, 14:95.10, permit exemptions, Castle Doctrine) appended
- **output-deliverable-specs.md** — Step 8. Section-by-section contents of the Firearms Case Analysis Report and the secondary deliverables (Predicate Conviction Audit Spreadsheet, Second Amendment Challenge Memo, Dual Jurisdiction Forum Analysis)
- **second-amendment-post-bruen.md** — Step 6. Second Amendment challenges post-*Bruen*: rapidly-evolving area; framework for current 5th Circuit precedent and verification steps before filing; Step 6 operational guidance (*Bruen*, *Rahimi*, *Range* circuit split, 5th Circuit tracking, when to raise) appended
- **state-federal-firearms-matrix.md** — Step 2 and the state-vs-federal quick reference. State-vs-federal firearms prosecution matrix: side-by-side statute comparison to inform forum-selection strategy; Step 2 operational guidance (state/federal charges, federal adoption risk, forum selection) and the R.S. 14:95.1 vs. § 922(g) comparison table appended
