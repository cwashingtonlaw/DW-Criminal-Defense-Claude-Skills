# Steps 6C–6D — Google Drive Detection & file:// Links (Detailed)

Read from SKILL.md **Steps 6C and 6D** — the three shared drives, the parish-based detection procedure, the host-path pattern, URL-encoding rules, the standard link table, and the verify-before-linking rule.

### 6C — Auto-Detect Google Drive Location

Case files are stored on Google Drive for Desktop across three shared drives. When creating a new Case Brain, auto-detect which drive holds the client folder — never ask the attorney to specify this.

**The three shared drives:**

| Drive Name | Host Path Pattern |
|---|---|
| NOLA Conflict Cases | `/Users/greatelephant82/Library/CloudStorage/GoogleDrive-cjw@danielswashington.com/Shared drives/NOLA Conflict Cases/` |
| CALCASIEU PDO Files | `/Users/greatelephant82/Library/CloudStorage/GoogleDrive-cjw@danielswashington.com/Shared drives/CALCASIEU PDO Files/` |
| D&W Law Firm (CJW) | `/Users/greatelephant82/Library/CloudStorage/GoogleDrive-cjw@danielswashington.com/Shared drives/D&W Law Firm (CJW)/` |

**Detection procedure:**
1. The Cowork workspace folder for the case is already mounted at `/sessions/.../mnt/[Case Folder Name]`. Check the case folder name — it usually indicates the client (e.g., `Tezeno, Titus - Murder`).
2. Determine which shared drive the case is on by checking the parish: Calcasieu Parish cases are on `CALCASIEU PDO Files`, New Orleans conflict cases on `NOLA Conflict Cases`, all others on `D&W Law Firm (CJW)`.
3. If the parish is ambiguous, check the `CASE-BRAIN-CONFIG.md` in the Obsidian vault for known case-to-drive mappings.
4. Record the drive name in `gdrive_root` and construct the full host path in `gdrive_path`.

The **host path** (used for `file://` links) follows this pattern:
```
/Users/greatelephant82/Library/CloudStorage/GoogleDrive-cjw@danielswashington.com/Shared drives/[Drive Name]/[Client Folder]
```

### 6D — Generate file:// Links for Case File Locations

The Case File Locations table appears in the Case Brain between "Charges & Exposure" and "Theory of Case." Each row links to a case folder or file using a `file://` URI that opens it directly on the attorney's Mac.

**URL encoding rules** — the host path must be URL-encoded for the `file://` URI:
- Spaces → `%20`
- Commas → `%2C`
- `@` → `%40`
- `&` → `%26`
- Parentheses → `%28` / `%29`

**Format:** `[Display Name](file:///URL-encoded-host-path)`

**Standard links to generate** (if the folders/files exist):

| Source | Expected Path |
|---|---|
| Client Folder | `[gdrive_path]` |
| Trial Notebook | `[gdrive_path]/01 - Trial Notebook` |
| Pretrial Notebook | `[gdrive_path]/02 - Pretrial Notebook` |
| Case Tables | `[gdrive_path]/Case Tables.xlsx` |
| Pleadings | `[gdrive_path]/02 - Pretrial Notebook/01 - Pleadings` |
| Discovery | `[gdrive_path]/02 - Pretrial Notebook/02 - Discovery` |
| Case Analysis | `[gdrive_path]/02 - Pretrial Notebook/03 - Case Analysis & Notes` |

Also scan the root folder for PDFs, motions (.docx), and other significant documents and link them individually (e.g., Arrest Report, PSA Report, Theory of Defense).

**Verify every link target exists** before adding it to the table. If a folder or file doesn't exist yet, omit it — don't link to things that aren't there.
