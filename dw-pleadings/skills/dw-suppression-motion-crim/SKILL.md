---
name: dw-suppression-motion-crim
category: pleadings
description: >
  Draft suppression motions AND audit search warrants. ALWAYS invoke for "suppress," "motion
  to suppress," "illegal search," "bad warrant," "audit the warrant," "probable cause,"
  "Franks," or "fruit of the poisonous tree." Covers 4th and 5th Amendment issues. Read
  dw-shared-protocols-crim/references/template-selection-protocol.md before drafting.
---

# Daniels & Washington — Suppression Motion & Warrant Auditor
**Version 2.0 | Internal Use Only**

This skill has two modes:

1. **Audit Mode** — Produces a comprehensive Search Warrant Constitutional Audit Report (.docx) analyzing probable cause, particularity, Franks viability, execution compliance, and Leon preemption. Use when the attorney wants to evaluate a warrant before deciding whether to file a motion.

2. **Motion Mode** — Generates complete, ready-to-edit suppression motions as two separate Word documents: a short-form **Motion to Suppress** and a detailed **Memorandum in Support**. For Search & Seizure (warrant-based) suppression, the warrant audit runs first and feeds directly into the motion.

Both modes read discovery files to extract facts, search firm databases for templates and prior authority, and apply Louisiana law throughout.

**Mode Selection:** If the attorney says "audit the warrant," "review the affidavit," "look at this warrant," or "anything wrong with this search" → start in **Audit Mode**. If the attorney says "suppress," "motion to suppress," "file a motion" → start in **Motion Mode**. After an audit, always offer: *"Want me to draft the suppression motion based on these findings?"*

**Cowork drafts; attorney approves.** Every output is a draft for attorney review. The attorney verifies facts, confirms legal arguments, signs, and files.

---

## STEP 0 -- FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any search warrants, affidavits, arrest reports, body-worn camera footage, interrogation recordings, statements, or other discovery, do not analyze anything yet.**

Your only response must be:
> *"Before I begin -- are you uploading any additional search warrants, affidavits, returns on warrants, arrest reports, BWC footage, interrogation recordings, Miranda waiver forms, witness statements, or other case documents? I'll start the audit/motion only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** Mid-analysis discovery of an additional warrant, a body camera recording of the search execution, or an interrogation recording would require complete re-evaluation of probable cause, particularity, execution compliance, Franks viability, and any companion 5th/6th Amendment suppression theory.

---

### Source Citation Mandate

Every factual assertion in the Warrant Audit Report, Motion to Suppress, and Memorandum in Support must trace back to a specific source document. Suppression hearings are fact-intensive — the court evaluates probable cause, warrant particularity, and execution compliance based on the documented record. Unsourced claims about what officers did or didn't do carry no weight.

**Citation format:** Cite the document title, page number, and paragraph or timestamp. Examples:
- `(Search Warrant Affidavit, p. 2, para. 4)`
- `(Search Warrant — 14th JDC, signed 03/15/2026, Scope paragraph)`
- `(Return on Search Warrant, p. 1, Items Seized)`
- `(Officer Smith BWC — Warrant Execution, Timestamp 00:05:32)`
- `(Arrest Report — LCPD Case #2026-00456, p. 3, para. 2)`
- `(Inventory Receipt, Items #1-14)`
- `(Discovery Production, Bates #00145-00148)`

**Multiple-source rule:** When more than one document confirms a fact about the search, cite all of them — e.g., `(Warrant Affidavit, p. 2, para. 4; Officer Smith BWC, Timestamp 00:05:32)`.

**Unsourced assertions:** If a factual claim cannot be tied to a specific document, mark it `[UNSOURCED — VERIFY WITH CLIENT/DISCOVERY]` so the attorney knows to confirm or remove it before filing.

**Where sourcing applies:** All factual content — probable cause analysis, warrant scope review, execution compliance, Franks material, and fruit of the poisonous tree analysis. Legal standards and case law follow normal legal citation format.

---

## Suppression Categories

