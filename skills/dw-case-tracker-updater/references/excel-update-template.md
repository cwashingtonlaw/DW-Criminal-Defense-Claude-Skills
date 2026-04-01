# Excel Update Script Template

Use this Python template to update the tracker after collecting all case data from Defender Data.
Replace the `cases` list with actual collected data from the current session.

```python
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill
from datetime import date

filepath = '<PATH_TO_TRACKER_XLSX>'
wb = load_workbook(filepath)
ws = wb.active

today = date.today()  # Or use specific date if needed

# Styles
std_font = Font(name='Arial', size=10)
red_font = Font(name='Arial', size=10, color='FF0000', bold=True)
green_font = Font(name='Arial', size=10, color='008000')
gray_font = Font(name='Arial', size=10, color='808080')
orange_font = Font(name='Arial', size=10, color='FF8C00')
gray_fill = PatternFill('solid', fgColor='D9D9D9')

# Collected case data — populate from browser automation
# Each case is a dict with keys:
#   name, docket, section, ada, charges, next_court_event,
#   next_court_date (date or None), trial_date (date or None),
#   jail_visit (date or None), status ("Open" or "Closed"),
#   new (bool, True if not already in tracker)
cases = [
    # Example:
    # {
    #     "name": "JOHN DOE",
    #     "docket": "12345-24",
    #     "section": "E",
    #     "ada": "Smith, Jane",
    #     "charges": "Second Degree Murder",
    #     "next_court_event": "Pre Trial",
    #     "next_court_date": date(2026, 5, 1),
    #     "trial_date": date(2026, 7, 15),
    #     "jail_visit": date(2026, 3, 10),
    #     "status": "Open",
    #     "new": False
    # },
]

def find_row_for_client(ws, client_name, max_row):
    """Find row by client name with fuzzy matching."""
    cn = client_name.upper().strip()
    for row in range(2, max_row + 1):
        cell_val = ws.cell(row=row, column=4).value
        if cell_val:
            cv = cell_val.upper().strip()
            if cv == cn or cn.replace(" ", "") == cv.replace(" ", ""):
                return row
            # Match by first and last name
            parts_cn = cn.split()
            parts_cv = cv.split()
            if len(parts_cn) >= 2 and len(parts_cv) >= 2:
                if parts_cn[0] == parts_cv[0] and parts_cn[-1] == parts_cv[-1]:
                    return row
            # Match "LAST, FIRST" format
            if "," in cn and "," in cv:
                if cn.split(",")[0].strip() == cv.split(",")[0].strip():
                    return row
    return None

# Find the last row with data
last_data_row = 1
for row in range(2, ws.max_row + 1):
    if ws.cell(row=row, column=4).value:
        last_data_row = row
next_empty_row = last_data_row + 1

used_rows = set()

for case in cases:
    row = find_row_for_client(ws, case["name"], last_data_row)
    is_new = case.get("new", False)

    if row is None and not is_new:
        print(f"WARNING: Could not find row for {case['name']}")
        continue

    if is_new:
        row = next_empty_row
        next_empty_row += 1
        ws.cell(row=row, column=4, value=case["name"]).font = std_font

    used_rows.add(row)
    is_closed = case["status"] == "Closed"
    font = gray_font if is_closed else std_font

    # Update columns A-H
    ws.cell(row=row, column=1, value=case["docket"]).font = font
    ws.cell(row=row, column=2, value=case["section"]).font = font
    ws.cell(row=row, column=3, value=case["ada"]).font = font
    if is_closed:
        ws.cell(row=row, column=4).font = gray_font
    if case["charges"]:
        ws.cell(row=row, column=5, value=case["charges"]).font = font
    ws.cell(row=row, column=6, value="CLOSED" if is_closed else case["next_court_event"]).font = font
    ws.cell(row=row, column=7, value=case["next_court_date"]).font = font
    if case["next_court_date"]:
        ws.cell(row=row, column=7).number_format = 'MM/DD/YYYY'
    ws.cell(row=row, column=8, value=case["trial_date"]).font = font
    if case["trial_date"]:
        ws.cell(row=row, column=8).number_format = 'MM/DD/YYYY'

    # Column I: Jail Visit
    if is_closed:
        ws.cell(row=row, column=9, value="N/A").font = gray_font
    elif case["jail_visit"]:
        ws.cell(row=row, column=9, value=case["jail_visit"]).font = std_font
        ws.cell(row=row, column=9).number_format = 'MM/DD/YYYY'
    else:
        ws.cell(row=row, column=9, value="NO VISIT ON RECORD").font = red_font

    # Column J: Jail Visit Needed
    if is_closed:
        ws.cell(row=row, column=10, value="CLOSED").font = gray_font
        for col in range(1, 11):
            ws.cell(row=row, column=col).fill = gray_fill
    elif case["jail_visit"] is None:
        ws.cell(row=row, column=10, value="OVERDUE - NO VISIT ON RECORD").font = red_font
    elif (today - case["jail_visit"]).days > 30:
        days = (today - case["jail_visit"]).days
        ws.cell(row=row, column=10, value=f"OVERDUE - {days} DAYS SINCE LAST VISIT").font = red_font
    else:
        days = (today - case["jail_visit"]).days
        ws.cell(row=row, column=10, value=f"OK - {days} days ago").font = green_font

# Flag clients in tracker but not found in Defender Data
for row in range(2, last_data_row + 1):
    if row not in used_rows and ws.cell(row=row, column=4).value:
        ws.cell(row=row, column=10, value="NOT IN CURRENT CASELOAD - VERIFY STATUS").font = orange_font

# Set column widths
from openpyxl.utils import get_column_letter
widths = {1: 14, 2: 10, 3: 22, 4: 32, 5: 40, 6: 20, 7: 18, 8: 14, 9: 14, 10: 38}
for col, w in widths.items():
    ws.column_dimensions[get_column_letter(col)].width = w

wb.save(filepath)
print("Tracker updated successfully!")
```
