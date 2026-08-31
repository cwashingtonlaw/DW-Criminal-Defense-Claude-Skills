# Intake Memo + Scope of Representation

Read at SKILL.md MODULE F — Intake Memo + Scope of Representation; holds the intake memo template, the engagement-scope template menu, and the outputs-to-file table with markings.

### Intake memo structure

```
[ATTORNEY WORK PRODUCT MARKING]
[PROSPECTIVE-CLIENT MARKING — until engagement signed]

INTAKE MEMORANDUM
Client:           [Full legal name]
Date of Intake:   [YYYY-MM-DD]
Conducted by:     [Attorney name(s)]
Present:          [Client / family member with relationship / interpreter / other]
Custody status:   [In custody at [facility] / Out on bond / Summoned / Warrant pending / Charges threatened]

I.    CLIENT IDENTIFICATION
      [Tier 1 identity data — name, DOB, address, contact, aliases]

II.   CHARGES (CURRENT KNOWLEDGE)
      [Charge(s) as known at intake — La. R.S. citation if known, everyday description if not.
       Charge category routed to: [specialist]. Maximum exposure as known: [years/fine].]

III.  PROCEDURAL POSTURE
      [Date of offense / Date of arrest / Date charges filed / Court / Docket / Next court date /
       Bond status / Conditions of release / Prior counsel on this matter]

IV.   CONFLICT CHECK SUMMARY
      [Names screened, database queried, result, screening attorney, date — see separate
       Conflict Check Record for full documentation]

V.    CLIENT NARRATIVE (Module C output)
      [Open narrative in client's words, with direct-quote markers]
      [Structured timeline from closed phase]
      [Statements made to third parties]
      [Devices and accounts touched]
      All [CLIENT-REPORTED — UNVERIFIED] unless otherwise marked.

VI.   IMMEDIATE-ACTION ITEMS (Module D output)
      [Bond posture and routing to dw-bond-and-release-motion-crim]
      [Evidence preservation letters drafted — list]
      [Social media lockdown status]
      [Jail call hygiene letter status]
      [No-contact and surrender posture]
      [Device and digital footprint actions]

VII.  INVESTIGATION SEED (Module E output)
      [Witnesses, locations, video sources, devices, alibi, character, records, inconsistencies]
      Routed to dw-defense-investigator-tasking-crim.

VIII. CHARGE-TYPE DISPATCH (Module B output)
      [Specialist skill(s) the attorney should invoke after retention]
      [Charge-specific intake questions answered — addendum]

IX.   COLLATERAL CONSEQUENCES FLAGS
      [Padilla / immigration / professional license / firearms disability / sex offender registration /
       other — flag for downstream collateral-consequences analysis]

X.    OPEN QUESTIONS / NEXT STEPS
      [What we do not know yet]
      [What we are waiting on]
      [Next attorney-client meeting]
      [Next deadlines]
```

### Engagement scope draft

The scope of representation is the contractual term that tells client and firm what is and is not covered. It pairs with (but does not replace) the firm's standard engagement letter.

Use `references/engagement-scope-templates.md` to draft the scope language. The templates cover:

- Flat fee — pre-trial only
- Flat fee — through trial
- Flat fee — appellate only
- Hourly engagement — investigation phase
- Hourly engagement — full representation
- Specific exclusions (federal companion proceedings, civil collateral matters, post-conviction relief, immigration proceedings, professional-license proceedings)
- Withdrawal grounds language
- File-handling / file-return clauses on case closure
- Third-party payor disclosure (Rule 1.8(f))
- Conflict-waiver language where applicable

**The attorney signs the engagement letter.** Cowork drafts the scope; the attorney finalizes. A signed engagement letter (or a documented decline) is required before any privileged work product is produced for permanent storage.

### Outputs to file

| File | Path | Marking |
|---|---|---|
| Intake Memo | `00 - Client File/01 - Intake/Intake Memo - [Client] - [Date].docx` | Work product + Prospective-client (until signed) |
| Conflict Check Record | `00 - Client File/01 - Intake/Conflict Check - [Client] - [Date].docx` | Work product |
| Engagement Scope Draft | `00 - Client File/01 - Intake/Engagement Scope - [Client] - [Date].docx` | Work product (final signed letter is filed by attorney) |
| Immediate-Action Checklist | `00 - Client File/01 - Intake/Immediate Actions - [Client] - [Date].docx` | Work product |
| Preservation Letter Drafts | `00 - Client File/01 - Intake/Preservation Letters/` | Work product (final signed letters dispatched by attorney) |
| Social Media Lockdown Worksheet | `00 - Client File/01 - Intake/Social Media Lockdown - [Client].docx` | Work product (signed by client) |
| Investigation Seed | `02 - Investigation/00 - Investigation Plan/Investigation Seed - [Client] - [Date].docx` | Work product |
