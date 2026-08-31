---
name: dw-witness-threat-matrix-crim
category: trial-prep
description: "Build a Top 5 witness threat matrix by witness type for a criminal case at Daniels & Washington. ALWAYS invoke for \"witness threat matrix,\" \"key witnesses,\" \"top witnesses,\" \"rank the witnesses,\" \"most dangerous witnesses,\" \"witness priority,\" \"witness damage score,\" \"witness vulnerability,\" \"who do we cross hardest,\" \"witness ranking,\" \"refresh the threat matrix,\" \"update threat matrix after crosses,\" \"post-cross refresh,\" \"crosses are done — update the matrix,\" or \"rescore the witnesses.\" Phase 3 analytical capstone. Synthesizes existing case deliverables into ranked Top 5 lists per witness type with separate Damage and Vulnerability scores, source citations, impeachment hooks, and recommended defense actions. Includes Post-Cross Refresh Mode. Feeds dw-cross-exam-architect-crim. Do NOT use for discovery triage (dw-discovery-orchestrator-crim) or for drafting actual cross outlines (dw-cross-exam-architect-crim)."
---

# dw-witness-threat-matrix-crim

Phase 3 capstone that ranks the State's witnesses by threat level so the defense knows where to spend cross-exam prep time. Synthesis-only — does NOT re-read raw discovery.

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any witness statements, threat assessments, jail call recordings, social media posts, prior criminal records, or BWC of witness contacts, do not analyze anything yet.**

Your only response must be:

> *"Before I begin — are you uploading any additional witness statements, threat assessments, jail call recordings, social media posts, prior criminal records, or BWC of witness contacts? I'll start the threat matrix analysis only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception, including post-cross refresh runs where new impeachment material is being added.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting the threat matrix, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to the threat matrix header. The matrix is internal work product, never a filed pleading.
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `{{CASE_ROOT}}`).

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product. Output paths follow the Cowork Analysis / Witnesses formula:

```
{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/
```

with the threat matrix `.docx` saved at `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Witness Threat Matrix - [Last Name] - [YYYY-MM-DD].docx`. If any required Case Brain variable (`{{CASE_ROOT}}`, `{{DEFENDANT_NAME}}`, `{{DOCKET}}`) is missing, prompt the attorney before drafting.

---

## Source Citation Mandate

Every harmful-content claim and impeachment hook in the threat matrix must trace back to a specific source document. The matrix drives cross-exam prep priority and resource allocation — an unsourced "Damage 9" rating sends the defense down the wrong road and wastes prep time on the wrong witness.

**Citation format:** Cite the document title, page number, and paragraph or timestamp. Examples:
- `(Witness Statement — Smith, 03/15/2026, p. 2, para. 4)`
- `(BWC — Officer Jones, Timestamp 00:05:32)`
- `(DMAR Report, Section 3, p. 7)`
- `(Jail Call — Client to Mother, 02/14/2026, 04:18)`
- `(Brady/Giglio Audit, p. 12, Cooperator Deal Section)`
- `(Discovery Production, Bates #00145)`

**Multiple-source rule:** When more than one document confirms a fact about a witness, cite all of them — e.g., `(Witness Statement — Smith, p. 2; BWC — Officer Jones, Timestamp 00:05:32)`.

**Unsourced assertions:** If a Damage or Vulnerability claim cannot be tied to a specific document, mark it `[UNSOURCED — VERIFY]` so the attorney knows to confirm before relying on it. Do NOT score a witness CRITICAL without at least one cited source for the damage claim.

**Where sourcing applies:** All harmful-content entries, impeachment hooks, prior-inconsistency callouts, and bias/deal/motive findings. Witness type classification and scoring rationale must reference upstream deliverables (DMAR, Brady/Giglio audit, eyewitness audit, etc.) by name.

---

## Inputs

- `CASE_ROOT` — absolute path to client case folder
- Case Brain (via `dw-case-brain-crim`) for State's theory and contested elements
- Phase 1–3 deliverables in `CASE_ROOT`: DMAR, Brady/Giglio audit, Discovery Compliance Ledger, Video Audit, Forensic Dump Analysis, Eyewitness ID Audit, Confession/Interrogation Audit, Expert Witness Evaluations
- Every `.docx` already in `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/` (existing cross-exam outlines, named `Cross-Examination — [Witness Name].docx` per dw-data-contracts-crim Contract 3)

If the State's witness list is missing, STOP and tell the attorney to file a Bill of Particulars / motion to compel first. Do not invent witnesses.

## Witness types (assign exactly one)