This skill handles four categories of suppression, each with distinct constitutional foundations and analytical frameworks. Many cases involve overlapping categories (e.g., an illegal traffic stop that leads to both a warrantless search and a custodial statement). When multiple categories apply, generate a single combined motion covering all grounds — the court prefers consolidated filings over piecemeal motions.

| Category | Constitutional Basis | What Gets Suppressed |
|----------|---------------------|---------------------|
| **Search & Seizure** | 4th Amendment; La. Const. Art. I, § 5 | Physical evidence, contraband, weapons, digital data |
| **Statements** | 5th Amendment; La. Const. Art. I, § 13 | Confessions, admissions, custodial statements |
| **Identification** | 14th Amendment Due Process; La. Const. Art. I, § 2 | Lineup IDs, showup IDs, photo array IDs, in-court IDs |
| **Fruit of the Poisonous Tree** | *Wong Sun v. United States* | All evidence derived from the initial constitutional violation |

---

## Workflow

### STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any pleading, read `dw-shared-protocols-crim/SKILL.md` and load:

1. `dw-shared-protocols-crim/references/filed-pleading-boilerplate.md` — orchestrator for caption, signature, COS, notice, proposed order, citation style, and filing conventions
2. `dw-shared-protocols-crim/references/output-path-formula.md` — output path anchored on `CASE_ROOT`
3. `dw-shared-protocols-crim/references/letterhead.md` — firm letterhead; on a filed pleading it sits above the caption per firm preference (the court caption stays the controlling header — letterhead never replaces caption, signature block, or certificate of service)

Filed pleadings receive NO work product marking. Follow the boilerplate component sequence in order. Output to the appropriate `01 - Trial Notebook/` motion subfolder per the formula. The Warrant Audit Report (Audit Mode only) is internal work product — mark it per `attorney-work-product-marking.md` as noted in the Warrant Deep-Dive section.

### STEP 0.6 — Constitutional Red Flag Scan

Before proceeding to template selection and motion drafting, conduct a rapid constitutional triage of the case file. This scan identifies whether suppression motions are warranted and which grounds to prioritize.

Scan discovery for 4th Amendment (searches, warrants, consent, stops, phones), 5th Amendment (Miranda, invocation, Art. 230.1 delay, coercion, silence), and 6th Amendment (post-charge interrogation, counsel access, jailhouse informants) red flags. For each: cite the source, classify urgency (IMMEDIATE / STRATEGIC / MONITORING), note ground and authority. Output a ranked Red Flag Scan Summary; document a clean scan if none.

Read `references/red-flag-scan.md` now for the full red-flag category lists, per-flag documentation rules, and the Scan Summary output spec.

### Step 1: Template-First Search

Before drafting anything, search DEVONthink for firm templates and prior suppression filings. This is not optional — it's the firm's Template-First Drafting Rule.

**DEVONthink searches to run:**
```
"motion suppress" OR "suppression motion"
"memorandum support suppress"
"suppress statement" OR "suppress identification" OR "suppress search"
```

Also search with tags: `template`, `suppression`, `motion`

**After searches complete**, read and follow the Template Selection Protocol at `dw-shared-protocols-crim/references/template-selection-protocol.md` (Steps A through D). Present the top 3 results, let the attorney select a template or paste a DEVONthink link, and load the selection before proceeding. Do not proceed to Step 2 until the attorney has selected a template or chosen to draft from scratch.

If a template is selected, preserve the firm's preferred formatting, language, and legal positions — then update with case-specific facts and authority. If drafting from scratch, use this skill's built-in structure and offer to save the final approved version as a new template.

**TextExpander snippets to apply:**
- `;miranda` — Miranda citation block (for statement suppression)
- `;draft` — Cowork draft disclaimer

### Step 2: Gather Case Context

Parse the attorney prompt (client, docket, factual scenario, evidence to suppress); mine discovery — police/incident reports, body cam and interview transcripts, warrants and affidavits, forensic extraction reports, identification procedure records — for suppression-relevant facts; and check prior case analysis (Constitutional Issues Scan, Forensic Audit, Report 3, Cowork Analysis).

