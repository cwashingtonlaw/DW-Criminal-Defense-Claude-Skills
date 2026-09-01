---
name: dw-deadline-engine-crim
category: core
description: >
  Statutory deadline and clock computation for Louisiana criminal cases. ALWAYS invoke
  for "deadline," "clock," "time limitation," "prescription," "speedy trial," "578,"
  "701," "when does the State's time run," or "compute the clocks." Computes institution,
  trial-commencement, Art. 701, post-trial, appeal, and PCR clocks with full arithmetic.
  Do NOT use for drafting the resulting motions — use dw-pretrial-motion-library-crim
  (quash) or dw-bond-and-release-motion-crim (701 release).
---

# Deadline Engine — Statutory Clock Computation
**Daniels & Washington | Criminal Defense | Louisiana / 5th Circuit Default**

This skill takes the case's clock-relevant dates — offense, arrest, institution of prosecution, custody status, continuances with attribution, preliminary pleas filed and ruled — and computes every statutory clock that runs in a Louisiana criminal case: time limits on institution of prosecution (La. C.Cr.P. Arts. 571–576), time limits on commencement of trial (Arts. 578–583), Art. 701 speedy-trial custody-release windows, post-trial motion deadlines, the Art. 914 appeal delay, Art. 930.8 post-conviction prescription, and the habitual-offender reasonable-time doctrine.

The deliverable is a **Deadline Clock Table** with its arithmetic shown, plus a **CLOCK STATUS** block written into the Case Brain. Two remedy lanes stay strictly separate throughout: **Arts. 578/581 expiry → motion to quash (prosecution dies)**; **Art. 701 expiry → release without bail (prosecution survives)**. This skill computes and refers; motion drafting lives in `dw-pretrial-motion-library-crim` and `dw-bond-and-release-motion-crim`.

---

## STEP 0 — FILE INTAKE HARD STOP (Always First)

**If the user has uploaded or referenced any minute entries, bills of information, indictments, arrest reports, court orders, continuance orders, motion rulings, or other date-bearing case documents, do not compute anything yet.**

Your only response must be:
> *"Before I begin — are you uploading any additional minute entries, charging instruments, arrest or booking records, continuance or scheduling orders, motion rulings, or custody records? Clock arithmetic is only as good as the event ledger, so I'll start computing only after you confirm: 'No more uploads now.'"*

Proceed **only** after the user explicitly confirms no further uploads. If more are coming, acknowledge and wait. This hard stop applies to every new batch of uploads without exception.

**Rationale:** A single late-arriving minute entry — one more continuance, a preliminary plea ruling, a failure-to-appear — can move a computed expiry by months or flip a clock from EXPIRED-MOVE to RUNNING. A table computed on an incomplete ledger is worse than no table.

---

## STEP 0.5 — LOAD SHARED PROTOCOLS

Before producing any deliverable, read `dw-shared-protocols-crim/SKILL.md` and load:

1. `dw-shared-protocols-crim/references/attorney-work-product-marking.md` — apply to the Deadline Clock Table header
2. `dw-shared-protocols-crim/references/output-path-formula.md` — all output paths anchor on `{{CASE_ROOT}}`

Do not proceed until loaded. The Deadline Clock Table is internal work product.

### Source Citation Mandate

Every date in the computation must trace to a specific source document. Clock litigation is won and lost on the documented record — an interruption the State cannot prove, a continuance the defense did not move for. **Every factual assertion — every start date, custody change, continuance, filing, and ruling — must cite its source.**

**Citation format examples:**
- `(Bill of Information — filed 03/10/2025, clerk stamp p. 1)`
- `(Minute Entry 09/02/2025 — defense Motion to Suppress filed)`
- `(Minute Entry 04/14/2026 — continuance on joint motion, reset to 06/08/2026)`
- `(Booking Sheet — CPSO, arrest 01/22/2025)`
- `(Bond Release Order — 02/28/2025)`

**Multiple-source rule:** when more than one document establishes a date, cite all — `(Bill of Information, clerk stamp; Minute Entry 03/10/2025)`.

**Unsourced dates:** a date that cannot be tied to a document is not an input — the affected row becomes `NEEDS-DATA`, marked `[UNSOURCED — VERIFY]`. **The engine never guesses a date.**

---

## STEP 1 — Information Gathering Protocol

**Essential (compute nothing without these):**
1. **Date of offense** — FIRST, always (see Module A). With source.
2. Date of arrest; custody history since (in custody / bonded, with dates and sources)
3. Institution of prosecution: instrument type (indictment vs. bill), filing date, offense(s) charged with statute cites, any amendments
4. Every continuance: date, mover (defense / State / joint / court), minute cite, new setting
5. Every preliminary plea (motion to quash, suppress, discovery, bill of particulars, defense continuance motions): filed date and ruling date
6. Current procedural posture (pretrial / post-verdict / sentenced / on appeal)

