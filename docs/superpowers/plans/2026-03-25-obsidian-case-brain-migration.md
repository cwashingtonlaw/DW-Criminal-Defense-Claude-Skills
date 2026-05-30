# Obsidian Case Brain Migration — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate the D&W case brain system from DEVONthink to pure Obsidian with MCP integration, statute fetching from Westlaw, and Claude-driven document search.

**Architecture:** Obsidian vault at `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/` becomes the sole case brain store. The `dw-case-brain-crim` skill is rewritten to use Obsidian MCP (`obsidian-claude-code-mcp` plugin) instead of DEVONthink MCP. A statute fetcher workflow uses Claude in Chrome to pull statutes from legis.la.gov (primary) and Westlaw (secondary). Claude-driven document search replaces DEVONthink's AI search by reading PDFs from Google Drive via filesystem.

**Tech Stack:** Obsidian, obsidian-claude-code-mcp plugin, Obsidian Local REST API, Claude in Chrome MCP, Claude Code filesystem tools, Markdown/YAML

**Spec:** `docs/superpowers/specs/2026-03-25-obsidian-case-brain-migration-design.md`

**Rollback:** See spec Section 7 "Rollback Plan." All phases are additive — DEVONthink data is never modified or deleted. At any point, reverting to DEVONthink means re-enabling the original `dw-case-brain-crim` skill.

---

## Key Paths (Documentation Only — Use Full Paths in All Commands)

| Alias | Full Path |
|---|---|
| VAULT | `/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law` |
| CB | `/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS` |
| SKILLS | `/Users/greatelephant82/.claude/skills` |

---

## Chunk 1: Phase 1 — Vault Structure Updates

> **Note:** The Obsidian vault is NOT a git repo. There are no commits for vault changes. After completing this chunk, verify all changes in Obsidian before proceeding to Chunk 2.

### Task 1: Clean Up Vault Artifacts

**Files:**
- Delete: `CB/{Cases,Witnesses,...}` (brace-expansion artifact folder)
- Delete: `CB/Experts/` (redundant with `CB/Witnesses/Expert/`)

- [ ] **Step 1: Delete brace-expansion artifact folder**

```bash
rm -rf "/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/{Cases,Witnesses,Experts,Legal-Theories,Motions,Templates,Dashboards,.obsidian}"
```

Verify: `ls` the CB directory, confirm the `{Cases,...}` folder is gone.

- [ ] **Step 2: Delete redundant top-level Experts/ folder**

```bash
rm -rf "/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/Experts"
```

Verify: `ls` the CB directory, confirm `Experts/` is gone. Verify `Witnesses/Expert/` still has Downs, Amber.md and Quaal, Monica.md.

---

### Task 2: Create New Folders

**Files:**
- Create: `CB/Statutes/`
- Create: `CB/Witnesses/Persons-of-Interest/`

- [ ] **Step 1: Create Statutes folder**

```bash
mkdir "/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/Statutes"
```

- [ ] **Step 2: Create Persons-of-Interest subfolder**

```bash
mkdir "/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/Witnesses/Persons-of-Interest"
```

- [ ] **Step 3: Verify folder structure**

```bash
ls -la "/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/"
ls -la "/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/Witnesses/"
```

Expected: `Statutes/` visible at top level. `Witnesses/` has four subdirs: Defense, Expert, Prosecution, Persons-of-Interest.

---

### Task 3: Move Statute from Legal-Theories to Statutes

**Files:**
- Move: `CB/Legal-Theories/La. R.S. 14-30.md` → `CB/Statutes/La. R.S. 14-30 - First Degree Murder.md`
- Modify: `CB/Cases/Hadnot-Antonio.md` (update wikilinks)
- Modify: `CB/Cases/Nicholas-Jarrell.md` (check for references)

- [ ] **Step 1: Read current statute file to preserve content**

Read `CB/Legal-Theories/La. R.S. 14-30.md` — note the full content.