Read `references/case-context-intake.md` now for the full intake checklist by source.

### Step 3: Classify the Suppression Type

Based on the facts gathered, identify which suppression categories apply. Think through each one:

Work through the question sets for **Search & Seizure** (warrant validity, or which exception the State must prove; La. Const. Art. I, § 5), **Statements** (custody, interrogation, Miranda, invocation, waiver, *Bruton*), **Identification** (suggestiveness, *Manson* factors, Art. 253), and **Fruit of the Poisonous Tree** (derivative evidence and its exceptions).

Read `references/classification-questions.md` now for the full "ask yourself" question sets for all four categories.


### WARRANT DEEP-DIVE (Search & Seizure — Audit Mode or Motion Mode)

When a search warrant is uploaded or referenced, automatically run this comprehensive warrant audit. In Audit Mode, produce the Warrant Audit Report. In Motion Mode, use the findings to build the Search & Seizure section of the suppression motion.

Five analyses in order: **Four Corners Probable Cause** (conclusory-language scan, nexus, informant reliability, staleness), **Particularity & Scope**, **Franks v. Delaware** (flag `[FRANKS CANDIDATE]`), **Execution** (knock-and-announce, Art. 163 timing, force, return), and **Leon Good-Faith Preemption**. In Audit Mode, produce the nine-section Warrant Audit Report (.docx, work-product marked) and then offer to draft the motion.

Read `references/warrant-deep-dive.md` now for the complete audit protocol, the Warrant Audit Report section list with ratings, file naming, and the Search Warrant Legal Standards Quick Reference table.

### Step 4: Draft the Motion to Suppress (.docx #1)

The Motion to Suppress is a short, formal filing — typically 2-3 pages. It tells the court what the defense is asking for and why, without the full legal argument (that goes in the Memorandum).

**Structure:** Caption → MOTION TO SUPPRESS [EVIDENCE / STATEMENT / IDENTIFICATION] → NOW INTO COURT paragraph → I. Introduction → II. Statement of Facts → III. Legal Basis (Art. 703) → IV. Prayer for Relief (Art. 703(D) hearing; suppress evidence and fruits; bar reference at trial; other relief) → COS → Signature Block.

Read `references/motion-template.md` now for the full verbatim motion structure and the key rules (always request a hearing, name the specific items, keep facts tight, pin the Miranda timeline).

### Step 5: Draft the Memorandum in Support (.docx #2)

The Memorandum is the substantive legal brief — typically 8-20 pages depending on complexity. This is where the legal research, case law application, and detailed argument live.

**Structure:** Caption → MEMORANDUM IN SUPPORT OF MOTION TO SUPPRESS → I. Introduction → II. Statement of Facts (sourced) → III. Legal Standard → IV. Argument (per ground: legal rule, application, State cannot meet its burden; then C. Fruit of the Poisonous Tree) → V. Conclusion → COS → Signature Block.

