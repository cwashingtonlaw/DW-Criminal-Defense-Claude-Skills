# Caption — 12th JDC Avoyelles Parish

Standard criminal caption for the 12th Judicial District Court, Parish of Avoyelles, Marksville.

## Template

```
STATE OF LOUISIANA              *    12TH JUDICIAL DISTRICT COURT
                                *
VERSUS                          *    PARISH OF AVOYELLES
                                *
{{DEFENDANT_NAME}}              *    STATE OF LOUISIANA
                                *
DOCKET NO. {{DOCKET}}           *    DIVISION "{{DIVISION}}"
                                *
                                *    JUDGE {{JUDGE_NAME}}
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```

## Title block

Same format as 14th JDC — centered, bold, all caps motion title immediately below caption.

## Opening paragraph

```
NOW INTO COURT, through undersigned counsel, comes Defendant, {{DEFENDANT_NAME}}, who
respectfully {{moves|opposes|submits}} this Honorable Court {{requested action}}, and
in support {{thereof|states}} as follows:
```

## Notes

- Verify division letter and judge from Case Brain — 12th JDC has fewer divisions than 14th.
- ⚠️ **Verification flag:** Confirm the local 12th JDC clerk's preferred docket number format and any local rule on caption layout. Initial build assumes standard La. state criminal caption conventions.
- Filing conventions: defaults to general Louisiana state court conventions until a `filing-conventions-12thJDC.md` is built.
