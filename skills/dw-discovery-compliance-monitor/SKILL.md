---
name: dw-discovery-compliance-monitor
description: >
  Living discovery ledger tracking demanded vs. produced items. ALWAYS invoke for "discovery
  log," "update the ledger," "what hasn't been produced," "missing discovery," or "late
  disclosure." Do NOT use for Brady/Giglio analysis — use dw-brady-giglio-auditor.
---

# Discovery Compliance Monitor
**Daniels & Washington | Criminal Defense | Louisiana / 5th Circuit**

Systematic tracker of prosecution disclosure obligations. Maintains a living ledger of what has been demanded, what has been produced, what is outstanding, and what may have been suppressed. This tool converts discovery obligations from abstract constitutional duties into concrete, auditable tasks.

### Source Citation Mandate

Every ledger entry must trace back to a specific source document. When the defense argues that discovery is missing or late, the court will ask: where was this demanded, and what was or wasn't produced? Precise sourcing in the ledger turns a vague complaint into a documented compliance failure.

**Citation format:** Cite the document title, page number, and paragraph or item number. Examples:
- `(Defense Discovery Demand, 03/01/2026, Item #14)`
- `(State's Discovery Response, 03/15/2026, p. 3, Item #14 — "N/A")`
- `(Supplemental Discovery Production, 04/01/2026, Bates #00345-00360)`
- `(Court Order Compelling Discovery, 03/20/2026, para. 3)`
- `(State's 701 Motion Response, p. 2, para. 4)`
- `(Minute Entry, 03/22/2026 — State represents all discovery produced)`

**Multiple-source rule:** When documenting a gap, cite both the demand and the production (or lack thereof) — e.g., `(Demand Item #14; State's Response — "N/A"; no supplemental production as of 04/05/2026)`.

**Unsourced assertions:** If a discovery gap cannot be documented with specific demand-and-response citations, mark it `[UNSOURCED — VERIFY WITH CASE FILE]`.

**Where sourcing applies:** Every ledger entry — demands, productions, gaps, late disclosures, and compliance status updates. Legal authority citations follow normal citation format.

---

## STEP 0 — FILE INTAKE HARD STOP

**DO NOT PROCEED with analysis until all discovery materials are uploaded.**

Before beginning any discovery audit:

1. **Receive explicit instruction:** "I have uploaded all discovery in Case [CLIENT/CASE NUMBER]"
2. **Confirm file receipt:**
   - All demand letters (initial and supplemental) present
   - All discovery production received to date present
   - Any prior discovery motions/orders present
   - Charging documents present
   - Court orders present
3. **Verify completeness:** Ask "Are there additional discovery files to upload, or shall I proceed with audit?"
4. **Once confirmed:** Proceed to STEP 1

This prevents incomplete analysis and ensures no critical files are overlooked.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## STEP 1 — Information Gathering Protocol

All information must be extracted from uploaded documents or explicitly provided by user. Ranked by criticality:

### ESSENTIAL (Case-Critical)

- **Charges:** Specific counts with Louisiana Revised Statutes cites (e.g., La. R.S. 14:109 for manslaughter)
- **Discovery demands filed:**
  - Initial demand (date, scope)
  - All supplemental demands (dates, specific items)
  - Standing Brady/Giglio orders (if any)
- **Discovery produced to date:**
  - Dates of productions
  - General categories of items
  - Any productions marked "incomplete" or "under review"
- **Charging document:** Bill of Information or Indictment with count descriptions
- **Arraignment date:** Current status
- **All court dates:** Pretrial conferences, status hearings, discovery deadlines, trial date

### STRATEGIC (Case-Development)

