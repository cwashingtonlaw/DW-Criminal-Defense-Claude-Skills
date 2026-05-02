---
name: dw-firearms-specialist
category: offense-specialists
description: >
  Firearms and weapons offense defense framework for Louisiana and federal law. ALWAYS invoke for
  "gun charge," "firearm," "weapon," "felon in possession," "illegal carrying," "concealed weapon,"
  "R.S. 14:95," "R.S. 14:95.1," "922(g)," "felon with a gun," "armed offender," "firearm enhancement,"
  "prohibited person," "gun found," "weapon seized," or "ballistics." Covers state illegal carrying,
  felon-in-possession (state and federal), concealed carry issues, firearm enhancements, dual jurisdiction
  exposure, and Second Amendment challenges post-Bruen. Do NOT use for homicide cases where the firearm
  is the murder weapon (use dw-criminal-defense Phase 1) unless the gun charge is standalone or stacked.
---

# dw-Firearms Specialist

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

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

Use **dw-case-brain** to pull case data:
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

**STATE CHARGES:**
- R.S. 14:95 (Illegal carrying of weapons)
- R.S. 14:95.1 (Felon in possession: 10-20 years hard labor, no probation/parole)

**FEDERAL CHARGES:**
- 18 U.S.C. § 922(g) (Prohibited persons: felon, drug user, mental defective, domestic violence, etc.)
  - Penalty: up to 15 years (increased from 10 by Bipartisan Safer Communities Act 2022)
- 18 U.S.C. § 924(c) (Using/carrying during drug/violence crime: 5/7/10/25 years MANDATORY CONSECUTIVE)
- 18 U.S.C. § 924(e) ACCA (15-year mandatory minimum if 3+ violent felonies or serious drug offenses)

**FEDERAL ADOPTION RISK:**
Federal prosecutors routinely "adopt" state gun cases. Assess this risk immediately:
- Is ATF/FBI involved in investigation?
- Has federal grand jury been convened?
- Any drug nexus? (drugs + gun = federal ticket)
- Prior federal convictions?
- Multi-defendant conspiracy or organized crime indicators?
- Weapon type suggests trafficking (bulk purchases, altered serials)?

**FORUM SELECTION ANALYSIS:**
- Compare state vs. federal sentencing exposure
- Which forum has more favorable jury pool?
- Which sentencing judge is more favorable (if known)?
- Does federal adoption block plea options in state court?
- Can state conviction be avoided to prevent federal predicate?

---

## STEP 3 — STATE CHARGE ANALYSIS

**READ: `references/louisiana-firearms-statutes.md`**

### R.S. 14:95 — Illegal Carrying of Weapons

**ELEMENTS:**
- Intentionally carrying any firearm or other weapon in manner prohibited by statute
- Manner includes: concealed handgun without proper permit, carrying while intoxicated, carrying on school property, carrying at parade/demonstration, carrying in courthouse

**PENALTIES:**
- First offense: up to 6 months imprisonment and/or $500 fine
- Subsequent offense: up to 3 years imprisonment

**DEFENSES:**
- Valid concealed carry permit (R.S. 40:1379.3)
- Permit-exempt locations (residence, vehicle, workplace)
- No intent/knowledge of carrying
- Permit obtained but officer unaware (reasonable mistake of law)

### R.S. 14:95.1 — Felon in Possession of Firearm

**CRITICAL STATUTE — MANDATORY SENTENCING**

**ELEMENTS:**
1. Defendant is a convicted felon (within Louisiana or elsewhere)
2. Defendant intentionally possesses a firearm
3. Firearm is accessible to defendant
4. Defendant knows of possession
5. Firearm is not a destructive device and not subject to NFA registration

**PENALTIES:**
- 10 to 20 years hard labor at Angola
- **NO probation, parole, or suspension of sentence** — fully mandatory
- No good-time credit applicable in some interpretations

**PREDICATE CONVICTION AUDIT (MUST DO):**

Is the prior conviction actually a disqualifying felony?

