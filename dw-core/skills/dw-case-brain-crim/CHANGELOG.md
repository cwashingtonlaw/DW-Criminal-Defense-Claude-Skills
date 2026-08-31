# dw-case-brain-crim — Changelog

Version history for the Case Brain skill (moved verbatim from `SKILL.md` on 2026-08-30).

### v3.4 (April 2026)
- **Cleanup:** Removed the last residual reference to legacy non-Obsidian storage from the changelog
- Obsidian is — and has been — the sole repository for Case Brains; the skill body is now fully consistent with that fact
- Bumped header version to match the most recent changelog entry (was stuck at 3.2 despite v3.3 having been added)

### v3.3 (April 2026)
- **FIX:** Session close protocol repeatedly failed using obsidian_patch_content with heading-based targeting
- Rewrote entire STEP 4 (SESSION CLOSE) to use **full-document merge-and-rewrite strategy** instead of section-by-section patching
- Session Open now explicitly reads the complete Case Brain (not sections) to support eventual merge at close
- Added new steps 4C–4H: Read Full Document → Merge In-Memory → Write Complete Document → Verify → Fallback
- Added fallback protocol: if Obsidian write fails, save updated Case Brain to Google Drive and notify attorney
- Added guardrail: never use heading-based patching; always read full document, merge changes in-memory, write complete document
- This eliminates data loss from API failures and prevents silent sync errors

### v3.2 (March 2026)
- **FIX:** Obsidian MCP times out in Cowork because there's no local Obsidian app running in the cloud
- Added environment detection (Cowork vs Claude Code) to Step 6A — Cowork now skips MCP entirely and goes straight to mounted filesystem
- MCP is now Claude Code-only; Cowork uses Read/Write/Edit tools on mounted vault
- Updated guardrail from "always try MCP first" to "detect environment first"

### v3.1 (March 2026)
- Added Obsidian MCP server as primary vault access method (Steps 1–4, 6A)
- Corrected vault storage location: iCloud Drive (not Google Drive)
- Added MCP tool mapping table with concrete examples
- Added iCloud vault path for mounted-folder fallback
- Simplified Google Drive detection in Step 6C (parish-based routing, no MCP needed)
- Updated Fallback to trigger only when BOTH MCP and mounted folder are unavailable

### v3.0 (February 2026)
- Initial skill version with mounted-folder-only vault access
