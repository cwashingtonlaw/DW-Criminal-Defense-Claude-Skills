# OUTPUT FORMAT SPECIFICATIONS

## Output 1: Predicate Conviction Audit Table

A comprehensive table documenting the audit results for each predicate:

```
HABITUAL OFFENDER PREDICATE AUDIT — [CLIENT NAME]
Case: State v. [Client], Docket No. [___], [Court/Parish]
Date of Audit: [date]
Habitual Bill Filed: [date] / NOT YET FILED
Enhancement Tier Sought: [Second / Third / Fourth — with or without violence]

| # | Case No. | Charge | CoV? | Conviction Date | Sentence | Completion Date | Sequence | Cleansing | Boykin | Identity | Overall |
|---|----------|--------|------|-----------------|----------|-----------------|----------|-----------|--------|----------|---------|
| 1 | [___]    | [___]  | Y/N  | [date]          | [___]    | [date/UNKNOWN]  | [status] | [status]  | [status]| [status] | [RATING]|
| 2 | [___]    | [___]  | Y/N  | [date]          | [___]    | [date/UNKNOWN]  | [status] | [status]  | [status]| [status] | [RATING]|
| 3 | [___]    | [___]  | Y/N  | [date]          | [___]    | [date/UNKNOWN]  | [status] | [status]  | [status]| [status] | [RATING]|

STATUS KEY:
  PASS       — Element verified; no deficiency identified
  FAIL       — Fatal deficiency identified
  CHALLENGE  — Significant deficiency identified; viable challenge
  UNKNOWN    — Insufficient documentation to assess; additional records needed
  N/A        — Not applicable (e.g., Boykin for trial conviction)

OVERALL ASSESSMENT:
[Summary of audit findings — how many predicates are solid, how many are
challengeable, what is the realistic enhancement tier if challenges succeed,
and the strategic recommendation]
```

## Output 2: Habitual Offender Bill Response / Challenge Motion (.docx)

**This is a FILED PLEADING — apply caption, signature, COS, notice of hearing, and proposed order per shared protocols (`dw-shared-protocols-crim/SKILL.md`). Do NOT apply work product marking.** Save per the shared output path formula (filed motions → `{{CASE_ROOT}}/02 - Pretrial Notebook/01 - Pleadings/`).

Structure:

```
[CAPTION — per shared protocols]

DEFENDANT'S RESPONSE TO HABITUAL OFFENDER BILL OF INFORMATION
AND CHALLENGE TO PREDICATE CONVICTION(S)

NOW INTO COURT, through undersigned counsel, comes defendant [CLIENT NAME],
who responds to the State's Habitual Offender Bill of Information filed on
[date] pursuant to La. R.S. 15:529.1, and challenges the validity of
[specific predicate(s)], and in support thereof states the following:

I.    INTRODUCTION
      [Brief statement of the challenge — which predicates are challenged
       and on what grounds]

II.   PROCEDURAL BACKGROUND
      [Current conviction, habitual bill filing, predicates alleged]

III.  CHALLENGE TO PREDICATE CONVICTION(S)
      A. Predicate [#] — [Charge, Case No.]
         [Specific deficiency and legal basis for challenge]
      B. Predicate [#] — [Charge, Case No.]
         [Specific deficiency and legal basis for challenge]
      [Continue for each challenged predicate]

IV.   LEGAL ARGUMENT
      [Detailed legal analysis — Shelton burden-shifting, Boykin requirements,
       sequence analysis, cleansing period, as applicable]

V.    PRAYER FOR RELIEF
      WHEREFORE, defendant [CLIENT NAME] respectfully prays that this
      Honorable Court:
      (1) Find Predicate [#] invalid and strike it from the habitual
          offender bill;
      (2) [Additional predicate challenges];
      (3) Determine the defendant is [not a habitual offender / a second
          offender rather than a fourth offender / etc.];
      (4) Impose a sentence within the [base / reduced enhancement] range;
      (5) Grant such other relief as the Court deems just and proper.

[CERTIFICATE OF SERVICE — per shared protocols]
[SIGNATURE BLOCK — per shared protocols]
[NOTICE OF HEARING — per shared protocols, if hearing required]
[PROPOSED ORDER — per shared protocols, attach as separate document]
```

## Output 3: Boykinization Challenge Motion

Separate motion specifically challenging the constitutionality of a predicate guilty plea:

```
MOTION TO FIND PREDICATE CONVICTION CONSTITUTIONALLY INVALID
FOR FAILURE TO COMPLY WITH BOYKIN v. ALABAMA

[Detailed Boykin/Shelton analysis for the specific predicate,
 with line-by-line comparison of the plea transcript against
 Boykin requirements]
```

## Output 4: Enhanced Sentencing Range Calculation

Formatted worksheet showing the enhancement calculation (Module E template).

## Output 5: Cleansing Period Timeline

Visual timeline for each predicate (Module D template). For complex cases with multiple predicates, present as a single consolidated timeline showing all predicates, completion dates, subsequent offenses, and cleansing period windows.

## Output 6: Dorthey Excessive Sentence Motion Framework

Structured motion following the Dorthey framework (Module F template).

## Output 7: Hearing Preparation Checklist

```
HABITUAL OFFENDER HEARING PREPARATION CHECKLIST
Case: State v. [Client], Docket No. [___]
Hearing Date: [date]

PRE-HEARING
[ ] Review all predicate conviction documentation
[ ] Complete predicate audit (Modules A-D)
[ ] Prepare challenge motion(s) — filed? [date / NOT YET]
[ ] Prepare defense exhibits (annotated transcripts, timelines, calculations)
[ ] Subpoena witnesses if necessary
[ ] Research judge's habitual offender hearing history
[ ] Calculate enhanced sentencing range (Module E)
[ ] Assess Dorthey challenge viability (Module F)
[ ] Prepare plea negotiation position (Module H)

AT HEARING — STATE'S CASE
[ ] Object to any procedural deficiency in the habitual bill filing
[ ] Challenge identity proof if deficient
[ ] Challenge each predicate conviction:
    [ ] Predicate 1: [challenge / no challenge — reason]
    [ ] Predicate 2: [challenge / no challenge — reason]
    [ ] Predicate 3: [challenge / no challenge — reason]
[ ] Cross-examine fingerprint expert (if applicable)
[ ] Cross-examine records custodian
[ ] Object to introduction of uncertified or incomplete records
[ ] Invoke Shelton burden-shifting for guilty plea predicates

AT HEARING — DEFENSE CASE
[ ] Introduce defense exhibits
[ ] Present Boykinization challenge(s)
[ ] Present sequence analysis (if applicable)
[ ] Present cleansing period argument (if applicable)
[ ] Call defense witnesses (if any)

POST-HEARING
[ ] If adjudicated habitual — preserve all objections on the record
[ ] File Motion to Reconsider Sentence (La. C.Cr.P. Art. 881.1)
[ ] File Dorthey motion if applicable
[ ] Note appellate issues and deadlines
[ ] File appeal within 30 days if appropriate (La. C.Cr.P. Art. 914)
```
