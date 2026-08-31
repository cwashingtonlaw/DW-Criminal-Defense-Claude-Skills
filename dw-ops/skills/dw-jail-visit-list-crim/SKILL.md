---
name: dw-jail-visit-list-crim
category: ops
description: >-
  Build a checkable Apple Notes jail-visit list for Chris Washington. ALWAYS
  invoke for "jail visit list," "create a jail visit list," "make a list of
  people to see at the jail," "who I need to see at the jail," "jail visits for
  [date]," "schedule jail visits," or any time the user pastes or screenshots a
  list of clients to visit at the jail and wants a note to check them off.
  Produces one Apple Notes note in the "Jail Visits" folder, titled
  "Jail Visits — M/D/YY," with an H1 heading and one CHECKABLE circle per client
  formatted "Last, First (DOB)." Do NOT use for the Excel Court & Jail Visit
  Tracker (that is dw-court-jail-tracker-crim) or for logging completed visits
  into DefenderData (that is dw-defenderdata-meeting-logger-crim).
---

# Jail Visit List

Create a clean, checkable Apple Notes list of the people Chris needs to see at
the jail on a given day. The user checks off each circle after the visit.

## Inputs

The user will provide, in one of two ways:

1. **A screenshot** of a client roster (e.g., the JusticeWorks / DefenderData
   caseload view). Read the names and dates of birth directly from the image.
2. **A typed or pasted list** of names (with DOBs when available).

Plus a **visit date** (e.g., "7-16-26"). If no date is given, ask for it.

## Exact output format

Reproduce this format every time — it matches the version the user approved.

- **Location:** the `Jail Visits` folder in Apple Notes.
- **Title (H1 heading):** `Jail Visits — M/D/YY`
  - Use an em dash `—` (not a hyphen).
  - Date is the visit date, with no leading zeros on month/day and a 2-digit
    year. Example: `7-16-26` → `Jail Visits — 7/16/26`.
- **Body:** a **checklist** (checkable circles), one item per client:
  - `Last, First Middle Suffix (MM/DD/YYYY)`
  - Example: `Segobia, Drew Junior (10/16/1985)`
  - Keep DOB in parentheses with 2-digit month/day and 4-digit year exactly as
    shown on the source.
- Preserve the source order unless the user asks to sort.

### What to include / exclude
- Include only the **client** (the primary named person with a DOB).
- **Exclude** secondary attorney/co-counsel names that appear beneath a client
  on portal rosters (e.g., "Casanave, Andrew" or "Alexander, Edward" shown under
  an "Other, Other" row). Those are not people to visit.
- Repair obvious OCR line-wraps in a name (e.g., "Amador Espinal, Gerson
  Yovani" split across two lines) into a single clean line.

## Build procedure — IMPORTANT

A keystroke-intercepting app (e.g., Wispr Flow / dictation tools) can scramble
text that is **typed** character-by-character into Notes — turning "Segobia,
Drew Junior" into garbage and "Jail Visits" into "Aail Visio." **Never build or
edit this note by typing the text.** Use this two-step method instead:

**Step 1 — Write the content via the Apple Notes read/write MCP (no typing).**
- Use the create/update note tools of the Apple Notes MCP
  (`mcp__Read_and_Write_Apple_Notes__add_note` to create, or
  `update_note_content` if the note already exists), targeting the
  `Jail Visits` folder.
- Provide HTML: an H1 title followed by a `<ul>` of `<li>` items, e.g.:

  ```html
  <div><h1>Jail Visits — 7/16/26</h1></div>
  <ul>
  <li>Segobia, Drew Junior (10/16/1985)</li>
  <li>McClellan, Caleb Kyle (10/26/2000)</li>
  <!-- one <li> per client -->
  </ul>
  ```
- The MCP renders these as plain **bullets**, not checkboxes — that is expected;
  Step 2 converts them.
- Read the note back (`get_note_content`) to confirm the names landed correctly
  (the MCP write is not intercepted, so it will be clean).

**Step 2 — Convert the bullets to a checklist in the Notes app (no typing).**
- Bring up Apple Notes via the computer-use MCP: `request_access(["Notes"])`,
  then open the note.
- Click at the very start of the FIRST list item to place the cursor there.
- Press `Shift+Cmd+Down` to select from there through the end of the note
  (this selects all list items but leaves the H1 title unselected).
- Press `Shift+Cmd+L` to toggle the selection into a checklist (checkable
  circles). This uses only formatting keys — no characters are typed, so the
  scrambling problem does not occur.
- Take a screenshot to verify every client line now shows an empty circle and
  the title remains a heading.

## Verification (do this every run)
- Confirm the note title is `Jail Visits — M/D/YY` and lives in `Jail Visits`.
- Confirm the client count matches the source (state the number to the user).
- Confirm each line reads `Last, First (DOB)` and shows a checkable circle.
- Note: screenshots of Notes can look glyph-scrambled even when the underlying
  text is correct — trust `get_note_content`, and cross-check the DOBs, over the
  raw screenshot.

## Editing an existing list later
- To add/remove people, prefer editing via the MCP `update_note_content` (clean,
  no scrambling), then re-run Step 2 to restore the checkable circles — because
  a full MCP rewrite drops the checkbox formatting back to bullets.
- To check someone off, the user (or you, via computer-use) simply clicks the
  circle; do not retype the line.
