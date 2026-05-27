---
name: dw-drug-offense-specialist
category: offense-specialists
description: >
  Drug offense defense framework for Louisiana. ALWAYS invoke for "drug charge," "possession,"
  "distribution," "trafficking," "CDS," "controlled dangerous substance," "Schedule I/II/III/IV/V,"
  "constructive possession," "intent to distribute," "drug lab," "field test," "drug weight,"
  "893 diversion," "drug court," "marijuana," "cocaine," "methamphetamine," "fentanyl,"
  "heroin," "R.S. 40:966," "R.S. 40:967," "R.S. 40:968," "R.S. 40:969," or "R.S. 40:970."
  Do NOT use for DWI/DUI drug impairment (use dw-dwi-specialist).
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

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

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

1. Load case context from dw-case-brain
2. Charge classification & penalty exposure
3. Possession analysis (actual vs. constructive)
4. Lab analysis audit (field vs. confirmatory testing)
5. Search & seizure challenges
6. Intent to distribute analysis
7. Diversionary options evaluation
8. Generate outputs and integrate with other D&W tools

---

## STEP 1: LOAD CASE CONTEXT

**Action:** Invoke `dw-case-brain` to pull:
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

**Action:** Read `references/drug-schedule-penalties.md` to map:

- **Substance → Schedule mapping** under R.S. 40:964
  - Schedule I: heroin, LSD, marijuana >2.5 lbs, ecstasy, GHB
  - Schedule II: cocaine, methamphetamine, fentanyl, oxycodone, PCP
  - Schedule III: anabolic steroids, ketamine, hydrocodone combinations
  - Schedule IV: alprazolam, diazepam, zolpidem, tramadol
  - Schedule V: cough syrups with codeine

- **Charge tier → penalty matrix:**
  - Simple possession: 4-10 years (Schedule I/II), up to 5 years (III/IV), up to 2 years (V)
  - PWID: 5-30 years (most Schedules)
  - Distribution: 2-30 years depending on Schedule
  - Trafficking: mandatory minimums (cocaine 10g = 5 years mandatory, 28g = 10 years, 200g = 20 years, etc.)

- **Penalty enhancements to flag:**
  - Drug-free zone (R.S. 40:981.3): offense within 2,000 feet of school, church, public housing → penalties DOUBLED + 5-year mandatory
  - Firearm enhancement: possession or use of firearm during drug offense → add 5-year mandatory
  - Minor present: drug offense with child present → enhanced penalty
  - Prior drug felony: escalates penalties substantially

**Critical question:** Is the charged weight GROSS or NET? Gross weight includes packaging, cutting agents, containers. Net weight = pure substance only. Penalty thresholds (especially for cocaine and trafficking charges) depend entirely on this distinction.

**Output:** Penalty exposure grid showing:
- Base sentence range
- Enhancement scenarios and cumulative exposure
- Mandatory minimums triggered by weight or prior convictions

---

## STEP 3: POSSESSION ANALYSIS

**Action:** Read `references/constructive-possession-framework.md` and execute:

### Actual vs. Constructive Possession

**Actual possession:** Defendant has physical contact with substance (in pocket, hand, immediately accessible).

