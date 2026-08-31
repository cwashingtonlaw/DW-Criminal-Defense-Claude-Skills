# Deliverable Formatting — Cross-Examination Package

Applies to **all three** deliverables produced by this skill. Read before generating any file.

---

## 1. Typography (firm-specified for this skill)

| Element | Spec |
|---|---|
| **Body text** | **Times New Roman, 14 pt** |
| Chapter titles / section headers | Times New Roman, 14 pt, **bold** |
| Table cell text (Source/Exhibit, Questions, Notes) | Times New Roman, 14 pt |
| Table headers | Times New Roman, 14 pt, bold |
| Work product header/footer marking | Times New Roman, 10 pt |
| Footnotes, if any | Times New Roman, 12 pt |
| Page numbers (bottom right) | Times New Roman, 12 pt |

**Why 14 pt:** these are read standing at counsel table, under bad courtroom lighting, while a witness is waiting. Legibility beats density.

**Divergence noted.** The firm style guide (`dw-shared-protocols-crim/references/dw-firm-style-guide.md`) specifies 12 pt body for **filed pleadings**. The three deliverables from this skill are **internal work product**, never filed and never served, so the 14 pt spec governs here and does not conflict with the filing standard. If any portion of a cross-exam outline is ever adapted into a filed pleading, reset it to the 12 pt filing spec.

---

## 2. Page Setup

- **Margins:** 1" all sides
- **Orientation:** landscape for the chapter table pages (the three-column Source/Exhibit | Questions | Notes layout needs the width); portrait acceptable for cover page and Source Register
- **Line spacing:** single-spaced within table cells; one blank line between question sequences
- **Page numbers:** **bottom right** of every page, Times New Roman 12 pt. Format `Page N of M` so a dropped page is obvious mid-cross
- **Chapter breaks:** each chapter starts on a new page — never split a chapter across a page break mid-sequence

---

## 3. Work Product Marking

Per `dw-shared-protocols-crim/references/attorney-work-product-marking.md`:

**Footer sharing.** Page numbers sit bottom **right**; the two-line work product marking sits bottom **center** in the same footer. They do not collide. Where a deliverable puts the marking in the header instead, the footer carries the page number alone.

- **Cross-Examination Outline (.docx)** — marking in the **header** of every page
- **Source Catalog (.pdf)** — marking in the **footer** of every page
- **Combined Source Documents (.pdf)** — marking in the **footer** of divider pages

Marking text, two lines, no terminal period:

```
ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL
PREPARED IN ANTICIPATION OF LITIGATION
```

Apply via .docx header/footer XML rather than body text so it survives copy/paste and does not disrupt the table layout.

---

## 4. Output Location — All Three Files

All three deliverables are written to the **same folder**:

```
{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/
```

Cross-examination materials live with the witness file, not with the general case analysis — they are reached for at counsel table, keyed to a witness.

`{{CASE_ROOT}}` is resolved by `dw-case-brain-crim` and varies by case source (Calcasieu PDO / NOLA Conflict / D&W private). Never hardcode it; never write outside `CASE_ROOT`. See `dw-shared-protocols-crim/references/output-path-formula.md`.

**File names:**

| # | Deliverable | File name |
|---|---|---|
| 1 | Cross-Examination Outline | `Cross-Examination — [Witness Name].docx` |
| 2 | Source Catalog | `Source Catalog — [Witness Name].pdf` |
| 3 | Combined Source Documents | `Combined Sources — [Witness Name].pdf` |

If a witness is crossed again after a superseding production, version with a ` - v2` suffix rather than overwriting. A prior outline may already have been annotated by hand.

---

## 5. Pre-Delivery Format Check

Before presenting to the attorney, confirm:

- [ ] Body text is Times New Roman 14 pt throughout all three files
- [ ] Page numbers present, bottom right of every page, `Page N of M` format
- [ ] Work product marking present, in the correct position per file type
- [ ] All three files in `03 - Witnesses/Prosecution Witnesses/`, same folder
- [ ] File names match the pattern exactly
- [ ] No chapter split across a page break mid-sequence
- [ ] Source Register appears on page 2 of the outline, before Chapter 1
- [ ] Every SOURCE/EXHIBIT cell carries its `(N)` prefix
- [ ] All three columns bulleted or numbered — no running prose in any cell
- [ ] Questions numbered sequentially within each chapter; one fact per question
- [ ] Source Register has no short-name column; documents cited by actual title
- [ ] Source Exhibit Catalog has no date column in the TOC or metadata tables
- [ ] Parish, trial court, and Louisiana appellate circuit stated; any federal citation written as `5th Cir.` and any state one as `La. [N] Cir.` — no bare "5th Circuit"
- [ ] Every flagged question carries a preservation bullet naming the ground and the proffer substance
- [ ] Preservation Log appended as the final section, with Chapter/Question # pre-filled for flagged questions
- [ ] Discovery Gap Report present
- [ ] On a Fast Path build: the Fast Path notice appears on the cover page under the caption
