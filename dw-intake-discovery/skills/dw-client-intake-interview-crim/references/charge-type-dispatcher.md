# Charge-Type Dispatcher

Read at SKILL.md MODULE B — Charge Identification & Statutory Snapshot; holds the charge-identification list, the charge-type dispatcher table, and the charge-type intake question-branch summaries.

### Charge identification

From whatever the client/family knows (charge name, statute, charging instrument if produced), identify:

- The Louisiana statute(s) under which the client is or will be charged (La. R.S. citations)
- Felony or misdemeanor classification
- Maximum exposure (years, fine, mandatory minimums)
- Any sentencing enhancements likely (habitual offender, firearm enhancements, drug-free zone, hate crime, etc.)
- Whether the charge category triggers special collateral consequences (sex offender registration, deportation per *Padilla v. Kentucky*, professional license consequences, firearms disability)

If the client has not yet been charged but expects to be (warrant pending, target of investigation), capture the charge being threatened by law enforcement and proceed.

### Charge-type dispatcher

Route to the appropriate charge-type specialist for the statutory snapshot, charge-specific intake questions, and early defense framing:

| Charge category | Specialist to dispatch |
|---|---|
| Drug offense (possession, distribution, manufacture, conspiracy) | `dw-drug-offense-specialist-crim` |
| DWI / DUI / OWI | `dw-dwi-specialist-crim` |
| Sex offense (any La. R.S. 14:42 series, 14:43 series, 14:80 series, 14:81 series) | `dw-sex-offense-specialist-crim` |
| Violent crime (homicide, attempted homicide, armed robbery, aggravated battery, kidnapping) | `dw-violent-crime-specialist-crim` |
| Firearm offense (felon-in-possession, illegal carry, convicted-felon firearm enhancements) | `dw-firearms-specialist-crim` |
| Domestic violence / IPV | `dw-violent-crime-specialist-crim` (with intake-question-bank-by-charge-type domestic violence module) |
| White-collar / fraud / theft | Use the white-collar branch in `references/intake-question-bank-by-charge-type.md`; no dedicated specialist skill yet — flag for attorney review |
| Juvenile (client under 17 at time of offense) | Use the juvenile branch in `references/intake-question-bank-by-charge-type.md`; flag for attorney review |
| Multiple charges spanning categories | Run dispatcher for each applicable category; flag for attorney review and prioritize the most-exposure charge |
| Charge category unclear | Capture the everyday description, flag `[CHARGE CATEGORY UNCLEAR — ATTORNEY TO ROUTE]`, do not guess |

**Dispatcher output:** in the intake memo, list each charge category identified, the statute(s), and the specialist skill the attorney should invoke after intake closes. Do not invoke the specialist from inside this skill — intake produces the seed only. The attorney decides when to run the specialist.

### Charge-type intake questions

For each charge category, load the corresponding question branch from `references/intake-question-bank-by-charge-type.md`:

- Drug offense — possession context, search predicate, informant indicators, quantity, packaging, distribution markers
- DWI — stop predicate, field sobriety conditions, breath/blood test status, prior DWI history, license status
- Sex offense — relationship to complainant, age disparity, electronic communications, prior allegations
- Violent crime — self-defense indicia, weapon possession, victim relationship, witness universe, injury severity
- Firearm offense — possession context, prior felony status, ownership, location at time of seizure
- White-collar — entity vs. individual liability, document preservation, regulatory parallel proceedings
- Domestic violence — relationship, prior incidents, protective order status, mutual-arrest considerations
- Juvenile — age at offense, school status, parent/guardian involvement, transfer-to-adult-court exposure

Run the relevant branch in the interview. Produce the answers as a charge-specific addendum to the intake memo.
