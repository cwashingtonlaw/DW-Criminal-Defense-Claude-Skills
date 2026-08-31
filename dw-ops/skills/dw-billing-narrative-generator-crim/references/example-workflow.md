# Example Workflow — Session to Billing Entries

Read at the Example Workflow section of `dw-billing-narrative-generator-crim` when a worked end-to-end example (Steps 1 through 5) is needed; moved verbatim from SKILL.md.

**Scenario:** Attorney completes a session involving suppression motion drafting, discovery review, and Brady analysis.

1. **STEP 1 — Session Work Inventory**
   - dw-suppression-motion-crim invoked at 2:15 PM, completed 4:00 PM (1.75 hours)
   - dw-brady-giglio-auditor-crim invoked at 4:05 PM, completed 5:15 PM (1.25 hours)
   - dw-discovery-compliance-monitor-crim invoked at 1:30 PM, completed 2:10 PM (0.67 hours)
   - No duplicates identified

2. **STEP 1A — Deduplication Check**
   - Each skill invoked once with distinct subject matter
   - No consolidation needed
   - Proceed to mapping
3. **STEP 2 — Map to Billing Categories**
   - dw-suppression-motion-crim → L200.1 (Motion Drafting)
   - dw-brady-giglio-auditor-crim → L160.3 (Brady/Giglio Review)
   - dw-discovery-compliance-monitor-crim → L160.2 (Discovery Compliance Audit)

4. **STEP 3 — Generate Narratives** (Standard option shown)

   **Entry 1:**
   - Skill: dw-suppression-motion-crim
   - Time: 1.75 hours
   - LEDES Code: L200.1
   - Narrative: "Drafted Fourth Amendment suppression motion challenging warrantless vehicle search. Reviewed case law on vehicle exception to warrant requirement. Incorporated factual analysis from police reports and witness statements."

   **Entry 2:**
   - Skill: dw-brady-giglio-auditor-crim
   - Time: 1.25 hours
   - LEDES Code: L160.3
   - Narrative: "Conducted Brady/Giglio audit of prosecution discovery materials. Reviewed police reports and witness statements for material exculpatory information and witness credibility issues. Prepared summary for case file."

   **Entry 3:**
   - Skill: dw-discovery-compliance-monitor-crim
   - Time: 0.67 hours
   - LEDES Code: L160.2
   - Narrative: "Updated discovery compliance ledger with received police reports and digital evidence. Cross-referenced with case inventory to ensure all materials logged and tracked."
5. **STEP 4 — Present for Attorney Review**

   Summary displayed:
   ```
   Session: 2026-04-06 | Case: State v. Williams, 2025-CR-08847
   Total Hours (before approval): 3.67

   | Skill | Hours | Code | Narrative | Action |
   |-------|-------|------|-----------|--------|
   | dw-suppression-motion-crim | 1.75 | L200.1 | [Narrative] | [Approve] |
   | dw-brady-giglio-auditor-crim | 1.25 | L160.3 | [Narrative] | [Approve] |
   | dw-discovery-compliance-monitor-crim | 0.67 | L160.2 | [Narrative] | [Approve] |
   ```

   Attorney reviews, approves all three entries without modification.

6. **STEP 5 — Output Options**

   System generates:
   - XLSX: `/case-root/05 - Billing/Williams - Time Entries - 2026-04-06.xlsx`
   - CSV: `/case-root/05 - Billing/Williams - Time Entries - 2026-04-06.csv`
   - PDF: `/case-root/05 - Billing/Williams - Time Entries - 2026-04-06.pdf`

   Attorney selects XLSX export for import into Clio practice management system.
