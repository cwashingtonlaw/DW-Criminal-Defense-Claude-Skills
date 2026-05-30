# Chain of Custody at the Lab

This reference is loaded by `dw-crime-lab-auditor-crim` Module F. It covers the **lab-side** chain of custody — from the moment evidence enters the lab through analysis, sub-sampling, storage, and disposition.

**Scope boundary.** The **field-side** chain — collection at the scene, transport to the lab, and any pre-lab custody events — belongs to `dw-chain-of-custody-auditor-crim`. This reference does not duplicate that work. Where a defect is at the boundary (e.g., evidence was delivered to the lab but the field-side delivery log is missing), the audit flags both skills.

---

## 1. The Lab Intake Event

The lab's intake of evidence is the first lab-side custody event. It is also where field-side and lab-side chains meet.

### Required intake documentation

- **Delivery / submission form** — typically completed by the submitting agency, listing items, case number, requested analysis
- **Lab intake log** — entry noting date and time of receipt, the lab employee who received the items, the items received (counted and described), the condition (sealed / unsealed / damaged), and the lab case number assigned
- **Seal verification** — was the evidence sealed in tamper-evident packaging? Was each seal intact on receipt?
- **Photographic documentation** of unusual conditions (damaged seals, leaking containers, unexpected items)

### Audit points

- [ ] Date and time of receipt documented?
- [ ] Receiving lab employee identified by name (not just initials)?
- [ ] Items inventoried at receipt, with counts and descriptions?
- [ ] Seals verified intact, or noted broken?
- [ ] Discrepancies between the delivery form and the received items noted?
- [ ] Any deviation between weight at submission (per the submitting agency) and weight at intake (per the lab)?

A **weight discrepancy at intake** is a classic finding. A patrol officer documents 28.5 g at the scene; the lab intake records 27.9 g. A 0.6 g discrepancy in a 28-gram cocaine case can move the charge across a trafficking threshold. The discrepancy must be explained.

---

## 2. Internal Transfers and Sub-Sampling

Once at the lab, evidence moves between analysts, instruments, and storage locations. Each move is a custody event.

### Sub-sampling

For analysis, the analyst typically removes a representative portion of the bulk evidence — a few hundred milligrams of powder from a 28-gram package; a 1 mL aliquot from a 10 mL blood vial; a single tablet from a pill jar. Sub-sampling must be documented:

- **Date and time** of sub-sampling
- **Analyst name** (not just initials)
- **Mass or volume removed**
- **Description of what was removed and what remained**
- **Reseal documentation** — was the bulk repackaged and resealed after sampling?

### Internal analyst-to-analyst transfers

If a second analyst (e.g., for a confirmation test, or for QA review) handles the evidence, the transfer is a custody event. Each transfer must show:

- Date and time
- Releasing analyst
- Receiving analyst
- Purpose of the transfer

### Audit points

- [ ] Are all sub-sampling events documented with mass/volume removed?
- [ ] Are all internal transfers documented?
- [ ] Are transfers signed (or electronically attributed) by both releasing and receiving analyst?
- [ ] Are mass / volume balances reconciled? (Total bulk = remaining bulk + all sub-samples removed + any consumed in testing)
- [ ] Are there **anonymous handoffs** — periods where the evidence is in lab custody but no specific employee is identified as the custodian?

---

## 3. Storage Conditions

Evidence stored at the lab must be maintained under conditions that preserve integrity.

### Drug evidence (controlled substances)

- Secure storage with dual-access controls (typically two-person sign-out)
- Climate-controlled (temperature, humidity)
- Locked vault or evidence cage with documented access log
- Separation between bulk evidence, working samples, and reference standards

### Blood / urine specimens (toxicology)

- **Refrigerated** (typically 4 °C) or **frozen** (-20 °C or lower for long-term storage)
- Temperature monitoring with logs
- Power-failure / temperature-excursion alerts

### Audit points

- [ ] What are the documented storage conditions for the evidence in this case?
- [ ] Are temperature logs available for the entire storage period?
- [ ] Were there any temperature excursions during storage?
- [ ] How long was the evidence in storage between intake and analysis? Between analysis and trial / disposition?
- [ ] Was the storage location appropriate for the evidence type?

