---
name: dw-theory-deconstructor
category: analysis
description: >
  ALWAYS invoke for "deconstruct the theory," "deconstruct the state's theory,"
  "facts vs inferences," "theory analysis," "Report 2a," "what are the assumptions,"
  "break down the prosecution's case," "logical analysis," or "assumption audit."
  Do NOT use for building the defense narrative — use dw-criminal-defense Report 4.
  Do NOT use for stress-testing — use dw-adversarial-stress-test.
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

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all Report 2a headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `{{CASE_ROOT}}`)

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
1. **Report 2 — Prosecution's Case Summary:** the completed Report 2 output from `dw-criminal-defense` Phase 2 Step 2. This is the primary input. If Report 2 does not exist, STOP and route the attorney to generate it first — theory deconstruction without a prosecution case summary is premature.
2. **Charges:** all counts with statutory citations (La. R.S. numbers) and the elements of each charged offense. If a charge-type specialist has already built the element grid (e.g., `dw-violent-crime-specialist` Module A, `dw-drug-offense-specialist` Module A), read that output.
3. **Discovery files:** the full discovery production, organized and Bate-stamped per Phase 1 Step 2 of `dw-criminal-defense`. At minimum, the key evidence documents referenced in Report 2.
4. **Case Tables.xlsx — Evidence Table:** the populated evidence index with Review Priority and Defense Relevance columns from Phase 1 Step 4.

### Strategic (request if not provided)
5. **Case Profile (000 - Case Profile.docx):** defendant demographics, case posture, identified defenses.
6. **Report 3 — Immediate Red Flags:** constitutional issues, suppression candidates, and evidence-reliability concerns already identified.
7. **Charge-type specialist output:** element-by-element defense theory map (Module B of the applicable specialist skill).
8. **Defense theory draft:** any preliminary defense narrative from Report 4 or attorney direction — used for optional defense-theory deconstruction.

### Contextual (gather from uploaded files)
9. **Witness statements and interview transcripts:** for cross-referencing fact claims against witness accounts.
10. **Forensic and lab reports:** for verifying scientific evidence claims.
11. **Case Brain:** structured case context from `dw-case-brain`.

**Present missing essential items as a ranked checklist before deconstructing.** If items 1-3 are missing, do not proceed — ask for them first. Report 2 is a hard prerequisite.

---

## STEP 2 — MODULE A: Element Mapping

For each element of each charged offense, systematically map the State's evidentiary support. This module builds the structural skeleton that the remaining modules flesh out.

### A.1 — Identify Elements

Pull the elements of each charged offense from the statutory text (La. R.S. citations). If a charge-type specialist has already built the element grid, import it. Otherwise, build from scratch:

| Count | Charge | Statute | Element 1 | Element 2 | Element 3 | Element N |
|-------|--------|---------|-----------|-----------|-----------|-----------|
| 1 | [Charge] | La. R.S. ___:___ | [Element] | [Element] | [Element] | [Element] |

### A.2 — Map Evidence to Elements

For each element, identify:

1. **Direct evidence** — evidence that, if believed, proves the element without requiring any inferential step. Cite the specific document and Bate stamp.
2. **Circumstantial evidence** — evidence that requires an inference to connect it to the element. Cite the document and note the inferential step required.
3. **No evidence** — the element has no evidentiary support in the current discovery. Mark `[NO EVIDENCE IN DISCOVERY]`.

### A.3 — Classify Evidentiary Sufficiency

For each element, assign a sufficiency classification:

| Classification | Meaning |
|---------------|---------|
| **DIRECT** | Direct evidence supports this element; no inferential leap required |
| **INFERENTIAL** | Evidence exists but requires one or more inferences to connect to the element |
| **ASSUMED** | No evidence directly supports this element; the State must assume it |
| **CONTESTED** | Competing evidence exists — some supports, some contradicts |
| **SUPPRESSION CANDIDATE** | Evidence exists but may be excludable (cross-reference Report 3) |

---

## STEP 3 — MODULE B: Fact Extraction

