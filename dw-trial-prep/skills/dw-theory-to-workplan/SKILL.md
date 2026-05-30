---
name: dw-theory-to-workplan-crim
category: trial-prep
description: >
  ALWAYS invoke for "build a workplan," "theory to workplan," "action plan from theory,"
  "what do we need to do," "task list for trial," "work streams," "prep plan," or
  "explode the theory." Requires Report 4a (Theory Selection Memo) as input.
  Do NOT use for theory development — use dw-criminal-defense Report 4.
  Do NOT use for stress-testing — use dw-adversarial-stress-test.
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

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` -- apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` -- use for all output file paths (anchored on `{{CASE_ROOT}}`)

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
- `(Case Tables.xlsx, Defense Matrix, "Consent voluntariness contested")`

**Unsourced tasks:** If a task cannot be tied to a specific case fact or legal requirement, mark it `[UNSOURCED -- VERIFY NECESSITY]` so the attorney can confirm or remove it before resources are committed.

---

## STEP 1 -- Information Gathering Protocol

Before generating the workplan, collect the following in ranked order:

### Essential (must have before generating workplan)

1. **Report 4a -- Theory Selection Memo:** The attorney's selected defense theory with supporting rationale. This is the mandatory prerequisite. If Report 4a does not exist, STOP and route to `dw-criminal-defense` Report 4 for theory development. Do not generate a workplan without an attorney-selected theory.
2. **Charges:** All counts with statutory citations -- the charge architecture determines which streams need the most attention.
3. **Trial date (or next critical hearing date):** All task deadlines are calculated relative to this date. If no trial date is set, use the next hearing date and flag all deadlines as provisional.
4. **Case Brain:** Read from `dw-case-brain` for structured case context -- defendant demographics, docket, parish, court, judge, ADA, discovery status, and companion skill outputs already completed.

### Strategic (request if not provided)

5. **Reports 1-8 + 4a (Barone Discovery Workflow):** The full analytical output from `dw-criminal-defense` Phase 2 -- Comprehensive Case Timeline (Report 1), Prosecution's Case Summary (Report 2), Theory Deconstruction (Report 2a from `dw-theory-deconstructor`), Immediate Red Flags (Report 3), Competing Defense Theories (Report 4), Theory Selection Memo (Report 4a), Viable Legal Defenses (Report 5), Memorable Theme (Report 6), Table of Missing Discovery (Report 7), Key Witness Impeachment Plan (Report 8). Plus Report 0 (Neutral Discovery Inventory from `dw-neutral-inventory`).
6. **All completed audit reports:** Brady/Giglio audit, mobile forensic audit, chain of custody audit, crime scene audit, eyewitness ID audit, confession/interrogation audit, expert witness evaluation, DNA audit, crime lab audit, video evidence audit, jail call analysis, social media audit -- any audit that has been run feeds task generation.
7. **Case Tables.xlsx:** Evidence Table, Timeline, Witness Sheet, Defense Matrix -- these are the structured data that seed tasks.
8. **Discovery compliance ledger:** Outstanding discovery items from `dw-discovery-compliance-monitor` feed Stream 2 tasks directly.

### Contextual (gather from uploaded files)

9. **Budget and resource constraints:** Is this a public defender case with limited investigator hours? A retained case with expert budget? Resource constraints affect task prioritization and responsible-party assignment.
10. **Co-defendant posture:** Severance, joint defense, cooperator -- affects witness prep, motion practice, and discovery strategy.
11. **Prior workplan versions:** If this is an update, load the prior workplan to preserve completed tasks and track status changes.

**Present missing essential items as a hard stop. Present missing strategic items as a ranked request list before generating.**

---

## STEP 2 -- WORKPLAN GENERATION: THE 7 STREAMS

For each stream, generate tasks based on the selected defense theory, the case facts, and the current state of case preparation. Every task follows a standard format (see Step 2.1 below).

### STEP 2.1 -- Standard Task Format

