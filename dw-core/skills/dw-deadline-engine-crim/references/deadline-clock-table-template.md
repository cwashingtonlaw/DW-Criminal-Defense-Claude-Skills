# Deadline Clock Table — Output Contract & Templates

**FIXED CONTRACT.** Other skills (`dw-case-dashboard-crim`, `dw-case-brain-crim`, `dw-pretrial-motion-library-crim`, `dw-bond-and-release-motion-crim`) consume this output. Do not change the table schema, the status vocabulary, or the file path pattern without a coordinated cross-skill update.

---

## Deliverable (a) — the Deadline Clock Table file

**Path (verbatim pattern):**

```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Deadlines/YYYY-MM-DD - Deadline Clock Table - {Client}.md
```

`YYYY-MM-DD` is the computation date (today). Each refresh writes a NEW dated file — prior tables are the audit trail; never overwrite or delete them.

**Document structure:**

```markdown
[ATTORNEY WORK PRODUCT marking — per shared protocol]

# Deadline Clock Table — {Client} | {Docket}
**Computed:** YYYY-MM-DD | **Offense date:** YYYY-MM-DD (source) | **Statutory versions applied as of:** offense/prosecution date
**Custody status:** [in custody since DATE (source) / released on bond DATE (source)]

## ⚠ Attention Rows
[Every EXPIRED-MOVE row, every ⚠ MARGIN row (expiry within 30 days), every NEEDS-DATA row blocking a computation — repeated here verbatim from the master table]

## Master Clock Table

| Clock | Statutory Basis | Start Event | Start Date | Interruptions / Suspensions | Computed Expiry | Status |
|---|---|---|---|---|---|---|

## Arithmetic Appendix
[The lettered [a]–[e] computation for every computed row — see computation-rules.md format]

## Event Ledger
[Chronological list of every clock-relevant event used: arrest, institution, each continuance w/ mover + minute cite, each preliminary plea filed/ruled, custody changes — each with source citation]

## Data Gaps
[Every NEEDS-DATA item with the exact document/date needed to close it]

## Referrals
[EXPIRED-MOVE routing — see Audit Mode below]
```

**Master table row conventions:**

- **Clock** — short stable label, one clock per row: `Institution (Art. 572 — 6yr felony)`, `Trial commencement (Art. 578)`, `701(B) institution (felony, custody)`, `701(D) trial (motion filed 3/2/26)`, `MNT — general`, `MNT — new evidence`, `PVJA (Art. 821)`, `Arrest of judgment (Art. 861)`, `Appeal (Art. 914)`, `Reconsider sentence (Art. 881.1)`, `PCR (Art. 930.8)`, `Habitual bill (reasonable time)`.
- **Statutory Basis** — article(s) with subsection, flagged per house rules if unverified.
- **Start Event / Start Date** — event name + sourced date; `NEEDS-DATA` if unsourced.
- **Interruptions / Suspensions** — `None claimed`, or each item as `S: MTS 9/2/25→1/15/26 (+135d, def.)` / `I: FTA 4/1/25, anew from 6/2/25 (Art. 579(A)(3))`; prefix S=suspension, I=interruption; attribution always shown.
- **Computed Expiry** — final date after Art. 13 terminal-day rules, with a bracketed letter pointing to its Arithmetic Appendix entry, e.g. `2027-07-23 [c–e]`. `NO-LIMIT` for Art. 571 rows; event names for event-bound rows.
- **Status** — exactly one of the five vocabulary values below.

## Status vocabulary (closed set — use no other values)

| Status | Meaning |
|---|---|
| `RUNNING` | Clock alive, expiry in the future (or reasonable-time doctrine with no fixed date) |
| `EXPIRED-MOVE` | Deadline passed against the State — a defense motion is available (quash / 701 release / other) |
| `SATISFIED` | The event the clock limited occurred in time (bill filed, trial commenced, motion filed) — record the satisfying event + date |
| `TOLLED` | An interruption/suspension currently holds the clock (defendant absent, plea pending ruling, capacity commitment) |
| `NEEDS-DATA` | A required input date is missing or conflicting — arithmetic not run; never guess |

Defense-side deadlines that lapse (e.g., appeal window missed) are rendered `EXPIRED-MOVE` only when a curative defense motion exists (out-of-time appeal via PCR); otherwise note the lapse in the row and let the attorney classify.

## Deliverable (b) — the `## CLOCK STATUS` block for the Case Brain

Write (via `dw-case-brain-crim`'s read-merge-write protocol — never patch by heading) a section with this exact shape:

```markdown
## CLOCK STATUS
*Last computed: YYYY-MM-DD by dw-deadline-engine-crim — full table: [path to today's Deadline Clock Table file]*

| Clock | Statutory Basis | Start Event | Start Date | Interruptions / Suspensions | Computed Expiry | Status |
|---|---|---|---|---|---|---|
[same rows as the master table — schema identical, arithmetic appendix stays in the file deliverable]

**Attention:** [one line per EXPIRED-MOVE / ⚠ MARGIN / blocking NEEDS-DATA row; "None" if none]
```

If the Case Brain has an existing `## CLOCK STATUS` block, replace the block's contents wholesale with the new computation (the dated table files preserve history). If the Case Brain is unavailable, save the block's text at the end of the table file under `## CLOCK STATUS (pending Case Brain write)` and tell the attorney.

---

## Refresh Mode procedure

Trigger: any new clock-relevant event ("we got a continuance," "the State amended the bill," "he bonded out," "the court ruled on the motion to suppress," "refresh the clocks").

1. Load the most recent Deadline Clock Table file (and the Case Brain CLOCK STATUS block if present).
2. Intake ONLY the new event(s): date, type, mover/attribution, source document. Hard stop until sourced.
3. Append to the Event Ledger; recompute every affected clock from its full event history (never incremental-adjust a stale expiry — recompute from the start date each time).
4. Re-classify statuses; write a new dated table file; rewrite the CLOCK STATUS block.
5. Report the delta to the attorney: which expiries moved, by how many days, and why.

## Audit Mode procedure ("did the State blow the clock?")

1. Run (or refresh) the full computation first — audit conclusions come only from computed rows, never from impressions.
2. For each `EXPIRED-MOVE` row, produce a referral packet in the table's Referrals section:
   - **Arts. 578/581 (or 571–576) expiry** → refer to **`dw-pretrial-motion-library-crim`** for the **motion to quash**; attach the row, its arithmetic appendix entry, and the event ledger. Note the Art. 581 pre-trial waiver rule and the State's burden to prove interruption/suspension.
   - **Art. 701(B) or 701(D) expiry** → refer to **`dw-bond-and-release-motion-crim`** for the **motion for release under Art. 701**; attach arrest date, custody tier, window, expiry, and the just-cause event ledger. Remedy is release, not dismissal — say so in the referral.
   - **Habitual-bill unreasonable delay** → refer to **`dw-habitual-offender-auditor-crim`** with the elapsed-time facts.
3. For near-miss rows (State survived on an interruption/suspension), state exactly which event saved the State and its source — these are the facts to attack at the contradictory hearing.
4. Present a one-paragraph bottom line per clock lane: institution / trial commencement / 701 / post-trial. No motion recommendation without a computed row behind it.
