# Case Context Load (Step 0.6)

Read at Step 0.6 — sub-steps 0A (identify the case folder), 0B (load the Case Brain), and 0C (confirm scope), verbatim.

---

### 0A — Identify the Case Folder

The case folder is either:
- Already mounted in the Cowork workspace (check `/sessions/.../mnt/` for the case folder)
- Specified by the attorney ("build the trial notebook for Tezeno")

If no case folder is evident, ask:
> *"Which case are we building the trial notebook for? I need the case folder mounted or the client name so I can locate it."*

### 0B — Load the Case Brain

Read the Case Brain from the Obsidian vault (follow `dw-case-brain-crim` environment detection —
in Cowork, use the mounted `DW-CASE BRAINS` folder; in Claude Code, try MCP first).

From the Case Brain, extract:
- Client name and docket number
- Current phase (should be Phase 3 or 4 — if earlier, warn the attorney)
- Charges and statutory citations
- Lead attorney
- Trial date (if set)
- `COMPANION SKILL OUTPUTS` section — list of all deliverables already produced by other skills
- `gdrive_path` — for constructing `file://` links
- Theory of defense / case theme

If the Case Brain is not available, proceed with a folder-only scan but warn:
> *"No Case Brain found — I'll scan the folder structure directly, but I may miss deliverables stored outside the case folder."*

### 0C — Confirm Scope

Before scanning, confirm with the attorney:
> *"I'm ready to build the trial notebook for [Client Name] ([Docket #]). I'll scan the case folder, check for all upstream deliverables, organize the Trial Notebook tabs, generate the Master Index, identify gaps, and build your courtroom checklists. Anything specific you want me to focus on or skip?"*

Proceed after confirmation.
