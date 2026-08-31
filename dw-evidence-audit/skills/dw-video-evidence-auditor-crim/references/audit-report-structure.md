# Narrative Audit Report Structure

## Output Format
Produce the audit as a **Word document (.docx)** using the docx skill. Read and follow the `docx` SKILL.md for all formatting and generation instructions.

## Report Structure

```
VIDEO EVIDENCE AUDIT
Daniels & Washington | [Case Name / Docket No.]

CASE INFORMATION
Defendant:      [Name]
Charges:        [All counts with La. R.S. citations]
Offense Date:   [Date]
Responding Agency: [Department]
Video Sources:  [Count and types — e.g., "3 BWC, 1 dash cam, 2 CCTV"]
Total Footage:  [Combined duration across all sources]

SECTION 1: EXECUTIVE SUMMARY
[One-page overview: total video sources audited, critical
findings count, key activation gaps, top discrepancies
between video and reports, overall assessment]

SECTION 2: VIDEO INVENTORY & CLASSIFICATION
[Complete inventory of all video evidence with source
classification per the Video Source Matrix]

SECTION 3: ACTIVATION & COVERAGE ANALYSIS
[For BWC/dash cam — activation compliance assessment,
gap analysis per officer, policy compliance scorecard.
For CCTV — coverage map, recording schedule, retention
analysis]

SECTION 4: VIDEO-BY-VIDEO TIMESTAMP LOGS
[Detailed logs per Step 3 for each video file,
or reference to the appendix if voluminous]

SECTION 5: CONTENT-VS-REPORT DISCREPANCY ANALYSIS
[Every instance where video content differs from
written reports, organized by significance:
CRITICAL / SIGNIFICANT / MINOR
Each discrepancy with:
 - What the report says
 - What the video shows
 - Why it matters
 - Source citation (report page + video timestamp)]

SECTION 6: TECHNICAL LIMITATIONS ASSESSMENT
[Perspective restrictions, audio gaps, resolution
limitations, lighting conditions, compression artifacts,
and how each limitation affects the evidentiary value
of what the video purportedly shows]

SECTION 7: AUTHENTICATION & METADATA AUDIT
[For each video source:
 - File metadata integrity
 - Timestamp verification
 - Chain of custody assessment
 - Export/conversion documentation
 - Any signs of editing or alteration]

SECTION 8: POLICY COMPLIANCE ASSESSMENT
[BWC policy compliance by officer, with specific
violations cited against the agency's written policy.
Surveillance system compliance with retention
and disclosure obligations]

SECTION 9: ADMISSIBILITY CHALLENGES
[For each critical finding:
 - The deficiency
 - Legal basis for challenge
 - Recommended motion type
 - Supporting case law]

SECTION 10: CROSS-EXAMINATION QUESTIONS
[Organized by witness type:
 - Responding Officer(s) (BWC-related)
 - Video Unit Custodian / IT Personnel
 - Surveillance System Owner/Operator
 - Lead Detective (video-related)
 Each question with:
  - The gap/discrepancy it targets
  - Video timestamp reference
  - Report page/Bate stamp reference
  - Expected response and follow-up]

SECTION 11: DEFENSE ACTION ITEMS
[Prioritized:
 - Motions to file
 - Missing Discovery Demand items (missing videos,
   missing metadata, missing policies)
 - Expert witness needs
 - Independent video analysis requests
 - Items for Cross-Exam Architect skill]

SECTION 12: DISCOVERY GAP REPORT
[Expected video documentation not provided:
 Each with: what's missing, why it matters,
 recommended action]

APPENDIX A: COMPLETE TIMESTAMP LOGS
[If not included in Section 4]

APPENDIX B: CROSS-EXAM CHAPTER SEEDS
[Formatted for dw-cross-exam-architect-crim integration]

APPENDIX C: AGENCY BWC POLICY EXCERPTS
[Relevant policy sections with violation annotations]
```

## Severity Classification
Tag every finding:

- **CRITICAL:** Directly undermines the reliability or admissibility of the video evidence, or reveals a significant discrepancy between the video and the prosecution's narrative. Supports a motion or creates substantial reasonable doubt. Examples: key event occurs during an activation gap; officer's report describes events that are contradicted by the video; video evidence deleted or overwritten.
- **SIGNIFICANT:** Weakens evidentiary value or reveals procedural failures that provide strong cross-examination material. Examples: BWC not activated per policy but video from another source partially covers the gap; minor timeline discrepancies between video and reports; audio gaps during critical statements.
- **MINOR:** Procedural irregularity that may affect weight but does not independently undermine the evidence. Examples: brief activation delay at scene arrival; minor metadata documentation gaps; CCTV timestamp off by seconds rather than minutes.

---

## Moved from SKILL.md — Step 4 summary

Produce the audit as a **Word document (.docx)** using the docx skill. Read and follow the `docx` SKILL.md for all formatting and generation instructions. The report follows a fixed twelve-section structure (Executive Summary, Video Inventory, Activation & Coverage Analysis, Timestamp Logs, Content-vs-Report Discrepancies, Report-vs-Recording Matrix, Technical Limitations, Authentication & Metadata, Policy Compliance, Admissibility Challenges, Cross-Exam Questions, Defense Action Items, Discovery Gap Report) plus three appendices (Complete Timestamp Logs, Cross-Exam Chapter Seeds, Agency BWC Policy Excerpts).
