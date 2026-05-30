# Obsidian Case Brain Migration — Design Spec

> **Date:** 2026-03-25
> **Status:** In Review
> **Author:** Claude (brainstorming session with CJW)
> **Scope:** Migrate D&W case brain system from DEVONthink to pure Obsidian with MCP integration, statute fetching, and document search

---

## 1. Problem Statement

The D&W case brain system currently lives in DEVONthink, accessed via DEVONthink MCP. The attorney needs:

- **Wikilink navigation** between case brains, statutes, witnesses, and legal concepts — with internal resolution when the note exists and auto-creation when it doesn't
- **Statute fetching** from Westlaw when a statute note doesn't exist locally
- **Cross-case knowledge accumulation** — witnesses, experts, and legal theories that build up across cases over time
- **Full MCP integration** so Claude can read/write case brains automatically at session open/close

DEVONthink cannot do smart link fallthrough (try internal, fall back to external). Obsidian's wikilink system, combined with an MCP server and a Westlaw fetch workflow, satisfies all requirements.

---

## 2. Decision: Pure Obsidian (Drop DEVONthink)

**Approach chosen:** Move all case brains and practice knowledge to Obsidian. DEVONthink is fully replaced. Claude-driven document search replaces DEVONthink's AI search.

**Trade-offs accepted:**
- Lose DEVONthink's instant pre-indexed semantic search across PDFs
- Gain: single system, wikilink navigation, cross-case knowledge graph, statute auto-fetch
- Document search compensated by Claude reading PDFs on demand (slower but more contextually accurate)

---

## 3. Existing Vault Structure (Adopted As-Is)

The Obsidian vault already exists at:

```
/Users/greatelephant82/Library/Mobile Documents/iCloud~md~obsidian/Documents/Dream Team Law/
```

The case brain system lives in `DW-CASE BRAINS/` within that vault. Existing structure:

```
DW-CASE BRAINS/
├── CASE-BRAIN-CONFIG.md        ← Google Drive paths, link generation rules, YAML spec
├── README.md                   ← Setup guide, MCP config, usage instructions
├── Cases/
│   ├── Hadnot-Antonio.md       ← Active case brain (Phase 3)
│   └── Nicholas-Jarrell.md     ← Active case brain
├── Witnesses/
│   ├── Defense/                ← (empty, ready for use)
│   ├── Expert/
│   │   ├── Downs, Amber.md
│   │   └── Quaal, Monica.md
│   └── Prosecution/
│       ├── Randall, Devin Sr..md
│       ├── Stepney, Patrick.md
│       ├── Valle Portillo, David.md
│       ├── Fontenot, Det. Willie.md
│       └── ... (13 total)
├── Experts/                    ← REDUNDANT — to be removed
├── Legal-Theories/
│   ├── Art. 701 Speedy Trial.md
│   ├── Felony Murder.md
│   ├── La. R.S. 14-30.md      ← TO BE MOVED to Statutes/
│   └── Melendez Notice.md
├── Templates/
│   ├── Case-Brain-Template.md
│   ├── Expert-Template.md
│   ├── Legal-Theory-Template.md
│   ├── Motion-Template.md
│   └── Witness-Template.md
├── Dashboards/
│   ├── Active Cases.base
│   └── Witness Database.base
├── Case-Analysis/
├── Closing-Arguments/
├── Evidence/
├── Jury-Selection/
├── Opening-Statements/
├── Pleadings/
├── Pretrial-Orders/
├── Verdict-Sentencing/
└── {Cases,Witnesses,...}       ← ARTIFACT — brace expansion error, to be deleted
```

### Existing Configuration

**CASE-BRAIN-CONFIG.md** already defines:
- Three Google Drive shared drives (NOLA Conflict Cases, CALCASIEU PDO Files, D&W Law Firm CJW)
- Auto-detection procedure for finding client folders across drives
- `file://` link generation with URL encoding rules
- Standard links to generate (Client Folder, Trial Notebook, Pretrial Notebook, Case Tables, Pleadings, Discovery, Case Analysis)
- Required YAML frontmatter schema
- Known case-to-drive mappings

