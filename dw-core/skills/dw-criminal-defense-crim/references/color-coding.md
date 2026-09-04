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

Seven columns. This sheet is an admissibility worksheet — discovery-intake tracking lives in the Download Log and `Bate Stamp Master Log.xlsx`.

### Column Headers (Row 1)

| Column | Header Color | Hex | Text |
|--------|-------------|-----|------|
| Evidence Number | Navy | #003366 | White |
| Evidence Name | Indigo | #4B0082 | White |
| Number of Pages | Slate Gray | #708090 | White |
| Bate Stamp Range | Dark Cyan | #008B8B | White |
| Sponsoring Witness | Sea Green | #2E8B57 | White |
| Authentication Route | Steel Blue | #4682B4 | White |
| Anticipated Objections | Crimson | #DC143C | White |

### Authentication Route Dropdown Cell Colors

| Value | Fill Color | Hex | Text |
|-------|-----------|-----|------|
| Self-Authenticating | Green | #4CAF50 | White |
| Certified Public Record | Sea Green | #2E8B57 | White |
| Certified Business Record | Dark Cyan | #008B8B | White |
| Stipulated | Light Green | #90EE90 | Dark |
| Witness with Knowledge | Steel Blue | #4682B4 | White |
| Chain of Custody | Slate Gray | #708090 | White |
| Distinctive Characteristics | Cadet Blue | #5F9EA0 | White |
| Voice or Speaker ID | Medium Purple | #9370DB | White |
| Process or System | Dark Slate Blue | #483D8B | White |
| Contested — Motion Required | Red | #F44336 | White |
| TBD | Yellow | #FFD93D | Dark |

### Anticipated Objections Cell Colors

Free-text column using the shorthand legend in `phase1-step4-case-tables-population.md`. Apply by content:

| Content | Fill Color | Hex | Text |
|---------|-----------|-----|------|
| Contains `404(B)` or `CONFRONTATION` | Red | #F44336 | White |
| Contains `HEARSAY`, `AUTH`, or `BEST EVIDENCE` | Amber | #FFC000 | Dark |
| Any other objection code | Yellow | #FFD93D | Dark |
| `NONE ANTICIPATED` | Light Gray | #E0E0E0 | Dark |
| Blank | White | #FFFFFF | Dark |

### Sponsoring Witness Cell Colors

| Content | Fill Color | Hex | Text |
|---------|-----------|-----|------|
| `UNASSIGNED` | Yellow | #FFD93D | Dark |
| Any named witness | White | #FFFFFF | Dark |

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

## Witness List Sheet

Single consolidated sheet, four columns. Sorted alphabetically by Last, First; `Priority` is a sortable, color-coded column.

### Column Headers

All four headers use **white text on Navy (#003366)**.

Columns: Witness Name · Role in Case · Priority · Key Evidence Sources

### Priority Dropdown Cell Colors

| Value | Fill Color | Hex | Text |
|-------|-----------|-----|------|
| 1 – Critical | Red | #FF0000 | White (bold) |
| 2 – High | Amber | #FFC000 | Dark |
| 3 – Medium | Yellow | #FFD93D | Dark |
| 4 – Low | Light Green | #C6EFCE | Dark |
| 5 – Peripheral | Light Gray | #E0E0E0 | Dark |

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

*Daniels & Washington color coding standards. Last revised September 2026 (v6.0 — Defense Matrix section retired; Witness List reduced to four columns).*