Read `references/memorandum-template.md` now for the full memorandum structure and the key rules (lead with the strongest ground, anticipate the State's exceptions, quote the record, argue both Louisiana and federal grounds, make burden allocation explicit for searches, statements, and identifications).

### Step 6: Citation Research

For citations, use a layered approach:

**Layer 1 — Training knowledge:** Start with well-established suppression precedent. Read `references/suppression-citations.md` for the organized citation library covering all four suppression categories with Louisiana and federal authority.

**Layer 2 — DEVONthink:** Search for citations used in prior firm filings:
```
Search: "[constitutional issue]" in group "06 - Law & Research" OR tags contain "suppression"
```

After assembling citations, flag any that may need currency verification:
`[RESEARCH — confirm this case has not been overruled or modified]`

### Step 7: Generate the .docx Files

Court-filing format (US Letter, Times New Roman 12/14, double-spaced, left-aligned, footer page numbers, caption on page 1). Read `references/output-and-review.md` (Step 7) now for the formatting requirements and file-naming conventions.

### Step 8: Attorney Review Flags

Mark every item needing attorney attention with `[VERIFY]`, `[RESEARCH]`, `[ATTORNEY TO COMPLETE]`, or `[STRATEGIC DECISION]`. Read `references/output-and-review.md` (Step 8) now for the full flag definitions.

### Step 9: Save and Integrate

Save both documents to the case folder (or outputs directory if standalone), update the LWOP Worksheet, create the Clio review-and-file task, cross-reference the Constitutional Issues Scan, and present the attorney summary. Read `references/output-and-review.md` (Step 9) now for save locations, Clio task language, and the summary checklist.

---

## Multi-Category Motions

When multiple suppression grounds apply, consolidate into one motion and memorandum, organized chronologically from the earliest violation forward and ending with fruit of the poisonous tree. Read `references/memorandum-template.md` (final section) now for the recommended multi-category argument organization.

---

## Integration with Other Skills

| Skill | How It Integrates |
|-------|------------------|
| `dw-shared-protocols-crim` | Caption, signature, COS, notice of hearing, proposed order, citation style, filing conventions, output path |
| `dw-criminal-defense-crim` | Phase 2 Constitutional Issues Scan feeds suppression grounds |
| `dw-mobile-forensic-auditor-crim` | Forensic Audit report provides digital evidence suppression facts |
| `dw-cross-exam-architect-crim` | Warrant audit generates cross-exam seeds for affiant/executing officers |
| `docx` | Document generation — read for .docx creation instructions |
| TextExpander snippets | `;miranda`, `;draft` (skill-specific; caption/sig/cos now via shared protocols) |

### Search Warrant Legal Standards Quick Reference

The issue-by-authority table (probable cause, particularity, Franks, Leon, bare-bones, knock-and-announce, staleness, informants, *Riley*, digital particularity, La. C.Cr.P. Art. 163/167, anticipatory warrants) now lives with the audit protocol. Read `references/warrant-deep-dive.md` (final section) for the table.

---

## Output Location

Use the output path formula from `dw-shared-protocols-crim/references/output-path-formula.md`. Filed motions go to `{{CASE_ROOT}}/02 - Pretrial Notebook/01 - Pleadings/`; warrant audit reports go to `{{CASE_ROOT}}/02 - Pretrial Notebook/03 - Case Analysis & Notes/`. See shared protocols for CASE_ROOT resolution, filename conventions, and post-write reporting format.

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **suppression-citations.md** — Layer-1 citation library for suppression motions: federal and Louisiana authority organized by suppression category (4th Amendment search & seizure, 5th Amendment statements, 14th Amendment identification, *Wong Sun* fruit of the poisonous tree), keyed to firm DEVONthink template groups
- **red-flag-scan.md** — Step 0.6: 4th/5th/6th Amendment red-flag categories, per-flag documentation and urgency rules, Red Flag Scan Summary output spec
- **classification-questions.md** — Step 3: "ask yourself" question sets for Search & Seizure, Statements, Identification, and Fruit of the Poisonous Tree
- **warrant-deep-dive.md** — Warrant Deep-Dive step: four-corners probable cause, particularity & scope, Franks, execution, Leon preemption, Warrant Audit Report spec, and the Search Warrant Legal Standards Quick Reference table
- **motion-template.md** — Step 4: full Motion to Suppress structure and key drafting rules
- **memorandum-template.md** — Step 5: full Memorandum in Support structure, key drafting rules (burden allocation), and multi-category argument organization
- **case-context-intake.md** — Step 2: intake checklist by source (attorney prompt, discovery file types, prior case analysis)
- **output-and-review.md** — Steps 7–9: .docx formatting and file naming, attorney review flags, save locations, Clio task, presentation summary

---

*This skill reflects Daniels & Washington Suppression Motion & Warrant Auditor Version 2.0 (March 2026). It incorporates the former dw-search-warrant-auditor skill — all warrant auditing is now integrated here. Update whenever suppression case law or firm procedures change.*
