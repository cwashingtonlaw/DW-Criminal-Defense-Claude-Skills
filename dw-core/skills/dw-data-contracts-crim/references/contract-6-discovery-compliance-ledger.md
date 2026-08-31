# Contract 6: Discovery Compliance Ledger — Full Schema

Read from the SKILL.md **Contract 6: Discovery Compliance Ledger** section — the complete, authoritative schema (producers, consumers, filename pattern, required sections/fields, output location).

**Producer:** `dw-discovery-compliance-monitor-crim`
**Consumers:** `dw-brady-giglio-auditor-crim`, `dw-criminal-defense-crim` (Phase 2 Report 7), `dw-case-dashboard-crim`

### Required Columns

| Column | Type | Required |
|--------|------|----------|
| Item | Text | Yes |
| Category | Text (Document/Physical/Digital/Witness) | Yes |
| Discovery Bucket | Dropdown (1-7: Law Enforcement / Physical-Forensic / Digital-Electronic / Witness / Expert / Prosecution File / Brady-Giglio) | Yes |
| Demanded Date | Date | Yes |
| Demanded In | Text (motion/letter reference) | Yes |
| Produced Date | Date or "OUTSTANDING" | Yes |
| Production Set | Text | If produced |
| Bate Range | Text | If produced |
| Notes | Text | No |
| Brady Flag | Yes/No | Yes |

### Output Location
`01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/`
