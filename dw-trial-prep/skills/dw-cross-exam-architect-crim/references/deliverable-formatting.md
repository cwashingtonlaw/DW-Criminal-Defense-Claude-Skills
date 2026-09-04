# Deliverable Formatting — Cross-Examination Outline

This skill produces **one file**: `Cross-Examination — [Witness Name].docx`. Read before generating it.

---

## 1. Typography (firm-specified for this skill)

| Element | Spec |
|---|---|
| **Body text** | **Times New Roman, 12 pt** |
| Chapter titles | Times New Roman, 12 pt, **bold**, ALL CAPS |
| Section headers (CHAPTER GOALS, SOURCE REGISTER) | Times New Roman, 12 pt, **bold** |
| Table cell text (Source/Exhibit, Questions) | Times New Roman, 12 pt |
| Table headers | Times New Roman, 12 pt, bold, ALL CAPS |
| Work product header/footer marking | Times New Roman, 9 pt |
| Footnotes, if any | Times New Roman, 10 pt |
| Page numbers (bottom right) | Times New Roman, 10 pt |

**Hierarchy comes from weight and case, not from size.** Chapter titles are bold and capitalized rather than set larger, so a long chapter does not lose a line to an oversized heading. Only the work product marking, footnotes, and page numbers drop below 12 pt.

**Consistent with the firm standard.** The firm style guide (`dw-shared-protocols-crim/references/dw-firm-style-guide.md`) specifies 12 pt Times New Roman body for filed pleadings. This outline is **internal work product** — never filed, never served — but it uses the same 12 pt body spec, so any portion adapted into a filed pleading carries over without a reset.

### 1.1 Colour bands (firm-specified)

Three shaded bands, one colour per structural element. The colour means the same thing everywhere in the package.

| Band | Colour | Hex | Where it appears |
|---|---|---|---|
| **Source** | Blue | `D6E4F0` | Source Register header row; the SOURCE/EXHIBIT header cell in every chapter table |
| **Questions** | Red | `F4CCCC` | The QUESTIONS header cell in every chapter table |
| **Notes** | Yellow | `FFF2CC` | The NOTES — WITNESS RESPONSES label row at the foot of every chapter table |

**Rules**
- These are **light tints**, chosen so black 12 pt text stays legible on top and so the page survives a bad courtroom printer. Do not deepen them, and never set text in colour — body text is always black.
- Shade the **header/label rows only**. Never shade a cell that holds questions, sources, or the attorney's blank writing area.
- The blank NOTES writing row is **unshaded white**. It is written on.
- Apply shading with `ShadingType.CLEAR` and an explicit `fill`; `SOLID` renders black.
- **Printed in greyscale the three tints collapse to near-identical greys.** The label text (`SOURCE/EXHIBIT`, `QUESTIONS`, `NOTES — WITNESS RESPONSES`) carries the meaning on its own, so a black-and-white copy remains usable. Do not rely on colour alone to distinguish a band.

---

## 2. Page Setup

- **Margins:** 1" all sides
- **Orientation:** **landscape** for the chapter pages — the wider QUESTIONS column means fewer mid-question line wraps, and it gives the attorney a wider writing area in the notes box. Portrait for the cover page and Source Register
- **Column widths (chapter table, landscape, 12960 DXA usable):** SOURCE/EXHIBIT 4320, QUESTIONS 8640. Set `columnWidths` on the table **and** `width` on every cell, both in `WidthType.DXA` — percentage widths break in Google Docs
- **NOTES box:** the final two rows of the chapter table, each spanning both columns. Label row shaded yellow; blank row minimum height 1300 twips (about five lines at 12 pt) and set `cantSplit` so it never breaks across a page
- **Line spacing:** single-spaced within table cells; one blank line between question sequences
- **Page numbers:** **bottom right** of every page, Times New Roman 10 pt. Format `Page N of M` so a dropped page is obvious mid-cross
- **Question numbering:** restarts at 1 in each chapter. Use a separate numbering instance per chapter so the counter resets
- **Chapter breaks:** each chapter starts on a new page. **A chapter must fit one page including its notes box** — if it will not, it is two chapters. Set `cantSplit` on every table row so a row never breaks mid-sequence

