# Step 6B — Issue Code Status Scan

Read from SKILL.md **Step 6B** — how to read the `Issue Codes` sheet, group and sort Open codes, compute the 30-day stale flag, and the read-only / no-auto-routing rules.

Check `Case Tables.xlsx` for an `Issue Codes` sheet (maintained by `dw-issue-code-tracker-crim` v2.0). The v2.0 taxonomy is 33 codes total — 14 Universal + 8 Homicide + 11 Rape/Sexual Assault — with no gaps in numbering.

**If the sheet does NOT exist:**
- In the dashboard output, render this notice in place of the Issue Code Status block: "⚠️ Issue ledger not yet initialized. Run `dw-issue-code-tracker-crim` to set up."
- Skip the rest of this step. Do not error out — graceful degradation.

**If the sheet exists:**
1. **Count rows by `Status`** column: Open, Addressed, N/A, and total.
2. **Group all rows where `Status = Open`** by category (the prefix of the `Code` column):
   - **Universal** — codes prefixed `U-` (always render this category)
   - **Homicide** — codes prefixed `H-` (render only if at least one homicide code is Open)
   - **Rape/Sexual Assault** — codes prefixed `R-` (render only if at least one R-code is Open)
3. **Within each category, sort Open codes ascending by code number** (so `U-01, U-02, U-03...` reads naturally).
4. **Compute the stale flag for each Open code:**
   - Stale = `Status = Open` AND `(today − Last Updated) > 30 days`
   - Use the user's local timezone.
   - Append `⚠️ STALE` to stale codes in the Open list.
5. **If any stale codes exist**, also render a "Stale Issues Summary" sub-block listing each stale code with its `Last Updated` date and the day count since.
6. **If no Open codes are stale**, omit the stale summary entirely.

**Read-only.** This step never modifies the `Issue Codes` sheet. Updates to the ledger are the job of `dw-issue-code-tracker-crim` exclusively.

**No auto-routing.** Do not auto-suggest running a code's linked skill, even for stale codes. Surface the data; the attorney decides.
