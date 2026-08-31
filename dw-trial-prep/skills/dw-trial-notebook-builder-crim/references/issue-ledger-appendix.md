# Issue Ledger Appendix — Back Appendix (Step 5.5)

Read at Step 5.5 — source data, output location, document structure (header, full ledger table, audit trail), and the relationship to the Step 2.5 front-matter report, verbatim.

---

## Purpose

Generate a point-in-time snapshot of the Issue Code Ledger as a back-of-notebook appendix.
This document captures the ledger's state at the moment the trial notebook was assembled
and serves as the attorney's preserved record.

### 5.5A — Source Data

Read `Case Tables.xlsx` → `Issue Codes` sheet (same source as Step 2.5).

**If the sheet does not exist:** Generate a one-page placeholder noting the ledger was
not maintained, mirroring the Step 2.5 placeholder language. Continue without aborting.

### 5.5B — Output Location

`{CASE_ROOT}/01 - Trial Notebook/99-Issue-Code-Ledger-Appendix/[YYYY-MM-DD]_Issue-Ledger-Snapshot.docx`

The `99-` prefix ensures the appendix sorts to the bottom of the trial notebook tabs.

### 5.5C — Document Structure

Use the `docx` skill. Mark every page **Attorney Work Product — Privileged**.

**Header**

```
ISSUE CODE LEDGER — TRIAL APPENDIX
Daniels & Washington — Attorney Work Product — Privileged

Case:             State v. [Client Name]
Case Number:      [Number]
Snapshot Date:    [YYYY-MM-DD]
Total Codes:      [N]
Taxonomy Version: 2.0

This appendix is a point-in-time snapshot of the issue ledger as of the date above.
The live ledger is maintained in Case Tables.xlsx → Issue Codes sheet by
dw-issue-code-tracker-crim.
```

**Body — Full Ledger Table**

Reproduce every row from the `Issue Codes` sheet, sorted by Code ascending:

| Code | Category | Issue Name | Status | Last Updated | Notes | Linked Skill |
|------|----------|------------|--------|--------------|-------|--------------|
| U-01 | Universal | ... | Addressed | 2026-04-12 | ... | ... |
| ... | ... | ... | ... | ... | ... | ... |

**Audit Trail**

Read the `Issue Ledger Audit Trail` section from `Case-Brain.md` (Obsidian vault) and
append it to the appendix. This gives the trial notebook the full history of status
changes alongside the current snapshot.

If the Case Brain has no `Issue Ledger Audit Trail` section, note that fact in the
appendix and continue.

### 5.5D — Relationship to Step 2.5

The front-matter Gap Report (Step 2.5) is *analytical* — it filters to Open issues and
recommends action. This appendix is *archival* — every code, every status, full notes,
plus the audit trail. Both have a place in the trial notebook.
