# Issue Ledger Gap Report — Front Matter (Step 2.5)

Read at Step 2.5 — source data, output location, full document structure (header, sections 1–5, attorney sign-off), stale logic, and routing discipline for the issue-code-driven Gap Report, verbatim.

---

## Purpose

A second, complementary gap analysis driven by the Issue Code Ledger maintained by
`dw-issue-code-tracker-crim` (taxonomy v2.0). Where Step 2 asks "what *deliverables* are
missing," this step asks "what *legal issues* are still flagged Open." Both reports go
in the trial notebook. This one becomes the first analytical document the attorney reads.

### 2.5A — Source Data

Read `Case Tables.xlsx` → `Issue Codes` sheet (created by `dw-issue-code-tracker-crim` v2.0).

**If the sheet does not exist:** Generate a one-page placeholder reading:

> ⚠️ Issue ledger was not maintained for this case. Trial readiness cannot be assessed
> against the issue code taxonomy. Recommend running `dw-issue-code-tracker-crim` retroactively
> to identify any unaddressed issues before trial.

Save the placeholder and continue with the rest of the workflow — do not abort.

### 2.5B — Output Location

Save the Gap Report to the front of the trial notebook:

`{CASE_ROOT}/01 - Trial Notebook/00-Trial-Readiness-Gap-Report.docx`

The `00-` prefix ensures it sorts to the top alphabetically and signals "read this first."

### 2.5C — Document Structure

Use the `docx` skill. Mark every page **Attorney Work Product — Privileged**.

**Header**

```
TRIAL READINESS GAP REPORT
Daniels & Washington — Attorney Work Product — Privileged

Case:           State v. [Client Name]
Case Number:    [Number]
Trial Date:     [Date]
Report Date:    [YYYY-MM-DD]
Days to Trial:  [N]
```

**Section 1 — Executive Summary**

Status counts by category in a single table:

| Category | Total Codes | Addressed | Open | N/A |
|----------|-------------|-----------|------|-----|
| Universal | 14 | [N] | [N] | [N] |
| Homicide | 8 (if applicable) | [N] | [N] | [N] |
| Rape/Sexual Assault | 11 (if applicable) | [N] | [N] | [N] |
| **TOTAL** | **[N]** | **[N]** | **[N]** | **[N]** |

**Readiness Score:** Addressed / (Addressed + Open) = **[X]%**

**Section 2 — ⚠️ Critical Gaps (Open Issues)**

For each Open code, grouped by category in this order — Universal, then Homicide
(if applicable), then Rape/Sexual Assault (if applicable):

#### [U-XX] [Issue Name]

- **Status:** Open since [Last Updated] ([X] days)
- **Linked Skill:** [Linked Skill from skill-routing-map.md, if available]
- **Notes:** [Notes from Excel sheet, if any]
- **Recommended Action:**
  - If notes are blank → "No work product on file. Recommend running [Linked Skill]
    or marking N/A if not applicable."
  - If notes describe partial work → "Review whether the existing work product is
    sufficient for trial. If yes, mark Addressed."
  - If stale (>30 days since Last Updated) → "⚠️ STALE — Open more than 30 days.
    Review whether this is still an active issue."

Apply the same per-code structure for Homicide (H-XX) and Rape/Sexual Assault (R-XX) codes.

**Section 3 — Addressed Issues Summary**

Informational list confirming the ledger is current and showing the attorney's preserved
record:

- [Code] [Issue Name] — [Notes from Excel sheet]
- ...

**Section 4 — N/A Issues**

Codes determined Not Applicable to this case:

- [Code] [Issue Name] — [Notes from Excel sheet]
- ...

**Section 5 — Attorney Sign-Off**

```
Before trial, attorney should review this report and confirm:

[ ] All Open issues have been reviewed
[ ] Stale issues have been triaged (still Open, now Addressed, or now N/A)
[ ] Where Open issues will not be addressed, the strategic reason is documented
    in the Notes column of the Issue Codes sheet
[ ] Issue ledger is current as of [Trial Date − 7 days]

Signature: _________________________  Date: _____________
```

### 2.5D — Stale Logic

A code is **STALE** if its `Last Updated` date is more than 30 days before today AND its
status is still `Open`. Apply the ⚠️ STALE flag in Section 2 for any such code. This
mirrors the same threshold used in `dw-case-dashboard-crim`.

### 2.5E — Routing Discipline

The Gap Report lists `Linked Skill` as a *recommendation only*. Do **NOT** auto-invoke any
specialist skill from this report. The attorney decides which gaps to close and when —
consistent with the design choice of `dw-issue-code-tracker-crim`.
