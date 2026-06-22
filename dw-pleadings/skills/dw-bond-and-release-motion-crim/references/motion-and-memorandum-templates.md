# Motion and Memorandum Templates

This reference covers the two primary deliverables: the short-form Motion (.docx #1) and the substantive Memorandum in Support (.docx #2).

## Motion Template (.docx #1) — Short-form (2-3 pages)

Generate a short-form Motion using the `docx` skill conventions.

**Structure:**

```
[CAPTION — per shared protocols]

MOTION FOR REDUCTION OF BOND
[or appropriate motion type from the Motion Type Selection table]

NOW INTO COURT, through undersigned counsel, comes defendant [CLIENT NAME],
who respectfully moves this Honorable Court to [reduce bond / set bond /
grant personal recognizance bond / modify conditions of release] and in
support thereof states the following:

I.    INTRODUCTION
      [2-3 sentences: who the client is, what the current bond situation is,
       why it should change]

II.   CURRENT BOND STATUS
      [Current charges, current bond amount and type, date set, conditions]

III.  FACTUAL BASIS FOR RELIEF
      [Defendant's ties to community, employment, family, compliance history,
       inability to make current bond, impact of continued detention]

IV.   LEGAL BASIS
      [La. C.Cr.P. Art. 316, 334; La. Const. Art. I, § 18; reference to
       attached Memorandum for full argument]

V.    PROPOSED CONDITIONS
      [Alternative conditions the defense offers: GPS monitoring, curfew,
       check-ins, no-contact orders, surrender of passport, etc.]

VI.   PRAYER FOR RELIEF
      WHEREFORE, defendant [CLIENT NAME] respectfully prays that this
      Honorable Court:
      (1) Reduce bond from [current amount] to [proposed amount]; OR
      (2) Release defendant on personal recognizance bond with conditions;
      (3) Conduct a formal bail hearing pursuant to La. C.Cr.P. Art. 316(B);
      (4) Grant such other relief as the Court deems just and proper.

[CERTIFICATE OF SERVICE — per shared protocols]
[SIGNATURE BLOCK — per shared protocols]
```

Filed pleadings get caption, signature, certificate of service, and (when applicable) notice of hearing and proposed order per `dw-shared-protocols-crim`. Do not apply attorney-work-product marking to filed pleadings.

---

## Memorandum in Support Template (.docx #2) — Substantive (5-15 pages)

Generate a substantive Memorandum with full legal argument.

**Structure:**

```
[CAPTION — per shared protocols]

MEMORANDUM IN SUPPORT OF MOTION FOR REDUCTION OF BOND

I.    INTRODUCTION
      [Frame the constitutional issue — bail is about ensuring appearance,
       not punishing the presumptively innocent]

II.   STATEMENT OF FACTS
      [Detailed factual narrative: charges, client background, community ties,
       employment, family, financial situation, impact of detention.
       Cite arrest report and discovery by Bate stamp where available.]

III.  LEGAL STANDARD
      A. Louisiana Bail Provisions (La. C.Cr.P. Art. 311-342)
      B. Constitutional Protections (La. Const. Art. I, § 18; U.S. Const. 8th Amend.)
      C. Factors for Fixing Bail (La. C.Cr.P. Art. 316)

IV.   ARGUMENT
      [Apply Art. 316 factors to the specific facts. Each factor gets its own
       subsection. Lead with the strongest factors.]

      A. The Defendant's Ties to the Community Ensure Appearance
      B. The Defendant Poses No Danger to the Community [if applicable]
      C. The Current Bond Amount Is Excessive Under the Circumstances
      D. Continued Detention Causes Irreparable Harm
      E. Proposed Conditions of Release Adequately Protect the Community
      [Add additional subsections as warranted by the facts]

V.    CONCLUSION
      [Summarize and reiterate relief requested]

[CERTIFICATE OF SERVICE — per shared protocols]
[SIGNATURE BLOCK — per shared protocols]
```

---

## Citation Research (Layered Approach)

**Layer 1 — Training knowledge:** Core Louisiana bail law. See the Quick Reference table in the main SKILL.md.

**Layer 2 — DEVONthink:** Search for citations used in prior firm bond filings:
```
devonthink:search
query: "Art. 316" OR "Art. 341" OR "excessive bail" OR "Stack v. Boyle"
databaseName: Law Library-Criminal
limit: 15
```

Also search the Reference Materials group for the LA Criminal Trial Practice Formulary (bond/bail chapters):
```
devonthink:search
query: "bail" OR "bond"
databaseName: Law Library-Criminal
groupPath: /Reference Materials/LA Criminal Trial Practice Formulary
limit: 10
```

And search for seminar materials on pretrial release:
```
devonthink:search
query: "pretrial release" OR "pretrial detention" OR "bail reform"
databaseName: Law Library-Criminal
limit: 10
```

**Layer 3 — Case law database:** Search for case law in the Case Law group:
```
devonthink:search
query: "bond" OR "bail" OR "pretrial release"
databaseName: Law Library-Criminal
groupPath: /Case Law
limit: 10
```

After assembling citations, flag any that may need currency verification:
`[RESEARCH — confirm this case has not been overruled or modified]`

---

## .docx Generation

Read the `docx` skill (SKILL.md) for document creation instructions. Use `docx-js` to generate both files.

**Formatting requirements:**
- US Letter (8.5" x 11"), 1-inch margins
- Font: Times New Roman, 12pt body text, 14pt headings
- Double-spaced body text (court filing)
- Left-aligned text
- Page numbers centered in footer
- Caption on first page of each document

**File naming:**
- Motion: `Motion for Bond Reduction - [Client Last Name] - [Date].docx`
- Memorandum: `Memorandum in Support - Bond - [Client Last Name] - [Date].docx`
- ROR Motion: `Motion for Release on Personal Recognizance - [Client Last Name] - [Date].docx`
- Art. 701 Motion: `Motion for Release Under Art. 701 - [Client Last Name] - [Date].docx`
- Bail Revocation Opposition: `Opposition to Bail Revocation - [Client Last Name] - [Date].docx`
