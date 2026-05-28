# Integration Notes — dw-neutral-inventory (Report 0)

## Position in the Barone Discovery Workflow

Report 0 sits between Phase 1 (case intake and file organization) and Phase 2 (case analysis and the 8 analytical reports). The sequence is:

1. **Phase 1** — Case folder creation, document organization, Bate stamping, Case Profile, Case Tables population
2. **Report 0 (dw-neutral-inventory)** — Pre-strategic neutral catalog of ALL discovery materials
3. **Phase 2** — Reports 1-8 (timeline, prosecution summary, red flags, defense narrative, legal defenses, theme, missing discovery, impeachment plan)
4. **dw-theory-deconstructor** — Tests proposed defense theories against the complete evidence record
5. **dw-theory-to-workplan** — Converts validated theories into actionable investigation and litigation tasks
6. **dw-adversarial-stress-test** — Stress-tests the defense case from the prosecution's perspective

Report 0 is the bridge between organizing the file and analyzing it. Phase 1 answers "where is everything?"; Report 0 answers "what do we have?"; Phase 2 answers "what does it mean?"

## How dw-criminal-defense Phase 2 should reference Report 0

Phase 2 Step 2 (the 8 Case Analysis Reports) should consume Report 0 as a prerequisite input. Recommended integration:

- **Before generating any of the 8 reports**, check whether Report 0 exists in the Cowork Analysis folder. If it does, load it as the evidence baseline. If it does not, either generate it first or proceed with the existing triage routing memo (Step 1A) while noting that a neutral inventory was not performed.

- **Report 1 (Comprehensive Case Timeline)** — Use Report 0's document dates, media timestamps, and event references as the starting extraction list. Report 0 has already identified every document and its date; Report 1 extracts the timeline events from those documents.

- **Report 3 (Immediate Red Flags)** — Use Report 0's Completeness Flags (Module E) as a starting point. Items flagged as "referenced but not produced" may contain red flag material.

- **Report 7 (Table of Missing Discovery)** — Report 0's Completeness Flags directly seed Report 7. Every Module E flag is a candidate for the missing discovery table. The difference: Report 0 flags observationally ("this appears absent"); Report 7 analyzes whether the absence constitutes a discovery violation and recommends demand letter items.

- **All reports** — Report 0's Witness Roster (Module D) provides the definitive list of persons involved. Reports should cross-reference against this roster rather than building their own person lists from scratch.

## How dw-discovery-compliance-monitor can cross-reference Report 0

The discovery compliance monitor maintains a living ledger of demanded vs. produced items. Report 0 provides two key inputs:

1. **Module E (Completeness Flags)** — Every flag in the neutral inventory is a candidate entry for the compliance ledger. The compliance monitor adds the legal overlay: was this item demanded? Is the State obligated to produce it? What is the deadline? Has a motion to compel been filed?

2. **Module A-C (Document/Media/Physical Evidence Catalogs)** — The compliance monitor can cross-reference its production tracking against Report 0's catalog to verify that items marked "produced" in the ledger actually appear in the case file.

3. **Module F (Verification Status)** — Items marked [UNVERIFIED] in Report 0 may indicate items that were supposedly produced but were not accessible or reviewable. The compliance monitor should track these as potential production issues.

The compliance monitor should be run after Report 0 is complete, or updated with Report 0 findings when the inventory is produced for an existing case.

## Skill index update

The skill index (dw-skill-index/SKILL.md) needs to be updated to include dw-neutral-inventory in the routing table. Recommendation 10 of the Barone workflow changes handles this — the index regeneration script (`bin/regen-skill-index.py`) should pick up the new skill from its frontmatter automatically. If the index is hand-maintained, add an entry under the "analysis" or "discovery" category with trigger phrases: "neutral inventory," "discovery inventory," "catalog the evidence," "what do we have," "Report 0," "pre-strategic inventory," "Barone inventory," "list all discovery."

https://claude.ai/code/session_01LvMmvCHjdL1zGQA6oq8YBk
