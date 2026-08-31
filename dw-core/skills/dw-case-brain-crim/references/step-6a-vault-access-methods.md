# Step 6A — Obsidian File Location & Vault Detection (Detailed)

Read from SKILL.md **Step 6A** — environment detection (Cowork vs. Claude Code), Method 1 (Obsidian MCP) with the tool-mapping table, Method 2 (mounted / local filesystem), Method 3 (last resort), and the config-file rule.

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
