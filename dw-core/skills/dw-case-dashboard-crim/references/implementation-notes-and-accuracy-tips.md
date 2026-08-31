# Implementation Notes & Tips for Accuracy

Read from the SKILL.md **Implementation Notes** section before scanning — scanning methodology, error handling, Excel parsing, LWOP applicability, and the five accuracy tips.

### Scanning Methodology

Use these methods to check for file presence:

1. **Direct File Check:** Use `os.path.exists()` or equivalent to check for specific named files
2. **Row Count Check:** For Excel sheets, parse `Case Tables.xlsx` and count populated rows (> minimum threshold)
3. **Folder Scan:** List directory contents and look for file name patterns (e.g., files starting with `0[1-9]` for phase 2 reports)
4. **Substring Match:** For report names that may vary slightly, search for report type keywords (e.g., "Timeline", "Red Flags", "Impeachment")

### Error Handling

- **Missing Case Tables.xlsx:** Flag immediately and stop. This is a critical blocker.
- **Folder structure incomplete:** List missing subfolders and flag as workflow gap.
- **Mixed phase deliverables:** Flag inconsistency. Example: "Phase 2 reports exist but Phase 1 Master Evidence Table missing — discovery may not be properly organized."

### Excel Parsing

When reading `Case Tables.xlsx`, check these sheets for population:
- `Evidence Table`: Count rows with data (excluding headers)
- `Timeline Sheet`: Count rows with data
- `Witness Sheet`: Count rows with data
- `Witness List - Alpha` & `Witness List - Priority`: Count rows with data
- `Defense Matrix`: Count charge rows

If a sheet does not exist, note it as missing.

### LWOP Assessment

The LWOP Worksheet is **only required** if charges include:
- Homicide (First Degree, Second Degree, Manslaughter)
- Sex Offenses (Rape, Aggravated Rape, Molestation)

If the case has other charges only, note LWOP as "Not Applicable" in Phase 0 status.

## Tips for Accuracy

1. **Ask for the case path first.** Never assume the location — paths vary widely across user systems.
2. **Check for file naming variations.** D&W uses the `[3-digit] - [Name]` convention, but some files may have slight variations (spaces, dashes, underscores). Search for keywords instead of exact matches.
3. **Populate the % complete for each phase.** This gives the user a sense of progress. Formula: `(completed items / total expected items) × 100`
4. **Always include time estimates** for recommended next steps. Attorneys care about how long the work will take.
5. **Flag high-priority items clearly.** RED FLAGS, MISSING DISCOVERY DEMANDS, and IMPEACHMENT WORKSHEETS are attorney decision points — call them out.
