---
name: dw-case-law-researcher-crim
category: ops
description: >
  Multi-source legal research engine for D&W criminal defense: case.dev (case law + statutes),
  CourtListener (semantic search, citation verification, opinion text), DEVONthink (firm
  templates + prior work product), Consensus/Semantic Scholar (empirical research), and
  Westlaw/Fastcase/OpenCase via Chrome. ALWAYS invoke for "research case law," "find authority,"
  "find cases on," "what does the law say about," "pull up the case," "cite check," "shepardize,"
  "KeyCite," "is this still good law," "find studies on," "empirical research," "run Westlaw,"
  "search Fastcase," "search OpenCase," "legal research on," "find supporting authority," "look
  up the statute," "CourtListener," "find citing cases," "verify this citation," or any request
  for legal authority during motion drafting. Also auto-invoked by other D&W skills needing
  on-point authority. Do NOT use for template selection (use the template-selection-protocol in
  dw-shared-protocols-crim) or general web search unrelated to legal authority.
version: 1.1.0
---

# Case Law Researcher — Daniels & Washington

**Internal Use Only — Daniels & Washington Law Firm, LLC**

This skill finds on-point legal authority across five sources, synthesizes results into a structured research memo, and feeds citations directly into whatever motion or analysis is being drafted. It operates both standalone (attorney asks for research) and as a service layer called by other D&W skills mid-draft.

---

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any research questions, case briefs, prior research memos, draft motions, or discovery materials that frame the research scope, do not analyze anything yet.**

Your only response must be:
> *"Before I begin — are you uploading any additional research questions, case briefs, prior research memos, draft motions, opposing authority, or discovery materials that frame the research scope? I'll start the multi-source search only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** Mid-research discovery of an additional issue, a controlling case the attorney already located, or an opposing brief's authorities would change search strategy and may render Tier 1 results stale.

---

### Source Citation Mandate

Every factual assertion in the research memo — case holdings, statutory language, factual analogies, KeyCite/Bad Law flags, judge backgrounds, and empirical findings — must trace back to a verifiable source. Legal research feeds directly into motions and briefs; an unverified citation or paraphrased holding can mislead the court and expose the attorney to a Rule 11 / La. C.C.P. Art. 863 sanction risk.

**Citation format:** Cite the source database, opinion, statute, or article with full identifying information. Examples:
- `(State v. Prieur, 277 So.2d 126, 130 (La. 1973))`
- `(La. C.E. Art. 404(B)(1))`
- `(CourtListener Citation Verification — opinion ID 2123456, retrieved 2026-04-15)`
- `(case.dev search result — query "traffic stop drug dog Rodriguez", returned 2026-04-15)`
- `(DEVONthink — Prior Suppression Memo, Case File "Smith 2024", saved 2024-09-12)`
- `(Consensus search — false confession + juvenile, study DOI 10.xxxx, 2023)`
- `(Westlaw KeyCite — State v. Doe, 123 So.3d 456, retrieved 2026-04-15, no negative treatment)`

**Multiple-source rule:** When more than one source confirms a holding or factual claim, cite all of them — e.g., `(State v. Doe, 123 So.3d 456 (La. 2020); CourtListener Citation Verification — opinion ID 7891011, retrieved 2026-04-15)`.

**Unverified citations:** If a citation cannot be verified through CourtListener, case.dev, or Westlaw KeyCite, mark it `[UNVERIFIED — VERIFY BEFORE FILING]`. Never include an unverified citation in the memo without that flag.

**Where sourcing applies:** All cited authority — case law, statutes, constitutional provisions, secondary sources, empirical studies, and prior firm work product. Synthesis and analysis follow normal narrative format but must be traceable to the cited authorities.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load these references:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols-crim/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## How the Five Sources Work Together

Each source fills a different gap. The skill runs them in a tiered sequence — fast and cheap first, slow and deep last — so the attorney gets useful results quickly and can decide whether to go deeper.

- **Tier 1A — case.dev Legal Search** (always runs): case law, statutes, and legal authorities via the `casedev` CLI; API-based, fast, runs first
- **Tier 1B — CourtListener** (always runs, alongside case.dev): semantic / keyword / hybrid search, citation verification, full opinion text, citing cases, judge search via the CourtListener MCP tools; use the REST API (`references/courtlistener-api-reference.md`) for complex filtered or bulk queries. Run both in parallel and cross-reference — verify every case.dev citation through CourtListener before it goes in a filing
- **Tier 2 — DEVONthink Firm Library** (always runs): prior firm motions, templates, CLE materials, the LA Criminal Trial Practice Formulary, saved research memos
- **Tier 3 — Consensus / Semantic Scholar** (conditional): empirical research when the topic benefits from peer-reviewed backing (false confessions, eyewitness reliability, forensic methodology, etc.)
- **Tier 4 — Westlaw / Fastcase / OpenCase via Chrome** (on request or when deeper research is needed): KeyCite / Bad Law flags, headnotes, secondary sources; slowest, depends on attorney login

