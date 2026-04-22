---
name: dw-case-brain
description: >
  Session persistence. ALWAYS invoke for "load the case," "open the matter," "pick up where
  we left off," "save the session," "wrap up," or any session start/end. Do NOT use for
  initial case intake — use dw-criminal-defense. Do NOT use for case status — use
  dw-case-dashboard.
---

# D&W Case Brain — Persistent Case Memory

**Version 3.3 | Internal Use Only**

This skill gives every case a living memory stored in the firm's Obsidian vault ("Dream Team Law"). It eliminates manual case re-briefing by reading case state at session open and writing updates at session close. Every session picks up exactly where the last one left off. The Obsidian vault provides the attorney with a searchable, linked reference — with YAML frontmatter for properties/search and clickable `file://` links that open case folders directly from Google Drive for Desktop.

---

## How It Works

```
SESSION OPEN  →  Read Case Brain from Obsidian vault  →  Load into context
  [work happens]
SESSION CLOSE →  Write session delta to Obsidian vault →  Brain updated for next session
                                                        →  file:// links to Google Drive
```

The Case Brain is a structured markdown document with YAML frontmatter (for Obsidian properties/search) and clickable `file://` links to case files on Google Drive for Desktop.

---

## STEP 1 — SESSION OPEN: Identify the Case

When a session begins without full case context in the conversation, immediately:

1. **Ask for the case identifier** (if not already stated):
   > *"Which case are we working on today? Client name or docket number works."*

2. **Detect the Obsidian vault** (see Step 6A for vault detection — try Obsidian MCP first, then mounted folder) and search for the Case Brain file at:
   ```
   DW-CASE BRAINS/Cases/[LastName]-[FirstName].md
   ```
   - **Via MCP:** Call `mcp__obsidian__view` with `path: "DW-CASE BRAINS/Cases"` to list all Case Brains, then match by client name.
   - **Via mounted folder:** List the contents of `[vault mount path]/DW-CASE BRAINS/Cases/` and match by client name or docket number from the YAML frontmatter.

3. **If found** → proceed to Step 2 (Load).
4. **If not found** → proceed to Step 3 (Create).

---

## STEP 2 — SESSION OPEN: Load Case Brain

Read the Case Brain file from the Obsidian vault:
- **Via MCP:** `mcp__obsidian__view` with `path: "DW-CASE BRAINS/Cases/[LastName]-[FirstName].md"`
- **Via mounted folder:** Use the `Read` tool with the absolute path

Then do the following:

- **Display a SESSION OPEN CONFIRMATION** to the attorney:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CASE LOADED: [Client Name] | [Docket #]
Attorney: [Lead Attorney]
Charges: [Charge summary]
Phase: [Current Phase]
Last Session: [Date] — [One-line summary]
Open Issues: [Count] flagged items pending
CASE_ROOT: [absolute path from YAML frontmatter]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type "full brief" to see complete case history.
```

- Hold the **full Case Brain content** in context for the session — do not summarize it away.
- Resume work from the `CURRENT STATUS` and `OPEN ISSUES` sections of the Brain.
- Activate the appropriate D&W skill for the work being requested (e.g., `dw-criminal-defense`, `dw-forensic-dump-analyzer`, etc.).

---

## STEP 3 — FIRST SESSION: Create a New Case Brain

If no Case Brain exists for this case, create one now.

**Gather the following** (from attorney or existing case documents):
- Client full name
- Docket / case number
- Parish and court division
- Lead attorney
- Charges (with La. R.S. citations if known)
- Date of offense / date of arrest
- Current court date
- Current case phase (0–3)
- Any immediate priorities

**Read the config file** at `DW-CASE BRAINS/CASE-BRAIN-CONFIG.md` (via MCP or mounted folder) for Google Drive shared drives, known case mappings, and URL encoding reference. This config file is the authoritative reference.

**Auto-detect the Google Drive location** (see Step 6C) to populate `file://` links.

**Create the Case Brain file** in the Obsidian vault:
- **Via MCP:** `mcp__obsidian__create` with `path: "DW-CASE BRAINS/Cases/[LastName]-[FirstName].md"` and `file_text` containing the full Case Brain content.
- **Via mounted folder:** Use the `Write` tool with the absolute path. Make sure the `DW-CASE BRAINS/Cases/` directory exists before writing (create it if needed).

The file must include:
1. Full YAML frontmatter (see Step 6B)
2. Populated Case Brain body (see `references/case-brain-template.md`)
3. Case File Locations table with `file://` links (see Step 6D)

Then display the SESSION OPEN CONFIRMATION (Step 2) and proceed.

---

## STEP 4 — SESSION CLOSE: Write Updates Back

When the attorney signals the session is ending (any of: "done for now," "wrap up," "end session," "save the session," "that's it for today"), do the following before closing:

### 4A — Generate Session Delta

Summarize what happened this session in 3–8 bullet points:
- Tasks completed (with output file names if applicable)
- New information discovered
- Issues opened or closed
- Decisions made
- Next steps identified

### 4B — Prompt for Attorney Additions

Ask:
> *"Anything to add before I save? Any decisions, concerns, or next steps I should note?"*

### 4C — Update the Case Brain

Read the current Case Brain file from the Obsidian vault first (never blindly overwrite), then update these sections:

| Section | What to Update |
|---|---|
| `CURRENT STATUS` | New phase / status if changed |
| `SESSION LOG` | Prepend new session entry (most recent first) |
| `OPEN ISSUES` | Add new issues; mark resolved issues with checkmark |
| `NEXT STEPS` | Replace with fresh list from this session |
| `KEY DECISIONS` | Append any decisions made this session |
| `LAST UPDATED` | Today's date |

**Write procedure:**
1. Read the current file first (via MCP `mcp__obsidian__view` or `Read` tool)
2. Preserve the YAML frontmatter — update fields that changed, don't remove any
3. Preserve the Case File Locations section — only add new links for new files, don't remove existing links
4. Update the body content sections listed above
5. Write the updated file back:
   - **Via MCP (targeted edits):** Use `mcp__obsidian__str_replace` for section-level updates. This is preferred for small changes because it avoids overwriting the entire file.
   - **Via MCP (full rewrite):** If many sections changed, read the full file, apply all edits in memory, then use `mcp__obsidian__create` to write the complete updated file. Note: `mcp__obsidian__create` will overwrite the existing file — this is acceptable ONLY after you've read the current version and merged changes.
   - **Via mounted folder:** Use the `Edit` or `Write` tool with the absolute path.

### 4D — Confirm Save

Display:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CASE BRAIN SAVED: [Client Name] | [Date]
Session logged. [N] open issues. Next: [top next step]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## STEP 5 — FULL BRIEF (On Demand)

If the attorney types "full brief" or "full case summary," display the complete Case Brain in formatted sections:

1. Case Overview
2. Charges & Exposure
3. Case File Locations (with clickable links)
4. Theory of Case / Defense Narrative
5. Phase Status & Quality Gates
6. Key Evidence (flagged items only)
7. Open Issues (all unresolved)
8. Key Decisions Log
9. Session History (last 5 sessions)
10. Companion Skill Outputs (links/references)
11. Next Steps

---

## STEP 6 — OBSIDIAN VAULT, GOOGLE DRIVE & MAINTENANCE

### 6A — Obsidian File Location & Vault Detection

The Obsidian vault ("Dream Team Law") is stored in iCloud Drive on the attorney's Mac at:
```
/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/
```
The `DW-CASE BRAINS` folder lives at the vault root. The access method depends on your environment:

#### Step 1 — Detect Your Environment

**Cowork (cloud):** If the current working directory starts with `/sessions/` or you see `/sessions/.../mnt/` paths, you are in Cowork. **Skip the Obsidian MCP entirely** — it connects to a local Obsidian app that doesn't exist in Cowork and will time out. Go directly to Method 2 (Mounted Folder).

**Claude Code (local):** If you're running on the attorney's Mac (paths like `/Users/greatelephant82/...`), try Method 1 (Obsidian MCP) first. If it fails, fall back to Method 2 using the local iCloud path.

#### Method 1 — Obsidian MCP Server (Claude Code only)

The Obsidian MCP server (`mcp__obsidian__*` tools) provides direct read/write access to the vault. This only works in Claude Code where the Obsidian app is running locally.

**How to detect the Obsidian MCP at runtime:**
1. Call `mcp__obsidian__view` with `path: "DW-CASE BRAINS/Cases"` to list existing Case Brains
2. If the call succeeds → the MCP is connected. **Use MCP tools for all subsequent read/write operations in this session.**
3. If the call fails with a connection/timeout error → fall through to Method 2.

**MCP tool mapping:**

| Operation | MCP Tool | Example |
|---|---|---|
| Read a Case Brain | `mcp__obsidian__view` | `path: "DW-CASE BRAINS/Cases/Tezeno-Titus.md"` |
| Create a new Case Brain | `mcp__obsidian__create` | `path: "DW-CASE BRAINS/Cases/Tezeno-Titus.md"`, `file_text: "..."` |
| Update specific text in a Case Brain | `mcp__obsidian__str_replace` | For targeted section edits (preferred for small changes) |
| Overwrite a Case Brain (after reading) | `mcp__obsidian__create` | Same path — will overwrite. Only after reading current version. |
| List all Case Brains | `mcp__obsidian__view` | `path: "DW-CASE BRAINS/Cases"` (lists directory) |
| Read config file | `mcp__obsidian__view` | `path: "DW-CASE BRAINS/CASE-BRAIN-CONFIG.md"` |
| Create notes in subfolders | `mcp__obsidian__create` | `path: "DW-CASE BRAINS/Witnesses/Prosecution/Smith-John.md"` |

**IMPORTANT:** All paths used with MCP tools are **relative to the vault root** — do NOT use absolute filesystem paths. Example: `DW-CASE BRAINS/Cases/Tezeno-Titus.md`, NOT `/Users/.../DW-CASE BRAINS/Cases/Tezeno-Titus.md`.

#### Method 2 — Mounted / Local Filesystem (Cowork primary, Claude Code fallback)

Access the vault's `.md` files directly using `Read`, `Edit`, and `Write` tools with absolute paths.

**In Cowork:** The attorney adds the `DW-CASE BRAINS` folder (not the entire vault) as a Cowork workspace directory. The folder on the attorney's Mac is:
```
/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS
```

How to find it as a mounted folder:
1. List the contents of the Cowork mount directory (e.g., `ls /sessions/.../mnt/`)
2. Look for a folder named `DW-CASE BRAINS` — it will contain `Cases/` as a subdirectory.
3. Use absolute paths: `/sessions/.../mnt/DW-CASE BRAINS/Cases/[LastName]-[FirstName].md`

**In Claude Code (fallback):** If the MCP is unavailable, access the vault directly at:
```
/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/Cases/[LastName]-[FirstName].md
```

#### Method 3 — Neither Available (LAST RESORT)

If neither the Obsidian MCP nor the filesystem vault path is accessible, use the Fallback procedure described in the Fallback section below. Do not silently skip vault access — the Case Brain lives in Obsidian and the skill cannot function properly without it.

**Regardless of access method, Case Brains always live at:**
```
DW-CASE BRAINS/Cases/[LastName]-[FirstName].md
```

The filename uses hyphens (no pipes, no commas, no special characters) because Obsidian has trouble with certain characters in filenames.

**Always read the config file** at `DW-CASE BRAINS/CASE-BRAIN-CONFIG.md` (via whichever method is active) for the full list of Google Drive shared drives, known case mappings, and URL encoding reference. This config file is the authoritative reference and should be consulted every time you create or update a Case Brain.

### 6B — YAML Frontmatter

Every Case Brain starts with YAML frontmatter that Obsidian renders as "Properties." Include all case metadata so the attorney can search, filter, and sort cases in Obsidian.

Required YAML fields:

```yaml
---
tags:
  - case-brain
  - active
  - [charge-type]    # weapons, homicide, sex-offense, drugs, etc.
  - [phase]          # phase-0, phase-1, phase-2, phase-3
status: active
phase: "0 — Intake"
client_name: "First Last"
docket: "C-XXXXXX"
court: "Court Name, Section X"
parish: "Parish Name"
lead_attorney: "Christopher Washington"
charges: "Charge 1, Charge 2"
date_of_offense: YYYY-MM-DD
date_of_arrest: YYYY-MM-DD
next_court_date: "VERIFY"
prosecutor: "VERIFY"
judge: "VERIFY"
lwop_risk: false
co_defendants: "Name1, Name2"
gdrive_root: "Drive Name"
gdrive_path: "/Users/greatelephant82/Library/CloudStorage/GoogleDrive-cjw@danielswashington.com/Shared drives/[Drive Name]/[Client Folder]"
CASE_ROOT: "/Users/greatelephant82/Library/CloudStorage/GoogleDrive-cjw@danielswashington.com/Shared drives/[Drive Name]/[Client Folder]"
---
```

The `gdrive_root` and `gdrive_path` fields record which Google Drive shared drive holds this case's files. This makes it possible to regenerate `file://` links without re-searching.

**`CASE_ROOT` is the canonical output-path variable** — every D&W skill that writes a file reads `CASE_ROOT` from this frontmatter to construct its output path (see `OUTPUT_PATH_CONVENTION.md` at the repo root). `CASE_ROOT` and `gdrive_path` always hold the same absolute path; `CASE_ROOT` exists as a named alias so skills can reference it unambiguously. When updating `gdrive_path`, always update `CASE_ROOT` to match.

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

### 6E — Tagging Active vs. Archived Cases

- Active cases: include `active` in the YAML `tags` list and set `status: active`
- Resolved/closed cases: replace `active` tag with `closed`, set `status: closed`, note disposition in the body

### 6F — Linking to Other Cowork Outputs

When a companion skill generates a major output (suppression motion, forensic audit, cross-exam outline), record the output filename and date in the Case Brain under `COMPANION SKILL OUTPUTS`. This creates a map of everything Cowork has produced for the case.

### 6G — DW-CASE BRAINS Folder Structure

The Obsidian vault mirrors the attorney's Trial Notebook structure. When a companion skill generates witness profiles, legal theories, opening/closing drafts, or other trial prep materials, save them as individual notes in the appropriate folder. Each note should have YAML frontmatter with a `cases` field linking back to the relevant Case Brain(s).

**When saving notes via MCP**, use `mcp__obsidian__create` with paths relative to vault root:
```
mcp__obsidian__create with path: "DW-CASE BRAINS/Witnesses/Prosecution/[WitnessName].md"
```

```
DW-CASE BRAINS/
├── Cases/                  # Case Brain summary files (one per case)
├── Jury-Selection/         # Juror profiles, voir dire questions, strike tracking
├── Opening-Statements/     # Opening statement drafts and outlines
├── Witnesses/              # All witness profiles
│   ├── Prosecution/        # State/prosecution witnesses
│   ├── Defense/            # Defense witnesses
│   └── Expert/             # Expert witnesses (state or defense)
├── Closing-Arguments/      # Closing argument outlines, seeds, exhibit lists
├── Evidence/               # Evidence inventory, authentication, exhibit lists
├── Pleadings/              # Filed motions, oppositions, replies
├── Pretrial-Orders/        # Court orders, legal memos, jury instructions
├── Verdict-Sentencing/     # Verdict forms, sentencing memos, post-trial motions
├── Case-Analysis/          # Phase 2 analysis reports
├── Legal-Theories/         # Legal theory research notes
├── Templates/              # Note templates for each folder type
└── Dashboards/             # Obsidian Bases dashboards (.base files)
```

**Where to save new notes:**

| Content | Folder | Example |
|---|---|---|
| Prosecution witness profile | `Witnesses/Prosecution/` | `LeBlanc, P-O Preston.md` |
| Defense witness profile | `Witnesses/Defense/` | `Character Witness.md` |
| Expert witness evaluation | `Witnesses/Expert/` | `Downs, Amber.md` |
| Opening statement draft | `Opening-Statements/` | `Nicholas-Opening-v1.md` |
| Closing argument outline | `Closing-Arguments/` | `Nicholas-Closing-Seeds.md` |
| Jury selection materials | `Jury-Selection/` | `Nicholas-Voir-Dire-Questions.md` |
| Case analysis report | `Case-Analysis/` | `Nicholas-Report-3-Constitutional.md` |
| Legal theory research | `Legal-Theories/` | `Art. 893 First Offender.md` |
| Evidence note | `Evidence/` | `Nicholas-Exhibit-List.md` |
| Filed motion | `Pleadings/` | `Nicholas-Motion-to-Suppress.md` |
| Court order | `Pretrial-Orders/` | `Nicholas-Discovery-Order.md` |
| Sentencing material | `Verdict-Sentencing/` | `Nicholas-Sentencing-Memo.md` |

The Case Brain's **Trial Preparation** section displays a summary view of all these folders' contents for the case, with links back to the individual notes.

### 6H — CASE_ROOT: Canonical Output-Path Variable

Every D&W skill that writes a file depends on the `CASE_ROOT` variable to construct its output path. The Case Brain is the single source of truth for this value.

**Where `CASE_ROOT` lives:**

| Location | Purpose |
|---|---|
| YAML frontmatter (`CASE_ROOT:` field) | Authoritative value read by all file-writing skills |
| YAML frontmatter (`gdrive_path:` field) | Same value, used for `file://` link generation (legacy alias) |
| SESSION OPEN CONFIRMATION | Displayed at session start so the attorney can see and verify the path |

**`CASE_ROOT` always equals `gdrive_path`.** They are two labels for the same absolute path. The duplication exists because `gdrive_path` has historical meaning for the `file://` link generator in Step 6D, and `CASE_ROOT` is the name every output-writing skill looks for (per `OUTPUT_PATH_CONVENTION.md`).

**When creating a new Case Brain:**
- Set both `gdrive_path` and `CASE_ROOT` to the same absolute path
- Never leave `CASE_ROOT` blank — if you're uncertain of the path, ask the attorney before creating the Case Brain

**When updating an existing Case Brain:**
- If a case moves drives (e.g., conflict case reassigned), update BOTH fields together
- Never let them drift — a mismatch will cause output files to scatter between the old and new locations

**How other skills read it:**
1. Skill loads the active Case Brain (via `dw-case-brain`)
2. Skill reads `CASE_ROOT` from the YAML frontmatter
3. Skill constructs its output path: `{CASE_ROOT}/Deliverables/{Phase}/{SkillName}/{YYYY-MM-DD}_{filename}.{ext}`
4. Skill creates the subfolder chain and writes the file

**If `CASE_ROOT` is missing from the frontmatter** (older Case Brains created before v3.3): read `gdrive_path` and use that value, then backfill `CASE_ROOT` on the next session-close write.

---

## Fallback (If Vault Not Accessible)

If no access method works (MCP unavailable in Claude Code, vault not mounted in Cowork, filesystem path not found):
1. Notify the attorney: *"I can't reach your Obsidian vault. Want to connect the Obsidian MCP (in Claude Code) or add the 'DW-CASE BRAINS' folder as a workspace directory (in Cowork)?"*
2. If the attorney connects MCP or mounts the folder, detect it and proceed.
3. If the attorney declines or can't connect:
   - On session open: ask the attorney to paste in the last Case Brain content manually.
   - On session close: generate the updated Case Brain as a downloadable `.md` file for the attorney to place in their vault manually.

---

## Guardrails

- **Never overwrite a Case Brain without reading the current version first.** Always pull → merge → write. Never replace.
- **Never delete session log entries.** Session history is append-only.
- **Never mark an open issue resolved** unless the attorney explicitly confirms it is closed.
- **Never summarize away context** from the full brief — the Case Brain is the full record.
- **This skill fires before other skills** when no case context is present. Do not skip it.
- **Always read `CASE-BRAIN-CONFIG.md`** from the Obsidian vault before creating or updating a Case Brain — it contains the authoritative Google Drive mappings and encoding reference.
- **Detect the environment first** (Cowork vs Claude Code) and use the appropriate access method. In Cowork, skip the MCP — go straight to the mounted folder. In Claude Code, try MCP first, then fall back to the local filesystem.

---

## Integration with D&W Skill Ecosystem

After loading the Case Brain, hand off to the appropriate skill based on what the attorney needs:

| Task | Skill | Saves To Folder |
|---|---|---|
| Case intake / discovery processing | `dw-criminal-defense` | `Cases/` |
| Phone dump analysis | `dw-forensic-dump-analyzer` | `Case-Analysis/` |
| Suppression motion | `dw-suppression-motion` | `Pleadings/` |
| Cross-examination prep | `dw-cross-exam-architect` | `Witnesses/` (appropriate subfolder) |
| Brady/Giglio audit | `dw-brady-giglio-auditor` | `Case-Analysis/` |
| Search warrant challenge | `dw-suppression-motion` | `Pleadings/` |
| Cell site / CSLI | `dw-cell-site-geolocation-auditor` | `Case-Analysis/` |
| 404(b) opposition | `dw-404b-opposition` | `Pleadings/` |
| CI / informant audit | `dw-brady-giglio-auditor` | `Case-Analysis/` |
| LWOP worksheet | `dw-lwop-populator` | `Cases/` |
| Jury selection / voir dire | `dw-voir-dire-assistant` | `Jury-Selection/` |
| Expert witness evaluation | `dw-expert-witness-evaluator` | `Witnesses/Expert/` |
| Jury instructions | `dw-jury-instructions-builder` | `Pretrial-Orders/` |
| Sentencing mitigation | `dw-sentencing-mitigation-specialist` | `Verdict-Sentencing/` |
| Plea analysis | `dw-plea-negotiation-analyzer` | `Case-Analysis/` |

The Case Brain provides the context; the companion skill does the work.

---

## Changelog

### v3.3 (April 2026)
- Added `CASE_ROOT` as canonical output-path variable in YAML frontmatter (Step 6B)
- Added Step 6H documenting `CASE_ROOT` as the single source of truth for all file-writing D&W skills
- `CASE_ROOT` now displayed in SESSION OPEN CONFIRMATION so the attorney can verify the output path at session start
- `CASE_ROOT` and `gdrive_path` hold identical values; `CASE_ROOT` is the name 38 downstream skills look for per `OUTPUT_PATH_CONVENTION.md`
- Older Case Brains without `CASE_ROOT` fall back to `gdrive_path` and are backfilled on next session close

### v3.2 (March 2026)
- **FIX:** Obsidian MCP times out in Cowork because there's no local Obsidian app running in the cloud
- Added environment detection (Cowork vs Claude Code) to Step 6A — Cowork now skips MCP entirely and goes straight to mounted filesystem
- MCP is now Claude Code-only; Cowork uses Read/Write/Edit tools on mounted vault
- Updated guardrail from "always try MCP first" to "detect environment first"
- Removed DevonThink as a storage option — Obsidian is the sole case brain repository

### v3.1 (March 2026)
- Added Obsidian MCP server as primary vault access method (Steps 1–4, 6A)
- Corrected vault storage location: iCloud Drive (not Google Drive)
- Added MCP tool mapping table with concrete examples
- Added iCloud vault path for mounted-folder fallback
- Simplified Google Drive detection in Step 6C (parish-based routing, no MCP needed)
- Updated Fallback to trigger only when BOTH MCP and mounted folder are unavailable

### v3.0 (February 2026)
- Initial skill version with mounted-folder-only vault access

---

*Read `references/case-brain-template.md` for the full Case Brain document structure and all field definitions.*
