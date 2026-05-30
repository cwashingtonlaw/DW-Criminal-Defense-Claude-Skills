# Timestamp Analysis Template

Chronological event documentation for confession/interrogation audits. Convert the raw recording or transcript into a time-anchored event log so each finding ties to a specific moment in the record. The audit's CRITICAL / SIGNIFICANT severity ratings depend on this anchoring.

---

## 1. Event Log Format

| Time | Source | Event | Module | Severity | Note |
|------|--------|-------|--------|----------|------|
| `HH:MM:SS` | Recording / BWC / report | What happened (1-2 lines) | A / B / C / D / E / F / G | CRIT / SIG / MOD / MIN | Why it matters |

**Time formatting:**
- Use the recording's clock time when available (e.g., `14:32:18`).
- If the recording timestamp is unreliable or absent, use elapsed time from start (`00:23:45 from start`).
- If multiple recordings (BWC + interview room) cover the same period, cite both with their respective timestamps.

**Source citation:**
- `(Interview Recording, 14:32:18)`
- `(BWC Officer Smith, 14:32:18)`
- `(Officer Report, p. 3, para. 4)`
- `(Booking Log, 14:32:18)`

---

## 2. Required Anchor Events

Every audit timeline must include these anchor events when present in the record:

| Anchor | What to Capture |
|--------|-----------------|
| Initial contact / arrest | Time, location, officer(s), use of force, cuffing |
| Transport to station | Duration, anything said in transport |
| Arrival at station | Time, room assignment, restraints |
| Request for water / bathroom / food | Time and whether granted |
| Booking | Time and content of booking questions |
| First officer entry to interview room | Time, identity, demeanor |
| Miranda warnings administered | Time, exact wording, presence of waiver form |
| Waiver | Time, express vs. implied, written or oral |
| First substantive question | Time, subject matter |
| First admission (if any) | Time, content, prompted vs. spontaneous |
| First request for counsel (if any) | Time, exact words, officer response |
| First invocation of silence (if any) | Time, exact words, officer response |
| Coercive technique applied | Time, technique (Module C), suspect's response |
| False evidence ploy (if any) | Time, ploy used, suspect's response |
| Threats or promises (if any) | Time, exact words, who said it |
| Officer changes (shift change, partner swap) | Time, identity of new officer(s) |
| Breaks (with or without permission) | Time, duration, whether suspect alone |
| Physical contact / aggressive demeanor | Time, what occurred |
| Suspect distress (crying, asking to stop, mental break) | Time, what occurred |
| Final confession statement | Time, content |
| Conclusion of interrogation | Time, who ended it |

---

## 3. Severity Mapping

For each event in the log, map to the relevant audit module and severity:

| Event Type | Default Severity | Adjust UP if... | Adjust DOWN if... |
|-----------|------------------|----------------|-------------------|
| Missing or defective Miranda warning | CRITICAL | Multiple defects | Single minor wording issue |
| Question-first / Seibert pattern | CRITICAL | Multiple two-step exchanges | Isolated single instance |
| Post-invocation questioning | CRITICAL | Continued for extended time | Single confused exchange before re-invocation honored |
| Explicit threat | CRITICAL | Threat to family/loved ones | Vague suggestion of consequences |
| Explicit promise of leniency | CRITICAL | Specific quantified promise | Vague "things will go better" |
| Implied threat or implied promise | SIGNIFICANT | Repeated; combined with vulnerability | Single instance |
| Reid Technique step (minimization, maximization) | SIGNIFICANT | Combined with vulnerability or extended duration | Single instance, brief |
| False evidence ploy | SIGNIFICANT | Significant fabrication; suspect believes it | Vague hint |
| Denial of basic needs (water, bathroom, food) | MODERATE | Extended denial | Brief delay |
| Extended duration without breaks | SIGNIFICANT | > 4 hours continuous | < 1 hour |
| Suspect distress observed and ignored | SIGNIFICANT | Crying, asking to stop, repeatedly | Brief, single instance |
| Vulnerable suspect (juvenile, mental illness, intoxication) | SIGNIFICANT | Severe impairment | Mild |
| Officer demeanor (hostile, accusatory) | MODERATE | Extended; combined with techniques | Brief |
| Late warnings (delay between custody and Miranda) | MODERATE | > 1 hour | < 15 min |

---

## 4. Cross-Module Correlation

The timeline log feeds every other module. After the timeline is complete, run these cross-checks:

| Check | Question |
|-------|----------|
| Module A → Timeline | Are all advisement and waiver events anchored? |
| Module B → Timeline | Is every voluntariness factor (duration, breaks, demeanor, conditions) anchored? |
| Module C → Timeline | Are all coercive technique applications anchored? |
| Module D → Timeline | Are vulnerability events (distress, confusion) anchored? |
| Module E → Timeline | Are all invocation events anchored? Is the officer response timestamped? |
| Module F → Timeline | If juvenile, are parental/counsel notification events (or absences) anchored? |
| Module G → Timeline | Is the actual confession statement anchored to a specific time? |

If any module's findings are not anchored to specific timeline entries, the audit is incomplete and must be revisited before the suppression motion is drafted.

---

## 5. Output Format

Save the timeline as a separate deliverable:

```
{{CASE_ROOT}}/01 - Trial Notebook/09 - Case Analysis/Cowork Analysis/Interrogation Timeline - [Date of Interrogation].docx
```

Include a header block:

```
INTERROGATION TIMELINE
Defendant: [Name]
Case: [Case caption]
Interrogation Date: [Date]
Recording Sources: [list with durations]
Officers Present: [list]
Audit Date: [Date]
```

Followed by the event log table, with severity legend, and a closing summary section noting:
- Total interrogation duration
- Number of CRITICAL events
- Number of SIGNIFICANT events
- Cumulative coerciveness assessment (1-2 paragraphs)
- Recommended Art. 703 motion strength (Strong / Moderate / Weak; with rationale)

The timeline becomes Exhibit A to the suppression motion (see `suppression-motion-checklist.md`).
