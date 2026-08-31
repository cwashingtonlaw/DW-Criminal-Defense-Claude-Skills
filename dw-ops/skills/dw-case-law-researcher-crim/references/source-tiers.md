# How the Five Sources Work Together — Tier Detail

Read at SKILL.md "How the Five Sources Work Together"; holds each source's coverage, why it runs where it does in the tier sequence, best uses, and exact tool names.

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
