---
name: dw-404b-opposition-crim
category: pleadings
description: >
  Oppose other crimes evidence under 404(b). ALWAYS invoke for "404(b)," "Prieur notice,"
  "prior bad acts," "other crimes evidence," "oppose 404(b)," or "kitchen sink notice."
  Produces Opposition + Memorandum in Support. Read
  dw-shared-protocols-crim/references/template-selection-protocol.md before drafting.
---

# Daniels & Washington — 404(B) Other Crimes Evidence Opposition Generator
**Version 1.0 | Internal Use Only**

This skill generates complete, ready-to-edit filings to oppose the State's introduction of other crimes evidence under La. C.E. Art. 404(B). It produces two separate Word documents: a short-form **Opposition to State's 404(B) Notice** (or **Motion in Limine to Exclude**) and a detailed **Memorandum in Support**. It reads the State's Prieur notice and discovery files to extract facts, searches firm databases for templates and prior authority, and applies Louisiana law throughout.

**Cowork drafts; attorney approves.** Every output is a draft for attorney review. The attorney verifies facts, confirms legal arguments, signs, and files.

---

## STEP 0 -- FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any 404(b) notices, Prieur notices, prior conviction records, prior bad acts evidence, witness statements, or case discovery, do not analyze anything yet.**

Your only response must be:
> *"Before I begin -- are you uploading any additional 404(b)/Prieur notices, prior conviction records, prior bad acts evidence, witness statements, police reports, or other case documents? I'll start analysis only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** Mid-analysis discovery of an additional prior bad act, a missing exhibit referenced in the State's notice, or a co-defendant's similar 404(b) ruling would require complete re-evaluation of the opposition's relevance, prejudice, and Prieur compliance arguments.

---

### Source Citation Mandate

Every factual assertion in the Opposition and Memorandum in Support must trace back to a specific source document. 404(b) litigation is fact-intensive — the court evaluates whether each prior act qualifies under an enumerated exception based on the documented record. Unsourced claims about what the defendant allegedly did, when, or in what context carry no weight at a Prieur hearing.

**Citation format:** Cite the document title, page number, and paragraph or timestamp. Examples:
- `(State's 404(B) Notice, p. 2, para. 3)`
- `(Prior Conviction Minute Entry — Docket #2018-CR-0456, p. 1)`
- `(Prior Police Report — LCPD Case #2018-00123, p. 4, para. 5)`
- `(Witness Statement — [Name], 03/15/2026, p. 2)`
- `(Discovery Production, Bates #00145-00148)`

**Multiple-source rule:** When more than one document confirms a fact about a prior act, cite all of them — e.g., `(Prior Police Report, p. 4, para. 5; Booking Record, p. 1)`.

**Unsourced assertions:** If a factual claim cannot be tied to a specific document, mark it `[UNSOURCED — VERIFY WITH CLIENT/DISCOVERY]` so the attorney knows to confirm or remove it before filing.

**Where sourcing applies:** All factual content about prior acts, the State's proffered exception, the defense theory, and prejudice analysis. Legal standards and case law follow normal legal citation format.

---

## Filing Types

This skill generates two types of filings depending on the posture:

| Filing Type | When to Use | Triggered By |
|-------------|-------------|--------------|
| **Opposition to State's 404(B) Notice** | The State has filed a Prieur notice seeking to introduce other crimes evidence | State's notice is uploaded or described |
| **Defense Motion in Limine** | The defense wants to preemptively exclude anticipated 404(b) evidence before the State files notice | Attorney identifies evidence the State is likely to use |

When the State has filed a notice, generate an Opposition. When the defense is acting preemptively, generate a Motion in Limine. In both cases, the Memorandum in Support follows the same analytical framework.

---

## The 404(B) Analytical Framework

Louisiana's 404(B) exclusionary rule bars other-crimes evidence offered to prove conformity with character (*Prieur*). The State must satisfy ALL six requirements: (1) adequate written Prieur notice, (2) a pretrial hearing with item-by-item rulings, (3) a legitimate non-character purpose, (4) independent relevance to a material fact genuinely at issue, (5) proof the defendant committed the other acts, and (6) Art. 403 balancing. This framework drives every argument in the filing.

Read `references/404b-analytical-framework.md` now for the full six-requirement framework with controlling authority (*Prieur*, *Goffner I–III*, *Rose*, *Martin*, *Galliano*).

---

## Workflow

### STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any pleading, read `dw-shared-protocols-crim/SKILL.md` and load:

1. `dw-shared-protocols-crim/references/filed-pleading-boilerplate.md` — orchestrator for caption, signature, COS, notice, proposed order, citation style, and filing conventions
2. `dw-shared-protocols-crim/references/output-path-formula.md` — output path anchored on `CASE_ROOT`
3. `dw-shared-protocols-crim/references/letterhead.md` — firm letterhead; on a filed pleading it sits above the caption per firm preference (the court caption stays the controlling header — letterhead never replaces caption, signature block, or certificate of service)

