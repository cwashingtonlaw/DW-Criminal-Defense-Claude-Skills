---
name: dw-theory-deconstructor-crim
category: analysis
description: >
  ALWAYS invoke for "deconstruct the theory," "deconstruct the state's theory,"
  "facts vs inferences," "theory analysis," "Report 2a," "what are the assumptions,"
  "break down the prosecution's case," "logical analysis," or "assumption audit."
  Do NOT use for building the defense narrative — use dw-criminal-defense-crim Report 4.
  Do NOT use for stress-testing — use dw-adversarial-stress-test-crim.
---

# D&W Theory Deconstructor (Report 2a)
**Daniels & Washington | Criminal Defense | Louisiana / 5th Circuit Default**

This skill is **Report 2a** in the Barone Discovery Workflow. It takes the prosecution's case summary (Report 2) and systematically decomposes the State's theory — and optionally any defense theory — into three categories: (1) **verified facts** supported by discovery, (2) **inferences** drawn from those facts, and (3) **assumptions** not supported by evidence. For each element of the charged offense, it maps what the State actually HAS (evidence), what the State is INFERRING (logical leaps from evidence), and what the State is ASSUMING (assertions without evidentiary support). This structured decomposition reveals the logical scaffolding of each theory and identifies where it is strongest and where it is weakest.

The deliverable arms the attorney with a clear-eyed inventory of every logical step the prosecution must take to connect its evidence to a conviction. Where the inferential chain is strong, the defense knows to avoid frontal attacks. Where it is weak — particularly where it depends on assumptions unsupported by discovery — the defense knows exactly where to strike.

**Cowork drafts; attorney approves.** Every output is a draft for attorney review. The attorney verifies facts, confirms legal arguments, and makes all strategic decisions. This skill never represents its work product as final or filed.

---

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any discovery files, case documents, Report 2 outputs, police reports, witness statements, forensic reports, or other case materials, do not analyze anything yet.**

Your only response must be:
> *"Before I begin — are you uploading any additional discovery files, case documents, police reports, witness statements, forensic reports, or the Report 2 (Prosecution's Case Summary)? I'll start the theory deconstruction only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** Theory deconstruction depends on a complete picture of what the State has and does not have. Mid-analysis discovery of additional evidence — a new witness statement, a forensic report, or a supplemental police narrative — would require re-evaluation of the entire fact/inference/assumption classification, invalidating prior work.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all Report 2a headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `{{CASE_ROOT}}`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula:

```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/
```

If any required Case Brain variable (`{{DEFENDANT_NAME}}`, `{{DOCKET}}`, `{{PARISH}}`, `{{COURT}}`, `{{JUDGE_NAME}}`, `{{ADA_NAME}}`) is missing, prompt the attorney before drafting.

---

### Source Citation Mandate

Every factual assertion in the Theory Deconstruction Report must trace back to a specific source document. The entire purpose of this skill is to distinguish what is grounded in evidence from what is not — unsourced factual claims would defeat the analytical framework.

**Citation format:** Cite the document title, page number, and paragraph, Bate stamp, or timestamp. Examples:
- `(Arrest Report — LCPD Case #2026-00456, p. 3, para. 2)`
- `(Victim Statement, Bates #00145, p. 1, para. 3)`
- `(BWC — Officer Smith, Timestamp 00:12:44)`
- `(Lab Report — Toxicology, Bates #00312, p. 2, Results Section)`
- `(Report 2 — Prosecution's Case Summary, Section III, Element 2)`
- `(Case Tables.xlsx — Evidence Table, Row 14)`
- `(Discovery Production, Bates #00145-00148)`
- `(911 Audio, Timestamp 00:02:15)`

**Multiple-source rule:** When more than one document supports a fact, cite all of them — e.g., `(Arrest Report, p. 3, para. 2; BWC — Officer Smith, Timestamp 00:12:44)`.

**Unsourced assertions:** If a factual claim cannot be tied to a specific document, mark it `[UNSOURCED — VERIFY]` so the attorney knows to confirm or remove it before relying on the deliverable.

**Where sourcing applies:** All factual content — fact extraction (Module B), element mapping (Module A), and the evidentiary basis for each inference (Module C). Legal elements and standards follow normal legal citation format.

---

## STEP 1 — Information Gathering Protocol

Before performing the theory deconstruction, collect the following in ranked order:

### Essential (must have before deconstructing)
1. **Report 2 — Prosecution's Case Summary:** the completed Report 2 output from `dw-criminal-defense-crim` Phase 2 Step 2. This is the primary input. If Report 2 does not exist, STOP and route the attorney to generate it first — theory deconstruction without a prosecution case summary is premature.
2. **Charges:** all counts with statutory citations (La. R.S. numbers) and the elements of each charged offense. If a charge-type specialist has already built the element grid (e.g., `dw-violent-crime-specialist-crim` Module A, `dw-drug-offense-specialist-crim` Module A), read that output.
3. **Discovery files:** the full discovery production, organized and Bate-stamped per Phase 1 Step 2 of `dw-criminal-defense-crim`. At minimum, the key evidence documents referenced in Report 2.
4. **Case Tables.xlsx — Evidence Table:** the populated evidence index with Review Priority and Defense Relevance columns from Phase 1 Step 4.

