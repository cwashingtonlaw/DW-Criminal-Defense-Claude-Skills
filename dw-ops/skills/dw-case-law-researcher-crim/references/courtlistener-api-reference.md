# CourtListener REST API Reference

> Practical reference for the `dw-case-law-researcher-crim` skill. Covers the endpoints most relevant to Louisiana criminal defense research. For full docs, see https://www.courtlistener.com/help/api/

## Authentication

All requests require an API token in the header:
```
Authorization: Token <your_token>
```
Free key: https://www.courtlistener.com/help/api/rest/ → "API tokens" section.
Rate limit: 5,000 requests/hour.

---

## Data Model

CourtListener organizes case law in a hierarchy:

```
Court → Docket → Cluster → Opinion(s)
```

- **Court**: The tribunal (e.g., `lasc` = LA Supreme Court)
- **Docket**: The case-level record (docket number, parties, dates)
- **Cluster**: A group of opinions issued together for a single docket entry (contains metadata like date filed, citation, judges)
- **Opinion**: The actual text of a judicial decision (one cluster may have majority + concurrence + dissent)

### Why This Matters for D&W
When you find a case via search, you get a **cluster**. To read the full text, follow the cluster → opinion link. To find the procedural history and related filings, follow the cluster → docket link.

---

## Core Endpoints

### 1. Courts — `/api/rest/v4/courts/`

List or retrieve court metadata.

**Key fields**: `id` (court code), `full_name`, `citation_string`, `jurisdiction`, `in_use`

**Louisiana court codes** (use these for filtering):

| Code | Court |
|------|-------|
| `lasc` | Louisiana Supreme Court |
| `la1coa` | LA 1st Circuit Court of Appeal |
| `la2coa` | LA 2nd Circuit Court of Appeal |
| `la3coa` | LA 3rd Circuit Court of Appeal |
| `la4coa` | LA 4th Circuit Court of Appeal |
| `la5coa` | LA 5th Circuit Court of Appeal |
| `ca5` | U.S. Court of Appeals, 5th Circuit |
| `lawd` | U.S. District Court, Western District of LA |
| `lamd` | U.S. District Court, Middle District of LA |
| `laed` | U.S. District Court, Eastern District of LA |

**Example — get court details**:
```
GET /api/rest/v4/courts/lasc/
```

---

### 2. Dockets — `/api/rest/v4/dockets/`

Case-level records with docket numbers, party names, and links to clusters.

**Key fields**: `id`, `court`, `docket_number`, `case_name`, `date_filed`, `date_terminated`, `clusters` (linked), `source`

**Useful filters**:
- `court__id=lasc` — filter by court
- `docket_number=2019-00355` — exact docket number lookup
- `case_name__icontains=hunt` — partial name search
- `date_filed__gte=2020-01-01` — filed after date

**Example — find a docket by number**:
```
GET /api/rest/v4/dockets/?court__id=lasc&docket_number=2019-00355
```

**Example — find all dockets mentioning a party**:
```
GET /api/rest/v4/dockets/?case_name__icontains=state+v+hunt&court__id=lasc
```

---

### 3. Clusters — `/api/rest/v4/clusters/`

Groups of opinions from a single decision. This is the primary unit for citation and case metadata.

**Key fields**: `id`, `docket` (link), `sub_opinions` (list of opinion links), `case_name`, `date_filed`, `citation` (list of citation objects), `judges`, `precedential_status`, `syllabus`, `source`

**Useful filters**:
- `docket__court__id=lasc` — filter by court
- `date_filed__gte=2020-01-01` — filed after date
- `date_filed__lte=2025-12-31` — filed before date
- `citation__volume=XXX&citation__reporter=So.3d&citation__page=YYY` — lookup by citation
- `precedential_status=Published` — only published opinions

**Precedential status values**: `Published`, `Unpublished`, `Errata`, `Separate`, `In-chambers`, `Relating-to`, `Unknown`

**Example — find a cluster by citation**:
```
GET /api/rest/v4/clusters/?citation__volume=283&citation__reporter=So.3d&citation__page=1
```

