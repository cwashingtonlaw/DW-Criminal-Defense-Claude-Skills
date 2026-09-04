# Case Tables Write Protocol

**CRITICAL:** Google Drive sync can silently overwrite changes to `Case Tables.xlsx` if the file is open in Excel, Google Sheets, or any other application on another device. To prevent data loss, **ALWAYS follow this protocol before writing to any sheet in `Case Tables.xlsx`** — including Evidence Table, Witness List, Timeline, and any future sheets.

## Pre-Write Warning

Before modifying any sheet in `Case Tables.xlsx`, alert the attorney with this exact message:

> "I need to update Case Tables.xlsx. **Please close it in Excel, Google Sheets, or any other application before I proceed.** Google Drive sync can overwrite my changes if the file is open elsewhere. Confirm when it's closed."

## Wait for Confirmation

Do not proceed to write until the attorney explicitly confirms the file is closed. Accept confirmations like:
- "closed"
- "go ahead"
- "it's closed"
- "ready"
- Any other affirmative confirmation that the file is no longer open

## Write the Changes

Once confirmed, perform the update to `Case Tables.xlsx`.

## Post-Write Verification

After writing, instruct the attorney:

> "Update complete. Please open Case Tables.xlsx and confirm you can see [specific sheet name and change description]. If the change isn't visible, let me know and I'll reapply it."

## Retry Protocol — If Changes Disappear

If the attorney reports the change is missing:
1. Ask them to close the file again
2. Re-read the current state of `Case Tables.xlsx` (it may have been overwritten by sync)
3. Reapply the changes
4. Verify again using the Post-Write Verification message above

## Guardrail

**Never write to `Case Tables.xlsx` without first warning the attorney to close the file and waiting for confirmation.** Google Drive sync conflicts can silently overwrite changes, causing lost work.
