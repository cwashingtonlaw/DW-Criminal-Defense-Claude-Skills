# Step 5 — Objection Log

Maintain a running objection log for ALL evidentiary objections encountered at trial (not just exhibit objections):

| # | Exhibit | Party Offering | Objecting Party | Basis | Court's Ruling | Limiting Instruction | Appeal Flag |
|---|---------|---------------|-----------------|-------|-----------------|---------------------|-------------|
| 1 | D-1 | Defense | State | Hearsay - not exception | Sustained | N/A | YES - Preserve |
| 2 | S-3 | State | Defense | Relevance - unfair prejudice 403 | Overruled | Limited to [purpose] | NO |
| 3 | D-5 | Defense | State | Authentication - chain gap | Sustained | N/A | YES - Preserve |

**Common Louisiana Evidentiary Objections:**
- **Hearsay (Art. 802):** Out-of-court statement offered for truth — identify exception if applicable (Art. 803, 804)
- **Relevance (Art. 401/402):** Not probative of material fact OR probative value substantially outweighed by unfair prejudice (Art. 403)
- **Unfair Prejudice (Art. 403):** Probative but unduly prejudicial to party (e.g., gruesome photos, prior bad acts)
- **Authentication (Art. 901):** Insufficient foundation that exhibit is what it claims to be
- **Best Evidence (Art. 1002):** Original writing/recording required (exception for duplicate or oral testimony)
- **Confrontation Clause (Crawford v. Washington, 541 U.S. 36):** Testimonial hearsay against criminal defendant without cross-opportunity
- **Privilege (Art. 505-514):** Attorney-client, spousal, clergy, physician-patient, psychotherapist, etc.
- **Character Evidence (Art. 404/405):** Character evidence generally inadmissible except limited exceptions
- **Other Crimes (Art. 404(b)):** Evidence of other bad acts not admissible to prove character or propensity
- **Expert Methodology (Art. 702 / Daubert-Foret):** Expert methodology unreliable or not sufficient basis for opinion

**Feed sustained objections to appellate preservation:**
Every time the court sustains an objection to a defense exhibit or allows State evidence against objection, automatically flag to **dw-appellate-error-monitor** with:
- Exhibit number or statement
- Objection basis
- Ruling (Sustained / Overruled)
- Judge's exact language if available
- Trial date and judge name
