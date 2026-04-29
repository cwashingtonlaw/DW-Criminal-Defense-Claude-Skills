---
name: dw-case-tracker-updater
description: >
  Update the Court & Jail Visit Tracker from Defender Data. ALWAYS invoke for "update the tracker,"
  "jail visit tracker," "case tracker update," "check jail visits," "update court dates,"
  "run the tracker," "Defender Data update," "update the spreadsheet from Defender Data,"
  or "who am I overdue to visit." Logs into Defender Data, reviews all assigned cases,
  collects docket/section/ADA/charges/court events/jail visits, updates the Excel tracker,
  and flags overdue jail visits in RED. This is a browser-automation skill requiring
  Claude in Chrome.
---

# Court & Jail Visit Tracker Updater — Daniels & Washington

Automates the bi-weekly process of reviewing all cases in Defender Data and updating the
CALCASIEU Contract Cases (Court & Jail Visit Tracker).xlsx spreadsheet. Flags any client
whose last jail visit was more than 30 days ago in RED.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before drafting any deliverable, read `dw-shared-protocols/SKILL.md` and load these references:

1. `dw-shared-protocols/references/attorney-work-product-marking.md` — apply work product marking to all deliverable headers
2. `dw-shared-protocols/references/output-path-formula.md` — use for all output file paths (anchored on `CASE_ROOT`)

Do not proceed to Step 1 until these protocols are loaded. All deliverables from this skill are internal work product — apply marking per the shared protocol. Output paths follow the Cowork Analysis formula: `{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`.

---

## When to Use This Skill

Use this skill whenever the attorney says:
- "Update the jail visit tracker"
- "Run the case tracker update"
- "Check my jail visits"
- "Who am I overdue to visit?"
- "Update court dates from Defender Data"
- "Pull my cases from Defender Data"
- "Update the spreadsheet"
- Or any scheduled run of the bi-weekly tracker task

---

## Prerequisites

- **Browser**: Claude in Chrome extension active with a Chrome tab available
- **Defender Data URL**: `https://online.justiceworks.com/dd7/web/start/1199`
- **Attorney**: Christopher Washington
- **Tracker file**: `CALCASIEU Contract Cases (Court & Jail Visit Tracker).xlsx` in the mounted workspace folder
- **Python**: openpyxl installed (`pip install openpyxl --break-system-packages`)

---

## Workflow

### Phase 1: Login to Defender Data

1. Navigate to `https://online.justiceworks.com/dd7/web/start/1199` using Claude in Chrome
2. Take a screenshot to check the current state
3. **If a login form is visible:**
   - Check if Chrome has saved credentials or 1Password auto-fills
   - If credentials are auto-filled, click the Login button
   - If no auto-fill, notify the user: "Please log into Defender Data. Let me know when you're ready."
   - Wait for user confirmation before proceeding
4. **If already logged in:** Proceed directly to Phase 2

### Phase 2: Search for All Assigned Cases

1. Click the **Search** button in the top toolbar
2. In the search form, set **Attorney** to "Washington, Ch" (type it in the Attorney field)
3. Click the **Search** button within the form to execute
4. Collapse the search form by clicking the collapse arrow to reveal the results grid
5. Take a screenshot and count total cases in the results header (e.g., "Results (26)")
6. Record the total count — this is how many cases to process

### Phase 3: Review Each Case (Case Tab + Events Tab)

For each case, collect:
- **From Case tab**: Docket Number, Section, ADA, Judge, Status (Open/Closed), Charges
- **From Events tab**: Last jail visit date, next court event, next court date, trial date

#### Navigation Pattern

1. **Double-click the first case** in the search results grid to open it
2. The Case tab loads by default — record docket, section, ADA, status
3. Click the **Events** tab at the bottom of the page
4. Scan events for:
   - Most recent "Jail Visit - In person" or "Jail Visit - Telephone" entry → record the date
   - Upcoming Trial Date, Pre Trial, Sentence, Status Hearing, Art 701 events → record as next court event/date
5. Click **Next** in the toolbar to advance to the next case
6. Repeat steps 2-5 for all cases

#### Important Navigation Notes

