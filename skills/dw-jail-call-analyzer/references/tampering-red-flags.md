# Tampering & Obstruction Red-Flag Catalog

Used by `dw-jail-call-analyzer` Module D. Provides the pattern catalog for witness tampering, witness intimidation, evidence tampering, and obstruction-of-justice exposure surfaced from recorded jail calls.

## Why This Module Carries Independent Weight

Tampering exposure is not just a trial-strategy concern. Substantively, witness contact from a recorded jail call can:

1. Generate **new charges** under La. R.S. 14:129.1 (intimidating a witness) or federal 18 U.S.C. § 1512 if any phone leg crosses state lines or implicates a federal proceeding
2. Generate **bond revocation** — most pretrial release orders in Louisiana state and federal courts include "no contact" conditions covering victims and witnesses; a recorded violation is enough
3. Generate **sentencing enhancements** — obstruction-of-justice enhancements add levels under federal sentencing guidelines and provide aggravating-factor support in Louisiana sentencing
4. **Destroy** any plea-bargain leverage the defense had and dramatically harden the prosecutor's posture
5. Drag the recipient (the relay person) into the indictment as a co-conspirator

Therefore: any CRITICAL Module D finding gets verbal counsel notification before the audit document is finalized.

## Direct vs. Relay vs. Three-Way

### Direct Contact

Client calls a witness's number directly. Always traceable. Vendor records both sides. The State will subpoena the witness's phone records to corroborate.

If the call connects: full Module D analysis applies. If the witness refuses the call or the system blocks it: the attempt itself is logged and is admissible to show intent.

### Relay Contact

Client calls a relay person (typically a family member or friend) who then conveys a message to a witness. The vendor records the client's side; the relay leg is unrecorded but the State may pursue the relay person under conspiracy / accomplice theories.

The relay-contact pattern is harder to charge but easier to prove because the relay is captured verbatim on the call. Look for:

- "Tell [witness name] that..."
- "Make sure [witness] knows..."
- "When you see [witness], let them know..."
- "Get word to [witness] about..."
- Open-ended requests that imply relay ("can you talk to her for me about that thing")

### Three-Way Contact

Vendor systems detect and usually block three-way connect attempts. Even an attempted three-way is evidence of intent. Securus, GTL/ViaPath, and NCIC all log three-way detect events; the log entries appear in the call detail record even when the call was blocked before the third party connected.

A pattern of repeated three-way attempts to numbers associated with witnesses is a CRITICAL flag regardless of whether any individual call connected.

## Red-Flag Patterns

### Pattern 1: Leave-Town / Avoidance Instructions

Statements directing a witness, or directing a relay person to direct a witness, to:

- Leave the jurisdiction temporarily ("just go to your aunt's in Texas until this is over")
- Become unavailable for service ("if anybody comes asking, you didn't get the subpoena")
- Change phone numbers or move
- Avoid responding to investigators, the DA, or even the defense

Statutory exposure: La. R.S. 14:129.1 (intimidating a witness) when the avoidance instruction is paired with anything that resembles pressure, threat, or coercion. Even without coercion, the conduct may support obstruction-of-justice charging.

Severity: HIGH or CRITICAL depending on specificity and whether the witness actually became unavailable.

### Pattern 2: Story-Coordination Instructions

Statements coordinating what the witness or relay person should say if asked:

- "Just tell them you don't remember"
- "Stick with the story we already told"
- "If they ask, say [specific fact]"
- "Make sure everyone is on the same page about that night"
- "Don't mention [specific person / object / event]"

These are direct obstruction patterns under both Louisiana and federal law. The State will introduce them substantively as consciousness-of-guilt evidence and may use them as predicate acts for separate obstruction or conspiracy charges.

Severity: CRITICAL when the coordinated story would be material to a charged element; HIGH when the coordination is peripheral.

### Pattern 3: Threat or Intimidation

Direct or implied threats toward a witness or the witness's family:

- Explicit threats ("she better watch herself if she shows up to court")
- Implied threats through references to the witness's children, residence, employment
- Use of intermediaries to communicate threats ("tell him I said hello and he should think real hard about what he's doing")

Severity: CRITICAL with virtually no exception. Verbal counsel notification immediately.

### Pattern 4: Bribery / Inducement

Offers of money, property, or other benefit conditioned on testimony or non-testimony:

- "If she just doesn't show, my mom will take care of her"
- "Tell him I'll make it right when I get out"
- References to specific dollar amounts, asset transfers, or future benefits

Severity: CRITICAL.

### Pattern 5: Coded Language

Use of nicknames, place-names, or numerical codes after counsel has warned the client about call recording, or after the corpus shows the client moving from plain-language references to coded references mid-stream.

Codes are themselves evidence — they signal consciousness of recording and consciousness of guilt — and they are easily decoded at trial when paired with other call traffic. Flag every consistent coded reference and document the inferred meaning.

