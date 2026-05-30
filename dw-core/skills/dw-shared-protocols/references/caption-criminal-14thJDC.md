# Caption — 14th JDC Calcasieu Parish

Standard criminal caption for the 14th Judicial District Court, Parish of Calcasieu, Lake Charles.

## Template

```
STATE OF LOUISIANA              *    14TH JUDICIAL DISTRICT COURT
                                *
VERSUS                          *    PARISH OF CALCASIEU
                                *
{{DEFENDANT_NAME}}              *    STATE OF LOUISIANA
                                *
DOCKET NO. {{DOCKET}}           *    DIVISION "{{DIVISION}}"
                                *
                                *    JUDGE {{JUDGE_NAME}}
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```

## Title block (immediately below caption)

Centered, bold, all caps:

```
{{MOTION_TITLE}}
```

Examples:
- `MOTION TO SUPPRESS EVIDENCE`
- `OPPOSITION TO STATE'S NOTICE OF INTENT TO USE OTHER CRIMES EVIDENCE`
- `MOTION FOR REDUCTION OF BOND`
- `MEMORANDUM IN SUPPORT OF MOTION TO SUPPRESS EVIDENCE`

## Opening paragraph format

```
NOW INTO COURT, through undersigned counsel, comes Defendant, {{DEFENDANT_NAME}}, who
respectfully {{moves|opposes|submits}} this Honorable Court {{requested action}}, and
in support {{thereof|states}} as follows:
```

## Notes

- Division designations in Calcasieu are letters (A through G typically; verify from Case Brain).
- Docket numbers in 14th JDC use the format used by the Clerk's office; do not invent a format — pull directly from Case Brain.
- Caption font: Times New Roman 12 pt (per `filing-conventions-14thJDC.md`).
- The asterisk column should align consistently; use a tab stop at ~3.25" if rendering to .docx.

## Variations

**Sealed / juvenile cases:** add `IN RE:` line and `SEALED` watermark; no defendant name in caption — use initials per La. Ch.C. art. 412.

**Multi-defendant:**
```
{{DEFENDANT_NAME_1}}
AND                             *
{{DEFENDANT_NAME_2}}
```
Or list in single line if all defendants are joining the motion.