**Example — recent published LA Supreme Court opinions**:
```
GET /api/rest/v4/clusters/?docket__court__id=lasc&precedential_status=Published&date_filed__gte=2024-01-01&ordering=-date_filed
```

---

### 4. Opinions — `/api/rest/v4/opinions/`

The actual text of judicial decisions.

**Key fields**: `id`, `cluster` (link), `author` (judge link), `type` (majority, concurrence, dissent, etc.), `plain_text`, `html`, `html_with_citations`, `download_url`

**Opinion type values**: `010combined`, `015unamimous`, `020lead`, `025plurality`, `030concurrence`, `040dissent`, `050addendum`, `060remittitur`, `070rehearing`, `080on-the-merits`, `090assigned`, `900special`

**Useful filters**:
- `cluster__id=12345` — all opinions in a cluster
- `type=040dissent` — only dissents
- `author__name_last__icontains=weimer` — opinions by a specific judge

**Example — get all opinions for a cluster**:
```
GET /api/rest/v4/opinions/?cluster__id=12345
```

**Example — read opinion text**:
```
GET /api/rest/v4/opinions/67890/
```
The response includes `plain_text` (raw text), `html` (formatted), and `html_with_citations` (with hyperlinked citations).

---

### 5. Legal Search — `/api/rest/v3/search/`

Full-text search across all CourtListener data. This is the most flexible endpoint for finding cases.

**Key parameters**:
- `q` — search query (supports Boolean: AND, OR, NOT, quotes for phrases)
- `type` — what to search: `o` (opinions), `r` (PACER filings), `d` (dockets), `p` (judges), `oa` (oral arguments)
- `court` — comma-separated court codes (e.g., `court=lasc,la3coa,ca5`)
- `filed_after` — date filter (YYYY-MM-DD)
- `filed_before` — date filter (YYYY-MM-DD)
- `cited_gt` — minimum citation count
- `cited_lt` — maximum citation count
- `ordering` — sort: `score desc` (relevance), `dateFiled desc` (newest), `dateFiled asc` (oldest), `citeCount desc` (most cited)
- `stat_Published` — include published opinions (`on`)
- `stat_Unpublished` — include unpublished (`on`)

**Example — search for traffic stop extension cases in Louisiana**:
```
GET /api/rest/v3/search/?q="traffic+stop"+AND+("extended"+OR+"prolonged")+AND+"drug+dog"&type=o&court=lasc,la1coa,la2coa,la3coa,la4coa,la5coa&stat_Published=on&ordering=score+desc
```

**Example — recent Miranda custody cases in 5th Circuit**:
```
GET /api/rest/v3/search/?q="Miranda"+AND+"custody"+AND+"free+to+leave"&type=o&court=ca5&filed_after=2020-01-01&ordering=dateFiled+desc
```

**Example — most-cited suppression opinions in Louisiana**:
```
GET /api/rest/v3/search/?q="motion+to+suppress"+AND+"Fourth+Amendment"&type=o&court=lasc&ordering=citeCount+desc
```

**Search tips**:
- The `snippet` field in results contains highlighted matching text — useful for quick relevance assessment
- Results are paginated; use `page` parameter for subsequent pages
- Combine `court` filter with `filed_after`/`filed_before` for precision
- The search also returns a `caseName`, `dateFiled`, `citation`, and `court` for each result

---

### 6. Citations — `/api/rest/v4/opinions-cited/`

Track citation relationships between opinions. Essential for building citation chains and checking if a case has been distinguished or overruled.

**Key fields**: `id`, `citing_opinion` (link), `cited_opinion` (link), `depth` (how many times cited within the opinion)

**Useful filters**:
- `cited_opinion__id=12345` — find all cases that **cite** opinion 12345 (forward citations)
- `citing_opinion__id=12345` — find all cases **cited by** opinion 12345 (backward citations)
- `depth__gte=2` — only substantive citations (mentioned 2+ times in the citing opinion)

**Example — find all cases citing a landmark opinion (forward citations)**:
```
GET /api/rest/v4/opinions-cited/?cited_opinion__id=12345&depth__gte=1
```

