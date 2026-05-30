---
name: dw-exhibit-manager-crim
category: trial-prep
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
**Daniels & Washington | Criminal Defense | Louisiana / 5th Circuit Default**

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

Scan the case folder for all potential exhibits and classify by type — documentary, visual, digital, expert, defense investigation, and demonstrative (non-admitted). Cross-reference with **dw-discovery-compliance-monitor** for authentication issues, chain of custody gaps, or Brady/Giglio concerns.

**Reference:** Read `references/step-1-exhibit-inventory-categories.md` for the full per-type item lists (documentary, visual, digital, expert, defense investigation, demonstratives).


### STEP 2 — PRE-MARK EXHIBITS

Assign exhibit numbers following court convention — Defense (D-1, D-2…), State (S-1, S-2…), Joint (J-1, J-2…) — and create an Exhibit Card for each. The card captures every field needed to track the exhibit from pre-marking through trial-day ruling: description, type, source, Bates number, authentication method, authenticating witness, foundation elements, anticipated objections, prepared responses, offering context, status, and the separated pre-trial vs. trial status fields (never overwrite the pre-trial plan).

**Reference:** Read `references/step-2-exhibit-card-schema.md` for the full Exhibit Card field table and numbering conventions.


### STEP 3 — AUTHENTICATION CHAIN TRACKING

For each exhibit requiring testimonial authentication, list foundation questions, identify the authenticating witness, note hearsay exceptions (La. C.E. Art. 803, 804), flag Art. 901 issues, and cross-reference with **dw-cross-exam-architect** for impeachment vulnerabilities of the authenticating witness. For self-authenticating exhibits, apply La. C.E. Art. 902 (certified public records, official publications, business records with proper certification) — but remember even self-authenticating exhibits remain subject to relevance and hearsay objections.

**Reference:** Read `references/step-3-authentication-chain.md` for the full foundation-question framework, the hearsay-exception checklist, and the Art. 901/902 self-authentication categories.


### STEP 4 — LIVE TRIAL TRACKING

