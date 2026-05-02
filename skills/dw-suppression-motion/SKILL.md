---
name: dw-suppression-motion
category: pleadings
description: >
  Draft suppression motions AND audit search warrants. ALWAYS invoke for "suppress," "motion
  to suppress," "illegal search," "bad warrant," "audit the warrant," "probable cause,"
  "Franks," or "fruit of the poisonous tree." Covers 4th and 5th Amendment issues. Read
  ../dw-shared-protocols/references/template-selection-protocol.md before drafting.
---

# Daniels & Washington — Suppression Motion & Warrant Auditor
**Version 2.0 | Internal Use Only**

This skill has two modes:

1. **Audit Mode** — Produces a comprehensive Search Warrant Constitutional Audit Report (.docx) analyzing probable cause, particularity, Franks viability, execution compliance, and Leon preemption. Use when the attorney wants to evaluate a warrant before deciding whether to file a motion.

2. **Motion Mode** — Generates complete, ready-to-edit suppression motions as two separate Word documents: a short-form **Motion to Suppress** and a detailed **Memorandum in Support**. For Search & Seizure (warrant-based) suppression, the warrant audit runs first and feeds directly into the motion.

Both modes read discovery files to extract facts, search firm databases for templates and prior authority, and apply Louisiana law throughout.

**Mode Selection:** If the attorney says "audit the warrant," "review the affidavit," "look at this warrant," or "anything wrong with this search" → start in **Audit Mode**. If the attorney says "suppress," "motion to suppress," "file a motion" → start in **Motion Mode**. After an audit, always offer: *"Want me to draft the suppression motion based on these findings?"*

**Cowork drafts; attorney approves.** Every output is a draft for attorney review. The attorney verifies facts, confirms legal arguments, signs, and files.

---

## STEP 0 -- FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any search warrants, affidavits, arrest reports, body-worn camera footage, interrogation recordings, statements, or other discovery, do not analyze anything yet.**

Your only response must be:
> *"Before I begin -- are you uploading any additional search warrants, affidavits, returns on warrants, arrest reports, BWC footage, interrogation recordings, Miranda waiver forms, witness statements, or other case documents? I'll start the audit/motion only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** Mid-analysis discovery of an additional warrant, a body camera recording of the search execution, or an interrogation recording would require complete re-evaluation of probable cause, particularity, execution compliance, Franks viability, and any companion 5th/6th Amendment suppression theory.

---

### Source Citation Mandate

Every factual assertion in the Warrant Audit Report, Motion to Suppress, and Memorandum in Support must trace back to a specific source document. Suppression hearings are fact-intensive — the court evaluates probable cause, warrant particularity, and execution compliance based on the documented record. Unsourced claims about what officers did or didn't do carry no weight.

**Citation format:** Cite the document title, page number, and paragraph or timestamp. Examples:
- `(Search Warrant Affidavit, p. 2, para. 4)`
- `(Search Warrant — 14th JDC, signed 03/15/2026, Scope paragraph)`
- `(Return on Search Warrant, p. 1, Items Seized)`
- `(Officer Smith BWC — Warrant Execution, Timestamp 00:05:32)`
- `(Arrest Report — LCPD Case #2026-00456, p. 3, para. 2)`
- `(Inventory Receipt, Items #1-14)`
- `(Discovery Production, Bates #00145-00148)`

**Multiple-source rule:** When more than one document confirms a fact about the search, cite all of them — e.g., `(Warrant Affidavit, p. 2, para. 4; Officer Smith BWC, Timestamp 00:05:32)`.

**Unsourced assertions:** If a factual claim cannot be tied to a specific document, mark it `[UNSOURCED — VERIFY WITH CLIENT/DISCOVERY]` so the attorney knows to confirm or remove it before filing.

**Where sourcing applies:** All factual content — probable cause analysis, warrant scope review, execution compliance, Franks material, and fruit of the poisonous tree analysis. Legal standards and case law follow normal legal citation format.

---

## Suppression Categories

This skill handles four categories of suppression, each with distinct constitutional foundations and analytical frameworks. Many cases involve overlapping categories (e.g., an illegal traffic stop that leads to both a warrantless search and a custodial statement). When multiple categories apply, generate a single combined motion covering all grounds — the court prefers consolidated filings over piecemeal motions.

