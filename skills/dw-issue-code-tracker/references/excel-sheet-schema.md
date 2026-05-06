# Case Tables.xlsx — Issue Codes Sheet Schema

**Version:** 2.0 (renumbered, no gaps)

Sheet name: **`Issue Codes`**

## Columns

| Col | Header | Type | Notes |
|-----|--------|------|-------|
| A | Code | Text | e.g., `U-01`, `H-04`, `R-09` |
| B | Category | Text | `Universal` / `Homicide` / `Rape-Sexual Assault` |
| C | Issue Name | Text | Full name from taxonomy (e.g., "Eyewitness Identification") |
| D | Status | Dropdown | `Open` / `Addressed` / `N/A` (data validation) |
| E | Last Updated | Date | YYYY-MM-DD; auto-set on status change |
| F | Notes | Text | Free-form attorney notes |
| G | Linked Skill | Text | From skill-routing-map.md (reference only — no auto-routing) |

## Conditional Formatting

- **Status = Open** → light yellow fill
- **Status = Addressed** → light green fill
- **Status = N/A** → light gray fill, italic text

## Header Row Style

- Row 1: bold, white text on dark navy fill
- Freeze top row so columns stay visible during scrolling

## Data Validation

- Column D (Status): dropdown limited to `Open` / `Addressed` / `N/A`
- Column A (Code): regex `^[UHR]-\d{2}$` (e.g., U-01, H-08, R-11)
- Column A valid ranges: U-01 through U-14, H-01 through H-08, R-01 through R-11

## Sort Order on Initialize

Sort ascending by Code (A → Z), so Universal codes appear first (U-01 to U-14), then Homicide (H-01 to H-08), then Rape (R-01 to R-11).

---

## Pre-Populated Rows on INITIALIZE

The skill writes one row per applicable code based on case type:
- **Other Felony:** 14 rows (Universal only)
- **Homicide:** 22 rows (Universal + Homicide)
- **Rape/Sexual Assault:** 25 rows (Universal + Rape)
- **Multiple (e.g., homicide + sex offense):** up to 33 rows (all categories)

All rows initialize with:
- `Status` = `Open`
- `Last Updated` = today (YYYY-MM-DD)
- `Notes` = blank
- `Linked Skill` = pre-populated from skill-routing-map.md