Every task in every stream includes these fields:

| Field | Description | Required |
|-------|-------------|----------|
| **Task ID** | Stream number + sequential (e.g., S1-001, S2-001) | Yes |
| **Task Description** | Concrete, actionable description of what must be done | Yes |
| **Theory Link** | How this task supports or tests the selected defense theory | Yes |
| **Source** | Case fact or legal requirement that makes this task necessary (per Source Citation Mandate) | Yes |
| **Priority** | CRITICAL / HIGH / MEDIUM / LOW (see priority definitions below) | Yes |
| **Responsible Party** | Attorney / Investigator / Expert / Paralegal / Cowork | Yes |
| **D&W Skill** | If Cowork-executable, the specific D&W skill to invoke | If Cowork |
| **Deadline** | Relative to trial date (e.g., T-60 days, T-30 days, T-7 days) or absolute date if trial date is set | Yes |
| **Dependencies** | Task IDs that must be completed before this task can begin | If any |
| **Status** | NOT STARTED / IN PROGRESS / COMPLETE / BLOCKED / DEFERRED | Yes |
| **Notes** | Additional context, attorney instructions, or strategic considerations | Optional |

### Priority Definitions

| Priority | Definition | Timing |
|----------|-----------|--------|
| **CRITICAL** | Theory collapses without this task. Must be completed or case cannot go to trial on this theory. | Immediate -- begin now |
| **HIGH** | Substantially strengthens or is necessary to the theory. Failure to complete materially weakens the defense. | T-60 days or sooner |
| **MEDIUM** | Supports the theory or addresses a secondary issue. Important but not theory-determinative. | T-30 days or sooner |
| **LOW** | Nice to have. Marginal improvement to the defense or addresses a contingency. | T-14 days or as time permits |

---

### MODULE A -- STREAM 1: Investigation Tasks

What facts need to be verified, investigated, or developed to support or test the selected theory?

**Task categories:**

1. **Witness interviews** -- Which witnesses need to be located and interviewed? What questions flow from the defense theory? Which witnesses have not yet been contacted?
   - Alibi witnesses (verify alibi timeline)
   - Occurrence witnesses (develop defense-favorable version)
   - Character witnesses (if character evidence is part of the theory)
   - Victim background witnesses (prior aggression, reputation for violence -- relevant to self-defense theories)

2. **Physical location visits** -- What scenes need to be visited, photographed, measured, or reconstructed?
   - Crime scene (lighting, sightlines, distances, access points)
   - Alibi locations (verify plausibility)
   - Surveillance camera canvass (identify cameras that may have captured relevant footage)

3. **Record subpoenas** -- What records need to be subpoenaed to support or test the theory?
   - Medical records (victim or defendant)
   - Employment records
   - Phone records (call logs, cell site data)
   - Social media account records
   - Prior police reports involving the victim
   - 911 audio and CAD records
   - Surveillance footage from businesses

4. **Fact verification** -- What factual claims in the theory need independent verification?
   - Timeline verification against physical evidence
   - Witness statement consistency checks
   - Physical plausibility of the defense version

**Routing:** Generate tasks and route to `dw-defense-investigator-tasking` for investigator assignment and tracking.

---

### MODULE B -- STREAM 2: Discovery Actions

What additional discovery is needed to support or test this theory? What discovery deficiencies must be resolved?

**Task categories:**

1. **Outstanding discovery demands** -- Pull from `dw-discovery-compliance-monitor` ledger. What has been demanded but not produced?
   - Flag items that are CRITICAL to the selected theory
   - Draft motion to compel for items outstanding beyond 30 days