Read `references/source-tiers.md` now for each source's coverage, why it runs where it does, best uses, and exact tool names.

**Important**: The attorney always controls which platforms run. Never launch into any search without confirming platforms first (see Step 1 of the Standalone Research Workflow). For Tier 4 specifically, the attorney may prefer to do that research themselves, or the earlier tiers may be sufficient.

---

## Standalone Research Workflow

When the attorney directly asks for legal research (not called by another skill):

### Step 1: Clarify the Research Question and Confirm Platforms

Before searching, make sure you understand:
- **The legal issue**: What specific question of law needs answering? (e.g., "Can the state use a co-defendant's statement under the co-conspirator hearsay exception when the conspiracy charge was dropped?")
- **The jurisdiction priority**: Louisiana state courts are the default. Ask if federal (5th Circuit, W.D. La., M.D. La., E.D. La.) or other state authority is also wanted
- **The purpose**: Is this for a specific motion type? A memo to the attorney? General issue-spotting? This affects how deep to go
- **Any known starting points**: Does the attorney already have a case name, statute, or article number to build from?

**REQUIRED — Platform Confirmation**: always present the available sources and ask the attorney which ones to use before running any searches. Tailor the recommendation to the request, but always let the attorney confirm before executing. Exception — when invoked as a service layer by another D&W skill, use the calling skill's platform preferences; if none, default to case.dev + CourtListener + DEVONthink (Tiers 1A + 1B + 2) without asking. Read `references/platform-confirmation.md` now for the exact platform-menu prompt and the service-layer exception rules.

### Step 2: Run Tiered Searches

Run Tier 1A (case.dev) and Tier 1B (CourtListener) in parallel, then deduplicate and cross-reference — verify outliers through the other source and run CourtListener citation verification on every case.dev result bound for a filed pleading. Run Tier 2 (DEVONthink) for prior work product and templates. Run Tier 3 (Consensus) only when the topic touches an empirical trigger area. Run Tier 4 (Westlaw / Fastcase / OpenCase) only if selected in Step 1 — if Tiers 1–3 return thin or uncertain results, ask before escalating. Read `references/tiered-search-procedures.md` now for the case.dev commands and search strategy, the CourtListener tool order and Louisiana court filters, the DEVONthink queries, the Consensus trigger list, the per-platform Chrome procedures, and the Chrome automation ground rules.

### Step 3: Synthesize Results

After all tiers complete, produce a **Research Memo**: header (issue, case, date, researcher, sources consulted), Short Answer, Controlling Authority by weight (Louisiana Supreme Court, Louisiana Courts of Appeal with circuit noted, Fifth Circuit / Federal, Statutes & Code — each with citation-verified status and cited-by count), Prior Firm Work Product, Empirical Research, Adverse Authority, Citation Chain, and Flags. Read `references/research-memo-template.md` now for the full memo template.

### Step 4: Integration with Calling Skill

If this skill was invoked by another D&W skill (suppression motion, 404(b) opposition, etc.), return the Research Memo content in a format the calling skill can use directly:
- Citation blocks ready to paste into a memorandum in support
- Parenthetical descriptions for each case
- Page-specific pinpoint citations where available
- Citation verification status for each case (CourtListener-verified vs. needs KeyCite)
- Flag any citations that need additional KeyCite/Shepard's verification before filing

---

## Jurisdiction Priority

Louisiana criminal defense is the default context. When searching, prioritize authority in this order:

