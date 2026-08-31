# Objection Log Schema and Missed Objection Sub-Log (Module B)

Read at **MODULE B — Real-Time Objection Log** of `SKILL.md`; field-by-field row formats that match `dw-appellate-error-monitor-crim` MODULE A / MODULE B.

### Objection Log Row Format (matches dw-appellate-error-monitor-crim MODULE A schema)

| Field | Content | Notes |
|---|---|---|
| Obj. # | Sequential — `Obj-001`, `Obj-002` | Counter resets per case, NOT per day |
| Day | Trial day number | For roll-up |
| Time | Contemporaneous timestamp (`10:42 AM`) | Required even when transcript page is later filled in |
| Transcript Page/Line | `(T. Vol. __, p. __, ll. __)` if known; else blank with timestamp | Filled in once transcript is delivered |
| Phase | Voir dire / opening / State case / defense case / rebuttal / closing / instructions / sentencing | |
| Objecting Party | Defense / State | |
| Subject | One-line description of trigger (e.g., "State asked Sgt. Doe to recount what dispatch told him") | Not prose — a single line |
| Type of Objection | Hearsay / relevance / foundation / 404B / Crawford / leading / speculation / opinion / argumentative / asked-and-answered / cumulative / vague / compound / improper closing / etc. | See `references/objection-cheat-sheet.md` |
| Legal Basis Cited | Specific rule cited in real time (e.g., `La. C.E. Art. 802 — hearsay; no exception`) | The grounds counsel actually stated |
| Specificity Assessment | Yes / Partial / No — was the ground specific enough to satisfy Art. 841? | Critical for preservation |
| Court's Ruling | Sustained / Overruled / Deferred / No ruling / Sustained in part | |
| Curative Instruction Requested? | Yes / No | |
| Curative Instruction Given? | Yes (text or summary) / No / N/A | |
| Proffer Made? | Yes / No / N/A (if not an exclusion ruling) | If excluded and no proffer, FLAG |
| Continuing Objection? | Yes (scope) / No | Capture exact stated scope |
| Preservation Status | PRESERVED / PARTIALLY / WAIVED / TBD | TBD until transcript verified |

### Missed Objection Sub-Log (MO-###)

Run a parallel log for objections counsel intended but did not make. Schema matches `dw-appellate-error-monitor-crim` MODULE B:

| Field | Content |
|---|---|
| MO-# | Sequential — `MO-001` |
| Day | |
| Time | Contemporaneous (`11:14 AM`) |
| Transcript Location | Filled later |
| What Happened | One-line description of the objectionable event |
| What Objection Should Have Been Made | Type + legal basis (e.g., "404B — prior bad act, no Prieur notice") |
| Why It Was Objectionable | One-line legal flag |
| Why It Wasn't Made | Strategic choice / didn't catch in time / believed waived by prior ruling / other |
| Salvage Pathway | Errors patent (Art. 920) / structural / IAC (post-conviction) / Brady / N/A |
| Prejudice | Critical / Significant / Minor / De minimis |