- **Defense theory:** What the defense intends to prove; how discovery relates
- **Witness list:** Prosecution and defense witnesses (to assess discovery sufficiency)
- **Expert list:** Any retained or prosecution experts (triggers discovery of underlying data, reports, CVs, prior opinions)
- **Co-defendant status:** Joint trial, severed, guilty plea, cooperation (affects discovery obligations)
- **Plea offers:** Any formal offers (to assess discovery's impact on evaluation)

### CONTEXTUAL (Enhancement)

- **Case chronology:** Arrest → charges → arraignment → discovery
- **Attorney notes:** Flag any items the defense attorney suspects are missing
- **Prior discovery motions/orders:** What has been ruled, what discovery was compelled, what was denied

---

## STEP 2 — Louisiana Discovery Framework

Louisiana criminal discovery is governed by La. C.Cr.P. (Code of Criminal Procedure), Articles 716-729.5. The state has broad **continuing duty** to disclose favorable material.

### **La. C.Cr.P. Art. 716 — Disclosure by the State (Defendant's Statements)**

**What Must Be Disclosed:**
- All written statements made by the defendant
- Any oral statements reduced to writing (interrogation summaries, agent notes)
- Audio/video recordings of defendant statements
- Any statements made to law enforcement, jail informants, or other government agents

**When:**
- Upon request (not automatic)
- No later than 10 days before trial (La. C.Cr.P. Art. 723)
- Continuing obligation if new statements obtained

**Remedy for Non-Compliance:**
- Motion to exclude statement (La. C.Cr.P. Art. 729.3)
- In extreme cases: mistrial, continuance, or contempt

---

### **La. C.Cr.P. Art. 717 — Disclosure by the State (Co-Defendant Statements)**

**What Must Be Disclosed:**
- All written statements of co-defendants
- Oral statements reduced to writing
- Audio/video recordings of co-defendant statements
- Plea agreements with co-defendants (typically contains admissions)

**When:**
- Upon request
- At least 10 days before trial
- Continuing obligation

**Remedy for Non-Compliance:**
- Exclusion of co-defendant statement
- Severance from co-defendant trial (if joint prosecution)
- Mistrial (if violation extremely prejudicial)

---

### **La. C.Cr.P. Art. 718 — Discovery of Documents and Tangible Objects**

**What Must Be Disclosed:**
- All police reports, narratives, supplemental reports
- Photographs, diagrams, sketches of crime scenes
- Physical evidence logs and custody records
- Search warrants and results
- Subpoenas issued and responses
- Any documents in the state's possession relating to the charges

**When:**
- Upon request
- No later than 10 days before trial
- Continuing obligation

**Remedy for Non-Compliance:**
- Exclusion of document/tangible object
- Continuance for inspection and investigation
- Sanction under Art. 729.3

---

### **La. C.Cr.P. Art. 719 — Discovery of Reports and Results of Scientific Tests**

**What Must Be Disclosed:**
- DNA reports and underlying data
- Drug testing results (qualitative and quantitative analysis)
- Toxicology reports
- Fingerprint reports and comparison photos
- Ballistics reports
- Any forensic analysis (fiber, gunshot residue, blood spatter)
- Expert reports prepared for the state
- CV and prior opinions of expert witnesses
- All underlying lab notes, protocols, accreditation documentation
- Negative or inconclusive results

**When:**
- Upon request
- At least 10 days before trial
- Continuing obligation if new testing performed

**Remedy for Non-Compliance:**
- Expert testimony excluded
- Exclusion of scientific report
- Continuance for independent testing
- Sanction under Art. 729.3

---

### **La. C.Cr.P. Art. 720 — Discovery of Statements of Witnesses (Jencks Material)**

**What Must Be Disclosed:**
- All written statements of witnesses (including police interviews, written statements, affidavits)
- Audio/video recorded statements of witnesses
- Oral statements reduced to writing (detective notes)
- Grand jury transcripts (witness testimony)
- Plea agreements with witnesses/informants (contains witness admissions)

**When:**
- Upon request (generally, per La. C.Cr.P. Art. 723)
- **IMPORTANT:** Prior statements of prosecution witnesses may be withheld until they are called to testify (Jencks Act analog), then must be produced before cross-examination
- Continuing obligation

**Remedy for Non-Compliance:**
- Witness statement excluded
- Testimony excluded
- Continuance for examination of statement
- Mistrial (if witness credibility material and suppressed)

---

### **La. C.Cr.P. Art. 721 — Disclosure of Informant Identity**

**What Must Be Disclosed:**
- Informant identity, subject to exception for confidential informants
- If confidential informant is necessary to the defense, identity must be revealed on in camera motion
- Information regarding informant reliability, compensation, prior accusations

**When:**
- Upon proper request and showing of need
- Subject to protective order

**Remedy for Non-Compliance:**
- In camera hearing on identity
- Possible dismissal of charges if informant testimony essential to prosecution

---

### **La. C.Cr.P. Art. 722 — Continuing Duty to Disclose**

**Critical Provision:**
The state has a **continuing obligation** to disclose throughout the case, including:
- After initial production
- After supplemental demands
- Up to and during trial
- If new evidence discovered or obtained by law enforcement

**When:**
- No fixed deadline; triggered by discovery of new material
- Materiality standard applies

**Remedy for Non-Compliance:**
- Late disclosure: motion to exclude, continuance, or sanction
- Brady violation: reversal on appeal if material and suppressed

---

### **La. C.Cr.P. Art. 723 — Discovery Procedures**

**What This Article Covers:**
- Mechanism for requesting discovery (written demand)
- State's obligation to respond within 10 days
- Defense right to request list of discovery
- Time limits for production
- Duty to make discovery available for inspection

**Key Timing Rule:**
All discovery must be produced **no later than 10 days before trial**, except:
- Jencks material (witness statements) — may be withheld until witness called
- Protective order material — subject to court order
- Informant identity — subject to in camera hearing

---

### **La. C.Cr.P. Art. 724 — Protective Orders**

**What This Article Covers:**
- State may request protective order for sensitive discovery (informant files, police techniques, medical records)
- Court may limit disclosure to defense counsel or defense experts only
- Order must be narrowly tailored to legitimate state interest

**Key Point:**
A protective order does **not** eliminate the discovery obligation; it merely limits who can see the material.

---

### **La. C.Cr.P. Art. 725 — Sanctions for Non-Compliance**

**Enforcement Mechanism:**
If state fails to comply with discovery obligation:
- Court may strike state's evidence
- Court may declare mistrial
- Court may hold prosecutor in contempt
- Court may dismiss charges

---

### **La. C.Cr.P. Art. 729.3 — Sanctions Available for Procedural Violations**

**Specific Sanctions for Discovery Violations:**

| Sanction | Application | Standard |
|----------|-------------|----------|
| **Mistrial** | State's discovery violation is so prejudicial defense cannot recover | High bar; must show exceptional prejudice |
| **Exclusion of Evidence** | State-discovered evidence produced late or withheld | Depends on materiality and prejudice |
| **Continuance** | Defense needs time to investigate late discovery | Reasonable request if discovery substantial |
| **Contempt** | Prosecutor or agent willfully violates discovery order | Requires knowing/willful violation |
| **Adverse Inference** | Allow jury instruction that withheld evidence would have favored defense | Available in Brady context; aggressive remedy |

---

### **La. C.Cr.P. Art. 729.5 — Additional Sanctions**

Court has discretion to impose additional sanctions including:
- Dismissal of charges (for extreme violations)
- Striking of state's evidence
- Suppression of evidence obtained through discovery violation
- Criminal prosecution of prosecutor for willful suppression (rare)

---

### **Constitutional Overlay: Brady, Giglio, and Kyles**

**Brady v. Maryland, 373 U.S. 83 (1963)**
- Prosecution must disclose evidence **favorable to the defense**
- Violation occurs if evidence is "favorable," "material," and "suppressed"
- Applies even if defense does not request evidence
- **Three-Pronged Test:**
  1. Evidence favorable to defense (exculpatory or impeachment)
  2. Material (reasonable probability of different outcome)
  3. Suppressed (known to prosecution, withheld from defense)

**Giglio v. United States, 405 U.S. 150 (1972)**
- Specific application of Brady to **impeachment material**
- Prosecutor must disclose information that could impeach credibility of state's witness
- Failure to disclose witness credibility material violates Brady/Giglio

**Kyles v. Whitley, 514 U.S. 419 (1995)**
- Constructive knowledge: prosecution has duty to search all agents' files
- Cumulative materiality: assess materiality of suppressed evidence collectively, not item-by-item
- Prosecution responsible for evidence in police files even if prosecutor didn't personally know

**Strickler v. Greene, 527 U.S. 263 (1999)**
- Brady has three components: favorable evidence, materiality, and suppression
- Defense must prove each element to prevail
- Brady claim independent of defense's diligence (no "could have discovered" defense)

**Smith v. Cain, 565 U.S. 73 (2012)**
- Witness statements are "favorable evidence" even if witness credibility disputed
- Materiality assessment accounts for defense's ability to use statement for impeachment

**State v. Knapper** (Louisiana Supreme Court)
- Louisiana adopts Brady/Giglio standards
- Prosecution has duty to disclose all favorable evidence
- "Favorable evidence" broadly construed to include any evidence assisting defense

**Connick v. Thompson, 563 U.S. 51 (2011)**
- Context: prosecutor office liability for discovery violations
- Individual prosecutors may have qualified immunity
- But reflects that Brady violations are serious constitutional violations

---

## MODULE A — Discovery Demand Generator

This module generates comprehensive, tiered discovery demands covering all material the prosecution must produce under Louisiana law and Constitution.

### **Initial Discovery Demand Template**

**TO: [District Attorney / Assistant District Attorney]**

**RE: Discovery Demand — State v. [Defendant] / Case No. [Number]**

**DATE: [Today's Date]**

---

#### **PART I — DEFENDANT'S STATEMENTS (La. C.Cr.P. Art. 716)**

The defense demands all of the following:

1. All written statements made by the defendant to law enforcement
2. All audio/video recordings of statements by the defendant
3. Summaries or reports of oral statements made by the defendant (interrogation notes, interview summaries)
4. All statements made by defendant to jail informants, undercover agents, or cooperating witnesses
5. Any consent forms, Miranda waivers, or invocation of rights documentation
6. Any statements made by defendant at any court proceeding

---

#### **PART II — CO-DEFENDANT STATEMENTS (La. C.Cr.P. Art. 717)**

1. All written statements of co-defendants
2. All audio/video recordings of co-defendant statements
3. Summaries or reports of co-defendant statements
4. Plea agreements with co-defendants (in entirety)
5. Proffer agreements or cooperation agreements with co-defendants

---

#### **PART III — DOCUMENTS AND TANGIBLE OBJECTS (La. C.Cr.P. Art. 718)**

1. All police reports (narrative, supplemental, detective follow-up)
2. All dispatch records and 911 calls (audio and transcript)
3. All photographs, video, and diagrams of crime scene
4. All photographs, video, and documentation of defendant
5. All photographs, video, and documentation of alleged victim(s)
6. All evidence logs, chain of custody records
7. All search warrant applications and returns
8. All inventory of items seized
9. All property/evidence receipts
10. All arrest reports and booking documentation
11. All traffic stop documentation (if applicable)
12. All citation or ticket documentation
13. All surveillance footage from any source (police, private, commercial)
14. All body-worn camera footage
15. All dash camera footage
16. All patrol vehicle camera footage
17. All photographs of injuries to any party
18. All sketches, diagrams, or maps prepared by law enforcement
19. All expert diagrams or reconstructions

---

#### **PART IV — SCIENTIFIC TESTS AND EXPERT REPORTS (La. C.Cr.P. Art. 719)**

1. All DNA reports and underlying data, methodology, controls
2. All laboratory reports for DNA (including bench notes, testing protocol, accreditation)
3. All drug testing qualitative results
4. All drug testing quantitative results (weight/purity)
5. All laboratory reports for drug analysis (including bench notes, protocol)
6. All toxicology reports and underlying test data
7. All toxicology lab notes and methodology
8. All fingerprint reports and comparison photographs
9. All fingerprint lab notes and analysis documentation
10. All ballistics reports and comparison photographs
11. All ballistics lab notes and examination documentation
12. All gunshot residue testing (GSR) reports
13. All fiber analysis reports
14. All trace evidence analysis reports
15. All blood spatter analysis reports and photographs
16. All pathology or medical examiner reports
17. All autopsy reports
18. All photographs from autopsy/medical examination
19. All toxicology from medical examiner
20. All expert reports prepared by state experts (in full, including all drafts)
21. Curriculum vitae (CV) of all state experts
22. Prior opinions or testimony of state experts
23. Accreditation and certification documentation for all testing facilities
24. Quality assurance records for all testing procedures
25. Validation studies for any novel forensic technique
26. Negative or inconclusive test results
27. Results of any testing performed but not relied upon by state
28. All bench notes, raw data, and original work product related to all testing

---

#### **PART V — WITNESS STATEMENTS (La. C.Cr.P. Art. 720 — Jencks Material)**

1. All written statements of prosecution witnesses
2. All audio/video recorded statements of prosecution witnesses
3. All oral statements of prosecution witnesses reduced to writing (interview notes, detective summaries)
4. All prior inconsistent statements made by prosecution witnesses
5. Grand jury transcript (if defendant indicted by grand jury)
6. Testimony of witnesses before grand jury (if available)
7. All affidavits prepared by witnesses
8. All prior police reports or incident reports prepared by witnesses (if witnesses are officers)

---

#### **PART VI — INFORMANT IDENTITY AND INFORMATION (La. C.Cr.P. Art. 721)**

1. All information regarding confidential informants, including:
   - Identity of informant (subject to in camera review if necessary)
   - Reliability and credibility history of informant
   - Prior accusations made by informant
   - Compensation or benefits given to informant
   - Criminal history of informant
   - All statements made by informant
2. All controlled buys or undercover operations
3. All recordings of informant conversations
4. Any records of informant payments or benefits

---

#### **PART VII — BRADY AND GIGLIO MATERIAL (Constitutional Mandatory Disclosure)**

1. All exculpatory evidence (evidence that tends to negate guilt or reduce culpability)
2. All evidence of innocence or credible alternative suspects
3. All impeachment material regarding prosecution witnesses:
   - Prior misconduct by law enforcement witnesses
   - Prior dishonesty or dishonest acts
   - Bias, motive, or interest in the case
   - Financial incentives or benefits
   - Prior complaints of dishonesty or bias
4. All evidence of witness credibility problems
5. All prior inconsistent statements by prosecution witnesses
6. All deals, promises, or benefits given to witnesses
7. Evidence of law enforcement bias or motivation to frame defendant
8. Evidence of mistaken identity or unreliable identification procedures
9. Evidence of police misconduct in the investigation

---

#### **PART VIII — BODY CAMERA AND DASH CAMERA FOOTAGE**

1. All body-worn camera (BWC) footage from all officers involved
2. All dash camera footage from all patrol vehicles involved
3. All in-car video system (ICVS) footage
4. All audio recordings from body cameras and dash cameras
5. All timestamps and metadata associated with footage
6. Logs of camera activation/deactivation times

---

#### **PART IX — COMMUNICATIONS EVIDENCE**

1. All 911 calls (audio and transcript) related to the incident
2. All dispatch radio records and recordings
3. All cellular phone records for defendant and alleged victim (calls, texts, data usage)
4. All cellular phone forensic extractions (if performed)
5. All social media records, posts, messages, and account information
6. All email records (if relevant)
7. All text message records
8. All messaging app communications (WhatsApp, Facebook Messenger, etc.)

---

#### **PART X — LOCATION AND GPS DATA**

1. All cellular phone location data
2. All cell tower records
3. All GPS data from vehicles involved
4. All GPS data from tracking devices (if any)
5. All location data from social media check-ins or applications
6. All records from any tracking devices

---

#### **PART XI — FINANCIAL RECORDS**

1. All financial records of defendant
2. All bank account records
3. All credit card records
4. All records of payments or transfers
5. All financial information relevant to motive

---

#### **PART XII — OFFICER AND AGENT RECORDS**

1. Prior complaints against all officers involved
2. Internal affairs investigations of officers involved
3. Personnel files of all officers involved (Henthorn material, limited by privacy law)
4. Prior dishonesty or credibility findings
5. Prior disciplinary action
6. History of racial profiling complaints or patterns
7. Prior use of force complaints
8. Prior allegations of planting evidence or dishonesty
9. Commendations or disciplinary records

---

#### **PART XIII — AGENCY POLICIES AND TRAINING**

1. All policies governing the investigation or arrest
2. All training records for officers involved
3. All policies regarding evidence handling and chain of custody
4. All policies regarding interrogation and recording of statements
5. All policies regarding identification procedures
6. All policies regarding use of force

---

#### **PART XIV — GRAND JURY MATERIALS**

1. Grand jury transcript (if indicted)
2. All evidence presented to grand jury
3. All testimony before grand jury
4. Any exculpatory evidence presented to grand jury (or not presented)

---

#### **PART XV — PLEA AGREEMENTS AND COOPERATION**

1. All plea agreements with co-defendants
2. All proffer agreements or cooperation agreements
3. All statements of cooperating witnesses
4. All benefits or considerations given to cooperating witnesses

---

#### **PART XVI — PRIOR CONVICTIONS AND IMPEACHMENT RECORDS**

1. Prior convictions of prosecution witnesses (for impeachment under La. C.E. Art. 609)
2. Prior acts of dishonesty or false statement (for impeachment)
3. Prior disciplinary actions against law enforcement witnesses
4. Prior credibility findings against prosecution witnesses

---

#### **TIME FOR PRODUCTION**

All discovery requested herein shall be produced no later than **10 days before trial**, except that Jencks Act material may be withheld until the witness is called to testify, at which point it must be produced immediately.

The undersigned requests written confirmation of receipt of this demand and an estimate of when production will occur.

---

### **Supplemental Discovery Demand Template**

After reviewing initial production, supplemental demand should address:

1. **Gaps in initial production** — items listed in demand but not produced
2. **Deficient production** — incomplete or partial items
3. **New theories emerging** — requests for additional categories based on produced evidence
4. **Expert discovery** — requests for underlying data to expert reports
5. **Late-discovered evidence** — requesting items that appear to have been created or obtained after initial demand
6. **Clarification** — requests for explanation of incomplete or unclear items

---

## MODULE B — Discovery Production Tracker (Core Module)

**Living ledger of all discovery demanded, produced, outstanding, late, or never produced.**

This tracker is the operational heart of the compliance monitor. It converts abstract discovery obligations into concrete, trackable items.

### **DISCOVERY PRODUCTION TRACKER — [Case Name] / [Case No.]**

| Item # | Category | Description | Demanded (Date) | Produced (Date) | Status | Days Outstanding | Notes |
|--------|----------|-------------|-----------------|-----------------|--------|-------------------|-------|
| 1 | Statements (Art. 716) | Defendant's written statements to NOPD | 3/1/2024 | 3/8/2024 | RECEIVED | 0 | 2-page statement; appears complete |
| 2 | Statements (Art. 716) | Defendant's interrogation audio/video | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Critical — likely exists; withheld? |
| 3 | Police Reports (Art. 718) | Initial arrest report | 3/1/2024 | 3/8/2024 | RECEIVED | 0 | Complete report; 8 pages |
| 4 | Police Reports (Art. 718) | Supplemental detective reports | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Multiple reports expected; none produced |
| 5 | Photographs (Art. 718) | Crime scene photographs | 3/1/2024 | 3/15/2024 | LATE | 0 | Produced 14 days late; 47 photos |
| 6 | Photographs (Art. 718) | Photographs of defendant at time of arrest | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Should exist per arrest report |
| 7 | 911 Calls (Art. 718) | 911 call audio and transcript | 3/1/2024 | 3/8/2024 | RECEIVED | 0 | 2 calls; audio clear |
| 8 | Dispatch Records (Art. 718) | Dispatch radio recordings | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Essential; likely retained |
| 9 | Scientific Tests (Art. 719) | Drug analysis report | 3/1/2024 | 3/22/2024 | LATE | 0 | Produced 21 days late |
| 10 | Scientific Tests (Art. 719) | Lab bench notes for drug testing | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Underlying data; critical |
| 11 | Scientific Tests (Art. 719) | DNA report | 3/1/2024 | PENDING | OUTSTANDING | 35+ | No DNA alleged; confirm not performed |
| 12 | Witness Statements (Art. 720) | Written statement from Officer Martinez | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Will be needed before trial |
| 13 | Witness Statements (Art. 720) | Interview notes from alleged victim | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Prior inconsistent statement possible |
| 14 | Officer Records | Prior complaints against Sgt. Brown | 3/1/2024 | PENDING | OUTSTANDING | 35+ | Potentially Brady material |
| 15 | Brady/Giglio | All exculpatory evidence | 3/1/2024 | NONE | DISPUTED | 35+ | DA claims none exists; assert Brady order |

---

### **STATUS LEGEND**

| Status | Definition |
|--------|-----------|
| **RECEIVED** | Item produced in full, complete, and timely |
| **OUTSTANDING** | Item demanded; no production to date |
| **PARTIALLY PRODUCED** | Item produced but appears incomplete or edited |
| **LATE** | Item produced but after 10-day deadline |
| **NEVER PRODUCED** | Item demanded; deadline passed; no indication of production |
| **DISPUTED** | State claims item doesn't exist or is privileged; dispute pending |
| **UNDER REVIEW** | State claims item under review/redaction; timeline unclear |

---

### **AUTOMATED FLAGS**

The tracker should automatically flag items that are:

- **Outstanding 30+ days** — Use reminder language: "Item outstanding beyond 10-day statutory deadline"
- **Outstanding 60+ days** — Escalate: "Potential motion to compel or sanctions warranted"
- **Outstanding 90+ days** — Critical: "Presumptively withheld; consider Brady violation"
- **Partially produced** — Query: "Is production complete? Request clarification"
- **Produced late** — Calculate: "Item late by [X] days. Assess prejudice and need for continuance"

---

### **COMPLIANCE METRICS**

Calculate automatically:

- **Total items demanded:** [Count]
- **Items received:** [Count] ([%])
- **Items outstanding:** [Count] ([%])
- **Items late:** [Count] with average delay of [X] days
- **Estimated compliance:** [%] of demand satisfied

**Interpretation:**
- 95%+ compliance: Adequate (monitor for pattern)
- 75-94% compliance: Deficient (consider motion to compel)
- 50-74% compliance: Significantly deficient (motion to compel + sanctions recommended)
- <50% compliance: Presumptive Brady violation; consider writ application

### **PRIORITIZED MISSING ITEMS REPORT**

After updating the discovery ledger, generate a Prioritized Missing Items Report that synthesizes all outstanding discovery items into a defense-focused deliverable. This transforms raw ledger data into an actionable list ranked by defense impact.

For each missing item (e.g., body-cam footage, dispatch logs, lab notes, personnel files, 911 audio):

- **Item Description:** What is missing and why it should exist (cite the source document that references or implies its existence)
- **Priority Ranking:**
  - **CRITICAL** — Constitutional materiality (Brady/Giglio material, exculpatory evidence)
  - **HIGH** — Direct impact on defense theory at trial
  - **MEDIUM** — Corroborative value or impeachment potential
  - **LOW** — Administrative completeness
- **Source Citation:** The specific demand, report, or document that references or implies the item should have been produced — e.g., `(Arrest Report, p. 3, para. 2 — references "dash cam recording" but no video produced)` or `(Defense Discovery Demand, 03/01/2026, Item #14)`
- **Deadline Urgency:** Days until next court date or discovery deadline

This report feeds directly into the **dw-criminal-defense** Phase 2 Report 7 (Table of Missing Discovery) and triggers the Auto-Action Missing Discovery Demand Letter. Route CRITICAL items immediately to **dw-brady-giglio-auditor**.

---

## MODULE C — Brady/Giglio Compliance Ledger (Critical Module)

**Separate, parallel ledger specifically tracking exculpatory and impeachment material.**

This module operates independently from the general discovery tracker because Brady/Giglio material may be:
- Withheld intentionally or inadvertently
- Scattered across various agencies' files
- Subject to constructive knowledge (Kyles)
- Cumulative in materiality (Kyles)

### **BRADY/GIGLIO COMPLIANCE LEDGER — [Case Name] / [Case No.]**

| Item # | Item Description | Type (Brady/Giglio/Both) | Why Favorable to Defense | Demanded? | Produced? | Materiality Assessment | Missing? | Action Required |
|--------|------------------|-------------------------|--------------------------|-----------|-----------|------------------------|----------|-----------------|
| 1 | Prior complaint against Officer Martinez for dishonesty (2019) | Giglio | Impeaches key witness credibility | Yes (3/1) | No | MATERIAL — credibility critical | YES | Motion for discovery; if not produced, adverse inference |
| 2 | Lab report showing inconclusive results on contested evidence | Brady | Exculpatory; tends to exclude defendant | Yes (3/1) | Yes (3/22) — **LATE** | MATERIAL — supports innocence | No | Calculate prejudice of late disclosure; assess trial impact |
| 3 | Alternative suspect identified but ruled out | Brady | Exculpatory; alternative theory | Yes (3/1) | No | MATERIAL — weakens prosecution case | YES | Critical; demand immediately; consider sanctions |
| 4 | Witness credibility issue (prior recantation) | Giglio | Impeaches witness | Yes (3/1) | No | MATERIAL — if witness testifies | LIKELY | Demand; assert Giglio standing order |
| 5 | Police photo showing potential exculpatory evidence in background | Brady | Exculpatory evidence | Yes (3/1) | Partial (some photos, not all) | POTENTIALLY MATERIAL | YES | Demand all photos; assess completeness |
| 6 | Internal memo noting suspect identifications were unreliable | Brady | Exculpatory; undermines ID | Yes (3/1) | No | MATERIAL — directly supports defense | YES | Assert Brady violation; demand immediately |
| 7 | Officer bias/motivation notes from investigation file | Brady | Shows prosecution bias | Yes (3/1) | No | MATERIAL — relevant to credibility | YES | Demand; Brady material |
| 8 | Evidence of improper investigation technique | Brady | Undermines reliability of evidence | Yes (3/1) | No | POTENTIALLY MATERIAL | LIKELY | Demand detailed investigation protocols |
| 9 | Plea agreement with cooperating witness showing financial incentive | Giglio | Impeaches witness motive | Yes (3/1) | Yes (3/8) | MATERIAL — incentive must be disclosed | No | Ensure full plea agreement produced; assess sufficiency |
| 10 | Laboratory protocols not followed in evidence testing | Brady | Taints reliability of evidence | Implicit | No | HIGHLY MATERIAL — challenges all testing | YES | Demand QA records; expert may need to examine |

---

### **BRADY/GIGLIO LEGAL FRAMEWORK**

For each item, assess against three-pronged test:

**Brady/Giglio Materiality Test:**

1. **Favorable to Defense?** — Does the evidence:
   - Negate an element of the crime?
   - Provide alternative explanation?
   - Impeach a prosecution witness?
   - Suggest bias or motive?
   - Show unreliability of identification?
   - Undermine credibility of evidence?

2. **Material?** — Would the evidence:
   - Affect verdict (reasonable probability of different outcome)?
   - Undermine confidence in conviction?
   - Cumulative with other suppressed evidence?

3. **Suppressed (Known and Withheld)?** — Did the prosecution:
   - Know of the evidence?
   - Withhold it from the defense?
   - Have constructive knowledge (Kyles)?

**If all three elements satisfied: Brady/Giglio violation.**

---

### **CONSTRUCTIVE KNOWLEDGE (Kyles Standard)**

Prosecution is responsible for:
- Evidence in all police agency files
- Evidence in crime lab files
- Evidence in DA's own files
- Evidence that could be "reasonably located" within government agencies
- Even if individual prosecutor didn't personally review the evidence

---

### **CUMULATIVE MATERIALITY (Kyles Standard)**

Brady violation assessment must consider:
- Evidence collectively, not item-by-item
- If suppressed evidence taken together would create reasonable probability of different outcome, violation exists
- Don't dismiss individual items as "minor" without considering cumulative impact

---

### **IMPEACHMENT VS. EXCULPATORY**

- **Brady Material:** Exculpatory evidence (tends to prove innocence or negate guilt)
- **Giglio Material:** Impeachment evidence (impeaches credibility of prosecution witness)
- **Both:** Evidence that is both exculpatory and impeaches key witness

---

## MODULE D — Late Disclosure Impact Assessment

When discovery is produced after the statutory 10-day deadline (La. C.Cr.P. Art. 723):

### **LATE DISCLOSURE PROTOCOL**

**STEP 1 — Document the Late Disclosure**

| Element | Information |
|---------|-------------|
| **Item** | [Specific discovery item] |
| **Demanded** | [Date of demand] |
| **Deadline** | 10 days before trial = [Specific date] |
| **Actually Produced** | [Actual date produced] |
| **Days Late** | [Calculate] |
| **Type** | Critical / Significant / Minor |

---

**STEP 2 — Assess Prejudice to Defense**

| Prejudice Factor | Assessment |
|------------------|-----------|
| **Complexity of Material** | Does item require complex analysis? Can expert review in time? |
| **Time Until Trial** | How much time does defense have to prepare response? |
| **Nature of Item** | Is it witness statement? Scientific evidence? Documentary? |
| **Criticality to Case** | Is this item outcome-determinative? Can defense proceed without it? |
| **Reasonable Notice** | Could defense have anticipated this evidence would exist? |
| **Defense Investigation** | What additional investigation does late disclosure require? |
| **Expert Review** | If expert needed, can expert review and prepare within remaining time? |
| **Cross-Examination** | Can defense prepare adequate cross-examination with condensed timeline? |
| **Cumulative Prejudice** | Are multiple late disclosures creating pattern of prejudice? |

**Materiality of Prejudice:**
- **No prejudice:** Defense had sufficient time to prepare response and it's not outcome-determinative
- **Minor prejudice:** Defense had to compress preparation but can respond adequately
- **Significant prejudice:** Defense preparation compromised; expert review incomplete; cross-examination insufficient
- **Severe prejudice:** Impossibility to adequately prepare; outcome likely affected

---

**STEP 3 — Determine Need for Continuance**

| Factor | Analysis |
|--------|----------|
| **Time Available** | How many days between late disclosure and trial? |
| **Expert Needed?** | Does defense expert need to review and prepare? (Likely yes for scientific evidence) |
| **Inconsistencies** | Are there prior statements by prosecution witness that contradict late-disclosed evidence? |
| **Investigation** | Does defense need additional investigation based on late disclosure? |
| **Reasonable Request** | Is continuance request reasonable given circumstances? |

**Presumptions:**
- Scientific evidence produced fewer than 10 days before trial: Continuance presumptively justified
- Witness statement produced fewer than 5 days before trial: Continuance justified
- Documentary evidence produced fewer than 2 days before trial: Continuance justified
- Brady/Giglio material produced any time late: Continuance warranted (and possible dismissal)

---

**STEP 4 — Evaluate Evidence Exclusion Under Art. 729.3**

**Standard:** Court has discretion to exclude evidence produced late under La. C.Cr.P. Art. 729.3 if:

1. State failed to comply with discovery deadline
2. Exclusion serves interests of justice
3. Defense prejudiced by late disclosure
4. No other adequate remedy available

**Factors for exclusion:**

- Evidence not within discovery demand? → Less likely to exclude
- Prosecution had evidence but failed to produce timely? → More likely to exclude
- Late disclosure due to negligence vs. impossibility? → Negligence favors exclusion
- Evidence is critical to prosecution case? → Courts may exclude more readily if prejudice severe
- Pattern of late disclosure? → Prior violations increase exclusion likelihood

**Practical Application:**
- Late DNA report produced 5 days before trial with no warning → Strong argument for exclusion
- Late witness statement discovered by prosecution only days before trial → Exclusion appropriate
- Late-discovered evidence from new witness → Depends on whether state knew witness existed

---

**STEP 5 — Generate Motion for Sanctions**

See Module F for motion templates. Late disclosure typically supports motions for:
- **Continuance:** to allow adequate preparation
- **Exclusion:** of evidence under Art. 729.3
- **Sanctions:** against prosecution for failure to comply with discovery obligations
- **Adverse Inference:** allowing jury instruction that evidence should be viewed skeptically

---

**STEP 6 — Track Pattern of Late Disclosure**

Create summary table:

| Item | Days Late | Category | Total Items | Running Pattern |
|------|-----------|----------|-------------|-----------------|
| Item 1 | 14 days | Photos | 1 | 1 item late |
| Item 2 | 21 days | Lab report | 2 | Pattern emerging |
| Item 3 | 7 days | Witness statement | 3 | Pattern established |

**Pattern Assessment:**
- 1-2 late items: Isolated incident (request explanation)
- 3+ late items: Pattern of non-compliance (consider sanctions motion)
- Mix of substantive + administrative items late: Systemic problem (escalate)

---

## MODULE E — Supplemental Discovery Demand Generator

After reviewing initial production, auto-generate supplemental demands based on gaps, inconsistencies, and new information.

### **SUPPLEMENTAL DEMAND TRIGGERS**

Supplemental demand should be filed when:

1. **Gap Identified in Production Tracker**
   - Item listed in initial demand; deadline passed; not produced
   - Request written explanation and deadline for production
   - Include language: "If this discovery no longer exists, state must explain when it was destroyed and why"

2. **Incomplete Production**
   - Item produced but appears partial (e.g., 5 of 12 photos; 2 of 5 police reports)
   - Demand: "Please provide complete set of [Item]; clarify if additional materials exist and timeline for production"

3. **New Leads from Initial Production**
   - Produced police report references other items not produced (e.g., "Officer notes attached" — no notes produced)
   - Produced statement mentions prior complaint against witness — demand that complaint
   - Produced photo shows unidentified individuals — demand identification

4. **Witness Statements Referencing Unknown Individuals**
   - Witness statement: "I saw the defendant talking to a man in a blue jacket"
   - Demand: "Identify the individual in blue jacket and produce all statements/evidence regarding this person"

5. **Expert Reports Lacking Underlying Data**
   - Drug lab report produced; bench notes not included
   - Demand: "Provide all bench notes, raw data, QA records, and test protocols used in analysis"

6. **Co-Defendant Plea Agreements**
   - If any co-defendant pleads, their plea agreement may contain admissions relevant to defense
   - Demand: "Provide all plea agreements and statements by co-defendants"

7. **Law Enforcement Discipline Records**
   - If any officer has questionable credibility, demand:
     - Prior complaints (Henthorn discovery)
     - Disciplinary findings
     - Prior instances of dishonesty or credibility issues

8. **Informant Connections**
   - If informant was used, demand:
     - Identity (subject to in camera review)
     - Reliability history
     - Prior accusations by informant
     - Compensation or benefits
     - Criminal history

---

### **SUPPLEMENTAL DEMAND TEMPLATE**

**TO: [District Attorney / Assistant District Attorney]**

**RE: SUPPLEMENTAL DISCOVERY DEMAND — State v. [Defendant] / Case No. [Number]**

**DATE: [Today's Date]**

---

Pursuant to La. C.Cr.P. Articles 716-729 and Brady v. Maryland, 373 U.S. 83 (1963), the defense hereby files this supplemental discovery demand. In reviewing the state's initial production dated [Date], the following gaps have been identified:

**PART I — ITEMS DEMANDED BUT NOT PRODUCED**

1. **Interrogation Audio/Video of Defendant** — Arrest report references "recorded interrogation"; no audio/video produced. Demand production within 5 business days. If destroyed, provide certification of destruction with date and reason.

2. **Supplemental Police Reports** — Initial arrest report references "detective follow-up ongoing." Demand all supplemental reports prepared since initial demand.

3. **Photographs of Defendant at Arrest** — Arrest report states "photos taken of defendant"; no photos in production. Demand within 5 business days.

4. **Dispatch Radio Recordings** — Police reports reference specific radio transmissions (e.g., "dispatch cleared scene at 2:15 PM"). Demand dispatch audio for [Time Range].

---

**PART II — ITEMS PRODUCED BUT APPARENTLY INCOMPLETE**

1. **Crime Scene Photographs** — 47 photos produced; police report references "examination of defendant's vehicle." Are photos of vehicle included? If not, demand immediately.

2. **Witness Statements** — Detective notes state "Interview with Jane Doe" but no statement of Jane Doe produced. Demand written statement or recorded interview.

---

**PART III — UNDERLYING DATA FOR EXPERT REPORTS**

1. **Drug Lab Report** — Lab report provided (dated [Date]) but no bench notes or raw test data included. Demand:
   - All bench notes
   - Raw test data
   - QA/QC records
   - Lab protocols used
   - Calibration records
   - Accreditation documentation
   - Negative controls
   - Standards used
   - Prior test results on same substance (if any)

---

**PART IV — INFORMATION REFERENCED BUT NOT PRODUCED**

1. [Specific Example from Initial Production]

---

**PART V — BRADY/GIGLIO MATERIAL**

The state is reminded of its continuing duty under Brady v. Maryland and Giglio v. United States to disclose all exculpatory and impeachment material. The defense specifically demands:

1. All evidence of witness credibility problems
2. All evidence of law enforcement bias or motivation
3. All evidence of alternative suspects
4. All evidence of unreliable investigation techniques
5. All prior complaints or discipline against officers involved

---

**PRODUCTION DEADLINE**

All discovery shall be produced within **5 business days** of this demand. The state is reminded that discovery obligations are not favors; they are constitutional mandates. Continued failure to produce may result in motions to compel, sanctions, and/or exclusion of evidence under La. C.Cr.P. Art. 729.3 and Brady/Giglio principles.

---

## MODULE F — Discovery Motion Practice

Templates and frameworks for discovery-related motions under Louisiana law.

### **MOTION TO COMPEL DISCOVERY**

**Standard:** Court may compel production if state has failed to produce discovery within 10 days of demand (La. C.Cr.P. Art. 723).

**Elements of Motion:**

1. **Specific Items:** List each item demanded, date demanded, and status
2. **Statutory Basis:** Cite La. C.Cr.P. Art. [716-721] requiring production
3. **Prior Demand:** Show that discovery was demanded and deadline has passed
4. **Prejudice:** Explain how withholding prejudices defense
5. **Relief:** Request production within [X] days and cost shifting if applicable

**Template Language:**

> The defense respectfully moves this Court to compel the state to produce discovery in violation of La. C.Cr.P. Articles 716-723. Specifically, the state has failed to produce the following items despite repeated demand:
>
> [List items]
>
> These items are required to be disclosed under La. C.Cr.P. Art. [___], which requires the state to produce [Specific obligation]. The state's failure to produce prejudices the defense by:
> - Preventing adequate investigation
> - Preventing expert review
> - Preventing preparation for cross-examination
> - Preventing preparation for trial
>
> Wherefore, the defense requests that the Court order production of all discovery within 5 business days, and such other relief as the Court deems just and equitable.

---

### **MOTION FOR SANCTIONS FOR DISCOVERY VIOLATIONS**

**Standard:** Court may impose sanctions for discovery violations under La. C.Cr.P. Art. 729.3, including exclusion of evidence, mistrial, continuance, contempt, or dismissal.

**Elements of Motion:**

1. **Violation Established:** Show clear violation of discovery obligation
2. **Materiality:** Show evidence is material to guilt/innocence
3. **Prejudice:** Show defense prejudiced by violation
4. **Proportionality:** Request sanctions proportionate to violation

**Sanction Hierarchy:**
- **Lightest:** Continuance to allow preparation
- **Moderate:** Exclusion of evidence produced late
- **Severe:** Mistrial, dismissal

**Template Language:**

> The State's failure to produce [Item] violates La. C.Cr.P. Art. [___] and prejudices the defense. The evidence is material because [Explanation]. The defense has been prejudiced because [Specific prejudice]. Under La. C.Cr.P. Art. 729.3, this Court has discretion to impose sanctions including [Specific sanction requested].
>
> Wherefore, the defense requests [Specific relief].

---

### **MOTION FOR BRADY/GIGLIO STANDING ORDER**

Many courts will issue standing orders directing ongoing disclosure of Brady/Giglio material throughout the case.

**Template Language:**

> Pursuant to Brady v. Maryland, 373 U.S. 83 (1963) and Giglio v. United States, 405 U.S. 150 (1972), the prosecution has a duty to disclose all exculpatory and impeachment evidence. To ensure compliance, the defense respectfully requests that the Court issue a standing order requiring:
>
> 1. Continuing disclosure of all Brady material throughout the case
> 2. Continuing disclosure of all Giglio material regarding prosecution witnesses
> 3. Disclosure of all law enforcement discipline or credibility issues
> 4. Certification of compliance by the prosecutor on the record
> 5. Sanctions for violations of this order

---

### **MOTION TO EXCLUDE LATE-DISCLOSED EVIDENCE**

**Standard:** Court may exclude evidence under La. C.Cr.P. Art. 729.3 if produced late and defense prejudiced.

**Elements:**

1. **Timeline:** Show when evidence was demanded vs. when produced
2. **Deadline:** Show statutory deadline (10 days before trial per Art. 723)
3. **Lateness:** Show how late the disclosure is
4. **Prejudice:** Show defense cannot adequately respond
5. **No Waiver:** Show defense did not waive the violation

**Template Language:**

> The State produced [Item] on [Date], which is [X] days after the statutory deadline of [Date]. This late disclosure violates La. C.Cr.P. Art. 723 and prejudices the defense because:
>
> [Specific prejudice — expert review impossible, cross-examination inadequate, investigation incomplete]
>
> Under La. C.Cr.P. Art. 729.3, the defense requests that this evidence be excluded to serve the interests of justice.

---

### **MOTION FOR CONTINUANCE DUE TO LATE DISCOVERY**

**Standard:** Court should grant continuance if discovery is late and defense needs time to respond.

**Elements:**

1. **Late Disclosure:** Show discovery was produced after statutory deadline
2. **Nature of Evidence:** Explain why additional preparation time is needed
3. **Trial Date:** Show trial date is imminent
4. **Reasonable Request:** Show continuance is reasonable, not dilatory
5. **Prejudice Without Continuance:** Explain how proceeding would be unfair

**Template Language:**

> The State produced [Item] on [Date], only [X] days before trial. This evidence [Description] requires expert review / investigation / witness preparation. The defense cannot adequately prepare for trial without additional time. The Court should grant a continuance of [X] days to allow the defense adequate preparation time. This is not dilatory; rather, it serves the interests of justice and ensures a fair trial.

---

### **MOTION FOR IN CAMERA INSPECTION (Protective Orders)**

If state claims protective order applies to certain discovery, motion for in camera inspection.

**Standard:** Court may review material in camera to determine if protective order is warranted.

**Template Language:**

> The State has claimed that certain discovery is subject to a protective order. The defense respectfully requests that the Court review this material in camera to determine:
>
> 1. Whether a legitimate protective order applies
> 2. Whether the material is subject to Brady/Giglio disclosure regardless of protective order
> 3. What conditions on disclosure (counsel-only, expert-only) are appropriate
>
> Wherefore, the defense requests in camera inspection.

---

### **MOTION TO DISMISS FOR DISCOVERY VIOLATIONS (Extreme Cases)**

In extreme cases where discovery violations are so prejudicial that fair trial is impossible:

**Standard:** High bar; requires showing that "entire case is undermined" by discovery violations.

**Template Language:**

> The State's pattern of discovery violations [Describe pattern] has so prejudiced the defense that a fair trial is impossible. Specifically:
>
> [List specific violations and prejudice]
>
> This cumulative violation requires dismissal of charges to serve the interests of justice.

---

### **WRIT APPLICATION FOR DISCOVERY DISPUTES**

If trial judge refuses to compel discovery and appeal is necessary, consider writ application to supervisory court.

**Standard:** Louisiana Supreme Court may issue writ of mandamus to compel trial judge to compel discovery.

**Process:**
- File in Louisiana Supreme Court (or appellate court with original jurisdiction)
- Show trial judge abused discretion by refusing to compel
- Show legal right to discovery is clear
- Show no adequate remedy on appeal
- Request urgent review (may be expedited)

---

## MODULE G — Open File Policy Audit

Many Louisiana DA offices claim "open file discovery." This module audits whether "open file" claim is truthful and complete.

### **OPEN FILE POLICY AUDIT CHECKLIST**

**Question 1: Does an "Open File" Policy Officially Exist?**

- [ ] DA's office website states open file policy
- [ ] Standing order exists requiring open file discovery
- [ ] Prior written policy from DA's office available
- [ ] If policy exists, obtain copy and analyze scope

**Question 2: What Does "Open File" Mean in This Jurisdiction?**

Common interpretations:
- **Broad interpretation:** All materials generated during investigation available to defense
- **Narrow interpretation:** Police reports and witness statements; excluding internal memos, work product, informant files
- **Middle ground:** Police reports, offense reports, witness statements; excluding attorney work product and investigator-generated materials

Determine which version this DA applies.

---

**Question 3: What Physical Access Exists to Open File?**

- [ ] File available at DA's office during business hours
- [ ] Digital access available (email, portal, shared drive)
- [ ] Copies provided to defense attorney
- [ ] Limitations on copying (DA controls reproduction)

---

**Question 4: What Categories Are Excluded from "Open File"?**

Commonly excluded:
- Attorney work product (legal memos, strategy notes)
- Internal law enforcement memos (not from police reports)
- Informant files (subject to protective order)
- Personnel files (subject to privacy law)
- Ongoing investigation materials

**Audit:** Does the DA claim any of these are excluded? Demand legal basis for exclusion.

---

**Question 5: Verification — Is Everything in Open File Consistent with Statutory Discovery Demands?**

Create comparison table:

| Item Category | Required by La. C.Cr.P. | In Open File? | Status |
|---------------|------------------------|---------------|--------|
| Defendant statements | Art. 716 | Yes / No / Partial | Verify completeness |
| Co-defendant statements | Art. 717 | Yes / No / Partial | Verify completeness |
| Police reports | Art. 718 | Yes / No / Partial | Verify completeness |
| Scientific reports | Art. 719 | Yes / No / Partial | Verify completeness |
| Witness statements | Art. 720 | Yes / No / Partial | Verify completeness |
| Informant info | Art. 721 | Yes / No / Partial | Verify completeness |
| Brady/Giglio material | Constitutional | Yes / No / Partial | Verify completeness |

**Assessment:** If any required category is missing or incomplete, the "open file" is deficient and supplemental demands should be filed.

---

**Question 6: Are Items in Open File Complete and Unedit**?

- [ ] Police reports appear complete or note page numbers
- [ ] Photographs all present or log provided
- [ ] Audio files accessible
- [ ] Redactions, if any, clearly marked with basis
- [ ] No indication that items have been edited or altered

---

**Question 7: Are Brady/Giglio Items Included in Open File?**

Critical test: Does open file include:
- Evidence of witness credibility problems
- Evidence of law enforcement bias
- Evidence of alternative suspects
- Evidence of unreliable investigation

If "open file" claim is made but Brady/Giglio material is withheld, the claim is suspect.

---

### **OPEN FILE AUDIT SUMMARY REPORT**

**OPEN FILE POLICY AUDIT — [Case Name] / [Case No.]**

**Finding: [Open File Adequate / Deficient / Misleading]**

**Specific Findings:**

1. **Policy Definition:** [Policy exists / doesn't exist] and defined as [Narrow / Broad / Middle Ground]

2. **Access:** [Type of access provided]

3. **Excluded Categories:** [What is excluded and claimed basis]

4. **Comparison to Statutory Demand:** [Items missing / incomplete]

5. **Brady/Giglio Inclusion:** [Brady/Giglio material included / withheld]

6. **Completeness of Items:** [All items appear complete / significant redactions / items appear edited]

**Assessment:**

If open file is deficient, supplement with targeted demands for missing categories.

---

## MODULE H — Severity Classification

Classify discovery deficiencies by severity to prioritize responses:

### **CRITICAL Violations**

| Violation Type | Definition | Example | Response |
|----------------|-----------|---------|----------|
| **Brady Suppression** | Material exculpatory evidence knowingly withheld | Evidence of innocence; alternative suspect; exculpatory scientific result | Immediate motion to compel; writ if necessary; consider dismissal motion |
| **Giglio Suppression** | Material impeachment evidence withheld from key witness | Prior dishonesty by detective; credibility problem; bias | Immediate disclosure demand; standing order; cross-examination preparation |
| **Late Brady/Giglio** | Brady/Giglio material produced on eve of trial | Critical evidence disclosed days before trial | Motion to exclude; continuance; potential mistrial |
| **Evidence Destruction** | Material evidence destroyed without explanation | Police reports destroyed; recordings deleted; physical evidence discarded | Demand certification of destruction; adverse inference; possible dismissal |
| **Pattern of Suppression** | Multiple Brady/Giglio violations suggesting systemic problem | Repeated credibility issues withheld; repeated exculpatory evidence late | Pattern sanction motion; escalate to appellate level |

---

### **SIGNIFICANT Violations**

| Violation Type | Definition | Example | Response |
|----------------|-----------|---------|----------|
| **Substantial Delay** | Discovery produced 60+ days late | Lab report produced 90 days after demand | Motion for sanctions; assess prejudice; possible exclusion |
| **Partial Production** | Material produced but clearly incomplete | 5 of 12 police reports produced; 20 of 47 photos | Supplemental demand with follow-up deadline |
| **Incomplete Witness Statement** | Witness statement produced but appears edited or partial | Interview notes provided but question-and-answer portion missing | Demand complete version; assert withholding violation |
| **Expert Report Without Data** | Expert report provided but underlying data withheld | DNA report provided but not bench notes or raw data | Demand underlying data; expert may need to conduct independent review |
| **Informant File Withheld** | Informant information withheld without in camera hearing | Demand informant information; motion for in camera review |

---

### **MINOR Violations**

| Violation Type | Definition | Example | Response |
|----------------|-----------|---------|----------|
| **Administrative Delay** | Discovery produced 10-30 days late for non-critical items | Supplemental police report 14 days late | Note in tracker; request explanation |
| **Duplicate Production** | Same item produced multiple times | Same photo produced in two separate productions | Administrative; note in tracker |
| **Technical Deficiency** | Item produced but in format requiring conversion | Police report produced as TIFF instead of PDF | Request reformat; minor production issue |

---

## MODULE I — Report Template

Generate professional written report summarizing discovery compliance audit.

### **DISCOVERY COMPLIANCE REPORT — [Case Name/Client] / Case No. [___]**

**Prepared by:** [Defense Attorney/Firm]

**Date:** [Today's Date]

**Case Information:**

| Field | Information |
|-------|-------------|
| **Defendant(s)** | [Names] |
| **Charges** | [List counts with statutory cites] |
| **Case Number** | [Court/Case No.] |
| **Charging District** | [District, Parish] |
| **Trial Date** | [Date] |
| **Prosecutor(s)** | [Names] |

---

### **EXECUTIVE SUMMARY**

[1-2 paragraphs summarizing overall discovery compliance status, key findings, and recommended actions]

---

### **DISCOVERY DEMAND AND PRODUCTION SUMMARY**

| Metric | Status |
|--------|--------|
| **Initial Demand Filed** | [Date] |
| **Supplemental Demand(s) Filed** | [Dates, if any] |
| **Total Items Demanded** | [Number] |
| **Items Received Timely** | [Number] ([%]) |
| **Items Outstanding** | [Number] ([%]) |
| **Items Produced Late** | [Number] with average delay [X] days |
| **Overall Compliance** | [%] |

---

### **PRODUCTION TRACKER**

[Insert full production tracker from Module B]

---

### **BRADY/GIGLIO ANALYSIS**

[Insert Brady/Giglio ledger from Module C]

**Specific Brady/Giglio Concerns:**
- [Item 1]
- [Item 2]

---

### **LATE DISCLOSURE IMPACT ANALYSIS**

[For each late item, include analysis from Module D]

---

### **OPEN FILE POLICY AUDIT**

[Include audit findings from Module G]

---

### **SEVERITY CLASSIFICATION**

| Category | Items | Risk Level |
|----------|-------|-----------|
| **Critical** | [List] | HIGH |
| **Significant** | [List] | MEDIUM |
| **Minor** | [List] | LOW |

---

### **RECOMMENDED ACTIONS**

1. **Immediate (Within 48 hours):**
   - [Specific action]
   - [Specific action]

2. **Short-term (This week):**
   - [File supplemental demand]
   - [File motion to compel]

3. **Medium-term (Before trial):**
   - [Expert review]
   - [Investigation of gaps]

4. **Pre-trial Conference:**
   - [Raise discovery issues]
   - [Request ruling on Brady/Giglio material]

---

### **MOTIONS RECOMMENDED**

- [ ] Motion to Compel Discovery (Items: [List])
- [ ] Motion for Sanctions (Basis: [Describe])
- [ ] Motion for Continuance Due to Late Discovery (Timeline: [X] days)
- [ ] Motion for Brady/Giglio Standing Order
- [ ] Motion to Exclude Late-Disclosed Evidence (Items: [List])
- [ ] Writ Application (If: [Condition])

---

### **CROSS-EXAMINATION SEEDS**

For use in preparing witnesses for deposition or trial. See Module J below.

---

### **INTEGRATION NOTES**

- [ ] Evidence table in Case Tables.xlsx updated
- [ ] Pretrial Notebook/02-Discovery folder populated
- [ ] Cross-exam architect skill alerted to key witnesses
- [ ] Gaps flagged for ongoing investigation

---

## MODULE J — Cross-Examination Chapter Seeds

For use in dw-cross-exam-architect or trial preparation.

### **CROSS-EXAM SEED — Detective [Name] (Lead Investigator)**

**Topic: Discovery Withholding**

**Premise:** Detective [Name] participated in investigation and has knowledge of items that should exist but were not produced.

**Questions:**

1. "Detective [Name], in your investigation of this case, did you prepare any written reports beyond the [Specific Report produced]?"
   - Follow-up: "And those reports would contain evidence gathered?"
   - Objective: Establish that additional reports should exist

2. "You took photographs at the crime scene, correct?"
   - Follow-up: "And how many photographs did you take?"
   - Follow-up: "I've reviewed [Number] photographs produced; you said you took [Larger Number]; where are the rest?"

3. "In your interrogation of the defendant, did you record that conversation?"
   - Follow-up: "You didn't produce that recording to the defense, correct?"
   - Follow-up: "Why was a recording made but not disclosed?"

4. "You took statements from witnesses at the scene, correct?"
   - Follow-up: "Those statements were reduced to writing or recorded?"
   - Follow-up: "Those statements have been produced to the defense?"
   - Follow-up: "All of them?"

5. "In your investigation, did you identify any [Alternative suspects / prior complaints against officers / exculpatory evidence]?"
   - Follow-up: "And that was documented in your investigation file?"
   - Follow-up: "That documentation should have been produced to the defense?"

---

### **CROSS-EXAM SEED — Evidence Custodian / Records Clerk**

**Topic: Production Timeline and Completeness**

**Premise:** Records keeper has knowledge of when items were requested and when produced.

**Questions:**

1. "When did you receive the defense discovery demand?"
   - Follow-up: "What was the deadline for production?"
   - Follow-up: "Your office complied with that deadline?"

2. "For [Specific Item], when did you locate that item in your files?"
   - Follow-up: "And when did you deliver it to the prosecution?"
   - Follow-up: "And when did the prosecution deliver it to the defense?"
   - Objective: Establish timeline and identify delays

3. "Are there any items that you could not locate in your files?"
   - Follow-up: "Do your records show what happened to those items?"
   - Follow-up: "When were they destroyed?"

4. "For [Scientific Evidence], did the lab provide complete documentation?"
   - Follow-up: "Did that documentation include [Bench notes / raw data / QA records]?"
   - Follow-up: "Why not?"

5. "Is it your practice to produce all requested discovery or only a subset?"
   - Follow-up: "What determines what gets produced?"

---

### **CROSS-EXAM SEED — Prosecutor (Brady/Giglio Obligations)**

**Topic: Discovery Obligations and Compliance**

**Premise:** Prosecutor has duty to ensure all Brady/Giglio material disclosed.

**Questions:**

1. "As a prosecutor, you understand your obligation to disclose exculpatory evidence, correct?"
   - Follow-up: "You understand that obligation applies even if the defense doesn't specifically request that evidence?"

2. "In this case, you reviewed all police reports to identify any exculpatory evidence?"
   - Follow-up: "Did you find any?"
   - Follow-up: "And you disclosed it?"

3. "You understand your obligation to disclose any evidence that could impeach your witnesses?"
   - Follow-up: "In this case, [Specific Officer], you were aware of [Prior complaint / prior dishonesty], correct?"
   - Follow-up: "You disclosed that information?"

4. "If evidence came to your attention after your initial production, you would disclose it immediately?"
   - Follow-up: "Have you discovered any additional evidence since your last production?"

5. "You're familiar with Brady v. Maryland and Giglio v. United States?"
   - Follow-up: "Those cases impose affirmative obligations on the state?"
   - Follow-up: "You've complied with those obligations in this case?"

---

## MODULE K — Quick Reference Tables

### **LOUISIANA DISCOVERY ARTICLES MATRIX**

| Article | Topic | What Must Be Disclosed | Deadline | Penalty for Non-Compliance |
|---------|-------|------------------------|----------|---------------------------|
| 716 | Defendant statements | All written/recorded defendant statements | 10 days before trial | Exclusion; motion to compel |
| 717 | Co-defendant statements | All co-defendant statements and plea agreements | 10 days before trial | Exclusion; mistrial (if joint trial) |
| 718 | Documents & tangibles | Police reports, photos, physical evidence | 10 days before trial | Exclusion; sanction |
| 719 | Scientific tests | Lab reports, bench notes, underlying data | 10 days before trial | Exclusion; expert may need independent review |
| 720 | Witness statements | All witness statements (Jencks material) | 10 days before trial (withheld until witness testifies) | Exclusion; testimony excluded; mistrial |
| 721 | Informant identity | Informant identity and reliability info | Subject to in camera hearing | Possible dismissal if essential to defense |
| 722 | Continuing duty | Any new discovery obtained post-production | Upon discovery | Brady violation on appeal; reversal |
| 723 | Procedures | Response to discovery demand | 10 days of receipt | Motion to compel; Art. 729.3 sanctions |
| 724 | Protective orders | Limited disclosure for sensitive materials | As ordered by court | Contempt if violated |
| 725 | Sanctions enforcement | Court may compel through contempt | N/A | Contempt of court |

---

### **BRADY/GIGLIO ELEMENTS CHECKLIST**

Use this checklist for each potential Brady/Giglio item:

| Element | Brady | Giglio | Assessment |
|---------|-------|--------|-----------|
| **Favorable to defense?** | Exculpatory (proves innocence) | Impeaching (damages credibility) | Yes / No / Unclear |
| **Material?** | Reasonable probability different outcome | Impeachment affects verdict | Yes / No / Unclear |
| **Suppressed (known & withheld)?** | Prosecutor knew & withheld | Prosecutor knew & withheld | Yes / No / Unclear |
| **Constructive knowledge (Kyles)?** | Should have known from agency files | Should have known from agency files | Yes / No / Unclear |
| **Cumulative with others?** | Consider with other suppressed evidence | Consider with other suppressed evidence | Yes / No / Unclear |

**If all elements "Yes": Brady/Giglio violation exists.**

---

### **SANCTIONS COMPARISON TABLE**

| Sanction | Severity | Applicable When | Procedure |
|----------|----------|-----------------|-----------|
| **Continuance** | Low | Late discovery requires preparation | Motion to continue; presumptively granted if discovery late |
| **Exclusion of evidence** | Medium | Evidence produced late; prejudice shown | Motion under Art. 729.3; court discretion |
| **Continuance + Exclusion** | Medium-High | Pattern of late disclosure | Combined motion |
| **Mistrial** | Very High | Discovery violation so prejudicial fair trial impossible | Interlocutory appeal; high bar |
| **Dismissal** | Very High | Pattern of egregious violations; fair trial impossible | Motion; rarely granted |

---

### **DISCOVERY TIMELINE CALCULATOR**

**For use in tracking deadlines:**

| Event | Date | Deadline | Days Remaining |
|-------|------|----------|-----------------|
| Discovery demand filed | [Date] | 10 days | Calculate |
| Trial date | [Date] | [Determine] | Calculate |
| Pretrial conference | [Date] | [Determine] | Calculate |
| Supplemental demand filing | [Date] | [Determine] | Calculate |

---

## Guardrails

**Maintain objectivity and professionalism:**

- Track discovery status objectively; don't assume bad faith without evidence
- Distinguish between inadvertent omissions and willful suppression
- Document everything with dates, deadlines, and specific items
- Maintain professional tone in all motions and communications
- Remember: Discovery obligations are constitutional mandates, not favors

**Avoid:**
- Accusatory language without evidentiary support
- Assumption of bad faith by DA
- Failure to follow procedural requirements (notice, briefing, local rules)
- Missed deadlines for discovery motions
- Failure to preserve record for appeal

---

## Integration Points

This skill integrates with other Daniels & Washington tools:

- **Master Evidence Table** (Case Tables.xlsx) — updated with all discovered items
- **Pretrial Notebook** — 02-Discovery folder populated with all demand letters, correspondence, and production summaries
- **dw-cross-exam-architect** — seeded with discovery gaps and credibility issues for detective and prosecutor cross-examination
- **dw-criminal-defense** (Phase 4) — informs trial strategy around late disclosures and Brady issues
- **dw-expert-witness-evaluator** — validates that all underlying data for expert opinions has been produced

---

## Quick Reference — Brady/Giglio Standing Order Language

**Recommended language for requesting standing order in open court:**

> "Your Honor, the defense requests that the Court issue a standing order requiring the State to disclose all Brady and Giglio material throughout this case. Specifically, the State shall disclose:
>
> (1) All evidence favorable to the defense, including exculpatory evidence, evidence of innocence, and evidence tending to negate guilt;
> (2) All evidence that could impeach the credibility of prosecution witnesses, including prior dishonesty, bias, motive, or financial incentive;
> (3) All law enforcement discipline or credibility issues regarding officers who testify;
> (4) All evidence of alternative suspects;
> (5) All evidence of unreliable investigation techniques;
> (6) Any new evidence discovered or obtained after the initial production.
>
> This order shall remain in effect throughout trial and shall obligate the State to make immediate disclosure of any material discovered prior to or during trial.
>
> Failure to comply shall result in exclusion of evidence, continuance, or such other relief as the Court deems just."

---

**END OF SKILL.MD**

*This skill is maintained by Daniels & Washington and should be updated as Louisiana criminal procedure rules change or new case law develops.*