**Strategic:** failure-to-appear events and later arrest/notice dates (Art. 579); dismissals and refiles (Art. 576); competency commitments (Arts. 575/579); any filed 701 motion with its affidavit; State's asserted interruption facts; sentencing date and any Art. 881.1 motion; verdict date; habitual-bill filing date.

**Contextual:** charged statute's penalty clause as of offense date (hard-labor classification); parish/circuit (attribution splits); emergency-order periods overlapping the case; co-defendant severance history.

Rank the gaps: anything Essential that is missing becomes a `NEEDS-DATA` row and a line in the Data Gaps section — the computation still runs for every clock whose inputs are complete.

---

## STEP 2 — Analytical Modules

### MODULE A — Offense-Date Discipline & Statute Versioning

**Confirm the date of offense before anything else**, then warn the attorney, verbatim in the deliverable header: time-limit articles are applied **as of the offense/prosecution date** — Arts. 571, 571.1, 572, 573, and 930.8, and La. R.S. 15:529.1, have all been amended over time, and an amendment generally cannot revive a period that had already expired. When the offense predates the current text, pull the historical version before computing; if the applicable version cannot be confirmed, compute under the current text, mark the row `[ATTORNEY VERIFY — statutory version as of offense date]`, and **never fabricate historical statutory values**.

### MODULE B — Institution Clocks (Arts. 571–576)

Compute the prescription-on-institution rows: Art. 571 no-limit offenses, Art. 571.1 delayed-start sex-offense clock, the Art. 572 felony/misdemeanor tiers (6yr / 4yr / 2yr / 6mo) with hard-labor classification, Art. 573 discovery-rule offenses, Art. 574 lesser-included carryover, Art. 575 interruptions, and Art. 576 new-prosecution-after-dismissal windows. One row per differently-classified count. Read `references/institution-clocks.md` now.

### MODULE C — Trial-Commencement Clocks (Arts. 578–583)

Compute the trial clock from institution: Art. 578 tiers (capital 3yr / felony 2yr / misdemeanor 1yr), Art. 579 interruptions (run anew, including the failure-to-appear notice rule), Art. 580 suspensions by preliminary pleas with the **one-year-minimum-after-ruling** comparison, Art. 581 quash remedy and pre-trial waiver, Arts. 582–583 new-trial/mistrial resets. Attribution of every continuance is load-bearing. Read `references/trial-commencement-clocks.md` now.

### MODULE D — Art. 701 Speedy Trial (remedy = release; keep separate)

Compute the custody-release windows: 701(B) institution-after-arrest tiers (custody vs. bond; felony / misdemeanor / capital-or-life), and 701(D) trial windows that run **only after a speedy-trial motion with counsel's readiness affidavit** is filed. Remedy is release without bail or bail discharge absent just cause — these rows never merge with, and never route like, the Art. 578 rows. Read `references/art-701-speedy-trial.md` now.

### MODULE E — Post-Trial, Appeal & PCR Clocks

Compute the defense-side rows: motion for new trial (Arts. 851/853 — before sentence; new-evidence ground 1 year from verdict), post-verdict judgment of acquittal (Art. 821 — before sentence), arrest of judgment (Arts. 859/861 — before sentence), motion for appeal (Art. 914 — 30 days, restarted by an Art. 881.1 ruling), finality, and Art. 930.8 PCR prescription (2 years from finality). Timing only — drafting routes to `dw-pretrial-motion-library-crim`, `dw-appellate-brief-builder-crim`, and `dw-post-conviction-relief-crim`. Read `references/post-trial-appeal-pcr-clocks.md` now.

### MODULE F — Habitual Offender (reasonable-time doctrine)

No fixed prescription: the multiple bill must be filed within a **reasonable time** after the DA has the necessary information — *State v. Muhammad*, 2003-2991 (La. 5/25/04), 875 So.2d 45 `[VERIFY CITATION — attorney to Westlaw-check currency and subsequent treatment]`. Render as RUNNING with elapsed-time facts, never a date-certain expiry; long unexplained delay routes to `dw-habitual-offender-auditor-crim`. Detail in the Module E reference (final section).

### MODULE G — Computation Rules (Art. 13)

All date arithmetic follows La. C.Cr.P. Art. 13: exclude the trigger day, include the last day unless it is a legal holiday (then roll to the next non-holiday — the terminal weekend/holiday rule), holidays excluded entirely from periods under seven days; legal holidays per La. R.S. 1:55 `[VERIFY CITATION — confirm current holiday list]`. Every computed expiry shows its arithmetic in the lettered [a]–[e] format. Read `references/computation-rules.md` now.

---

## STEP 3 — Output Format

