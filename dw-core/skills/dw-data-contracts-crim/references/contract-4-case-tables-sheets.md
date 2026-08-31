# Contract 4: Case Tables.xlsx Sheet Schemas — Full Schema

Read from the SKILL.md **Contract 4: Case Tables.xlsx Sheet Schemas** section — the complete, authoritative schema (producers, consumers, filename pattern, required sections/fields, output location).

**Shared Resource:** `Case Tables.xlsx` at case root
**Writers:** `dw-criminal-defense-crim` (creates), Phase 2 and 3 skills (populate)
**Readers:** `dw-case-dashboard-crim`, `dw-trial-notebook-builder-crim`, `dw-cross-exam-architect-crim`

### Evidence Table Sheet

| Column | Type | Populated By | Required |
|--------|------|-------------|----------|
| Doc # | Text (3-digit) | Auto from filename | Yes |
| Evidence Type | Text | Auto from file type | Yes |
| Name | Text | Auto from filename | Yes |
| Description | Text | Staff | Yes |
| Bate Stamp | Text | Auto from Bate Log | Yes |
| Reviewed (Y/N) | Dropdown | Staff/Attorney | Yes |
| Notes | Text | Staff/Attorney | No |
| Discovery Set | Text | Auto from Download Log | Yes |
| Date of Delivery | Date | Auto from Download Log | Yes |
| Review Priority | HIGH/MED/LOW | Cowork AI | Yes |
| Defense Relevance | FAVORABLE/NEUTRAL/FLAG | Cowork AI | Yes |

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

### Witness Sheet

| Column | Type | Required |
|--------|------|----------|
| Name | Text | Yes |
| Witness Type | Text (Prosecution/Defense/Expert) | Yes |
| Association | Text | Yes |
| Sources (Bate stamps) | Text | Yes |
| Trial Exam Prepared (Y/N) | Dropdown | Yes |

### Defense Matrix Sheet

| Column | Type | Required |
|--------|------|----------|
| Charge | Text (includes La. R.S. citation) | Yes |
| Elements | Text | Yes |
| Responsive Verdicts | Text | Yes |
| Defense(s) | Text | Yes |
| Evidence Supporting Defense | Text | Yes |
| Notes | Text | No |