Severity: MODERATE on its own; promotes to HIGH or CRITICAL when paired with another red-flag pattern.

### Pattern 6: Asset / Evidence Disposal

References to disposing of, hiding, destroying, or moving:

- The weapon
- The vehicle
- The phone(s) used during the offense
- Clothing or other forensic-evidence items
- Cash or other proceeds
- Digital evidence (deleting accounts, wiping devices)

Severity: HIGH or CRITICAL. Triggers cross-feed to `dw-chain-of-custody-auditor` if the evidence in question is on the State's exhibit list.

### Pattern 7: Coordination With Co-Defendants

Calls relaying messages between charged co-defendants who are subject to no-contact orders or whose attorneys have not authorized direct communication:

- Status updates on each other's charges, plea offers, or cooperation posture
- Coordinated factual positions ("we both need to say...")
- Attempts to influence a co-defendant's cooperation decision ("tell him the snitches don't last in there")

Severity: HIGH. Often pairs with Pattern 2 (story coordination) and Pattern 3 (intimidation).

### Pattern 8: Surveillance of Witnesses

References to monitoring a witness's whereabouts, court appearances, residence, or social media:

- "She's been posting about the case"
- "I heard she got a new place over on..."
- "They saw her at court last Tuesday"

Severity: HIGH. Even without an explicit threat, surveillance references support an intimidation theory and bond-revocation exposure.

### Pattern 9: Awareness-of-Recording Followed by Continued Discussion

Statements acknowledging that the calls are recorded ("they record this you know") followed by case discussion. This pattern is doubly damaging: the awareness shows consciousness of recording, and the continued discussion shows the client did not believe the content was sufficiently incriminating to stop, or did not care.

Sometimes the client uses awareness-of-recording as a performative shield ("I'm not going to talk about that on this phone") followed by a hand-off through a relay or a code. That hand-off pattern is itself a Module D flag.

Severity: MODERATE on its own; promotes to HIGH when paired with Patterns 1, 2, 5, or 7.

### Pattern 10: Court / Juror / System Contact

Discussion of contacting jurors, judges, court staff, or attempts to influence judicial process. Rare but extremely serious when present.

Severity: CRITICAL. Verbal counsel notification immediately and consideration of a confidential disclosure obligation.

## Severity Assignment Rubric

| Severity | Definition | Counsel Action |
|----------|-----------|----------------|
| **CRITICAL** | Statement that, if played for a prosecutor, would generate new charges, bond revocation, or a fundamental change in plea posture | Verbal counsel notification BEFORE audit document finalization; consider immediate client conference |
| **HIGH** | Statement that materially increases tampering exposure, supports an obstruction theory, or undermines the defense's plea or trial posture | Flag in audit; recommend attorney conference within 7 days |
| **MODERATE** | Statement that creates some tampering exposure but is defensible or readily contextualized | Flag in audit; integrate into ongoing case strategy |
| **LOW** | Statement that is technically a tampering signal but is unlikely to be acted on by the State | Document for completeness; minimal further action |

## Cross-Feed Routing

| Module D Finding | Routes To | Payload |
|------------------|-----------|---------|
| Any flag involving a named State's witness | `dw-witness-threat-matrix` (Refresh Mode) | Updated Damage / Vulnerability scores; new impeachment hooks |
| Any relay person identified | `dw-defense-investigator-tasking` | Investigator tasking to interview relay person and assess co-conspirator exposure |
| Any asset-disposal flag implicating exhibit-list evidence | `dw-chain-of-custody-auditor` | Chain-of-custody audit for the affected exhibit |
| Any CRITICAL flag | Verbal counsel notification | Direct attorney call before document finalization |
| Any pattern affecting bond conditions | `dw-bond-and-release-motion` | Bond-posture review for revocation exposure |
| Pattern 7 (co-defendant coordination) where co-defendant is represented by separate counsel | Conflict review | Confirm no joint-defense agreement violations and no inadvertent privilege issues |

## Self-Tampering by the Client

The client's own awareness-and-continued-discussion patterns (Pattern 9), and the client's own statements describing the recording system, are themselves damaging — they evidence consciousness of guilt and consciousness of the recording. Document these as a separate sub-section of the Module D output, distinct from witness-directed conduct.

## Documentation Requirements

For every Module D entry:

- Call ID and timestamp range
- Verbatim quote (or transcript excerpt)
- Pattern number(s) and severity
- Identified parties (client, recipient, named third parties)
- Statutory or doctrinal exposure
- Cross-feed routing
- Recommended counsel action with timeline

## Operational Caution

When a Module D CRITICAL flag surfaces, the audit team must NOT independently contact the affected witness, relay person, or co-defendant. Witness-related investigation routes through `dw-defense-investigator-tasking` under attorney supervision. The analyzer's job is detection and documentation; field action is the investigator's and the assigned attorney's call.
