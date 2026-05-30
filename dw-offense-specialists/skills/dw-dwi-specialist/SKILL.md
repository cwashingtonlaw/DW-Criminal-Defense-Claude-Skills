---
name: dw-dwi-specialist-crim
category: offense-specialists
description: >
  DWI/DUI defense framework for Louisiana. ALWAYS invoke for "DWI," "DUI," "drunk driving,"
  "operating while intoxicated," "OWI," "Intoxilyzer," "breathalyzer," "blood alcohol,"
  "BAC," "field sobriety," "SFST," "implied consent," "license suspension," "ignition interlock,"
  "R.S. 14:98," or "refusal to submit." Covers breath/blood testing challenges, SFST protocol
  audits, rising BAC defense, retrograde extrapolation, and the DWI enhancement ladder.
  Do NOT use for general traffic offenses or vehicular homicide (use dw-criminal-defense Phase 1).
---

# DWI/DUI Defense Framework for Louisiana

## Overview

This skill provides systematic DWI/DUI defense analysis under Louisiana law (R.S. 14:98 and related statutes). Every DWI case requires:
1. Hard-stop offense classification and exposure calculation
2. Testing methodology audit (breath/blood/urine)
3. Field sobriety test protocol review
4. Rising BAC / retrograde extrapolation analysis
5. Constitutional and procedural challenge identification
6. Diversionary and alternative disposition evaluation

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

### Source Citation Mandate

Every factual assertion in the DWI defense analysis — BAC reading, test methodology, SFST observations, arrest circumstances, prior offense dates, and aggravating factor findings — must trace back to a specific source document. DWI cases are document-driven: the Intoxilyzer printout establishes the BAC, the SFST report establishes the field test results, and the arrest report establishes the stop justification. Unsourced claims about the BAC, test timing, or refusal are not defensible at suppression hearings or trial.

**Citation format:** Cite the document title, page number, and paragraph or timestamp. Examples:
- `(Intoxilyzer 9000 Printout, Test #2026-001, dated 03/15/2026)`
- `(Blood Draw Report — LSP Crime Lab, Sample #2026-001, p. 1)`
- `(SFST Report — Trooper Smith, p. 2, para. 3)`
- `(Arrest Report — LSP Case #2026-00456, p. 1, para. 2)`
- `(Officer Smith BWC — Traffic Stop, Timestamp 00:05:32)`
- `(Implied Consent Form, signed 03/15/2026)`
- `(Prior Conviction Minute Entry — Docket #2018-CR-0123, dated 06/12/2018)`

**Multiple-source rule:** When more than one document confirms a fact about the stop, test, or arrest, cite all of them — e.g., `(Intoxilyzer Printout, Test #2026-001; Officer Smith BWC, Timestamp 00:25:18)`.

**Unsourced assertions:** If a factual claim cannot be tied to a specific document, mark it `[UNSOURCED — VERIFY WITH CLIENT/DISCOVERY]` so the attorney knows to confirm or remove it before relying on it.

**Where sourcing applies:** All factual content — BAC values, test methodology, calibration records, SFST clue counts, stop justification, accident details, prior conviction dates and cleansing-period calculations. Legal standards, R.S. 14:98 statutory citations, and case law follow normal legal citation format.

---

## STEP 0: HARD STOP — Confirm DWI Case Type

**Do NOT proceed without establishing:**
- Specific offense level (1st/2nd/3rd/4th+ offense under R.S. 14:98)
- BAC result (if any)
- Test type (breath/blood/urine/refusal)
- Arrest circumstances (routine stop vs. accident vs. checkpoint)
- Whether accident involved (and if so, injuries/fatalities — may be vehicular homicide, route to dw-criminal-defense)
- Child passenger under 13? (R.S. 14:98.5 enhancement)
- BAC ≥ 0.15 or ≥ 0.20? (aggravating factors)

**If vehicular homicide involved:** Stop here and invoke dw-criminal-defense (Phase 1: Homicide).