1. **Lay Eyewitness** — civilian percipient witness
2. **Law Enforcement** — sworn officers, detectives, supervisors
3. **Expert** — noticed under La. C.E. 702 / Daubert / Foret
4. **Cooperator / Informant** — co-defendants, jailhouse witnesses, CIs, deal witnesses
5. **Custodian / Foundation** — records custodians, evidence techs, lab personnel
6. **Civilian Corroborator** — context witnesses, not percipient

## Scoring (independent, 1–10)

**Damage** — how badly they hurt unchallenged.
- 9–10: State's case collapses without them
- 7–8: Major proof of contested element, hard to replace
- 5–6: Meaningful but cumulative corroboration
- 3–4: Background/context only
- 1–2: Marginal

**Vulnerability** — how attackable they are.
- 9–10: Multiple Brady/Giglio hits, prior inconsistencies, deal, bias
- 7–8: One strong impeachment vector
- 5–6: Some impeachment, requires foundation
- 3–4: Limited attack surface
- 1–2: Clean

**Priority** (derived):
- **CRITICAL** — Damage ≥ 7 AND Vulnerability ≥ 6
- **HIGH** — Damage ≥ 7 OR (Damage ≥ 5 AND Vulnerability ≥ 7)
- **MEDIUM** — Damage 4–6 with some vulnerability
- **LOW** — everything else

## Process

1. Load State's witness list from Case-Tables excel document.  Look at the `Witness List` sheet (single consolidated sheet; use its `Priority (1–5)` column and `Witness Name`).
2. Classify each witness by type.
3. Score Damage and Vulnerability independently from upstream deliverables. Every harmful claim must have a source citation. Do not score CRITICAL without at least one cited source.
4. Select Top 10 per type. If a type has fewer than 10, list all and note count. If zero, omit and note in Gap Report.
5. Build per-type matrix tables (columns below).
6. Build the Cross-Exam Priority Heat Map — single table sorted by Priority, then Damage descending.
7. Build the **Missing Witness Gap Report** — names appearing in police reports, BWC, jail calls, or witness statements with apparent percipient knowledge, no statement produced, and not on the State's list. Cross-reference Discovery Ledger.
8. Build the **Deliverable Gap Report** — Top 10 witnesses missing the corresponding upstream audit (e.g., noticed expert with no `dw-expert-witness-evaluator-crim` output, eyewitness ID witness with no `dw-eyewitness-identification-auditor-crim` output, custodial statement with no `dw-confession-interrogation-auditor-crim` output, any witness with no cross outline).
9. Write `.docx` (structure below).
10. Update Case Brain "Witness Strategy" section with date, top 5 CRITICAL witnesses, file path, open gaps.
11. Handoff: name top 5 CRITICAL witnesses, count of cross outlines still needed, any discovery gaps warranting a motion to compel.

**After building the initial threat matrix, it should be refreshed whenever a batch of cross-examination outlines is completed or updated. Use the Post-Cross Refresh Mode (see below) for this.**

## Matrix table columns

`# | Witness (name + role + type) | Why They Matter (1 sentence — element proved) | Harmful Content | Source (path / Bates / DMAR cite / timestamp) | Impeachment Hooks | Damage | Vulnerability | Priority | Defense Action | Cross Outline Status`

Cross Outline Status comes from actually scanning `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/`: "Drafted" (with file link), "In progress," or "Not started."

## Document structure

1. Cover page (caption, docket, date, attorney)
2. Executive Summary — top 10 CRITICAL witnesses across all types
3. State's Theory Snapshot (from Case Brain)
4. Top 5 tables, one per witness type (skip empty types)
5. Cross-Exam Priority Heat Map (sorted by Priority, then Damage)
6. Missing Witness Gap Report
7. Deliverable Gap Report
8. Recommended Next Steps — ordered list of skills to run next, by priority
9. Score Change Log (REFRESH MODE only)

## Output location

Apply the output-path formula from `dw-shared-protocols-crim/references/output-path-formula.md` (anchored on `{{CASE_ROOT}}`):

```
{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Witness Threat Matrix - [Last Name] - [YYYY-MM-DD].docx
```

