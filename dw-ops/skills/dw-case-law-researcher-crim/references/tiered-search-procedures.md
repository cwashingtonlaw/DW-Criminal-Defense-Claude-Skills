# Tiered Search Procedures

Read at SKILL.md Standalone Research Workflow — Step 2; holds the per-tier procedures: case.dev commands and strategy, CourtListener tool order and court filters, DEVONthink queries, Consensus trigger list, Westlaw / Fastcase / OpenCase Chrome procedures, and the Chrome automation ground rules.

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