2. **New discovery demands driven by the theory** -- What has not yet been demanded but is now needed because of the theory selection?
   - Brady/Giglio demands specific to this theory (e.g., if self-defense theory, demand victim's criminal history, prior DV reports, prior threats)
   - Expert-related discovery (lab bench notes, calibration records, analyst training records)
   - Witness-related discovery (witness criminal histories, prior statements, cooperation agreements)

3. **Motions to compel** -- For any outstanding critical items, draft or route motion to compel.

4. **Discovery preservation** -- Identify evidence at risk of destruction or loss and issue preservation demands.

**Routing:** Route discovery ledger tasks to `dw-discovery-compliance-monitor`. Route Brady/Giglio demands to `dw-brady-giglio-auditor`. Route motions to compel to `dw-pretrial-motion-library`.

---

### MODULE C -- STREAM 3: Expert Witness Needs

What expert testimony is needed to support this theory? What prosecution experts need to be challenged?

**Task categories:**

1. **Defense expert retention** -- What experts does the defense need to retain?
   - Identify the discipline (forensic pathologist, ballistics, DNA, mental health, accident reconstruction, cell site, etc.)
   - Define the scope of engagement (consulting only vs. testifying)
   - Budget estimate and funding source (if public defender, indigent defense fund application under La. C.Cr.P. Art. 725)
   - Timeline for retention, report completion, and deposition/testimony

2. **Prosecution expert challenges** -- What prosecution experts need Daubert/Foret challenges?
   - Identify each prosecution expert and their discipline
   - Route to `dw-expert-witness-evaluator` for full evaluation
   - Timeline for filing Daubert/Foret motion and hearing

3. **Expert opinion development** -- What specific opinions need to be developed?
   - Define the question the expert must answer
   - Identify the materials the expert needs to review
   - Set deadline for expert report

4. **Expert coordination** -- Schedule expert review of materials, coordinate with investigator for scene visits if needed, arrange for expert to review opposing expert's report.

**Routing:** Route expert evaluations to `dw-expert-witness-evaluator`. Route indigent expert funding motions to `dw-pretrial-motion-library`.

---

### MODULE D -- STREAM 4: Motion Practice

What pretrial motions support this theory? What motions must be filed to exclude harmful evidence or preserve favorable evidence?

**Task categories:**

1. **Suppression motions** -- Based on constitutional issues identified in the case analysis:
   - 4th Amendment (search and seizure) -- route to `dw-suppression-motion`
   - 5th Amendment (statements / Miranda) -- route to `dw-suppression-motion`
   - 14th Amendment (identification) -- route to `dw-suppression-motion`
   - Fruit of the poisonous tree cascades

2. **404(b) opposition** -- If the State has filed or signaled a Prieur notice:
   - Route to `dw-404b-opposition` for opposition drafting
   - If the defense wants to introduce 404(b) evidence about the victim (e.g., prior violence in a self-defense case), draft the supporting motion

3. **Motions in limine** -- Theory-specific evidentiary motions:
   - Exclude prejudicial photographs (inflammatory autopsy photos, crime scene photos)
   - Exclude hearsay or improper opinion testimony
   - Limit expert testimony scope
   - Exclude prior bad acts of the defendant

4. **Severance motions** -- Sever counts or co-defendants if joinder prejudices the selected theory.

5. **Other pretrial motions** -- Bill of particulars, bond reduction, continuance, venue change, recusal -- any motion that advances the theory or removes obstacles.

**Routing:** Route all motions to `dw-pretrial-motion-library` for template selection and drafting. Route suppression motions to `dw-suppression-motion`. Route 404(b) work to `dw-404b-opposition`.

---

### MODULE E -- STREAM 5: Witness Preparation

Which witnesses need to be prepared? What testimony supports the theory? What cross-examination themes align with the theory?

**Task categories:**

1. **Cross-examination outlines for prosecution witnesses** -- For each prosecution witness:
   - How does their testimony interact with the defense theory?
   - What concessions can be extracted that support the theory?
   - What impeachment material exists?
   - Route to `dw-cross-exam-architect` for full outline development

2. **Direct-examination outlines for defense witnesses** -- For each defense witness:
   - What testimony supports the theory?
   - What foundation must be laid?
   - What exhibits will be introduced through this witness?
   - Route to `dw-direct-exam-architect` for full outline development

3. **Witness preparation sessions** -- Schedule and plan preparation for:
   - Defendant (if testifying -- strategic decision for attorney)
   - Character witnesses
   - Expert witnesses (coordinate testimony with expert report)
   - Alibi witnesses

4. **Witness sequencing** -- Determine the order of defense witnesses to build the theory narrative. Cross-reference with `dw-trial-narrative-builder` for narrative arc.

**Routing:** Route cross-examination work to `dw-cross-exam-architect`. Route direct-examination work to `dw-direct-exam-architect`.

---

### MODULE F -- STREAM 6: Exhibit & Evidence Strategy

What exhibits support the theory? What demonstratives need to be created? What evidence authentication issues must be resolved?

**Task categories:**

1. **Exhibit identification** -- From the Evidence Table in Case Tables.xlsx, identify every exhibit that supports the defense theory:
   - Documentary exhibits (records, reports, photographs)
   - Physical exhibits (weapons, clothing, objects)
   - Digital exhibits (cell phone records, social media, surveillance video)
   - Demonstrative exhibits (diagrams, maps, timelines, charts)

2. **Exhibit preparation** -- For each identified exhibit:
   - Authentication method (stipulation, witness testimony, self-authentication)
   - Predicate witness (who lays the foundation?)
   - Enlargements or display format for trial
   - Pre-marking and exhibit list preparation

3. **Demonstrative creation** -- What demonstratives need to be built?
   - Crime scene diagram with defense-favorable annotations
   - Timeline chart showing defense version
   - Comparison charts (e.g., witness statement inconsistencies)
   - Maps (alibi route, cell site coverage areas)

4. **Evidence authentication challenges** -- What prosecution exhibits can be challenged on authentication, chain of custody, or admissibility grounds?
   - Cross-reference with `dw-chain-of-custody-auditor` findings
   - Identify hearsay, best evidence, or foundation deficiencies

**Routing:** Route exhibit management to `dw-exhibit-manager`. Route trial notebook assembly to `dw-trial-notebook-builder`.

---

### MODULE G -- STREAM 7: Narrative & Theme Development

How does the theory translate into the courtroom story? What is the memorable theme? How does every piece of the trial reinforce that theme?

**Task categories:**

1. **Case theme development** -- Distill the defense theory into a one-sentence theme that:
   - Is memorable and repeatable
   - Frames the entire case from the defense perspective
   - Can be introduced in voir dire, reinforced in opening, proved through evidence, and argued in closing

2. **Opening statement outline** -- Build the opening around the theme:
   - Hook / primacy opener tied to the theme
   - Defense narrative in story form
   - Roadmap of the evidence the jury will hear
   - Route to `dw-trial-narrative-builder` for full development

3. **Closing argument framework** -- Build the closing around the theme:
   - Element-by-element burden walk using the Defense Matrix
   - Witness credibility summary using cross-examination findings
   - Verdict form walk-through
   - Route to `dw-trial-narrative-builder` for full development

4. **Jury instruction requests** -- What special jury instructions does the theory require?
   - Self-defense charges (La. R.S. 14:20 -- no duty to retreat, castle doctrine)
   - Heat-of-passion / manslaughter responsive verdict
   - Specific intent negation (intoxication, mental defect)
   - Lesser included offenses / responsive verdicts
   - Route to `dw-jury-instructions-builder` for charge package

5. **Voir dire themes** -- What juror attitudes and experiences are relevant to this theory?
   - Route to `dw-voir-dire-assistant` for voir dire question development

**Routing:** Route narrative work to `dw-trial-narrative-builder`. Route jury instruction work to `dw-jury-instructions-builder`. Route voir dire work to `dw-voir-dire-assistant`.

---

## STEP 3 -- WORKPLAN SUMMARY DASHBOARD

After generating all seven streams, produce a summary dashboard at the top of the workplan document:

### Dashboard Contents

1. **Theory Summary** -- One paragraph restating the selected defense theory from Report 4a
2. **Trial Date** -- Absolute date and days remaining
3. **Task Count by Stream**

| Stream | Total Tasks | Critical | High | Medium | Low | Complete | Blocked |
|--------|------------|----------|------|--------|-----|----------|---------|
| 1 - Investigation | | | | | | | |
| 2 - Discovery | | | | | | | |
| 3 - Expert Witness | | | | | | | |
| 4 - Motion Practice | | | | | | | |
| 5 - Witness Prep | | | | | | | |
| 6 - Exhibit & Evidence | | | | | | | |
| 7 - Narrative & Theme | | | | | | | |
| **TOTAL** | | | | | | | |

4. **Critical Path** -- List the CRITICAL-priority tasks across all streams in deadline order. These are the tasks that, if not completed, prevent the case from going to trial on this theory.
5. **Blocked Tasks** -- List any tasks with BLOCKED status and the reason for the block.
6. **Immediate Action Items** -- Top 5 tasks to begin today, with responsible party and routing skill.
7. **Budget & Resource Summary** -- Estimated investigator hours, expert costs, and paralegal time (if data available).

---

## STEP 4 -- OUTPUT FORMAT

### Primary Deliverable: Theory-to-Workplan (.docx)

Filename: `Theory to Workplan - {{DEFENDANT_LAST}} - {{YYYY-MM-DD}}.docx`

Location: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

**Document structure:**

1. **Header** -- Attorney work product marking per shared protocols
2. **Case Caption Block** -- Defendant name, docket number, parish/court, judge, ADA, trial date, lead attorney
3. **Selected Defense Theory** -- From Report 4a, with attorney's rationale
4. **Summary Dashboard** -- Per Step 3
5. **Stream 1 -- Investigation Tasks** -- Full task table (Module A)
6. **Stream 2 -- Discovery Actions** -- Full task table (Module B)
7. **Stream 3 -- Expert Witness Needs** -- Full task table (Module C)
8. **Stream 4 -- Motion Practice** -- Full task table (Module D)
9. **Stream 5 -- Witness Preparation** -- Full task table (Module E)
10. **Stream 6 -- Exhibit & Evidence Strategy** -- Full task table (Module F)
11. **Stream 7 -- Narrative & Theme Development** -- Full task table (Module G)
12. **Cross-Stream Dependencies** -- Dependency map showing how tasks in one stream depend on completion of tasks in another (e.g., Stream 5 cross-exam outlines depend on Stream 2 discovery production)
13. **Revision History** -- Date, author, what changed (for living-document tracking)

### Secondary Deliverable: Summary Checklist (Apple Notes)

Push a condensed checklist of all CRITICAL and HIGH priority tasks to Apple Notes via the same mechanism used by `dw-criminal-defense` Phase 2 Step 6. Format:

```
[Case Name] -- Theory-to-Workplan Summary
Theory: [One-line theory statement]
Trial Date: [Date] ([X] days)

CRITICAL TASKS:
[ ] S1-001: [Description] -- [Responsible] -- by [Deadline]
[ ] S2-003: [Description] -- [Responsible] -- by [Deadline]
...

HIGH PRIORITY TASKS:
[ ] S3-001: [Description] -- [Responsible] -- by [Deadline]
...
```

### Case Brain Registration

Register the workplan output with `dw-case-brain` per Contract 5 in `dw-data-contracts`:

```
- **[Date]** | `dw-theory-to-workplan` | Theory to Workplan - [Client Last Name] - [Date].docx | 01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/
```

Update the Case Brain's OPEN ISSUES section with any BLOCKED tasks.

---

## CROSS-SKILL INTEGRATION

### This skill REQUIRES (prerequisite):

- `dw-criminal-defense` Report 4/4a -- Theory Selection Memo (mandatory input; will not generate workplan without it)

### This skill READS FROM:

- `dw-case-brain` -- structured case context, companion skill outputs, open issues
- `dw-criminal-defense` Reports 1-8 + 4a -- all Phase 2 analytical outputs (plus Report 0 from `dw-neutral-inventory` and Report 2a from `dw-theory-deconstructor`)
- `dw-discovery-compliance-monitor` -- outstanding discovery ledger (feeds Stream 2)
- `dw-brady-giglio-auditor` -- Brady/Giglio findings (feeds Streams 2 and 4)
- All completed audit reports -- every auditor skill's output feeds task generation across streams
- `Case Tables.xlsx` -- Evidence Table, Timeline, Witness Sheet, Defense Matrix

### This skill ROUTES TO (downstream execution):

| Stream | D&W Skill | What Flows |
|--------|-----------|-----------|
| 1 - Investigation | `dw-defense-investigator-tasking` | Investigation tasks with witness lists, location visits, record subpoenas |
| 2 - Discovery | `dw-discovery-compliance-monitor`, `dw-brady-giglio-auditor` | New discovery demands, Brady/Giglio-specific demands |
| 2 - Discovery | `dw-pretrial-motion-library` | Motions to compel |
| 3 - Expert | `dw-expert-witness-evaluator` | Prosecution expert evaluations, Daubert/Foret challenge seeds |
| 3 - Expert | `dw-pretrial-motion-library` | Indigent expert funding motions (La. C.Cr.P. Art. 725) |
| 4 - Motions | `dw-suppression-motion` | Suppression motions (4th, 5th, 14th Amendment) |
| 4 - Motions | `dw-404b-opposition` | 404(b) / Prieur opposition |
| 4 - Motions | `dw-pretrial-motion-library` | All other pretrial motions |
| 5 - Witness | `dw-cross-exam-architect` | Cross-examination outlines for prosecution witnesses |
| 5 - Witness | `dw-direct-exam-architect` | Direct-examination outlines for defense witnesses |
| 6 - Exhibit | `dw-exhibit-manager` | Exhibit identification, preparation, and pre-marking |
| 6 - Exhibit | `dw-trial-notebook-builder` | Trial notebook assembly with theory-aligned tabs |
| 7 - Narrative | `dw-trial-narrative-builder` | Opening statement, closing argument, theme tracker |
| 7 - Narrative | `dw-jury-instructions-builder` | Theory-specific jury charges and verdict form |
| 7 - Narrative | `dw-voir-dire-assistant` | Theory-aligned voir dire questions |

### This skill WRITES TO:

- Workplan document (primary deliverable)
- Apple Notes summary checklist (secondary deliverable)
- `dw-case-brain` -- registers output and updates OPEN ISSUES with BLOCKED tasks

---

## Guardrails

1. **Requires attorney-selected theory.** Do not generate a workplan without Report 4a (Theory Selection Memo) containing the attorney's selected defense theory. If Report 4a does not exist or does not contain a clear theory selection, STOP and route to `dw-criminal-defense` Report 4 for theory development. A workplan without a theory is a to-do list without a strategy.

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

This skill does not maintain its own `references/` subdirectory. It is an orchestrator that reads from and routes to other skills. Key reference documents consumed indirectly through downstream skills:

- **Report 4a (Theory Selection Memo)** -- mandatory input; produced by `dw-criminal-defense` Report 4
- **dw-shared-protocols/references/attorney-work-product-marking.md** -- work product marking for all deliverables
- **dw-shared-protocols/references/output-path-formula.md** -- output path anchored on `{{CASE_ROOT}}`
- **dw-data-contracts/SKILL.md** -- Contract 5 (Case Brain Registration) for registering output

---

*This skill is part of the Daniels & Washington criminal defense toolkit -- Barone Discovery Workflow. It bridges strategic theory selection (Report 4a) and tactical trial preparation across all seven preparation domains. Pair with `dw-adversarial-stress-test` to stress-test the theory before committing resources to the workplan, and with `dw-case-brain` for ongoing status tracking and case context.*
