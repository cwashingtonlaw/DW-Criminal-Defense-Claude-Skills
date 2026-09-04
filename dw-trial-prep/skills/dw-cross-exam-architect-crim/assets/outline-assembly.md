# ASSET — Outline Assembly Order

Every Cross-Examination Outline .docx is assembled in this order. Items 1, 2, 4, and 5 are mandatory on every build, Fast Path included.

1. **Cover page** — case caption, witness name, witness type, build date, attorney. On a Fast Path build, the notice from `fast-path-notice.md` goes here, directly under the caption.
2. **Source Register** — page 2, before Chapter 1. Three columns: **Source Number | Evidence Item | Reference/Bates**, header row shaded blue `D6E4F0`. No short-name column, no date column.
3. **Chapters** — one per page, in the Step 4 sequence. Goals block per `chapter-goals-and-scoring.md`, then the **two-column SOURCE/EXHIBIT (blue) | QUESTIONS (red)** table, closing with the **NOTES — WITNESS RESPONSES** band (yellow) and a blank ~5-line row. No third column, and nothing but sources and questions in the table. A chapter that will not fit one page with its notes box is two chapters.
4. **Discovery Gap Report** (Step 6).
5. **Preservation Log** (Step 5.5) — final section, per `preservation-log.md`, with Chapter, Question #, Ground to state and Proffer substance pre-filled.

**Formatting:** Times New Roman 12 pt body and table text · 1" margins · landscape for chapter pages, portrait for cover and register · page numbers bottom right (`Page N of M`) · question numbers restart at 1 in each chapter · each chapter starts on a new page and fits on one page including its notes box.

**Filenames** (data-contract binding):

| # | Deliverable | Filename |
|---|---|---|
| 1 | Cross-Examination Outline | `Cross-Examination — [Witness Name].docx` |
| 2 | Source Catalog | `Source Catalog — [Witness Name].pdf` |
| 3 | Combined Sources | `Combined Sources — [Witness Name].pdf` |

All three to `{{CASE_ROOT}}/01 - Trial Notebook/03 - Witnesses/Prosecution Witnesses/`. Version with ` - v2` rather than overwriting — a prior outline may already carry handwritten annotations.
