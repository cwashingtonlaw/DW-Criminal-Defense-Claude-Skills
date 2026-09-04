# Contract 4: Case Tables.xlsx Sheet Schemas — Full Schema

Read from the SKILL.md **Contract 4: Case Tables.xlsx Sheet Schemas** section — the complete, authoritative schema (producers, consumers, filename pattern, required sections/fields, output location).

**Shared Resource:** `Case Tables.xlsx` at case root
**Writers:** `dw-criminal-defense-crim` (creates), Phase 2 and 3 skills (populate)
**Readers:** `dw-case-dashboard-crim`, `dw-trial-notebook-builder-crim`, `dw-cross-exam-architect-crim`

### Evidence Table Sheet

Admissibility worksheet, seven columns. Discovery-intake tracking (arrival date, production set, completeness) lives in the Download Log and `Bate Stamp Master Log.xlsx`, not here.

| Column | Type | Populated By | Required |
|--------|------|-------------|----------|
| Evidence Number | Text (3-digit) | Auto from filename | Yes |
| Evidence Name | Text | Auto from filename | Yes |
| Number of Pages | Number, or `A/V — HH:MM:SS` | Auto | Yes |
| Bate Stamp Range | Text (`DW-000123–000145`) | Auto from Bate Log | Yes |
| Sponsoring Witness | Text (`Last, First`) or `UNASSIGNED` | Cowork AI, attorney confirms | Yes |
| Authentication Route | Dropdown (11 values; see skill reference) | Cowork AI, attorney confirms | Yes |
| Anticipated Objections | Text (comma-separated codes) | Cowork AI, attorney confirms | Yes |

`Sponsoring Witness` is a foreign key into the Witness List `Witness Name` column — the two sheets join on it.

### Timeline Sheet

| Column | Type | Required |
|--------|------|----------|
| Start Date | Date | Yes |
| Start Time | Time | No |
| End Date | Date | No |
| End Time | Time | No |
| Title | Text | Yes |
| Subtitle | Text | No |
| Description | Text | Yes |
| Tags (Cowork Flags) | Text | No |
| Certainty | Dropdown (CONFIRMED / PROBABLE / DISPUTED / UNCONFIRMED / ALLEGED) | Yes |
| Bate Stamp | Text | Yes |
| Notes | Text | No |

### Witness List Sheet

| Column | Type | Populated By | Required |
|--------|------|-------------|----------|
| Witness Name | Text (`Last, First`) | Auto/Staff | Yes |
| Role in Case | Text | Auto/Staff | Yes |
| Priority | Dropdown (`1 – Critical` … `5 – Peripheral`) | Cowork AI, attorney confirms | Yes |
| Key Evidence Sources | Text (Bate refs / file names, comma-separated) | Auto | Yes |

Four columns only. Ranking rationale, impeachment material, addresses, and exam-prep tracking live in Report 8 and the per-witness worksheets — not on this sheet.

*Retired in v6.0:* the Defense Matrix, Legal Defenses (Rape), Legal Defenses (Homicide), Dealing with States Narrative, and Running List sheets. `Case Tables.xlsx` now carries three sheets: Evidence Table, Witness List, Timeline.