- [ ] **Step 2: Create renamed file in Statutes/**

Write the same content to `CB/Statutes/La. R.S. 14-30 - First Degree Murder.md`, updating the YAML frontmatter to add `fetch_date` and `source` fields:

```yaml
---
tags:
  - statute
  - homicide
type: Statute
statute: "La. R.S. 14:30"
title: "First Degree Murder"
source: "Manual entry"
fetch_date: 2026-03-20
---
```

Keep the body content identical.

- [ ] **Step 3: Delete old file**

```bash
rm "/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/Legal-Theories/La. R.S. 14-30.md"
```

- [ ] **Step 4: Check case brains for wikilinks to old filename**

Search both case brain files for `[[La. R.S. 14-30]]` or `[[La. R.S. 14:30]]`. Update any wikilinks to:
`[[La. R.S. 14-30 - First Degree Murder|La. R.S. 14-30]]`

- [ ] **Step 5: Verify**

Confirm `CB/Legal-Theories/` no longer contains `La. R.S. 14-30.md`. Confirm `CB/Statutes/La. R.S. 14-30 - First Degree Murder.md` exists with correct content.

---

### Task 4: Create Statute Template

**Files:**
- Create: `CB/Templates/Statute-Template.md`

- [ ] **Step 1: Write Statute Template**

```markdown
---
tags:
  - statute
type: Statute
statute: ""
title: ""
effective_date: ""
source: ""
fetch_date: ""
---

# {{statute}} — {{title}}

## Full Text

*(As enacted — paste or fetch from legis.la.gov)*

## Elements / Requirements

-

## Penalty

-

## Responsive Verdicts

-

## Key Case Law

-

## Annotations / Practice Notes

-

## Related Statutes

- [[]]

## Source

- **Primary:** legis.la.gov
- **Enhanced:** Westlaw (if annotations fetched)
- **Fetch Date:** {{fetch_date}}

## Cases

- [[]]
```

- [ ] **Step 2: Verify template exists alongside other templates**

```bash
ls "/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/Templates/"
```

Expected: Statute-Template.md listed alongside Case-Brain-Template.md, Expert-Template.md, Legal-Theory-Template.md, Motion-Template.md, Witness-Template.md.

---

### Task 5: YAML Schema Reconciliation & Template Update

**Files:**
- Modify: `CB/Templates/Case-Brain-Template.md`
- Modify: `CB/CASE-BRAIN-CONFIG.md`
- Modify: `CB/Cases/Hadnot-Antonio.md` (add missing YAML fields)
- Modify: `CB/Cases/Nicholas-Jarrell.md` (add missing YAML fields)

- [ ] **Step 1: Add missing YAML fields to Case Brain Template**

Update the frontmatter in `CB/Templates/Case-Brain-Template.md` to:

```yaml
---
tags:
  - case-brain
  - active
status: active
phase: "0 — Intake"
client_name: ""
docket: ""
court: ""
parish: ""
lead_attorney: ""
staff: ""
charges: ""
victims: ""
date_of_offense: ""
date_of_arrest: ""
next_court_date: ""
prosecutor: ""
judge: ""
lwop_risk: false
gdrive_root: ""
gdrive_path: ""
---
```

- [ ] **Step 2: Update Key Evidence Flags section in template**

Replace the Flag Type cell content. Old: `Brady / Suppression / Impeachment / Defense`. New: `Defense (exculpatory) / Defense (third-party suspect) / Defense (identity) / Prosecution (inculpatory) / Brady (potential) / Impeachment`

- [ ] **Step 3: Update CASE-BRAIN-CONFIG.md — add missing fields to schema**

In the `## Required YAML Frontmatter` section, add `victims` (text, optional) to the YAML block. Add comments marking required vs optional fields. Ensure `gdrive_root` and `gdrive_path` are documented.

- [ ] **Step 4: Add Statutes/ path config to CASE-BRAIN-CONFIG.md**

Append a new section after "Known Case Mappings":

```markdown
---

## Statute Notes Location

```
Statutes: DW-CASE BRAINS/Statutes/[La. R.S. XX-XX - Title].md
```

### Statute Naming Convention

Filename: `La. R.S. XX-XX - [Statute Title].md`
Example: `La. R.S. 14-30 - First Degree Murder.md`

### Wikilink Format in Case Brains

Use display alias for clean tables:
`[[La. R.S. 14-30 - First Degree Murder|La. R.S. 14-30]]`
```

- [ ] **Step 5: Update existing case brain YAML frontmatter**

Read `CB/Cases/Hadnot-Antonio.md` and `CB/Cases/Nicholas-Jarrell.md`. For each, ensure all fields from the canonical schema are present (add any missing fields with empty/default values). The Hadnot file already has `victims`, `gdrive_root`, and `gdrive_path` — verify they match the schema. Nicholas-Jarrell may be missing these fields — add them.

- [ ] **Step 6: Verify**

Read both template and config files. Read both case brain YAML blocks. Confirm all use the same field set.

---

### Task 6: Update README.md

**Files:**
- Modify: `CB/README.md`

- [ ] **Step 1: Read current README**

Read `CB/README.md` in full.

- [ ] **Step 2: Update Overview section**

Find the paragraph starting `**What does NOT live here:**`. Replace with:

```markdown
**What does NOT live here:** Source documents (discovery PDFs, police reports, forensic reports). Those stay in Google Drive shared drives. Statutes and legal research are fetched on demand from legis.la.gov and Westlaw.
```

- [ ] **Step 3: Update Vault Structure diagram**

Find the code block under `## Vault Structure`. Replace with:

```
DW-CASE BRAINS/
├── Cases/              ← Case Brain for each active matter
├── Witnesses/          ← One note per witness (across all cases)
│   ├── Defense/
│   ├── Expert/
│   ├── Prosecution/
│   └── Persons-of-Interest/
├── Legal-Theories/     ← Doctrines, motion frameworks, case law
├── Statutes/           ← Louisiana statute notes (auto-fetched)
├── Dashboards/         ← Obsidian Base files for firm-wide views
├── Templates/          ← Templates for Case Brains, witnesses, etc.
└── README.md           ← This file
```

- [ ] **Step 4: Update MCP configuration section**

Find the section `### Step 4: Configure Obsidian MCP for Claude`. Replace with:

```markdown
### Step 4: Configure Obsidian MCP for Claude

**Primary: obsidian-claude-code-mcp plugin** (recommended)

Install the `obsidian-claude-code-mcp` community plugin in Obsidian. It runs a WebSocket server on port 22360 that Claude Code auto-discovers. Also supports Claude Desktop via HTTP/SSE transport.

**Fallback: npx mcp-obsidian**

If the plugin is unavailable, add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "mcp-obsidian", "/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law"]
    }
  }
}
```
```

- [ ] **Step 5: Delete DEVONthink indexing section**

Find the section `### Step 5: Index Vault in DEVONthink`. Delete the entire section. Renumber Step 6 → Step 5.

- [ ] **Step 6: Update skill configuration section (now Step 5)**

Find the section about updating the dw-case-brain-crim skill. Replace with:

```markdown
### Step 5: Verify dw-case-brain-crim Skill

The `dw-case-brain-crim` skill reads and writes Case Brains via Obsidian MCP. Verify:
- Obsidian MCP is connected (check Claude's MCP status)
- Skill can search for a case brain in `Cases/`
- Skill can read and write case brain content
- Fallback: If Obsidian MCP is unavailable, paste case brain content manually
```

- [ ] **Step 7: Update "Adding Witnesses" section**

Find the section `### Adding Witnesses`. Replace `Experts/` references with `Witnesses/Expert/`. Add mention of `Witnesses/Persons-of-Interest/` for non-testifying persons.

- [ ] **Step 8: Update Frontmatter Property Reference**

Find the Case Brains property table. Add rows for `victims` (text, optional), `gdrive_root` (text, required w/ GDrive), `gdrive_path` (text, required w/ GDrive).

- [ ] **Step 9: Verify — grep for remaining DEVONthink references**

Search the full README and CASE-BRAIN-CONFIG.md for "DEVONthink". No active references should remain (historical mentions in comments are acceptable).

```bash
grep -n "DEVONthink\|devonthink" "/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/README.md"
grep -n "DEVONthink\|devonthink" "/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/CASE-BRAIN-CONFIG.md"
```

- [ ] **Step 10: Verify — test file:// links**

Open `CB/Cases/Hadnot-Antonio.md` in Obsidian. Click a `file://` link to a Google Drive folder (e.g., Trial Notebook). Confirm it opens the folder in Finder. If Google Drive for Desktop is not running, note as a known prerequisite.

> **Chunk 1 Checkpoint:** Before proceeding to Chunk 2, open Obsidian and verify: (1) vault structure matches the spec, (2) no broken folder references, (3) dashboards still load.

---

## Chunk 2: Phase 2 — MCP Setup & Skill Rewrite

### Task 7: Install and Inspect Obsidian MCP Plugin

> **Prerequisite:** Obsidian must be running with the vault open.

- [ ] **Step 1: Verify obsidian-claude-code-mcp plugin is installed**

In Obsidian: Settings → Community Plugins → search for `obsidian-claude-code-mcp`. If not installed, install and enable it.

- [ ] **Step 2: Verify the MCP server is running**

The plugin should be listening on WebSocket port 22360. Check Claude Code's MCP status to see if an Obsidian MCP server is listed.

- [ ] **Step 3: Inspect available tool names**

List all tools provided by the Obsidian MCP server. Record the exact tool names for:
- Searching/listing notes
- Reading note content
- Writing/creating notes
- Searching vault content

These names will be used in the skill rewrite. If the plugin uses different names than assumed (e.g., `vault_read` vs `read_note`), note the actual names.

- [ ] **Step 4: Test basic operations**

Using the confirmed tool names:
1. Search for "Hadnot" in the vault — confirm the case brain is found
2. Read the content of `DW-CASE BRAINS/Cases/Hadnot-Antonio.md` — confirm full markdown returned
3. Write a test line to a scratch note, then read it back to confirm round-trip works
4. Delete the scratch note

Document any issues or limitations discovered.

---

### Task 8: Rewrite dw-case-brain-crim SKILL.md — Core Session Lifecycle

**Files:**
- Modify: `/Users/greatelephant82/.claude/skills/dw-case-brain-crim/SKILL.md`

> **Dependency:** Task 7 must be complete. Use the confirmed MCP tool names from Task 7 Step 3.

- [ ] **Step 1: Read current SKILL.md**

Read the full file. Note every DEVONthink reference.

- [ ] **Step 2: Update frontmatter description**

Replace "DEVONthink" with "Obsidian vault" throughout the description field.

- [ ] **Step 3: Update "How It Works" section**

Replace `Read Case Brain from DEVONthink` → `Read Case Brain from Obsidian vault` (both open and close lines). Update the description paragraph to reference Obsidian vault path and CASE-BRAIN-CONFIG.md.

- [ ] **Step 4: Rewrite STEP 1 — SESSION OPEN: Identify the Case**

Replace DEVONthink search with:
1. Read `DW-CASE BRAINS/CASE-BRAIN-CONFIG.md` via Obsidian MCP or filesystem
2. Search Obsidian MCP for files in `DW-CASE BRAINS/Cases/` matching client name
3. Alternatively, construct filename directly: `Cases/[LastName]-[FirstName].md`

Use the actual MCP tool names confirmed in Task 7.

- [ ] **Step 5: Rewrite STEP 2 — SESSION OPEN: Load Case Brain**

Replace `devonthink:get_record_content` with the confirmed Obsidian MCP read tool. Keep the SESSION OPEN CONFIRMATION display block identical.

- [ ] **Step 6: Rewrite STEP 3 — FIRST SESSION: Create a New Case Brain**

Replace `devonthink:create_record` with Obsidian MCP file creation. Add the Google Drive auto-detection step from CASE-BRAIN-CONFIG.md. Reference the Case Brain Template at `DW-CASE BRAINS/Templates/Case-Brain-Template.md`.

- [ ] **Step 7: Rewrite STEP 4 — SESSION CLOSE**

Replace `devonthink:update_record_content` with Obsidian MCP write. Emphasize: read current content first, merge updates, then write back. Never overwrite without reading.

- [ ] **Step 8: Rewrite STEP 6 — CASE BRAIN MAINTENANCE**

Replace DEVONthink tagging with YAML frontmatter updates (`status`, `tags`). Replace DEVONthink fallback with: (1) try filesystem read, (2) ask attorney to paste manually, (3) generate updated markdown at session close.

- [ ] **Step 9: Verify — grep for DEVONthink references**

```bash
grep -n "DEVONthink\|devonthink:" "/Users/greatelephant82/.claude/skills/dw-case-brain-crim/SKILL.md"
```

Expected: Zero matches for active DEVONthink tool calls. Zero matches for "DEVONthink" as the storage system.

- [ ] **Step 10: Verify guardrails are preserved**

Confirm the Guardrails section still contains all five rules:
1. Never overwrite without reading first
2. Never delete session log entries
3. Never mark issue resolved without attorney confirmation
4. Never summarize away context
5. Skill fires before other skills when no case context

---

### Task 9: Add New Workflow Sections to dw-case-brain-crim SKILL.md

**Files:**
- Modify: `/Users/greatelephant82/.claude/skills/dw-case-brain-crim/SKILL.md`

> **Dependency:** Verify `CB/Templates/Legal-Theory-Template.md` exists. Read it to confirm structure.

- [ ] **Step 1: Add Statute & Legal Theory Linking section**

After the Integration table, add a new `## Statute & Legal Theory Linking` section covering:
- Statute link format: `[[La. R.S. 14-30 - First Degree Murder|La. R.S. 14-30]]`
- Auto-fetch from legis.la.gov when statute note missing
- Westlaw enhanced fetch (requires attorney's active Chrome session)
- Legal theory link format: `[[Art. 701 Speedy Trial]]`
- Auto-fetch from Westlaw for case law/doctrines (author summary, not verbatim)
- Witness link format: `[[Last, First]]`
- Case file link format: `[Name](file:///path)` per CASE-BRAIN-CONFIG.md

- [ ] **Step 2: Add Document Search section**

Add a new `## Document Search (Replacing DEVONthink AI Search)` section covering:
- Search procedure: read Case File Locations → narrow candidates → read files → return results
- Token management: target 3–5 file reads, two-pass strategy
- Search index caching: `Case-Search-Index.md` for heavy-use cases

- [ ] **Step 3: Update Integration table**

Add `dw-mobile-forensic-auditor-crim` to the skill integration table.

- [ ] **Step 4: Update references/case-brain-template.md**

Read `/Users/greatelephant82/.claude/skills/dw-case-brain-crim/references/case-brain-template.md`. Update it to match `CB/Templates/Case-Brain-Template.md` (the canonical version). Add `victims` and `gdrive_root`/`gdrive_path` to YAML. Update Key Evidence Flags types.

- [ ] **Step 5: Commit core skill rewrite + new sections**

```bash
cd /Users/greatelephant82/.claude/skills
git add dw-case-brain-crim/SKILL.md dw-case-brain-crim/references/case-brain-template.md
git commit -m "feat: rewrite dw-case-brain-crim skill for Obsidian MCP (replace DEVONthink)"
```

---

### Task 10: Update Companion Skill Output Paths

**Files:** 11 companion skills (see list below). Each skill that writes output to DEVONthink needs updating.

**Output path strategy:** All skill outputs go to the relevant top-level category folder in the vault, NOT per-case subfolders. This matches the existing vault structure.

| Skill Type | Output Folder |
|---|---|
| Motions (suppression, 404b) | `CB/Pleadings/` |
| Cross-exam outlines | `CB/Cross-Exam/` (if folder exists) or case-specific note |
| Forensic audits | `CB/Case-Analysis/` |
| Evidence audits (Brady, CI, search warrant) | `CB/Evidence/` |
| LWOP worksheets | `CB/Verdict-Sentencing/` |
| General case analysis | `CB/Case-Analysis/` |

Skills to update:
1. `dw-criminal-defense-crim` 2. `dw-forensic-dump-analyzer-crim` 3. `dw-suppression-motion-crim` 4. `dw-cross-exam-architect-crim` 5. `dw-brady-giglio-auditor-crim` 6. `dw-search-warrant-auditor` 7. `dw-cell-site-geolocation-auditor-crim` 8. `dw-404b-opposition-crim` 9. `dw-ci-auditor` 10. `dw-lwop-populator` 11. `dw-mobile-forensic-auditor-crim`

- [ ] **Step 1: Batch 1 — Read and update skills 1–4**

For each: read SKILL.md, search for "DEVONthink"/"devonthink:", replace output storage references with the Obsidian vault path per the table above. Add instruction: "Record the output in the Case Brain's COMPANION SKILL OUTPUTS section."

- [ ] **Step 2: Batch 2 — Read and update skills 5–8**

Same process for skills 5–8.

- [ ] **Step 3: Batch 3 — Read and update skills 9–11**

Same process for skills 9–11.

- [ ] **Step 4: Verify — grep all companion skills for DEVONthink**

```bash
cd /Users/greatelephant82/.claude/skills
grep -rn "DEVONthink\|devonthink:" dw-*/SKILL.md
```

Expected: No matches for active DEVONthink references.

- [ ] **Step 5: Commit**

```bash
cd /Users/greatelephant82/.claude/skills
git add dw-*/SKILL.md
git commit -m "feat: update companion skill output paths from DEVONthink to Obsidian vault"
```

---

## Chunk 3: Phase 3 — Statute & Legal Theory Fetcher

### Task 11: Test Statute Fetcher End-to-End

> The workflow is documented in the skill (Task 9). This task validates it works.

- [ ] **Step 1: Verify Claude in Chrome MCP is available**

Check that these tools are accessible: `mcp__Claude_in_Chrome__navigate`, `mcp__Claude_in_Chrome__get_page_text`, `mcp__Claude_in_Chrome__read_page`. If not, verify the extension is installed and running.

- [ ] **Step 2: Test legis.la.gov fetch — La. R.S. 14:30.1 (Second Degree Murder)**

Execute the fetch workflow:
1. Navigate to legis.la.gov
2. Search for "R.S. 14:30.1"
3. Extract: title, full text, effective date
4. Create `CB/Statutes/La. R.S. 14-30.1 - Second Degree Murder.md` using Statute Template
5. Populate all template sections

- [ ] **Step 3: Verify the created statute note**

Read the file. Confirm: YAML frontmatter complete, full text present, elements populated, penalty populated, source metadata includes fetch date.

- [ ] **Step 4: Test Westlaw enhanced fetch (Manual Test — requires attorney's active Westlaw session)**

If attorney has an active Westlaw session: navigate to Westlaw, search for La. R.S. 14:30.1, extract annotations/case law, update the note. If Westlaw not available, skip and log for later.

- [ ] **Step 5: Test wikilink resolution**

Verify `[[La. R.S. 14-30 - First Degree Murder]]` resolves in Obsidian. Verify `[[La. R.S. 14-30.1 - Second Degree Murder]]` would resolve.

- [ ] **Step 6: Batch-create statutes for existing case brain references**

Read all case brains. Extract every La. R.S. citation. For each without a note in `Statutes/`, fetch from legis.la.gov and create.

---

### Task 12: Test Legal Theory Fetcher

- [ ] **Step 1: Verify existing legal theory notes and Legal-Theory-Template.md**

Read `CB/Templates/Legal-Theory-Template.md` to confirm structure. Read each file in `CB/Legal-Theories/`: Art. 701 Speedy Trial.md, Felony Murder.md, Melendez Notice.md. Confirm they have adequate content; enhance stubs.

- [ ] **Step 2: Test fetch — Franks v. Delaware (Manual Test — requires Westlaw or web search)**

Author a summary note for Franks v. Delaware (1978) using Legal-Theory-Template.md. Include: holding, elements for a Franks hearing, Louisiana application, key case law. Save to `CB/Legal-Theories/Franks v. Delaware.md`.

- [ ] **Step 3: Verify the note**

Read the file. Confirm YAML frontmatter, all template sections populated, wikilinks to related cases/statutes present.

---

## Chunk 4: Phase 4 — Document Search & Verification

### Task 13: Test Document Search Workflow

- [ ] **Step 1: Test search — Hadnot case (Manual Test — requires Google Drive for Desktop running)**

Execute a test search:
1. Read Hadnot case brain's Case File Locations section
2. Get the Google Drive path from `gdrive_path` YAML field
3. List files in the discovery directory
4. Read a candidate PDF (if locally cached)

Document: which files are accessible, any cloud-only issues, approximate response time.

- [ ] **Step 2: Build search index for Hadnot case**

Create `CB/Cases/Hadnot-Search-Index.md` with:
- File inventory (names and one-line descriptions)
- Key topics mapped to files

This is a Phase 4 deliverable per the spec.

- [ ] **Step 3: Commit**

```bash
cd /Users/greatelephant82/.claude/skills
git add dw-case-brain-crim/SKILL.md
git commit -m "feat: finalize document search workflow in dw-case-brain-crim"
```

---

### Task 14: Spec Success Criteria Verification

- [ ] **Step 1: Verify witness/expert backlinks across cases**

Open `CB/Witnesses/Expert/Downs, Amber.md` in Obsidian. Check the backlinks panel — it should show both Hadnot-Antonio.md and Nicholas-Jarrell.md (if Downs appears in both). If backlinks don't appear, check that wikilinks in case brains use the exact filename.

- [ ] **Step 2: Verify file:// links open correctly**

Open a case brain in Obsidian. Click a `file://` link. Confirm it opens the target in Finder. If Google Drive is not mounted, note as prerequisite.

