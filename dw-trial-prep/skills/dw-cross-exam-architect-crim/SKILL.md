---
name: dw-cross-exam-architect-crim
category: trial-prep
description: >
  Build cross-examination outlines for any witness. ALWAYS invoke for "build a cross,"
  "cross-exam outline," "impeachment outline," or "prep cross for [witness]." Produces
  three deliverables per witness — Cross-Examination Outline (.docx), Source Catalog (.pdf),
  and Combined Sources (.pdf) — in the D&W chapter template, Times New Roman 14 pt, saved to
  01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/. Louisiana law, U.S. 5th Circuit
  for federal matters, and the state appellate circuit resolved from the parish of prosecution
  across the Louisiana First, Third, and Fourth Circuits. Endpoint of all auditor chains.
---

# Master Cross-Examination Architect
**Daniels & Washington | Criminal Defense | Louisiana law · U.S. 5th Circuit for federal · state appellate circuit resolved by parish**

Build cross-examination outlines under the Louisiana Code of Evidence and Code of Criminal Procedure, in the D&W chapter template. Controlling authority comes from the parish of prosecution — the firm spans the Louisiana First, Third, and Fourth Circuits and three federal districts.

**Three deliverables per witness, always:** Cross-Examination Outline (.docx) · Source Catalog (.pdf) · Combined Sources (.pdf).

**Source citation mandate.** Every question traces to a specific document — confront with the document, not with memory. After Step 4 every citation carries its `(N)` register number, the document's actual title, then page/Bates/timestamp. Spell agencies and labs out in full; no abbreviations, no short names, one name per document. Cite every supporting document, not just the best one — multiple sources give the attorney options if one exhibit is excluded. Anything untraceable is marked `[UNSOURCED — VERIFY BEFORE USING AT TRIAL]` and never asserted as fact. → `references/source-register-and-template.md`

---

## STEP 0 — File Intake Hard Stop

If documents were uploaded or referenced, analyze nothing yet. Respond only:

> *"Before I begin — are you uploading any additional documents right now? I'll start analysis only after you confirm: 'No more uploads now.'"*

Applies to every new batch. If analysis is requested with nothing attached, ask whether uploads are coming — begin only once the attorney confirms either (a) none are coming, or (b) proceed without documents.

---

## STEP 0.5 — Load Protocols

From `dw-shared-protocols-crim`: `attorney-work-product-marking.md`, `output-path-formula.md`.

From `references/`: `guardrails.md` · `deliverable-formatting.md` · `jurisdiction-and-court-map.md` (carries the **art. 608(B) gate**, §3.5) · `quick-reference-tables.md` (consult before any evidentiary assertion) · `error-preservation-protocol.md`.

Load all seven before Step 0.52. Load `references/confrontation-and-surrogate-analysts.md` at Step 3 when the witness testifies about work performed by someone else.

All output is internal work product — apply marking. **All three deliverables go to one folder:** `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/`, where `{{CASE_ROOT}}` comes from `dw-case-brain-crim` and varies by case source. Never hardcode it.

---

## STEP 0.52 — Choose the Path

- **FULL BUILD** (default) — trial prep, multiple witnesses, or no prior cross work in this matter. Runs every step.
- **FAST PATH** — one named witness, needed soon. Skips Step 0.6, defers Step 1.A, makes Step 8.5 optional. Nothing else.

Fast Path narrows scope; it never lowers the floor. Every Fast Path outline carries the cover-page notice in `assets/fast-path-notice.md`.

→ `references/build-paths.md`. State the path in Step 2.

---

## STEP 0.55 — Resolve Jurisdiction

From the Case Brain, resolve **trial court**, **Louisiana Court of Appeal**, and — if federal — **district**. This sets the evidentiary toggle for the whole outline. → `references/jurisdiction-and-court-map.md` §1, §4

**Two Fifth Circuits — write which one you mean.** `5th Cir.` is the **U.S.** Fifth Circuit, which governs all three Louisiana federal districts and is the firm's correct federal default. `La. 5th Cir.` is the Louisiana Fifth Circuit Court of Appeal — **no footprint parish is in it**, so a state-court citation to it is almost certainly a mistake. For state appellate authority, name the parish's own circuit: First, Third, or Fourth.

**16th JDC trap:** Iberia, St. Martin, and St. Mary share the 16th JDC, but **St. Mary appeals to the First Circuit** while the other two appeal to the Third. Resolve by parish, never by district.

Outside the footprint table, ask — do not guess.

---

## STEP 0.58 — Upstream Intake & Witness History

**Runs on both paths, before any analysis.** The firm's other skills have already done most of this work and the data contracts name this skill their consumer.

