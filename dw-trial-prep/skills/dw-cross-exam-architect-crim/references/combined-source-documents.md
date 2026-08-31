# Combined Source Documents (PDF)

**This step is MANDATORY. Every cross-examination outline must be accompanied by a Combined Source Documents PDF.**

After completing the catalog, merge all source document PDFs into a single combined file with professional divider pages.

## Combined PDF Structure

1. **Cover Page** — Firm name, "SOURCE DOCUMENTS," witness name, case caption, table of contents listing all sources with Bates ranges

2. **For each source in Source Register order:**
   - **Divider Page** — Dark banner with source number and title, metadata (evidence item, Bates range, date, file name, page count, cross-exam chapters referenced), and a note indicating the document follows
   - **Actual Source Document** — All pages of the original PDF appended immediately after the divider

## Combined PDF Output

- **Format:** PDF (using pypdf to merge + reportlab for divider pages)
- **File name:** `Combined Sources — [Witness Name].pdf`
- **Typography:** divider page text in Times New Roman 14 pt, per `deliverable-formatting.md` (original source documents are appended as-is and retain their own formatting)
- **Location:** `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/` — the same folder as the outline and the catalog
- **Footer on divider pages:** ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL / PREPARED IN ANTICIPATION OF LITIGATION

## Handling Non-PDF Sources

- If a source is an audio/video recording with a transcript PDF placeholder, include the placeholder PDF
- If a source has no PDF in the case file (e.g., a document referenced but not yet produced), include only the divider page with a note: `[DOCUMENT NOT IN FILE — flagged in Discovery Gap Report]`
- If a source is a civil filing stored outside the evidence folder, locate it in the case root or Pretrial Notebook
