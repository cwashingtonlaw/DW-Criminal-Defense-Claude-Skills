# Witness Priority Rubric (1–5)

Daniels & Washington standard for ranking every witness on the **Witness List** sheet of `Case Tables.xlsx` by importance to the case outcome. This rubric is the single source of truth for the `Priority (1–5)` column. Apply it identically on every case so rankings are reproducible and defensible.

The ranking is **defense-theory-driven**: a witness's importance is measured by how much their testimony helps or hurts the defense theory of the case (from the Case Profile / Report 4 selected theory) and the elements the State must prove. Read the selected defense theory FIRST, then rank.

---

## Method: First-Match Decision Rule

Evaluate each witness against the tiers **in order, 1 → 5, and assign the FIRST tier the witness satisfies.** Do not average. If a witness plausibly fits two tiers, the first match (lower number = higher priority) wins, subject to the modifiers below.

The `Priority (1–5)` cell is written as a number + label: `1 – Critical`, `2 – High`, `3 – Medium`, `4 – Low`, `5 – Peripheral`.

### 1 – Critical (case-determinative)
Assign 1 if the witness is any of:
- The **defendant**.
- An **eyewitness to the charged act** (saw the offense conduct itself).
- The witness whose account is the **linchpin of the defense theory** (e.g., the surviving narrator who establishes the victim was the armed aggressor in a self-defense case).
- A **co-defendant** whose statement implicates or exculpates the defendant (*Bruton* / *Giglio* exposure).
- The **lead forensic witness on the central contested fact** (e.g., the autopsy pathologist on trajectory; the analyst whose result decides identity or causation).

### 2 – High (strongly probative / contested)
Assign 2 if not already 1 and the witness is any of:
- The **lead or case detective(s)** who took key statements or authored the core investigative report.
- A **forensic analyst on a contested item** (DNA, latent prints, ballistics, tox) whose result bears on a disputed issue.
- A **near-scene witness** who heard or partially observed the act.
- An **expert the defense will challenge** under *Daubert* / *Foret*.
- The **guardian/custodian of a minor eyewitness** to the core events.

### 3 – Medium (material corroboration)
Assign 3 if not already 1–2 and the witness is any of:
- A **secondary fact or ear-witness** (heard shots, saw aftermath, places people in time/space).
- A **timeline corroborator**.
- A **scene officer** who collected, logged, or photographed key evidence.
- An **assisting (non-lead) detective** with a documented substantive role.
- A **records witness whose records are contested**.

### 4 – Low (foundation / likely stipulable)
Assign 4 if not already 1–3 and the witness is any of:
- A **routine responding or assisting officer**.
- A **booking officer, evidence-room custodian, or records/E911 custodian**.
- A **chain-of-custody-only** witness.
- Any witness needed solely to admit a document or item that will likely be stipulated.

### 5 – Peripheral / Minimal
Assign 5 if not already 1–4 and the witness is any of:
- **Summoned but unlikely to be called**, or **cumulative/duplicative** of a higher-ranked witness.
- A **subpoena service-recipient officer** with no substantive role.
- The **deceased victim** (no live testimony) — proof about the victim is developed through the expert/records witnesses.
- **Relevance unconfirmed pending discovery** — assign `5 (prov.)` and re-rank when a transcript/report identifies the role.

---

## Modifiers (apply after the base tier)

1. **Two-tier fit:** take the higher tier (lower number).
2. **Impeachment / Brady-Giglio bump:** if the witness carries significant impeachment value or known *Brady*/*Giglio* material, move them **one step toward 1** (e.g., a 3 with a cooperation deal becomes a 2).
3. **Provisional flag:** if the role is not yet confirmed (transcript/report outstanding), append `(prov.)` to the label and revisit at every discovery supplement.
4. **Defense vs. State:** the tier reflects importance to the **case**, regardless of who called the witness. A State-listed officer who saw the victim draw first can be a 1; a defense-listed character witness is usually a 4.

---

## Procedure (how to rank a full list)

1. Load the **selected defense theory** (Case Profile / Report 4a). Note the contested elements and the facts the theory turns on.
2. For each witness, gather: role, what they observed/analyzed, the Bate refs of their statement/report, and any impeachment/Brady flags.
3. Apply the **first-match rule** to set the base tier, then the **modifiers**.
4. Write `Priority (1–5)` as `N – Label` and capture the one-to-two-sentence justification in **Priority Rationale**, naming the specific defense-theory connection.
5. Sort the sheet **alphabetically by Last, First** (Priority remains a sortable column).
6. Re-run this rubric whenever a new transcript, lab report, or discovery supplement changes what a witness offers.

---

## Worked Example — State v. Drake (self-defense)

Theory: defendant fired only because he believed the deceased was about to shoot him.

- **1 – Critical:** Drake (defendant); Brignac & Curtis (co-defendants, *Bruton*/*Giglio*); Tobias (surviving narrator — victim armed, "handle business"); McClain, MD (pathologist — trajectory); K. Ellender (coroner ME — wounds).
- **2 – High:** Det. Johnson (lead) & Det. Randolph (key interviews); Cooley (scene/ballistics) & Mixon (homicide casings); Alexander (DNA on the gun — *modifier: contested*) ; Corbello (latent prints on the gun); Rubin c/o minor O.H. (backyard aggressor sequence).
- **3 – Medium:** Ford (first responder, res gestae); Cole, the Poullards, Green (ear/near-scene); scene detectives.
- **4 – Low:** routine LCP responders; Rachal (E911 custodian).
- **5 – Peripheral:** subpoena service-recipient officers; Ware (deceased victim); civilians whose relevance is unconfirmed (`5 (prov.)`).

---

*Daniels & Washington — Witness Priority Rubric. Consumed by `dw-criminal-defense-crim` (Witness List build, Phase 1 Step 4 / Phase 3 Step 2). Cross-checked by `dw-witness-threat-matrix-crim`, which scores cross-examination danger (Damage × Vulnerability) on a separate axis — the two are complementary, not interchangeable.*
