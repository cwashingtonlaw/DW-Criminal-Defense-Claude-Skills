# Audit Report Structure

## Output Format
Produce the audit as a **Word document (.docx)** using the docx skill. Read and follow the `docx` SKILL.md for all formatting and generation instructions.

## Report Structure

```
CHAIN OF CUSTODY AUDIT
Daniels & Washington | [Case Name / Docket No.]

CASE INFORMATION
Defendant:      [Name]
Charges:        [All counts with La. R.S. citations]
Offense Date:   [Date]
Evidence Items: [Total number of items audited]
Agencies:       [All agencies involved in evidence handling]
Lab(s):         [Name(s) / ASCLD/LAB Accreditation Status]

SECTION 1: EXECUTIVE SUMMARY
[One-page overview: total evidence items audited, chain integrity
ratings summary (how many INTACT / WEAKENED / COMPROMISED / BROKEN),
critical findings count, top defense opportunities, recommended
immediate actions]

SECTION 2: EVIDENCE INVENTORY & TYPE CLASSIFICATION
[Complete inventory of all evidence items with:
 - Item number
 - Description
 - Evidence type (Physical / Digital / Biological / Drug / Firearm)
 - Applicable audit module
 - Chain integrity rating (preliminary)
 Items sorted by severity of chain issues — worst first]

SECTION 3: ITEM-BY-ITEM CHAIN OF CUSTODY TIMELINE
[For each evidence item (or grouped by type if items share
identical chains):

 ITEM [#]: [Description]
 Chain Integrity Rating: [INTACT / WEAKENED / COMPROMISED / BROKEN]

 LINK 1: Collection
   Handler: [Name / Badge / Agency]
   Date/Time: [Timestamp]
   Location: [Where collected]
   Packaging: [Type / Seal documentation]
   Documentation Status: COMPLETE / PARTIAL / ABSENT
   Deficiencies: [List any]

 LINK 2: Transport to Evidence Facility
   [Same structure]

 LINK 3: Evidence Facility Intake
   [Same structure]

 LINK 4: Storage
   [Same structure — include storage conditions]

 LINK 5: Lab Submission / Return
   [Same structure]

 LINK 6: Trial/Court Presentation
   [Same structure, if applicable]

 GAPS IDENTIFIED:
   Gap 1: [Date range] — [Duration] — Evidence unaccounted for
   Gap 2: [Date range] — [Duration] — Evidence unaccounted for

 DEFICIENCY SUMMARY:
   CRITICAL: [Count and list]
   SIGNIFICANT: [Count and list]
   MINOR: [Count and list]]

SECTION 4: EVIDENCE-TYPE-SPECIFIC AUDIT FINDINGS
[Subsection per applicable Module (B through E):

 4A: Digital Evidence Chain Findings (Module B)
   - Hash value verification results
   - Write-blocking documentation status
   - Imaging procedure documentation
   - Each finding tagged: CRITICAL / SIGNIFICANT / MINOR

 4B: Biological Evidence Chain Findings (Module C)
   - Cold-chain continuity assessment
   - Contamination risk analysis
   - Sample consumption tracking
   - Each finding tagged

 4C: Drug Evidence Chain Findings (Module D)
   - Weight reconciliation table (weight at every transfer point)
   - Secure storage compliance
   - Field test consumption documentation
   - Each finding tagged

 4D: Firearm/Ballistic Evidence Chain Findings (Module E)
   - Serial number verification across chain
   - Comparison surface preservation
   - Each finding tagged]

SECTION 5: CHAIN DOCUMENTATION DEFICIENCY MATRIX (Module F)
[Master table: every evidence item scored against the seven
documentation requirements at every transfer link.
Visual matrix showing COMPLETE / PARTIAL / ABSENT / CONTRADICTED
for each cell. Summary statistics.]

SECTION 6: ADMISSIBILITY vs. WEIGHT ANALYSIS
[For each CRITICAL and SIGNIFICANT finding:
 - The deficiency
 - Whether it affects ADMISSIBILITY (suppression argument) or
   WEIGHT (cross-examination opportunity) — or both
 - Legal authority
 - Recommended motion or trial strategy
 - The distinction under Louisiana law per State v. Sweeney:
   "A defect in the chain of custody goes to the weight of the
   evidence rather than its admissibility" — BUT when the chain
   is so deficient that the evidence cannot be authenticated
   under La. C.E. Art. 901, admissibility IS at issue]

SECTION 7: SUPPRESSION MOTION FRAMEWORK
[For chain failures warranting exclusion:
 - Legal basis (La. C.E. Art. 901(B)(1), La. C.Cr.P. Art. 703,
   4th Amendment if seizure was illegal)
 - Factual basis (the specific chain failures)
 - Argument structure
 - Supporting case law
 - Anticipated State response and rebuttal
 - If evidence was destroyed/lost: Youngblood / Trombetta
   analysis (bad faith inquiry)]

SECTION 8: CROSS-EXAMINATION QUESTION SETS
[Organized by witness type:
 - Evidence Custodian / Property Room Technician
 - Crime Scene Technician (evidence handling)
 - Transport Officer
 - Lab Intake Technician
 - Forensic Analyst (chain-related questions only)
 - Lead Detective (evidence handling oversight)

 Each question set formatted per Module G template with:
  - The deficiency it targets
  - Source document and page/Bate stamp reference
  - Expected response and follow-up if denied
  - Impeachment note if applicable]

SECTION 9: DEFENSE ACTION ITEMS
[Prioritized list:
 - Motions to file (suppress, compel chain documentation,
   request independent testing before sample exhaustion)
 - Missing Discovery Demand items (chain documentation the
   State has not produced)
 - Expert witness needs (evidence handling expert, forensic
   chemist for weight analysis, digital forensics expert)
 - Independent testing requests (especially for biological
   and drug evidence before samples are exhausted)
 - Items for Cross-Exam Architect skill
 - Items requiring investigator follow-up (verify storage
   conditions, photograph evidence room, obtain agency SOPs)
 - Evidence preservation demands (if destruction is imminent)]

SECTION 10: DISCOVERY GAP REPORT
[Chain of custody documentation expected but not provided:
 Each with: what's missing, why it matters, legal authority
 for demanding it (La. C.Cr.P. Art. 718-719), recommended
 supplemental discovery demand language]

APPENDIX A: WEIGHT RECONCILIATION TABLE (Drug Evidence)
[If drug evidence exists: complete weight tracking table
 showing weight at every documented transfer point with
 variance calculations]

APPENDIX B: HASH VALUE VERIFICATION TABLE (Digital Evidence)
[If digital evidence exists: complete hash value tracking
 table showing hash values at every documented checkpoint]

APPENDIX C: COLD-CHAIN TIMELINE (Biological Evidence)
[If biological evidence exists: temperature/storage condition
 timeline from collection through lab analysis]

APPENDIX D: LEGAL AUTHORITY REFERENCE TABLE
[All statutes, case law, and standards cited in the audit]

APPENDIX E: CROSS-EXAM CHAPTER SEEDS
[Formatted for dw-cross-exam-architect integration]
```

## Severity Classification

Tag every finding with a severity level:

- **CRITICAL:** Chain failure that directly undermines the authentication or integrity of the evidence. Supports a motion to suppress, creates a genuine question about whether the evidence presented at trial is the same evidence collected at the scene, or reveals destruction/loss of potentially exculpatory material. Examples: broken chain with no documentation for days; biological evidence stored at room temperature for weeks; hash values that don't match; drug weight discrepancy of 20%+ with no explanation; evidence consumed without defense notification.

- **SIGNIFICANT:** Chain deficiency that weakens the evidentiary value and provides strong cross-examination material, but may not independently support exclusion under Louisiana's weight-not-admissibility framework. Examples: evidence booked hours after collection with no explanation for the delay; no cold-chain documentation for biological samples (but refrigeration claimed); single-person access to drug storage; write-blocker use not documented (but claimed).

- **MINOR:** Procedural irregularity that may affect weight with the jury but does not independently undermine admissibility or integrity. Examples: evidence label partially illegible; transfer form missing time (but date present); periodic inventory not conducted on schedule but evidence otherwise accounted for.
