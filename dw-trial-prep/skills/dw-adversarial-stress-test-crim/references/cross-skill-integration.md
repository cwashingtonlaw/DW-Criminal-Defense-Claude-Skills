# Cross-Skill Integration — Prerequisites, Inputs, Outputs, Pairings

Read at the **Cross-Skill Integration** section (after Step 3) — what this skill requires, reads from, feeds, and pairs with.

---

### This skill REQUIRES (prerequisite):
- `dw-criminal-defense-crim` Phase 2 Step 2 -- Reports 1-8 must exist.
- Report 4a (Theory Selection Memo) -- the attorney's selected defense theory. Without this, the stress test has no target.
- Report 2a (Theory Deconstruction) -- the vulnerability baseline from `dw-theory-deconstructor-crim`.

### This skill READS FROM:
- `dw-case-brain-crim` -- structured case context, prior analysis, Case Tables.
- `dw-theory-deconstructor-crim` -- Report 2a vulnerability analysis (the starting point for Module A).
- Reports 1-8 (Phase 2 Case Analysis) -- evidence inventory, timeline, prosecution summary, impeachment plan.
- All evidence audit reports -- forensic, identification, confession, Brady/Giglio, jail call, crime scene, mobile forensic findings.
- `dw-expert-witness-evaluator-crim` -- expert vulnerability assessments.
- Case Tables.xlsx -- Evidence Table, Witness List, Timeline Sheet.

### This skill FEEDS:
- `dw-theory-to-workplan-crim` -- vulnerabilities from Module G create new tasks in Stream 5 (witness preparation), Stream 3 (motion practice), and other workplan streams. The Priority Preparation Checklist maps directly to workplan task entries.
- `dw-trial-narrative-builder-crim` -- Module E (Defense Counter-Response Matrix) feeds the Rebuttal Anticipation Memo. The narrative builder uses the counter-responses to build preemptive narrative elements into the defense story.
- `dw-cross-exam-architect-crim` -- Module B (Prosecution Cross-Examination Simulation) identifies the hardest questions defense witnesses will face; the cross-exam architect uses these to build witness preparation outlines.
- `dw-voir-dire-assistant-crim` -- Module F (Jury Perception Risk Assessment) identifies jury-perception risks that inform voir dire focus areas and juror-profile criteria.
- `dw-case-brain-crim` -- stress test completion status, top-5 summary, routing tasks.

### This skill PAIRS WITH:
- `dw-theory-deconstructor-crim` -- deconstructor identifies structural weaknesses; this skill tests those weaknesses under adversarial fire.
- `dw-trial-narrative-builder-crim` -- narrative builder constructs the affirmative story; this skill identifies where the story breaks under attack.