- [ ] **Step 3: YAML frontmatter audit**

Read every file in `CB/Cases/`. For each, verify YAML contains all canonical schema fields. List any discrepancies.

- [ ] **Step 4: Verify dashboards display correctly**

Open `CB/Dashboards/Active Cases.base` — all cases should appear with correct fields. Open `CB/Dashboards/Witness Database.base` — all witnesses should appear.

---

## Chunk 5: Phase 5 — Migration & Decommission

> **Prerequisite:** DEVONthink must still be running and its MCP server active for the inventory step.

### Task 15: Migrate Remaining DEVONthink Case Brains

- [ ] **Step 1: Inventory DEVONthink case brains**

Search DEVONthink via MCP for all records tagged "case-brain". List all results. Compare against `CB/Cases/`. Identify which need migration.

- [ ] **Step 2: Migrate each unmigrated case brain (~5–10 min per case)**

For each case brain in DEVONthink but not in Obsidian:
1. Read full content from DEVONthink
2. Create file at `CB/Cases/[LastName]-[FirstName].md`
3. Ensure YAML matches canonical schema
4. Convert links to Obsidian wikilinks and `file://` links per CASE-BRAIN-CONFIG.md
5. Create missing witness notes in `CB/Witnesses/`
6. Create missing statute notes in `CB/Statutes/`

