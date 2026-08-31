# Step 4 — Session Close Protocol (Detailed)

Read from SKILL.md **STEP 4 — SESSION CLOSE** — the full 4A–4H procedure: session delta, attorney prompt, full-document read, in-memory merge table, full-document write-back, verification, fallback protocol, and the confirmation banner.

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

### 4C — Read Current Case Brain (Full Document)

Use the **same method** you used at session open to read the entire current Case Brain into memory:
- **Via MCP:** `obsidian_get_file_contents` with `filepath: "DW-CASE BRAINS/Cases/[LastName]-[FirstName].md"`
- **Via mounted folder:** Use the `Read` tool with the absolute path

Do NOT attempt to read sections individually. Read the complete document in one operation.

### 4D — Merge All Changes In-Memory

Apply all updates to the full document now in Claude's context:

| Section | What to Update |
|---|---|
| `YAML Frontmatter` | Update `last_updated` and `phase` fields if changed. Preserve all other YAML fields. |
| `CURRENT STATUS` | Update phase / status if changed |
| `SESSION LOG` | Prepend new session entry at the top of this section (most recent first) |
| `OPEN ISSUES` | Add new issues; mark resolved issues with checkmark; preserve all existing issues |
| `NEXT STEPS` | Replace with fresh list from this session |
| `KEY DECISIONS` | Append any decisions made this session |
| `COMPANION SKILL OUTPUTS` | Add links to new deliverables (files, motions, analysis reports, etc.) generated this session |
| `Case File Locations` | Only add links to new files if they've been created during this session. Preserve all existing links. |

**IMPORTANT MERGE RULE:** Preserve ALL existing content that has not changed. This is a merge, not a replacement. You are updating specific fields while keeping the rest of the document intact.

### 4E — Write Full Document Back

Write the complete merged document using **full-document replacement**, never section-by-section patching:
- **Via MCP:** Use `obsidian_patch_content` with `operation: "replace"` on the target `filepath`, passing the complete updated document content.
  - Alternatively, use `obsidian_delete_file` followed by `obsidian_create_record` with the complete merged document.
- **Via mounted folder:** Use the `Edit` tool with `old_string` set to the entire original document and `new_string` set to the complete merged document. Or use the `Write` tool with `mode: "rewrite"` to overwrite the entire file.

**CRITICAL RULE:** Never attempt to patch individual sections by heading name. Always write the complete document. This prevents data loss from heading-targeting failures.

### 4F — Verify Write Success

Read the file back immediately with the same method you used at 4C:
- **Via MCP:** `obsidian_get_file_contents` with the same filepath
- **Via mounted folder:** Use the `Read` tool with the same path

Confirm that:
- The new session entry appears in `SESSION LOG`
- Updated fields (status, next steps, issues) match what you merged
- YAML frontmatter is intact and `last_updated` reflects today's date
- No content was lost

### 4G — Fallback Protocol (If Write Fails)

If the Obsidian write fails for any reason (MCP timeout, filesystem error, permission issue, or any other failure):

1. **Save the complete updated Case Brain as a markdown file** in the case folder on Google Drive at:
   ```
   [case-root]/02 - Pretrial Notebook/03 - Case Analysis & Notes/CASE BRAIN — [Client Name] | [Docket].md
   ```
   Use the complete merged document content you created in step 4D.

2. **Notify the attorney:**
   > *"Obsidian sync failed. I've saved the updated Case Brain to your case folder at [path]. You can manually paste the content into Obsidian, or I can try the write again. Whatever you prefer."*

3. **Never lose session data** due to an Obsidian API or filesystem failure. The fallback ensures the updated Case Brain is always preserved somewhere accessible.

### 4H — Confirm Save

Display:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CASE BRAIN SAVED: [Client Name] | [Date]
Session logged. [N] open issues. Next: [top next step]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