Extract every verifiable fact from the discovery — things that are objectively documented and not subject to interpretation.

### B.1 — Fact Categories

Organize extracted facts by category:

- **Physical evidence facts:** items seized, locations, quantities, conditions (cite evidence logs, inventory receipts, lab reports)
- **Documentary facts:** dates, times, records, financial transactions, communications (cite documents by Bate stamp)
- **Testimonial facts:** statements made by witnesses or the defendant that are direct quotes or objectively verifiable claims (cite transcripts, statements, BWC timestamps)
- **Forensic facts:** lab results, DNA profiles, toxicology readings, ballistics matches, digital forensic artifacts (cite lab reports by Bate stamp and page)
- **Timeline facts:** undisputed chronological events with source documentation (cite 911 logs, CAD records, BWC timestamps, surveillance footage)

### B.2 — Verification Protocol

For each extracted fact, apply the verification protocol:

| Status | Criteria |
|--------|----------|
| **[VERIFIED]** | Fact is documented in at least one discovery item AND is not contradicted by any other discovery item |
| **[MULTI-SOURCE VERIFIED]** | Fact is documented in two or more independent discovery items |
| **[UNVERIFIED]** | Fact appears in one source but cannot be independently confirmed; no contradiction found |
| **[CONTRADICTED]** | Fact is asserted in one source but contradicted by another — cite both sources |
| **[CONTESTED]** | Fact is disputed between witnesses or between witness accounts and physical evidence |

### B.3 — Fact Inventory Table

