# Integration Notes: dw-theory-to-workplan

## Role in the Barone Discovery Workflow

`dw-theory-to-workplan` is the bridge between strategic decision and tactical execution. It sits at the inflection point in the Barone Discovery Workflow where the attorney has completed the analytical phase (Reports 1-9) and selected a defense theory (Report 4a), and now needs to convert that choice into concrete, delegatable work across every domain of trial preparation.

Without this skill, the attorney has a theory but no systematic way to identify every task that theory demands. With it, the theory is "exploded" into 7 streams covering investigation, discovery, experts, motions, witnesses, exhibits, and narrative -- each stream populated with tasks that trace back to specific case facts.

---

## Dependency on Report 4a (Theory Selection Memo)

This skill has a hard prerequisite: **Report 4a (Theory Selection Memo) must exist with the attorney's selected defense theory.** The skill will not generate a workplan without it.

Report 4a is produced by `dw-criminal-defense` Phase 2 Report 4. The typical flow is:

1. `dw-criminal-defense` Phase 2 generates Reports 1-9, including Report 4 (Defense Theory Development), which presents multiple candidate theories.
2. The attorney reviews Report 4 and selects the theory to pursue.
3. Report 4a (Theory Selection Memo) is created, documenting the selected theory and the attorney's rationale.
4. `dw-theory-to-workplan` consumes Report 4a and generates the 7-stream action plan.

If the attorney has not yet selected a theory, this skill stops and routes back to `dw-criminal-defense` Report 4. If the attorney wants to stress-test the theory before committing resources, route to `dw-adversarial-stress-test` first, then return here after the theory survives scrutiny.

---

## How It Routes to Downstream Skills

The workplan is an orchestrator -- it generates tasks but does not execute them. Each task is tagged with the D&W skill that should execute it. The routing table:

| Stream | Downstream Skill(s) | What Flows |
|--------|---------------------|-----------|
| 1 - Investigation | `dw-defense-investigator-tasking` | Witness interview lists, scene visits, record subpoenas, fact verification tasks |
| 2 - Discovery | `dw-discovery-compliance-monitor` | New discovery demands, outstanding item escalation |
| 2 - Discovery | `dw-brady-giglio-auditor` | Theory-specific Brady/Giglio demands |
| 2 - Discovery | `dw-pretrial-motion-library` | Motions to compel for outstanding critical items |
| 3 - Expert | `dw-expert-witness-evaluator` | Prosecution expert evaluation requests, Daubert/Foret challenge seeds |
| 3 - Expert | `dw-pretrial-motion-library` | Indigent expert funding motions (La. C.Cr.P. Art. 725) |
| 4 - Motions | `dw-suppression-motion` | Constitutional suppression motions (4th/5th/14th Amendment) |
| 4 - Motions | `dw-404b-opposition` | Prieur notice opposition |
| 4 - Motions | `dw-pretrial-motion-library` | All other pretrial motions (severance, limine, bill of particulars, etc.) |
| 5 - Witnesses | `dw-cross-exam-architect` | Cross-examination outlines for prosecution witnesses |
| 5 - Witnesses | `dw-direct-exam-architect` | Direct-examination outlines for defense witnesses |
| 6 - Exhibits | `dw-exhibit-manager` | Exhibit identification, preparation, authentication planning |
| 6 - Exhibits | `dw-trial-notebook-builder` | Trial notebook assembly with theory-aligned organization |
| 7 - Narrative | `dw-trial-narrative-builder` | Opening statement, closing argument, theme tracker |
| 7 - Narrative | `dw-jury-instructions-builder` | Theory-specific jury charges and verdict form requests |
| 7 - Narrative | `dw-voir-dire-assistant` | Theory-aligned voir dire questions |

The routing is one-directional: this skill generates tasks and points to the skill that should execute each one. The downstream skill receives the task context (case facts, theory link, source citation) and produces its own deliverable per its own standard pattern.

---

## Integration with dw-case-brain for Status Tracking

The workplan integrates with `dw-case-brain` in three ways:

### 1. Reads case context on build

Before generating the workplan, the skill reads from `dw-case-brain` to pull:
- Defendant demographics, docket, parish, court, judge, ADA
- Trial date (critical for deadline calculation)
- Companion skill outputs already completed (to avoid duplicating tasks for work already done)
- Open issues (to incorporate into the workplan as tasks)

### 2. Registers output after build

After generating the workplan, the skill registers its output with Case Brain per Contract 5 in `dw-data-contracts`:

```
- **[Date]** | `dw-theory-to-workplan` | Theory to Workplan - [Client Last Name] - [Date].docx | 01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/
```

### 3. Updates OPEN ISSUES on refresh

When the workplan is updated (living document), any BLOCKED tasks are written to the Case Brain's OPEN ISSUES section so they surface in case status reviews:

```
- [ ] [S2-003] Motion to compel cell site records -- BLOCKED on State response to demand letter (30 days) -- from `dw-theory-to-workplan` (2026-05-28)
```

This creates a feedback loop: Case Brain tracks what has been done, the workplan tracks what needs to be done, and BLOCKED items surface in both places so nothing falls through the cracks.

---

## Living Document Protocol

The workplan is not a one-shot deliverable. It is designed to be updated throughout the life of the case:

- **New discovery arrives** -- new tasks may be needed; existing tasks may be completed or mooted
- **Attorney changes theory** -- all tasks re-evaluated for relevance to the new theory
- **Task completed** -- status updated from NOT STARTED/IN PROGRESS to COMPLETE
- **Task blocked** -- status updated to BLOCKED with reason; BLOCKED tasks pushed to Case Brain OPEN ISSUES
- **Trial date changes** -- all relative deadlines recalculate
- **Audit report produces new findings** -- new tasks generated in the relevant stream

Each update preserves the prior version's revision history. The workplan document includes a Revision History section at the end for tracking changes across updates.

---

## Relationship to Adjacent Skills

| Skill | Relationship |
|-------|-------------|
| `dw-criminal-defense` Report 4/4a | **Upstream producer** -- provides the selected theory that seeds the workplan |
| `dw-adversarial-stress-test` | **Parallel** -- stress-tests the theory; should run before this skill commits resources |
| `dw-case-brain` | **Bidirectional** -- reads context, writes output registration and BLOCKED issues |
| `dw-case-dashboard` | **Consumer** -- can read workplan status for case-level reporting |
| `dw-trial-notebook-builder` | **Consumer** -- the completed workplan tasks feed trial notebook assembly |
