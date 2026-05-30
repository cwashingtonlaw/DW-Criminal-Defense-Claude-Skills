# Signature Block

Standard signature block for filed pleadings. Pulled from the firm's filing template and applied at the end of every motion, opposition, and memorandum.

## State court signature block

```
                              Respectfully submitted,

                              DANIELS & WASHINGTON, LLC


                              ___________________________________
                              CHRISTOPHER J. WASHINGTON #31354
                              {{FIRM_ADDRESS_LINE_1}}
                              {{FIRM_ADDRESS_LINE_2}}
                              Lake Charles, Louisiana 70601
                              Telephone: {{FIRM_PHONE}}
                              Facsimile: {{FIRM_FAX}}
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
                              Louisiana Bar No. {{BAR_NUMBER}}
                              {{FIRM_ADDRESS_LINE_1}}
                              {{FIRM_ADDRESS_LINE_2}}
                              Lake Charles, Louisiana 70601
                              Telephone: {{FIRM_PHONE}}
                              Email: cjw@danielswashington.com
                              ATTORNEY FOR DEFENDANT,
                              {{DEFENDANT_NAME}}
```

## Variables to resolve from firm config

The consuming skill should pull these from a firm config file (or Case Brain firm section) — never hardcoded:

- `{{BAR_NUMBER}}` — Chris's Louisiana bar roll number
- `{{FIRM_ADDRESS_LINE_1}}`, `{{FIRM_ADDRESS_LINE_2}}` — current firm street address
- `{{FIRM_PHONE}}`, `{{FIRM_FAX}}` — current firm telephone and fax

If firm config is missing, prompt attorney before drafting — never insert placeholder text into a filed pleading.

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