## STEP 1: Load Case Context

Invoke **dw-case-brain** to retrieve:
- Prior DWI convictions and conviction dates (for offense level calculation and 10-year cleansing period)
- Specific R.S. 14:98 subsection charged
- BAC reading (exact numerical value)
- Test method and timing (breath at what time post-arrest, blood draw, urine test)
- Arresting agency and officer name
- Whether implied consent advisement was given
- Whether test was refused

## STEP 2: Offense Classification & Exposure

📖 Reference: Read `references/dwi-penalty-ladder.md`

**Map the charge to the correct tier:**
- 1st offense (R.S. 14:98(A)): fine $300-1000, jail 10 days-6 months (48 hrs mandatory minimum or 32 hrs community service), license suspension 90 days
- 2nd offense (R.S. 14:98(B)): fine $750-1000, jail 30 days-6 months (48 hrs mandatory minimum), license suspension 2 years, ignition interlock
- 3rd offense (R.S. 14:98(C)): fine $2000, imprisonment 1-5 years (1 year mandatory minimum), license suspension 4 years, vehicle seizure, ignition interlock, substance abuse treatment
- 4th+ offense (R.S. 14:98(D)): fine $5000, imprisonment 10-30 years (10 years mandatory minimum), permanent license revocation, vehicle seizure

**Flag aggravating factors:**
- BAC ≥ 0.15 (enhanced penalties)
- BAC ≥ 0.20 (further enhanced)
- Child passenger under 13 (R.S. 14:98.5 — misdemeanor becomes felony, mandatory 48 hrs jail minimum)
- Accident with injury or property damage

**Calculate cleansing period:** 10 years from prior conviction date. Priors older than 10 years do NOT count toward offense level.

## STEP 3: Breath/Blood Test Audit

📖 Reference: Read `references/breath-blood-testing-standards.md`

### Breath Test Audit (Intoxilyzer 9000)

**Critical points to verify:**
- Operator certification: Was operator certified? Refresher training current?
- Calibration records: When was Intoxilyzer last calibrated (within 1 year required)? Calibration within acceptable tolerance (±0.005)?
- 20-minute observation period: Was there continuous observation of suspect for 20 minutes immediately before test? Any mouth alcohol contamination?
- Duplicate test: Were two samples required? Did they agree within 0.020 BAC?
- Maintenance logs: Any documented malfunctions, repairs, or issues?
- Radio frequency interference: Was testing location free from RFI sources?
- Temperature: Was instrument operating within acceptable temperature range?

### Blood Test Audit

**Critical points to verify:**
- Phlebotomist qualifications: Was person who drew blood qualified and certified?
- Proper tube: Sodium fluoride/potassium oxalate anticoagulant? Correct volume?
- Chain of custody: Unbroken from draw to lab?
- Storage conditions: Temperature maintained? Stored properly?
- Lab accreditation: ASCLD/LAB accredited? Analyst credentials?
- Methodology: Gas chromatography with headspace analysis?
- Fermentation defense: How long between draw and testing? Risk of fermentation/bacterial growth?

### Refusal Cases

**Critical points to verify:**
- Implied consent advisement: Was R.S. 32:661 advisement properly given verbatim?
- Unequivocal refusal: Did suspect clearly and unambiguously refuse? Or was refusal ambiguous?
- Administrative license suspension: Did officer issue notice of intent to suspend (R.S. 32:414)?

## STEP 4: Field Sobriety Test Audit

📖 Reference: Read `references/sfst-protocol-standards.md`

### Standardized Field Sobriety Tests (NHTSA Protocol)

**Horizontal Gaze Nystagmus (HGN):**
- Proper stimulus (smooth, stimulus size correct)?
- 14 specific clues (lack of smooth pursuit, distinct and sustained nystagmus at maximum deviation, onset before 45 degrees — per eye)?
- Medical conditions causing nystagmus: neurological disorders, inner ear disorders, medications, alcohol intoxication itself?