**Example — find all cases cited by an opinion (backward citations / authorities relied on)**:
```
GET /api/rest/v4/opinions-cited/?citing_opinion__id=12345
```

**Example — check if a Louisiana case has been cited by the Supreme Court**:
```
GET /api/rest/v4/opinions-cited/?cited_opinion__id=12345&citing_opinion__cluster__docket__court__id=lasc
```

### Citation Chain Strategy for D&W

1. Find the seminal case via search (e.g., *State v. Thompson* on traffic stop extensions)
2. Get its opinion ID from the cluster
3. Query forward citations: `opinions-cited/?cited_opinion__id=<ID>`
4. Filter to Louisiana courts to see how the principle has been applied locally
5. Check `depth` — higher depth means the citing court engaged substantively with the authority
6. Use the citing opinions' dates to track whether the trend is favorable or unfavorable

---

## Pagination

All list endpoints return paginated results:
```json
{
  "count": 150,
  "next": "https://www.courtlistener.com/api/rest/v4/clusters/?page=2",
  "previous": null,
  "results": [...]
}
```

Default page size is 20. Use `page_size` parameter (max varies by endpoint) to adjust.

---

## CourtListener MCP vs. REST API

The skill has access to both the CourtListener MCP server (12 tools) and the REST API directly. Use them for different purposes:

| Task | Use MCP | Use REST API |
|------|---------|-------------|
| Semantic/hybrid search | ✅ `search_opinions_semantic` | ❌ Not available via REST |
| Keyword search | ✅ `search_opinions_keyword` | ✅ `/api/rest/v3/search/` |
| Citation verification | ✅ `verify_citation` | ✅ Citation-based cluster lookup |
| Forward/backward citations | ✅ `get_citing_cases` | ✅ `/api/rest/v4/opinions-cited/` |
| Read full opinion text | ✅ `get_opinion` | ✅ `/api/rest/v4/opinions/<id>/` |
| Complex filtered queries | ❌ Limited filters | ✅ Full filter set |
| Docket-level research | ❌ Not available | ✅ `/api/rest/v4/dockets/` |
| Judge-specific research | ✅ `search_judges` | ✅ `/api/rest/v3/search/?type=p` |
| Bulk data retrieval | ❌ One-at-a-time | ✅ Paginated bulk access |

**Rule of thumb**: Start with the MCP tools (faster, semantic search). Fall back to the REST API when you need complex filtering, docket-level data, or bulk retrieval.

---

## Error Handling

| Status | Meaning | Action |
|--------|---------|--------|
| 200 | Success | Process results |
| 401 | Bad/missing token | Check `Authorization` header |
| 403 | Forbidden | Endpoint may require elevated access |
| 404 | Not found | Check ID/URL |
| 429 | Rate limited | Wait and retry; you get 5,000/hour |
| 500 | Server error | Retry after brief delay |

---

## Quick-Reference: D&W Research Patterns

### Pattern 1: Find and verify a case
```
1. Search: /api/rest/v3/search/?q="State v. Thompson"&court=lasc&type=o
2. Get cluster: /api/rest/v4/clusters/<cluster_id>/
3. Read opinion: /api/rest/v4/opinions/<opinion_id>/
4. Check citations: /api/rest/v4/opinions-cited/?cited_opinion__id=<opinion_id>
```

### Pattern 2: Build authority for a motion
```
1. Search: /api/rest/v3/search/?q=<legal issue>&court=lasc,la3coa,ca5&ordering=citeCount desc
2. Get top 5 most-cited results
3. For each: check forward citations for recent LA application
4. Flag any with adverse citing opinions (distinguished/overruled language)
```

### Pattern 3: Track how a SCOTUS/5th Circuit rule plays in Louisiana
```
1. Find the federal opinion's cluster ID
2. Forward citations: /api/rest/v4/opinions-cited/?cited_opinion__id=<ID>
3. Filter to LA courts in the citing opinions
4. Sort by date to see evolution
5. Check depth ≥ 2 for substantive treatment
```
