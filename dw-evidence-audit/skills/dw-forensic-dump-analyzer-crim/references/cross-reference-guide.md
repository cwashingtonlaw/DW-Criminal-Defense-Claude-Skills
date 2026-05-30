# Cross-Reference Guide — Phone Data vs. Case Documents

This reference provides the detailed methodology for cross-referencing phone dump contents against police reports, witness statements, and the State's timeline. This is an optional but powerful analytical layer that activates when the attorney provides case documents alongside the phone data.

---

## TABLE OF CONTENTS
1. [Cross-Reference Principles](#principles)
2. [Phone Data vs. Police Reports](#police)
3. [Phone Data vs. Witness Statements](#witnesses)
4. [Phone Data vs. State's Timeline](#timeline)
5. [Phone Data vs. Phone Data (Multi-Device)](#multi)
6. [Phone Data vs. Surveillance & Body Cam Video](#video)
7. [Contradiction Classification & Severity](#severity)
8. [Documentation Standards](#documentation)

---

## 1. Cross-Reference Principles {#principles}

### Why Cross-Referencing Matters
Phone data is objective — it records what happened on the device without narrative spin. Police reports and witness statements are subjective — they reflect what someone claims happened, filtered through memory, bias, and sometimes deliberate fabrication. When objective phone data contradicts subjective narrative, the phone data wins.

### Analytical Approach
1. **Extract testable claims** from each case document — specific times, communications, locations, sequences of events
2. **Map each claim** to corresponding phone data (or the absence of corresponding data)
3. **Classify the result:** Corroborated, Contradicted, Partially Supported, No Data Available, or Suspicious Gap
4. **Assess significance:** How material is this contradiction to the defense?

### Important Limitations
- Phone data is not infallible — timestamps can be wrong, data can be incomplete, and extraction errors exist
- Absence of phone data doesn't always mean the event didn't happen — not all activity leaves digital traces
- Minor discrepancies (off by a few minutes) may reflect innocent clock differences rather than fabrication
- Flag uncertain findings as "requires further investigation" rather than overstating their significance

---

## 2. Phone Data vs. Police Reports {#police}

### What to Extract from Police Reports
Read each police report and extract every testable factual claim:

**Time Claims:**
- "At approximately [time], officers responded to..."
- "The defendant stated he was at [location] at [time]"
- "The victim called 911 at [time]"
- "Officers arrived on scene at [time]"

**Communication Claims:**
- "The victim stated the defendant called her at [time]"
- "The defendant admitted to texting [person] about [topic]"
- "Witnesses observed the defendant on his phone at [time]"

**Location Claims:**
- "The defendant was observed at [location]"
- "The defendant stated he was at [location]"
- "Cell phone records place the defendant at [location]" (verify the report's own interpretation)

**Sequence Claims:**
- "First [X] happened, then [Y], then [Z]"
- Any narrative describing the order of events

### Cross-Reference Protocol

For each extracted claim, check:

```
CLAIM: [Specific factual assertion from police report]
SOURCE: [Report, page number, officer name]
PHONE DATA: [What the phone data shows]
RESULT: [Corroborated / Contradicted / No Data / Partial / Ambiguous]
SIGNIFICANCE: [How this affects the defense]
```

### Common Police Report vs. Phone Data Discrepancies

**Timing errors:** Officers estimate times from memory; phone records are timestamped. Discrepancies of 15-30 minutes are common and may not be significant. Discrepancies of hours are significant.

**Communication misattribution:** The report says the defendant "called" when phone records show the victim called the defendant (or vice versa). Direction matters — it affects who initiated contact.

**Omitted communications:** The report describes select communications but omits others that provide exculpatory context. Check: are there calls or messages during the relevant period that the report doesn't mention?

**Location assumptions:** The report places the defendant at a location based on an officer's interpretation of cell data that may be more nuanced than the report suggests. Verify the underlying data.

**Timeline compression:** Officers sometimes compress a sequence of events to fit their narrative. Phone data with precise timestamps may show the sequence took much longer (or shorter) than the report implies.

---

## 3. Phone Data vs. Witness Statements {#witnesses}

### What to Extract from Witness Statements

**Communication Claims:**
- "He called me at around [time]"
- "She texted me saying [content]"
- "I tried to call him but he didn't answer"
- "We were texting back and forth that night"

**Timing Claims:**
- "This happened around [time]"
- "I saw him at about [time]"
- "He left at [time]"

**Denial Claims:**
- "I never spoke to him that day"
- "I didn't text her about that"
- "I wasn't in contact with anyone"

**Relationship Claims:**
- "I barely know him"
- "We hadn't spoken in months"
- "She was afraid of him and wouldn't contact him"

### Cross-Reference Protocol

For each witness claim:

```
WITNESS: [Name]
CLAIM: [Specific assertion]
SOURCE: [Statement, page/paragraph]
PHONE DATA: [What the records show]
RESULT: [Corroborated / Contradicted / No Data / Partial]
IMPEACHMENT VALUE: [High / Medium / Low / None]
SUGGESTED USE: [Cross-exam / Motion / Argument]
```

### High-Value Contradiction Patterns

**"I never contacted him" + phone records showing contact:** Witness credibility destroyed. The witness either lied deliberately or has unreliable memory — either way, their other claims are suspect.

**"He called me threatening" + records showing no call at that time:** If the claimed threatening call doesn't appear in the phone records, the claim may be fabricated. Caveats: the call could have been from a different phone, or the witness may have the time wrong.

**"We texted about [X]" + messages showing a completely different conversation:** The witness may be confusing conversations, confusing people, or deliberately misrepresenting the communication.

**"She was afraid and wouldn't contact him" + records showing victim initiated frequent contact:** Powerful impeachment of claims of fear — the victim's own behavior contradicts their stated fear.

**"I was with him at [time]" + phone data showing the alibi witness's phone was elsewhere:** If a defense alibi witness's own phone data contradicts their alibi testimony, identify this BEFORE the State does and address it.

### Witness-Specific Notes

**Victim as witness:** Cross-reference every factual claim the victim made to police against the phone data. Victims in adversarial situations may exaggerate, misremember, or fabricate. The phone data either corroborates or contradicts — and contradictions are powerful impeachment material.

**Co-defendant as witness:** If a co-defendant is cooperating with the State, cross-reference their claims against phone data from both phones. Cooperators have incentive to minimize their role and exaggerate the client's — phone data can expose this.

**Law enforcement as witness:** Officers are witnesses too. Their claims about what they observed, when they responded, and what they were told should be cross-referenced against phone data and dispatch records.

---

## 4. Phone Data vs. State's Timeline {#timeline}

### Building the Comparison

**Step 1:** Extract the State's claimed sequence of events. This may come from:
- The charging document / bill of information
- The police report narrative
- Witness statements aggregated into a prosecution theory
- The State's opening (if available post-trial start)

**Step 2:** Create a two-column timeline:

```
STATE'S TIMELINE                    | PHONE DATA TIMELINE
────────────────────────────────────|──────────────────────────────────
8:00 PM — Defendant arrives at     | 7:55 PM — Text from def to friend:
         victim's home             |           "heading home, long day"
                                   | 8:02 PM — Wi-Fi connects to
                                   |           [defendant's home network]
                                   | 8:15 PM — Def browsing Netflix
                                   |
9:00 PM — State claims assault     | 8:45 PM — Def texts mom: "goodnight"
         occurred                  | 9:03 PM — Def's phone connects to
                                   |           cell tower near def's home
                                   |           (not near victim's home)
                                   | 9:15 PM — Def playing mobile game
                                   |           (screen time data)
                                   |
10:30 PM — Victim calls 911       | 10:28 PM — Victim texts friend:
                                   |            "[context message]"
                                   | 10:31 PM — 911 call in phone log
```

**Step 3:** Identify every conflict and gap. For each:
- What the State claims vs. what the phone shows
- Whether the conflict is a timing discrepancy or a factual impossibility
- How the defense can use it

### Feasibility Analysis

When the State's timeline requires the defendant to travel between locations, calculate feasibility:

```
FEASIBILITY CHECK
─────────────────────────────────────────────
State claims defendant traveled from [A] to [B]
between [time1] and [time2].

Time available: [minutes]
Distance (driving): [miles] / [estimated minutes]
Distance (walking): [miles] / [estimated minutes]

Phone data shows:
  - Last ping at/near [A]: [time]
  - First ping at/near [B]: [time]
  - Activity during transit window: [any calls/texts/data use?]

CONCLUSION: [Feasible / Tight / Improbable / Impossible]
NOTE: [If improbable/impossible, recommend independent timing verification]
```

---

## 5. Phone Data vs. Phone Data (Multi-Device) {#multi}

When dumps from multiple phones are available (defendant + victim, defendant + co-defendant, etc.), cross-reference between them.

### Key Cross-References

**Message symmetry:** Messages sent from Phone A should appear as received on Phone B (and vice versa). Discrepancies indicate:
- Deletion on one device
- Extraction failure on one device
- Messages sent to a different number than expected
- One device using a messaging platform the other didn't have

**Call log matching:** Outgoing calls on Phone A should match incoming calls on Phone B. Check for:
- Matching timestamps (within 1-2 seconds is normal variance)
- Matching durations (small differences are normal; large differences indicate one phone dropped the call)
- Calls present on one phone but missing from the other

**Location correlation:** If both phones have location data, check for:
- Co-location (both phones at the same place at the same time — confirms the two people were together)
- Separation (phones at different locations — contradicts claims they were together)
- Movement patterns (did they travel together or separately?)

**Contact list comparison:** Check whether each phone has the other's number saved, what name it's saved under, and when the contact was created.

---

## 6. Phone Data vs. Surveillance & Body Cam Video {#video}

### Why This Cross-Reference Matters

Surveillance footage and body camera video provide an independent visual timeline that either corroborates or contradicts what the phone data shows. When they align, both become stronger evidence. When they conflict, something is wrong with one source — and the defense needs to know which.

### Clock Synchronization Challenge

**This is the critical issue:** Video recording systems and phone clocks are almost never perfectly synchronized.

- **Surveillance cameras:** Often drift by minutes to hours. Many systems are set manually and never adjusted for DST. Some use UTC, some use local time, some are simply wrong.
- **Body cameras:** Typically more accurate (synced to department servers), but still may be off by seconds to minutes. Check whether the department calibrates regularly.
- **Phone clocks:** Usually accurate (NTP sync to carrier network), but may drift if set to manual time. Carrier timestamps in CDRs are the most reliable.

**Step 1:** Identify at least one synchronization point — a moment visible on video that also appears in phone records (e.g., the defendant visibly answers a phone call that appears in the call log). Calculate the offset between the video timestamp and the phone timestamp.

**Step 2:** Apply that offset to all subsequent cross-references. If video clock is 3 minutes behind phone clock, adjust before comparing.

**Step 3:** If no synchronization point is available, note the potential offset range and flag all timestamp comparisons as approximate.

### Cross-Reference Protocol

```
VIDEO TIMESTAMP        | PHONE TIMESTAMP       | SYNC OFFSET
─────────────────────────────────────────────────────────────
[Camera time]          | [Phone record time]   | [±N min/sec]
```

**Phone Use Visible on Camera:**
- Can you see the defendant using their phone on video? Does the phone record show corresponding activity at the same (adjusted) time?
- If the defendant appears to be texting on video but no outgoing message appears in the phone records at that time, either the message was sent via an app not captured in the extraction, or the person was doing something else on the phone
- If a call appears in the phone records but the defendant is not seen holding the phone on video, the call may have been on speaker, connected to Bluetooth, or the video doesn't capture the defendant at that moment

**Location Corroboration:**
- Does the video show the defendant at the location the phone data indicates?
- If phone data shows the defendant's phone at Location A but video shows the defendant at Location B, either: (a) someone else had the phone, (b) the location data is imprecise, or (c) the video identification is wrong

**Officer Conduct (Body Cam):**
- Compare officer's verbal statements on body cam against what appears in the police report
- Compare the timing of events on body cam against officer-reported times
- Note any discrepancies between what the officer is seen doing on video and what the phone records of participants show was happening

### Documentation Format

```
VIDEO CROSS-REFERENCE FINDING #[N]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Video Source: [Surveillance camera ID / Body cam officer name]
Video Timestamp: [HH:MM:SS as shown on video]
Adjusted Timestamp: [After sync offset applied]
Sync Offset Used: [±N min/sec, basis for offset]

Phone Record: [Type — call, message, location ping]
Phone Timestamp: [As recorded]
Source File: [filename, row/line]

COMPARISON: [Corroborated / Contradicted / No Data / Ambiguous]
SIGNIFICANCE: [How this affects the defense]
CAVEATS: [Sync uncertainty, video quality, angle limitations]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 7. Contradiction Classification & Severity {#severity}

### Classification System

| Classification | Definition | Example |
|---------------|-----------|---------|
| **HARD CONTRADICTION** | Phone data makes the claim factually impossible | State says defendant called victim at 9 PM; no call exists in either phone's records |
| **STRONG CONTRADICTION** | Phone data is highly inconsistent with the claim | State says defendant was at crime scene at 9 PM; phone connected to home Wi-Fi at 9:03 PM |
| **SOFT CONTRADICTION** | Phone data is inconsistent but not conclusively | Witness says "around 8 PM"; phone records suggest 8:45 PM — could be memory error |
| **CORROBORATED** | Phone data supports the claim | Witness says "he texted me at 9"; text appears at 9:02 PM |
| **NO DATA** | Phone records don't address the claim one way or the other | Claim about in-person conversation with no phone involvement |
| **SUSPICIOUS GAP** | Expected phone data is missing during the period of the claim | State claims extended interaction, but phone shows zero activity for 3 hours in a normally active period |

### Severity Assessment

For each contradiction, assess:

**Material to a charge element?** Does this contradiction affect the State's ability to prove an element of the offense (identity, presence, intent, timing)?

**Material to credibility?** Even if not directly about a charge element, does it destroy a key witness's credibility?

**Independently verifiable?** Can the phone data finding be confirmed through another source (carrier records, surveillance video, independent witness)?

**Explainable by the State?** Could the prosecution offer a reasonable explanation for the discrepancy, or is it a hard contradiction?

Rate overall significance:
- **CRITICAL:** Contradicts a charge element or makes the State's theory physically impossible
- **SIGNIFICANT:** Seriously undermines witness credibility or creates reasonable doubt about the narrative
- **MODERATE:** Creates a meaningful inconsistency the defense can exploit
- **MINOR:** Noted for completeness but unlikely to carry significant weight alone

---

## 8. Documentation Standards {#documentation}

### For Each Cross-Reference Finding

Document with enough specificity that the attorney can verify independently:

```
CROSS-REFERENCE FINDING #[N]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Classification: [HARD/STRONG/SOFT CONTRADICTION or CORROBORATED or SUSPICIOUS GAP]
Severity: [CRITICAL / SIGNIFICANT / MODERATE / MINOR]

CASE DOCUMENT CLAIM:
  Source: [Document name, page, paragraph]
  Who said it: [Officer/Witness name]
  The claim: [Exact quote or precise paraphrase]

PHONE DATA:
  Source: [Data file name, row/line, record ID]
  The data: [What the phone record shows]
  Timestamp: [Exact timestamp from the record]

THE CONTRADICTION:
  [Plain-language explanation of why these two things conflict]

DEFENSE USE:
  [How to use this finding — cross-exam, motion, argument]
  [Cross-exam seed if applicable — format per SKILL.md Step 5]

CAVEATS:
  [Any limitations on this finding — possible innocent explanations,
  need for further investigation, expert verification needed]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

*This reference is loaded by the dw-forensic-dump-analyzer-crim skill during Step 4 (Cross-Reference Mode). It is only relevant when the attorney provides case documents alongside the phone data. If no case documents are provided, the skill operates in standalone mode and skips this reference.*