### Strategic (request if not provided)
5. **Case Profile (000 - Case Profile.docx):** defendant demographics, case posture, identified defenses.
6. **Report 3 — Immediate Red Flags:** constitutional issues, suppression candidates, and evidence-reliability concerns already identified.
7. **Charge-type specialist output:** element-by-element defense theory map (Module B of the applicable specialist skill).
8. **Defense theory draft:** any preliminary defense narrative from Report 4 or attorney direction — used for optional defense-theory deconstruction.

### Contextual (gather from uploaded files)
9. **Witness statements and interview transcripts:** for cross-referencing fact claims against witness accounts.
10. **Forensic and lab reports:** for verifying scientific evidence claims.
11. **Case Brain:** structured case context from `dw-case-brain-crim`.

**Present missing essential items as a ranked checklist before deconstructing.** If items 1-3 are missing, do not proceed — ask for them first. Report 2 is a hard prerequisite.

---

## STEP 2 — MODULE A: Element Mapping

For each element of each charged offense, systematically map the State's evidentiary support. This module builds the structural skeleton that the remaining modules flesh out.

A.1 pull or import the element grid per count; A.2 map each element to direct evidence, circumstantial evidence (noting the inference required), or `[NO EVIDENCE IN DISCOVERY]`; A.3 classify each element DIRECT / INFERENTIAL / ASSUMED / CONTESTED / SUPPRESSION CANDIDATE.

Read `references/module-a-element-mapping.md` now for the grid template and the classification definitions.

---

## STEP 3 — MODULE B: Fact Extraction

Extract every verifiable fact from the discovery — things that are objectively documented and not subject to interpretation.

B.1 organize facts as physical, documentary, testimonial, forensic, or timeline; B.2 tag each `[VERIFIED]` / `[MULTI-SOURCE VERIFIED]` / `[UNVERIFIED]` / `[CONTRADICTED]` / `[CONTESTED]`; B.3 enter every fact in the Fact Inventory Table with source, Bate stamp, status, and element(s) supported.

Read `references/module-b-fact-extraction.md` now for the category definitions, status criteria, and table template.

---

## STEP 4 — MODULE C: Inference Identification

Identify every inference the prosecution draws — or must draw — from the verified facts to connect evidence to charged elements.

C.1 state each inference, cite its underlying Fact Inventory numbers, rate it STRONG / MODERATE / WEAK, and note alternative inferences (feeds Module F); C.2 map stacked chains (`Fact(s) → Inference A → Inference B → Element`) — any WEAK link is a defense target; C.3 complete the Inference Table.

Read `references/module-c-inference-identification.md` now for the strength criteria, chain analysis, and table template.

---

## STEP 5 — MODULE D: Assumption Audit

Identify every assumption the prosecution makes that is NOT supported by evidence in the discovery. Assumptions are the weakest points in any theory — they are assertions the State needs the jury to accept without proof.

D.1 state each assumption, explain why it is unsupported, identify what evidence would cure it, and rate defense challenge viability HIGH / MEDIUM / LOW; D.2 complete the Assumption Table with element affected and a brief defense strategy note.

Read `references/module-d-assumption-audit.md` now for the viability criteria and table template.

---

## STEP 6 — MODULE E: Gap Analysis Matrix

Synthesize the outputs of Modules A through D into a single summary matrix showing, for each element of each charged offense, the complete logical path from evidence to proof.

E.1 build the Element Gap Matrix (evidence, inferences and strength, assumptions and viability, overall vulnerability, defense opportunity); E.2 rate each element FORTIFIED / SOLID / EXPOSED / VULNERABLE / CRITICAL GAP (the last signals possible La. C.Cr.P. Art. 778 / 821 relief); E.3 write the 2-3 paragraph Prosecution Theory Strength Summary.

Read `references/module-e-gap-analysis-matrix.md` now for the matrix template and rating criteria.

---

## STEP 7 — MODULE F: Alternative Inference Table

For each prosecution inference identified in Module C, propose the strongest defense counter-inference that can be drawn from the same underlying facts. This module feeds directly into `dw-criminal-defense-crim` Report 4 (Competing Theories) and provides the raw material for defense narrative construction.

F.1 for each prosecution inference propose the strongest defense counter-inference from the same facts, rate it, and cite supporting evidence; F.2 complete the Alternative Inference Table with a Report 4 theme tag; F.3 identify 2-3 defense narrative seeds with supporting counter-inferences, remaining gaps, and compatibility notes. **Do not advocate for a particular defense theory** — present alternatives neutrally; the attorney selects.

Read `references/module-f-alternative-inference.md` now for the five-step development protocol and table template.

---

## STEP 8 — Output Format

### Primary Deliverable: Report 2a — Theory Deconstruction (.docx)

**Filename:** `Report 2a - Theory Deconstruction - {{DEFENDANT_LAST}} - {{YYYY-MM-DD}}.docx`

