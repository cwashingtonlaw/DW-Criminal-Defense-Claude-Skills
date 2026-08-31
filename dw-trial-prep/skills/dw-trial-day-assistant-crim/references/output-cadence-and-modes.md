# Output Cadence Table and Mode Detection Table

Read at **STEP 2 — Output Cadence** of `SKILL.md` (cadence table) and again at **Mode Detection** (mode table).

## Output Cadence

| When | What | Length | Format |
|---|---|---|---|
| Morning, before court | Module A — Daily Docket | One page max | Bullet list / small table |
| Rolling, all day | Module B — Objection Log | One row per objection | Table |
| After each witness done | Module C — Witness Scorecard | Half-page per witness | Bullets, no prose |
| Rolling, all day | Module D — Exhibit Tracker | One row per exhibit | Spreadsheet table |
| Rolling, all day | Module E — Juror Observation | Brief notes | Bullet list |
| As issues arise | Module G — Issue Spotter | One short flag per issue | Alert format |
| End of day | Module F — Recap + Tomorrow Prep | One page | Structured memo (only longer output) |

## Mode Detection

| Mode | Triggers | Output |
|---|---|---|
| **Day Setup** | "today's docket," "trial day [N] start" | Module A only |
| **Live Logging** | "log this," "objection," "exhibit," "juror," "issue" | Single-row append to relevant module |
| **Witness Debrief** | "scorecard for [witness]," "witness recap" | Module C single witness |
| **End of Day** | "EOD memo," "wrap up Day [N]," "tomorrow prep" | Module F + snapshots of B-E |
| **Issue Spot** | "is this a 770?," "Brady flag," "mistrial trigger" | Module G alert |
