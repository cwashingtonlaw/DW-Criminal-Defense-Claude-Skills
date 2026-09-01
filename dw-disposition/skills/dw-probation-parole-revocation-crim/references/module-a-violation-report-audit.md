# Module A — Violation-Report Audit

Audit the violation report (and the warrant/detainer paperwork behind it) allegation-by-allegation before conceding anything. Build the Allegation Audit Table (template in `output-format-specifications.md`) with a severity rating per allegation: **FATAL / SIGNIFICANT / MODERATE / MINOR / NO DEFICIENCY**.

## A-1. Hearsay-reliance audit

For each allegation, classify the proof source:

| Class | Example | Defense posture |
|---|---|---|
| Officer's personal knowledge | PO personally observed missed check-ins in their own log | Hardest to attack; shift to mitigation |
| Records the officer maintains | Payment ledger, contact chronos | Demand the underlying records, not the summary; audit for gaps/inconsistency |
| Second-hand hearsay | PO recites a police report, a lab fax, an employer's phone call | **Confrontation demand:** insist the declarant testify or the court make a specific on-the-record good-cause finding (Morrissey right #4). No finding = preserved error for the writ. |
| Multi-level hearsay | PO recites what a detective said a witness said | Object to reliability outright; even revocation's relaxed evidence rules require *reliable* hearsay |

**Drug screens deserve their own line:** instant-cup/field tests without laboratory confirmation, missing chain of custody, unnamed cutoff levels, and unproduced litigation packets are classic reliability attacks. Demand the confirmation record (GC/MS or equivalent) and the technician if the screen is the whole case.

## A-2. Staleness audit

- Date each alleged violation against the report date and the warrant date. Months-old conduct suddenly charged only after a new arrest signals the violation report is pretextual packaging for the new charge — argue it in mitigation and as to condition-notice fairness.
- Check the supervision term: conduct alleged **after the term expired** cannot support revocation, and (parole) revocation action initiated after term expiration is void except for a felony conviction committed on parole (La. R.S. 15:574.9). Cross-check expiration math against the `dw-deadline-engine-crim` CLOCK STATUS block if present.
- For probation, confirm the warrant/detainer actually issued **during** the probation term — an Art. 899 warrant issued before expiration can preserve the court's authority past expiration [VERIFY — confirm current interruption/tolling rule and its article placement before briefing].

## A-3. Condition-vagueness and notice attack

- Pull the **signed** conditions form. An allegation that maps to no written condition, or to a condition never signed/acknowledged, fails on Morrissey notice grounds.
- Attack conditions too vague to guide conduct ("maintain suitable employment," "associate with no undesirable persons") as applied — due process requires fair warning of what supervision forbids.
- Special-condition traps: verify a special condition (curfew, no-contact, treatment) was actually **ordered by the court** (probation) or **imposed in the certificate** (parole), not invented in supervision. An officer cannot unilaterally add conditions.
- Delegation problems: conditions that delegate their content wholesale to the officer's discretion are challengeable [VERIFY — confirm Louisiana authority on improper delegation of condition-setting before briefing].

## A-4. Paperwork-integrity audit

- Warrant vs. summons: was custody even authorized? Art. 899 requires reasonable cause for the officer's warrantless arrest — demand the officer's written statement of grounds.
- Notice adequacy: does the written notice identify each violation with conduct, date, and condition number? Anything found beyond the notice is unpreserved for the State.
- Internal inconsistencies among report, chronos, and warrant (dates, condition numbers, alleged facts) — every inconsistency is cross-examination material for Module C.

**Citation discipline:** every audit finding cites the source document per the Source Citation Mandate — e.g., `(Violation Report, 04/12/2026, Allegation 2)`, `(Conditions of Probation form, signed 01/09/2024, Condition 8)`, `(P&P Chrono, entry 03/02/2026)`. Unsourced findings carry `[UNSOURCED — VERIFY]`.