- [ ] **Step 3: Verify all case brains in Obsidian**

```bash
ls "/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/DW-CASE BRAINS/Cases/"
```

Count should match DEVONthink inventory. Spot-check 2–3 files for content completeness.

---

### Task 16: Parallel Run Validation

> All steps in this task are **Manual Tests** requiring interactive Claude sessions.

- [ ] **Step 1: Test session open/close on 2+ cases**

For each of at least 2 cases:
1. Start a new Claude session
2. "Load the [client] case"
3. Verify loads from Obsidian
4. Perform a small task (add note, update issue)
5. "Wrap up" → verify case brain updated in Obsidian
6. Start NEW session, reload → verify updates persisted

- [ ] **Step 2: Test statute auto-fetch in live session**

Reference a statute that doesn't exist. Verify Claude detects, fetches from legis.la.gov, creates note, wikilink resolves.

- [ ] **Step 3: Test document search in live session**

Ask to find something in discovery. Verify Claude reads Case File Locations, navigates to correct path, returns passage.

- [ ] **Step 4: Confirm go/no-go criteria**

- [ ] All case brains accessible via Obsidian MCP (2+ sessions each)
- [ ] No data loss or corruption during parallel run
- [ ] Attorney confirms Obsidian is primary system
- [ ] Statute fetcher used successfully 3+ times
- [ ] Westlaw enhanced fetch used successfully 2+ times
- [ ] Legal concept auto-fetch used successfully 2+ times
- [ ] Document search used successfully on 2+ cases
- [ ] Search token cost under 50K per typical query
- [ ] Witness/expert backlinks resolve across cases
- [ ] YAML frontmatter consistent across all case brains

- [ ] **Step 5: Decommission DEVONthink (after attorney explicit approval)**

1. Remove remaining DEVONthink references from README
2. DEVONthink data retained (never deleted) but no longer actively used
3. `dw-case-brain-crim` skill Obsidian-only path is now the sole path

---

## Summary

| Phase | Tasks | Key Deliverable |
|---|---|---|
| Phase 1 | Tasks 1–6 | Vault restructured, templates updated, README updated |
| Phase 2 | Tasks 7–10 | MCP configured, dw-case-brain-crim rewritten, companion skills updated |
| Phase 3 | Tasks 11–12 | Statute fetcher tested, legal theory fetcher tested |
| Phase 4 | Tasks 13–14 | Document search tested, success criteria verified |
| Phase 5 | Tasks 15–16 | All case brains migrated, parallel run validated, DEVONthink decommissioned |