**Walk and Turn (WAT):**
- 8 clues tracked: can't balance during instructions, starts too soon, stops walking, doesn't touch heel-to-toe, steps off line, uses arms, wrong number of steps, improper turn
- Environmental factors: surface conditions, footwear, weather, lighting?
- Physical limitations: age, weight, leg injuries, arthritic conditions?

**One Leg Stand (OLS):**
- 4 clues: sways while balancing, uses arms, hopping, puts foot down
- Physical limitations: same as WAT

**Non-standardized tests:** Finger-to-nose, alphabet recitation, counting backward — NO validated error rates, unreliable, should be challenged

### Officer Training & Certification
- NHTSA DWI Detection & SFST course (24-hour initial)?
- Current refresher training (8-hour, if required)?
- Actual certification documentation reviewed?

### Video Comparison
- Does BWC/dash cam footage of SFST match officer's written account?
- Any discrepancies flag credibility issues and unreliability

## STEP 5: Rising BAC / Retrograde Extrapolation Defense

📖 Reference: Read `references/rising-bac-defense.md`

**Rising BAC Theory:**
- BAC was below legal limit at time of driving but rose during absorption phase (30-90 min post-drink) before testing
- Test time BAC ≠ driving time BAC

**Retrograde Extrapolation:**
- Prosecution's expert calculates BAC backward from test time to driving time using Widmark formula
- Formula: BAC = (A / (r × W)) - (β × t)
  - A = grams of alcohol consumed
  - r = gender-specific distribution ratio (0.73 male, 0.66 female)
  - W = body weight (kg)
  - β = elimination rate (typically 0.015 per hour, but highly individual)
  - t = time since drinking

**Challenge assumptions:**
- Individual elimination rate variation (±50% common)
- Food intake (delays absorption, extends absorption phase)
- Body composition (affects distribution ratio)
- Drinking pattern (bolus drinking vs. sipping)
- Gastric emptying rate (highly variable)

**When rising BAC defense is strongest:**
- Short time between driving and testing (< 60 min)
- Evidence of recent drinking (near time of driving)
- BAC result close to 0.08 legal limit

## STEP 6: Constitutional & Procedural Challenges


**Traffic stop legality:**
- Did officer have reasonable suspicion for initial stop? (R.S. 32 violations, weaving, speed)
- Route to dw-suppression-motion for Fourth Amendment challenge

**Arrest probable cause:**
- Was there probable cause for DWI arrest before testing?
- Rely on SFST clues, BAC, statements, performance?

**Implied consent advisement:**
- Was R.S. 32:661 advisement properly given?
- Any deviation from statutory language?

**Miranda issues:**
- Was suspect in custody? Was custodial interrogation (statement or admissions) made without Miranda warning?
- Route to dw-confession-interrogation-auditor if interrogation occurred

**Checkpoint legality:**
- DWI checkpoints must comply with state constitutional requirements (La. Const. Art. I, § 5)
- Primary purpose must be DWI detection
- Minimal intrusion, adequate notice, supervisory oversight required
- Route to dw-suppression-motion for checkpoint challenge

**Video preservation:**
- Was dash cam/BWC preserved? Deleted? Poor quality?
- Route to dw-video-evidence-auditor for video analysis

## STEP 7: Diversionary & Alternative Disposition

📖 Reference: Read `references/dwi-diversion-alternatives.md`

### First Offense Diversionary Programs
- Art. 894 probation (adjudication withheld): Requires State consent and meets suitability criteria
- Substance abuse treatment court (if available in parish)
- Pre-trial diversion programs (parish-specific; consult local DA office)

### Reduced Charge Negotiations
- Reckless operation (R.S. 14:99): 30 days-3 months jail, $25-100 fine (not a DWI)
- Careless operation (R.S. 32:58): Traffic violation, fine $500-1000 (not a DWI)
- Reduces criminal exposure, no DWI license suspension, ignition interlock avoidance

