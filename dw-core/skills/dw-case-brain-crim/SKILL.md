---
name: dw-case-brain-crim
category: core
description: >
  Session persistence. ALWAYS invoke for "load the case," "open the matter," "pick up where
  we left off," "save the session," "wrap up," or any session start/end. Do NOT use for
  initial case intake — use dw-criminal-defense-crim. Do NOT use for case status — use
  dw-case-dashboard-crim.
---

# D&W Case Brain — Persistent Case Memory

**Version 3.4 | Internal Use Only**

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

Read the **entire** Case Brain file from the Obsidian vault (do not read sections piecemeal):
- **Via MCP:** `obsidian_get_file_contents` with `filepath: "DW-CASE BRAINS/Cases/[LastName]-[FirstName].md"`
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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type "full brief" to see complete case history.
```

- **IMPORTANT:** Hold the **entire Case Brain content in memory** for the session — do not summarize it away. You will need the full document when merging changes at session close.
- Resume work from the `CURRENT STATUS` and `OPEN ISSUES` sections of the Brain.
- Activate the appropriate D&W skill for the work being requested (e.g., `dw-criminal-defense-crim`, `dw-forensic-dump-analyzer-crim`, etc.).

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

Run **4A → 4H** in order: **4A** Generate Session Delta (3–8 bullets) → **4B** Prompt for Attorney Additions → **4C** Read the current Case Brain in full (same method as session open) → **4D** Merge all changes in-memory (section-by-section update table; a merge, never a replacement) → **4E** Write the full document back (full-document replacement, never heading-based patching) → **4F** Verify by reading the file back → **4G** Fallback Protocol if the write fails (save the merged document to `[case-root]/02 - Pretrial Notebook/03 - Case Analysis & Notes/CASE BRAIN — [Client Name] | [Docket].md` and notify the attorney) → **4H** Display the CASE BRAIN SAVED banner.

Read `references/step-4-session-close-protocol.md` now for the merge table, tool-specific read/write/verify commands, fallback wording, and the confirmation banner.

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
11. Clock Status (statutory deadline clocks — written by dw-deadline-engine-crim)
12. Next Steps

---

## STEP 6 — OBSIDIAN VAULT, GOOGLE DRIVE & MAINTENANCE

### 6A — Obsidian File Location & Vault Detection

The vault ("Dream Team Law") is in iCloud Drive at `/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/`; regardless of access method, Case Brains always live at `DW-CASE BRAINS/Cases/[LastName]-[FirstName].md` (hyphens only). **Detect the environment first:** Cowork (`/sessions/...` paths) → skip the MCP entirely and use the mounted `DW-CASE BRAINS` folder (Method 2); Claude Code (`/Users/greatelephant82/...`) → try the Obsidian MCP (Method 1, `mcp__obsidian__view` on `DW-CASE BRAINS/Cases`), fall back to the local iCloud path; neither → Method 3 / Fallback section. **Always read `DW-CASE BRAINS/CASE-BRAIN-CONFIG.md`** before creating or updating a Case Brain.

Read `references/step-6a-vault-access-methods.md` now for the detection procedure, the MCP tool-mapping table, mounted-folder discovery, and path rules.

### 6B — YAML Frontmatter

Every Case Brain starts with YAML frontmatter that Obsidian renders as "Properties" (tags, status, phase, client_name, docket, court, parish, lead_attorney, charges, date_of_offense, date_of_arrest, next_court_date, prosecutor, judge, lwop_risk, co_defendants, gdrive_root, gdrive_path). Read the **Step 6B** section of `references/case-brain-template.md` now for the required field block.

### 6C — Auto-Detect Google Drive Location

Case files live on three Google Drive shared drives (NOLA Conflict Cases, CALCASIEU PDO Files, D&W Law Firm (CJW)). Detect the drive by parish — never ask the attorney — and record `gdrive_root` and the full host path in `gdrive_path`. Read `references/step-6c-6d-drive-detection-and-file-links.md` now for the drive table, detection procedure, and host-path pattern.

### 6D — Generate file:// Links for Case File Locations

Build the Case File Locations table (between "Charges & Exposure" and "Theory of Case") with URL-encoded `file://` links to the client folder, both notebooks, Case Tables, Pleadings, Discovery, Case Analysis, and significant root documents. **Verify every link target exists** before adding it. Encoding rules and the standard link table are in the same 6C–6D reference.