During trial, update exhibit status in real-time as the attorney reports offers and rulings. Use exact timestamped language for each event: Offered, Objection Lodged (basis + objecting party + attorney name), Ruling Made (Sustained/Overruled with judge's exact language), Limiting Instruction (record verbatim for appellate purposes), Withdrawn (with reason if disclosed). Every excluded exhibit (Sustained ruling) AUTOMATICALLY flags to **dw-appellate-error-monitor**.

**Reference:** Read `references/step-4-live-trial-tracking.md` for the full status-update language templates and the automatic appellate flag format.


### STEP 5 — OBJECTION LOG

Maintain a running objection log for ALL evidentiary objections encountered at trial — not just exhibit objections. The log captures # / Exhibit / Party Offering / Objecting Party / Basis / Court's Ruling / Limiting Instruction / Appeal Flag. Every sustained objection to a defense exhibit (or State exhibit admitted over defense objection) automatically feeds **dw-appellate-error-monitor** with full ruling context.

**Reference:** Read `references/step-5-objection-log.md` for the objection log table template, the catalog of common Louisiana evidentiary objections (Art. 802 hearsay, 401/402 relevance, 403 unfair prejudice, 901 authentication, 1002 best evidence, Crawford Confrontation, 505-514 privilege, 404/405 character, 404(b) other crimes, 702/Daubert-Foret expert methodology), and the appellate-feed schema.


### STEP 6 — OUTPUTS

All outputs saved to: `{{CASE_ROOT}}/01 - Trial Notebook/04 - Exhibit List/`

Four deliverables:
- **6A. Master Exhibit List (.xlsx)** — full exhibit tracker with separate sheets for Defense / State / Joint / Excluded
- **6B. Clerk's Exhibit List (.docx)** — formatted document for filing with clerk of court (post-trial)
- **6C. Objection Log (.xlsx)** — complete record of all evidentiary objections with appeal-flag filter for dw-appellate-error-monitor
- **6D. Authentication Checklist (.docx)** — per-exhibit authentication script for attorney use at counsel table

**Reference:** Read `references/step-6-output-specifications.md` for the full file-naming conventions, column lists for each spreadsheet, and the per-exhibit Authentication Checklist format block.


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

This skill addresses ten recurring exhibit categories that demand specialized handling:

- **Demonstrative Exhibits (Non-Admitted)** — track separately; aid jury but never admitted into evidence
- **Art. 404(b) Other Crimes Evidence** — flag and route to dw-404b-opposition; prepare for bifurcated ruling
- **State's Exhibits (Adverse Evidence)** — same pre-trial rigor; prepare objections in advance
- **Confrontation Clause Issues (Crawford)** — testimonial hearsay analysis; lab reports without analyst (Davidison v. Prince [VERIFY CITATION])
- **Prior Statements (Impeachment vs. Substantive)** — La. C.E. Art. 607, 613 distinction
- **Expert Reports & CVs** — Daubert/Foret reliability; cross-reference dw-expert-witness-evaluator
- **Audio/Video Evidence** — BWC, dash cam, surveillance; cross-reference dw-video-evidence-auditor
- **Digital Evidence (Phone Dumps, Social Media, Metadata)** — extraction methodology; cross-reference dw-forensic-dump-analyzer and dw-social-media-auditor
- **Business Records (La. C.E. Art. 803(6))** — custodian certification vs. live testimony
- **Physical Evidence** — chain of custody scrutiny; cross-reference dw-chain-of-custody-auditor

**Reference:** Read `references/special-situations.md` for the full handling protocol for each category (foundation elements, anticipated objections, cross-references).


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

Exhibit marking conventions vary by judge. Some prefer shorthand (D-1, D-2), some prefer spelled-out ("Defense Exhibit 1"); some courts use civil-style Plaintiff/Defense even in criminal. Other preferences vary on pre-trial submission, joint exhibit lists, marking timing, binder organization, and Bates numbering. **Always ask attorney or check local rules / prior cases before this judge.**

**Reference:** Read `references/judge-preferences.md` for the full preference catalog and pre-flight checklist.

---

## COMMON OBJECTION RESPONSES (LOUISIANA EVIDENTIARY RULES)

Quick-deployment bank of prepared responses to the seven most common objections at trial: Hearsay, Authentication, Relevance, Best Evidence, Unfair Prejudice (Art. 403), Confrontation Clause (Crawford), and Expert Methodology (Art. 702 / Daubert-Foret). Each objection has 3-6 templated response patterns ready to be tailored to the specific exhibit and witness.

**Reference:** Read `references/objection-responses-bank.md` for the full prepared-response bank organized by objection type.

---

## ERROR PRESERVATION FOR APPEAL

Every excluded exhibit and every sustained objection must be flagged to **dw-appellate-error-monitor** with the eight-field appellate package (Exhibit/Statement, Objection Basis, Ruling, Judge's Language, Trial Date, Judge Name, Preservation Method, Significance). Every sustained objection to Defense exhibit OR every State exhibit admitted over Defense objection automatically triggers a dw-appellate-error-monitor entry.

**Reference:** Read `references/appellate-error-preservation.md` for the full eight-field appellate-feed schema.

---

## TEMPLATE INTEGRATION

Use the template selection protocol in dw-shared-protocols/references/template-selection-protocol.md to access:
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

---

## Quick References

The references directory contains the detailed exhibit-management content offloaded from this orchestration scaffold. Load each file when you reach the corresponding step or section:

| File | Purpose | Loaded At |
|------|---------|-----------|
| `references/step-1-exhibit-inventory-categories.md` | Per-type exhibit item lists (documentary, visual, digital, expert, defense investigation, demonstratives) | Step 1 |
| `references/step-2-exhibit-card-schema.md` | Exhibit Card field table + Defense/State/Joint numbering conventions | Step 2 |
| `references/step-3-authentication-chain.md` | Foundation-question framework, hearsay exceptions (Art. 803/804), Art. 901/902 self-authentication | Step 3 |
| `references/step-4-live-trial-tracking.md` | Real-time status-update language templates (Offered / Objection / Ruling / Limiting / Withdrawn) + automatic appellate flag | Step 4 |
| `references/step-5-objection-log.md` | Objection log table template + Louisiana evidentiary objection catalog + appellate feed schema | Step 5 |
| `references/step-6-output-specifications.md` | Master Exhibit List, Clerk's Exhibit List, Objection Log, Authentication Checklist — file naming, columns, format blocks | Step 6 |
| `references/special-situations.md` | Demonstratives, 404(b), State exhibits, Crawford, prior statements, expert reports, A/V, digital, business records, physical evidence | Special Situations |
| `references/judge-preferences.md` | Judge marking-preference catalog and pre-flight checklist | Judge-Specific Preferences |
| `references/objection-responses-bank.md` | Prepared-response bank for Hearsay, Authentication, Relevance, Best Evidence, Unfair Prejudice, Confrontation, Expert Methodology | Common Objection Responses |
| `references/appellate-error-preservation.md` | Eight-field appellate-feed schema for dw-appellate-error-monitor | Error Preservation for Appeal |