**README.md** already documents:
- MCP configuration for Claude Desktop, Claude Code, and Claude Chat
- Plugin requirements (Bases, Templates, Backlinks, Graph View, Tags)
- Recommended community plugins (Templater, Dataview, Calendar)
- Frontmatter property reference for Cases and Witnesses
- Usage workflows for session open/close, creating case brains, adding witnesses

---

## 4. Structural Changes to Existing Vault

### 4A. Add `Statutes/` Folder

Statutes need their own folder, separate from Legal-Theories, to support the Westlaw auto-fetch workflow. Claude must be able to distinguish "this is a statute I should fetch from Westlaw" from "this is an internally authored legal theory."

Flat structure (no Title subfolders — simpler, avoids requiring Title lookup overhead):

```
Statutes/
├── La. R.S. 14-30 - First Degree Murder.md
├── La. R.S. 14-30.1 - Second Degree Murder.md
├── La. R.S. 15-529.1 - Habitual Offender Law.md
└── ...
```

Each statute file follows a Statute Template (to be created as a Phase 1 deliverable — see 4D).

**Migration:** Move `Legal-Theories/La. R.S. 14-30.md` to `Statutes/La. R.S. 14-30 - First Degree Murder.md`. Update all wikilinks in existing case brains.

### 4B. Add `Witnesses/Persons-of-Interest/` Subfolder

People like Chasity Nix-Corbello (given Miranda, interrogated as suspect, not a testifying witness) don't fit Defense, Expert, or Prosecution. Add:

```
Witnesses/
├── Defense/
├── Expert/
├── Prosecution/
└── Persons-of-Interest/    ← NEW
```

### 4C. Remove Redundant `Experts/` Folder

Top-level `Experts/` is empty and redundant with `Witnesses/Expert/`. Remove it.

### 4D. Add Statute Template

New template: `Templates/Statute-Template.md` — to be authored during Phase 1 implementation.

Required sections:
- YAML frontmatter: `tags`, `statute_number`, `title`, `effective_date`, `source`, `fetch_date`
- Full statute text (as enacted)
- Elements / requirements (bulleted breakdown)
- Key case law interpreting the statute
- Annotations / practice notes
- Related statutes (wikilinks)
- Source metadata (Westlaw citation, legis.la.gov URL, fetch date)

### 4E. Update Case Brain Template

Ensure `Templates/Case-Brain-Template.md` includes all sections from the Hadnot case brain PDF:

- Case Overview (with Additional Staff field)
- Charges & Exposure
- Case File Locations (with `file://` links per CASE-BRAIN-CONFIG.md)
- Theory of Case / Defense Narrative
- Current Status (with Phase Quality Gates)
- Open Issues
- Next Steps
- Key Decisions
- Key Evidence Flags (expanded types: Defense exculpatory, Defense third-party suspect, Defense identity, Prosecution inculpatory, Brady potential, Impeachment)
- Companion Skill Outputs
- Discovery Status
- Witness Summary (including Defense potential witnesses with VERIFY status)
- Motions Status
- Session Log

### 4F. Reconcile YAML Frontmatter Schema

The CASE-BRAIN-CONFIG.md defines a required YAML schema, but existing case brains contain fields not in the schema (e.g., `victims`, `staff`). During Phase 1:

- Audit all YAML fields in existing case brains (Hadnot-Antonio.md, Nicholas-Jarrell.md)
- Add missing fields to the canonical schema in CASE-BRAIN-CONFIG.md: `victims` (list), `staff` (list/text)
- Mark each field as required or optional
- Ensure `gdrive_root` and `gdrive_path` are documented in the Case Brain Template
- Update all existing case brains to match the reconciled schema

### 4G. Clean Up Vault Artifacts

