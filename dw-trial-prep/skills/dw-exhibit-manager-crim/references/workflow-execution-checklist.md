# Workflow Execution Checklist

Read at WORKFLOW EXECUTION CHECKLIST of `dw-exhibit-manager-crim/SKILL.md` — the three-phase checkbox list, moved verbatim from SKILL.md.

---

Use this checklist to ensure complete exhibit management:

**PRE-TRIAL PHASE:**
- [ ] Invoked dw-case-brain-crim for case context and trial date
- [ ] Checked with dw-trial-notebook-builder-crim for existing exhibit list
- [ ] Confirmed trial date, court, judge, and judge's exhibit marking preference with attorney
- [ ] Confirmed scope: pre-trial only, live trial only, or both
- [ ] Completed STEP 1 — Exhibit Inventory (all documentary, visual, digital, expert, demonstrative exhibits identified)
- [ ] Cross-referenced dw-discovery-compliance-monitor-crim for authentication issues
- [ ] Completed STEP 2 — Pre-mark all exhibits with exhibit cards (all columns populated)
- [ ] Completed STEP 3 — Authentication chain tracking (foundation questions, witness ID, hearsay exceptions noted)
- [ ] Completed STEP 4 — Prepared for live trial (attorney briefed on exhibit offer procedures)
- [ ] Generated OUTPUTS:
  - [ ] Master Exhibit List (.xlsx) with all columns and separate sheets (Defense, State, Joint, Excluded)
  - [ ] Authentication Checklist (.docx) ready for counsel table
  - [ ] Objection Log template (.xlsx) prepared
  - [ ] Clerk's Exhibit List template (.docx) prepared

**LIVE TRIAL PHASE (if applicable):**
- [ ] Attorney provides exhibit offer, objection, and ruling information in real-time
- [ ] Update exhibit status for each offered exhibit (Offered → Objected → Ruled → Admitted/Excluded)
- [ ] Log all evidentiary objections in Objection Log with basis and ruling
- [ ] For every sustained objection: AUTOMATICALLY flag to dw-appellate-error-monitor-crim
- [ ] Track limiting instructions from court
- [ ] Update Master Exhibit List with trial status (actual ruling column)

**POST-TRIAL PHASE:**
- [ ] Finalize Objection Log with all trial objections
- [ ] Finalize Clerk's Exhibit List with court rulings
- [ ] Generate Excluded Exhibits sheet (all ruled inadmissible)
- [ ] Feed all sustained objections to dw-appellate-error-monitor-crim
- [ ] Update dw-case-brain-crim with exhibit admission/exclusion summary
- [ ] Prepare trial notebook package for dw-trial-notebook-builder-crim
- [ ] File Clerk's Exhibit List with clerk of court (if required by local rule)
