---
name: dw-case-law-researcher-crim
category: ops
description: >
  Multi-source legal research engine for Daniels & Washington criminal defense.
  Searches case.dev (case law + statutes), CourtListener (9M+ cases with semantic search,
  citation verification, full opinion text), DEVONthink (firm templates + prior work product),
  Consensus/Semantic Scholar (empirical/academic research), and Westlaw/Fastcase/OpenCase via
  Chrome (KeyCite, Shepard's, premium secondary sources). ALWAYS invoke for "research case law,"
  "find authority," "find cases on," "what does the law say about," "pull up the case,"
  "cite check," "shepardize," "KeyCite," "is this still good law," "find studies on,"
  "empirical research," "run Westlaw," "search Fastcase," "search OpenCase," "legal research on,"
  "find supporting authority," "look up the statute," "CourtListener," "find citing cases,"
  "who is the judge," "verify this citation," or any request for legal authority during motion
  drafting. Also auto-invoked by other D&W skills (suppression, 404(b), bond, sentencing, etc.)
  when they need on-point authority beyond DEVONthink templates. Do NOT use for template selection
  (use the template selection protocol in dw-shared-protocols-crim/references/template-selection-protocol.md)
  or for general web search unrelated to legal authority.
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

### Tier 1A: case.dev Legal Search (always runs)
- **What it covers**: Case law databases, statutes, legal authorities across jurisdictions
- **Why it runs first**: API-based, returns structured results in seconds, no login required
- **Best for**: Finding on-point opinions, statutory text, similar cases by topic or by citation similarity
- **Tool**: `casedev search legal` and `casedev search cases` (via the casedev CLI — read `casedev:search` skill if unfamiliar with syntax)

### Tier 1B: CourtListener (always runs, alongside case.dev)
- **What it covers**: 9+ million case opinions, 18+ million citations, 16,000+ judges, 3,353 courts, dockets, oral arguments
- **Why it runs alongside case.dev**: Free open API (Free Law Project nonprofit), semantic search via vector embeddings (natural language queries), plus citation verification against the full database. CourtListener and case.dev have different strengths — case.dev is better for statutory research and jurisdiction-filtered queries, CourtListener excels at semantic similarity, citation networks, and full opinion text retrieval
- **Best for**: Natural language case search ("cases where police extended a traffic stop to wait for a drug dog"), verifying citations are real and accurate, finding all cases that cite a given opinion, retrieving full opinion text without needing Westlaw, looking up judge backgrounds
- **Tools**: CourtListener MCP tools (installed at `/sessions/eager-jolly-clarke/courtlistener-mcp/`):
  - **Semantic search** — natural language case law search using vector embeddings
  - **Keyword search** — Boolean operators and fielded queries (court, date range, judge)
  - **Hybrid search** — combines semantic understanding with required keywords for precision
  - **Citation verification** — validates that a citation exists and is accurate against 18M+ records
  - **Get opinion** — retrieves full opinion text with metadata
  - **Citing cases** — finds all cases that cite a specific opinion (the "cited by" search)
  - **Judge search** — biographical data on 16,000+ federal and state judges
  - **Court info** — jurisdiction details for 3,353 courts

**Direct REST API access**: For complex filtered queries, docket-level research, or bulk retrieval beyond what the MCP tools support, use the CourtListener REST API directly. Read `references/courtlistener-api-reference.md` for endpoints, parameters, Louisiana court codes, and D&W-specific research patterns.

**CourtListener + case.dev together**: Run both in parallel when possible. Cross-reference results — if case.dev returns a citation, verify it through CourtListener's citation verification tool before including it in a filing. If CourtListener's semantic search surfaces cases that case.dev missed, add them. The two sources complement rather than duplicate each other.

### Tier 2: DEVONthink Firm Library (always runs)
- **What it covers**: Prior firm motions, templates, CLE materials, the LA Criminal Trial Practice Formulary, saved research memos
- **Why it matters**: The firm may have already briefed this exact issue. A prior filing that won or went unchallenged is more valuable than a fresh draft
- **Best for**: Finding prior work product that cited the same authority, firm templates addressing the legal issue, saved research
- **Tools**: `devonthink:search`, `devonthink:get_record_content`, `devonthink:list_group_content`

### Tier 3: Consensus / Semantic Scholar (conditional)
- **What it covers**: 200M+ academic papers from Semantic Scholar, PubMed, ArXiv
- **When it runs**: Only when the research topic benefits from empirical backing — false confessions, eyewitness reliability, forensic methodology validity, interrogation psychology, juvenile brain development, PTSD/trauma responses, DNA mixture statistics, cell tower accuracy studies, etc.
- **Why it matters**: Louisiana courts (and the 5th Circuit) increasingly cite social science research in suppression hearings, Daubert/Foret challenges, and sentencing mitigation. A peer-reviewed study can make or break a Daubert challenge
- **Tool**: Consensus MCP search (`mcp__375e8680-0d99-4473-91c4-f470b8b5a093__search`)

### Tier 4: Westlaw / Fastcase / OpenCase via Chrome (on request or when deeper research needed)
- **What it covers**: Full opinion text with headnotes, KeyCite (Westlaw), Bad Law flags (Fastcase), AI-assisted research (OpenCase), citing references, secondary sources, treatises, ALR annotations, law review articles
- **When it runs**: When the attorney says "run Westlaw," "check KeyCite," "shepardize this," "pull up the full opinion," "search OpenCase," OR when Tiers 1-2 return a key citation that needs validation beyond what CourtListener can provide (e.g., Westlaw's KeyCite negative treatment flags are more granular than CourtListener's citation data)
- **Why it's last**: Requires browser automation, is slower, and depends on active login sessions (Westlaw/Fastcase) or account access (OpenCase)
- **Tools**: Claude in Chrome MCP (`mcp__Claude_in_Chrome__*`) — navigate, read_page, get_page_text, form_input, find

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

**REQUIRED — Platform Confirmation**: Because this skill spans multiple research platforms with different speeds, costs, and coverage, always present the available sources and ask the attorney which ones to use before running any searches. Present them like this:

> **Which platforms should I search?**
> 1. **case.dev** — case law & statutes, API-based, fast
> 2. **CourtListener** — 9M+ opinions, semantic search, citation verification, free
> 3. **DEVONthink** — firm library, prior work product, templates
> 4. **Consensus** — academic/empirical research (200M+ papers)
> 5. **Westlaw / Fastcase / OpenCase** — premium databases, requires browser login
>
> I'd recommend [1, 2, 3] for this issue. Want me to run all of those, or a different combination?

Tailor the recommendation to the request — e.g., suggest Consensus only when empirical research is relevant, suggest Westlaw only when KeyCite/Shepard's validation is needed. But always let the attorney confirm before executing.

**Exception — called by another skill**: When invoked as a service layer by another D&W skill (e.g., `dw-suppression-motion-crim` calls for authority), use the calling skill's platform preferences if specified. If not specified, default to case.dev + CourtListener + DEVONthink (Tiers 1A + 1B + 2) without asking, since the attorney already initiated the parent workflow. The attorney can always say "also run Westlaw" or "skip DEVONthink" to override.

### Step 2: Run Tiered Searches

**Tier 1A — case.dev** (run in parallel with Tier 1B):
```bash
# Topic-based legal search (default: broad, then narrow)
casedev search legal "[legal issue in search-friendly terms]" --jurisdiction "louisiana" --limit 15 --json

# If attorney provided a specific case, find similar authority
casedev search cases --url "[case URL]" --json

# For statutory research
casedev search legal "[statute number or topic]" --jurisdiction "louisiana" --json
```

Search strategy for case.dev:
- Run a **broad query** first (the legal principle), then a **narrow query** (the specific factual scenario)
- If the issue spans state and federal, run both `--jurisdiction "louisiana"` and `--jurisdiction "5th circuit"` (or omit jurisdiction for all)
- Use `--deep` flag for complex issues that benefit from multi-query analysis
- Use `--alt-query` to provide alternative phrasings of the same issue

**Tier 1B — CourtListener** (run in parallel with Tier 1A):

Use CourtListener's tools in this order:

1. **Semantic search** for the legal issue in natural language — this is CourtListener's strongest feature. Phrase the query the way you'd describe the issue to a colleague, not as Boolean operators:
   - Good: "police extended traffic stop beyond original purpose to wait for drug dog without reasonable suspicion"
   - Bad: "traffic stop AND drug dog AND extended"

2. **Keyword search** to catch anything semantic search might miss — use Boolean operators, filter by court (Louisiana courts), and date range:
   - Filter to Louisiana: use court filter for `lasc` (Supreme Court), `la1coa` through `la5coa` (Courts of Appeal), `ca5` (5th Circuit)

3. **Citation verification** for every case you plan to include in the Research Memo — confirm the citation is real and accurate before the attorney relies on it

4. **Citing cases** search when you find a strong on-point case — find everything that cites it to build the full citation chain and check for negative treatment

5. **Judge search** if the attorney asks about the assigned judge's background, prior rulings, or tendencies

**Cross-referencing Tier 1A + 1B results**: After both searches complete, deduplicate. If a case appears in both results, note it — dual hits increase confidence. If case.dev found a case that CourtListener didn't (or vice versa), verify the outlier through the other source before including it. Use CourtListener's citation verification tool on every case.dev result that will appear in a filed pleading.

**Tier 2 — DEVONthink**:
```
devonthink:search
  query: "[legal issue keywords]"
  databaseName: "Law Library-Criminal"
  limit: 10

devonthink:search
  query: "tag:research OR tag:memo [issue keywords]"
  databaseName: "Law Library-Criminal"
  limit: 10
```

Search strategy for DEVONthink:
- Search the `Law Library-Criminal` database first
- Also search within `06 - Law & Research/` group if doing case-specific research
- Look for prior filings that addressed the same legal issue (these will have the firm's tested arguments and citation chains)
- Check for saved research memos from prior cases on the same topic

**Tier 3 — Consensus** (if applicable):
```
Consensus MCP search:
  query: "[academic search terms — use research terminology, not legal terminology]"
  year_min: 2010  (for recent studies; adjust based on topic)
```

Trigger Consensus when the research topic touches any of these areas:
- Eyewitness identification reliability (cross-racial ID, weapon focus, stress effects, confidence-accuracy relationship)
- False confessions and interrogation psychology (Reid Technique effectiveness, juvenile susceptibility, intellectual disability)
- Forensic science methodology (DNA mixture interpretation, bite mark analysis, hair microscopy, fingerprint error rates, ballistics)
- Memory and suggestibility (child witness competency, delayed disclosure in sexual abuse, trauma and memory)
- Sentencing and recidivism (juvenile brain development, rehabilitation outcomes, risk assessment instrument validity)
- Cell site location accuracy (granularity limitations, indoor vs. outdoor, urban vs. rural)
- Drug recognition expert (DRE) reliability
- Arson investigation methodology (debunked indicators, modern fire science)

**Tier 4 — Westlaw / Fastcase / OpenCase** (only if selected in Step 1):

Only run if the attorney selected Westlaw, Fastcase, or OpenCase during the platform confirmation in Step 1. If the attorney didn't select Tier 4 upfront but the earlier tiers returned thin or uncertain results, ask before escalating:
> "Tiers 1–3 returned [brief summary of gaps]. Would you like me to also check Westlaw, Fastcase, or OpenCase?"

If approved, the attorney chooses which platform(s) to use:

**Westlaw** (`westlaw.com` or `1.next.westlaw.com`):
1. Use Chrome MCP to navigate to Westlaw
2. Check if already logged in — look for the search bar on the main research page
3. If not logged in, notify the attorney: "Westlaw needs a login. Can you log in and let me know when you're on the main search page?"
4. Once on the search page:
   - Use `form_input` to enter the search query in the main search bar
   - Use `get_page_text` to read results
   - For KeyCite: navigate to the case, look for the KeyCite status flag (green, yellow, red, orange)
   - For full text: click into the opinion and use `get_page_text` to extract

**Fastcase** (`fastcase.com`):
1. Use Chrome MCP to navigate to Fastcase
2. Same login check — notify attorney if credentials needed
3. Once logged in:
   - Enter search terms in the search interface
   - Use `get_page_text` to read results and opinion text
   - Check Bad Law flags and Authority Check for citation validity

**OpenCase** (`opencase.com`):
1. Use Chrome MCP to navigate to OpenCase
2. Check login status — OpenCase has a free tier and paid Pro tier
3. If not logged in, notify the attorney: "OpenCase needs a login. Can you log in and let me know when you're ready?"
4. Once on the research page:
   - OpenCase uses AI-assisted natural language search trained on Cornell LII's database
   - Enter the legal question in natural language (OpenCase is optimized for this, unlike Westlaw's Boolean-heavy syntax)
   - Use `get_page_text` to read results — OpenCase provides case summaries with verified citations
   - OpenCase also has a Microsoft Word plugin — if the attorney is drafting in Word, suggest using the Word plugin for inline citation insertion

**Chrome automation ground rules** (applies to all three platforms):
- Never store or log any login credentials
- If the page shows a login screen, stop and ask the attorney to authenticate — do not attempt to fill login forms
- Read results using `get_page_text` rather than screenshotting (faster, more reliable)
- If the page structure is unfamiliar or has changed, describe what you see and ask the attorney for guidance rather than guessing at clicks

### Step 3: Synthesize Results

After all tiers complete, produce a **Research Memo** with this structure:

```
# Legal Research Memo
## [Legal Issue — one-line statement of the question]

**Case**: [Client name / Docket number if available]
**Date**: [Current date]
**Researched by**: Claude / Daniels & Washington
**Sources consulted**: [List which tiers were used]

---

## Short Answer
[2-3 sentence answer to the legal question, citing the controlling authority]

## Controlling Authority
[The most on-point cases and statutes, organized by weight]

### Louisiana Supreme Court
- **[Case Name]**, [Citation] ([Year]) — [1-2 sentence holding and relevance]
  - Citation verified: [Yes/No — via CourtListener] | Cited by: [X cases]

### Louisiana Courts of Appeal
- **[Case Name]**, [Citation] ([Year]) — [1-2 sentence holding and relevance]
  - [Note which circuit — 1st, 2nd, 3rd, 4th, 5th — and whether it's the client's circuit]
  - Citation verified: [Yes/No] | Cited by: [X cases]

### Fifth Circuit / Federal
- **[Case Name]**, [Citation] ([Year]) — [1-2 sentence holding and relevance]
  - Citation verified: [Yes/No] | Cited by: [X cases]

### Statutes & Code
- **[Statute]** — [What it provides and how it applies]

## Prior Firm Work Product
[If DEVONthink returned relevant prior filings]
- **[Document title]** (DEVONthink ID: [UUID]) — [How this prior filing addressed the same issue, what arguments it used, outcome if known]

## Empirical Research
[If Consensus was consulted]
- **[Author(s)]**, "[Paper Title]," *[Journal]* ([Year]) — [Key finding and how it supports the defense argument]
  - Cited [X] times | [Study type] | Sample: [N]

## Adverse Authority
[Cases or statutes that cut against the defense position — critical for candor and for preparing responses]
- **[Case Name]**, [Citation] — [Why it's adverse and how to distinguish it]

## Citation Chain
[For the strongest on-point case, list its full citation chain via CourtListener's "citing cases" tool — shows how the legal principle has developed and whether the trend favors the defense]

## Flags
- [VERIFY — KeyCite/Shepard's needed]: [Citations where CourtListener verification passed but Westlaw/Fastcase KeyCite would add confidence before filing]
- [VERIFY — quote accuracy]: [Quotations from summaries, not full opinion text — verify against actual opinion]
- [RESEARCH — thin results]: [Sub-issues where Tiers 1-2 returned few results; deeper Westlaw/Fastcase/OpenCase research recommended]
- [DISTINGUISH — adverse authority]: [Cases the state will likely cite that need distinguishing arguments]
- [VERIFIED — CourtListener confirmed]: [Citations confirmed accurate through CourtListener's citation verification]
```

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

Quick reference for common patterns:

| Calling Skill | Primary Search Focus | Consensus Needed? |
|---|---|---|
| `dw-suppression-motion-crim` (4th Amdt) | Warrant requirements, probable cause, good faith exception, fruit of poisonous tree | Rarely |
| `dw-suppression-motion-crim` (5th Amdt) | Miranda, voluntariness, custody analysis, invocation of rights | Yes — false confession research, interrogation psychology |
| `dw-404b-opposition-crim` | Prieur notice requirements, Art. 404(B) exceptions, balancing test, limiting instructions | No |
| `dw-bond-and-release-motion-crim` | Art. 316/341 factors, excessive bail, pretrial detention conditions | Sometimes — risk assessment validity |
| `dw-sentencing-mitigation-specialist-crim` | Art. 894.1 factors, Dorthey, excessive sentence jurisprudence, youthful offender | Yes — rehabilitation, brain development, trauma |
| `dw-expert-witness-evaluator-crim` | Daubert/Foret reliability factors, Art. 702, specific methodology challenges | Yes — methodology validity studies |
| `dw-eyewitness-identification-auditor-crim` | Manson/Neil v. Biggers factors, Henderson framework, suggestive procedures | Yes — eyewitness reliability research |
| `dw-habitual-offender-auditor-crim` | Art. 529.1, predicate validity, Boykin requirements, cleansing period | No |
| `dw-pretrial-motion-library-crim` | Varies by motion type — speedy trial (Barker), severance, venue, compel discovery | Rarely |
| `dw-jury-instructions-builder-crim` | Responsive verdicts, lesser included offenses, self-defense, specific intent | No |

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

The CourtListener MCP server is installed at `/sessions/eager-jolly-clarke/courtlistener-mcp/`.

**To activate** (one-time setup):
1. Register for a free API key at https://www.courtlistener.com/help/api/rest/
2. Create the `.env` file: `cp /sessions/eager-jolly-clarke/courtlistener-mcp/.env.example /sessions/eager-jolly-clarke/courtlistener-mcp/.env`
3. Add your API key to the `.env` file
4. Add the MCP to your Claude configuration: `claude mcp add courtlistener python /sessions/eager-jolly-clarke/courtlistener-mcp/src/server.py`

**Rate limits**: 5,000 API requests per hour (more than sufficient for research sessions).

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

- **courtlistener-api-reference.md** — Practical reference for the CourtListener REST API endpoints most relevant to Louisiana criminal defense research (auth, rate limits, endpoint patterns)
- **search-strategies.md** — Tailored CourtListener search queries by motion type, with semantic/keyword/Boolean patterns and Louisiana court filters