- Delete the `{Cases,Witnesses,Experts,Legal-Theories,Motions,Templates,Dashboards,.obsidian}` folder (brace expansion artifact from a failed mkdir command)

---

## 5. Technical Architecture

### 5A. Obsidian MCP Integration

**Primary MCP server:** `obsidian-claude-code-mcp` plugin (WebSocket on port 22360). This is preferred because:
- Runs as an Obsidian plugin (no separate process to manage)
- Supports both Claude Code and Claude Desktop simultaneously
- Auto-discovered by Claude Code

**Fallback MCP server:** `npx mcp-obsidian` (npm package) if the plugin is unavailable.

The `dw-case-brain-crim` skill is rewritten to use Obsidian MCP instead of DEVONthink MCP.

**Operation mapping (obsidian-claude-code-mcp tool names):**

| Operation | DEVONthink (current) | Obsidian MCP (new) |
|---|---|---|
| Search for case brain | `devonthink:search` | `obsidian:search` — query filename in `DW-CASE BRAINS/Cases/` |
| Read case brain | `devonthink:get_record_content` | `obsidian:read_note` — path `DW-CASE BRAINS/Cases/[Client].md` |
| Write/update case brain | `devonthink:update_record_content` | `obsidian:write_note` — path + full content |
| Create new case brain | `devonthink:create_record` | `obsidian:create_note` — path + template content |
| Tag management | `devonthink:add_tags` | Edit YAML frontmatter `tags:` field via `obsidian:write_note` |

*Note: Exact tool names will be confirmed during Phase 2 when the MCP server is configured and its schema is inspected. The skill rewrite depends on this confirmation.*

**Session lifecycle unchanged:**
1. Session open → read case brain from Obsidian → load into context → display confirmation
2. Work happens (using companion D&W skills)
3. Session close → generate delta → update case brain in Obsidian → confirm save

**Fallback:** If Obsidian MCP is unavailable, attorney pastes case brain content manually. At session close, Claude generates updated markdown for attorney to paste back.

### 5B. Statute Fetcher

**Trigger:** Claude encounters a statute wikilink (e.g., `[[La. R.S. 14-30.1 - Second Degree Murder]]`) that doesn't resolve to an existing note, or the attorney explicitly requests a statute.