1. **Was it a conviction?** (not a deferral under La. C.C.P. Art. 893, not a deferred adjudication)
2. **Was it actually a felony?** (Some charges can be adjudicated as misdemeanors or felonies depending on sentencing)
3. **Has it been expunged?** (Check LSHB 1018 — some felonies can be expunged after 5-10 years)
4. **Was Boykin colloquy proper?** (Failure to comply with Boykin in guilty plea = void conviction)
5. **What is the specific statute of conviction?** (Some crimes are wobbler offenses)

**10-YEAR CLEANSING PERIOD — R.S. 14:95.1(C):**
- Cleansing period runs from completion of sentence, NOT from date of conviction
- If prior felony sentence ended 9 years ago, defendant is still within window
- Completion includes parole/probation termination
- Document exact dates of sentence and parole release

### R.S. 14:95.2 — Firearm-Free Zone

- Possession within 1000 feet of school property: enhanced penalty
- Carries additional crime (separate charge possibility)
- School property defined broadly (building, grounds, buses)

### R.S. 14:95.5 — Prohibited Possession (Domestic Abuse)

- Defendant convicted of domestic abuse battery (R.S. 14:35.3)
- Possession of firearm while under such conviction: prohibited
- Overlaps with federal § 922(g)(9) domestic violence prohibitor

### R.S. 14:95.10 — Protective Order/Domestic Abuse

- Possession prohibited while under protective order
- Or while convicted of domestic abuse crime
- Overlaps with federal law (18 U.S.C. § 922(g)(8))

### Concealed Carry Permit Exemptions

- R.S. 40:1379.3 outlines permit requirements
- Certain locations exempt (vehicle, residence, workplace with employer consent)
- Permit required for public carry in populated areas

### Castle Doctrine / Stand Your Ground

- R.S. 14:20 (Justifiable homicide) — self-defense principles
- May apply as mitigation if firearm used in self-defense scenario
- Separate from illegal carrying charge itself

---

## STEP 4 — FEDERAL CHARGE ANALYSIS

**READ: `references/federal-firearms-framework.md`**

### 18 U.S.C. § 922(g) — Prohibited Persons

**PENALTY:** Up to 15 years imprisonment (increased from 10 by Bipartisan Safer Communities Act 2022)

**NINE CATEGORIES OF PROHIBITED PERSONS:**

1. **Convicted of crime punishable by imprisonment >1 year (§ 922(g)(1))**
   - **NOTE: Federal definition differs from state**
   - Federal uses "crime punishable by imprisonment for more than one year" — ANY offense, even if classified as misdemeanor under state law
   - Example: Some Louisiana felonies carry sentences <1 year; federal court may not recognize as disqualifying
   - **Rehaney/Lara issues:** Does the state conviction meet federal predicates?
   - ALWAYS check: what was the actual sentence imposed vs. what was authorized?

2. **Fugitive from justice (§ 922(g)(2))**
   - Fleeing to avoid prosecution, conviction, imprisonment, or testimony
   - Active warrant = fugitive status

3. **Unlawful user of controlled substance (§ 922(g)(3))**
   - Marijuana use (federal illegal despite state decriminalization) = disqualifier
   - Can be proven by positive drug test, possession, admission
   - NOT limited to felony drug convictions
   - Can trigger federal indictment independent of state charge

4. **Adjudicated mental defective (§ 922(g)(4))**
   - Prior adjudication of mental illness affecting judgment
   - Involuntary commitment
   - Incompetence to stand trial finding

5. **Illegal alien (§ 922(g)(5))**
   - Not lawful permanent resident
   - Includes individuals on temporary visa, overstays, undocumented status

6. **Dishonorable discharge (§ 922(g)(6))**
   - Military dishonorable discharge only (not other-than-honorable)
   - Must be from U.S. Armed Forces