Pull the Witness Analysis Card, the **DMAR**, **auditor reports**, the Brady/Giglio audit, any theory stress-test findings, and **all prior sworn testimony** — suppression hearing, preliminary exam, grand jury, prior trial. Prior sworn inconsistency is the strongest impeachment there is; a hearing with no transcript in the file is an action item. → `references/upstream-intake.md` · `references/integration-map.md`

Check whether the firm has **crossed this witness before**, across all three case sources. Report the result either way — silence is ambiguous. Public-record transcripts are free to use; **firm work product from another client's matter requires the attorney's conflicts confirmation first.** → `references/witness-history-lookup.md`

Report what was found and what was absent in the Step 2 confirmation block.

---

## STEP 0.6 — Witness Prioritization Audit

*Full Build only.* Rank impeachment vulnerabilities for the top 10 prosecution witnesses across four categories: internal contradictions, external contradictions, omissions, credibility.

Uses the Step 0.58 intake — ranking without the DMAR and auditor findings is ranking blind. Run the **art. 608(B) gate** on every credibility item before ranking; do not rank what the attorney cannot ask about. Every point cites a source with page/paragraph/timestamp.

Deliverable: **Ranked Witness Impeachment Report**, shared with the attorney before Step 1. → `references/witness-prioritization-audit.md`

---

## STEP 1 — Information Gathering

Step 0.58 has already pulled the analyzed upstream material. Gather the rest.

**Essential — do not draft without these:** witness type · charges with statutory citations · **case theme in one sentence** (the spine of every chapter) · defense theory · concessions needed from this witness.

**Strategic and contextual tiers:** → `references/information-tiers.md`

Present missing items as a ranked checklist. **If an essential item is missing, do not draft — ask.**

---

## STEP 1.A — Master Witness Table

Five-column inventory, refreshed with every new outline. Every witness appearing in any outline must have a row. **Fast Path defers this, it does not waive it.** → `references/master-witness-table.md`

---

## STEP 2 — Pre-Draft Confirmation

Reproduce the confirmation block in `assets/pre-draft-confirmation.md`, filled in — including what Step 0.58 found and what was absent. **Do not draft until the attorney responds.**

---

## STEP 3 — Witness Module

Apply the matching module: **Law Enforcement** · **Expert** · **Civilian** (eyewitness / complainant / character / fact) · **Co-Defendant / Accomplice / Cooperator** · **Document Custodian**. Each sets tone, focus, and auto-flags; LE chapters also carry Impact / Fragility scoring. All types use short-question sequencing — 3–5 leading questions per point, locking the precondition before revealing the contradiction.

- **Cooperators:** run `dw-brady-giglio-auditor-crim` first. Deal terms are *Giglio* material; the cross is built on bias under art. 607(D)(1) — extrinsic proof permitted, untouched by art. 608(B).
- **Surrogate analysts:** if the witness did not perform or observe the work, that is an **objection before it is a cross**.

→ `references/witness-type-modules.md` · `references/agency-and-lab-module.md` · `assets/chapter-goals-and-scoring.md` · `references/confrontation-and-surrogate-analysts.md` (conditional)

---

## STEP 4 — Source Register & Outline

Build the **Source Register** before any chapter — a numbered list of every source to be cited. Each gets a permanent `(N)` that never changes across any deliverable. **No short-name column**: cite by the document's actual title.

Then draft in the D&W template — one chapter per page: CHAPTER TITLE, CHAPTER GOALS, and the three-column SOURCE/EXHIBIT | QUESTIONS | NOTES table.

**Three mandatory drafting rules:**

1. **Every cell in all three columns is a list, never a paragraph.** Sources bulleted with `(N)` prefixes; questions numbered sequentially; notes bulleted. One idea per bullet, one fact per question. Prose in any column is a defect — this is read standing up, mid-examination.
2. **Every impeachment question carries all three branches** — `IF ADMITS →` / `IF DENIES →` / `IF NO RECALL →`. An expected answer is a prediction, not a plan.
3. **Every flagged question carries a preservation bullet** naming the ground to state and the substance to proffer. A flag without one throws away the appellate issue.

**Sequencing:** open on the favorable, close on your best point; order CRITICAL DMAR findings into chapters you are certain to reach. The case theme appears in at least one chapter title and in every substantive chapter's goals. Full seven-step default order → `references/source-register-and-template.md`.

→ `references/source-register-and-template.md` · `assets/outline-assembly.md` · `assets/chapter-goals-and-scoring.md`

---

## STEP 5 — Auto-Scan: Prior Inconsistent Statements

Identify every statement this witness made across all sources; flag every inconsistency (report vs. supplemental, report vs. BWC, statement vs. prior sworn testimony, hearing transcript vs. expected trial testimony); tag each as an Impeachment Bullet with source, page, and Bates; insert into the relevant chapter with its branch logic.