**Location:** `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

**Contents:** work-product header; Executive Summary; Sections 1-6 (Modules A-F in order); Section 7 Prosecution Theory Strength Summary; Section 8 Recommended Next Steps (elements to target, investigation, discovery demands, experts, motions); Source Citation Appendix.

Read `references/report-2a-contents.md` now for the required content of each of the eleven sections.

### Case Brain Update

After producing Report 2a, update `dw-case-brain-crim` with:
- Theory deconstruction completion status
- Number of VULNERABLE and CRITICAL GAP elements identified
- Key assumptions flagged for defense exploitation
- Pointer to the Report 2a file path

---

## Cross-Skill Integration

Reads Report 2 (hard prerequisite), Report 3, Case Tables.xlsx, Case Brain, and charge-type specialist element grids; feeds `dw-criminal-defense-crim` Report 4 (Module F), `dw-adversarial-stress-test-crim` (Modules D–E), and `dw-theory-to-workplan-crim`. Read `references/cross-skill-integration.md` for the full tables and workflow-position diagram.

---

## Guardrails

1. **Source Citation Mandate.** Every fact in the Fact Inventory (Module B) must cite its source document with Bate stamp or timestamp. Every inference (Module C) must trace to underlying facts. Every assumption (Module D) must explain why evidentiary support is absent. Unsourced claims are marked `[UNSOURCED — VERIFY]` and never appear in a final deliverable.

2. **Verification Protocol required.** Every extracted fact must carry a verification status: `[VERIFIED]`, `[MULTI-SOURCE VERIFIED]`, `[UNVERIFIED]`, `[CONTRADICTED]`, or `[CONTESTED]`. Do not classify a fact as verified without confirming the source document supports it.

3. **No fabricated citations.** Every Louisiana statute, code article, and case citation must be verifiable. If a citation cannot be verified, mark it `[VERIFY CITATION]`. Anchor authorities listed in CLAUDE.md may be cited without a flag.

4. **Do not argue for a particular defense theory.** Module F presents alternative inferences and defense narrative seeds neutrally. The attorney selects the theory. This skill provides the analytical foundation — it does not advocate. Present all viable alternatives with their respective strengths and weaknesses.

5. **Cowork drafts; attorney approves.** Every output is a draft for attorney review. The attorney verifies facts, confirms the fact/inference/assumption classifications, and makes all strategic decisions about which weaknesses to exploit. This skill never represents its work product as final or filed.

6. **Report 2 is a hard prerequisite.** Do not attempt theory deconstruction without a completed Report 2. If Report 2 does not exist, direct the attorney to generate it first via `dw-criminal-defense-crim` Phase 2 Step 2. Deconstructing a theory that has not been articulated produces unreliable analysis.

7. **Do not speculate beyond the discovery.** The Assumption Audit (Module D) identifies what the State is assuming — it does not speculate about what undisclosed evidence the State might have. If additional discovery is anticipated, note it in the Recommended Next Steps but do not incorporate speculative evidence into the element mapping.

8. **Suppression candidates affect element mapping.** When Report 3 or `dw-suppression-motion-crim` has identified evidence that may be excludable, note this in the Element Mapping (Module A) with the `SUPPRESSION CANDIDATE` classification. The Gap Analysis Matrix (Module E) should reflect the element's vulnerability both with and without the challenged evidence.

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **module-a-element-mapping.md** — Step 2: element grid, evidence-to-element mapping, sufficiency classifications
- **module-b-fact-extraction.md** — Step 3: fact categories, verification protocol, Fact Inventory Table
- **module-c-inference-identification.md** — Step 4: inference extraction, strength scale, chain analysis, Inference Table
- **module-d-assumption-audit.md** — Step 5: assumption identification, challenge-viability scale, Assumption Table
- **module-e-gap-analysis-matrix.md** — Step 6: Element Gap Matrix, vulnerability ratings, theory strength summary
- **module-f-alternative-inference.md** — Step 7: counter-inference development, Alternative Inference Table, defense narrative seeds
- **cross-skill-integration.md** — Cross-Skill Integration: READS FROM / FEEDS tables and workflow-position diagram
- **report-2a-contents.md** — Step 8: the eleven-section contents specification for Report 2a

It also relies on:

- **Report 2 output** — the prosecution's case summary generated by `dw-criminal-defense-crim` Phase 2 Step 2
- **Case Tables.xlsx** — the evidence index and witness tables from Phase 1 Step 4
- **Charge-type specialist element grids** — from `dw-violent-crime-specialist-crim`, `dw-drug-offense-specialist-crim`, `dw-dwi-specialist-crim`, `dw-sex-offense-specialist-crim`, or `dw-firearms-specialist-crim` as applicable
- **dw-shared-protocols-crim/references/attorney-work-product-marking.md** — work product marking standard
- **dw-shared-protocols-crim/references/output-path-formula.md** — output path convention

---

*This skill is part of the Daniels & Washington criminal defense toolkit. It is Report 2a in the Barone Discovery Workflow. Pair with dw-criminal-defense-crim for the full case analysis pipeline, dw-adversarial-stress-test-crim for stress-testing the weaknesses identified here, and dw-theory-to-workplan-crim for converting the deconstruction into an actionable defense workplan.*
