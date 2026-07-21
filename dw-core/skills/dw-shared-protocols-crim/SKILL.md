---
name: dw-shared-protocols-crim
category: core
description: Shared boilerplate protocol library for all Daniels & Washington file-writing skills. This skill is NOT triggered directly by user prompts — it is read as a reference protocol by other D&W skills before they generate any document deliverable. Provides standardized captions (14th JDC Calcasieu, 12th JDC Avoyelles, Orleans CDC, 19th JDC EBR, Federal WDLA, plus fill-in for other courts), attorney work product marking, signature block, certificate of service, notice of hearing, proposed order, Louisiana citation style, 14th JDC filing conventions, and the CASE_ROOT-anchored output path formula. If you are a file-writing skill and your SKILL.md says to read this protocol, read it now and follow it before producing output.
version: 1.0.0
---

# dw-shared-protocols-crim

Centralized boilerplate so every D&W file-writing skill produces consistent captions, headers, signatures, certificates, and output paths. When the firm convention changes, this skill changes — and every consuming skill picks it up automatically.

## How to consume this skill

If you are a D&W file-writing skill, your SKILL.md should include a step near the top that reads:

> Before drafting, read `dw-shared-protocols-crim/SKILL.md` and load the references listed for your document type below. Then continue with the substance of your skill.

Template selection: the DEVONthink Template-First search protocol now lives in this skill's `references/template-selection-protocol.md`. Read it before drafting any pleading.

## Reference manifest by document type

> **Filed pleading orchestration:** for any filed pleading (motion, opposition, memo, sentencing memo, proposed order), read `filed-pleading-boilerplate.md` first — it walks through every component reference in the correct order. The table below remains the authoritative source for which component references each document type requires.

| Document type | Required references |
|---|---|
| State criminal motion (14th JDC Calcasieu) | `filed-pleading-boilerplate.md`, `caption-criminal-14thJDC.md`, `signature-block.md`, `certificate-of-service.md`, `notice-of-hearing.md`, `proposed-order.md`, `louisiana-citation-style.md`, `filing-conventions-14thJDC.md`, `output-path-formula.md` |
| State criminal motion (12th JDC Avoyelles) | `caption-criminal-12thJDC-avoyelles.md` + (work-product, signature, COS, notice, order, citation, output-path) |
| State criminal motion (Orleans CDC) | `caption-criminal-orleans-CDC.md` + (work-product, signature, COS, notice, order, citation, output-path) |
| State criminal motion (19th JDC EBR) | `caption-criminal-19thJDC-EBR.md` + (work-product, signature, COS, notice, order, citation, output-path) |
| Federal motion (WDLA) | `caption-criminal-federal-WDLA.md` + (work-product, signature, COS-federal version inside `certificate-of-service.md`, order, citation, output-path) |
| Other Louisiana parish (any court not listed above) | `caption-criminal-fill-in.md` + (work-product, signature, COS, notice, order, citation, output-path) — agent prompts attorney for parish/court-specific values |
| Sentencing memorandum | Caption per parish + `attorney-work-product-marking.md` + `signature-block.md` + `certificate-of-service.md` + `louisiana-citation-style.md` + `output-path-formula.md` |
| Internal work product (Case Brain, threat matrix, cross outline, audit reports) | `attorney-work-product-marking.md` + `output-path-formula.md` ONLY |
| Discovery ledger / triage report | `attorney-work-product-marking.md` + `output-path-formula.md` ONLY |
| Client deliverable (LWOP review sheet, plea analysis) | `attorney-work-product-marking.md` + `signature-block.md` + `output-path-formula.md` |

## Variables expected from Case Brain

When a consuming skill reads this protocol, it should already have these variables resolved from `dw-case-brain-crim` (v3.3+) before applying any caption or signature template:

- `{{CASE_ROOT}}` — absolute path to the case folder
- `{{DEFENDANT_NAME}}` — last, first, middle as filed
- `{{DOCKET}}` or `{{CASE_NUMBER}}` — docket/case number
- `{{PARISH}}` — parish name
- `{{COURT}}` — judicial district or court name
- `{{DIVISION}}` or `{{SECTION}}` — division letter (state) / section letter (Orleans)
- `{{JUDGE_NAME}}` — assigned judge
- `{{ADA_NAME}}` — assigned ADA / AUSA
- `{{ADA_EMAIL}}` — service email
- `{{HEARING_DATE}}`, `{{HEARING_TIME}}` — if applicable
- `{{CLIENT_NICKNAME}}` — short folder name for path formula

If any required variable is missing, the consuming skill must prompt the attorney before drafting — never insert placeholders into a final deliverable.

## Filed vs. internal — the work product marking rule

- **Filed pleadings** (motions, oppositions, memos in support, sentencing memoranda, proposed orders, notices of hearing): NO work product marking.
- **Internal deliverables** (Case Brain, threat matrices, cross outlines, audit reports, discovery ledgers, investigation plans, plea analyses, voir dire dashboards): Work product marking REQUIRED per `attorney-work-product-marking.md`.
- Ambiguous case (e.g., proposed jury instructions): treat as filed — no marking — unless skill explicitly produces an internal draft for attorney review only.

## Migration notes

- v1.0.0 — initial build. Template selection protocol now lives in this skill's `references/template-selection-protocol.md`. Captions: 14th JDC, 12th JDC Avoyelles, Orleans CDC, 19th JDC EBR, Federal WDLA, fill-in template.
- Future: add 15th JDC, 16th JDC, 9th JDC, civil captions, post-conviction captions as needed.
