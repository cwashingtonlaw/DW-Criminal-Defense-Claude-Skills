# Rising BAC Defense & Retrograde Extrapolation

## Overview

One of the most powerful DWI defenses: the BAC result obtained at time of testing does NOT equal the BAC at time of driving. During the absorption phase (30-90 minutes after drinking), blood alcohol continues to rise. If testing occurred during this phase, BAC at driving time could have been below 0.08%.

**Core Premise:** The prosecution must prove BAC at time of driving was ≥0.08%. If rising BAC applies, the burden of disproving rising BAC falls on prosecution.

---

## Absorption & Elimination Kinetics

### Alcohol Absorption Timeline

**After consuming alcohol:**
1. **0-15 minutes:** Minimal absorption (alcohol still in stomach)
2. **15-90 minutes:** Peak absorption phase (alcohol absorbed through small intestine)
3. **After 90 minutes:** Absorption generally complete; steady-state BAC reached

**Key Point:** During absorption (first 30-90 min post-drink), BAC is still rising. Testing during this window means test BAC > driving BAC.

### Alcohol Elimination (Post-Absorption)

Once absorption complete, elimination is relatively linear:
- **Typical elimination rate:** 0.015% BAC per hour (NHTSA standard assumption)
- **Range:** 0.010-0.020 per hour (highly individual)
- **Variation factors:** Body weight, metabolism, age, sex, liver function

**Critical Issue:** Elimination rate is NOT the same as absorption rate. Absorption is steep and rapid; elimination is gradual and linear.

---

## Rising BAC: When It Applies

### Circumstances Suggesting Rising BAC

**More likely to apply if:**
- [ ] Short time between driving and testing (< 60 minutes, especially < 30 min)
- [ ] Suspect consumed alcohol within 30-45 minutes of driving
- [ ] Multiple drinks consumed in short time period (bolus drinking)
- [ ] Drinking continued after driving stopped (e.g., suspect pulled over, drank at scene, tested later)
- [ ] Test BAC result close to legal limit (0.08-0.10%)
- [ ] Suspect reported recent eating/drinking to officer or BAC test observer
- [ ] Food content unknown or low (alcohol absorbs faster on empty stomach)

### Timeline Reconstruction Required

**Obtain from case file:**
1. When did suspect last drink? (Exact time from witness or suspect statement)
2. When was suspect pulled over? (From traffic stop timestamp/officer report)
3. When was breath/blood test conducted? (From Intoxilyzer printout or blood draw documentation)
4. Time elapsed from last drink to test = critical factor

**Example Scenario:**
- Suspect pulled over 8:30 PM
- Last drink consumed 7:50 PM (40 minutes before stop)
- Breath test conducted 8:52 PM (62 minutes after last drink, 22 minutes after stop)
- Result: 0.084 BAC at time of test