1. **Louisiana Supreme Court** — binding on all Louisiana courts
2. **Louisiana Court of Appeal, [client's circuit]** — binding within the circuit
3. **Louisiana Courts of Appeal, other circuits** — persuasive, useful for emerging issues or circuit splits
4. **Fifth Circuit Court of Appeals** — binding on federal constitutional issues, highly persuasive on state constitutional analogues
5. **U.S. Supreme Court** — binding on federal constitutional issues
6. **Other federal circuits** — persuasive only, but useful when 5th Circuit hasn't addressed the issue
7. **Other state supreme courts** — persuasive, especially states with similar code-based systems (Texas for procedure, Mississippi for 5th Circuit issues)

For federal cases (e.g., client is in W.D. La. or M.D. La.), adjust: 5th Circuit becomes binding, district court precedent within the same district is persuasive.

**CourtListener court codes** (for filtered searches):
- Louisiana Supreme Court: `lasc`
- LA 1st Circuit Court of Appeal: `la1coa`
- LA 2nd Circuit Court of Appeal: `la2coa`
- LA 3rd Circuit Court of Appeal: `la3coa`
- LA 4th Circuit Court of Appeal: `la4coa`
- LA 5th Circuit Court of Appeal: `la5coa`
- Fifth Circuit Court of Appeals: `ca5`
- Western District of Louisiana: `lawd`
- Middle District of Louisiana: `lamd`
- Eastern District of Louisiana: `laed`

---

## Search Strategy by Motion Type

When called by a motion-drafting skill, tailor the search to the motion's needs. Read `references/search-strategies.md` for detailed query templates organized by motion type.

Read `references/search-strategies.md` now — its closing quick-reference table maps each calling skill to its primary search focus and whether Consensus is needed, and the sections above it hold the detailed query templates by motion type.

---

## Quality Standards

Every citation in the Research Memo must include:
- **Full case name** (not abbreviated beyond standard legal citation form)
- **Official citation** (So.3d for Louisiana, F.3d/F.4th for federal) — if only a Westlaw citation is available, note it
- **Year of decision**
- **Parenthetical** describing the relevant holding (not just the general topic)
- **Pinpoint page** where possible (especially for quotable language)
- **CourtListener verification status** — note whether the citation was confirmed via CourtListener's citation verification tool

Flag system:
- `[VERIFIED — CourtListener]` — citation confirmed accurate through CourtListener's citation verification tool. This is the baseline for all Tier 1 results
- `[VERIFY — KeyCite/Shepard's needed]` — citation verified as existing but negative treatment status unknown. Use this for any citation that will appear in a filed pleading where you want to confirm it hasn't been overruled
- `[VERIFY — quote accuracy]` — quotation extracted from a summary, not the full opinion text. Verify against the actual opinion before filing
- `[RESEARCH — thin results]` — the search returned few results on this sub-issue; deeper Westlaw/Fastcase/OpenCase research recommended
- `[DISTINGUISH]` — adverse authority the state may cite; include a suggested distinguishing argument

---

## CourtListener Setup

The CourtListener MCP server is installed at `/sessions/eager-jolly-clarke/courtlistener-mcp/`. Read `references/courtlistener-api-reference.md` (section "CourtListener MCP Server Setup") now for the one-time activation steps and rate limits.

---

## Notes for Calling Skills

If you are a D&W skill invoking this researcher:

1. **Pass context**: Tell the researcher what motion you're drafting and what specific legal question needs authority. The more specific the question, the better the results. "Find suppression cases" is vague. "Find Louisiana cases where the court suppressed evidence from a traffic stop where the officer extended the stop beyond its original purpose to wait for a drug dog" gives the researcher something to work with.

2. **Specify jurisdiction**: If the case is in federal court, say so — it changes the priority order.

3. **Flag what you already have**: If you've already found authority in DEVONthink templates, tell the researcher so it doesn't duplicate effort.

4. **Use the output**: The Research Memo's citation blocks are formatted for direct insertion into a memorandum in support. The parentheticals are drafted in legal citation style. All citations include CourtListener verification status.

---

## Quick References

This skill uses the following reference materials, available in the `references/` subdirectory:

- **source-tiers.md** — "How the Five Sources Work Together"; per-source coverage, sequencing rationale, best uses, exact tool names
- **platform-confirmation.md** — Workflow Step 1; the required platform-menu prompt and the service-layer exception
- **tiered-search-procedures.md** — Workflow Step 2; case.dev, CourtListener, DEVONthink, Consensus, and Westlaw / Fastcase / OpenCase procedures plus Chrome ground rules
- **research-memo-template.md** — Workflow Step 3; the full Research Memo structure
- **courtlistener-api-reference.md** — Tier 1B and CourtListener Setup; REST API endpoints, auth, rate limits, Louisiana court codes, D&W research patterns, MCP server setup
- **search-strategies.md** — Search Strategy by Motion Type; tailored queries by motion type with semantic / keyword / Boolean patterns, plus the calling-skill quick-reference table