Filed pleadings receive NO work product marking. Follow the boilerplate component sequence in order. Output to the appropriate `01 - Trial Notebook/` motion subfolder per the formula.

### Step 1: Template-First Search

Before drafting, search DEVONthink for firm templates and prior 404(b) filings. This is the firm's Template-First Drafting Rule.

Run the DEVONthink queries against the `404 B - Other Crimes` group (Law Library-Criminal) and the active case folder's `06 - Law & Research`, and check the catalog of known 404(B) documents (prior motion template, brief memo, Neveaux Goffner supplement, notice-requirement analysis, Notes of Decisions, *State v. Jones*).

Read `references/devonthink-search-protocol.md` now for the exact search strings and the known-document catalog.

**After searches complete**, read and follow the Template Selection Protocol at `dw-shared-protocols-crim/references/template-selection-protocol.md` (Steps A through D). Present the top 3 results, let the attorney select a template or paste a DEVONthink link, and load the selection before proceeding. Do not proceed to Step 2 until the attorney has selected a template or chosen to draft from scratch.

If a template is selected, preserve the firm's preferred formatting and legal positions — then update with case-specific facts and authority. If drafting from scratch, use this skill's built-in structure and offer to save the final approved version as a new template.

### Step 2: Gather Case Context

Parse the attorney prompt (client, docket, charged offense, the other-crimes evidence at issue, defense theory); catalog each act in the State's Prieur notice with its claimed exception, specificity, and timeliness; mine discovery (police reports, criminal history, witness statements, charged-offense details); and check prior case analysis (Report 3 Red Flags, Constitutional Issues Scan, Witness Cross-Reference).

Read `references/case-context-intake.md` now for the full intake checklist by source.

### Step 3: Analyze Each Item of Evidence

For every item of other crimes evidence the State seeks to introduce, work through the six-requirement framework above. This analysis drives the argument structure.

**For each item,** answer five questions: notice adequacy; whether the stated purpose is legitimate or pretextual (tested exception by exception — motive, opportunity, intent, preparation, plan/scheme/system, knowledge, identity, absence of mistake, res gestae); whether the claimed material fact is genuinely contested; the State's proof that the defendant committed the act; and Art. 403 probative-vs-prejudicial balance.

Read `references/item-analysis-checklist.md` now for the full per-item question set and the exception-by-exception pretext tests. Then read `references/attack-vectors.md` for the checklist of defense attack lines organized by the exception the State claims.

### Step 4: Draft the Opposition / Motion in Limine (.docx #1)

The Opposition (or Motion in Limine) is a short, formal filing — typically 3-5 pages. It frames the issue and requests relief.

**Structure:** Caption → title (Opposition or Motion in Limine) → NOW INTO COURT paragraph → I. Introduction → II. Background → III. Summary of Argument → IV. Prayer for Relief (deny, order adequate Prieur/Goffner notice, individualized Prieur hearing, exclude under 404(B)/403, other relief) → Certificate of Service → Signature Block.

Read `references/opposition-template.md` now for the full verbatim document structure and the Motion in Limine (preemptive) variant instructions.

### Step 5: Draft the Memorandum in Support (.docx #2)

The Memorandum is the substantive legal brief — typically 10-25 pages depending on the number of items challenged and complexity of the arguments.

**Structure:** Caption → title → I. Introduction → II. Statement of Facts (A. charged offense; B. other acts) → III. Legal Standard → IV. Argument (A. notice inadequate; B. no legitimate purpose, item by item; C. no independent relevance; D. State cannot prove the other acts; E. Art. 403) → V. Conclusion → COS → Signature.

Read `references/memorandum-template.md` now for the full memorandum structure and the key drafting rules (lead with the strongest argument, address each item individually, anticipate the State's "integral to the narrative" claim, use the State's own language, emphasize prejudice, cite both Supreme Court and Circuit authority).

### Step 6: Citation Research

Use a layered approach:

**Layer 1 — Training knowledge:** Start with well-established 404(B) precedent. Read `references/404b-citations.md` for the organized citation library.

**Layer 2 — DEVONthink:** Search for citations used in prior firm filings:
```
Search in "404 B - Other Crimes" group
Search: "404" OR "Prieur" OR "other crimes" in "06 - Law & Research"
```

**Layer 3 — Web search for recent authority:** Search for recent Louisiana 404(B) case law, particularly from the circuit covering the case. Focus on decisions from the past 2 years that may have refined the *Prieur* framework or modified the burden analysis.

After assembling citations, flag any that may need currency verification:
`[VERIFY CITATION — confirm this case has not been overruled or modified]`

### Step 7: Generate the .docx Files

Read the `docx` skill (SKILL.md) for document creation instructions.

