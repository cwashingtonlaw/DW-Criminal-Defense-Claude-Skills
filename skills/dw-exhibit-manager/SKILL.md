---
name: dw-exhibit-manager
description: >
  Manages the full lifecycle of trial exhibits from pre-marking through admission.
  Tracks both State and Defense exhibits, maintains authentication chains, logs objections
  and rulings, and produces the clerk's exhibit list. ALWAYS invoke for "exhibit list,"
  "mark exhibits," "pre-mark exhibits," "exhibit management," "trial exhibits,"
  "authentication chain," "exhibit log," "admit exhibit," "exhibit objection,"
  "defense exhibits," "state exhibits," "exhibit tracker," "exhibit binder."
  Works alongside dw-trial-notebook-builder (assembles the trial notebook) and
  dw-appellate-error-monitor (tracks evidentiary objection errors for appeal).
---

# dw-exhibit-manager

**CORE PURPOSE:**
Track every exhibit in the case — both what the defense intends to offer and what the State may offer against your client. Pre-mark all exhibits, document the authentication method for each, anticipate objections with prepared responses, and maintain a complete trial record of what was offered, objected to, and admitted or excluded. Feed every sustained objection to appellate preservation.

**CORE RULES:**
1. Every exhibit must have a documented authentication method BEFORE trial
2. Every sustained objection must be flagged to dw-appellate-error-monitor for appeal preservation
3. Never assume an exhibit is admissible — always identify potential objections and prepare responses
4. Track both Defense AND State exhibits (know what's coming in against your client)
5. Maintain separate pre-trial (planned) and trial (actual) status — don't overwrite pre-trial plans
6. Demonstrative exhibits (timelines, charts) are NOT admitted into evidence — track them separately
7. For Art. 404(b) other crimes evidence, cross-reference with dw-404b-opposition for objection strategy
8. Source citation: every exhibit must trace back to its discovery source or defense investigation origin


---

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any exhibit lists, evidence inventories, exhibit physical/digital files, prior trial exhibit packages, or court orders setting exhibit protocols, do not analyze anything yet.**

Your only response must be:
> *"Before I begin — are you uploading any additional exhibit lists, evidence inventories, exhibit files, prior trial exhibit packages, court orders setting exhibit protocols, or discovery materials that may become exhibits? I'll start exhibit-management work only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** Mid-process discovery of an additional State exhibit, a missing authentication source, or a court order setting exhibit-marking conventions would require complete re-numbering, re-authentication mapping, and re-objection planning.

---

### Source Citation Mandate

Every factual assertion in the exhibit log, authentication chain, and objection record must trace back to a specific source document. Trial exhibits are admitted (or excluded) based on the documented foundation — chain of custody, authentication witness, business-record certification, or discovery production source. Unsourced claims about an exhibit's origin or authenticity will not survive an objection.

**Citation format:** Cite the document title, page number, and paragraph or timestamp. Examples:
- `(Discovery Production, Bates #00145-00148)`
- `(Lab Report — LSP Crime Lab, Sample #2026-001, p. 1)`
- `(Custodian Affidavit — Verizon Wireless, dated 03/15/2026)`
- `(Officer Smith BWC — Vehicle Stop, Timestamp 00:05:32)`
- `(Subpoena Return — St. Elizabeth's Medical Records, dated 03/15/2026)`
- `(Defense Investigator Report — Witness Interview Smith, 04/02/2026, p. 2)`

**Multiple-source rule:** When more than one document supports an exhibit's authentication, cite all of them — e.g., `(Custodian Affidavit — Verizon Wireless; Subpoena Return, dated 03/15/2026, p. 1)`.

**Unsourced assertions:** If an exhibit's source or authentication method cannot be tied to a specific document, mark it `[UNSOURCED — VERIFY WITH ATTORNEY/DISCOVERY]` so the team knows to confirm before pre-marking or offering at trial.

**Where sourcing applies:** All factual content — exhibit origin, chain-of-custody history, authentication witness identification, discovery Bates references. Evidentiary rules (La. C.E. Art. 901, 902, 803) and objection grounds follow normal legal citation format.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## WORKFLOW STEPS

### STEP 0.6 — LOAD CASE AND TRIAL CONTEXT

**Hard Stop Gate:** Before proceeding, establish foundational case data.

1. Invoke **dw-case-brain** to retrieve:
   - Case name, docket number, charges, trial date
   - Witness list (State's witnesses, defense witnesses)
   - Trial venue and judge assignment
   - Any prior trial dates or sentencing phase indicator

2. Invoke **dw-trial-notebook-builder** to check:
   - Does a trial notebook already exist?
   - If yes, import the existing exhibit list as the starting point
   - If no, begin fresh exhibit inventory

3. Confirm with attorney:
   - "What is the trial date? Which court? Which judge?"
   - Judges often have exhibit marking preferences (e.g., some prefer D-1, D-2; others prefer "Defense Exhibit 1")
   - "Are we pre-marking exhibits before trial, or tracking exhibits during trial, or both?"

4. Set scope:
   - Pre-trial only: Create pre-marked exhibit package with authentication checklists
   - Live trial: Prepare for real-time status updates as exhibits are offered and ruled upon
   - Both: Build full package and prepare for live tracking


### STEP 1 — EXHIBIT INVENTORY

Scan case folder for all potential exhibits and classify by type:

**Documentary Evidence:**
- Police reports, supplemental reports, incident reports
- Lab reports (toxicology, DNA, drug analysis, ballistics)
- Medical records, autopsy reports, ME reports
- Business records (phone records, bank records, surveillance system logs)
- Subpoenaed records (school records, employment records, hospital records)
- Text messages, email printouts, chat logs
- Prior statements (defendant statements, witness statements, recorded calls)

**Visual Evidence:**
- Photographs of crime scene, physical evidence, persons
- Video evidence (body-worn camera, dash cam, surveillance video, jail calls)
- Audio evidence (911 calls, recorded interviews, intercepted communications)

**Digital Evidence:**
- Phone dumps, social media screenshots, digital forensics reports
- GPS tracking data, cell site location information
- Metadata extraction (creation dates, modification dates, geolocation)

**Expert Evidence:**
- Expert reports, CVs, qualifications summaries
- Demonstrative exhibits created by experts (diagrams, models, animations)

**Defense Investigation:**
- Defense investigator reports, photographs, witness statements
- Interview recordings, charts, timelines

**Demonstrative Exhibits (Non-Admitted):**
- Timelines, maps, diagrams, organizational charts, financial charts
- Note: These aid jury understanding but are NOT admitted into evidence

Cross-reference with **dw-discovery-compliance-monitor** for authentication issues, chain of custody gaps, or Brady/Giglio concerns.


### STEP 2 — PRE-MARK EXHIBITS

Assign exhibit numbers following court convention:
- **Defense exhibits:** D-1, D-2, D-3... (or "Defense Exhibit 1" per court preference)
- **State exhibits:** S-1, S-2, S-3... (from State's exhibit list if provided)
- **Joint exhibits:** J-1, J-2... (stipulated items both parties agree to admit)

For each exhibit, create an **Exhibit Card** with the following fields:

| Field | Content |
|-------|---------|
| Exhibit # | D-1, S-1, J-1, etc. |
| Description | Short, clear description of the exhibit |
| Type | Document / Photo / Audio / Video / Physical / Digital / Demonstrative |
| Source | Discovery production, defense investigation, subpoena, stipulation |
| Bate Number | If Bates-stamped (e.g., "State-001234") |
| Authentication Method | Witness testimony, business records certification (La. C.E. Art. 803(6)), self-authenticating (La. C.E. Art. 902), stipulation |
| Authenticating Witness | Which witness will lay the foundation |
| Foundation Elements | Chain of custody, author identification, business records custodian, expert methodology, etc. |
| Anticipated Objections | Hearsay, relevance, authentication, best evidence, unfair prejudice (Art. 403), Confrontation, expert methodology |
| Response to Objections | Prepared responses citing La. C.E. articles and applicable case law |
| Offered During | Which witness's testimony, which trial phase (guilt/penalty) |
| Status | Pre-marked / Offered / Objected / Admitted / Excluded / Withdrawn |
| Pre-Trial Status | What we planned pre-trial (DO NOT overwrite during trial) |
| Trial Status | What actually happened at trial |


### STEP 3 — AUTHENTICATION CHAIN TRACKING

For each exhibit requiring testimonial authentication:

1. **List foundation questions:**
   - Who observed the exhibit? When? Where?
   - How was it created, collected, or obtained?
   - What is its condition now versus when created?
   - Has there been any gap in chain of custody?

2. **Identify the authenticating witness:**
   - Police officer, detective, lab technician, business records custodian, defendant, bystander
   - Note: Not every witness can authenticate every exhibit

3. **Note hearsay exceptions if needed** (La. C.E. Art. 803, 804):
   - Business records (803(6)): Requires custodian or preparer
   - Public records (803(8)): Lab reports, police records
   - Excited utterances (803(2)): 911 calls, bystander statements
   - State of mind (803(3)): Diary entries, threat statements
   - Confrontation Clause issues: Davidison v. Prince (La. 2017) — lab reports without analyst testimony

4. **Flag Art. 901 issues:**
   - Authentication requirements — circuit court must be satisfied exhibit is what it claims to be
   - For demonstratives: Must be authenticated as fair and accurate representation

5. **Cross-reference with dw-cross-exam-architect:**
   - If the authenticating witness is cross-examined, note impeachment opportunities
   - Prepare direct examination to prevent cross-examination impeachment

**For self-authenticating exhibits (La. C.E. Art. 902):**
- Certified copies of public records
- Official publications, government seals
- Business records with proper certification
- Note: Even self-authenticating exhibits subject to relevance and hearsay objections


### STEP 4 — LIVE TRIAL TRACKING

During trial, update exhibit status in real-time as attorney reports offers and rulings. Use exact timestamped language:

**Exhibit Offered:**
- "D-1 offered" → Status: Offered | Time: [HH:MM] | During: [witness name]
- Record which witness testimony context

**Objection Lodged:**
- "D-1 objection — hearsay" → Log in Objection Log
- Objecting party: State / Defense
- Basis: Hearsay, authentication, relevance, unfair prejudice, best evidence, Confrontation, expert methodology, etc.
- Objecting attorney name

**Ruling Made:**
- "D-1 objection overruled, admitted" → Status: Admitted | Ruling: Overruled | Time: [HH:MM]
- "D-1 objection sustained, excluded" → Status: Excluded | Ruling: Sustained | Time: [HH:MM]
- Record judge's exact ruling language if possible

**Limiting Instruction:**
- If court gives limiting instruction ("Exhibit D-1 admitted only for [specific purpose], not for [excluded purpose]")
- Record exact language for appellate purposes

**Automatic Appellate Flag:**
- Every excluded exhibit (Ruling: Sustained) → AUTOMATICALLY flag to **dw-appellate-error-monitor**
  - "Exhibit [#] excluded — [basis] — trial date [date] — Judge [name] — Preserve for appeal"

**Withdrawn:**
- If attorney withdraws exhibit offer before ruling: Status: Withdrawn | Time: [HH:MM]
- Note reason if disclosed (e.g., authentication foundation missing, opposing counsel made record objection)


### STEP 5 — OBJECTION LOG

Maintain a running objection log for ALL evidentiary objections encountered at trial (not just exhibit objections):

| # | Exhibit | Party Offering | Objecting Party | Basis | Court's Ruling | Limiting Instruction | Appeal Flag |
|---|---------|---------------|-----------------|-------|-----------------|---------------------|-------------|
| 1 | D-1 | Defense | State | Hearsay - not exception | Sustained | N/A | YES - Preserve |
| 2 | S-3 | State | Defense | Relevance - unfair prejudice 403 | Overruled | Limited to [purpose] | NO |
| 3 | D-5 | Defense | State | Authentication - chain gap | Sustained | N/A | YES - Preserve |

**Common Louisiana Evidentiary Objections:**
- **Hearsay (Art. 802):** Out-of-court statement offered for truth — identify exception if applicable (Art. 803, 804)
- **Relevance (Art. 401/402):** Not probative of material fact OR probative value substantially outweighed by unfair prejudice (Art. 403)
- **Unfair Prejudice (Art. 403):** Probative but unduly prejudicial to party (e.g., gruesome photos, prior bad acts)
- **Authentication (Art. 901):** Insufficient foundation that exhibit is what it claims to be
- **Best Evidence (Art. 1002):** Original writing/recording required (exception for duplicate or oral testimony)
- **Confrontation Clause (Crawford v. Washington, 541 U.S. 36):** Testimonial hearsay against criminal defendant without cross-opportunity
- **Privilege (Art. 505-514):** Attorney-client, spousal, clergy, physician-patient, psychotherapist, etc.
- **Character Evidence (Art. 404/405):** Character evidence generally inadmissible except limited exceptions
- **Other Crimes (Art. 404(b)):** Evidence of other bad acts not admissible to prove character or propensity
- **Expert Methodology (Art. 702 / Daubert-Foret):** Expert methodology unreliable or not sufficient basis for opinion

**Feed sustained objections to appellate preservation:**
Every time the court sustains an objection to a defense exhibit or allows State evidence against objection, automatically flag to **dw-appellate-error-monitor** with:
- Exhibit number or statement
- Objection basis
- Ruling (Sustained / Overruled)
- Judge's exact language if available
- Trial date and judge name


### STEP 6 — OUTPUTS

All outputs saved to: `<case-root>/03 - Trial Notebook/01 - Exhibit List/`

**6A. Master Exhibit List (.xlsx)**

File name: `[ClientLastName] - Master Exhibit List - [TrialDate].xlsx`

Spreadsheet with full exhibit tracker. Columns:
- Exhibit #
- Description
- Type
- Source
- Bate Number
- Authentication Method
- Authenticating Witness
- Foundation Elements
- Anticipated Objections
- Response to Objections
- Offered During
- Pre-Trial Status
- Trial Status (actual ruling)

Separate sheets:
- Defense Exhibits (D-1, D-2, etc.)
- State Exhibits (S-1, S-2, etc.)
- Joint Exhibits (J-1, J-2, etc.)
- Excluded Exhibits (all exhibits ruled inadmissible)

**6B. Clerk's Exhibit List (.docx)**

File name: `[ClientLastName] - Clerk Exhibit List - [TrialDate].docx`

Formatted document for filing with clerk of court (post-trial). Columns:
- Exhibit #
- Description
- Party Offering
- Date Offered
- Court's Ruling (Admitted / Excluded)
- Ruling Language (if applicable)

Include cover letter with case name, docket number, trial judge, trial date.


**6C. Objection Log (.xlsx)**

File name: `[ClientLastName] - Objection Log - [TrialDate].xlsx`

Complete record of all evidentiary objections for appellate preservation. Columns:
- #
- Exhibit / Statement
- Party Offering
- Objecting Party
- Objection Basis
- Court's Ruling (Sustained / Overruled)
- Limiting Instruction (if any)
- Appeal Flag (YES / NO)
- Judge Name
- Trial Date
- Notes

Filter for "Appeal Flag: YES" to generate the list for dw-appellate-error-monitor.

**6D. Authentication Checklist (.docx)**

File name: `[ClientLastName] - Authentication Checklist - [TrialDate].docx`

Per-exhibit authentication requirements for attorney use at counsel table during trial. Format:

```
EXHIBIT D-1: [Brief Description]
Authenticating Witness: [Name, title]
Foundation Elements:
  1. Who created / obtained / observed?
  2. When?
  3. Where?
  4. How was it handled since creation?
  5. Chain of custody breaks?

Key Foundation Questions:
  Q: [Foundation question 1]
  Q: [Foundation question 2]
  [etc.]

Anticipated Objections & Responses:
  Objection: Hearsay
  Response: Not offered for truth; or falls under [exception], La. C.E. Art. [###]
  
  Objection: Authentication
  Response: [witness name] will testify he/she [foundation]
```

Use dw-cross-exam-architect output to identify cross-examination vulnerabilities.


---

## INTEGRATION

**Reads from:**
- **dw-case-brain:** Case context, charges, witness list, trial date, judge assignment
- **dw-trial-notebook-builder:** Existing exhibit list (if trial notebook already created)
- **dw-cross-exam-architect:** Witness examination plans and cross-examination vulnerabilities
- **dw-discovery-compliance-monitor:** Evidence inventory and authentication issues
- **dw-chain-of-custody-auditor:** Chain of custody gaps and evidence handling concerns

**Writes to:**
- **dw-appellate-error-monitor:** Every sustained objection automatically, with exhibit #, objection basis, ruling, judge, trial date
- **dw-case-brain:** Update case status with exhibit admission/exclusion summary post-trial
- **Trial Notebook folder:** Master Exhibit List (xlsx), Clerk's Exhibit List (docx), Objection Log (xlsx), Authentication Checklist (docx)

**Feeds into:**
- **dw-trial-notebook-builder:** Final exhibit package (Master Exhibit List, Authentication Checklist, Clerk's Exhibit List)
- **dw-appellate-error-monitor:** Sustained objections and excluded exhibits for error preservation
- **dw-404b-opposition:** If any exhibits implicate Art. 404(b) other crimes evidence, cross-reference for objection strategy

**Uses these skills:**
- **xlsx skill:** Master Exhibit List, Objection Log
- **docx skill:** Clerk's Exhibit List, Authentication Checklist

---

## SPECIAL SITUATIONS

**Demonstrative Exhibits (Non-Admitted)**

Demonstrative exhibits (timelines, diagrams, organizational charts, financial charts, maps) are used to aid jury understanding but are NOT admitted into evidence. Track these separately:
- Mark as Type: "Demonstrative"
- Status: "Used for illustration" (not "Admitted")
- No court ruling on admissibility required
- Cannot cite as fact to jury; used only to illustrate testimony
- Store separately in Trial Notebook (not in admitted exhibits)


**Art. 404(b) Other Crimes Evidence**

If any exhibit references other crimes, bad acts, or uncharged conduct:
1. Flag as "Art. 404(b) Concern" in exhibit card
2. Cross-reference immediately with **dw-404b-opposition** for objection strategy
3. Prepare for bifurcated ruling (court may rule outside jury's presence)
4. Note if evidence is offered by State — prepare affirmative objection
5. If Defense uses such evidence (rare), ensure it passes Art. 404(b) test:
   - Offered for permissible purpose (not character/propensity)
   - Probative of that purpose
   - Not unduly prejudicial (Art. 403)

**State's Exhibits (Adverse Evidence)**

Track State's exhibits with same rigor as Defense exhibits:
- Pre-trial: Obtain State's exhibit list (discovery obligation)
- Analyze each State exhibit for authentication gaps, chain of custody breaks, hearsay problems
- Prepare objections pre-trial and assign objection strategy to attorney
- At trial: Log State's offers and track objections (both State objections and Defense objections)
- Post-trial: Analyze excluded State exhibits for potential appeal

**Confrontation Clause Issues (Crawford v. Washington)**

For any testimonial hearsay offered against defendant (lab reports, statements by unavailable witnesses):
1. Identify if it's testimonial (created with primary purpose of proving defendant committed crime)
2. Determine if witness unavailable and defendant had prior opportunity to cross
3. If both true: Confrontation problem — prepare Art. 901(b) objection or demand live testimony
4. Examples: Lab reports without analyst (Davidison v. Prince), police reports offered for truth, victim statements
5. Flag for dw-appellate-error-monitor if court overrules Confrontation objection

**Prior Statements (Impeachment vs. Substantive)**

If offering a witness's prior inconsistent statement (La. C.E. Art. 607, 613):
1. Determine if offered for impeachment only OR substantive use
2. If impeachment: Lay foundation (confrontation about statement)
3. If substantive: Must fall under exception (excited utterance, state of mind, etc.)
4. Track separately in exhibit list with authentication method clearly noted
5. Mark anticipated objection: "Hearsay — if offered substantively"


**Expert Reports & CVs**

Expert reports and curriculum vitae exhibit cards:
1. Report itself: Authenticating witness is the expert; foundation is expert's personal knowledge
2. CV: Self-authenticating or offered through expert's testimony
3. Authentication method: Expert testimony (Daubert / Foret reliability challenge)
4. Anticipated objections:
   - Hearsay (if factual bases contain hearsay, note exception)
   - Expert methodology (Art. 702, Daubert-Foret standard)
   - Relevance (expert's opinion on ultimate issue limited)
5. Cross-reference with **dw-expert-witness-evaluator** for methodology vulnerabilities

**Audio/Video Evidence**

For BWC, dash cam, surveillance video, jail calls, recorded interviews:
1. Authentication method: Officer/videographer testimony + chain of custody
2. Foundation: Who recorded, when, where, equipment used, no alterations, accurate depiction
3. Anticipated objection: Entire video is not offered — identify clips/segments
4. If edited/redacted: Flag that court may require unedited version for inspection
5. Best Evidence rule: Original recording or certified copy required (La. C.E. Art. 1002)
6. Cross-reference with **dw-video-evidence-auditor** for technical authentication issues

**Digital Evidence (Phone Dumps, Social Media, Metadata)**

For phone extractions, social media screenshots, metadata:
1. Chain of custody: Who extracted, what tool used, forensic certification
2. Authentication: Expert testimony on extraction methodology + relevance
3. Screenshots vs. native files: Native files more reliable
4. Anticipated objections:
   - Authentication (sufficient foundation for digital extraction)
   - Relevance (social media relevance often marginal)
   - Hearsay (social media posts are statements by third parties)
5. Cross-reference with **dw-forensic-dump-analyzer** and **dw-social-media-auditor** for content analysis


**Business Records (La. C.E. Art. 803(6))**

For business records (phone records, bank statements, hospital records, police reports):
1. Authentication method: Business records certification OR custodian testimony
2. Foundation elements required:
   - Record made in regular course of business
   - Kept in course of regularly conducted activity
   - Made at or near time of occurrence
   - Habit or routine practice
   - Absence of circumstances suggesting lack of trustworthiness
3. Custodian certification (preferred):
   - Custodian prepares affidavit/certificate
   - Affidavit authenticated by notary (self-authenticating, La. C.E. Art. 902)
   - No live testimony required unless challenged
4. If no certification: Custodian must testify live to foundation
5. Anticipated objections:
   - Hearsay (if document contains statements by third parties — separate objection)
   - Authenticity (if certification lacking or incomplete)
   - Relevance (records may be voluminous — prepare to offer only relevant portions)

**Physical Evidence**

Physical evidence (weapon, drug evidence, clothing, personal items):
1. Chain of custody: Every person who handled must be identified and testify
2. Authentication: Identifying characteristics (photo, description, serial number, markings)
3. Foundation: Where found, who found, condition, handling, no contamination/alteration
4. Anticipated objections:
   - Chain of custody (gaps or breaks)
   - Authentication (not clearly identified)
   - Unfair prejudice (gruesome items, weapons)
5. Note: Some physical evidence inadmissible if prejudicial outweighs probative value (Art. 403)
6. Cross-reference with **dw-chain-of-custody-auditor** for custody gaps before trial


---

## WORKFLOW EXECUTION CHECKLIST

Use this checklist to ensure complete exhibit management:

**PRE-TRIAL PHASE:**
- [ ] Invoked dw-case-brain for case context and trial date
- [ ] Checked with dw-trial-notebook-builder for existing exhibit list
- [ ] Confirmed trial date, court, judge, and judge's exhibit marking preference with attorney
- [ ] Confirmed scope: pre-trial only, live trial only, or both
- [ ] Completed STEP 1 — Exhibit Inventory (all documentary, visual, digital, expert, demonstrative exhibits identified)
- [ ] Cross-referenced dw-discovery-compliance-monitor for authentication issues
- [ ] Completed STEP 2 — Pre-mark all exhibits with exhibit cards (all columns populated)
- [ ] Completed STEP 3 — Authentication chain tracking (foundation questions, witness ID, hearsay exceptions noted)
- [ ] Completed STEP 4 — Prepared for live trial (attorney briefed on exhibit offer procedures)
- [ ] Generated OUTPUTS:
  - [ ] Master Exhibit List (.xlsx) with all columns and separate sheets (Defense, State, Joint, Excluded)
  - [ ] Authentication Checklist (.docx) ready for counsel table
  - [ ] Objection Log template (.xlsx) prepared
  - [ ] Clerk's Exhibit List template (.docx) prepared

**LIVE TRIAL PHASE (if applicable):**
- [ ] Attorney provides exhibit offer, objection, and ruling information in real-time
- [ ] Update exhibit status for each offered exhibit (Offered → Objected → Ruled → Admitted/Excluded)
- [ ] Log all evidentiary objections in Objection Log with basis and ruling
- [ ] For every sustained objection: AUTOMATICALLY flag to dw-appellate-error-monitor
- [ ] Track limiting instructions from court
- [ ] Update Master Exhibit List with trial status (actual ruling column)

**POST-TRIAL PHASE:**
- [ ] Finalize Objection Log with all trial objections
- [ ] Finalize Clerk's Exhibit List with court rulings
- [ ] Generate Excluded Exhibits sheet (all ruled inadmissible)
- [ ] Feed all sustained objections to dw-appellate-error-monitor
- [ ] Update dw-case-brain with exhibit admission/exclusion summary
- [ ] Prepare trial notebook package for dw-trial-notebook-builder
- [ ] File Clerk's Exhibit List with clerk of court (if required by local rule)


---

## JUDGE-SPECIFIC PREFERENCES

Exhibit marking conventions vary by judge. Confirm before pre-marking:

**Common Preferences:**
- Some judges prefer: D-1, D-2, D-3 (shorthand)
- Other judges prefer: "Defense Exhibit 1," "Defense Exhibit 2" (spelled out)
- Some courts use: Plaintiff/Defense (civil-style) even in criminal
- Louisiana state court conventions often vary by parish and judge

**Other Judge Preferences:**
- Some judges require pre-trial submission of exhibit list (order to show compliance)
- Some judges require joint exhibit list agreed by both parties
- Some judges allow exhibits only on testimony, others allow pre-trial marking
- Some judges require exhibit binders organized by exhibit number
- Some judges require Bates numbering on all exhibits

**Action:** Always ask attorney or check local rules / prior cases before this judge.

---

## COMMON OBJECTION RESPONSES (LOUISIANA EVIDENTIARY RULES)

Quick reference for prepared responses to common objections:

**Hearsay Objection → Responses:**
- "Not offered for truth; offered to show [specific non-hearsay use]"
- "Falls under La. C.E. Art. 803(6) business records exception"
- "Falls under La. C.E. Art. 803(2) excited utterance; witness will testify circumstances"
- "Falls under La. C.E. Art. 803(3) state of mind; relevant to defendant's knowledge"
- "Stipulated hearsay exception per agreement of the parties"
- "Witness will be available for cross-examination; no Confrontation problem"

**Authentication Objection → Responses:**
- "[Witness name] will testify he/she [personal knowledge / created / observed]"
- "Self-authenticating under La. C.E. Art. 902 [specify category]"
- "Certified business record under La. C.E. Art. 803(6); certification attached"
- "Exhibit bears identifying characteristics [describe]; foundation will be established"

**Relevance Objection → Responses:**
- "Probative of [specific element]; relevant under La. C.E. Art. 401"
- "Not unduly prejudicial; probative value substantially outweighs unfair prejudice (Art. 403)"
- "Relevant to credibility / bias of witness"
- "Relevant to [specific theory of defense]"

**Best Evidence Objection → Responses:**
- "Original exhibit provided; not a duplicate"
- "Certified copy under La. C.E. Art. 1002 — acceptable substitute"
- "Oral testimony of contents permissible under [exception]"
- "Witness will authenticate original before exhibit is offered"


**Unfair Prejudice Objection (Art. 403) → Responses:**
- "Probative value substantially outweighs unfair prejudice; essential to [theory]"
- "Court can give limiting instruction to mitigate prejudice"
- "[Gruesome photo / weapon] is necessary to establish [specific element]; no less prejudicial alternative"
- "Prejudicial impact is to elements we must prove; not improper character evidence"

**Confrontation Clause Objection (Crawford) → Responses:**
- "Witness will testify live; defendant has opportunity to cross-examine"
- "Not testimonial in nature; offered for [non-testimonial purpose]"
- "Business record exception satisfies Confrontation; not 'accusatory' statement"
- "Prior Davidison v. Prince / State v. [case] objection — [specific response to precedent]"

**Expert Methodology Objection (Art. 702 / Daubert-Foret) → Responses:**
- "Expert will testify regarding methodology, peer review, acceptance in field"
- "Methodology reliable under Foret standard; [specific reliability factors]"
- "Court previously admitted similar expert testimony in [prior case]"
- "Foundation for expert opinion will be established through direct examination"

---

## ERROR PRESERVATION FOR APPEAL

Every excluded exhibit and every sustained objection must be flagged to **dw-appellate-error-monitor** with:

1. **Exhibit / Statement:** D-1, S-5, or narrative description
2. **Objection Basis:** Exact basis (hearsay, authentication, relevance, etc.)
3. **Ruling:** Sustained / Overruled / Excluded / Admitted
4. **Judge's Language:** Exact ruling language if available
5. **Trial Date:** Date of trial
6. **Judge Name:** Judge who ruled
7. **Preservation:** How was error preserved at trial (objection made, offer of proof, cross-examination)
8. **Significance:** Why this error is appellable (State's key evidence excluded affecting guilt; Defense exculpatory evidence excluded)

**Automatic Feed:** Every sustained objection to Defense exhibit or every State exhibit admitted over Defense objection should trigger dw-appellate-error-monitor entry.

---

## TEMPLATE INTEGRATION

Use dw-template-selector to access:
- Exhibit card template (for Step 2)
- Objection log template (for Step 5)
- Authentication checklist template (for output 6D)
- Clerk's exhibit list template (for output 6B)


---

## RELATED SKILLS (DO NOT USE FOR)

This skill handles exhibit management ONLY. Do NOT use for:

- **Trial notebook assembly:** Use **dw-trial-notebook-builder**
  - Assembles complete trial notebook (all sections, exhibits, jury instructions, etc.)
  - dw-exhibit-manager feeds INTO it

- **Evidence chain of custody auditing:** Use **dw-chain-of-custody-auditor**
  - Audits evidence handling from initial collection through trial
  - Identifies custody gaps and break-in-chain issues pre-trial
  - dw-exhibit-manager reads from it

- **Cross-examination planning:** Use **dw-cross-exam-architect**
  - Designs witness examination outlines and cross-examination strategies
  - Identifies impeachment opportunities for authenticating witnesses
  - dw-exhibit-manager reads from it

- **404(b) opposition strategy:** Use **dw-404b-opposition**
  - Develops objections to other crimes evidence
  - dw-exhibit-manager flags 404(b) exhibits to it

- **Appellate error preservation:** Use **dw-appellate-error-monitor**
  - Tracks all trial errors (evidentiary, instructional, procedural)
  - dw-exhibit-manager FEEDS sustained objections INTO it

- **Discovery compliance:** Use **dw-discovery-compliance-monitor**
  - Tracks discovery obligations, production status, sanctions risk
  - dw-exhibit-manager reads authentication/custody issues from it

---

## QUICK START

1. **Invoke dw-case-brain** → Get case context, trial date, judge
2. **Check dw-trial-notebook-builder** → Import existing exhibit list if available
3. **Scan case folder** → Identify all potential exhibits (STEP 1)
4. **Pre-mark exhibits** → Assign numbers, create exhibit cards (STEP 2)
5. **Document authentication** → For each exhibit, note foundation & witness (STEP 3)
6. **Prepare for trial** → Generate Master Exhibit List, Authentication Checklist (STEP 6)
7. **At trial** → Update status in real-time as exhibits are offered (STEP 4)
8. **Log objections** → Record all objections and rulings (STEP 5)
9. **Feed to appellate monitor** → Automatic flag for every sustained objection
10. **File clerk list** → Submit Clerk's Exhibit List post-trial if required

---

## QUESTIONS TO ASK ATTORNEY

Before beginning:
1. What is the trial date? Court? Judge?
2. Does Judge [name] have exhibit marking preferences (D-1 vs. "Defense Exhibit 1")?
3. Are we pre-marking exhibits before trial, tracking live at trial, or both?
4. Does the State have an exhibit list to track?
5. Do we anticipate any Art. 404(b) exhibits?
6. Any exhibits with known authentication problems (custody gaps, foundational issues)?
7. Any demonstrative exhibits (timelines, diagrams) planned?
8. Should we object to any State exhibits pre-trial, or prepare for live objections?
9. Is there an existing trial notebook exhibit list to import?
10. Will the clerk require a filed Clerk's Exhibit List post-trial?
