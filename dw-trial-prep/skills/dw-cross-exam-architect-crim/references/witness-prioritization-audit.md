# Witness Prioritization & Impeachment Audit

**Before any outline drafting begins, conduct a systematic audit of all prosecution witnesses.**

## Scope & Objective

**Pre-check — run upstream intake first.** Before ranking anything, pull the analyzed inputs listed in `upstream-intake.md`: the **DMAR** (§4 Inconsistency Matrix, §9 Cross-Examination Seeds, §10 Report-vs-Recording Matrix with its CRITICAL/SIGNIFICANT/MINOR severities), **auditor reports** (§6 Key Findings for Cross-Examination), and the **Brady/Giglio audit**. Ranking impeachment strength without them means ranking blind to the richest evidence in the file — the DMAR severity ratings in particular map almost directly onto this audit's strength assessment. If dw-witness-statement-analyzer-crim has already produced Witness Analysis Cards and a Conflict Matrix for this case, import those findings directly. The Analysis Cards contain pre-identified inconsistencies, credibility indicators, and defense utility assessments that map directly to the impeachment categories below. This can significantly accelerate the Witness Prioritization audit.

For the top 10 prosecution witnesses identified in discovery, systematically identify and rank impeachment vulnerabilities. This audit produces the witness triage necessary to sequence cross-examination strategy and identify which witnesses present the highest-value targets for impeachment before STEP 1 outline building begins.

## Impeachment Analysis Framework

For each prosecution witness, identify and document:

**1. Internal Contradictions** — Witness contradicts themselves
- Within the same statement: e.g., "The door was locked" vs. "I entered without forced entry"
- Across different statements: e.g., Report A says "Suspect fled" but Preliminary Hearing testimony says "Suspect complied"
- Within testimony: prior statement vs. trial testimony inconsistency

**2. External Contradictions** — Witness A contradicts Witness B
- Competing witness accounts of the same event
- Officer A's report vs. Officer B's report (cross-agency discrepancy)
- Witness statement vs. physical evidence location/timing conflict

**3. Omissions** — What standard procedure requires but is absent from reports
- Missing BWC footage for incident type
- Missing supplemental reports after initial incident report
- Missing chain of custody documentation
- Missing lab reports, evidence photographs, or investigative follow-up
- Absence of standard investigative steps (interviews, measurements, photos, drawings)

**4. Credibility Issues** — Bias, motive to fabricate, or prior dishonesty

> **⚠ ADMISSIBILITY GATE — La. C.E. art. 608(B).** Before ranking any credibility item, classify it. In Louisiana state court, "particular acts, vices, or courses of conduct" may **not** be inquired into to attack character for truthfulness — art. 608(B) bars it, unlike FRE 608(b). An item is usable only if it is:
> 1. A **conviction** under art. 609.1,
> 2. A **bias, interest, corruption, or defect of capacity** fact under art. 607(D)(1) — deals, grudges, own exposure, financial stake (extrinsic proof permitted),
> 3. An attack on the **truthfulness or accuracy of this testimony** under art. 607(C) — perception, memory, intoxication, distraction, internal implausibility, or
> 4. A **prior inconsistent statement** under art. 613.
>
> If it is none of the four, do not rank it as a live impeachment point. Record it as `[608(B) REVIEW REQUIRED — not usable as character evidence; attorney to assess constitutional exception]`. A disciplinary file full of unrelated misconduct is not cross material in Louisiana just because it was produced. See §3.5 of `jurisdiction-and-court-map.md`.
- Financial interest in outcome (expert paid by one party, officer facing discipline if credibility damaged)
- Relationship bias (family, romantic, professional loyalty affecting objectivity)
- Prior dishonesty, impeachment convictions, or pattern of credibility issues — **run the art. 608(B) gate above before ranking**; convictions qualify under art. 609.1, uncharged conduct generally does not
- Motive to fabricate (covering up own error, protecting superior, securing case closure)

## Citation Mandate

**Every impeachment point must cite source documents with page/paragraph/timestamp.** If you cannot point to a specific document, it cannot be included in the audit output.

**On `(N)` numbering at this stage:** the formal Source Register is built at Step 4, after this audit. Use `(N)` register numbers here only if a register already exists for this case; otherwise cite by full document title and page/Bates/timestamp, and the numbers will be assigned when the register is built. Do not invent numbers now — a number assigned here and changed later breaks the "source numbering is sacred" rule.

**Format for each impeachment finding:**
> **[Witness Name]** — [Impeachment Category]
> - Contradiction: [Quote from Source A] vs. [Quote from Source B]
> - Source A: [(1) Document Title, p. ___, para. ___ / timestamp ___]
> - Source B: [(2) Document Title, p. ___, para. ___ / timestamp ___]
> - Strength Assessment: [High / Medium / Low] — [1-2 sentence explanation]

## Deliverable: Ranked Witness Impeachment Report

Output a table ranked by impeachment strength (highest risk to prosecution first):

| Rank | Witness Name | Type | Primary Impeachment | Source(s) | Strength | Preliminary Cross Strategy |
|------|--------------|------|-------------------|-----------|----------|---------------------------|
| 1 | [Name] | [LE/Expert/Civilian] | [Internal/External/Omission/Credibility] | [(N) Docs cited] | High/Med/Low | [One-sentence strategy] |
| 2 | ... | ... | ... | ... | ... | ... |

**Preliminary Cross Strategy** for each witness must:
- Identify the single most damaging impeachment point
- Describe how to sequence the cross to establish foundation before revealing contradiction
- Flag any evidentiary or procedural concerns (La. C.E. art. 613 foundation before **extrinsic** proof of a prior statement — not before asking about it; witness availability; art. 608(B) admissibility per the gate above)

## When to Begin STEP 1

Proceed to STEP 1 (Information Gathering) **only after** this Witness Prioritization audit is complete and shared with the attorney. The audit informs which specific witnesses to focus on and determines the cross-examination priority sequence.
