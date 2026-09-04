---
name: dw-theory-to-workplan-crim
category: trial-prep
description: >
  ALWAYS invoke for "build a workplan," "theory to workplan," "action plan from theory,"
  "what do we need to do," "task list for trial," "work streams," "prep plan," or
  "explode the theory." Requires Report 4a (Theory Selection Memo) as input.
  Do NOT use for theory development — use dw-criminal-defense-crim Report 4.
  Do NOT use for stress-testing — use dw-adversarial-stress-test-crim.
---

# D&W Theory-to-Workplan Orchestrator
**Daniels & Washington | Criminal Defense | Louisiana / 5th Circuit Default**

This skill takes the attorney's selected defense theory (from Report 4a -- Theory Selection Memo) and generates a comprehensive, 7-stream action plan covering every domain of trial preparation. Each stream maps to a specific preparation domain, and every task within each stream is concrete, delegatable, and linked to the D&W skill that can execute it. The workplan is a living document -- it is updated as the case evolves, new discovery arrives, or the attorney redirects strategy.

The 7 streams are: (1) Investigation Tasks, (2) Discovery Actions, (3) Expert Witness Needs, (4) Motion Practice, (5) Witness Preparation, (6) Exhibit & Evidence Strategy, (7) Narrative & Theme Development. Together they translate a strategic choice into tactical execution across every axis of trial readiness.

**Cowork drafts; attorney approves.** The workplan is a recommendation for attorney review, not a directive. The attorney prioritizes, reassigns, and approves every task before it is executed.

---

## STEP 0 -- FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any case files, discovery, reports, or the Theory Selection Memo, do not analyze anything yet.**

Your only response must be:
> *"Before I begin -- are you uploading any additional case files, discovery documents, audit reports, or the Theory Selection Memo (Report 4a)? I'll start the workplan only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** The workplan must account for every known case fact, every completed audit, and every outstanding discovery gap. Mid-build discovery of additional reports or audit findings would require restructuring tasks, reprioritizing streams, and recalculating deadlines across all seven streams.

---

## STEP 0.5 -- LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` -- apply work product marking to all deliverable headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` -- use for all output file paths (anchored on `{{CASE_ROOT}}`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product -- apply marking per the shared protocol. Output paths follow the Cowork Analysis formula:

```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/
```

If any required Case Brain variable (`{{DEFENDANT_NAME}}`, `{{DOCKET}}`, `{{PARISH}}`, `{{COURT}}`, `{{JUDGE_NAME}}`, `{{ADA_NAME}}`, `{{TRIAL_DATE}}`) is missing, prompt the attorney before drafting. Trial date is particularly critical for this skill -- all task deadlines are calculated relative to it.

---

### Source Citation Mandate

Every task in the workplan must trace to a specific case fact or legal requirement that justifies its inclusion. The workplan is a derivative of the defense theory, which is itself grounded in discovery. Unsourced tasks waste investigator time, attorney hours, and budget.

**Citation format:** Cite the source that makes this task necessary. Examples:
- `(Report 4a -- Theory Selection Memo, p. 3, "Self-defense theory requires proof of victim's prior aggression")`
- `(BWC_Officer_Smith_2024-03-12.mp4 at 03:42 -- officer admits no Miranda warning given)`
- `(Discovery Gap -- no autopsy toxicology results produced; demanded 2026-02-15)`
- `(Report 2 -- Evidence Audit, p. 7, "Cell site records not yet subpoenaed")`
- `(La. C.Cr.P. Art. 703 -- suppression motion must be filed pretrial)`
- `(Report 4a Theory Selection Memo, "Consent voluntariness contested")`

**Unsourced tasks:** If a task cannot be tied to a specific case fact or legal requirement, mark it `[UNSOURCED -- VERIFY NECESSITY]` so the attorney can confirm or remove it before resources are committed.

---

## STEP 1 -- Information Gathering Protocol

Before generating the workplan, collect the following in ranked order:

Collect inputs in three ranked tiers: **Essential** (Report 4a Theory Selection Memo — mandatory, STOP and route to `dw-criminal-defense-crim` Report 4 if absent; charges; trial date or next critical hearing date; Case Brain), **Strategic** (Reports 0–8 + 4a, all completed audit reports, Case Tables.xlsx, discovery compliance ledger), and **Contextual** (budget/resource constraints, co-defendant posture, prior workplan versions). Read `references/information-gathering-protocol.md` now for the full ranked list with what each item feeds.

**Present missing essential items as a hard stop. Present missing strategic items as a ranked request list before generating.**

---

## STEP 2 -- WORKPLAN GENERATION: THE 7 STREAMS

For each stream, generate tasks based on the selected defense theory, the case facts, and the current state of case preparation. Every task follows a standard format (see Step 2.1 below).

### STEP 2.1 -- Standard Task Format

