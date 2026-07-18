# Proposed Order

Every contested motion in Louisiana state court should be filed with a proposed order. The proposed order is a separate document but filed contemporaneously.

## Standard proposed order

```
[CAPTION — same as motion, copied verbatim]


                              ORDER


       Considering the foregoing {{MOTION_TITLE}}:

       IT IS ORDERED that the {{requested action — e.g., "Defendant's Motion
to Suppress Evidence is hereby GRANTED" / "DENIED" / "set for hearing on _______"}}.

       {{Additional ordered relief, if any}}.

       SIGNED this _______ day of ____________, 20___, in {{CITY}}, Louisiana.



                              ___________________________________
                              JUDGE, {{COURT_NAME}}
                              {{DIVISION_LABEL}} "{{DIVISION}}"
```

## Granted / Denied / Setting variant

Best practice in Louisiana state court: file a proposed order with both GRANT and DENY language as alternative blocks, OR file a neutral "set for hearing" order. The choice depends on whether the motion is contested.

**If unopposed or expected to be granted on the papers:**
```
IT IS ORDERED that {{Defendant's Motion to ___}} is hereby GRANTED.
```

**If contested (most common):**
```
IT IS ORDERED that the foregoing motion is set for contradictory hearing
on the _______ day of ____________, 20___, at _______ o'clock ___.M.,
before the Honorable {{JUDGE_NAME}}, {{DIVISION_LABEL}} "{{DIVISION}}",
{{COURT_NAME}}.
```

## Federal proposed order

Federal court typically uses a more streamlined order:

```
[CAPTION]

                              ORDER

       Before the Court is Defendant's {{MOTION_TITLE}}. After consideration
of the motion and the applicable law,

       IT IS ORDERED that the motion is {{GRANTED|DENIED}}.

       {{Additional language as needed}}.

       THUS DONE AND SIGNED in chambers at {{CITY}}, Louisiana, on this
_______ day of ____________, 20___.



                              ___________________________________
                              UNITED STATES {{DISTRICT|MAGISTRATE}} JUDGE
```

## Filing convention

- Proposed order filed as a separate PDF/.docx, not stapled to the motion.
- Caption identical to the motion.
- No certificate of service on the proposed order — the motion's COS covers it.
- No work product marking — this is a filed document.
- File name format (per `output-path-formula.md`): `[motion-name]_PROPOSED-ORDER.docx`

## When to omit a proposed order

- Notice of hearing (the notice itself sets a hearing — no separate order needed)
- Discovery requests (no court action requested)
- Internal memoranda (not filed)
