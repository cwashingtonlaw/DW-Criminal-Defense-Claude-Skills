# Integration Notes — dw-theory-deconstructor (Report 2a)

## Position in Workflow

Report 2a sits between Report 2 (Prosecution's Case Summary) and Report 4 (Core Defense Narrative / Competing Theories) in the Barone Discovery Workflow:

```
Report 2 (Prosecution's Case Summary)
    │
    ▼
Report 2a (Theory Deconstruction) ◄── THIS SKILL
    │
    ├──► Report 4 (Competing Theories / Core Defense Narrative)
    ├──► dw-adversarial-stress-test
    └──► dw-theory-to-workplan
```

Report 2a is a bridge skill: it takes the prosecution's articulated theory (Report 2) and breaks it down into its logical components so that downstream skills can build on a rigorous foundation rather than intuition.

## Dependency on Report 2 Output

Report 2 (Prosecution's Case Summary) is a **hard prerequisite**. The skill enforces this in two places:

1. **Step 1 (Information Gathering Protocol), Essential Item 1** — Report 2 is listed as the primary input. If it does not exist, the skill STOPs and routes the attorney to generate it first.
2. **Guardrail 6** — explicitly states that theory deconstruction without a completed Report 2 produces unreliable analysis and must not be attempted.

**What Report 2 provides to Report 2a:**
- The State's articulated theory of the case (narrative form)
- The evidence the State relies on, organized by charge
- The State's theory of how the evidence connects to each element
- Any concessions or weaknesses the State's summary implicitly reveals

**What Report 2a does with it:**
- Decomposes the narrative into discrete facts, inferences, and assumptions
- Maps each component to the elements of each charged offense
- Classifies the evidentiary sufficiency of each element
- Identifies the logical gaps the defense can exploit

## How the Gap Analysis Matrix Feeds dw-adversarial-stress-test

Module E (Gap Analysis Matrix) produces the primary input for `dw-adversarial-stress-test`. The relationship is:

| Report 2a Output | How dw-adversarial-stress-test Uses It |
|---|---|
| **Element-by-element vulnerability ratings** (FORTIFIED / SOLID / EXPOSED / VULNERABLE / CRITICAL GAP) | The stress-test focuses its attacks on EXPOSED, VULNERABLE, and CRITICAL GAP elements — these are where the theory is most likely to fail under adversarial pressure |
| **Assumption Audit (Module D)** | Each unsupported assumption with MEDIUM or HIGH challenge viability becomes a specific stress-test scenario: "What if the defense proves this assumption false?" |
| **Inference chains (Module C, Section C.2)** | Stacked inference chains are stress-tested by attacking each link independently: if any link breaks, the chain fails |
| **Suppression candidates (Module A, A.3)** | Elements supported only by evidence flagged as SUPPRESSION CANDIDATE are stress-tested in a "post-suppression" scenario — what happens to the State's case if the challenged evidence is excluded? |

The stress-test skill should receive the full Module E matrix and the Module D assumption table. It should not need to re-derive facts or inferences from scratch — Report 2a has already done that work.

## How the Alternative Inference Table Feeds Revised Report 4 (Competing Theories)

Module F (Alternative Inference Table) provides the raw analytical material for constructing or revising Report 4 (Core Defense Narrative / Competing Theories):

| Report 2a Output | How Report 4 Uses It |
|---|---|
| **Counter-inferences (Module F, F.2)** | Each defense counter-inference is a candidate building block for the competing defense narrative. Report 4 selects the counter-inferences that are internally consistent, thematically coherent, and strongest when combined. |
| **Defense narrative seeds (Module F, F.3)** | The 2-3 candidate narrative threads identified by Report 2a provide starting points for Report 4's full narrative development. Report 4 evaluates each seed against the full case context and selects or synthesizes the strongest one. |
| **Counter-inference strength ratings** | Report 4 prioritizes counter-inferences rated STRONG and avoids building a narrative that depends on WEAK counter-inferences — unless no stronger alternative exists. |
| **Remaining gaps identified per narrative seed** | Report 4 notes which defense theories require additional investigation, expert testimony, or discovery to become viable, informing the defense workplan. |

The flow is:
1. Report 2a identifies what the State is inferring and proposes what the defense could infer from the same facts
2. Report 4 takes the strongest defense inferences and weaves them into a coherent competing narrative
3. dw-adversarial-stress-test then tests both the prosecution theory (using Module E gaps) and the defense theory (using Report 4 output)

This three-step sequence ensures that defense theories are built on analytical foundations, not intuition, and are stress-tested before the attorney commits to a trial strategy.

## Implementation Notes

- **No references subdirectory needed at launch.** Report 2a relies on Report 2 output, Case Tables.xlsx, and charge-type specialist element grids — all of which are produced by other skills. If discipline-specific inference-pattern libraries become useful (e.g., common prosecution inferences in drug cases, common alternative inferences in self-defense cases), a `references/` subdirectory can be added later.
- **Case Brain update is required.** After Report 2a is generated, the skill updates `dw-case-brain` with the deconstruction completion status, key vulnerability counts, and file path. Downstream skills (`dw-adversarial-stress-test`, `dw-theory-to-workplan`) should check Case Brain for Report 2a availability before proceeding.
- **Optional defense-theory deconstruction.** The skill can deconstruct not just the prosecution theory but also a defense theory (if one has been articulated). This is useful for self-assessment: before committing to a defense narrative in Report 4, the attorney can run the defense theory through the same fact/inference/assumption framework to identify its own weaknesses. This mode is invoked by providing a defense theory alongside Report 2.
