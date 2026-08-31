# Module A — Sentencing Range Calculator

Read at SKILL.md Module A (Sentencing Range Calculator) — five-step Louisiana range calculation and the output table.

### Purpose

Calculate the full sentencing exposure for every count of conviction, including enhancements, mandatory minimums, habitual offender exposure, and consecutive vs. concurrent stacking. Present the range as a table so the attorney and client understand the floor, ceiling, and realistic range.

### Louisiana Sentencing Range Calculation

#### Step 1: Base Statutory Range

For each count of conviction, identify:

| Field | Source |
|-------|--------|
| Statute | La. R.S. citation from charging document |
| Offense Grade | Felony (hard labor / without hard labor) or Misdemeanor |
| Statutory Minimum | Minimum sentence authorized by statute |
| Statutory Maximum | Maximum sentence authorized by statute |
| Fine Range | Minimum and maximum fine authorized |
| Hard Labor | Whether sentence must be served at hard labor |

#### Step 2: Enhancement Analysis

Check every applicable enhancement and calculate the modified range:

**Firearm Enhancements:**
- La. R.S. 14:64.3 -- Armed robbery with firearm: additional 5 years without probation, parole, or suspension
- La. C.Cr.P. Art. 893.1 -- Additional penalty for use of firearm during felony
- Determine whether enhancement is mandatory or discretionary

**Victim-Based Enhancements:**
- Victim under 13: triggers enhanced penalties for many offenses
- Victim over 65: enhanced penalties for certain offenses
- Victim is law enforcement officer: enhanced penalties under specific statutes
- Domestic violence enhancements

**Drug-Free Zone Enhancements:**
- La. R.S. 40:981.3 -- Distribution within 2,000 feet of school, church, public housing
- Enhancement adds one-half the maximum sentence as additional penalty

**Prior Conviction Enhancements:**
- Offense-specific recidivist provisions (separate from habitual offender)
- DWI third and subsequent offense mandatory minimums
- Domestic violence repeat offense enhancements

#### Step 3: Habitual Offender Exposure (La. R.S. 15:529.1)

If the State has filed or may file a habitual offender bill, calculate enhanced exposure.

> **📖 Reference:** Read `references/habitual-offender-reference.md` for enhancement rules by offender status (second, third, fourth offender), cleansing period requirements, and challenge points.

**Critical Notes:**
- "Longest term" means the maximum sentence for the current offense of conviction
- La. R.S. 15:529.1(G): Court **shall** impose habitual offender sentence unless State agrees to withdraw the bill
- Predicate offenses must meet cleansing period requirements (10-year window for most offenses)
- Verify each predicate: proper Boykinization, non-expunged, not pardoned
- State v. Shelton, 621 So.2d 769 (La. 1993): State must prove predicate convictions beyond reasonable doubt
- State v. Johnson, 432 So.2d 815 (La. 1983): Defendant must be advised of right to a hearing

#### Step 4: Concurrent vs. Consecutive Analysis

- La. C.Cr.P. Art. 883 -- Default: sentences run concurrently unless court orders otherwise
- La. C.Cr.P. Art. 883.1 -- Mandatory consecutive sentences for certain crimes of violence committed with a firearm
- La. C.Cr.P. Art. 883.2 -- Mandatory consecutive for offenses against different victims
- Identify which counts can run concurrently and which may be ordered consecutive
- Calculate worst-case (all consecutive) and best-case (all concurrent) total exposure
#### Step 5: Output -- Sentencing Range Table

| Count | Statute | Offense | Base Min | Base Max | Enhanced Min | Enhanced Max | Habitual Min | Habitual Max |
|-------|---------|---------|----------|----------|-------------|-------------|-------------|-------------|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| **TOTAL (Concurrent)** | | | | | | | | |
| **TOTAL (Consecutive)** | | | | | | | | |

**Mandatory Minimum Flag:** If any count carries a mandatory minimum, flag it prominently and note whether Art. 890 departure is available.