---

## 4. Consumption in Testing — Trombetta / Youngblood

Some testing consumes the sample. A small drug sample is fully consumed by GC/MS; a small blood sample is consumed by headspace GC plus confirmation. When the evidence is consumed in testing, two defense-side rules apply:

### Sample preservation

Best practice and (in some jurisdictions) legal requirement: **the lab should preserve an aliquot for defense testing whenever feasible**. La. R.S. 32:663 and related Louisiana provisions establish defendant rights to preserved-sample independent testing in some contexts (**VERIFY CURRENT**).

### Trombetta / Youngblood

If the State consumes evidence without preservation, the defense may have a due-process / spoliation argument:

- **California v. Trombetta, 467 U.S. 479 (1984)** — due process requires preservation of evidence that "possesses an exculpatory value that was apparent before the evidence was destroyed" and "of such a nature that the defendant would be unable to obtain comparable evidence by other reasonably available means"
- **Arizona v. Youngblood, 488 U.S. 51 (1988)** — when the evidence is only "potentially useful" (not clearly exculpatory), the defendant must show **bad faith** by the State

In a forensic-lab consumption context, *Trombetta* arguments succeed only rarely (the State's analysis itself is admissible; the defense lacks an independent test). But the consumption is fully fair game for cross-examination on the defendant's inability to independently verify.

### Louisiana Code of Evidence Article 1004

La. C.E. Art. 1004 addresses admissibility of evidence when the original is lost or destroyed. In a lab-consumption context, the State will typically argue that the lab report is the best-available evidence and that the destruction was not in bad faith. Audit:

- [ ] Was the consumption necessary, or was a non-destructive method available?
- [ ] Was the defense notified of the planned consumption in time to request independent testing?
- [ ] Was an aliquot preserved as a matter of routine?

---

## 5. Disposition / Disposal

After analysis, the evidence is either:

1. Returned to the submitting agency for storage / trial use
2. Retained at the lab for further analysis or as reference
3. Destroyed per agency policy (typically after appeals are exhausted)

Each disposition is a custody event. **Premature destruction** — destruction before appeals are exhausted or before defense testing has occurred — is a significant finding.

### Audit points

- [ ] What is the documented disposition of each item?
- [ ] Was any item destroyed during the pendency of the case?
- [ ] If destroyed, was defense counsel notified in time?
- [ ] Is the residue of consumed samples (instrument vials, GC vials) retained, and for how long?

---

## 6. Documentation Standards

A defensible lab-side chain produces:

- A **single integrated chain document** showing every event, every actor, every date/time
- **Continuous custody** — no unexplained gaps
- **Reconciled quantities** — masses and volumes balance
- **Signed (or electronically attributed) transfers** at every step
- **Storage logs** showing temperature, security, access

A **fragmented chain** — events documented across multiple disconnected forms, with custodial gaps and unattributed handoffs — is a common defense target.

---

## 7. Common Chain-of-Custody Defects at the Lab

1. **Anonymous handoffs.** The intake form names the receiving lab employee; the storage log lists "evidence vault"; the analyst worksheet picks up the chain at the start of analysis. The interval between intake and analysis has no specifically-identified custodian. Cross-examine the lab's witness on who specifically had access during this interval.

2. **Undocumented sub-samples.** The analyst's worksheet states "0.5 g removed for analysis" but no sub-sample receipt or balance reconciliation is in the file. Demand the bench notes, balance printouts, and any reseal documentation.

3. **Seal break without log entry.** Tamper-evident seals are designed to be broken once for sub-sampling and then resealed (with the date and analyst's initials over the new seal). Audit photographs of the resealed evidence. Multiple unexplained seal-break events suggest improper access.

4. **Weight / volume discrepancies.** Reconcile every quantity in every document. A discrepancy that crosses a charging threshold is critical.

5. **Refrigeration / freezer gaps.** Temperature logs with gaps, or documented temperature excursions, undermine the integrity of blood / urine samples especially.

6. **Premature destruction.** Evidence destroyed before appeals are exhausted, before defense testing, or before the case is fully resolved.

7. **No preserved aliquot for defense testing.** The State consumed the sample without preserving a portion for the defense, despite statutory entitlement or best-practice norms.

8. **Mixed-batch contamination risk.** Multiple defendants' samples analyzed in the same batch without proper sequencing, blanks, or carryover controls. (This overlaps with Module A/B methodology audit but the chain-of-custody record is what shows the batch composition.)

9. **Late-arriving "additional" evidence.** Evidence that surfaces at the lab without a documented field-side delivery — flag for `dw-chain-of-custody-auditor-crim` to investigate the missing field-side link.

10. **Loss / spoliation.** Evidence reported as misplaced, unable to be located, or accidentally destroyed.

---

## 8. La. Brady Obligations on Chain Documents

Chain-of-custody irregularities at the lab are *Brady* material when they would tend to undermine the State's case. Examples include:

- Documented seal-break events without explanation
- Weight discrepancies between submission and intake
- Temperature excursions during sample storage
- Internal lab quality findings (nonconformances) involving the specific evidence or batch
- Mixed-batch contamination risk identified internally
- Premature or unauthorized destruction events

If the lab has not produced complete chain documentation, the audit's finding is the failure to produce — and the discovery demand follows.

---

## 9. Boundary with `dw-chain-of-custody-auditor-crim`

This skill's lab-side audit is paired with `dw-chain-of-custody-auditor-crim`'s field-side and overall audit. Coordinate as follows:

- **`dw-chain-of-custody-auditor-crim`** owns: collection at the scene; field documentation; transport from the scene to the agency or lab; agency evidence-room intake; transfer from agency evidence room to lab; cross-evidence-type chain issues; the integrated chain narrative across all custody phases.
- **`dw-crime-lab-auditor-crim` Module F** owns: lab intake event; lab internal custody; sub-sampling; storage at the lab; consumption in testing; lab disposition; lab-specific Brady issues.

When the audit identifies a defect at the boundary (e.g., the lab intake form contradicts the submitting officer's delivery log), both skills are flagged. The auditor report notes the boundary and indicates that `dw-chain-of-custody-auditor-crim` should also be invoked for the integrated chain analysis.

---

## 10. Discovery Demand Checklist — Lab-Side Chain

- [ ] Lab intake log entries for all items in this case
- [ ] Lab delivery / submission forms from the submitting agency
- [ ] Lab case file with bench notes for each analyst who touched the evidence
- [ ] All sub-sampling records with mass / volume documentation
- [ ] Internal lab transfer records
- [ ] Storage location log with date / time of every move
- [ ] Temperature monitoring records for refrigerated / frozen storage
- [ ] Evidence-vault access logs for the relevant period
- [ ] Disposition records (destruction, return, retention)
- [ ] Photographs of evidence at intake and after analysis (where taken)
- [ ] Any nonconformance reports involving the evidence batch
- [ ] Notice records — was defense counsel notified of planned consumption or destruction?

---

## 11. Audit Findings — Severity Mapping

| Finding | Severity |
|---|---|
| Unexplained gap in custody — no documented custodian for a defined period | SIGNIFICANT (CRITICAL if combined with seal-break or quantity discrepancy) |
| Weight discrepancy crossing a charging threshold | CRITICAL |
| Seal broken without log entry | SIGNIFICANT |
| Temperature excursion during storage of blood / urine | SIGNIFICANT |
| Sample consumed without preservation of defense aliquot | CRITICAL in jurisdictions with statutory preservation right; SIGNIFICANT otherwise |
| Evidence destroyed before appeals exhausted | CRITICAL |
| Anonymous handoff between intake and analysis | SIGNIFICANT |
| Sub-sampling undocumented | SIGNIFICANT |
| Documentation otherwise complete and reconciled | INFORMATIONAL — credit for credibility |

---

*Last updated: see SKILL.md version. Mark any specific statutory provision (e.g., La. R.S. 32:663, La. C.E. Art. 1004) `[VERIFY CURRENT]` before filing.*