Cross-reference the Witness Analysis Card and DMAR §4 Inconsistency Matrix rather than duplicating them — and confirm nothing they found was dropped.

**Prior convictions use art. 609.1, never art. 609.** Fact, name, date, sentence come in; details open only on the art. 609.1(C) triggers. Art. 609.1(B) bars inquiry into arrest, warrant, indictment, prosecution, or acquittal.

→ `assets/impeachment-bullet.md` (all bullet formats) · `references/jurisdiction-and-court-map.md` §3

---

## STEP 5.5 — Preservation Log

Append to every outline per `assets/preservation-log.md`, with Chapter and Question # pre-filled for each flagged question. Filled in during trial. Hands off to `dw-appellate-error-monitor-crim` and `dw-issue-code-tracker-crim`. → `references/error-preservation-protocol.md`

---

## STEP 6 — Discovery Gap Report

Append to every outline: every material expected for this witness type that was not produced. For each — name it, explain why it matters for cross, and flag whether it belongs in the Table of Missing Discovery (Phase 2, Report 7) and the Missing Discovery Demand Letter.

---

## STEP 7 — Source Catalog (PDF) · MANDATORY

Standalone PDF indexing every Source Register entry: cover page, contents, per-source detail sheets, Missing Discovery table, Cross-Reference Matrix. **No date column.** → `references/source-exhibit-catalog.md`

---

## STEP 8 — Combined Sources (PDF) · MANDATORY

All source PDFs merged, each behind a divider page carrying source number and metadata. → `references/combined-source-documents.md`

---

## STEP 8.5 — Red-Team the Outline

**Self-check — do not hand this to `dw-adversarial-stress-test-crim`;** that skill runs *into* this one, not out of it (see `references/integration-map.md`). If a theory stress test exists it is an upstream input at Step 0.58 — the cross must not open a door the theory cannot survive.

Work the nine-target checklist, report what you found and changed, and surface what you cannot fix. Optional on Fast Path — note it in the notice. → `references/red-team-checklist.md`

---

## Deliverable Checklist

Three files, one folder, per `assets/outline-assembly.md`:

`Cross-Examination — [Witness Name].docx` · `Source Catalog — [Witness Name].pdf` · `Combined Sources — [Witness Name].pdf`

Times New Roman 14 pt, page numbers bottom right. Run the pre-delivery check in `references/deliverable-formatting.md` §5, then present all three.

---

## Guardrails

Full list loaded at Step 0.5 → `references/guardrails.md`. The six that most often go wrong:

1. **Name which Fifth Circuit.** `5th Cir.` (U.S., the federal default) vs. `La. 5th Cir.` — never a bare "5th Circuit." For state appeals, resolve the parish's own Louisiana circuit.
2. **Scope is wide open in state court** (art. 611(B)) — do not `[SCOPE FLAG]` a question merely because it exceeded direct.
3. **Art. 608(B) bars specific-acts character attacks.** Four lawful routes: 609.1 conviction · 607(D)(1) bias · 607(C) accuracy of this testimony · 613 prior inconsistent statement. Otherwise `[608(B) REVIEW REQUIRED]`.
4. **Prior convictions are art. 609.1, never 609.**
5. **Preserve every flag** — ground stated at the moment (art. 841) plus substance proffered (art. 103(A)(2)).
6. **Cite every fact** with an `(N)` prefix; nothing untraceable is asserted as fact.

---

## File Index

Each step names the files it needs. **Load those and no others.**

**`assets/`** — copied into the deliverable or governing how it is built:
`fast-path-notice` · `pre-draft-confirmation` · `outline-assembly` · `chapter-goals-and-scoring` · `impeachment-bullet` · `preservation-log`

**`references/`** — read for detail:
`guardrails` · `deliverable-formatting` · `jurisdiction-and-court-map` · `quick-reference-tables` · `error-preservation-protocol` · `build-paths` · `upstream-intake` · `witness-history-lookup` · `integration-map` · `witness-prioritization-audit` · `information-tiers` · `master-witness-table` · `witness-type-modules` · `agency-and-lab-module` · `confrontation-and-surrogate-analysts` · `source-register-and-template` · `source-exhibit-catalog` · `combined-source-documents` · `red-team-checklist`

---

*Part of the Daniels & Washington Cowork criminal defense toolkit. Pair with `dw-criminal-defense-crim` for Phase 3 integration.*

**Criminal only** — no civil or PI cross-examination. Upstream producers, downstream consumers, contract bindings, and the `dw-adversarial-stress-test-crim` direction warning: `references/integration-map.md`.
