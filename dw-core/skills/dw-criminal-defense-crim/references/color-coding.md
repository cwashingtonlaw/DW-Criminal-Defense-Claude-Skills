# Daniels & Washington — Spreadsheet Color Coding Reference

This reference defines the firm's standard color coding scheme for all sheets in `Case Tables.xlsx`. Use it whenever creating, updating, or formatting any case spreadsheet to ensure visual consistency across all cases. SKILL.md points here from Phase 1 Step 4 (Evidence Table population) and Phase 3 Step 1 (Timeline Sheet color coding).

---

## Core Rules

- **Never modify data** when applying color coding — this skill only affects formatting.
- **Preserve existing formatting** unless it conflicts with the standards below.
- **Use the `xlsx` skill** to apply all formatting programmatically.
- All header rows use **white text on colored background** unless otherwise noted.
- All dropdown/conditional color coding applies to **data cells**, not headers.
- When a sheet already has firm color coding applied, verify it matches these standards and correct any deviations.

---

## Evidence Table Sheet

### Column Headers (Row 1)

| Column | Header Color | Hex | Text |
|--------|-------------|-----|------|
| Doc # | Navy | #003366 | White |
| Evidence Type | Dark Slate Blue | #483D8B | White |
| Name | Indigo | #4B0082 | White |
| Description | Teal | #008080 | White |
| Bate Stamp | Dark Cyan | #008B8B | White |
| Reviewed (Y/N) | Sea Green | #2E8B57 | White |
| Notes | Olive | #808000 | White |
| Discovery Set | Steel Blue | #4682B4 | White |
| Date of Delivery | Slate Gray | #708090 | White |
| Review Priority ★ | Dark Orange | #FF8C00 | White |
| Defense Relevance ★ | Crimson | #DC143C | White |

### Evidence Type Dropdown Cell Colors

When a cell value matches one of these types, apply the corresponding fill:

| Evidence Type | Fill Color | Hex | Text |
|--------------|-----------|-----|------|
| Police Report | Navy | #003366 | White |
| Incident Report | Dark Slate Blue | #483D8B | White |
| Supplemental Report | Steel Blue | #4682B4 | White |
| Witness Statement | Indigo | #4B0082 | White |
| Interview / Interrogation | Purple | #800080 | White |
| Lab Report | Dark Cyan | #008B8B | White |
| Forensic Report | Teal | #008080 | White |
| Forensic Extraction | Dark Green | #006400 | White |
| Autopsy / Medical Examiner | Maroon | #800000 | White |
| Medical Record | Crimson | #DC143C | White |
| SANE Report | Dark Red | #8B0000 | White |
| Photograph | Olive | #808000 | White |
| Audio Recording | Dark Orange | #FF8C00 | White |
| Video / Body Camera | Orange Red | #FF4500 | White |
| Transcript | Goldenrod | #DAA520 | Dark |
| Surveillance Footage | Sienna | #A0522D | White |
| 911 Call / Dispatch | Tomato | #FF6347 | White |
| Prior Bad Acts | Red | #FF0000 | White |
| Chain of Custody | Slate Gray | #708090 | White |
| Court Document | Cadet Blue | #5F9EA0 | White |
| Plea Agreement | Sea Green | #2E8B57 | White |
| Booking / Arrest Record | Dim Gray | #696969 | White |
| Administrative | Light Gray | #D3D3D3 | Dark |
| Correspondence | Medium Purple | #9370DB | White |
| UNSURE | Yellow | #FFD93D | Dark |

### Review Priority Dropdown Cell Colors

| Value | Fill Color | Hex | Text |
|-------|-----------|-----|------|
| HIGH | Red | #FF6B6B | Dark |
| MED | Yellow | #FFD93D | Dark |
| LOW | Light Green | #90EE90 | Dark |

### Defense Relevance Dropdown Cell Colors

| Value | Fill Color | Hex | Text |
|-------|-----------|-----|------|
| FAVORABLE | Green | #4CAF50 | White |
| FLAG | Red | #F44336 | White |
| NEUTRAL | Light Gray | #E0E0E0 | Dark |

### Reviewed (Y/N) Dropdown Cell Colors

| Value | Fill Color | Hex | Text |
|-------|-----------|-----|------|
| Y | Green | #4CAF50 | White |
| N | Light Gray | #E0E0E0 | Dark |

---

## Bate Stamp Master Log Sheet

### Column Headers