---

## 3. Work Product Marking

Per `dw-shared-protocols-crim/references/attorney-work-product-marking.md`:

The two-line marking goes in the **header** of every page; the footer carries the page number alone, bottom right. They do not collide.

Marking text, two lines, no terminal period:

```
ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL
PREPARED IN ANTICIPATION OF LITIGATION
```

Apply via .docx header/footer XML rather than body text so it survives copy/paste and does not disrupt the table layout.

---

## 4. Output Location

The outline is written to:

```
{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/
```

Cross-examination material lives with the witness file, not with the general case analysis — it is reached for at counsel table, keyed to a witness.

`{{CASE_ROOT}}` is resolved by `dw-case-brain-crim` and varies by case source (Calcasieu PDO / NOLA Conflict / D&W private). Never hardcode it; never write outside `CASE_ROOT`. See `dw-shared-protocols-crim/references/output-path-formula.md`.

**File name:** `Cross-Examination — [Witness Name].docx`

**No Source Catalog and no Combined Sources PDF.** Do not generate them and do not reference them from the outline. The Source Register on page 2 is the outline's only index, and exhibits are pulled from the case file by the Reference/Bates entry the register gives — which is why that entry has to be precise.

If a witness is crossed again after a superseding production, version with a ` - v2` suffix rather than overwriting. A prior outline may already have been annotated by hand.

---

## 5. Pre-Delivery Format Check

Before presenting to the attorney, confirm:

**Type and colour**
- [ ] Body and table text is Times New Roman 12 pt throughout
- [ ] SOURCE/EXHIBIT header shaded blue `D6E4F0`; QUESTIONS header shaded red `F4CCCC`; NOTES label shaded yellow `FFF2CC`
- [ ] No body text set in colour; no shaded question, source, or writing cells
- [ ] Page numbers present, bottom right of every page, `Page N of M` format
- [ ] Work product marking present in the header of every page; page number alone in the footer

**Source Register**
- [ ] Appears on page 2 of the outline, before Chapter 1, header row blue
- [ ] Exactly three columns — Source Number | Evidence Item | Reference/Bates — no short-name column, no date column
- [ ] Where a date distinguishes one version of a document from another, it appears inside the Evidence Item entry
- [ ] Every `(N)` cited anywhere in the outline has a register row, and each row's Evidence Item title plus Reference/Bates entry is enough to pull that document from the case file with no catalog to consult

**Chapter pages**
- [ ] **Every chapter table has exactly two columns — SOURCE/EXHIBIT and QUESTIONS. No third column anywhere**
- [ ] **No expected answers, branch logic, impeachment bullets, evidentiary flags, preservation bullets, or strategy notes printed on any chapter page**
- [ ] Every SOURCE/EXHIBIT cell carries its `(N)` prefix, or `—` where the row rides on the exhibit already in hand
- [ ] Both columns bulleted or numbered — no running prose in either cell
- [ ] Question numbers restart at 1 in each chapter; one fact per question
- [ ] **Every chapter ends with the NOTES — WITNESS RESPONSES box, blank, roughly five lines, spanning both columns**
- [ ] Every chapter fits on one page including its notes box; any that does not has been split into two chapters

**Appendices and law**
- [ ] Preservation Log appended as the final section, with Chapter, Question #, **Ground to state** and **Proffer substance** pre-filled for every flagged question
- [ ] Discovery Gap Report present
- [ ] Exactly one file was produced — no Source Catalog, no Combined Sources PDF
- [ ] Parish, trial court, and Louisiana appellate circuit stated; any federal citation written as `5th Cir.` and any state one as `La. [N] Cir.` — no bare "5th Circuit"
- [ ] The Step 5 report to the attorney covers every branch, flag, and reserve question that is no longer printed on the chapter page
- [ ] On a Fast Path build: the Fast Path notice appears on the cover page under the caption
