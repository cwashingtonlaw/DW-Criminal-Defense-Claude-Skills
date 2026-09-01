# Computation Rules — La. C.Cr.P. Art. 13 and Date Arithmetic

**MODULE G working reference.** Every Computed Expiry in the Deadline Clock Table must be produced by these rules, and the arithmetic must be shown in the row or its footnote. No silent date math.

---

## Art. 13 — Computation of time (the controlling rule)

In computing any period allowed or prescribed by law or court order:

1. **Exclude the trigger day.** The date of the act, event, or default after which the period begins to run is **not included**. (Arrest on March 10 → day 1 of a 60-day period is March 11.)
2. **Include the last day** — unless it is a **legal holiday**, in which case the period **runs until the end of the next day that is not a legal holiday** (the terminal-holiday extension).
3. **A half-holiday counts as a legal holiday.**
4. **Intermediate legal holidays count** (are included in the period), **except** when:
   - they are expressly excluded by the governing provision;
   - the holiday would otherwise be the **last day** of the period; or
   - the period is **less than seven days** (then holidays are excluded from the count entirely).

## Legal holidays (what counts)

"Legal holiday" is defined by statute — **La. R.S. 1:55** `[VERIFY CITATION — confirm the current R.S. 1:55 holiday list and its parish/clerk-closure provisions before relying]` — and includes **Saturdays and Sundays** for most purposes, statewide holidays (Mardi Gras in some parishes, Good Friday, etc.), and days the clerk's office is closed by proclamation or emergency order. Because the list has parish-specific and emergency components:

- **Terminal weekend rule (practical form):** an expiry that lands on a Saturday, Sunday, or holiday rolls forward to the **next business day** — apply this to every computed expiry and show both dates: `2027-07-23 (Sat) → 2027-07-26 (Mon)`.
- For deadlines under 7 days (rare in this skill's clocks but present in some post-trial windows), compute by **counting only non-holiday days**.
- **Emergency suspensions:** hurricane/emergency orders (statewide or by the Louisiana Supreme Court / local court) can suspend prescriptive periods. If the case window overlaps a known emergency-order period, add a ledger note `[ATTORNEY VERIFY — emergency-order suspension may apply for MM/DD–MM/DD]` rather than silently extending.

## Year-and-month arithmetic

- **Years:** anniversary-date method — a 2-year period from institution on 2025-03-10 expires 2027-03-10 (then apply terminal-day rules). If the anniversary does not exist (Feb 29 start), use Feb 28 of the target year and flag the row.
- **Days:** calendar-day counting per Art. 13 (exclude trigger day, include last day).
- **Suspension addition:** count suspended days as whole calendar days from the suspending filing (exclusive) through the ruling date (inclusive) `[ATTORNEY VERIFY — circuits differ on inclusive/exclusive endpoints for suspension counting; present the count and the two-day sensitivity band]`. Then apply the Art. 580 one-year-minimum comparison BEFORE terminal-day rules.

## Mandatory arithmetic display format

Every computed row must carry (inline or as a lettered footnote):

```
[a] Start: 2025-03-10 (Bill filed — clerk stamp)
[b] Base period: 2 years (Art. 578(A)(2)) → 2027-03-10
[c] Suspensions: +135 days (MTS pending 9/2/25–1/15/26) → 2027-07-23
[d] Art. 580 minimum: ruling 1/15/26 + 1 yr = 2027-01-15 → keep [c] (later)
[e] Terminal-day check: 2027-07-23 = Friday, no holiday → FINAL: 2027-07-23
```

## Uncertainty handling

- Any input date the file does not document → the row is **NEEDS-DATA**. Never estimate, never use "approximately," never borrow a date from an unsourced narrative.
- Two sources conflict on a date → compute BOTH, show both expiries, flag `[CONFLICT — attorney resolve]`, Status NEEDS-DATA.
- When arithmetic lands within **30 days** of today in either direction, add a **⚠ MARGIN** marker — these are the rows attorneys need at the top of the table.