Create `01 - Trial Notebook/03 - Witnesses/` if it does not exist. Apply attorney work-product marking per `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — the matrix is an internal deliverable, never filed.

## Run modes

**TRIAGE MODE** (default — no prior matrix exists). Runs after Phase 3 audits and BEFORE most cross outlines exist. Tells the attorney which witnesses deserve a `dw-cross-exam-architect-crim` build and in what order. Cross Outline Status will mostly read "Not started." Recommended Next Steps lists every CRITICAL/HIGH witness as a cross-exam-architect candidate in priority order.

**REFRESH MODE** (prior matrix exists). Runs AFTER cross outlines have been drafted for at least the CRITICAL witnesses. Refines Vulnerability scores using impeachment hooks discovered during cross prep, updates Cross Outline Status, and converts the matrix from prep planner into trial-prep dashboard.

Refresh process:
1. Load most recent prior matrix from `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/`
2. Re-scan upstream deliverables AND every cross-exam outline now present
3. Re-score every witness; add any newly-identified witnesses
4. Record deltas in a **Score Change Log** table for any witness whose Damage or Vulnerability moved ≥ 2 points OR whose Priority tier changed: `Witness | Prior D/V/Priority | New D/V/Priority | Reason | Source of New Information`
5. Refresh Cross Outline Status and both Gap Reports
6. Save with versioned filename — do NOT overwrite the prior matrix:
   ```
   Witness Threat Matrix - [Last Name] - [YYYY-MM-DD] - v[N].docx
   ```
   `[N]` increments from highest existing version. Original triage matrix has no suffix and is preserved as baseline.
7. Update Case Brain: "Refreshed [date] — [N] score changes, [N] tier changes"
8. Handoff explicitly calls out: witnesses whose Priority tier changed, witnesses still without a cross outline despite CRITICAL/HIGH priority, and whether the case is ready for `dw-trial-notebook-builder-crim`.

**Mode detection:**
- No prior matrix → TRIAGE MODE
- Prior matrix + attorney did not specify → ask which mode
- "refresh / update / re-score" → REFRESH MODE
- "rebuild from scratch / start over" → TRIAGE MODE

## Post-Cross Refresh Mode

**Trigger phrases:** "refresh the threat matrix," "update threat matrix after crosses," "post-cross refresh," "crosses are done — update the matrix," "rescore the witnesses"

**When to use:** After building or updating cross-examination outlines for multiple witnesses, use this mode to rescore the matrix based on new intelligence discovered during cross-exam prep.

**Workflow:**

1. **Detect Recent Cross-Exam Work** — Scan `<case-root>/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/` for cross-examination outlines. Compare file modification dates against the current threat matrix to identify which crosses are newer than the last matrix build.

2. **Extract New Intelligence** — For each updated/new cross-exam outline, extract:
   - Number of chapters and questions (scope indicator)
   - Chapter Goals and Impact/Fragility scores (for law enforcement witnesses)
   - Impeachment bullets identified (count and severity)
   - Discovery gaps flagged
   - Key concessions targeted
   - Source documents available vs. missing

3. **Rescore Witnesses** — Update Damage and Vulnerability scores based on new cross-exam intelligence:
   - **Damage score increases** if: more impeachment material found, more inconsistencies documented, more SOP violations identified
   - **Damage score decreases** if: witness concessions are limited, testimony is largely consistent
   - **Vulnerability score increases** if: cross has strong impeachment chapters, prior inconsistent statements documented, fragility ratings are low (witness likely to concede)
   - **Vulnerability score decreases** if: witness has few impeachment points, high fragility ratings (will fight hard)

4. **Delta Report** — Present a comparison showing:
   - Previous Damage/Vulnerability scores vs. updated scores for each affected witness
   - New impeachment hooks discovered since last matrix build
   - Witnesses who moved up or down in priority ranking
   - Any new witnesses added (crosses built for previously unranked witnesses)
   - Any witnesses still missing cross-examination outlines

5. **Update the Matrix Document** — Regenerate the threat matrix .docx with updated scores, rankings, and intelligence summaries. Save as a new versioned file (do not overwrite the prior matrix).

6. **Downstream Recommendations** — After refresh, suggest:
   - Which witnesses now warrant additional investigation (dw-defense-investigator-tasking-crim)
   - Which witnesses have enough impeachment material to draft a full cross-exam outline (if one doesn't exist yet)
   - Whether the defense theory or case theme should be adjusted based on the updated threat landscape

**Guardrail: The Post-Cross Refresh always produces a delta report showing score changes before updating the matrix document. Never silently update scores.**

## Guardrails

- Do NOT invent witnesses. If the State's list is missing, stop.
- Do NOT score CRITICAL without a cited source for the damage claim.
- Do NOT re-read raw discovery PDFs. If an upstream deliverable is missing, flag it in the Deliverable Gap Report.
- Do NOT draft cross-exam questions — that's `dw-cross-exam-architect-crim`.
- Defense witnesses are out of scope.
- **Post-Cross Refresh always produces a delta report showing score changes before updating the matrix document. Never silently update scores.**