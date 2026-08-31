# Master Trial Index Structure (Step 4)

Read at Step 4 — index file name and location, cover section, per-tab table format, front matter and appendix links, and the file:// link construction / URL-encoding rules, verbatim.

---

### Index Document Structure

**File name:** `MASTER TRIAL INDEX — [Client Last Name] [Date].docx`
**Save to:** Case root (same level as `Case Tables.xlsx`)

**Cover Section:**
```
MASTER TRIAL INDEX
State v. [Client Name]
Docket: [Number] | [Court] | [Parish]
Charges: [Summary]
Trial Date: [Date or "NOT SET"]
Lead Attorney: [Name]
Defense Theme: [One-line theme from Case Brain]
Generated: [Date] | Readiness: [READY / NEAR-READY / etc.]
```

**For each Trial Notebook tab, create a section with:**

1. **Tab header** with the tab number and name
2. **Table of deliverables** within that tab:

| # | Document | Type | Date | Status | Link |
|---|----------|------|------|--------|------|
| 1 | Cross-Examination — Officer LeBlanc | .docx | 2026-03-15 | Complete | [Open](file://...) |
| 2 | Source Catalog — Officer LeBlanc | .pdf | 2026-03-15 | Complete | [Open](file://...) |

3. **Gap callouts** for any missing items in that tab (red text or bold flag)

**Before any tab section, include a Front Matter section:**
- **00 — Trial Readiness Gap Report (Issue Ledger)** — link to
  `00-Trial-Readiness-Gap-Report.docx` from Step 2.5. Label it "READ FIRST."

**After all tabs, include:**
- **Pretrial Notebook Cross-References** — links to key pretrial items that inform trial
  (arraignment filings, discovery motions, pretrial orders)
- **Case Tables Link** — direct `file://` link to `Case Tables.xlsx`
- **Case Brain Link** — if the Case Brain is in the Obsidian vault, link to it
- **99 — Issue Code Ledger Appendix** — link to the snapshot `.docx` produced in
  Step 5.5. Label it "Reference / Record."

### Constructing file:// Links

Use the `gdrive_path` from the Case Brain to construct host-path `file://` links. Apply
the same URL encoding rules as `dw-case-brain-crim`:
- Spaces → `%20`
- Commas → `%2C`
- `@` → `%40`
- `&` → `%26`
- Parentheses → `%28` / `%29`

**In Cowork:** The mounted path (e.g., `/sessions/.../mnt/[Case Folder]`) is the working
path, but `file://` links in the index must use the **host path** from `gdrive_path` so they
work on the attorney's Mac. If `gdrive_path` is not available, use the mounted path and warn
that links will only work within Cowork.

**Verify every link target exists** before adding it to the index. If a file has been moved
or deleted since the scan, flag it rather than linking to a dead path.