**Primary source: legis.la.gov** (Louisiana Legislature's free public website)

For standard Louisiana statute text, the free public source is preferred:
1. Claude navigates to `legis.la.gov` via Claude in Chrome MCP
2. Searches for the statute by R.S. citation
3. Extracts the full statute text, title, and effective date
4. Creates a new markdown file using Statute Template
5. Saves to `Statutes/La. R.S. XX-XX - [Statute Title].md`

**Secondary source: Westlaw** (for annotations, case law, practice notes)

When the attorney needs more than the bare statute text (annotations, key citing decisions, practice notes):
1. Claude opens Chrome via Claude in Chrome MCP
2. Navigates to Westlaw — **assumes the attorney is already logged in** via an active browser session
3. If not logged in, Claude prompts: *"Westlaw needs authentication. Please log in and tell me when you're ready."*
4. If 2FA is required, Claude prompts: *"Westlaw is asking for two-factor authentication. Please complete it and tell me when you're ready."*
5. Claude searches for the statute, extracts enhanced content (annotations, case notes)
6. Merges with or replaces the legis.la.gov content in the statute note

**Failure modes:**
- **Westlaw session expired / not logged in:** Claude prompts attorney to log in manually, then resumes
- **2FA / CAPTCHA:** Claude prompts attorney to complete, then resumes
- **Westlaw UI changes break extraction:** Claude falls back to legis.la.gov for statute text; flags that Westlaw annotations could not be fetched
- **Complete fetch failure:** Claude prompts attorney to paste statute text manually; Claude formats into template and saves

**Westlaw Terms of Service note:** This workflow uses Claude in Chrome to interact with Westlaw through the attorney's authenticated browser session, the same way the attorney would manually browse. Claude does not scrape, store credentials, or bypass authentication. The attorney maintains their active Westlaw subscription and session.

### 5C. Legal Theory Fetcher (Separate from Statute Fetcher)

Fetching case law and legal doctrines (e.g., `[[Franks v. Delaware]]`, `[[Daubert Standard]]`) is substantially more complex than fetching a statute. Statutes have canonical text; case law requires selecting the right reporter, extracting holdings, and summarizing relevance.

**Workflow for case law / doctrines:**
1. Claude searches Westlaw (via attorney's active session) for the case or doctrine
2. Extracts: case citation, court, date, holding, key facts, and relevance to criminal defense
3. Claude **authors a summary note** rather than copying verbatim — this is attorney work product
4. Saves to `Legal-Theories/[Case or Doctrine Name].md`

**This is a Phase 3 deliverable**, separate from and after the statute fetcher. It shares the same Chrome MCP transport but has different extraction logic and a higher error rate.

### 5D. Document Search (Replacing DEVONthink AI Search)

Claude-driven search replaces DEVONthink's pre-indexed semantic search.

**Access method:** Claude Code's native filesystem Read tool. Google Drive for Desktop mounts shared drives at the paths documented in CASE-BRAIN-CONFIG.md. Files accessed via these paths are read through the macOS FUSE mount.

**Workflow:** When attorney asks something like "find the document where Randall describes the shooter":
1. Claude reads the case brain's Case File Locations to get Google Drive paths
2. Uses Glob/Read tools to list and read files in relevant directories
3. For PDFs: reads them directly via the Read tool (Claude reads PDFs natively, max 20 pages per request)
4. For text/markdown: uses Grep for keyword search, then Read for context
5. Returns the relevant document with the specific passage

**Handling cloud-only files:** Google Drive for Desktop may stream files on demand rather than caching them locally. If a file read fails or times out:
- Claude reports which files could not be read
- Suggests the attorney open the file in Google Drive to trigger local caching
- Retries after the attorney confirms

**Token budget and pagination:** Discovery sets for a murder case can be thousands of pages. To manage token costs:
- Claude searches **file names and directory structure first** to narrow candidates before reading content
- PDFs are read in 20-page chunks, scanning for relevance before reading more
- When searching across many documents, Claude uses a **two-pass strategy**: (1) keyword grep/skim to identify candidate files, (2) deep read of top candidates only
- **Target: identify relevant passages within 3–5 file reads** for a typical query

**Search index caching (Phase 4 deliverable):** For heavy-use cases, Claude builds a `Case-Search-Index.md` note in the case folder that caches:
- File inventory with descriptions
- Key passages and their locations (file + page number)
- Keyword-to-file mappings
This index is updated incrementally as new discovery is processed.

**Trade-offs:**

| Factor | DEVONthink Search | Claude-Driven Search |
|---|---|---|
| Speed | Instant (pre-indexed) | 30–120 seconds typical |
| Accuracy | Good fuzzy match | Better contextual understanding |
| Scope | Everything in database | Scoped to case file locations |
| Requires | DEVONthink running | Claude session active |
| Cost | None (local) | ~5K–50K tokens per search |

### 5E. Skill Rewrite Scope

**Full inventory of skills requiring changes:**

| Skill | Change Required |
|---|---|
| `dw-case-brain-crim` | Full rewrite — Obsidian MCP instead of DEVONthink MCP |
| `dw-criminal-defense-crim` | Update output paths: write skill outputs to vault case folder |
| `dw-forensic-dump-analyzer-crim` | Update output paths |
| `dw-suppression-motion-crim` | Update output paths |
| `dw-cross-exam-architect-crim` | Update output paths |
| `dw-brady-giglio-auditor-crim` | Update output paths |
| `dw-search-warrant-auditor` | Update output paths |
| `dw-cell-site-geolocation-auditor-crim` | Update output paths |
| `dw-404b-opposition-crim` | Update output paths |
| `dw-ci-auditor` | Update output paths |
| `dw-lwop-populator` | Update output paths |
| `dw-mobile-forensic-auditor-crim` | Update output paths |
| `CASE-BRAIN-CONFIG.md` | Remove DEVONthink references; add statute fetcher config; add Statutes/ path |
| `README.md` | Full update — see Section 5F |

### 5F. README.md Updates Required

The following README sections must be updated to remove DEVONthink references and reflect the pure-Obsidian architecture:

| README Section | Current Content | Required Change |
|---|---|---|
| Overview (line 14) | "DEVONthink (law library)" | Remove DEVONthink reference |
| Vault Structure (lines 20–29) | Shows `Experts/`, `Motions/` | Add `Statutes/`, `Persons-of-Interest/`; remove `Experts/` |
| Step 4: Configure Obsidian MCP (lines 63–81) | Documents both MCP options | Specify primary (obsidian-claude-code-mcp) and fallback |
| Step 5: Index Vault in DEVONthink (lines 83–92) | Full DEVONthink indexing instructions | **Delete entire section** |
| Step 6: Update dw-case-brain-crim (lines 96–101) | References DEVONthink fallback | Rewrite for Obsidian-only |
| Adding Witnesses (lines 120–124) | References `Experts/` folder | Update to `Witnesses/Expert/` |
| Frontmatter Property Reference (lines 142–170) | Missing `victims`, `staff` | Add all reconciled fields |

---

## 6. Linking Model

### Four Link Types

**1. Statute Links**
- Format: `[[La. R.S. 14-30 - First Degree Murder|La. R.S. 14-30]]` (alias for clean display)
- Resolves to: `Statutes/La. R.S. XX-XX - [Title].md`
- If missing: Claude fetches from legis.la.gov (primary) or Westlaw (enhanced)

**2. Legal Concept Links**
- Format: `[[Art. 701 Speedy Trial]]`, `[[Felony Murder]]`, `[[Franks v. Delaware]]`
- Resolves to: `Legal-Theories/[concept].md`
- If missing: Claude fetches from Westlaw and authors a summary note (Phase 3)

**3. People Links**
- Format: `[[Randall, Devin Sr.]]`, `[[Downs, Amber]]`
- Resolves to: `Witnesses/[Type]/[Name].md`
- Obsidian resolves wikilinks by filename regardless of subfolder path

**4. File System Links**
- Format: `[Trial Notebook](file:///URL-encoded-path)`
- Opens folder/file on disk via Google Drive
- Generated per CASE-BRAIN-CONFIG.md URL encoding rules

### Cross-Case Knowledge Network

```
Case Brain: Hadnot ──→ [[Downs, Amber]] ←── Case Brain: Nicholas
                   ──→ [[La. R.S. 14-30]] ←── Case Brain: [Future]
                   ──→ [[Fontenot, Det. Willie]] ←── Case Brain: [Future]
```

- Witness note backlinks → every case they appear in
- Statute note backlinks → every case charging under it
- Legal theory backlinks → every case using that defense
- Graph View visualizes the full practice knowledge web

### Link Maintenance

When Claude creates or updates a case brain:
- All statute citations → wikilinks to `Statutes/`
- All witness/expert names → wikilinks to `Witnesses/`
- All legal concepts → wikilinks to `Legal-Theories/`
- All case file paths → `file://` links per CASE-BRAIN-CONFIG.md
- Claude checks for broken wikilinks and flags missing notes (or auto-creates via fetch)

---

## 7. Migration Plan (5–20 Active Case Brains)

### Phase 1: Vault Structure Updates
- Create `Statutes/` folder (flat structure)
- Create `Witnesses/Persons-of-Interest/`
- Remove redundant top-level `Experts/`
- Delete brace-expansion artifact folder
- Move `La. R.S. 14-30.md` from Legal-Theories to Statutes (with renamed file)
- Author `Templates/Statute-Template.md`
- Update `Templates/Case-Brain-Template.md` with all Hadnot PDF sections
- Reconcile YAML frontmatter schema (Section 4F)
- Update CASE-BRAIN-CONFIG.md
- Update README.md (all sections per 5F)

### Phase 2: MCP & Skill Rewrites
- Install and configure `obsidian-claude-code-mcp` plugin
- Inspect MCP tool schema and confirm tool names
- Rewrite `dw-case-brain-crim` skill for Obsidian MCP
- Update all 11 companion skills (output paths)
- **Parallel run begins:** Both DEVONthink and Obsidian are active; Obsidian is primary, DEVONthink is read-only fallback

### Phase 3: Statute & Legal Theory Fetcher
- Build legis.la.gov statute fetch workflow (primary)
- Build Westlaw enhanced fetch workflow (secondary)
- Build legal theory fetch workflow (case law, doctrines)
- Create initial statute notes for all statutes referenced in existing case brains
- Test auto-fetch on a missing statute end-to-end

### Phase 4: Document Search
- Build Claude-driven search workflow against Google Drive case files
- Test against known queries (e.g., "find where Randall describes the shooter")
- Build search index caching (`Case-Search-Index.md`) for heavy-use cases
- Validate token costs are within acceptable range (~5K–50K tokens per search)

### Phase 5: Case Brain Migration & Decommission
- For each of the 5–20 existing case brains in DEVONthink:
  - Export content
  - Verify it matches the Obsidian version (if already migrated like Hadnot)
  - Ensure all wikilinks resolve
  - Update YAML frontmatter to reconciled schema
- Verify dashboards (Active Cases.base, Witness Database.base) display correctly
- **Go/no-go criteria for decommissioning DEVONthink:**
  - [ ] All case brains successfully read/written via Obsidian MCP for 2+ sessions each
  - [ ] No data loss or corruption incidents during parallel run
  - [ ] Attorney confirms Obsidian is the primary system
  - [ ] Statute fetcher has been used successfully at least 3 times
  - [ ] Document search has been used successfully on at least 2 cases
- Once all criteria met: decommission DEVONthink for case brain storage

### Rollback Plan

If critical issues arise during any phase:
- **Phase 1–2:** Obsidian vault changes are additive (new folders, updated files). DEVONthink case brains are untouched. Rollback = revert to DEVONthink skill, no data loss.
- **Phase 3–4:** These are new capabilities (fetcher, search). Rollback = disable the workflows; core case brain functionality is unaffected.
- **Phase 5:** Case brains are not deleted from DEVONthink until all go/no-go criteria pass. During parallel run, DEVONthink remains fully functional as a read-only fallback.

At no point is DEVONthink data deleted or modified. Decommissioning means stopping use, not deleting data.

---

## 8. Guardrails (Carried Forward)

- Never overwrite a case brain without reading the current version first. Always pull → merge → write.
- Never delete session log entries. Session history is append-only.
- Never mark an open issue resolved unless the attorney explicitly confirms.
- Never summarize away context from the full brief.
- The case brain skill fires before other skills when no case context is present.

---

## 9. Success Criteria

- [ ] All existing case brains accessible via Obsidian MCP from Claude sessions
- [ ] Session open/close cycle works end-to-end with Obsidian (tested on 2+ cases, 2+ sessions each)
- [ ] Statute wikilinks auto-fetch from legis.la.gov when note is missing (3+ successful fetches)
- [ ] Westlaw enhanced fetch works when attorney is logged in (2+ successful fetches)
- [ ] Legal concept wikilinks auto-fetch from Westlaw (2+ successful fetches)
- [ ] Witness/expert wikilinks resolve across cases via backlinks
- [ ] `file://` links open Google Drive folders from case brains
- [ ] Claude can search discovery PDFs on demand and return relevant passages within 2 minutes
- [ ] Search token cost stays under 50K tokens per typical query
- [ ] Dashboards display all active cases and witnesses correctly
- [ ] YAML frontmatter is consistent across all case brains and matches canonical schema
- [ ] DEVONthink go/no-go criteria all pass before decommissioning