**Formatting requirements:**
- US Letter (8.5" x 11"), 1-inch margins
- Font: Times New Roman, 12pt body text, 14pt headings
- Double-spaced body text (court filing)
- Left-aligned text (no full justification)
- Page numbers centered in footer
- Caption on first page of each document
- Each document starts on page 1

**File naming:**
- Opposition: `Opposition to 404(B) Notice - [Client Last Name] - [Date].docx`
- Motion in Limine: `Motion in Limine - 404(B) - [Client Last Name] - [Date].docx`
- Memorandum: `Memorandum in Support - 404(B) - [Client Last Name] - [Date].docx`

### Step 8: Attorney Review Flags

Before presenting the output, mark all items that need attorney attention:

- `[VERIFY — confirm this fact with client/discovery]` — factual assertions not directly sourced
- `[VERIFY CITATION — confirm current validity]` — case law that may have been modified
- `[ATTORNEY TO COMPLETE]` — signature block, specific dates, bar number
- `[STRATEGIC DECISION]` — whether to challenge notice adequacy vs. substance, whether to request a continuance for inadequate notice, which items to prioritize
- `[RESEARCH NEEDED]` — areas where additional legal research would strengthen the argument

### Step 9: Save and Integrate

**If part of an active case folder:**
- Save both documents to `02 - Pretrial Notebook/01 - Pleadings/`
- Update the LWOP Worksheet's Motions section if applicable
- Create a Clio task: *"Review and File 404(B) Opposition — [Client Name]"*
- Cross-reference with Report 3 (Immediate Red Flags) if one exists

**If standalone:**
- Save to the current working folder / outputs directory

**Present to the attorney with a summary:**
- Filing type (Opposition vs. Motion in Limine)
- Number of items of other crimes evidence challenged
- Key arguments and the legal basis for each
- Primary authorities cited
- Items flagged for attorney attention
- Prieur hearing date (if known)
- Whether a prior firm template was used as the base

---

## Common 404(B) Attack Vectors

These are the most effective lines of attack organized by the exception the State typically claims. Use these as a checklist when analyzing the State's notice.

Organized by claimed exception: "Motive," "Intent," "Plan / Scheme / System," "Knowledge," "Identity," "Absence of Mistake or Accident," and "Res Gestae / Integral Act."

Read `references/attack-vectors.md` now for the full attack-vector checklist under each exception.

---

## Integration with Other Skills

| Skill | How It Integrates |
|-------|------------------|
| `dw-criminal-defense-crim` | Phase 2 Report 3 (Red Flags) may identify 404(b) issues |
| `dw-suppression-motion-crim` | If 404(b) evidence was obtained through a constitutional violation, suppression is the primary remedy; 404(b) exclusion is an alternative |
| `dw-cross-exam-architect-crim` | If 404(b) evidence is admitted despite opposition, build cross-examination to minimize its impact |
| `dw-brady-giglio-auditor-crim` | Undisclosed favorable evidence may undermine the other acts the State seeks to introduce |
| `docx` | Document generation — read for .docx creation instructions |
| `dw-shared-protocols-crim` | Caption, signature, COS, notice of hearing, proposed order, citation style, filing conventions, output path |
| DEVONthink | Template-First search in `404 B - Other Crimes` folder |
| TextExpander | `;draft` (skill-specific; caption/sig/cos now via shared protocols) |

---

*This skill reflects Daniels & Washington 404(B) Opposition Generator Version 1.0 (March 2026). Update whenever 404(B) case law or firm procedures change.*


---

## Output Location

Use the output path formula from `dw-shared-protocols-crim/references/output-path-formula.md`. Filed motions go to `{{CASE_ROOT}}/02 - Pretrial Notebook/01 - Pleadings/`. See shared protocols for CASE_ROOT resolution, filename conventions, and post-write reporting format.

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **404b-citations.md** — 404(B) citation library: Louisiana opposition authority (Prieur framework foundational cases) with DEVONthink links to firm copies; cite-check before filing
- **404b-analytical-framework.md** — Analytical Framework section / Step 3: the six requirements the State must satisfy (notice, hearing, legitimate purpose, independent relevance, proof of the other acts, Art. 403) with controlling authority
- **item-analysis-checklist.md** — Step 3: per-item five-question analysis, including exception-by-exception pretext tests
- **attack-vectors.md** — Step 3 / Memorandum Argument B: defense attack lines organized by the exception the State claims
- **opposition-template.md** — Step 4: full Opposition / Motion in Limine document structure and preemptive-motion variant
- **memorandum-template.md** — Step 5: full Memorandum in Support structure (Sections I–V, Argument A–E) and key drafting rules
- **devonthink-search-protocol.md** — Step 1: DEVONthink search strings and the catalog of known 404(B) documents in the firm database
- **case-context-intake.md** — Step 2: intake checklist by source (attorney prompt, Prieur notice, discovery, prior case analysis)