### 6E — Tagging Active vs. Archived Cases

- Active cases: include `active` in the YAML `tags` list and set `status: active`
- Resolved/closed cases: replace `active` tag with `closed`, set `status: closed`, note disposition in the body

### 6F — Linking to Other Cowork Outputs

When a companion skill generates a major output (suppression motion, forensic audit, cross-exam outline), record the output filename and date in the Case Brain under `COMPANION SKILL OUTPUTS`. This creates a map of everything Cowork has produced for the case.

The `## CLOCK STATUS` block is a recognized Case Brain section: `dw-deadline-engine-crim` writes and refreshes it (via this skill's read-merge-write protocol). Persist and reload it like any other section, but never edit its contents by hand — clock rows change only through a dw-deadline-engine-crim recomputation.

### 6G — DW-CASE BRAINS Folder Structure

The vault mirrors the attorney's Trial Notebook structure; companion-skill outputs (witness profiles, theories, opening/closing drafts) save as individual notes in the matching folder, each with a `cases` YAML field linking back to the Case Brain. Read `references/step-6g-vault-folder-structure.md` now for the folder tree and the where-to-save table.

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

- **Never patch individual sections by heading name.** The Obsidian API's heading-based targeting is unreliable and prone to failure. Instead, always read the full document, merge all changes in Claude's context, and write the complete document back in a single operation. This prevents data loss from heading-targeting failures.
- **Never overwrite a Case Brain without reading the current version first.** Always read → merge in-memory → write full document. Never blindly replace.
- **Never delete session log entries.** Session history is append-only.
- **Never mark an open issue resolved** unless the attorney explicitly confirms it is closed.
- **Never summarize away context** from the full brief — the Case Brain is the full record. Load the entire document at session open and keep it in memory for the eventual merge.
- **This skill fires before other skills** when no case context is present. Do not skip it.
- **Always read `CASE-BRAIN-CONFIG.md`** from the Obsidian vault before creating or updating a Case Brain — it contains the authoritative Google Drive mappings and encoding reference.
- **Detect the environment first** (Cowork vs Claude Code) and use the appropriate access method. In Cowork, skip the MCP — go straight to the mounted folder. In Claude Code, try MCP first, then fall back to the local filesystem.
- **Use the fallback protocol** if any write operation fails — save the updated Case Brain to Google Drive and notify the attorney. Never lose session data due to an API failure.

---

## Integration with D&W Skill Ecosystem

After loading the Case Brain, hand off to the appropriate companion skill — the Case Brain provides the context; the companion skill does the work. Read `references/skill-ecosystem-handoff-table.md` for the task → skill → vault-folder table.

---

## Changelog

Version history (v3.0 – v3.4) lives in `CHANGELOG.md` at the skill root.

---

## Quick References

Reference materials in the `references/` subdirectory:

- **case-brain-template.md** — Step 3 (create) and Step 4 (merge): full Case Brain document structure, all field definitions, and the Step 6B YAML frontmatter block
- **step-4-session-close-protocol.md** — Step 4: 4A–4H session-close procedure, merge table, write/verify commands, fallback protocol
- **step-6a-vault-access-methods.md** — Step 6A (and Steps 1–2): environment detection, Obsidian MCP tool mapping, mounted-folder access, path rules
- **step-6c-6d-drive-detection-and-file-links.md** — Steps 6C–6D: shared-drive table, parish-based detection, URL-encoding rules, standard file:// link table
- **step-6g-vault-folder-structure.md** — Step 6G: DW-CASE BRAINS folder tree and where-to-save table for companion-skill notes
- **skill-ecosystem-handoff-table.md** — Integration section: task → companion skill → vault folder hand-off table

---

*Read `references/case-brain-template.md` for the full Case Brain document structure and all field definitions.*