**Constructive possession:** Defendant has dominion and control over substance without physical contact (substance in residence, vehicle, or locker under defendant's control).

### State v. Harris Framework (Mandatory Test)

All four elements must be proven beyond reasonable doubt:

1. **Awareness:** Defendant knew CDS was in the area
2. **Knowledge:** Defendant knew CDS was actually present
3. **Dominion and Control:** Defendant had exclusive or joint control over location/item
4. **Guilty Knowledge:** Defendant knew the substance was a controlled dangerous substance

### Location-Based Analysis

**Defendant's sole-occupied residence:** Constructive possession typically established if substance found in bedroom, safe, nightstand, or personal spaces. Prosecution burden is lower.

**Multi-occupant residence:** Must prove dominion/control over specific area and rule out other residents' possession. Substance in common area (kitchen counter, living room table) creates ambiguity — challenge this.

**Vehicle (sole driver/owner):** Substance in glove compartment, center console, or trunk supports constructive possession. Passenger scenario is weaker — see **State v. Trahan** analysis below.

**Vehicle (passenger scenario):** Substance under seat, in door pocket, or passenger-area location. Prosecution must prove passenger had dominion/control. Mere presence + knowledge ≠ constructive possession per **State v. Bell**.

### Key Case Law

- **State v. Harris:** Establishes four-element test (see above). Applies statewide.
- **State v. Bell:** Mere presence at scene + knowledge of substance ≠ constructive possession. Must have dominion/control + guilty knowledge.
- **State v. Trahan:** Vehicle passenger: prosecution must prove passenger exercised dominion over substance, not just that it was in vehicle.
- **State v. Cann:** Multi-occupant residence: prosecution must exclude other residents' possession; common area substances are weaker.
- **State v. Mitchell:** Circumstantial evidence of dominion (keys to premises, payment of utilities, recent presence) supports constructive possession but must be corroborated.

### Defense Strategies by Scenario

**Lack of awareness:** "I didn't know the substance was in my car / apartment"
- Challenge: How did prosecution prove awareness? Testimony only? Circumstantial?
- Defense: Prior search of vehicle/home, no reason to suspect substance present

**Lack of dominion/control:** "It belonged to my roommate / the other passenger"
- Challenge: Did prosecution prove defendant had exclusive control?
- Defense: Other person present, access to substance, defendant's lack of keys/authority

**Mere presence:** "I was at a party where drugs were present"
- Challenge: Did prosecution prove anything beyond presence?
- Defense: No dominion/control, no guilty knowledge, no personal items near substance

**Planted evidence:** "The substance was placed there by police or another person"
- Connect to dw-suppression-motion (illegal search), or challenge chain of custody

### Documentation Checklist

For every constructive possession case, document:
- [ ] Exact location of substance (which room, which surface, which container)
- [ ] Who had keys/access to the location
- [ ] Defendant's personal items in vicinity (clothing, phone, wallet, ID)
- [ ] Physical evidence linking defendant (fingerprints, DNA, photos of defendant in space)
- [ ] Statements defendant made during arrest (admissions vs. denials)
- [ ] Co-defendants or other occupants present
- [ ] Alibi or timeline evidence (was defendant actually at location?)

---

## STEP 4: LAB ANALYSIS AUDIT

**Action:** Read `references/drug-lab-methodology.md` and pull discovery:

### CRITICAL DISTINCTION: Field Test vs. Confirmatory Lab Testing

**Field tests** (Marquis, Mandelin, Mecke, Scott reagents) are NOT conclusive. They are preliminary tools only. False positive rates are significant — chocolate, vitamins, caffeine, legal supplements, and many other substances trigger false positives on field tests.

**Confirmatory testing** (GC-MS, HPLC) is the gold standard and is required to establish corpus delicti.

**Your immediate question:** Has the substance been confirmed by laboratory analysis, or does the prosecution only have field test results?

- If field test only: Demand lab testing before trial. Without lab confirmation, possession charge is weakened significantly.
- If lab tested: Audit the lab methodology (see below).

### Lab Methodology Audit

**GC-MS (Gas Chromatography-Mass Spectrometry):**
- Gold standard for drug identification
- Separates compounds by molecular weight and identifies by mass spectrum
- Methodology: substance is vaporized, passed through chromatography column, detected by mass spectrometer
- Retention time must match known standard for the substance
- Common challenge points:
  - Instrument calibration records (were standards run recently?)
  - Analyst qualification and experience
  - Lab accreditation (ASCLD/LAB or equivalent)
  - Chain of custody from seizure through lab
  - Contamination risk assessment

**HPLC (High-Performance Liquid Chromatography):**
- Used for liquid samples, some solids
- Similar methodology to GC-MS but doesn't vaporize samples
- Often paired with UV detection or mass spectrometry
- Challenge points: same as GC-MS

### Weight Determination — CRITICAL FOR PENALTY THRESHOLDS

**Gross weight:** Total weight of substance plus packaging, container, cutting agents, moisture, etc.

**Net weight:** Weight of pure substance only.

**Why this matters:** Cocaine trafficking thresholds are:
- 10g = 5-year mandatory minimum
- 28g = 10-year mandatory minimum
- 200g = 20-year mandatory minimum
- 400g = 40-year mandatory minimum

If prosecution is charging based on gross weight of 210g (but net is only 180g), you've just lost 20 years of potential exposure.

**Audit process:**
1. Request lab worksheets showing tare weight (weight of container alone)
2. Confirm gross weight minus tare weight = net weight
3. Ask: Does the reported weight reflect net substance or gross weight?
4. For mixtures (e.g., cocaine cut with filler): Did lab identify pure cocaine weight separately?
5. Moisture content: Did lab account for water weight in substance?

### Lab Accreditation and Analyst Qualification

- Is the lab accredited by ASCLD/LAB or equivalent?
- How long has the analyst been in position?
- How many samples has the analyst analyzed?
- Has the analyst testified in court before? How many times?
- Are there any disciplinary records or reliability issues for this analyst?

**Route to dw-expert-witness-evaluator** to vet lab analyst qualifications.

### Chain of Custody Audit

- Who seized the substance?
- Who transported it to the lab?
- How was it stored (sealed container, locked evidence room)?
- Who performed the analysis?
- Who signed off on the results?
- Are there gaps in the chain (dates/times missing, unsealed containers)?

### Re-testing and Independent Lab Analysis

- Does defendant have the right to independent lab testing?
- Is there enough substance remaining for retesting?
- Cost of independent lab analysis? (Defense must typically bear cost)
- Strategic value: Does retesting strengthen or weaken the defense?

---

## STEP 5: SEARCH & SEIZURE CHALLENGES

**Action:** Route to `dw-suppression-motion` with drug-specific framing. Analyze:

### Vehicle Searches

**Probable cause:** Did officer have probable cause before searching vehicle?
- Plain view: Substance visible on seat? In cup holder?
- Plain smell: **State v. Shumate** — marijuana odor can establish probable cause, but officer must be trained to distinguish marijuana from other sources
- Stop legality: Was the initial traffic stop lawful?

**Automobile exception:** Exception to warrant requirement if vehicle is mobile and readily movable. But exception does NOT eliminate probable cause requirement.

**Search incident to arrest:** Officer can search passenger compartment if defendant is unsecured and within reaching distance, or reasonable belief evidence of the crime is present. Trunk is NOT searchable unless defendant is recent occupant.

**Consent search:** Was consent voluntary? Was consent obtained through:
- Coercion or deception?
- Misrepresentation of officer authority?
- Ambiguous language ("Do you mind if I search?") without clear consent?

**Inventory search:** Police can inventory vehicle contents during impound, but only if inventory procedure is standardized (not pretextual). Drug evidence found during inventory may be suppressible if procedure was improper.

### Residence Searches

**Warrant requirement:** Searches of residences require a search warrant based on probable cause, except in exigent circumstances.

**Warrant particularity:** Does warrant describe the specific location and items to be seized? Overly broad warrant ("seize all items of interest") is challengeable.

**Knock-and-announce:** Did officers knock, announce authority, and wait reasonable time before entering? Violation may support suppression.

**Scope of search:** Was search limited to areas where drugs could reasonably be found? (Search of baby diapers may exceed scope; search of freezer is reasonable for solid drugs)

**Protective sweep:** Did officers sweep beyond areas necessary to secure premises? Rooms where no one could hide may exceed scope.

### Person Searches

**Terry stop and frisk:** Based on reasonable suspicion, officer can conduct limited pat-down of outer clothing for weapons. Frisk for drugs exceeds Terry scope unless officer feels object that is immediately recognizable as drug contraband.

**Search incident to arrest:** Once arrested, officer can search person and immediately surrounding area (within reaching distance) for weapons or evidence of the crime.

**Seizure of drug evidence:** If officer finds substance during lawful search, it is not suppressible unless the search itself was unlawful.

### Confidential Informant (CI) Stops and Tips

**CI reliability:** Did prosecution establish CI reliability through:
- **Aguilar-Spinelli test:** (outdated but still referenced) Did CI have basis of knowledge? Has CI been reliable in past?
- **Gates totality of circumstances test:** (modern standard) Weighing all factors, was there probable cause?

**Corroboration requirement:** Innocent details (location, appearance, vehicle) observed by police corroborate CI information.

**Defense challenge:** Did police follow up on CI tip independently, or did they conduct pretextual search? (See **State v. Brooks** on pretextual stops)

### Drug Dog Alerts

**Handler reliability:** Is the handler trained and experienced? How many false alerts has the dog had?

**Dog certification and training records:** Request records showing dog's training, certification, accuracy rates.

**Alert accuracy:** What is the actual false positive rate for this dog? (Some studies show 15-30% false positive rates)

**Alert specificity:** Did dog alert to location of drugs, or merely to residue/past presence?

**Time and environment:** Were conditions conducive to accurate alert (weather, odors, handler bias)?

**Defense expert:** Route to dw-expert-witness-evaluator to challenge drug dog reliability if needed.

### Cell Phone Searches

**Riley v. California:** Warrantless search of cell phone is unconstitutional, even incident to arrest. Prosecutor must obtain separate warrant for cell phone search.

**Challenge:** If officers searched phone without warrant, suppress all phone evidence (text messages, location data, photos, etc.)

**Exception:** Exigent circumstances may permit limited warrantless search, but burden is high.

---

## STEP 6: INTENT TO DISTRIBUTE ANALYSIS

**Action:** Read `references/intent-to-distribute-factors.md` and evaluate:

### Prosecution's Circumstantial Evidence of Intent

Prosecutors typically rely on multiple factors to prove intent to distribute (PWID) rather than simple possession. Each factor is circumstantial and can be challenged individually.

### Factor 1: Quantity

**Prosecution argument:** Large quantity suggests distributor, not personal user.

**Your challenge:** Personal use quantity varies widely by substance, tolerance, addiction severity.
- Cocaine: Some sources say 28g/month = personal use, but heavy users consume 1g+ per day
- Methamphetamine: Tolerance builds rapidly; heavy users consume 0.5-1g+ per day
- Heroin: Tolerance varies; 2-5g per day is common for addicted users
- Marijuana: Personal use typically 1-2 ounces/month, but varies

**Expert testimony:** Retain pharmacology/toxicology expert to testify on personal use quantities for the specific substance and defendant's profile (age, tolerance, addiction history).

### Factor 2: Packaging

**Prosecution argument:** Individually wrapped units suggest distribution prep.

**Your challenge:** Some personal users pre-portion drugs into smaller packages for:
- Multi-day trips (pack a few doses)
- Privacy (hide drugs in small packages)
- Dosing control (pre-weigh doses to manage tolerance)

**Counter-evidence:** Absence of distribution materials (no baggies factory, no bulk packaging, no labels).

### Factor 3: Scales/Weighing Equipment

**Prosecution argument:** Scale is a distribution tool.

**Your challenge:** Personal users also weigh drugs for:
- Dosing consistency
- Budgeting ("how much can I afford?")
- Tolerance management

**Evidence:** If scale is found with substance, was it used for dosing or distribution? (Look at quantity of substance, packaging, and other factors)

### Factor 4: Large Amounts of Cash

**Prosecution argument:** Cash indicates drug proceeds.

**Your challenge:** Legitimate explanations:
- Employment income (defendant works cash-based job: restaurant, construction, services)
- Inheritance or tax refund
- Cash withdrawal from bank (for privacy, habit, or legitimate reason)
- Savings from budget-conscious living

**Evidence:** Bank records, employment history, prior spending patterns.

### Factor 5: Cell Phones and Text Messages

**Prosecution argument:** Multiple phones = drug operation; text messages = drug deals.

**Your challenge:** Everyone has multiple phones (personal, work, burner for privacy). Text messages are often ambiguous:
- "You still good?" = social question, not drug deal
- "Meet up later?" = social plans
- "How much?" = asking about quantity for personal purchase, not selling

**Cross-examination:** Did prosecutor cherry-pick messages out of context?

**Mobile forensic review:** Route to dw-forensic-dump-analyzer and dw-mobile-forensic-auditor to mine phone content for legitimate uses (job search, social plans, etc.) that counter distribution narrative.

### Factor 6: Location (High-Crime Area)

**Prosecution argument:** Defendant found in high-drug area = likely distributor.

**Your challenge:** Defendant may live, work, or socialize in that area. High-crime area is not evidence of distribution.

**Evidence:** Employment address, residence, family ties to area, legitimate reason for being there.

### Factor 7: Absence of Paraphernalia (Inverse Factor)

**Prosecution argument:** No pipes, rolling papers, or consumption items = defendant is distributor, not user.

**Your challenge:** Not all drug users have visible paraphernalia. Heroin users may use needles (not always present). Cocaine users may snort (no paraphernalia). Marijuana users may have lost papers.

**Evidence:** Absence of paraphernalia is weak evidence of intent without corroborating factors.

### Factor 8: Conduct During Arrest

**Prosecution argument:** Defendant destroyed evidence, fled, or made admissions of selling.

**Your challenge:** Fleeing can be fear of arrest, not evidence of distribution. Destruction of evidence is separate charge, not proof of PWID. Admissions must be properly admitted (Mirandized? Voluntary?).

**Cross-examine:** What exactly did defendant say/do during arrest?

---

## STEP 7: DIVERSIONARY OPTIONS EVALUATION

**Action:** Read `references/drug-diversion-programs.md` and immediately assess:

### Article 893 First Offender Diversion (Louisiana Code of Criminal Procedure)

**Eligibility criteria:**
- First felony drug offense (prior misdemeanor drug convictions OK)
- No prior felony convictions of ANY kind
- Prosecutor and judge must consent (but judge cannot refuse if criteria met and defendant requests)

**Procedure:**
- Defendant pleads guilty or nolo contendere
- Court defers adjudication
- Probation term: 2-5 years (typically 3 years)
- Defendant must comply with probation (drug testing, treatment, no arrests)

**Completion effect:**
- If probation successfully completed: conviction is SET ASIDE
- Defendant may answer "no" to "Have you been convicted of a felony?" on employment applications
- Record is sealed (though not expunged)

**CRITICAL:** This is a powerful tool for first-time drug offenders. Evaluate eligibility IMMEDIATELY before proceeding to trial strategy.

### Article 890 Suspension/Deferral of Sentence

**Differs from Art. 893:** Available to defendants with prior convictions.

**Procedure:** Defendant pleads guilty, court suspends imposition of sentence and places defendant on probation.

**Effect:** On successful completion of probation, sentence is suspended (not set aside — conviction remains).

### Drug Court

**Eligibility:**
- Voluntary participation
- Substance abuse disorder diagnosis
- Non-violent offense (violent offenses typically excluded)
- No prior violent felonies
- Parish-specific availability (not all parishes have drug courts)

**Program structure:**
- 4 phases typically (treatment intensive → work/education focused → community reintegration → transition)
- Frequent court appearances (weekly initially)
- Mandatory treatment (inpatient or outpatient)
- Mandatory drug testing
- 12-24 months typical duration

**Outcome:** Successful completion = case dismissed or conviction set aside (varies by parish)

**Strategic value:** Drug court removes case from traditional criminal docket, focuses on treatment, and provides exit ramp from criminal justice system.

### Pre-Trial Diversion

**DA discretion:** District attorney's office may offer pre-trial diversion (typical terms: no arrest record, stay out of trouble for 6-12 months, diversion fees, community service).

**Parish-specific:** Availability varies by parish and DA policy.

**Advantage:** Case never prosecuted if diversion completed.

### Marijuana-Specific Options (Post-Act 274, 2024)

**First offense, small amount (<14g):** Misdemeanor, not felony. Fine up to $300, no jail.

**Second offense:** Misdemeanor, up to 30 days jail.

**Third+ offense:** Felony charges apply.

**Expungement eligibility:** Marijuana misdemeanors may be expungeable after conviction.

### Federal vs. State Diversion

**Federal cases:** No Art. 893 equivalent. Drug Offender Self-Sufficiency (DOSS) program may be available in some districts. Federal sentencing guidelines are generally more stringent.

---

## STEP 8: OUTPUTS AND INTEGRATION

### Output Files to Generate

**1. Drug Case Analysis Report (.docx)**
Location: `<case-root>/02 - Pretrial Notebook/03 - Case Analysis & Notes/`

Contents:
- Defendant demographics and case summary
- Charge(s) and penalty exposure matrix
- Substance identification, Schedule classification, weight analysis
- Possession analysis (actual vs. constructive, Harris framework, multi-occupant analysis if applicable)
- Lab methodology audit findings (GC-MS confirmation, analyst qualifications, chain of custody)
- Search and seizure challenge roadmap
- Intent to distribute factor analysis (if PWID charged)
- Diversion eligibility assessment (Art. 893 status, drug court, pretrial diversion)
- Critical next steps and expert needs

**2. Lab Methodology Challenge Memo (if applicable) (.docx)**
Location: `<case-root>/02 - Pretrial Notebook/04 - Expert Reports & Challenges/`

If lab testing is weak, ambiguous, or missing:
- Field test limitations and false positive rates
- GC-MS procedure critique (if available)
- Analyst qualification questions
- Chain of custody gaps
- Weight determination methodology challenges
- Recommendations for independent lab testing or Daubert challenge

**3. Constructive Possession Defense Memo (if applicable) (.docx)**
Location: `<case-root>/02 - Pretrial Notebook/05 - Defense Strategy/`

If constructive possession is charged:
- Multi-occupant residence/vehicle analysis
- State v. Harris element-by-element breakdown
- Missing links in prosecution's proof (awareness, knowledge, dominion, guilty knowledge)
- Factual gaps (no fingerprints, no DNA, no statements, competing explanations)
- Cross-examination outline for officers

**4. Diversionary Eligibility Assessment (.docx)**
Location: `<case-root>/02 - Pretrial Notebook/06 - Negotiations & Plea/`

- Art. 893 eligibility (YES/NO with supporting facts)
- Drug court eligibility assessment
- Pre-trial diversion availability (DA discretion)
- Negotiation leverage analysis (trial risk vs. diversion benefit)

---

## INTEGRATION WITH OTHER D&W TOOLS

### Tools That Feed INTO This Skill

- **dw-case-brain:** Pulls initial case facts, prior convictions, charges
- **dw-discovery-orchestrator:** Routes drug evidence (lab reports, officer reports, CI documents)

### Tools to ROUTE TO After This Skill

- **dw-suppression-motion:** Formulate search/seizure challenges with drug-specific probable cause analysis
- **dw-expert-witness-evaluator:** Vet lab analysts, toxicologists, drug dog handlers, CI reliability experts
- **dw-brady-giglio-auditor:** Audit CI deals and informant reliability in drug investigations
- **dw-plea-negotiation-analyzer:** Evaluate plea offers against trial risk in light of PWID vs. simple possession distinction
- **dw-cross-exam-architect:** Build cross-examination of officer (search legality), lab analyst (methodology), CI handler (reliability)
- **dw-sentencing-mitigation-specialist:** If convicted, prepare mitigation materials (addiction history, treatment readiness, Art. 893 opportunity lost, etc.)
- **dw-habitual-offender-auditor:** If prior drug felonies exist, audit mandatory minimum applicability
- **dw-trial-notebook-builder:** Assemble final trial materials with drug evidence sections

### Tools for Specific Evidence

- **dw-forensic-dump-analyzer:** Analyze phone dump for distribution indicators (text messages, call logs, contacts)
- **dw-mobile-forensic-auditor:** Audit phone extraction methodology (was warrant obtained? proper chain of custody?)
- **dw-video-evidence-auditor:** Audit body camera or surveillance video of search execution (was it lawful? scope complied?)

---

## CORE RULES — NEVER DEVIATE

1. **Never accept a field test as conclusive** — Always demand confirmatory lab testing (GC-MS or HPLC). Field tests have unacceptable false positive rates.

2. **Always distinguish gross weight from net weight** — Penalty thresholds (especially for cocaine and trafficking) depend entirely on this. A 30-gram error can mean 10+ years difference.

3. **Constructive possession requires more than proximity** — Must prove all four Harris elements (awareness, knowledge, dominion, guilty knowledge). Mere presence + knowledge is insufficient per *State v. Bell*.

4. **Always check Art. 893 eligibility immediately** — If defendant qualifies for first offender diversion, this is a game-changer. Evaluate before committing to trial strategy.

5. **Always audit the confidential informant chain** — If a CI was involved, route to dw-brady-giglio-auditor. CI reliability, deals, track record of truthfulness are critical to suppression strategy.

6. **Drug-free zone enhancement requires proof defendant KNEW** — Prosecution must prove defendant knew they were within 2,000 feet of school, church, or public housing. Challenge this affirmatively.

7. **For distribution charges, State must prove actual distribution or intent** — Mere possession of large quantity is NOT automatic intent to distribute. PWID requires intent beyond reasonable doubt.

---

## CHECKLIST FOR CASE COMPLETION

- [ ] Charge type and statute confirmed (R.S. 40:966-970 section identified)
- [ ] Substance and Schedule classification verified
- [ ] Net vs. gross weight determined and documented
- [ ] Lab testing status confirmed (tested or field test only?)
- [ ] Lab methodology audit completed (if tested)
- [ ] Search and seizure analysis routed to dw-suppression-motion
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

- **constructive-possession-framework.md** — Louisiana case-law analysis of constructive possession; the four-element *State v. Harris*, 472 So.2d 576 (La. 1985) test the State must prove beyond reasonable doubt
- **drug-diversion-programs.md** — Louisiana Art. 893, Art. 890, drug court, and pre-trial diversion programs; eligibility assessment to be completed before committing to trial strategy
- **drug-lab-methodology.md** — Field testing vs. confirmatory laboratory analysis: distinguishing preliminary screening from conclusive evidence of drug identity
- **drug-schedule-penalties.md** — Louisiana Controlled Dangerous Substances Act (R.S. 40:964-970) schedule-by-schedule substances and penalties (including marijuana special rules)
- **intent-to-distribute-factors.md** — Intent-to-distribute analysis framework: prosecution factors and defense counters; possession of large quantity is not automatic intent to distribute