| # | Fact | Category | Source(s) | Bate Stamp | Verification Status | Element(s) Supported |
|---|------|----------|-----------|------------|--------------------|--------------------|
| 1 | [Statement of fact] | [Category] | [Document] | [Bate #] | [Status] | [Element ref] |

---

## STEP 4 — MODULE C: Inference Identification

Identify every inference the prosecution draws — or must draw — from the verified facts to connect evidence to charged elements.

### C.1 — Inference Extraction

For each inference:

1. **State the inference** — what conclusion is the prosecution drawing?
2. **Identify the underlying fact(s)** — what verified facts (from Module B) support this inference? Cite by Fact Inventory number.
3. **Assess inferential strength:**

| Strength | Criteria |
|----------|----------|
| **STRONG** | The inference follows logically and almost inevitably from the facts; few reasonable alternative explanations exist |
| **MODERATE** | The inference is reasonable but not the only logical conclusion; alternative explanations exist and are plausible |
| **WEAK** | The inference requires a significant logical leap; multiple equally plausible or more plausible alternatives exist |

4. **Identify the alternative inference(s)** — what other conclusions could a reasonable person draw from the same facts? This feeds Module F.

### C.2 — Inference Chain Analysis

Some prosecution theories require stacked inferences — Inference A must be accepted before Inference B is possible, and Inference B must be accepted before Inference C connects to the element. Map the chain:

```
Fact(s) → Inference A (strength) → Inference B (strength) → Element
```

Stacked inferences compound weakness. A chain with two MODERATE links is weaker than either link alone. A chain with any WEAK link is a defense target.

### C.3 — Inference Table

| # | Inference | Underlying Fact(s) | Strength | Element Supported | Alternative Inference(s) | Chain Position |
|---|-----------|-------------------|----------|------------------|------------------------|----------------|
| 1 | [Inference] | Fact #[N], #[N] | STRONG/MOD/WEAK | [Element ref] | [Alternatives] | Standalone / Chain [X] Link [N] |

---

## STEP 5 — MODULE D: Assumption Audit

Identify every assumption the prosecution makes that is NOT supported by evidence in the discovery. Assumptions are the weakest points in any theory — they are assertions the State needs the jury to accept without proof.

### D.1 — Assumption Identification

For each assumption:

1. **State the assumption** — what is the prosecution taking for granted?
2. **Explain why it is unsupported** — what evidence would be needed to convert this assumption into a fact, and why is that evidence absent?
3. **Identify what evidence would cure it** — if this assumption were converted to a verified fact, what document or testimony would do it? This identifies both discovery gaps the State might fill and investigation opportunities for the defense.
4. **Assess defense challenge viability:**

| Viability | Criteria |
|-----------|----------|
| **HIGH** | The assumption is demonstrably false or contradicted by existing evidence — the defense can affirmatively disprove it |
| **MEDIUM** | The assumption is unsupported but not contradicted — the defense can highlight the gap but cannot affirmatively disprove it |
| **LOW** | The assumption is unsupported but common-sense plausible — the jury may accept it without evidence, making it harder to challenge |

### D.2 — Assumption Table

| # | Assumption | Why Unsupported | Evidence Needed to Cure | Challenge Viability | Element Affected | Defense Strategy |
|---|------------|----------------|------------------------|--------------------|-----------------|-----------------| 
| 1 | [Assumption] | [Explanation] | [What would cure] | HIGH/MED/LOW | [Element ref] | [Brief strategy note] |

---

## STEP 6 — MODULE E: Gap Analysis Matrix

Synthesize the outputs of Modules A through D into a single summary matrix showing, for each element of each charged offense, the complete logical path from evidence to proof.

### E.1 — Element Gap Matrix

| Element | State's Evidence (Direct/Circumstantial) | Inference(s) Required | Inference Strength | Assumption(s) Required | Assumption Challenge Viability | Overall Vulnerability | Defense Opportunity |
|---------|----------------------------------------|----------------------|-------------------|----------------------|-------------------------------|---------------------|-------------------|
| [Element 1] | [Evidence with Bate stamps] | [Inference #s from Module C] | STRONG/MOD/WEAK | [Assumption #s from Module D] | HIGH/MED/LOW | [Rating] | [Brief opportunity note] |

### E.2 — Overall Vulnerability Rating

For each element, assign an overall vulnerability rating based on the combined strength of the evidentiary chain:

| Rating | Criteria |
|--------|----------|
| **FORTIFIED** | Direct evidence supports the element; no inference or assumption required. Defense should not attack this element head-on. |
| **SOLID** | Circumstantial evidence with STRONG inferences; no unsupported assumptions. Difficult to challenge but not impossible. |
| **EXPOSED** | Evidence requires MODERATE inferences or contains one or more unsupported assumptions with LOW challenge viability. Viable defense target. |
| **VULNERABLE** | Evidence requires WEAK inferences, stacked inference chains, or unsupported assumptions with MEDIUM or HIGH challenge viability. Priority defense target. |
| **CRITICAL GAP** | No evidence, or evidence likely excludable, or assumption with HIGH challenge viability on an essential element. The State may not survive a motion for judgment of acquittal (La. C.Cr.P. Art. 778 / 821) on this element. |

### E.3 — Prosecution Theory Strength Summary

Provide a 2-3 paragraph narrative summary of the prosecution's overall theory strength, organized by:
- Where the theory is strongest (FORTIFIED / SOLID elements)
- Where the theory is weakest (VULNERABLE / CRITICAL GAP elements)
- The single most significant weakness the defense should exploit

---

## STEP 7 — MODULE F: Alternative Inference Table

For each prosecution inference identified in Module C, propose the strongest defense counter-inference that can be drawn from the same underlying facts. This module feeds directly into `dw-criminal-defense` Report 4 (Competing Theories) and provides the raw material for defense narrative construction.

### F.1 — Counter-Inference Development

For each prosecution inference:

1. **Restate the prosecution inference** (from Module C)
2. **Identify the underlying fact(s)** (same facts the prosecution relies on)
3. **Propose the defense counter-inference** — the strongest alternative reading of the same facts that is consistent with innocence, lesser culpability, or an affirmative defense
4. **Assess counter-inference strength** — using the same STRONG / MODERATE / WEAK scale
5. **Identify supporting evidence** — any additional facts from the discovery that bolster the defense reading over the prosecution reading

### F.2 — Alternative Inference Table

| Prosecution Inference | Underlying Facts | Defense Counter-Inference | Counter Strength | Supporting Evidence | Feeds Report 4 Theme |
|----------------------|-----------------|--------------------------|-----------------|--------------------|--------------------|
| [State's reading] | Fact #[N], #[N] | [Defense reading] | STRONG/MOD/WEAK | [Additional evidence] | [Theme tag] |

### F.3 — Defense Narrative Seeds

Based on the counter-inferences with the strongest support, identify 2-3 candidate defense narrative threads. For each:
- State the narrative thread in one sentence
- List the counter-inferences that support it (by number)
- Identify remaining gaps the defense would need to fill (investigation, expert, testimony)
- Assess compatibility with other defense theories being considered

**Do not advocate for a particular defense theory.** Present the alternatives neutrally with their respective strengths and weaknesses. The attorney selects the theory; this skill provides the analytical foundation.

---

## STEP 8 — Output Format

### Primary Deliverable: Report 2a — Theory Deconstruction (.docx)

**Filename:** `Report 2a - Theory Deconstruction - {{DEFENDANT_LAST}} - {{YYYY-MM-DD}}.docx`

**Location:** `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`

**Contents:**

1. **Header** — work-product marking per `dw-shared-protocols/references/attorney-work-product-marking.md`. Defendant name, docket number, parish/court, date, attorney.
2. **Executive Summary** — 1-2 paragraphs summarizing the prosecution theory, its strongest and weakest points, and the number of verified facts, inferences, and assumptions identified.
3. **Section 1: Element Mapping** (Module A) — charge-by-charge element grid with evidentiary sufficiency classifications.
4. **Section 2: Fact Inventory** (Module B) — complete table of extracted facts with verification status and source citations.
5. **Section 3: Inference Analysis** (Module C) — complete table of prosecution inferences with strength assessments and alternative inferences.
6. **Section 4: Assumption Audit** (Module D) — complete table of unsupported assumptions with challenge viability and cure requirements.
7. **Section 5: Gap Analysis Matrix** (Module E) — element-by-element synthesis with vulnerability ratings and defense opportunities.
8. **Section 6: Alternative Inference Table** (Module F) — counter-inferences and defense narrative seeds.
9. **Section 7: Prosecution Theory Strength Summary** — narrative assessment of overall theory strength.
10. **Section 8: Recommended Next Steps** — prioritized list of defense actions informed by the deconstruction:
    - Elements to target at trial
    - Investigation needs (to convert assumptions to contradicted facts)
    - Discovery demands (to force the State to fill gaps or reveal weaknesses)
    - Expert needs (to challenge inferences requiring scientific interpretation)
    - Motion opportunities (suppression, judgment of acquittal, directed verdict)
11. **Source Citation Appendix** — every factual claim mapped to its discovery citation.

### Case Brain Update

After producing Report 2a, update `dw-case-brain` with:
- Theory deconstruction completion status
- Number of VULNERABLE and CRITICAL GAP elements identified
- Key assumptions flagged for defense exploitation
- Pointer to the Report 2a file path

---

## Cross-Skill Integration

### This skill READS FROM:

| Skill | What It Provides |
|-------|-----------------|
| `dw-criminal-defense` Phase 2 Step 2 | Report 2 — Prosecution's Case Summary (hard prerequisite) |
| `dw-criminal-defense` Phase 1 Step 4 | Case Tables.xlsx — Evidence Table |
| `dw-case-brain` | Structured case context, charge information, Case Brain variables |
| Charge-type specialists (`dw-violent-crime-specialist`, `dw-drug-offense-specialist`, etc.) | Element grids and defense theory maps |
| `dw-criminal-defense` Phase 2 Step 2 | Report 3 — Immediate Red Flags (suppression candidates affecting element mapping) |

### This skill FEEDS:

| Skill | What It Receives |
|-------|-----------------|
| `dw-criminal-defense` Report 4 | Alternative Inference Table (Module F) provides raw material for Competing Theories / Core Defense Narrative construction |
| `dw-adversarial-stress-test` | Gap Analysis Matrix (Module E) identifies the weakest points for stress-testing; Assumption Audit (Module D) provides the specific assumptions to attack |
| `dw-theory-to-workplan` | Full deconstruction output informs workplan prioritization — VULNERABLE and CRITICAL GAP elements drive investigation and motion priorities |

### Workflow Position:

```
Report 2 (Prosecution's Case Summary)
    │
    ▼
Report 2a (Theory Deconstruction) ◄── YOU ARE HERE
    │
    ├──► Report 4 (Competing Theories / Core Defense Narrative)
    ├──► dw-adversarial-stress-test
    └──► dw-theory-to-workplan
```

---

## Guardrails

1. **Source Citation Mandate.** Every fact in the Fact Inventory (Module B) must cite its source document with Bate stamp or timestamp. Every inference (Module C) must trace to underlying facts. Every assumption (Module D) must explain why evidentiary support is absent. Unsourced claims are marked `[UNSOURCED — VERIFY]` and never appear in a final deliverable.

2. **Verification Protocol required.** Every extracted fact must carry a verification status: `[VERIFIED]`, `[MULTI-SOURCE VERIFIED]`, `[UNVERIFIED]`, `[CONTRADICTED]`, or `[CONTESTED]`. Do not classify a fact as verified without confirming the source document supports it.

3. **No fabricated citations.** Every Louisiana statute, code article, and case citation must be verifiable. If a citation cannot be verified, mark it `[VERIFY CITATION]`. Anchor authorities listed in CLAUDE.md may be cited without a flag.

4. **Do not argue for a particular defense theory.** Module F presents alternative inferences and defense narrative seeds neutrally. The attorney selects the theory. This skill provides the analytical foundation — it does not advocate. Present all viable alternatives with their respective strengths and weaknesses.

5. **Cowork drafts; attorney approves.** Every output is a draft for attorney review. The attorney verifies facts, confirms the fact/inference/assumption classifications, and makes all strategic decisions about which weaknesses to exploit. This skill never represents its work product as final or filed.

6. **Report 2 is a hard prerequisite.** Do not attempt theory deconstruction without a completed Report 2. If Report 2 does not exist, direct the attorney to generate it first via `dw-criminal-defense` Phase 2 Step 2. Deconstructing a theory that has not been articulated produces unreliable analysis.

7. **Do not speculate beyond the discovery.** The Assumption Audit (Module D) identifies what the State is assuming — it does not speculate about what undisclosed evidence the State might have. If additional discovery is anticipated, note it in the Recommended Next Steps but do not incorporate speculative evidence into the element mapping.

8. **Suppression candidates affect element mapping.** When Report 3 or `dw-suppression-motion` has identified evidence that may be excludable, note this in the Element Mapping (Module A) with the `SUPPRESSION CANDIDATE` classification. The Gap Analysis Matrix (Module E) should reflect the element's vulnerability both with and without the challenged evidence.

---

## Quick References

This skill does not currently maintain its own `references/` subdirectory. It relies on:

- **Report 2 output** — the prosecution's case summary generated by `dw-criminal-defense` Phase 2 Step 2
- **Case Tables.xlsx** — the evidence index and witness tables from Phase 1 Step 4
- **Charge-type specialist element grids** — from `dw-violent-crime-specialist`, `dw-drug-offense-specialist`, `dw-dwi-specialist`, `dw-sex-offense-specialist`, or `dw-firearms-specialist` as applicable
- **dw-shared-protocols/references/attorney-work-product-marking.md** — work product marking standard
- **dw-shared-protocols/references/output-path-formula.md** — output path convention

---

*This skill is part of the Daniels & Washington criminal defense toolkit. It is Report 2a in the Barone Discovery Workflow. Pair with dw-criminal-defense for the full case analysis pipeline, dw-adversarial-stress-test for stress-testing the weaknesses identified here, and dw-theory-to-workplan for converting the deconstruction into an actionable defense workplan.*
