---
name: dw-court-jail-tracker
description: Refresh the Calcasieu Public Defender Court & Jail Visit Tracker for Chris Washington. ALWAYS invoke for "update the tracker," "court and jail tracker," "refresh my cases," "who do I need to see this week," "weekly visit list," "jail visits due," "pull my cases from JusticeWorks," "court and jail visit tracker," "update court tracker," "run the Sunday case sweep," or any request to refresh assigned-case status from the JusticeWorks portal. Pulls Open and Awaiting-Bill cases from the JusticeWorks portal at online.justiceworks.com/dd7/web/start/1199, merges them into the firm Excel tracker at "Court & Jail Visit Tracker.xlsx," recomputes jail-visit OVERDUE/OK status (more than 30 days since last visit triggers OVERDUE), and dispatches a "who you need to see" reminder via email and Google Chat. Designed to run weekly on Sunday at midnight via scheduled task, but also works on demand.
---

# DW Court & Jail Visit Tracker

This skill keeps Chris Washington's weekly visit list current. It runs end-to-end:

1. **Scrape** the Calcasieu PDO JusticeWorks portal for his assigned Open + Awaiting-Bill cases.
2. **Merge** that data into the firm tracker spreadsheet, preserving manual edits to the JAIL VISIT column.
3. **Recompute** jail-visit status (OVERDUE if last visit >30 days ago) and identify who needs to be seen this week.
4. **Dispatch** the visit list to two channels: email and Google Chat.

The skill is intentionally split into deterministic Python scripts for the parts a script can do (Excel I/O, status math, HTTP webhooks) and inline orchestration for the parts that need Claude's MCPs (Chrome scraping, Gmail). Don't push everything into Python — Chrome MCP and the Gmail MCP aren't reachable from a script subprocess.

## Files in this skill

```
dw-court-jail-tracker/
├── SKILL.md                          ← you are here
├── scripts/
│   ├── update_tracker.py             ← merges scraped rows into the xlsx
│   ├── compute_visit_list.py         ← decides who needs to be seen
│   ├── post_google_chat.py           ← POSTs the digest to a Chat webhook
│   └── config.py                     ← loads credentials from ~/.dw-tracker/config.json
├── references/
│   ├── justiceworks_navigation.md    ← exact selectors / page flow for the portal
│   └── google_chat_webhook_setup.md  ← how to create the incoming-webhook URL
└── assets/
    ├── config.example.json           ← template for ~/.dw-tracker/config.json
    └── visit_email_template.html     ← Gmail body template
```

## Constants

| Thing | Value |
| --- | --- |
| Portal URL | `https://online.justiceworks.com/dd7/web/start/1199` |
| Tracker xlsx | `/Users/greatelephant82/Library/CloudStorage/GoogleDrive-cjw@danielswashington.com/Shared drives/CALCASIEU PDO Files/Court & Jail Visit Tracker/Court & Jail Visit Tracker.xlsx` |
| Config file | `~/.dw-tracker/config.json` (created on first run) |
| Visit cadence | OVERDUE if >30 days since last jail visit |
| Court-soon window | Court date within 7 days |
| Trial-soon window | Trial date within 30 days |

## Execution flow

Step through these in order. If a step fails, stop and surface the error to Chris — do NOT silently fall through to the next step, because partial runs put bad data in the tracker and false reminders in his inbox.

### Step 1 — First-run config check

Read `~/.dw-tracker/config.json`. If it doesn't exist, copy `assets/config.example.json` there and tell Chris exactly which fields he needs to fill in:

- `gmail_to` — his email (default: cjw@danielswashington.com)
- `google_chat_webhook_url` — incoming webhook URL (see `references/google_chat_webhook_setup.md`)

If `google_chat_webhook_url` is still the placeholder string (`"FILL_ME_IN"`), skip Google Chat for this run and tell Chris at the end. Don't block the whole run on a missing webhook — the email always works because Gmail is already authenticated.

### Step 2 — Scrape the portal via Chrome MCP

Use the Claude-in-Chrome MCP (`mcp__Claude_in_Chrome__*`). The full selector map and page flow lives in `references/justiceworks_navigation.md` — **read that file before scraping**.

Quick version:

1. `navigate` to `https://online.justiceworks.com/dd7/web/start/1199`.
2. `read_page` to check whether Chris is already logged in. If you see a login form, stop and tell him to log in manually, then resume. (Don't try to enter credentials — they're not in config and shouldn't be.)
3. Navigate to the "My Cases" view, set the status filter to include both "Open" and "Awaiting Bill," and read the case list.
4. For each case extract: docket #, section, ADA, client name, charges, next court event, next court date, trial date, in-custody flag, last jail visit date.

Save the scraped rows as JSON to `~/.dw-tracker/scraped-cases-YYYY-MM-DD.json`. This both gives `update_tracker.py` an input file and creates an audit trail.

If the portal layout has changed and selectors fail, do NOT guess — read the page text, figure out the new structure, update `references/justiceworks_navigation.md` so the next run benefits, then proceed.

### Step 3 — Merge into the tracker

Run:

```bash
python /path/to/dw-court-jail-tracker/scripts/update_tracker.py \
  --scraped ~/.dw-tracker/scraped-cases-YYYY-MM-DD.json \
  --tracker "/Users/greatelephant82/Library/CloudStorage/GoogleDrive-cjw@danielswashington.com/Shared drives/CALCASIEU PDO Files/Court & Jail Visit Tracker/Court & Jail Visit Tracker.xlsx"
```

The script:
- Backs up the xlsx to `~/.dw-tracker/backups/Tracker-YYYY-MM-DD.xlsx` first (always, before any edit — this has saved real bacon).
- Matches scraped rows to existing rows by DOCKET # (the only stable key).
- For matched rows: updates SECTION, ADA, CLIENT NAME, CHARGES, NEXT COURT EVENT, NEXT COURT DATE, TRIAL DATE — but **never touches JAIL VISIT** (that's manually entered when Chris actually visits).
- For new rows: appends to the bottom with JAIL VISIT blank.
- For rows in the tracker but not in the scrape: leaves them alone (case may have closed; Chris decides whether to delete).
- Recomputes JAIL VISIT NEEDED for every in-custody case: `OVERDUE (N days)` if N > 30, `OK (N days)` otherwise. If JAIL VISIT is blank for an in-custody client, mark `NEVER VISITED`.
- Writes a JSON summary to stdout: `{"new_cases": [...], "updated_cases": [...], "overdue_visits": [...]}` — this is what Step 5 reads.

### Step 4 — Build the visit list

Run:

```bash
python /path/to/dw-court-jail-tracker/scripts/compute_visit_list.py \
  --tracker "/Users/greatelephant82/Library/CloudStorage/GoogleDrive-cjw@danielswashington.com/Shared drives/CALCASIEU PDO Files/Court & Jail Visit Tracker/Court & Jail Visit Tracker.xlsx" \
  --update-summary <path-to-Step-3-stdout-saved-as-json>
```

It produces a JSON object with four buckets, each a list of `{docket, client, why, when}` entries:

- `jail_visits_overdue` — JAIL VISIT NEEDED is OVERDUE or NEVER VISITED.
- `court_within_7_days` — NEXT COURT DATE is within 7 days of today.
- `trial_within_30_days` — TRIAL DATE is within 30 days of today.
- `new_cases` — appeared on the docket since the previous run (read from `~/.dw-tracker/last-run.json`, then update that file).

This is the single source of truth for what gets sent to every channel.

### Step 5 — Dispatch the two notifications

Send both. If a channel errors, log it and continue — don't let one broken channel suppress the other.

#### 5a. Email (via Gmail MCP)

Use `mcp__9df24712-...__create_draft` (Gmail). Render `assets/visit_email_template.html`, substituting in the four buckets from Step 4. Subject: `Weekly visit list — N overdue, M court soon (YYYY-MM-DD)`. Send to `gmail_to` from config.

If you can send directly (not just draft), do that. Otherwise create a draft and tell Chris where to find it.

#### 5b. Google Chat (via webhook)

Run:

```bash
python /path/to/dw-court-jail-tracker/scripts/post_google_chat.py \
  --webhook-url "$(jq -r .google_chat_webhook_url ~/.dw-tracker/config.json)" \
  --visit-list <path-to-Step-4-output>
```

Posts a Card-formatted message with collapsible sections per bucket.

### Step 6 — Report back

Post a one-screen summary to Chris in the chat:

```
Tracker updated. Backed up to ~/.dw-tracker/backups/Tracker-2026-04-27.xlsx.

7 new cases added, 3 cases updated.
Visit list this week:
  • 4 jail visits OVERDUE (top: HADNOT, PETE, LANDRY)
  • 6 clients with court in next 7 days
  • 2 trials within 30 days
  • 7 new cases since last Sunday

Notifications sent: ✅ email  ✅ Google Chat
```

If a notification channel was skipped (placeholder config) or failed, replace the ✅ with ⏭ or ❌ and one-line the reason.

## Triggering this skill from a schedule

The schedule is set up via `mcp__scheduled-tasks__create_scheduled_task` separately — see Chris's "Sunday tracker sweep" scheduled task. The task just sends Cowork the prompt: `Run the Sunday case sweep — update the court and jail tracker.`

## Things that are deliberate, in case you want to "improve" them

- **JAIL VISIT column is sacred.** Never overwrite it from the scrape. Chris fills it by hand when he actually goes to the jail. If you sync it, his real visit data dies.
- **Tracker rows are never deleted automatically.** A case missing from the scrape might have been disposed of, or it might be a one-week portal glitch. Chris decides.
- **Config lives in `~/.dw-tracker/`, not in this skill folder.** Skills get re-installed; config shouldn't get clobbered.
- **Both channels send the same content, just formatted differently.** Don't try to "smart" either one of them into a different list — the redundancy is the point. Chris sees the list whether he's at his desk or in chat.
- **The OVERDUE threshold (30 days) is in `compute_visit_list.py` as a constant.** If the firm's policy changes, edit there once.

## Failure modes you'll actually hit

| Symptom | Cause | Fix |
| --- | --- | --- |
| Chrome MCP shows JusticeWorks login page | Session expired | Tell Chris to log in manually in the open Chrome tab, then resume |
| `update_tracker.py` errors "tracker locked" | Excel is open on Chris's machine | Tell him to close it, then re-run from Step 3 |
| Gmail MCP returns 401 | OAuth expired | Suggest reconnecting via `mcp-registry__suggest_connectors` for Gmail |
| Google Chat webhook returns 404 | Webhook URL was rotated/deleted | Have him generate a new one and update config |
| Scraped JSON has 0 rows | Portal filter not applied or selectors changed | Re-read `references/justiceworks_navigation.md` and the portal page; update selectors |