### Alternative Sentences
- Ignition interlock in lieu of license suspension (R.S. 32:378.2): First offense may negotiate
- Day reporting, electronic monitoring, weekend jail
- Substance abuse counseling, ASAP enrollment

### DWI Court / Sobriety Court
- Some parishes have specialized DWI docket with intensive monitoring, frequent testing, treatment
- May reduce jail time or allow sentence downgrade upon successful completion
- Requires participant motivation and treatment compliance

## STEP 8: Output Documents

All documents saved to: `<case-root>/02 - Pretrial Notebook/03 - Case Analysis & Notes/`

**Document Suite:**

1. **DWI Case Analysis Report (.docx)**
   - Offense classification and exposure summary
   - Breath/blood test audit findings
   - SFST protocol deviations
   - Constitutional issues identified
   - Mitigation factors and client history

2. **Test Challenge Memorandum (.docx)**
   - Breath-specific OR blood-specific technical challenges
   - Expert witness requirements
   - Admissibility issues under La. C.C.P. Art. 215

3. **SFST Protocol Deviation Report (.docx)**
   - Each test documented with clues observed
   - Protocol deviations flagged
   - Medical condition history as alternative explanation

4. **Rising BAC Defense Memo (.docx)**
   - When rising BAC applies to this case
   - Retrograde extrapolation challenge strategy
   - Expert toxicology witness requirements

## Integration

**Reads from:**
- dw-case-brain (prior convictions, case details)
- dw-case-dashboard (case status)
- dw-video-evidence-auditor (BWC analysis of SFST and arrest)

**Routes to:**
- dw-suppression-motion (traffic stop/arrest/checkpoint challenges)
- dw-expert-witness-evaluator (toxicology/forensics experts)
- dw-plea-negotiation-analyzer (reduced charge negotiations)
- dw-sentencing-mitigation-specialist (if conviction results)
- dw-cross-exam-architect (officer cross, toxicologist cross)
- dw-trial-notebook-builder (trial prep)

**Uses:**
- docx skill (document generation)

## Core Rules (Non-Negotiable)

1. **Never assume BAC reading is accurate.** Always audit testing methodology completely.
2. **Always compare BWC/dash cam footage to officer's written account** of SFST and arrest procedures.
3. **Never skip the 20-minute observation period audit** for breath tests — this is foundational to Intoxilyzer reliability.
4. **Always check for medical conditions** that mimic impairment (diabetes, inner ear disorders, neurological conditions, fatigue, medications, hypoglycemia).
5. **Always calculate BAC at time of driving, not test time.** Rising BAC defense depends on this.
6. **Flag every deviation from NHTSA SFST protocol.** Even minor deviations affect clue reliability.
7. **For 2nd+ offenses, audit prior convictions for Boykin compliance** (knowing and intelligent waiver of rights at prior plea).

---

**NEXT STEPS:**

1. Confirm offense level and case facts with dw-case-brain
2. Request breath/blood test documents and calibration records from State
3. Request officer training certifications and SFST video from State
4. If BWC available, route to dw-video-evidence-auditor
5. Begin drafting suppression motion if Fourth Amendment issues identified
6. Retain toxicology expert if rising BAC defense viable
7. Evaluate plea negotiation options via dw-plea-negotiation-analyzer

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **breath-blood-testing-standards.md** — Breath (Intoxilyzer 9000) and blood testing standards for systematic audit of test methodology and admissibility challenges
- **dwi-diversion-alternatives.md** — Louisiana DWI diversionary programs and alternative dispositions (parish-by-parish, first-offense and beyond) to minimize criminal exposure
- **dwi-penalty-ladder.md** — La. R.S. 14:98 enhancement ladder: penalty escalation by prior convictions (10-year cleansing), BAC level, child passenger, and accident with injury
- **rising-bac-defense.md** — Rising BAC and retrograde extrapolation defense: BAC at testing does not equal BAC at driving; absorption-phase analysis
- **sfst-protocol-standards.md** — NHTSA Standardized Field Sobriety Test protocol standards, clues, and validation rates for systematic SFST audit