Produce, per the fixed contract in `references/deadline-clock-table-template.md` (read it now):

**(a) Deadline Clock Table** saved to:
```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Deadlines/YYYY-MM-DD - Deadline Clock Table - {Client}.md
```
containing the Attention Rows, the Master Clock Table in the exact schema below, the Arithmetic Appendix, the Event Ledger, Data Gaps, and Referrals.

**(b) `## CLOCK STATUS` block** written into the Case Brain via `dw-case-brain-crim`'s read-merge-write protocol, same schema:

```
| Clock | Statutory Basis | Start Event | Start Date | Interruptions / Suspensions | Computed Expiry | Status |
```

**Status vocabulary (closed set):** `RUNNING` / `EXPIRED-MOVE` (deadline passed, defense motion available) / `SATISFIED` / `TOLLED` / `NEEDS-DATA`. Every computed expiry shows its arithmetic; any missing date renders `NEEDS-DATA` — never a guess.

---

## STEP 4 — Refresh Mode

On any new clock event ("we got a continuance," "the court ruled," "he bonded out," "refresh the clocks"): load the latest table, intake only the sourced new events, append to the Event Ledger, **recompute affected clocks from their full history** (never adjust a stale expiry incrementally), write a new dated table file, rewrite the CLOCK STATUS block, and report the delta. Procedure in the template reference.

## STEP 5 — Audit Mode ("did the State blow the clock?")

Compute first, conclude second. For each `EXPIRED-MOVE` row, build the referral packet: **Arts. 578/581 (or 571–576) expiry → `dw-pretrial-motion-library-crim` (motion to quash)**; **Art. 701 expiry → `dw-bond-and-release-motion-crim` (release motion)** — each with the row, arithmetic, and event ledger attached. For near-misses, name the exact event that saved the State and its source. Full procedure in the template reference.

---

## Integration

| Skill | Relationship |
|---|---|
| `dw-case-brain-crim` | **Consumer** — persists/reloads the `## CLOCK STATUS` block across sessions |
| `dw-case-dashboard-crim` | **Consumer** — renders Clock Status from the CLOCK STATUS block |
| `dw-pretrial-motion-library-crim` | Audit-mode referral target: motion to quash (Art. 581); post-trial motion drafting |
| `dw-bond-and-release-motion-crim` | Audit-mode referral target: Art. 701 release motion |
| `dw-habitual-offender-auditor-crim` | Referral on unreasonable multiple-bill delay |
| `dw-post-conviction-relief-crim` / `dw-appellate-brief-builder-crim` | Consume the 930.8 / 914 rows |
| `dw-criminal-defense-crim` | Phase 2 invokes this skill when clock questions surface |

## Guardrails

- **Never guess a date.** Missing or conflicting input → `NEEDS-DATA`, listed in Data Gaps. No exceptions.
- **Never merge the remedy lanes.** 578→quash and 701→release are separate rows, separate referrals.
- **Never apply current statutory text to an older offense without the Module A warning**; never fabricate historical statutory values.
- **Never present a computed expiry without its arithmetic.** Unverifiable math is unusable in a contradictory hearing.
- **Attribution before conclusion:** no clock is declared blown until every continuance and plea is attributed with a minute cite — the State's interruption/suspension case is built from exactly these entries.
- **This skill recommends motions; it never drafts or files them.** Cowork drafts; attorney approves — every output is a draft for attorney review and independent date verification.
- **Prior tables are never overwritten** — each computation is a new dated file.

## Quick References

Reference materials in the `references/` subdirectory:

- **institution-clocks.md** — Module B: Arts. 571, 571.1, 572, 573, 574, 575, 576 — tiers, delayed starts, interruptions, dismissal-refile windows
- **trial-commencement-clocks.md** — Module C: Arts. 578–583 — tiers, interruption vs. suspension, Art. 580 one-year minimum, quash remedy, worked arithmetic pattern
- **art-701-speedy-trial.md** — Module D: 701(B)/(D) windows, custody tiers, motion + affidavit requirement, release remedy, just cause
- **post-trial-appeal-pcr-clocks.md** — Modules E–F: Arts. 851/853, 821, 859/861, 914, 881.1, 930.8, habitual-offender reasonable time
- **computation-rules.md** — Module G: Art. 13 arithmetic, legal holidays, terminal-day rules, arithmetic display format, uncertainty handling
- **deadline-clock-table-template.md** — Step 3–5: the fixed output contract, table schema, status vocabulary, CLOCK STATUS block, Refresh and Audit Mode procedures

---

## Version
Deadline Engine v1.0 — Initial build: institution / trial / 701 / post-trial / appeal / PCR / habitual clocks, fixed Deadline Clock Table contract, CLOCK STATUS Case Brain block, Refresh + Audit modes (August 2026)
