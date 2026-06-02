# Signature Block

Standard signature block for filed pleadings. Pulled from the firm's filing template and applied at the end of every motion, opposition, and memorandum.

## State court signature block

```
                              Respectfully submitted,

                              DANIELS & WASHINGTON LAW FIRM, LLC


                              ___________________________________
                              CHRISTOPHER J. WASHINGTON #31354
                              Daniels & Washington Law Firm, LLC
                              38167 Post Office Road
                              Prairieville, Louisiana 70769
                              Telephone: 225-383-3800
                              Facsimile: (225) 208-1567
                              Email: cjw@danielswashington.com
                              ATTORNEY FOR DEFENDANT,
                              {{DEFENDANT_NAME}}
```

## Federal court signature block

```
                              Respectfully submitted,

                              DANIELS & WASHINGTON LAW FIRM, LLC


                              /s/ Christopher J. Washington
                              ___________________________________
                              CHRISTOPHER J. WASHINGTON
                              Louisiana Bar No. 31354
                              Daniels & Washington Law Firm, LLC
                              38167 Post Office Road
                              Prairieville, Louisiana 70769
                              Telephone: 225-383-3800
                              Email: cjw@danielswashington.com
                              ATTORNEY FOR DEFENDANT,
                              {{DEFENDANT_NAME}}
```

## Firm identity (fixed — matches `letterhead.md`)

The firm name, address, phone, and fax are fixed values and are hardcoded in the blocks above. They must always read:

- **Firm:** Daniels & Washington Law Firm, LLC
- **Address:** 38167 Post Office Road, Prairieville, Louisiana 70769
- **Telephone:** 225-383-3800   **Facsimile:** (225) 208-1567
- **Christopher J. Washington** — Louisiana Bar No. 31354 — cjw@danielswashington.com

Keep these in sync with `letterhead.md` (the single source of truth for firm contact details). The only per-case variable in a single-attorney block is `{{DEFENDANT_NAME}}`. When a different attorney of record or co-counsel signs, use the multi-attorney variant below and supply their name/bar/firm.

## Multi-attorney variant

When co-counsel signs:

```
                              Respectfully submitted,

                              DANIELS & WASHINGTON LAW FIRM, LLC


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
