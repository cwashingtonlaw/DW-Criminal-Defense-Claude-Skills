# Signature Block

Standard signature block for filed pleadings. Pulled from the firm's filing template and applied at the end of every motion, opposition, and memorandum.

## State court signature block

```
                              Respectfully submitted,

                              DANIELS & WASHINGTON, LLC


                              ___________________________________
                              CHRISTOPHER J. WASHINGTON #31354
                              38167 Post Office Road
                              Prairieville, Louisiana 70769
                              Telephone: (225) 383-3800
                              Facsimile: (225) 208-1567
                              Email: cjw@danielswashington.com
                              ATTORNEY FOR DEFENDANT,
                              {{DEFENDANT_NAME}}
```

## Federal court signature block

```
                              Respectfully submitted,

                              DANIELS & WASHINGTON, LLC


                              /s/ Christopher J. Washington
                              ___________________________________
                              CHRISTOPHER J. WASHINGTON
                              Louisiana Bar No. 31354
                              38167 Post Office Road
                              Prairieville, Louisiana 70769
                              Telephone: (225) 383-3800
                              Email: cjw@danielswashington.com
                              ATTORNEY FOR DEFENDANT,
                              {{DEFENDANT_NAME}}
```

## Firm identity (standing values)

These are the firm's standing values, already filled into the blocks above. Update them here if the firm moves, changes numbers, or Chris's bar status changes:

- **Bar number:** 31354 (Christopher J. Washington, Louisiana)
- **Firm street address:** 38167 Post Office Road, Prairieville, Louisiana 70769
- **Telephone:** (225) 383-3800
- **Facsimile:** (225) 208-1567
- **Email:** cjw@danielswashington.com

Case-specific values (`{{DEFENDANT_NAME}}`, etc.) are still resolved from Case Brain at draft time. Never insert a blank or placeholder for the firm identity into a filed pleading — if any value above is ever cleared, prompt the attorney before drafting.

## Multi-attorney variant

When co-counsel signs:

```
                              Respectfully submitted,

                              DANIELS & WASHINGTON, LLC


                              ___________________________________
                              CHRISTOPHER J. WASHINGTON #31354
                              [firm address block]


                              ___________________________________
                              {{COCOUNSEL_NAME}} (#{{COCOUNSEL_BAR}})
                              {{COCOUNSEL_FIRM}}
                              [co-counsel address block]
                              CO-COUNSEL FOR DEFENDANT
```

## Notes

- Two blank lines above the signature line for ink signature in state court.
- `/s/` electronic signature standard in federal court (CM/ECF requirement) and acceptable in state court.
- "Respectfully submitted," precedes the firm name with a comma, no period.
- `ATTORNEY FOR DEFENDANT` line is mandatory — identifies role unambiguously.
