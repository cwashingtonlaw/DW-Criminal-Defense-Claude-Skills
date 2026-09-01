# Art. 701 Speedy Trial — Custody-Release Clocks

**MODULE D working reference.** Art. 701 is a **release** statute, not a dismissal statute. Its remedy is release without bail (or discharge of the bail obligation) — the prosecution itself survives. Never merge these rows with the Art. 578 rows: a case can be perfectly alive under Art. 578 while the client is entitled to release under Art. 701, and vice versa.

| Lane | Statute | Remedy |
|---|---|---|
| Trial-limitation lane | Arts. 578–583 | Quash — prosecution dies (Art. 581) |
| Speedy-trial lane | Art. 701 | Release without bail / bail obligation discharged — prosecution survives |

---

## 701(B) — Institution-of-prosecution windows (run from ARREST)

When the defendant is **continued in custody** after arrest, the indictment or information must be filed within:

| Held for | In custody | Not in custody (on bail) |
|---|---|---|
| Misdemeanor | **45 days** of arrest `[VERIFY CITATION — one secondary source reports 30 days for this cell; Westlaw-check the current text of Art. 701(B) before filing]` | **90 days** of arrest |
| Felony (non-capital/non-life) | **60 days** of arrest | **150 days** of arrest |
| Felony punishable by death or life imprisonment | **120 days** of arrest (indictment) | — |

**Remedy:** failure to institute within these windows results, upon hearing (contradictory with the DA), in **release without bail** or **discharge of the bail obligation** — unless the State shows **just cause**. Release under 701(B) does NOT bar the State from later instituting prosecution within the Arts. 571–576 limits; it only ends the pretrial detention.

**Start event:** date of **arrest** (not booking or 72-hour hearing). Source it from the arrest report or booking sheet. Custody status must be sourced and dated — a client who bonded out mid-window changes tiers.

## 701(D) — Trial windows after a filed speedy-trial motion

These windows are triggered **only by filing a motion for speedy trial**; they do not run automatically. The motion must be accompanied by an **affidavit of defendant's counsel certifying that both the defendant and counsel are prepared to proceed to trial** — a 701(D) motion filed without genuine trial readiness is a strategic error; confirm with the attorney before recommending one.

After the motion is filed, trial must commence within:

| Charge | In custody | Not in custody |
|---|---|---|
| Felony | **120 days** | **180 days** |
| Misdemeanor | **30 days** | **60 days** |

**Remedy:** failure to commence within the window results in **release without bail** or **discharge of the bail obligation**, absent **just cause**.

**Ledger rule:** if no 701(D) motion has been filed, render the 701(D) row as `NEEDS-DATA — no speedy-trial motion filed; window not running` (this is a strategic option to surface, not a running clock).

## "Just cause"

Just cause means grounds **beyond the control of the State or the court**. Defense-attributed continuances and defense preliminary pleas will generally be charged as just cause; State continuances and docket congestion are the contested ground. Log every delay event with attribution so the just-cause fight is documentable.

## Referral on expiry

When a 701 window shows **EXPIRED-MOVE**:

- Route to **`dw-bond-and-release-motion-crim`** for the motion for release under Art. 701, attaching this skill's computed arithmetic (arrest date, window, custody tier, expiry, no-just-cause facts).
- Do NOT route 701 violations to the motion-to-quash lane — wrong remedy.

## Interaction notes

- 701(B) and the Arts. 571–576 institution clocks both start pre-institution but measure different things (days-from-arrest vs. years-from-offense) with different remedies. Both get their own rows.
- A defendant released under 701 remains subject to the 578 trial clock; a 578 quash moots the 701 rows — mark them SATISFIED with a note, never delete history.
