# Geolocation Audit Report Structure

## Output Format
Produce the audit as a **Word document (.docx)** using the docx skill. Read and follow the `docx` SKILL.md for all formatting and generation instructions.

## Report Structure

```
CELL SITE LOCATION & GEOLOCATION AUDIT
Daniels & Washington | [Case Name / Docket No.]

CASE INFORMATION
Defendant:      [Name]
Charges:        [All counts with La. R.S. citations]
Offense Date:   [Date]
Offense Location: [Address / area the state alleges]
Carrier(s):     [Name(s)]
Network Type:   [2G/3G/4G LTE/5G]
State's Analyst: [Name / Agency / Credentials]

SECTION 1: EXECUTIVE SUMMARY
[One-page overview: types of location evidence audited,
critical findings count, overall assessment of whether
the location data actually supports the state's placement
claim, top 3 defense opportunities]

SECTION 2: LOCATION EVIDENCE INVENTORY & CLASSIFICATION
[Complete inventory of all geolocation evidence with
source classification per the Evidence Category Matrix]

SECTION 3: LEGAL AUTHORIZATION AUDIT
[For each location evidence type:
 - What legal process was used to obtain it
 - Whether the authorization satisfies Carpenter and
   applicable circuit/state law
 - Particularity and scope analysis
 - Timeliness (was the data request within the
   authorization period?)
 - Suppression recommendation if warranted]

SECTION 4: METHODOLOGY AUDIT
[Per applicable Module (A through G):
 - Data integrity assessment
 - Analysis methodology evaluation
 - Precision and accuracy claims vs. reality
 - Coverage area analysis
 - Alternative location explanations
 - Each finding tagged: CRITICAL / SIGNIFICANT / MINOR]

SECTION 5: PROSECUTION CLAIMS vs. DATA REALITY
[The core of the audit — for each specific placement
claim the prosecution makes:
 - What the prosecution says the data shows
 - What the data actually shows
 - The gap between the claim and the data
 - Alternative explanations consistent with the data
 - Whether the data is equally consistent with innocence]

SECTION 6: MAPPING & VISUALIZATION RECOMMENDATIONS
[What defense exhibits should be created, what they
should show, and what expert is needed to create them]

SECTION 7: ADMISSIBILITY CHALLENGES
[For each critical finding:
 - The deficiency
 - Legal basis for challenge
 - Recommended motion type
 - Supporting case law]

SECTION 8: CROSS-EXAMINATION QUESTIONS
[Organized by witness type:
 - Cell Site Analyst / Location Witness
 - Law Enforcement (who obtained the data)
 - Carrier Records Custodian (if testifying)
 Each question with:
  - The precision overstatement or methodology flaw it targets
  - Source document and page/Bate stamp reference
  - Expected response and follow-up
  - Impeachment note if applicable]

SECTION 9: DEFENSE ACTION ITEMS
[Prioritized:
 - Motions to file (suppress, Daubert, compel)
 - Missing Discovery Demand items
 - Defense expert needs (RF engineer, data analyst)
 - Independent analysis requests
 - Items for Cross-Exam Architect skill]

SECTION 10: DISCOVERY GAP REPORT
[Expected location documentation not provided:
 Each with: what's missing, why it matters,
 recommended action]

APPENDIX A: LEGAL STANDARDS REFERENCE TABLE
[All standards cited in the audit with full citations]

APPENDIX B: CROSS-EXAM CHAPTER SEEDS
[Formatted for dw-cross-exam-architect-crim integration]

APPENDIX C: TECHNICAL GLOSSARY
[Key terms defined for attorney and jury use]
```

## Severity Classification
Tag every finding:

- **CRITICAL:** Directly undermines the reliability or admissibility of the location evidence, or reveals that the data does not actually support the state's placement claim. Supports a motion to suppress, Daubert challenge, or creates substantial reasonable doubt. Example: the sector coverage area that the state says proves presence at the crime scene also covers the defendant's home; CSS use was concealed through parallel construction; geofence warrant lacked particularity.
- **SIGNIFICANT:** Weakens the evidentiary value and provides strong cross-examination material. Example: analyst used azimuth-only mapping without propagation analysis; tower dump captured 3,000 devices; GPS data points have large accuracy radii.
- **MINOR:** Technical irregularity that may affect weight but does not independently undermine the evidence. Example: CDR time zone not explicitly documented but inferable; analyst credentials lack specific training in the technology at issue.
