# Information Gathering Protocol — Ranked Intake List

Read at Step 1 — the ranked Essential / Strategic / Contextual list of inputs to collect before generating the workplan.

### Essential (must have before generating workplan)

1. **Report 4a -- Theory Selection Memo:** The attorney's selected defense theory with supporting rationale. This is the mandatory prerequisite. If Report 4a does not exist, STOP and route to `dw-criminal-defense-crim` Report 4 for theory development. Do not generate a workplan without an attorney-selected theory.
2. **Charges:** All counts with statutory citations -- the charge architecture determines which streams need the most attention.
3. **Trial date (or next critical hearing date):** All task deadlines are calculated relative to this date. If no trial date is set, use the next hearing date and flag all deadlines as provisional.
4. **Case Brain:** Read from `dw-case-brain-crim` for structured case context -- defendant demographics, docket, parish, court, judge, ADA, discovery status, and companion skill outputs already completed.

### Strategic (request if not provided)

5. **Reports 1-8 + 4a (Barone Discovery Workflow):** The full analytical output from `dw-criminal-defense-crim` Phase 2 -- Comprehensive Case Timeline (Report 1), Prosecution's Case Summary (Report 2), Theory Deconstruction (Report 2a from `dw-theory-deconstructor-crim`), Immediate Red Flags (Report 3), Competing Defense Theories (Report 4), Theory Selection Memo (Report 4a), Viable Legal Defenses (Report 5), Memorable Theme (Report 6), Table of Missing Discovery (Report 7), Key Witness Impeachment Plan (Report 8). Plus Report 0 (Neutral Discovery Inventory from `dw-neutral-inventory-crim`).
6. **All completed audit reports:** Brady/Giglio audit, mobile forensic audit, chain of custody audit, crime scene audit, eyewitness ID audit, confession/interrogation audit, expert witness evaluation, DNA audit, crime lab audit, video evidence audit, jail call analysis, social media audit -- any audit that has been run feeds task generation.
7. **Case Tables.xlsx:** Evidence Table, Witness List, Timeline -- these are the structured data that seed tasks.
8. **Discovery compliance ledger:** Outstanding discovery items from `dw-discovery-compliance-monitor-crim` feed Stream 2 tasks directly.

### Contextual (gather from uploaded files)

9. **Budget and resource constraints:** Is this a public defender case with limited investigator hours? A retained case with expert budget? Resource constraints affect task prioritization and responsible-party assignment.
10. **Co-defendant posture:** Severance, joint defense, cooperator -- affects witness prep, motion practice, and discovery strategy.
11. **Prior workplan versions:** If this is an update, load the prior workplan to preserve completed tasks and track status changes.

**Present missing essential items as a hard stop. Present missing strategic items as a ranked request list before generating.**
