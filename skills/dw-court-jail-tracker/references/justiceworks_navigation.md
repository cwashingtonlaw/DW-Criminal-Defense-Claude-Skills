# JusticeWorks portal navigation — scraping the My Cases view

Read this file before scraping. The JusticeWorks UI is a server-rendered DD7 (DefenderData 7) app, which means the page is mostly classic HTML with form posts — no SPA routing. Selectors tend to be stable across releases, but the operators do change CSS occasionally; if a selector below misses, fall back to text-content matching.

## Login

URL: `https://online.justiceworks.com/dd7/web/start/1199`

If the page shows a login form, **stop and ask Chris to log in manually in the open Chrome tab**, then resume. Don't store credentials in this skill — it'll be re-installed across machines and isn't a credential vault.

## Reaching "My Cases"

After login, the start page typically has a side nav with "My Cases," "My Calendar," "Search," etc. The DOM structure to look for:

- Side-nav anchor: `a[href*="myCases"]` or visible text "My Cases"
- The cases list lands at a URL containing `/dd7/web/myCases` or `/dd7/web/cases`

Once on the cases list:

1. Find the **status filter** — typically a dropdown labeled "Status" near the top of the table.
2. Set it to include both **"Open"** and **"Awaiting Bill"**. In DD7 this is sometimes a multi-select; if it's single-select, you'll need to run two passes (one filter, scrape, then change filter, scrape, dedupe by docket).
3. Find the **assigned-attorney filter** and confirm it's already restricted to Chris (some PDOs share the same My Cases view across the office; the URL `/start/1199` should be his personal view but verify).
4. Click "Apply" or whatever the filter-submit control is.

## Reading the case list

Each row is typically a `<tr>` inside a `<table class="caseList">` (or similar). Cell mapping observed in past versions of DD7:

| Cell | Field |
| --- | --- |
| 1 | Docket # (often a link to the case detail) |
| 2 | Section / Division |
| 3 | Client name (Last, First) |
| 4 | Charges (truncated; need detail page for full) |
| 5 | Status (Open / Awaiting Bill / Closed) |
| 6 | Next event type |
| 7 | Next event date |

You'll need to **click into each case row** to get the in-custody flag, last jail visit date, and the trial date if it's separate from the next event. There's no API, so this is a serial fetch — it will be slow. Budget ~2-3 seconds per case.

### What to extract from the case detail page

| Field | Where to find it |
| --- | --- |
| `docket` | URL or breadcrumb |
| `section` | "Section" label in case header |
| `ada` | "Prosecutor" or "ADA" field on case header |
| `client_name` | "Client" field |
| `charges` | "Charges" panel (concatenate count descriptions; mirror how the existing tracker formats them) |
| `next_court_event` | Top item in "Events" panel, type column |
| `next_court_date` | Top item in "Events" panel, date column |
| `trial_date` | "Trial Date" field if present, else first event with type containing "Trial" |
| `in_custody` | "Custody Status" field — true if value is "In Custody," "Jail," or "CCCC" (Calcasieu Correctional). False if "Out," "Bond," or "Released." |
| `last_jail_visit` | Look for a "Jail Visits" or "Contacts" sub-tab. If the visit log lives on a different system (e.g., the firm's internal tracker), set this to "" — `update_tracker.py` will preserve whatever Chris has manually entered in the JAIL VISIT column. |

If the detail page uses tabs (likely), use Chrome MCP's `find` to locate tab labels and click them programmatically rather than guessing CSS selectors.

## Output schema

Write the scraped rows as a JSON array to `~/.dw-tracker/scraped-cases-YYYY-MM-DD.json`:

```json
[
  {
    "docket": "16090-21",
    "section": "E",
    "ada": "Hall Lea R.",
    "client_name": "ANTONIO DEVON HADNOT",
    "charges": "First Degree Murder (2 Counts)",
    "next_court_event": "Trial Date",
    "next_court_date": "2026-04-13",
    "trial_date": "2026-04-13",
    "in_custody": true,
    "last_jail_visit": ""
  }
]
```

Use **ISO dates (YYYY-MM-DD)**. `update_tracker.py` reformats to MM/DD/YYYY for display.

## When selectors break

DD7 has had at least three layout updates in the past two years. If you can't find an expected element:

1. Use Chrome MCP's `read_page` to dump page text and visually identify the new structure.
2. Update the selector hints in this file and commit. Future runs benefit.
3. As a fallback, JusticeWorks usually has an "Export" button that produces a CSV. If selectors are too broken to scrape, look for that and download instead — `update_tracker.py` already accepts a CSV-derived JSON.

## Rate limiting

DD7 is hosted on Justice Systems' shared infra and gets cranky at >5 requests/sec. Add a 200ms `wait` between case-detail fetches.