| Category | Constitutional Basis | What Gets Suppressed |
|----------|---------------------|---------------------|
| **Search & Seizure** | 4th Amendment; La. Const. Art. I, § 5 | Physical evidence, contraband, weapons, digital data |
| **Statements** | 5th Amendment; La. Const. Art. I, § 13 | Confessions, admissions, custodial statements |
| **Identification** | 14th Amendment Due Process; La. Const. Art. I, § 2 | Lineup IDs, showup IDs, photo array IDs, in-court IDs |
| **Fruit of the Poisonous Tree** | *Wong Sun v. United States* | All evidence derived from the initial constitutional violation |

---

## Workflow

### STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any pleading, read `dw-shared-protocols/SKILL.md` and load:

1. `dw-shared-protocols/references/filed-pleading-boilerplate.md` — orchestrator for caption, signature, COS, notice, proposed order, citation style, and filing conventions
2. `dw-shared-protocols/references/output-path-formula.md` — output path anchored on `CASE_ROOT`

Filed pleadings receive NO work product marking. Follow the boilerplate component sequence in order. Output to the appropriate `01 - Trial Notebook/` motion subfolder per the formula. The Warrant Audit Report (Audit Mode only) is internal work product — mark it per `attorney-work-product-marking.md` as noted in the Warrant Deep-Dive section.

### STEP 0.6 — Constitutional Red Flag Scan

Before proceeding to template selection and motion drafting, conduct a rapid constitutional triage of the case file. This scan identifies whether suppression motions are warranted and which grounds to prioritize.

**Scan the discovery for these red flag categories:**

1. **4th Amendment — Search & Seizure Issues:**
   - Warrantless searches or seizures
   - Warrant defects (stale probable cause, overbroad scope, wrong address)
   - Consent issues (voluntariness, scope exceeded, authority to consent)
   - Traffic stop pretextuality or prolonged detention
   - Cell phone/digital device searches without warrant

2. **5th Amendment — Self-Incrimination Issues:**
   - Miranda warnings absent, late, or defective
   - Interrogation continued after invocation of rights
   - Statements obtained during impermissible delay (La. C.Cr.P. Art. 230.1)
   - Coerced or involuntary confessions
   - Use of silence as evidence

3. **6th Amendment — Right to Counsel Issues:**
   - Interrogation after formal charges without counsel
   - Denial of attorney access during custodial questioning
   - Use of jailhouse informants post-indictment

**For each red flag identified:**
- Cite the specific source document (document title, page, paragraph/timestamp)
- Classify urgency: IMMEDIATE (file now) / STRATEGIC (file before trial) / MONITORING (preserve for record)
- Note the specific suppression ground and applicable Louisiana/federal authority

**Output:** Red Flag Scan Summary — a ranked list of suppression grounds by strength and urgency. This summary determines which suppression categories (Search & Seizure, Statements, Identification, Fruit) to activate for full motion drafting.

