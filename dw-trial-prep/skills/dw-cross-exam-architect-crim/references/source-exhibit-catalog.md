# Source Catalog (PDF)

**This step is MANDATORY. Every cross-examination outline must be accompanied by a Source Catalog.**

After completing the cross-examination outline, generate a standalone PDF catalog of every source document in the Source Register. This catalog serves as the attorney's quick-reference index to all materials cited in the cross.

## Catalog Structure

The PDF must contain:

1. **Cover Page** — Firm name, "SOURCE / EXHIBIT DOCUMENT CATALOG," witness name, case caption, summary statistics (total sources, Bates range, evidence items, civil filings)

2. **Table of Contents** — One row per source: source number, title, evidence item, Bates range, chapters referenced. **No date column** — where a document's date matters, it appears in that source's description or key-references list, which can carry the context a bare date column cannot. The canonical record of each document's date is the **Source Register** in the cross-examination outline.

3. **Source Detail Sheets** — One entry per source document containing:
   - Source number and title (dark header bar)
   - Metadata table: Evidence Item, Bates Range, Custodian, Case Reference, File Location, Cross-Exam Chapters Referenced. **No date column** — if the document's date matters to a chapter, it belongs in the description or the key-references list where it can carry context
   - Description paragraph
   - Bulleted list of every key reference cited in the cross-examination (with timestamps, Bates pages, or page numbers) — one bullet per reference, never a paragraph

4. **Missing Discovery Table** — Mirrors the Discovery Gap Report from Step 6 in tabular format (Missing Item | Significance | Action Required)

5. **Cross-Reference Matrix** — A grid showing which sources are cited in which chapters (sources on rows, chapters on columns, checkmarks for citations)

## Catalog Output

- **Format:** PDF (using reportlab or equivalent)
- **File name:** `Source Catalog — [Witness Name].pdf`
- **Typography:** Times New Roman 14 pt body text throughout, per `deliverable-formatting.md`
- **Location:** `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/` — the same folder as the cross-examination outline and the Combined Source Documents PDF. All three deliverables live together.
- **Footer:** ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL / PREPARED IN ANTICIPATION OF LITIGATION, plus case caption
