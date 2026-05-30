# Source/Exhibit Document Catalog (PDF)

**This step is MANDATORY. Every cross-examination outline must be accompanied by a Source/Exhibit Document Catalog.**

After completing the cross-examination outline, generate a standalone PDF catalog of every source document in the Source Register. This catalog serves as the attorney's quick-reference index to all materials cited in the cross.

## Catalog Structure

The PDF must contain:

1. **Cover Page** — Firm name, "SOURCE / EXHIBIT DOCUMENT CATALOG," witness name, case caption, summary statistics (total sources, Bates range, date range, evidence items, civil filings)

2. **Table of Contents** — One row per source: source number, title, evidence item, Bates range, chapters referenced

3. **Source Detail Sheets** — One entry per source document containing:
   - Source number and title (dark header bar)
   - Metadata table: Evidence Item, Bates Range, Date, Custodian, Case Reference, File Location, Cross-Exam Chapters Referenced
   - Description paragraph
   - Bulleted list of every key reference cited in the cross-examination (with timestamps, Bates pages, or page numbers)

4. **Missing Discovery Table** — Mirrors the Discovery Gap Report from Step 6 in tabular format (Missing Item | Significance | Action Required)

5. **Cross-Reference Matrix** — A grid showing which sources are cited in which chapters (sources on rows, chapters on columns, checkmarks for citations)

## Catalog Output

- **Format:** PDF (using reportlab or equivalent)
- **File name:** `Source Exhibit Catalog - [Witness Name] Cross.pdf`
- **Location:** Same folder as the cross-examination outline (typically `01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/`)
- **Header/footer:** ATTORNEY WORK PRODUCT — PRIVILEGED & CONFIDENTIAL + case caption
