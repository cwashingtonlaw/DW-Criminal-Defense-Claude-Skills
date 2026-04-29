# Caption — Orleans Criminal District Court

Criminal District Court for the Parish of Orleans. Unique among Louisiana state courts: not a Judicial District, uses **Section** instead of **Division**, and has its own clerk and case-numbering system.

## Template

```
STATE OF LOUISIANA              *    CRIMINAL DISTRICT COURT
                                *
VERSUS                          *    PARISH OF ORLEANS
                                *
{{DEFENDANT_NAME}}              *    STATE OF LOUISIANA
                                *
CASE NO. {{CASE_NUMBER}}        *    SECTION "{{SECTION}}"
                                *
                                *    JUDGE {{JUDGE_NAME}}
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```

## Title block

Same format — centered, bold, all caps motion title immediately below caption.

## Opening paragraph

```
NOW INTO COURT, through undersigned counsel, comes Defendant, {{DEFENDANT_NAME}}, who
respectfully {{moves|opposes|submits}} this Honorable Court {{requested action}}, and
in support {{thereof|states}} as follows:
```

## Notes

- **Section, not Division.** Orleans CDC criminal sections are designated by letter (Sections A through L for criminal trial sections, plus Magistrate). Confirm the section letter from Case Brain — do not default to the Calcasieu "Division" terminology.
- **Case No., not Docket No.** Orleans CDC uses "CASE NO." as the standard label.
- ⚠️ **Verification flag:** Confirm magistrate caption variant if drafting at magistrate level (initial appearance, bond, search warrant return). If matter is in the Magistrate Section, change `SECTION "{{SECTION}}"` to `MAGISTRATE SECTION` and adjust.
- Service in Orleans CDC: typically via the District Attorney's Office, Tulane & Broad address. Confirm in Case Brain before finalizing certificate of service.
- E-filing: Orleans CDC has its own clerk e-filing portal — pull current portal info from `filing-conventions-orleans-CDC.md` if it exists; otherwise prompt attorney.