Every task in every stream carries the same eleven fields (Task ID, Task Description, Theory Link, Source, Priority, Responsible Party, D&W Skill, Deadline, Dependencies, Status, Notes) and one of four priority tiers (CRITICAL / HIGH / MEDIUM / LOW, each with a defined timing window relative to trial). Read `references/task-format-and-priority.md` now for the full field table and the priority definitions.

---

### MODULE A -- STREAM 1: Investigation Tasks

What facts need to be verified, investigated, or developed to support or test the selected theory?

Generate tasks from the Module A task-category checklist. Read `references/stream-modules.md` now for the Module A task categories (and for Modules A–G together if building all streams in one pass).

**Routing:** Generate tasks and route to `dw-defense-investigator-tasking-crim` for investigator assignment and tracking.

---

### MODULE B -- STREAM 2: Discovery Actions

What additional discovery is needed to support or test this theory? What discovery deficiencies must be resolved?

Generate tasks from the Module B task-category checklist. Read `references/stream-modules.md` now for the Module B task categories (and for Modules A–G together if building all streams in one pass).

**Routing:** Route discovery ledger tasks to `dw-discovery-compliance-monitor-crim`. Route Brady/Giglio demands to `dw-brady-giglio-auditor-crim`. Route motions to compel to `dw-pretrial-motion-library-crim`.

---

### MODULE C -- STREAM 3: Expert Witness Needs

What expert testimony is needed to support this theory? What prosecution experts need to be challenged?

Generate tasks from the Module C task-category checklist. Read `references/stream-modules.md` now for the Module C task categories (and for Modules A–G together if building all streams in one pass).

**Routing:** Route expert evaluations to `dw-expert-witness-evaluator-crim`. Route indigent expert funding motions to `dw-pretrial-motion-library-crim`.

---

### MODULE D -- STREAM 4: Motion Practice

What pretrial motions support this theory? What motions must be filed to exclude harmful evidence or preserve favorable evidence?

Generate tasks from the Module D task-category checklist. Read `references/stream-modules.md` now for the Module D task categories (and for Modules A–G together if building all streams in one pass).

**Routing:** Route all motions to `dw-pretrial-motion-library-crim` for template selection and drafting. Route suppression motions to `dw-suppression-motion-crim`. Route 404(b) work to `dw-404b-opposition-crim`.

---

### MODULE E -- STREAM 5: Witness Preparation

Which witnesses need to be prepared? What testimony supports the theory? What cross-examination themes align with the theory?

Generate tasks from the Module E task-category checklist. Read `references/stream-modules.md` now for the Module E task categories (and for Modules A–G together if building all streams in one pass).

**Routing:** Route cross-examination work to `dw-cross-exam-architect-crim`. Route direct-examination work to `dw-direct-exam-architect-crim`.

---

### MODULE F -- STREAM 6: Exhibit & Evidence Strategy

What exhibits support the theory? What demonstratives need to be created? What evidence authentication issues must be resolved?

Generate tasks from the Module F task-category checklist. Read `references/stream-modules.md` now for the Module F task categories (and for Modules A–G together if building all streams in one pass).

**Routing:** Record exhibit metadata on the `Case Tables.xlsx` Evidence Table; route live trial-day exhibit status to `dw-trial-day-assistant-crim` Module D. Route trial notebook assembly to `dw-trial-notebook-builder-crim`.

---

### MODULE G -- STREAM 7: Narrative & Theme Development

How does the theory translate into the courtroom story? What is the memorable theme? How does every piece of the trial reinforce that theme?

Generate tasks from the Module G task-category checklist. Read `references/stream-modules.md` now for the Module G task categories (and for Modules A–G together if building all streams in one pass).

**Routing:** Route narrative work to `dw-trial-narrative-builder-crim`. Route jury instruction work to `dw-jury-instructions-builder-crim`. Route voir dire work to `dw-voir-dire-assistant-crim`.

---

## STEP 3 -- WORKPLAN SUMMARY DASHBOARD

After generating all seven streams, produce a summary dashboard at the top of the workplan document:

The dashboard carries seven components: Theory Summary, Trial Date (with days remaining), Task Count by Stream table, Critical Path, Blocked Tasks, Immediate Action Items, and Budget & Resource Summary. Read `references/summary-dashboard.md` now for the full dashboard contents and the stream-count table.

---

## STEP 4 -- OUTPUT FORMAT

### Primary Deliverable: Theory-to-Workplan (.docx)

Filename: `Theory to Workplan - {{DEFENDANT_LAST}} - {{YYYY-MM-DD}}.docx`

Location: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

**Document structure:** 13 sections — work-product header, case caption block, selected defense theory, summary dashboard, the seven stream task tables (Modules A–G), cross-stream dependencies map, and revision history. Read `references/output-format-and-registration.md` now for the full document structure.

### Secondary Deliverable: Summary Checklist (Apple Notes)

Push a condensed checklist of all CRITICAL and HIGH priority tasks to Apple Notes via the same mechanism used by `dw-criminal-defense-crim` Phase 2 Step 6. Read `references/output-format-and-registration.md` now for the checklist format.