**Analysis:**
- At 62 minutes post-drink, suspect still in absorption phase (hasn't reached 90-min marker)
- BAC was rising from 7:50 PM to 8:52 PM
- At time of driving (8:30 PM), BAC was LOWER than test BAC (0.084)
- Likely BAC at driving < 0.08 (below legal limit)

---

## Retrograde Extrapolation: Mathematical Calculation

### Widmark Formula (Most Common)

**Formula:** BAC = (A / (r × W)) - (β × t)

**Variables:**
- **A** = Grams of ethanol consumed
- **r** = Gender-specific distribution ratio (alcohol disperses in body water, not fat)
  - Males: 0.73 (ethanol distributes to ~73% of body weight)
  - Females: 0.66 (higher body fat % = lower distribution ratio)
- **W** = Body weight in kilograms (convert: lb ÷ 2.2 = kg)
- **β** = Elimination rate in BAC per hour (typically 0.015, range 0.010-0.020)
- **t** = Time in hours since drinking

### Example Retrograde Extrapolation

**Given:**
- 180-lb male
- Test BAC: 0.084 at 8:52 PM (test time)
- Last drink: 7:50 PM (1 hour 2 minutes prior)
- Consumed: 3 beers (~36 grams ethanol)

**Calculation (backward to driving time):**

1. **Convert weight:** 180 lbs ÷ 2.2 = 81.8 kg
2. **Calculate BAC at test time from formula rearranged:**
   - Assumption: BAC still rising (not yet at steady state)
   - If absorption phase: elimination during absorption negligible
   - Estimated BAC at driving (8:30 PM) = Test BAC minus rise during 22 minutes between driving and test

3. **Rise in BAC in 22 minutes:**
   - During absorption, absorption rate >> elimination rate
   - Absorption rate: ~0.010-0.015 BAC per 10 minutes (varies)
   - In 22 minutes: approximately 0.022-0.033 BAC rise

4. **Result:**
   - Test BAC: 0.084
   - Minus estimated rise: ~0.025
   - Estimated BAC at driving: ~0.059 (below 0.08 limit)

---

## Defense Challenge to Retrograde Extrapolation

### Variables Subject to Extreme Individual Variation

**Alcohol Consumption (A):**
- How many drinks? Prosecution relies on suspect statement (unreliable)
- What type? Beer vs. wine vs. spirits (different alcohol content)
- Consumed over what time period? (Affects absorption rate)
- Food content? (Slows absorption dramatically)

**Distribution Ratio (r):**
- Assumes standard male/female ratio
- Individual variation: lean vs. obese (affects distribution)
- Genetic variation in water content
- Age and medical conditions affect distribution
- Use of 0.73 (male) or 0.66 (female) is crude estimate

**Body Weight (W):**
- Does prosecution have accurate weight?
- Weight fluctuates daily
- Muscle vs. fat composition not accounted for

**Elimination Rate (β):**
- **Most problematic variable**
- NHTSA assumes 0.015 per hour (middle of range)
- Individual variation: 0.010-0.020 per hour (100% variation)
- Some individuals eliminate at 0.010; others at 0.020
- No way to know individual's rate without prior testing
- Age, liver function, metabolism, metabolism-affecting drugs all affect rate

**Time (t):**
- When exactly did suspect stop drinking? (May be uncertain)
- When exactly was test? (Usually clear from documentation)

### Prosecution's Calculation ≠ Actual BAC

**Example:** Using "average" 0.015 elimination rate:
- Prosecution estimates BAC at driving = X
- Actual elimination rate might be 0.010 (slower) = higher actual BAC
- OR actual elimination rate might be 0.020 (faster) = lower actual BAC
- ±50% variation in outcome

**Defense argument:** "The prosecution's retrograde extrapolation uses assumptions that could be off by 50%. Given this margin of error, the calculated BAC at driving could have been below 0.08."

---

## Expert Witness: Toxicology

### When to Retain

**Retrograde extrapolation defense warranted if:**
- [ ] Time from last drink to test < 90 minutes
- [ ] Test BAC result 0.08-0.12 (borderline to modestly impaired)
- [ ] Prosecution intends to introduce expert testimony on retrograde extrapolation
- [ ] Individual variation factors present (unusual eating/drinking pattern, obesity, age, medical conditions)

### Expert Qualifications to Verify

- Forensic toxicologist (PhD or MS in toxicology, chemistry)
- Pharmacokinetics expertise (alcohol absorption and elimination)
- Published research on alcohol absorption, elimination, and individual variation
- Prior expert testimony in DWI cases
- NAAFS or ASFS certification (American Academy/Society of Forensic Sciences)
- No conflicts or disciplinary issues

### Expert Testimony Focus

**Expert should testify to:**
1. Widmark formula is crude estimate with large individual variation
2. Elimination rate assumption (0.015) is middle of range; individual rates vary 0.010-0.020
3. Given individual variation, prosecution's retrograde extrapolation could underestimate actual BAC or overestimate actual BAC by significant margin
4. Food intake, body composition, drinking pattern all affect absorption and elimination
5. Without prior testing of this suspect's elimination rate, actual rate is unknown
6. Conclusion: "At time of driving, this defendant's BAC could have been below 0.08%."

---

## Key Case Law (Louisiana)

### State v. Hebert, 1995-0833 (La. App. 4th Cir. 1996)

**Holding:** Retrograde extrapolation testimony is admissible to show BAC at time of driving, but prosecution must establish sufficient foundation:
- Reliable methodology
- Factual basis (drinking timeline, amount consumed, body weight)
- Expert qualifications

**Defense Application:** Hebert allows defense expert to testify that prosecution's retrograde extrapolation assumptions are unreliable and individual variation could lead to lower estimated BAC at driving.

### State v. Legendre, 1998-2265 (La. App. 4th Cir. 1999)

**Holding:** Defense may introduce evidence that suspect's BAC was still rising (absorption phase) at time of test, undermining accuracy of test as measure of impairment at driving.

**Defense Application:** Rising BAC testimony is admissible; can argue BAC was below legal limit at driving time.

---

## Rising BAC Defense Checklist

**Evaluate every DWI case for rising BAC applicability:**

- [ ] Time from last drink to traffic stop: ____ minutes
- [ ] Time from traffic stop to test: ____ minutes
- [ ] Total time from last drink to test: ____ minutes
- [ ] Is total time < 90 minutes? (If yes, suspect likely still in absorption phase)
- [ ] Test BAC result: ____ BAC
- [ ] Is test result 0.08-0.15? (Borderline range where rising BAC most impactful)
- [ ] Food consumed near time of drinking? (Details: ____)
- [ ] Drinking pattern: rapid/bolus or slow/gradual?
- [ ] Number of drinks: ____
- [ ] Time period over which drinks consumed: ____ minutes/hours
- [ ] Any drinking after driving (at scene, after arrest)? (Details: ____)
- [ ] Suspect's body weight, age, medical conditions affecting metabolism?

**If multiple "yes" answers to above, rising BAC is viable defense.**

---

## Defense Strategy

### Discovery Requests

- Obtain all statements by suspect regarding time of drinking, amount, type of alcohol, food consumption
- Obtain police report narrative (often contains drinking timeline)
- Obtain audio/video of implied consent advisement or pre-test interviews (may show suspect stating recent drinking)
- Obtain toxicology reports (if available)

### Cross-Examination of Officer

- "What time did the suspect state they consumed their last drink?"
- "What time was the traffic stop?"
- "What time was the breath/blood test administered?"
- "Officer, were you aware that alcohol continues to be absorbed into the bloodstream for up to 90 minutes after drinking?"
- "During that time period, the suspect's blood alcohol level would be rising, correct?"
- "That means the BAC at the time of driving could have been lower than the BAC at the time of testing?"

### Cross-Examination of Prosecution's Toxicology Expert

- Challenge assumptions in retrograde extrapolation
- Establish individual variation in elimination rate (±50%)
- Question how prosecution determined suspect's elimination rate without prior testing
- Highlight food intake/drinking pattern variables
- Establish that given variables and individual variation, actual BAC at driving could have been below 0.08%

### Jury Instructions

Request jury instruction on:
- Rising BAC: BAC at test time ≠ BAC at driving time
- Absorption phase occurs within 90 minutes of drinking
- During absorption, BAC rises

---

## Prosecution Rebuttal & Defense Counter

### Prosecution Argument: "Burden of Proof on Defense"

**Rebuttal:** Defense need not prove absence of impairment. Prosecution must prove BAC ≥ 0.08 at time of driving beyond reasonable doubt. If rising BAC creates reasonable doubt, conviction fails.

### Prosecution Argument: "Officer Observed Impairment"

**Rebuttal:** SFST clues do not prove BAC ≥ 0.08. Many conditions mimic impairment. BAC reading is only direct evidence of BAC; if BAC reading subject to rising BAC defense, prosecution's case is weakened.

### Prosecution Argument: "Amount of Alcohol Consumed Establishes BAC ≥ 0.08"

**Rebuttal:** Amount consumed depends on suspect's statement (unreliable). Even if 3 beers consumed, BAC depends on absorption rate, body weight, food intake, individual elimination rate. Cannot reliably calculate BAC backward from drinks consumed.

