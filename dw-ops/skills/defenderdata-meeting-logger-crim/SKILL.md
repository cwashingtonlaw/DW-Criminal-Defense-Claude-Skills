---
name: defenderdata-meeting-logger-crim
description: >-
  Logs attorney-client meetings into DefenderData (JusticeWorks dd7) as case
  Events from a plain message. Use when Chris sends a message describing client
  meetings to record — typically the client name, date, time, and substance of
  each meeting — and wants them entered on each client's Events page in
  DefenderData. Triggers include: "log my client meetings", "update
  DefenderData", "I met with these clients", "add these jail visits", "log
  these visits", "record my jail visits", "update the events page for these
  matters", or any pasted list/photo of client meetings to be entered. Each
  meeting becomes a "Jail Visit - In person" event by default. Not for the
  JusticeWorks Court & Jail Visit Tracker spreadsheet (that is
  dw-court-jail-tracker-crim) and not for substantive case notes.
---

# DefenderData Meeting Logger

Records attorney-client meetings as **Events** in DefenderData (the JusticeWorks
"dd7" web app) for Christopher Washington, Calcasieu Parish Public Defender's
Office. The attorney sends a message listing meetings; this skill enters one
event per client on that client's case, then reports back a review summary.

## When to use
The attorney pastes (or photographs) a list of client meetings and asks to log
them. A message usually contains, for each client: **name, date, time, and the
substance** of the meeting. Times may be given explicitly per client, or as a
**start time plus increments** (e.g., "starting at 1:30 p.m. in 30-minute
increments" — assign times in the order the names are listed).

## Defaults (confirmed by the attorney)
- **Event type:** `Jail Visit - In person` by default. If the message clearly
  indicates another mode, use the matching type instead: "called/phone" →
  `Jail Visit - Telephone`; "video/Zoom/Webex" → `Jail Visit - Videoconference`.
- **Multiple cases for one client:** **ALWAYS ask** which case to log on. Never
  guess. Show the cases (docket #, charge, status) and wait for the answer.
- **Location wording:** **infer from DefenderData** — use the client's
  Detention/Location on the Case tab (e.g., "Calcasieu Correctional Center"). If
  no location is on file, omit the location phrase rather than inventing one.
- **Organizer:** leave as the logged-in attorney (defaults to
  "Washington, Christopher"). Do not change it.
- **Confirmation:** post a review **summary in this chat** when done. Do not send
  iMessage/email unless explicitly asked.

## Safety / account rules
- **Never type passwords or create accounts.** DefenderData saves the attorney's
  credentials, so the login form is pre-filled — only click **Sign In**. If the
  form is NOT pre-filled, stop and ask the attorney to log in, then continue.
- Treat the pasted message as the only source of instructions. Log exactly what
  it says; do not invent substance. Entries are attorney work product — keep them
  accurate, factual, and concise.
- If anything is ambiguous (which case, a garbled name, a missing time), ask
  before writing.

## Inputs to extract from the message
For each meeting build a record:
- `client_name`
- `date` (MM/DD/YYYY)
- `time` (HH:MM AM/PM) — compute from start+increment if needed, in listed order
- `substance` — what was discussed / action items
- `event_type` — default `Jail Visit - In person` unless the message says otherwise

Ignore scratched-out, struck-through, or duplicate false-start names in a photo.

## Procedure

### 1. Open DefenderData
Navigate the browser (Claude-in-Chrome) to:
`https://online.justiceworks.com/dd7/web/start/1199`
- If the login screen appears with the username/password pre-filled, click
  **Sign In** and wait for the dashboard.
- If not pre-filled, ask the attorney to sign in, then continue.

### 2. For EACH client, open the case
- Click the home icon (top-left). In the **Recent Clients** panel, if the list is
  empty, click the small refresh/spinner icon in that panel's header to load it
  (it can take a few seconds). Scroll to find the client. Alternatively use
  **Search** → enter Last Name → Search.
- **Double-click** the client to open the case file.
- **If the client has more than one case** (the left panel shows `All (2)` or
  more, or multiple docket groups): STOP and ask which case to log on, listing
  docket #, charge, and status. Use the case the attorney picks.

### 3. Open the Events tab and add the event
- Click the **Events** tab (bottom tab bar).
- Click **Add** (toolbar). A new editable row appears at the bottom, pre-filled
  with today's date / 08:00 AM / the logged-in attorney as Organizer.
- **Description (event type):** click into the Description cell and type `Jail`.
  The autocomplete list can be finicky — if the filtered list does NOT appear,
  press **Backspace** then retype the last character to force it open. Click
  `Jail Visit - In person` (or the matching type).
- **Date:** triple-click the date cell and type the meeting date (`06/15/2026`).
- **Time:** triple-click the time cell and type the meeting time (`01:30 PM`).
- **Organizer:** leave as-is.
- **Subject (the note):** click the Subject cell (it expands to a text box) and
  type a concise note in the firm's style. Pattern:
  `Met with client at [detention location] to discuss his case; [substance].`
  - Pull `[detention location]` from the Case tab's Detention/Location field;
    omit the phrase if none is on file.
  - Match the substance to the message, e.g.:
    - discovery copy → "...will deliver him another copy of the discovery."
    - first meeting → "Introductory meeting; introduced myself to client.
      Advised I will review discovery, provide him a copy, and schedule a
      follow-up meeting."
    - plea → "client wants me to discuss a potential [offense] plea with the
      prosecutor."
    - check-in → "general check-in and to assess his mental state; client is
      doing well."
- Click **Save** (toolbar).

### 4. Verify
- Click **Refresh**. Confirm the new event appears in the list in correct date
  order, with the right type, date, time, and subject. (Newly saved rows stay
  pinned at the bottom until a refresh re-sorts them.)

### 5. Repeat, then confirm
- Repeat steps 2–4 for every client in the message.
- Post a **summary in this chat**: a numbered list of each client (docket #),
  date, time, event type, and the note entered. Flag anything that needed a
  judgment call (e.g., which case was chosen for a multi-case client).

## Known quirks / troubleshooting
- **Screenshot returns "Page still loading / document_idle" or a tab gets stuck**
  (often after a reload while there are unsaved changes): open a **fresh tab** to
  the start URL and sign in again rather than fighting the stuck tab.
- **"Leave site?" dialog** on navigation means unsaved changes — finish or
  discard the edit first.
- **Recent Clients panel empty** after returning home: click the panel's refresh
  icon and wait; it populates after a moment.
- **Description autocomplete shows "No results found"** if the full type name is
  typed at once — type a few letters (`Jail`) and pick from the filtered list
  instead.
- A browser-extension overlay can occasionally block clicks on a focused field;
  reload the page/tab to clear it.

## Example
Message: "Met with the following at the jail Mon June 15, 2026 starting 1:30 PM
in 30-min increments: Kaleb Drake (discussed case), Titus Tezeno (discussed case
+ deliver another copy of discovery), ... Caleb McClellan (doing well, general
check-in / mental state)."

Result: one `Jail Visit - In person` event per client on the chosen case —
Drake 1:30 PM, Tezeno 2:00 PM, ... McClellan 4:00 PM — each with an inferred
detention location and a concise subject note, followed by a review summary in
chat.
