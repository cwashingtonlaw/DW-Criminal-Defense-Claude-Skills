# Integration Notes -- dw-adversarial-stress-test

**Barone Discovery Workflow | Step 7 | Adversarial Stress Test**

---

## 1. Dependency on Report 4a (Theory Selection Memo)

The Adversarial Stress Test has a **hard prerequisite** on Report 4a (Theory Selection Memo). The skill will not proceed without it.

**Why this dependency is non-negotiable:**

- The stress test is a targeted red-team simulation against a *specific* defense theory. Without a selected theory, there is no target to attack.
- An unfocused "general stress test" produces noise -- it identifies every possible prosecution argument without weighting them against the defense's actual strategy. This wastes attorney time and dilutes preparation focus.
- Report 4a is the product of the theory development chain: `dw-criminal-defense` Report 4 (Core Defense Narrative) generates candidate theories, `dw-theory-deconstructor` (Report 2a) deconstructs them for structural weaknesses, and the attorney selects the strongest candidate in Report 4a.

**What happens if Report 4a is missing:**

The skill fires a hard stop and advises the attorney to run the theory development workflow first. It does not offer a degraded or partial stress test.

**What the skill reads from Report 4a:**

- Selected theory name and one-paragraph summary
- Supporting evidence inventory (the evidence the defense relies on)
- Theme / narrative frame
- Known limitations the attorney has already accepted
- Any conditions or contingencies noted by the attorney (e.g., "this theory works only if the suppression motion is granted")

---

## 2. Cross-Feed with dw-theory-to-workplan

The Adversarial Stress Test's **Module G (Priority Preparation Checklist)** is designed to feed directly into `dw-theory-to-workplan`.

**How the cross-feed works:**

1. Module G produces a ranked list of preparation tasks, each tagged with:
   - Vulnerability description
   - Priority level (CRITICAL / HIGH / STANDARD)
   - The D&W skill that should handle the preparation
   - A deadline relative to trial date

2. `dw-theory-to-workplan` ingests these tasks and distributes them across its workplan streams:
   - **Stream 5 (Witness Preparation)** receives all tasks routed to `dw-cross-exam-architect` -- these are defense witnesses who need preparation against the hardest prosecution cross-examination questions identified in Module B.
   - **Stream 3 (Motion Practice)** receives tasks routed to `dw-suppression-motion`, `dw-pretrial-motion-library`, and `dw-404b-opposition` -- these are evidentiary exclusion efforts targeting rebuttal evidence identified in Module D.
   - **Stream 2 (Investigation)** receives tasks routed to `dw-defense-investigator-tasking` -- these are additional investigation needs identified when the stress test reveals evidence gaps in the defense's counter-responses.
   - **Stream 4 (Expert Work)** receives tasks routed to `dw-expert-witness-evaluator` -- these are expert retention or challenge needs.
   - **Stream 1 (Legal Research)** receives tasks involving legal authority gaps in the defense counter-responses.

3. When the stress test is re-run (due to new evidence, theory shift, or motion ruling), the updated Module G replaces the prior task set in the workplan. `dw-theory-to-workplan` should diff the old and new checklists and flag tasks that were added, removed, or re-prioritized.

**Contract:** The Module G task format must remain stable across stress-test versions so that `dw-theory-to-workplan` can parse it reliably. The minimum required fields per task are: vulnerability description, priority level, routing skill, and deadline.

---

## 3. Module E Feeding dw-trial-narrative-builder Rebuttal Anticipation Memo

The **Defense Counter-Response Matrix (Module E)** feeds the `dw-trial-narrative-builder`'s Rebuttal Anticipation Memo.

**How the feed works:**

1. Module E documents every prosecution attack alongside a prepared defense response. The "Preparation Needed" column identifies attacks that require narrative-level preparation -- not just legal argument but story-level reframing.

