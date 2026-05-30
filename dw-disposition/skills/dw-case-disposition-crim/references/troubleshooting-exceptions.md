# Troubleshooting & Exceptions

## Exception 1: Co-Defendant Cases

If case involves multiple co-defendants:
- Close case only for the specific client represented by this firm
- Note in Case Brain if other co-defendants have pending cases
- Preserve any discovery or evidence for potential cross-case use
- Archive separately by client name to avoid confusion

## Exception 2: Retrial or Mistrial Ordered

If new trial is ordered after verdict:
- Do NOT archive case
- Mark in Case Brain: "MISTRIAL — RETRIAL SCHEDULED"
- Return to **dw-criminal-defense-crim** master workflow
- Re-invoke **dw-case-disposition-crim** only after final verdict/disposition

## Exception 3: Cases Transferred to Different Jurisdiction

If case transferred (federal, state, county):
- Mark disposition as "Transfer to [Jurisdiction]"
- Provide notice to new counsel if applicable
- Archive with note: "Case transferred — files maintained per original jurisdiction requirements"
- Retain files per both jurisdictions' rules of professional conduct (use longer requirement)

## Exception 4: Confidential Informant or Sensitive Documents

If case contains confidential informant information or sealed discovery:
- Flag files as "SENSITIVE — RESTRICTED ACCESS"
- Archive in secure location with access restrictions
- Do not tag in shared systems (DEVONthink, shared drives)
- Maintain separate secure log of sensitive files
- Consult with attorney re: destruction timeline (may exceed 5 years)

## Exception 5: Client Incarcerated Post-Sentencing

For clients entering custody:
- Ensure jail mail notification format complies with facility rules
- Include in letter: Sentence calculation, good-time credit projection (via **dw-sentencing-mitigation-specialist-crim**)
- Provide contact information for firm (appeals, record correction, etc.)
- Note in Case Brain if client will need appellate or post-conviction assistance
- Archive case but maintain active contact protocol for incarcerated client needs
