# Step 1 — Information Gathering Checklist

Collect these items before analyzing any revocation matter. Present missing items as a ranked checklist. If Essential items 1–6 are missing, do not analyze — ask for them first.

## Essential (1–6)

1. **Supervision type** — Probation (sentencing court retains jurisdiction, La. C.Cr.P. arts. 899–901) or parole (Committee on Parole, La. R.S. 15:574.7–574.11)? Some clients are on both simultaneously (split supervision after a partial suspension, or probation on one docket and parole on another) — each track gets its own analysis. **If the client is on bail/bond and the State seeks bond revocation, STOP — route to `dw-bond-and-release-motion-crim` Module H.**
2. **Violation paperwork** — For probation: the violation report / affidavit, warrant or summons under Art. 899, and any rule-to-revoke or motion filed by the State. For parole: the parole officer's violation report, the warrant/detainer ("parole hold"), and any notice of preliminary (prerevocation) or final revocation hearing.
3. **Underlying conviction and sentence** — Charge(s), **date of offense** (controls the governing statutory version — see the versioning protocol in Step 1 of SKILL.md), conviction date, sentence imposed, portion suspended, supervision term and its start/expiration dates.
4. **Conditions of supervision** — The signed conditions-of-probation form or parole certificate. The exact wording of each allegedly violated condition is the raw material for the vagueness and notice attacks in Module A.
5. **Custody status** — In custody on the hold? Detainer lodged on top of a new arrest? Bail set or available (Art. 899 permits bail on a probation-violation arrest)? Days already served in actual custody on the violation (feeds Module D credit math).
6. **Hearing posture and dates** — Preliminary/prerevocation hearing held or waived? Final hearing date? For an in-custody probationer, Art. 900 requires the court to bring the defendant before it within thirty days for the hearing — calendar this immediately.

## Strategic (7–12)

7. **Supervision file / officer chronos** — Field notes, contact logs, prior warnings, delinquency reports. Ordinary discovery rules do not apply of their own force; request them and anchor the request in the Morrissey/Gagnon disclosure-of-evidence right.
8. **Drug-screen documentation** — Instant-cup vs. confirmed lab results, chain of custody, cutoff levels, confirmation method (see Module A audit points).
9. **New-offense materials, if any** — Police report, charge status (arrest only? billed? pending trial?), and the new case's defense counsel and posture (triggers Module F coordination).
10. **Compliance and mitigation record** — Employment, treatment enrollment/completion, fee and restitution payments (and ability to pay — *Bearden*), family obligations, time successfully served on supervision.
11. **Prior violations and sanctions** — Any earlier administrative sanctions under Art. 899.1 / La. R.S. 15:574.7, prior technical revocations (tier position controls the sanction cap in Module B), prior warnings or extensions.
12. **The original plea context** — What the client was told about supervision exposure at the plea; the sentencing transcript's description of conditions.

## Contextual (13–15)

13. **Decisionmaker** — Which judge (probation) or committee panel (parole); known practices on technical violations and treatment alternatives.
14. **State's position** — DA/probation recommendation; whether the State would accept an alternative-sanctions disposition.
15. **Client's goals and constraints** — Treatment willingness, job/family anchor points, immigration exposure (a revocation sentence can carry immigration consequences — route advisement questions to `dw-padilla-advisement-crim`).

## Deadline-engine intake

If a `dw-deadline-engine-crim` CLOCK STATUS block is present in the conversation or the case file, ingest it before analysis: it supplies the supervision-term expiration date, the Art. 900 thirty-day hearing clock, and any writ-return or judicial-review windows already computed. Do not recompute clocks the engine has already established — reconcile and flag discrepancies instead.