2. `dw-trial-narrative-builder` reads Module E and uses it to:
   - **Build preemptive narrative elements** into the defense opening and direct examinations. If the stress test identifies that the prosecution will attack the defense theory on point X in closing, the narrative builder incorporates the defense counter-narrative for point X into the affirmative case -- "stealing thunder" before the prosecution can land the blow.
   - **Draft the Rebuttal Anticipation Memo** -- a standalone document that maps each anticipated prosecution rebuttal to a prepared defense response, organized by the order in which the prosecution is likely to raise them.
   - **Adjust the defense story arc** to minimize vulnerability windows. If Module E reveals that certain defense claims are unsupported and the counter-response is weak ("minimize" or "redirect" rather than "neutralize"), the narrative builder may advise the attorney to de-emphasize those claims in the story.

3. The Rebuttal Anticipation Memo structure mirrors Module E but translates legal/evidentiary responses into narrative language suitable for closing argument and jury communication.

**Contract:** Module E must include the response-strategy classification (Neutralize / Minimize / Redirect / Preempt / Exclude / Jury Instruction) so that `dw-trial-narrative-builder` can prioritize which attacks need narrative-level preparation versus purely legal responses.

---

## 4. Re-Run Triggers and Protocol

The Adversarial Stress Test must be re-run when the evidence landscape or defense strategy changes. A stress test against stale inputs is worse than no stress test -- it gives the defense team false confidence about their preparation posture.

**Trigger events requiring re-run:**

| Trigger | Why Re-Run Is Needed | What Changes |
|---|---|---|
| **New discovery production** | New evidence may create new prosecution attacks or eliminate existing ones. Module A vulnerability scan, Module D rebuttal evidence inventory, and Module E counter-responses may all shift. | Full re-run recommended. At minimum: Modules A, D, E, F, G. |
| **Theory shift (new Report 4a)** | The entire stress test is targeted at a specific theory. A new theory requires a complete re-run. | Full re-run required. All modules. |
| **Motion ruling (suppression granted or denied)** | A suppression ruling changes what evidence is admissible. If a key piece of prosecution evidence is suppressed, attacks relying on it become moot. If a defense motion is denied, attacks the defense planned to exclude are now live. | Modules D, E, F, G. Module C if the ruling affects the prosecution's closing argument structure. |
| **Defense witness changes** | Adding, removing, or changing a defense witness alters Module B (cross-examination simulation) and may affect Module E (counter-responses that depend on that witness's testimony). | Modules B, E, F, G. |
| **Prosecution witness disclosure** | Late-disclosed prosecution witnesses or changed witness testimony affect the prosecution's attack capability. | Modules A, B, C, D, E, F, G (scope depends on significance). |

**Re-run protocol:**

1. Set `STRESS_TEST_CURRENT` to `false` in Case Brain immediately upon learning of the trigger event.
2. Advise the attorney: *"The Adversarial Stress Test is no longer current due to [trigger]. Recommend re-running before [next preparation milestone]."*
3. When re-running, generate a new report with the current date. Do not overwrite the prior report.
4. Note in the new report header: *"Re-run: supersedes [prior report filename]. Reason: [trigger]."*
5. Update `dw-theory-to-workplan` with the revised Module G task set.
6. Update `dw-trial-narrative-builder` with the revised Module E counter-response matrix.
7. Update `dw-case-brain` with new stress test completion date and revised top-5 summary.

**Timing guidance:**

- The initial stress test should run as soon as Report 4a is finalized (theory selected).
- A final stress test should run no later than 2 weeks before trial, after all motions have been ruled on and the evidence landscape is settled.
- Between initial and final, re-run as needed per the trigger events above.

---

## Barone Workflow Position

```
dw-criminal-defense Phase 2 (Reports 1-8)
    |
    v
dw-theory-deconstructor (Report 2a)
    |
    v
Attorney selects theory --> Report 4a (Theory Selection Memo)
    |
    v
>>> dw-adversarial-stress-test (this skill) <<<
    |
    +---> dw-theory-to-workplan (Module G tasks --> workplan streams)
    +---> dw-trial-narrative-builder (Module E --> Rebuttal Anticipation Memo)
    +---> dw-cross-exam-architect (Module B --> witness prep outlines)
    +---> dw-voir-dire-assistant (Module F --> jury-selection focus areas)
    +---> dw-case-brain (status update, top-5 summary)
```

The stress test sits between theory selection and trial preparation execution. It is the last analytical gate before preparation work begins -- ensuring the defense team knows what they are preparing for.
