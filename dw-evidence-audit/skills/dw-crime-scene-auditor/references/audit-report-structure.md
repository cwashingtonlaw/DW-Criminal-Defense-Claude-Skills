# Crime Scene & Physical Evidence Audit Report Structure

### Output Format
Produce the audit as a **Word document (.docx)** using the docx skill. Read and follow the `docx` SKILL.md for all formatting and generation instructions.

### Report Structure

```
CRIME SCENE & PHYSICAL EVIDENCE AUDIT
Daniels & Washington | [Case Name / Docket No.]

CASE INFORMATION
Defendant:      [Name]
Charges:        [All counts with La. R.S. citations]
Offense Date:   [Date]
Scene Type:     [Indoor / Outdoor / Vehicle / Multiple]
Lead CSI:       [Name / Agency / Certifications]
Lab(s):         [Name(s) / ASCLD Accreditation Status]

SECTION 1: EXECUTIVE SUMMARY
[One-page overview: total evidence categories audited, critical
findings count, overall assessment of evidence reliability,
top 3 defense opportunities]

SECTION 2: SCENE PROCESSING AUDIT (Module A)
[Scene security, processing protocol, personnel, standards
compliance, deficiencies with cited standards]

SECTION 3: EVIDENCE-SPECIFIC AUDITS
[One subsection per applicable Module (B through F):
 - Collection methodology assessment
 - Analysis methodology assessment
 - Reliability concerns specific to this case
 - Standards violations identified
 - Each finding tagged: CRITICAL / SIGNIFICANT / MINOR]

SECTION 4: SCENE DOCUMENTATION AUDIT (Module G)
[Photography, sketching, video assessment with deficiency matrix]

SECTION 5: CHAIN OF CUSTODY AUDIT (Module H)
[Link-by-link analysis for each key evidence item,
red flags identified, timeline of custody]

SECTION 6: ADMISSIBILITY CHALLENGES
[For each critical finding:
 - The deficiency
 - Applicable standard violated
 - Legal basis for challenge (Daubert / La. C.E. Art. 702,
   suppression under La. C.Cr.P. Art. 703, authentication
   under La. C.E. Art. 901, or weight argument)
 - Recommended motion type
 - Supporting case law]

SECTION 7: CROSS-EXAMINATION QUESTIONS
[Organized by witness type:
 - Crime Scene Technician / Lead CSI
 - Evidence Custodian
 - Lab Analyst (per discipline)
 - Lead Detective (evidence-related only)
 Each question with:
  - The deficiency it targets
  - Source document and page/Bate stamp reference
  - Expected response and follow-up if denied
  - Impeachment note if applicable]

SECTION 8: DEFENSE ACTION ITEMS
[Prioritized list:
 - Motions to file (suppress, Daubert, compel)
 - Missing Discovery Demand items
 - Expert witness needs (by discipline)
 - Independent testing requests
 - Items for Cross-Exam Architect skill
 - Items requiring investigator follow-up]

SECTION 9: DISCOVERY GAP REPORT
[Expected forensic documentation not provided:
 Each with: what's missing, why it matters, recommended action]

APPENDIX A: STANDARDS REFERENCE TABLE
[All standards cited in the audit with full citations]

APPENDIX B: CROSS-EXAM CHAPTER SEEDS
[Formatted for dw-cross-exam-architect integration]
```

### Severity Classification
Tag every finding with a severity level:

- **CRITICAL:** Deficiency that directly undermines the reliability or admissibility of the evidence. Supports a motion to suppress, Daubert challenge, or creates substantial reasonable doubt. Example: DNA evidence collected with contaminated swabs; no chain of custody for the murder weapon.
- **SIGNIFICANT:** Deficiency that weakens the evidentiary value and provides strong cross-examination material, but may not independently support exclusion. Example: No elimination prints collected; crime scene log incomplete.
- **MINOR:** Procedural irregularity that may affect weight with the jury but does not independently undermine admissibility. Example: Photo log has minor gaps in sequence numbering; scene sketch lacks compass orientation.