7. **Domestic violence conviction (§ 922(g)(9))**
   - Misdemeanor crime of domestic violence (§ 921(a)(33))
   - Includes Louisiana DV battery convictions
   - **Rahimi (2024): DV restraining order also disqualifies** (separate from conviction)

8. **Subject to protective order (§ 922(g)(8))**
   - Restraining order issued by civil or criminal court
   - Order must find reasonable cause to believe domestic violence was committed OR order issued to prevent harassment/threatening
   - **United States v. Rahimi (2024):** upheld § 922(g)(8) under Bruen historical tradition test

9. **Renounced U.S. citizenship (§ 922(g)(7))**
   - Lesser-used category

### 18 U.S.C. § 924(c) — Using or Carrying Firearm During Crime of Violence or Drug Trafficking Crime

**MANDATORY CONSECUTIVE SENTENCING — HIGHEST STAKES ISSUE IN FIREARMS CASES**

**PENALTIES:**
- Base: 5 years consecutive (minimum)
- Brandished: 7 years consecutive
- Discharged: 10 years consecutive
- Discharged and caused death/serious injury: 25+ years consecutive
- **Second or subsequent § 924(c) conviction:** 25 years minimum

**"IN FURTHERANCE" REQUIREMENT:**
- Not just mere presence of gun near crime
- Gun must facilitate, promote, or have reasonable nexus to underlying crime
- Example: gun in car during drug transaction may not be "in furtherance" if never shown
- Much fact-intensive inquiry

**FEDERAL SENTENCING IMPLICATIONS:**
- § 924(c) sentence runs CONSECUTIVE to underlying crime (drug trafficking, robbery, etc.)
- Creates massive total sentence exposure
- Example: Drug trafficking 10 years + § 924(c) 7 years = 17 years minimum
- Cannot be shortened by guideline adjustments

### 18 U.S.C. § 924(e) — Armed Career Criminal Act (ACCA)

**15-YEAR MANDATORY MINIMUM SENTENCE**

**TRIGGER:**
- Defendant convicted of being felon in possession (§ 922(g)(1))
- AND has three or more prior convictions for violent felonies or serious drug offenses

**"VIOLENT FELONY" DEFINITION (Taylor categorical approach):**
- Must have elements of force or substantial risk that force will be used
- Typically: homicide, robbery, burglary, arson, aggravated assault
- NOTE: Johnson v. United States (2015) struck down "residual clause" as void for vagueness
- Must use elements test (Mathis v. United States, 2016)

**"SERIOUS DRUG OFFENSE" DEFINITION:**
- Federal felony drug offense (controlled substance)
- Trafficking in cocaine, methamphetamine, heroin, etc.
- NOT simple possession (unless it triggers mandatory minimum separately)

**PREDICATE CHALLENGE STRATEGY:**
- Every predicate must qualify categorically
- Use Taylor/Mathis categorical approach
- Get actual crime of conviction documents (indictment, plea colloquy, statute)
- Some Louisiana felonies may not meet federal definition of "violent" or "serious drug"
- Circuit split on whether Louisiana crimes qualify

### Federal Sentencing Guidelines (USSG § 2K2.1)

- Base offense level for § 922(g) possession: typically 12-14 (depending on weapon type)
- Enhancements: prior convictions, number of weapons, trafficking in firearms
- Criminal history category: calculated from prior convictions
- Final guideline range (before mandatory minimums override)
- REMEMBER: § 924(c) mandatory consecutive sentences override guideline calculations

---

## STEP 5 — POSSESSION ANALYSIS

### Actual Possession

**ELEMENTS:**
- Firearm is on person's body or in hand
- In waistband, holster, jacket pocket, or carried in hand
- Direct physical control
- Clear evidence: witness testimony, officer observation, body-cam footage