- The search results grid uses **virtual scrolling** — only ~15 DOM elements render at a time even for 26+ records. Do not try to click rows that may have shifted in the DOM.
- **Always use the Next/Prev buttons** to navigate between cases. If Prev/Next disappear (which happens if you click a sidebar case instead of using Next), return to Search results and re-run the search to restore navigation.
- If a case status shows "Closed" with a Result (e.g., "Withdrawn," "Jury GAC," "Plea - Lesser Felony"), mark it as CLOSED and skip the Events tab.

### Phase 4: Update the Excel Tracker

Read `references/excel-update-template.md` for the complete Python script template, then execute it with the collected data.

#### Column Mapping

| Column | Field | Source |
|--------|-------|--------|
| A | DOCKET # | Case tab → Docket Number |
| B | SECTION | Case tab → Organizations → Section |
| C | ADA | Case tab → Personnel → ADA |
| D | CLIENT NAME | Case header (already in tracker for existing clients) |
| E | CHARGES | Case tab → Charges tab or existing data |
| F | NEXT COURT EVENT | Events tab → next upcoming event description |
| G | NEXT COURT DATE | Events tab → date of next upcoming event |
| H | TRIAL DATE | Events tab → next Trial Date event |
| I | JAIL VISIT | Events tab → most recent jail visit date |
| J | JAIL VISIT NEEDED | Calculated: >30 days = RED "OVERDUE", else GREEN "OK" |

#### Update Rules

1. **Existing clients**: Match by CLIENT NAME (column D) and update all other columns
2. **New clients** (in Defender Data but not in tracker): Add new rows at the bottom
3. **Closed cases**: Gray out the entire row, set column F to "CLOSED", set column I to "N/A"
4. **Clients in tracker but not in Defender Data**: Flag in orange "NOT IN CURRENT CASELOAD - VERIFY STATUS"
5. **Overdue calculation**: If today's date minus last jail visit > 30 days, mark column J in RED font with "OVERDUE - X DAYS SINCE LAST VISIT"
6. **No visit on record**: Mark column I in RED with "NO VISIT ON RECORD" and column J with "OVERDUE - NO VISIT ON RECORD"
7. **Current visits** (<=30 days): Mark column J in GREEN with "OK - X days ago"

#### Formatting

- Header row: Arial 10pt, Bold
- Data rows: Arial 10pt
- RED font: `Font(name='Arial', size=10, color='FF0000', bold=True)` for overdue
- GREEN font: `Font(name='Arial', size=10, color='008000')` for current
- GRAY font + fill: `Font(color='808080')` + `PatternFill('solid', fgColor='D9D9D9')` for closed cases
- ORANGE font: `Font(color='FF8C00')` for verification-needed cases
- Date format: `MM/DD/YYYY`

### Phase 5: Summary Report

After updating the tracker, present a summary to the attorney:

```
TRACKER UPDATE COMPLETE — [DATE]
================================
Total active cases: X
Overdue jail visits (RED): X
  - [Client Name] — X days (last visit MM/DD/YYYY)
  - ...
Current jail visits (GREEN): X
Closed cases: X
New clients added: X
Clients needing verification: X
```

---

## Error Handling

- **Login timeout**: If no login after 60 seconds, remind the user
- **Page load failures**: Wait 3 seconds and retry; if still failing, take screenshot and report
- **Virtual scrolling issues**: Use Next/Prev buttons exclusively; never rely on DOM row positions
- **Missing Events tab data**: Record "NO VISIT ON RECORD" for jail visits with no entries
- **Excel file locked**: Check if file is open in another application; notify user

---

## File Locations

- **Tracker**: `CALCASIEU Contract Cases (Court & Jail Visit Tracker).xlsx` in mounted workspace
- **Defender Data**: `https://online.justiceworks.com/dd7/web/start/1199`



**Before writing:**

- Create the full subfolder chain with `Filesystem:create_directory` if it doesn't exist
- Confirm the path with the attorney if `{CASE_ROOT}` was resolved from the prompt (not from Case Brain)

**After writing, report the path:**

> ✅ Saved
> `{full absolute path}`
> Size: [size] | Type: [.docx / .pdf / .md / etc.]

List all files written, including intermediate exports (case tracker update log).