| Column | Header Color | Hex | Text |
|--------|-------------|-----|------|
| Production Set | Navy | #003366 | White |
| Date Received | Steel Blue | #4682B4 | White |
| Start Number | Teal | #008080 | White |
| End Number | Dark Cyan | #008B8B | White |
| Staff Member | Slate Gray | #708090 | White |
| Date Stamped | Cadet Blue | #5F9EA0 | White |

---

## Timeline Sheet

### Column Headers

| Column | Header Color | Hex | Text |
|--------|-------------|-----|------|
| Start Date | Navy | #003366 | White |
| Start Time | Dark Slate Blue | #483D8B | White |
| End Date | Indigo | #4B0082 | White |
| End Time | Purple | #800080 | White |
| Title | Teal | #008080 | White |
| Subtitle | Dark Cyan | #008B8B | White |
| Description | Sea Green | #2E8B57 | White |
| Tags (Cowork Flags) | Dark Orange | #FF8C00 | White |
| Certainty | Dark Green | #006400 | White |
| Bate Stamp | Steel Blue | #4682B4 | White |
| Notes | Slate Gray | #708090 | White |

### Row Color Coding (Event Type)

| Event Type | Row Fill | Description |
|-----------|---------|-------------|
| Prosecution events | Light Red | Events that support the State's case |
| Defense-favorable | Light Green | Events that support the defense |
| Neutral | White | All other events |

### Certainty Dropdown Cell Colors

| Value | Fill Color | Hex | Text |
|-------|-----------|-----|------|
| CONFIRMED | Dark Green | #006400 | White |
| PROBABLE | Sea Green | #2E8B57 | White |
| DISPUTED | Red | #F44336 | White |
| UNCONFIRMED | Yellow | #FFD93D | Dark |
| ALLEGED | Dark Orange | #FF8C00 | White |

### Tags (Cowork Flags) Dropdown Cell Colors

| Tag | Fill Color | Hex | Text |
|-----|-----------|-----|------|
| CONFLICT | Red | #F44336 | White |
| FAVORABLE | Green | #4CAF50 | White |
| IMPEACHMENT | Orange | #FF9800 | White |
| GAP | Yellow | #FFD93D | Dark |
| KEY EVENT | Navy | #003366 | White |

---

## Witness List Sheets (Alpha & Priority)

### Column Headers

| Column | Header Color | Hex | Text |
|--------|-------------|-----|------|
| Name | Navy | #003366 | White |
| Witness Type | Dark Slate Blue | #483D8B | White |
| Association | Teal | #008080 | White |
| Sources (Bate stamps) | Steel Blue | #4682B4 | White |
| Trial Exam Prepared (Y/N) | Sea Green | #2E8B57 | White |

### Witness Type Dropdown Cell Colors

| Witness Type | Fill Color | Hex | Text |
|-------------|-----------|-----|------|
| Law Enforcement | Navy | #003366 | White |
| Expert | Purple | #800080 | White |
| Eyewitness | Dark Orange | #FF8C00 | White |
| Character | Teal | #008080 | White |
| Civilian | Steel Blue | #4682B4 | White |
| Victim | Crimson | #DC143C | White |

### Trial Exam Prepared (Y/N) Dropdown Cell Colors

| Value | Fill Color | Hex | Text |
|-------|-----------|-----|------|
| Y | Green | #4CAF50 | White |
| N | Light Gray | #E0E0E0 | Dark |

---

## Defense Matrix Sheet

### Column Headers

| Column | Header Color | Hex | Text |
|--------|-------------|-----|------|
| Charge/Defense | Navy | #003366 | White |
| Responsive Verdicts | Crimson | #DC143C | White |
| Applicable Defenses | Dark Green | #006400 | White |

---

## How to Use This Reference

**When building or updating any `Case Tables.xlsx` sheet:**

1. Read this file to get the correct color specs.
2. Use the `xlsx` skill to apply formatting.
3. Apply header colors first (Row 1 of each sheet).
4. Apply conditional/dropdown cell colors to data rows.
5. Verify all colors match the standards above.

**When creating a new sheet not listed here:**
- Use Navy (#003366) for the first column header.
- Alternate through the firm's standard header palette: Dark Slate Blue, Indigo, Teal, Dark Cyan, Sea Green, Steel Blue, Slate Gray, Purple, Dark Orange, Crimson.
- Always use white text on dark backgrounds, dark text on light backgrounds.

---

*Daniels & Washington color coding standards. Last revised March 2026.*