**DEFENSE CONSIDERATIONS:**
- Temporary/innocent possession (picked up to secure, found on ground)
- Borrowed firearm (friend's gun, but whose knowledge/intent?)
- Concealed carry permit (if applicable to charge)

### Constructive Possession

**APPLIES TO:**
- Vehicle (glove box, under seat, center console, trunk)
- Residence (bedroom, kitchen, common area, closet)
- Shared spaces (apartment with roommates, office, business)

**CONSTRUCTIVE POSSESSION FRAMEWORK (Harris Analysis):**

Must prove three Harris factors:
1. **Awareness:** Defendant knew firearm was present in vehicle/residence
2. **Dominion and Control:** Defendant had power and intent to exercise control over firearm
3. **Guilty Knowledge:** Defendant knew the object was a firearm (not innocent mistake)

**MULTI-OCCUPANT ANALYSIS:**
- Who else had access to vehicle/residence?
- Can guilty knowledge/control be attributed to defendant or other occupants?
- Example: Roommate's gun in shared apartment — was defendant aware? Could defendant control it?
- Vehicle passengers: who had access to glove box, center console?
- Judge/jury must be convinced DEFENDANT specifically possessed it

**CONSTRUCTIVE POSSESSION WEAKNESSES:**
- Presence alone insufficient (Harris requires all three factors)
- Shared spaces create reasonable doubt if others had equal access
- Defendant's knowledge can be inferred but must be probative
- Some courts require additional factors (prior similar conduct, incriminating statements)

### Temporary/Innocent Possession Defense

- Defendant found firearm and immediately secured it (removed from crime scene)
- Defendant borrowed gun unaware of legal restriction (reasonable mistake)
- Defendant possessed on another's behalf but had no intent to exercise control
- BURDEN: Often on defense to raise, must be credible and consistent with evidence

---

## STEP 6 — SECOND AMENDMENT CHALLENGES (POST-BRUEN)

**READ: `references/second-amendment-post-bruen.md`**

**THIS IS THE MOST RAPIDLY EVOLVING AREA OF FIREARMS LAW**

### New York State Rifle & Pistol Association v. Bruen (2022)

**PARADIGM SHIFT:**
- Replaced multi-factor means-end scrutiny with **historical tradition test**
- New standard: text-history-and-tradition framework
- Court must look for "historical tradition" of comparable regulation
- Requires actual historical analogue, not just general principle

**IMPLICATION FOR § 922(g):**
- § 922(g) felon-in-possession prohibition being challenged
- Question: Is there historical tradition of disarming all persons convicted of felonies?
- Founding era evidence: very limited; felons traditionally could keep guns
- **Debate:** Does Rahimi foreclose all § 922(g) challenges? (See below)

### United States v. Rahimi (2024)

**DOMESTIC VIOLENCE RESTRAINING ORDER SURVIVES BRUEN**

- Court upheld § 922(g)(8) restraining order prohibition
- Applied Bruen historical tradition test
- Found sufficient historical tradition of domestic abuse regulations
- Rule: historical tradition doesn't require exact historical twin, but "analogue" suffices

**IMPLICATIONS:**
- Some § 922(g) categorical prohibitions survive post-Bruen challenge
- DV restraining order disqualification firmly upheld
- Unknown: whether Rahimi logic extends to all of § 922(g)(1)

### Circuit Split on § 922(g)(1) Felon-in-Possession Under Bruen

**RANGE v. ATTORNEY GENERAL (3rd Cir. 2023):**
- Nonviolent felon (false tax return conviction) may retain Second Amendment rights
- Court found no historical tradition of disarming nonviolent felons
- Suggested Second Amendment protections exist for some felon categories

**STATUS POST-RAHIMI:**
- Unclear whether Range survives Rahimi logic
- Some courts may distinguish violent vs. nonviolent predicates
- 5th Circuit (covering Louisiana) continues to develop jurisprudence
- **Must research current caselaw before filing any Second Amendment motion**

### 5th Circuit Post-Bruen Development

- Track **United States v. Daniels** (marijuana user § 922(g)(3) challenge)
- Track **United States v. Rahimi** (pre-SCOTUS 5th Cir. decisions, then SCOTUS reversal/affirmance)
- Search for ongoing circuit split on nonviolent felon category
- Check casedev:search for latest 5th Cir. firearms decisions

### When to Raise Second Amendment Challenge

**GOOD CANDIDATES:**
- Defendant convicted of nonviolent felony (white-collar crime, fraud, regulatory violation)
- Defendant convicted of misdemeanor-level crime but facing § 922(g) predicate
- Defendant subject to protective order but claims weak factual basis
- Historical tradition argument appears viable

**PROCEDURAL REQUIREMENTS:**
- Standing: defendant must be "regulated party" (person with gun or seeking to acquire)
- Ripeness: must be actual enforcement (not hypothetical)
- As-applied challenge: narrow tailoring argument
- Facial challenge: much harder to sustain

**RESEARCH REQUIREMENT:**
- ALWAYS verify current 5th Circuit precedent via casedev:search or WebSearch
- Bruen/Rahimi jurisprudence evolves constantly
- Circuit split remains unresolved on multiple issues

---

## STEP 7 — SEARCH & SEIZURE (FIREARM-SPECIFIC)

**ROUTE TO: `dw-suppression-motion` with firearms-specific framing**

### Terry Frisk Analysis

- Officer claimed reasonable suspicion defendant was "armed and dangerous"
- Was the suspicion justified? (Bulge consistent with weapon?)
- Did frisk scope exceed what was necessary to detect weapons?
- Did officer manipulate items through clothing excessively?

### Vehicle Stop and Firearm Discovery

- **Plain view doctrine:** Was firearm immediately apparent as firearm?
  - Officer observed gun in glove box / under seat / visible through window?
  - Lawful vantage point?
  - Inadvertence?
- **Automobile exception:** Officer searched vehicle without warrant — was exigent circumstance?
- **Inventory search:** Was gun found during lawful vehicle inventory?

### Residence Search

- Did warrant authorize search for firearm? (If warrant says "drugs," does it allow seizing gun?)
- Warrant scope exceeded for firearms discovery?
- Consent search: did defendant consent to search for guns?
- Third-party consent: did occupant with authority consent?

### Consent Search

- Was consent voluntary (not coerced by police presence/authority)?
- Scope of consent: did defendant consent to "firearm" specifically or "anything you find"?
- Withdrawal of consent: did defendant revoke consent before gun discovered?

### Constructive Search / Informant Tip

- Did police act on informant's tip that defendant had gun?
- Was informant reliable? (Prior accuracy, corroboration?)
- Did tip justify stop, frisk, or search?
- Did police engage in illegal surveillance based on tip?

### ShotSpotter / Gunshot Detection

- Relatively new technology — reliability challenges emerging
- Alert alone may not establish probable cause
- Civilian witness testimony may be more reliable than algorithm
- Consider suppressing alerts that lack additional corroboration

---

## STEP 8 — OUTPUTS AND DOCUMENTATION

### Primary Deliverable: Firearms Case Analysis Report

**Create a comprehensive .docx report (use `docx` skill) containing:**

**Section 1: Case Summary**
- Charges (state and federal)
- Weapon type/details
- Defendant's prior record
- Key facts of discovery/seizure
- Current jurisdiction (state, federal, both?)

**Section 2: Dual Jurisdiction Exposure Assessment**
- State law penalties (R.S. 14:95, R.S. 14:95.1) vs. federal (§ 922(g), § 924(c), § 924(e))
- Sentencing range comparison
- Federal adoption risk assessment (is ATF/FBI involved?)
- Forum analysis (which jurisdiction is more favorable?)
- Recommended strategy (push for state-only, negotiate federal dismissal, etc.)

**Section 3: Predicate Conviction Audit (if § 922(g) or ACCA exposure)**
- List all prior convictions relied on as predicates
- For each: Is it actually a felony? Was it a conviction (not deferral)? Has it been expunged?
- Boykin colloquy: was it proper?
- Cleansing period analysis (10 years from completion of sentence under R.S. 14:95.1(C))
- Federal vs. state predicate definition comparison
- Recommendations for attacking predicates

**Section 4: Possession Analysis**
- Actual vs. constructive
- Harris factors (if constructive)
- Multi-occupant analysis (if applicable)
- Innocent possession defense viability
- Constructive possession weaknesses to exploit

**Section 5: Second Amendment Challenge Memo (if applicable)**
- Candidate for Bruen challenge? (nonviolent predicate, weak historical tradition for prohibition?)
- Current 5th Circuit precedent (cite Rahimi, Range, Daniels, etc.)
- As-applied vs. facial challenge analysis
- Timing and procedural requirements
- Risk assessment (likelihood of success?)

**Section 6: Search & Seizure Issues**
- Reference: dw-suppression-motion work (cross-link)
- Firearm-specific suppression angles
- ShotSpotter/technology reliability issues
- Warrant scope, consent validity, etc.

**Section 7: Strategic Recommendations**
- Highest-leverage issues to attack first
- Plea negotiation strategy (state vs. federal exposure)
- Trial strategy (jury instructions, reasonable doubt arguments)
- Expert witness needs (ballistics, gunshot residue, etc.)

**SAVE TO:**
```
<case-root>/02 - Pretrial Notebook/03 - Case Analysis & Notes/
Firearms_Case_Analysis_[DefendantName]_[Date].docx
```

### Secondary Deliverables

**Predicate Conviction Audit Spreadsheet (if ACCA or R.S. 14:95.1 exposure):**
- Date, statute, sentence, parole release date
- Federal vs. state classification (felony?)
- Expungement status
- Boykin colloquy notes
- Categorization (violent felony, serious drug, other?)
- Risk assessment per predicate

**Second Amendment Challenge Memo (if filed):**
- Stand-alone memo if § 922(g) challenge likely
- Cite Bruen framework, Rahimi holding, 5th Circuit precedent
- As-applied challenge theory
- Historical tradition arguments specific to defendant's predicate

**Dual Jurisdiction Forum Analysis:**
- If federal adoption likely, create side-by-side state vs. federal comparison
- Include sentencing exposure, parole eligibility, guideline ranges
- Plea option analysis (can defendant plead state and avoid federal?)

---

## INTEGRATION WITH D&W ECOSYSTEM

### READS FROM:
- **dw-case-brain** — Case context, charges, defendant history
- **dw-case-dashboard** — Case status, filing deadlines, next steps

### ROUTES TO:
- **dw-suppression-motion** — Firearm discovery/seizure issues
- **dw-habitual-offender-auditor** — Predicate conviction analysis (overlapping expertise)
- **dw-expert-witness-evaluator** — Ballistics experts, gunshot residue experts, trajectory analysis
- **dw-plea-negotiation-analyzer** — State vs. federal exposure, plea strategy
- **dw-sentencing-mitigation-specialist** — R.S. 14:95.1 mandatory minimum mitigation, ACCA litigation
- **dw-drug-offense-specialist** — If stacked with drug charges (§ 924(c) analysis)

### FEEDS INTO:
- **dw-cross-exam-architect** — Impeach prosecution witness re: possession, knowledge, control
- **dw-trial-notebook-builder** — Jury instructions, cross-exam outlines, trial strategy

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

| Issue | Louisiana R.S. 14:95.1 | Federal § 922(g) |
|-------|------------------------|------------------|
| **Predicate** | Louisiana felony | Crime punishable >1 year |
| **Penalty Range** | 10-20 years hard labor | Up to 15 years |
| **Parole/Probation** | None allowed (mandatory) | Supervised release after 85% served |
| **Cleansing** | 10 years from end of sentence | No cleansing period |
| **Enhancements** | Habitual offender bill possible | ACCA (15-year min if 3+ predicates) |
| **§ 924(c) Exposure** | No federal consequence | 5-25 years mandatory consecutive |
| **Forum** | Louisiana state court | U.S. District Court |
| **Jury** | Louisiana jury (parish-specific) | Federal jury (diverse district) |

