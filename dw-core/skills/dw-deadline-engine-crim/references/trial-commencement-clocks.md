# Trial-Commencement Clocks — La. C.Cr.P. Arts. 578–583

**MODULE C working reference.** These clocks limit how long the State has to *commence trial* after institution of prosecution. Remedy for expiry: **motion to quash under Art. 581** (dismissal + bar on reprosecution) — NOT release. Keep this remedy lane separate from Art. 701 (remedy = release) in every output.

---

## Art. 578 — The general rule

No trial shall be commenced (nor any bail obligation be enforceable):

| Case class | Limit (from date of INSTITUTION of prosecution) |
|---|---|
| Capital cases | **3 years** |
| Other felony cases | **2 years** |
| Misdemeanor cases | **1 year** |

- **The offense charged determines the applicable limitation** (Art. 578(B)). An amended bill can change the class — recompute on any amendment and record both versions.
- Start event: **date of institution** (indictment returned / bill filed), NOT arrest. Source the filing date from the clerk-stamped instrument or minutes.
- "Commenced": trial commences for these purposes when the first prospective juror is called for examination (jury) or the first witness is sworn (bench) `[VERIFY CITATION — commencement definition lives in La. C.Cr.P. Art. 761; confirm text before relying]`.

## Art. 579 — Interruption (clock restarts anew)

The Art. 578 period is **interrupted** if:

1. The defendant, with purpose to avoid detection, apprehension, or prosecution, **flees the state, is outside the state, or is absent from his usual place of abode** in the state; or
2. The defendant **cannot be tried** because of insanity, or because his presence cannot be obtained by legal process, **or for any other cause beyond the control of the state**; or
3. The defendant **fails to appear at any proceeding pursuant to actual notice, proof of which appears of record**.

Effect: the period **runs anew** (full period, not the balance) from the date the cause of interruption no longer exists.

**Failure-to-appear special rule (later amendment):** where the defendant failed to appear and is later arrested, the period does **not** begin anew until the defendant appears in person in open court in the pending case, or the prosecuting DA has **notice of the defendant's custodial location**. Defense audit angle: if the client sat in another parish's jail while the DA had notice (detainer, teletype, transfer order), the anew-start may be earlier than the State claims — source the notice document.

**Burden:** once the defense shows the Art. 578 period facially expired, the **State bears the burden** of proving an interruption (or sufficient suspension). Log every fact the State would rely on, with its source.

## Art. 580 — Suspension by preliminary pleas (clock pauses + minimum period)

**(A)** When the **defendant** files a motion to quash **or other preliminary plea** (motions to suppress, motions for continuance filed by the defense, applications for discovery and bills of particulars have all been treated as suspending pleas — attribution matters), the Art. 578 period is **suspended until the ruling of the court thereon**; **but in no case shall the State have less than one year after the ruling to commence trial.**

The minimum-period rule means the computed expiry after a defense preliminary plea is:

```
Expiry = LATER OF:
  (a) original Art. 578 expiry + number of days suspended, or
  (b) ruling date + 1 year
```

**(B)** The Art. 578 periods are also suspended when the court grants a continuance under **Art. 709(B)** (material-witness continuance) `[VERIFY CITATION — confirm Art. 580(B) cross-reference and Art. 709(B) content before relying]`.

**Attribution rules for the ledger:**

- **Defense-filed** preliminary pleas and defense continuance motions → suspension (with the 1-year minimum tail from the ruling).
- **Joint continuances** → treated as suspension attributable to the defense in most circuits — flag for attorney confirmation in the case's circuit before counting against the State.
- **State continuances and court-initiated resets** → generally do NOT suspend Art. 578 (unless they qualify as an Art. 579 cause beyond the State's control). These are where clocks actually die — log them precisely.
- Every continuance row needs: date, mover (defense / State / joint / court), minute-entry citation, and new setting.

## Art. 581 — The remedy: motion to quash

Upon expiration of the limitations in this Chapter (institution clocks AND trial clocks):

- The court **shall dismiss the indictment** upon **motion of the defendant filed prior to trial** — the right is **waived** if not raised before trial.
- If dismissed under this article, **no further prosecution for the same or a lesser offense based on the same facts** is permitted.

Audit-mode output: when a clock shows EXPIRED-MOVE, the deliverable routes to `dw-pretrial-motion-library-crim` for the motion to quash, with this skill's computed arithmetic attached as the factual exhibit.

## Art. 582 — New trial / mistrial resets

When the defendant obtains a **new trial** (motion for new trial, appeal, post-conviction relief, or any other mechanism) **or when there is a mistrial**, the State must commence the second trial within:

- **1 year** from the date the new trial is granted or the mistrial is ordered, **or**
- the Art. 578 period, **whichever is longer.**

If the State seeks review of the new-trial grant, the period does not commence until the judgment granting the new trial is **final after the State exhausts review** (including the Louisiana Supreme Court).

## Art. 583 — Interruption of the Art. 582 period

The Art. 582 period is interrupted by any Art. 579 cause; upon cessation, the State must commence the new trial within **1 year** from the date the cause of interruption no longer exists.

---

## Worked arithmetic pattern (show this in every computed row)

```
Clock: Trial commencement (Art. 578 — felony, 2 years)
Institution: 2025-03-10 (Bill of Information, minutes p. 1)
Base expiry: 2027-03-10
Suspension: defense MTS filed 2025-09-02, ruled 2026-01-15 (135 days)
  (a) 2027-03-10 + 135 days = 2027-07-23
  (b) ruling 2026-01-15 + 1 year = 2027-01-15
Computed expiry = LATER of (a),(b) = 2027-07-23  → then apply Art. 13 terminal-day rules
Status: RUNNING
```
