# Integration with the D&W Skill Ecosystem

Read whenever a step reads from, invokes, or writes to another DW skill or external system (Case Brain, DEVONthink, Google Calendar).

### Reads From:
- **dw-case-brain-crim:** Full case history, preliminary disposition status
- **dw-case-dashboard-crim:** Case critical dates, final status
- **dw-appellate-error-monitor-crim:** Error preservation log (for appeal assessment in Step 4)

### Invokes:
- **dw-billing-narrative-generator-crim** (Step 2): Captures all unbilled work across case lifecycle
- **dw-client-communication-drafter-crim** (Step 3): Drafts disposition-specific client letters
- **dw-appellate-error-monitor-crim** (Step 4): Optional appeal viability assessment
- **dw-sentencing-mitigation-specialist-crim** (Step 3): Custody client good-time calculations
- **dw-pretrial-motion-library-crim** (Step 5): Optional expungement motion draft
- **dw-criminal-defense-crim** (Step 6, Phase 1 Step 3): LWOP review sheet completion via `000 - Case Profile.docx` Part 2A (Homicide) or 2B (Sex Offense), if applicable — formerly the dw-lwop-populator skill, merged into the master workflow in v5.3
- **dw-habitual-offender-auditor-crim** (Step 6): Habitual offender audit (if applicable)
- **docx** skill: Case closing checklist generation
- **xlsx** skill: Final billing summary workbook

### Writes To:
- **Case Brain:** Final disposition type, dates, sentence, appeal/expungement deadlines
- **Case Folder:** Closing checklist, billing summary, expungement memo, archive summary
- **DEVONthink:** Archive tags (if available)
- **Google Calendar:** Appeal deadline, expungement eligibility reminder, file destruction deadline

### Uses:
- **docx skill** for closing checklist
- **xlsx skill** for final billing summary
- **Google Calendar API** for deadline tracking
- **DEVONthink MCP** for archive tagging (if available)