### Case Brain Registration

Register the workplan output with `dw-case-brain-crim` per Contract 5 in `dw-data-contracts-crim`, and update the Case Brain's OPEN ISSUES section with any BLOCKED tasks. Read `references/output-format-and-registration.md` now for the exact registration line.

---

## CROSS-SKILL INTEGRATION

This skill REQUIRES Report 4/4a from `dw-criminal-defense-crim`; READS FROM the Case Brain, Reports 0–8 + 4a, the discovery compliance ledger, Brady/Giglio findings, all completed audit reports, and Case Tables.xlsx; ROUTES each stream to its executing D&W skill; and WRITES TO the workplan document, the Apple Notes checklist, and the Case Brain. Read `references/cross-skill-integration.md` now for the prerequisite list, upstream reads, the stream-to-skill routing table, and downstream writes.

---

## Guardrails

1. **Requires attorney-selected theory.** Do not generate a workplan without Report 4a (Theory Selection Memo) containing the attorney's selected defense theory. If Report 4a does not exist or does not contain a clear theory selection, STOP and route to `dw-criminal-defense-crim` Report 4 for theory development. A workplan without a theory is a to-do list without a strategy.

2. **Source Citation Mandate.** Every task must trace to a case fact or legal requirement. Tasks that cannot be sourced are marked `[UNSOURCED -- VERIFY NECESSITY]` and flagged for attorney review. Do not generate speculative tasks disconnected from the case record.

3. **Mark verification status.** For every factual assertion drawn from discovery or audit reports, mark `[VERIFIED]` (confirmed against source document) or `[UNVERIFIED]` (cited from secondary source or memory -- needs confirmation). This is particularly important for tasks generated from audit report findings that the attorney has not yet reviewed.

4. **Cowork drafts; attorney approves.** The workplan is a recommendation, not a directive. Every task is a proposal for attorney review. The attorney assigns priority, approves responsible parties, sets deadlines, and directs execution. No task is executed without attorney approval.

5. **Living document.** The workplan must be updated when:
   - New discovery arrives (new tasks may be needed; existing tasks may be completed or mooted)
   - The attorney changes or refines the defense theory (tasks must be re-evaluated for relevance)
   - A task is completed, blocked, or deferred (status update)
   - Trial date changes (all deadlines recalculate)
   - An audit report produces new findings (new tasks generated)

   When updating, preserve the prior version's revision history. Do not overwrite -- append a new revision entry.

6. **Do not fabricate citations.** All case law, statutory references, and procedural rules cited in task justifications must be verifiable. Use anchor authorities (La. C.Cr.P., La. C.E., La. R.S.) and well-established precedent. For any Louisiana case citation that is not an anchor authority, mark `[VERIFY CITATION]`.

7. **Respect resource constraints.** If this is a public defender case, prioritize tasks that can be accomplished with limited investigator hours and no expert budget. Flag expert retention tasks that require La. C.Cr.P. Art. 725 indigent funding motions. Do not generate a wish list that ignores practical constraints.

8. **Cross-stream dependency integrity.** When a task in one stream depends on a task in another stream, the dependency must be explicit (by Task ID). Do not create tasks that assume another stream's work is complete without listing the dependency.

---

## Quick References

Skill-local reference files (read at the step named):

- **information-gathering-protocol.md** — Step 1; the ranked Essential / Strategic / Contextual intake list
- **task-format-and-priority.md** — Step 2.1; the eleven-field task table and CRITICAL/HIGH/MEDIUM/LOW priority definitions
- **stream-modules.md** — Step 2, Modules A–G; the full task-category checklists and routing for all seven streams
- **summary-dashboard.md** — Step 3; dashboard contents and the task-count-by-stream table
- **output-format-and-registration.md** — Step 4; .docx document structure, Apple Notes checklist format, Case Brain registration line
- **cross-skill-integration.md** — Cross-Skill Integration; prerequisites, upstream reads, stream-to-skill routing table, downstream writes

External reference documents consumed through other skills:

- **Report 4a (Theory Selection Memo)** -- mandatory input; produced by `dw-criminal-defense-crim` Report 4
- **dw-shared-protocols-crim/references/attorney-work-product-marking.md** -- work product marking for all deliverables
- **dw-shared-protocols-crim/references/output-path-formula.md** -- output path anchored on `{{CASE_ROOT}}`
- **dw-data-contracts-crim/SKILL.md** -- Contract 5 (Case Brain Registration) for registering output

---

*This skill is part of the Daniels & Washington criminal defense toolkit -- Barone Discovery Workflow. It bridges strategic theory selection (Report 4a) and tactical trial preparation across all seven preparation domains. Pair with `dw-adversarial-stress-test-crim` to stress-test the theory before committing resources to the workplan, and with `dw-case-brain-crim` for ongoing status tracking and case context.*