If no constitutional red flags are identified, document the clean scan result and note for the file. The absence of red flags may itself be strategically significant (e.g., the State's case relies on properly obtained evidence, shifting defense focus to factual disputes rather than suppression).

### Step 1: Template-First Search

Before drafting anything, search DEVONthink for firm templates and prior suppression filings. This is not optional — it's the firm's Template-First Drafting Rule.

**DEVONthink searches to run:**
```
"motion suppress" OR "suppression motion"
"memorandum support suppress"
"suppress statement" OR "suppress identification" OR "suppress search"
```

Also search with tags: `template`, `suppression`, `motion`

**After searches complete**, read and follow the Template Selection Protocol at `/mnt/skills/user/dw-template-selector/SKILL.md` (Steps A through D). Present the top 3 results, let the attorney select a template or paste a DEVONthink link, and load the selection before proceeding. Do not proceed to Step 2 until the attorney has selected a template or chosen to draft from scratch.

If a template is selected, preserve the firm's preferred formatting, language, and legal positions — then update with case-specific facts and authority. If drafting from scratch, use this skill's built-in structure and offer to save the final approved version as a new template.

**TextExpander snippets to apply:**
- `;miranda` — Miranda citation block (for statement suppression)
- `;draft` — Cowork draft disclaimer

### Step 2: Gather Case Context

**From the attorney prompt:** Parse whatever the attorney provides — client name, docket number, the factual scenario, which evidence they want suppressed.

**From discovery files (when available):** Read uploaded PDFs and extract facts relevant to the suppression argument. Look for:

- **Police reports / incident reports** — who did what, when, where. Identify the initial encounter, the basis (or lack thereof) for the stop/search/arrest, and what was found.
- **Body cam / interview transcripts** — exact words spoken, timing of Miranda warnings (or absence), whether the defendant invoked rights, tone and demeanor suggesting coercion.
- **Search warrants & affidavits** — scope of warrant vs. what was actually searched, staleness of information, reliability of informant, whether warrant was obtained before or after the search.
- **Forensic extraction reports** — for digital evidence: what tool was used (Cellebrite, GrayKey), scope of extraction vs. scope of consent or warrant, whether device was searched incident to arrest.
- **Identification procedure records** — lineup instructions given to witness, filler selection, administrator blindness, time elapsed since offense, witness confidence statements.

**From case analysis (when available):** Check for:
- Phase 2 Constitutional Issues Scan (4th/5th/6th Amendment flags already identified)
- Forensic Audit report (mobile device extraction issues)
- Report 3 (Immediate Red Flags)
- Any Cowork Analysis flagging suppression-worthy issues

### Step 3: Classify the Suppression Type

Based on the facts gathered, identify which suppression categories apply. Think through each one:

**Search & Seizure — ask yourself:**
- Was there a warrant? If yes, was it valid (probable cause, particularity, staleness, scope)?
- If no warrant, does an exception apply? The State bears the burden of proving the exception.
  - Consent (voluntary? scope exceeded? authority to consent?)
  - Search incident to arrest (lawful arrest? scope? timing? *Riley* for cell phones)
  - Exigent circumstances (destruction of evidence? hot pursuit? emergency?)
  - Plain view (lawfully present? immediately apparent? inadvertent?)
  - Automobile exception (probable cause? scope limited to evidence sought?)
  - Terry stop/frisk (reasonable suspicion? articulable facts? scope of frisk?)
  - Inventory search (standardized procedures followed?)
- Louisiana provides broader protections than the federal 4th Amendment in some contexts — always check Art. I, § 5.


### WARRANT DEEP-DIVE (Search & Seizure — Audit Mode or Motion Mode)

When a search warrant is uploaded or referenced, automatically run this comprehensive warrant audit. In Audit Mode, produce the Warrant Audit Report. In Motion Mode, use the findings to build the Search & Seizure section of the suppression motion.

#### Four Corners Probable Cause Audit

The affidavit must establish probable cause **within its four corners** — information known to the judge at signing.

**Conclusory Language Scan** — Classify every factual assertion:
- **Factual:** Specific, verifiable facts with source attribution
- **Conclusory:** Bare assertions without supporting facts (e.g., "Based on my training and experience, the residence is used for drug trafficking")
- **Boilerplate:** Generic law enforcement language recycled across warrants
- **Hearsay (attributed):** Secondhand info with source identified and reliability established
- **Hearsay (unattributed):** Secondhand info without adequate source reliability

Flag every conclusory and boilerplate statement — these are the weak joints. An affidavit built primarily on conclusions fails probable cause under *Illinois v. Gates*, 462 U.S. 213 (1983).

**Nexus Analysis** — Probable cause requires nexus between three elements:
1. **Crime** — evidence that a crime has been or is being committed
2. **Evidence** — specific items that constitute evidence of that crime
3. **Location** — reason to believe the evidence is at the place to be searched

The most common deficiency is a weak nexus to **location**. When the affidavit uses "training and experience" to bridge the gap, flag as conclusory nexus.

**Informant Reliability (Aguilar-Spinelli / Gates)** — If affidavit relies on CI/anonymous tip:
- Basis of Knowledge: How does the CI know? Personal observation? Secondhand?
- Reliability / Track Record: Prior accurate information? How many times?
- Corroboration: What independent police work corroborated the CI's claims?
- Staleness of CI Contact: When did the CI last observe the activity?

**Staleness Analysis** — Flag as stale when:
- Single drug transaction > 2 weeks before warrant with no intervening surveillance
- Property crime evidence > 30 days old with no evidence of continued possession
- Digital evidence references > 60-90 days old
- Affidavit's most recent factual allegation is substantially older than the warrant date

#### Particularity & Scope Audit

- **Place:** Specific, identifiable location? Multi-unit buildings — unit specified? Vehicles — identified by make/model/plate/VIN? Digital devices — specific devices or "any and all"?
- **Things to Be Seized:** Specific categories tied to the crime? Or catch-all language ("any and all evidence," "any contraband")? Flag overbreadth per *Groh v. Ramirez*, 540 U.S. 551.
- **Scope of Execution vs. Authorization:** Compare warrant scope against what actually happened. Officers search beyond authorized areas? Seize items not described? Digital examination exceed temporal/subject-matter scope?

#### Franks v. Delaware Analysis

Under *Franks v. Delaware*, 438 U.S. 154 (1978):

**Prong 1:** Affiant made false statement or omitted material facts **deliberately or with reckless disregard for truth**.
**Prong 2:** If false statement excised (or omission added), remaining content insufficient for probable cause.

**What to look for:**
- Dates/times/locations not matching police reports or other discovery
- Affiant's observations contradicted by body cam, radio logs, or other officers
- Overstated CI reliability
- Mischaracterized lab results or criminal history
- Material omissions: CI criminal history, exculpatory surveillance, failed corroboration attempts, other suspects, changed tenants

Cross-reference every factual claim against all discovery. Flag: `[FRANKS CANDIDATE — [description]]`

#### Execution Audit

- **Knock-and-Announce:** Did officers comply? Wait time? (*Wilson v. Arkansas*; *United States v. Banks* — 15-20 seconds minimum). No-knock authorization: specific articulable facts or boilerplate?
- **Timing:** Night warrant authorized per La. C.Cr.P. Art. 163? Executed within 10-day window?
- **Force:** Proportionate? Occupants detained — how long? Non-targets (children, elderly) present?
- **Return & Inventory:** Complete inventory prepared? Filed with court? Matches evidence room? Items in evidence not on inventory (or vice versa)?

#### Good Faith Exception (Leon) Preemption

For each deficiency, assess whether *Leon*, 468 U.S. 897 (1984) saves the warrant. Leon does NOT apply when:
1. Magistrate was misled by affiant's false statements (Franks)
2. Magistrate wholly abandoned judicial role (rubber stamp)
3. Affidavit "so lacking in indicia of probable cause" that belief in it was entirely unreasonable — the **bare bones** affidavit
4. Warrant "so facially deficient" that executing officers could not presume it valid

#### Warrant Audit Report Output (Audit Mode Only)

When in Audit Mode, produce a .docx report with:
- Warrant Overview (court, judge, affiant, dates, location, authorized items)
- Section 1: Probable Cause Analysis (four corners, conclusory findings, nexus, informant reliability, staleness) — Rating: SUFFICIENT / DEFICIENT / BARE BONES
- Section 2: Particularity & Scope — Rating: ADEQUATE / DEFICIENT / FACIALLY INVALID
- Section 3: Franks Analysis — Viability: STRONG / ARGUABLE / WEAK / N/A
- Section 4: Execution Audit — Rating: COMPLIANT / DEFICIENT / CRITICAL VIOLATIONS
- Section 5: Leon Preemption — Survivability: LIKELY / ARGUABLE / UNLIKELY
- Section 6: Suppression Roadmap (constitutional basis, factual support, applicable law for each deficiency)
- Section 7: Cross-Examination Ammunition (for affiant and executing officers)
- Section 8: Defense Action Items (motions, Franks hearing request, missing discovery, expert needs)
- Section 9: Discovery Gap Report

File naming: `[3-digit prefix] - Search Warrant Audit - [Client Last Name].docx`
Location: `02 - Pretrial Notebook/03 - Case Analysis & Notes`
Mark: per `attorney-work-product-marking.md` in shared protocols (internal deliverable)

After producing the audit report, offer: *"This warrant has [X] deficiencies. Want me to draft the suppression motion based on these findings?"*

**Statements — ask yourself:**
- Was the defendant in custody? (Would a reasonable person feel free to leave?)
- Was the defendant interrogated? (Questions or functional equivalent designed to elicit incriminating response?)
- Were Miranda warnings given? (Complete? Before questioning began?)
- Did the defendant invoke their rights? (Unambiguous invocation? Did questioning stop?)
- Was the waiver knowing, intelligent, and voluntary? (Totality of circumstances: age, education, mental state, intoxication, duration, coercion, deception)
- Was there a *Bruton* issue with co-defendant statements?

**Identification — ask yourself:**
- Was the procedure unnecessarily suggestive? (Single photo showup? Biased lineup? Administrator knowledge? Instructions to witness?)
- Under the totality of circumstances, was the ID reliable despite any suggestiveness? (*Manson v. Brathwaite* factors: opportunity to view, degree of attention, accuracy of description, certainty, time between crime and confrontation)
- Louisiana's eyewitness identification reform act (La. C.Cr.P. Art. 253) — were the statutory requirements followed?

**Fruit of the Poisonous Tree — ask yourself:**
- If any primary evidence should be suppressed, what was derived from it?
- Does an exception apply? (Independent source? Inevitable discovery? Attenuation of the taint?)

### Step 4: Draft the Motion to Suppress (.docx #1)

The Motion to Suppress is a short, formal filing — typically 2-3 pages. It tells the court what the defense is asking for and why, without the full legal argument (that goes in the Memorandum).

**Structure:**

```
[CAPTION — per shared protocols]

MOTION TO SUPPRESS [EVIDENCE / STATEMENT / IDENTIFICATION]

NOW INTO COURT, through undersigned counsel, comes defendant [CLIENT NAME],
who respectfully moves this Honorable Court to suppress [specific description
of evidence to be suppressed] and to grant a hearing on this motion, and in
support thereof states the following:

I.    INTRODUCTION
      [2-3 sentences: what happened, what constitutional right was violated,
       what evidence should be excluded]

II.   STATEMENT OF FACTS
      [Concise factual narrative. Cite discovery by Bate stamp where available.
       Focus only on facts relevant to the constitutional issue.]

III.  LEGAL BASIS
      [Brief statement of the legal standard. Reference La. C.Cr.P. Art. 703
       and the specific constitutional provision. Note that full argument is
       presented in the attached Memorandum in Support.]

IV.   PRAYER FOR RELIEF
      WHEREFORE, defendant [CLIENT NAME] respectfully prays that this
      Honorable Court:
      (1) Conduct an evidentiary hearing on this motion pursuant to
          La. C.Cr.P. Art. 703(D);
      (2) Suppress [specific evidence] and any fruits thereof;
      (3) Prohibit the State from referencing [suppressed evidence] at trial;
      (4) Grant such other relief as the Court deems just and proper.

[CERTIFICATE OF SERVICE — per shared protocols]
[SIGNATURE BLOCK — per shared protocols]
```

**Key rules for the Motion:**
- Always request a hearing — La. C.Cr.P. Art. 703(D) requires the court to hold an evidentiary hearing when a motion to suppress raises factual issues.
- Be specific about what you want suppressed. "All evidence" is too vague. Name the items.
- The Statement of Facts should be tight and factual, not argumentative. Save the argument for the Memorandum.
- If the motion involves statements, reference whether Miranda warnings were given and cite the specific point in the timeline where the constitutional violation occurred.

### Step 5: Draft the Memorandum in Support (.docx #2)

The Memorandum is the substantive legal brief — typically 8-20 pages depending on complexity. This is where the legal research, case law application, and detailed argument live.

**Structure:**

```
[CAPTION — per shared protocols]

MEMORANDUM IN SUPPORT OF MOTION TO SUPPRESS

I.    INTRODUCTION
      [One paragraph framing the constitutional issue and what's at stake]

II.   STATEMENT OF FACTS
      [Detailed factual narrative with Bate stamp citations. Include relevant
       quotes from transcripts. Build the factual record the court will need
       to rule. Every factual assertion must be sourced.]

III.  LEGAL STANDARD
      [The applicable legal framework. Start with the constitutional provision,
       then the Louisiana statutory authority, then the governing case law.
       See references/suppression-citations.md for the citation library.]

IV.   ARGUMENT
      [Apply the law to the facts. This is the heart of the Memorandum.
       Organize by issue if multiple grounds for suppression exist.
       Each argument section should:
       - State the legal rule
       - Apply it to the specific facts
       - Distinguish or address likely State counterarguments
       - Conclude with why this evidence must be suppressed]

      A. [First Ground for Suppression]
         1. The Legal Rule
         2. Application to the Facts
         3. The State Cannot Meet Its Burden

      B. [Second Ground, if applicable]
         ...

      C. Fruit of the Poisonous Tree
         [If primary evidence is suppressed, all derivative evidence
          must also be excluded. Identify specific derivative evidence.]

V.    CONCLUSION
      [Summarize the constitutional violation and the remedy. Reiterate
       the specific relief requested.]

[CERTIFICATE OF SERVICE — per shared protocols]
[SIGNATURE BLOCK — per shared protocols]
```

**Key rules for the Memorandum:**
- Lead with the strongest argument. Courts read the first argument most carefully.
- Anticipate the State's counterarguments and address them. The prosecutor will argue exceptions — beat them to it.
- Use quotes from transcripts and discovery. Direct quotes from the officer's own report or body cam are powerful because the court can verify them.
- Cite both Louisiana and federal authority. Louisiana's constitution sometimes provides broader protections — always check and argue both grounds.
- For the suppression hearing burden: the State bears the burden of proving the lawfulness of a warrantless search or seizure. For statements, the State must prove voluntariness and Miranda compliance. Make the burden allocation explicit in your argument.
- For identification, the defendant bears the initial burden of showing the procedure was suggestive, then the State must prove reliability.

### Step 6: Citation Research

For citations, use a layered approach:

**Layer 1 — Training knowledge:** Start with well-established suppression precedent. Read `references/suppression-citations.md` for the organized citation library covering all four suppression categories with Louisiana and federal authority.

**Layer 2 — DEVONthink:** Search for citations used in prior firm filings:
```
Search: "[constitutional issue]" in group "06 - Law & Research" OR tags contain "suppression"
```

After assembling citations, flag any that may need currency verification:
`[RESEARCH — confirm this case has not been overruled or modified]`

### Step 7: Generate the .docx Files

Read the `docx` skill (SKILL.md) for document creation instructions. Use `docx-js` to generate both files as .docx.

**Formatting requirements:**
- US Letter (8.5" x 11"), 1-inch margins
- Font: Times New Roman, 12pt body text, 14pt headings
- Double-spaced body text (this is a court filing, not an internal memo)
- Left-aligned text (no full justification — courts prefer left-aligned)
- Page numbers centered in footer
- Caption on first page of each document
- Each document starts on page 1

**File naming:**
- Motion: `Motion to Suppress - [Client Last Name] - [Date].docx`
- Memorandum: `Memorandum in Support - Suppress - [Client Last Name] - [Date].docx`

### Step 8: Attorney Review Flags

Before presenting the output, mark all items that need attorney attention:

- `[VERIFY — confirm this fact with client/discovery]` — any factual assertion not directly sourced from discovery
- `[RESEARCH — confirm current validity of this citation]` — any case law that may have been modified or overruled
- `[ATTORNEY TO COMPLETE]` — signature block details, specific dates, bar number
- `[STRATEGIC DECISION]` — choices about which arguments to include/exclude, whether to request an evidentiary hearing vs. submission on brief

### Step 9: Save and Integrate

**If part of an active case folder:**
- Save both documents to `02 - Pretrial Notebook/01 - Pleadings/`
- Update the LWOP Worksheet's "Motion to Suppress" field (if applicable)
- Create a Clio task: *"Review and File Motion to Suppress — [Client Name]"*
- Cross-reference with the Constitutional Issues Scan if one exists

**If standalone:**
- Save to the current working folder / outputs directory

**Present to the attorney with a summary:**
- Suppression category (which constitutional grounds)
- Key arguments and the facts supporting them
- Legal authorities cited
- Items flagged for verification
- Filing deadline (if known)
- Whether a prior firm template was used as the base

---

## Multi-Category Motions

When a case involves multiple suppression grounds (common in drug cases with a traffic stop leading to a search leading to a phone seizure leading to a custodial statement), consolidate into a single motion and memorandum with clearly separated argument sections.

**Recommended argument organization for multi-category motions:**

1. Start with the earliest constitutional violation in the chronological chain (usually the stop or encounter)
2. Build forward through each subsequent violation
3. End with fruit of the poisonous tree — showing how suppression of the initial violation cascades to suppress everything that followed

This chronological approach is persuasive because it tells a story: one illegal action led to the next, and the entire evidentiary chain is poisoned.

---

## Integration with Other Skills

| Skill | How It Integrates |
|-------|------------------|
| `dw-shared-protocols` | Caption, signature, COS, notice of hearing, proposed order, citation style, filing conventions, output path |
| `dw-template-selector` | Template-First DEVONthink search protocol before drafting |
| `dw-criminal-defense` | Phase 2 Constitutional Issues Scan feeds suppression grounds |
| `dw-mobile-forensic-auditor` | Forensic Audit report provides digital evidence suppression facts |
| `dw-cross-exam-architect` | Warrant audit generates cross-exam seeds for affiant/executing officers |
| `docx` | Document generation — read for .docx creation instructions |
| TextExpander snippets | `;miranda`, `;draft` (skill-specific; caption/sig/cos now via shared protocols) |

### Search Warrant Legal Standards Quick Reference

| Issue | Authority |
|-------|-----------|
| Probable cause (totality of circumstances) | *Illinois v. Gates*, 462 U.S. 213 (1983) |
| Particularity requirement | U.S. Const. Amend. IV; La. Const. Art. I, Sec. 5 |
| Franks hearing (false affidavit) | *Franks v. Delaware*, 438 U.S. 154 (1978) |
| Good faith exception | *United States v. Leon*, 468 U.S. 897 (1984) |
| Bare bones affidavit (no good faith) | *United States v. Satterwhite*, 980 F.2d 317 (5th Cir. 1992) |
| Knock and announce | *Wilson v. Arkansas*, 514 U.S. 927 (1995) |
| Wait time before forced entry | *United States v. Banks*, 540 U.S. 31 (2003) |
| Overbreadth / facial invalidity | *Groh v. Ramirez*, 540 U.S. 551 (2004) |
| Staleness of probable cause | *United States v. Bremner*, 195 F.3d 221 (5th Cir. 1999) |
| Informant reliability | *Illinois v. Gates*; *Aguilar v. Texas*; *Spinelli v. United States* |
| Cell phone search warrant required | *Riley v. California*, 573 U.S. 373 (2014) |
| Digital evidence particularity | *United States v. Ganias*, 824 F.3d 199 (2d Cir. 2016) |
| Nighttime search warrants (LA) | La. C.Cr.P. Art. 163 |
| Warrant execution window (LA) | La. C.Cr.P. Art. 163 (10 days) |
| Return and inventory requirement | La. C.Cr.P. Art. 167 |
| Anticipatory warrants | *United States v. Grubbs*, 547 U.S. 90 (2006) |

---

## Output Location

Use the output path formula from `dw-shared-protocols/references/output-path-formula.md`. Filed motions go to `{{CASE_ROOT}}/02 - Pretrial Notebook/01 - Pleadings/`; warrant audit reports go to `{{CASE_ROOT}}/02 - Pretrial Notebook/03 - Case Analysis & Notes/`. See shared protocols for CASE_ROOT resolution, filename conventions, and post-write reporting format.

---

*This skill reflects Daniels & Washington Suppression Motion & Warrant Auditor Version 2.0 (March 2026). It incorporates the former dw-search-warrant-auditor skill — all warrant auditing is now integrated here. Update whenever suppression case law or firm procedures change.*
