# Cross-Case Finding Schemas (XW / XO / XT / XB / XS)

Read at Step 2 (Cross-Case Inconsistency Analysis) of `dw-dmar-synthesizer-crim` before writing any finding; the exact finding-block formats for Modules S1–S5 and the S1 inconsistency-type definitions moved verbatim from SKILL.md.

## Module S1 — CROSS-CASE WITNESS INCONSISTENCY [XW-###] and Inconsistency Types

```
CROSS-CASE WITNESS INCONSISTENCY [XW-001]
Witness: [Name]
Case A: [Client name] — DMAR Section [X], [source file] @ [timestamp]
  Statement: "[What the witness said in Case A]"
Case B: [Client name] — DMAR Section [X], [source file] @ [timestamp]
  Statement: "[What the witness said in Case B]"
Inconsistency Type: DIRECT CONTRADICTION / MATERIAL OMISSION / DETAIL SHIFT / SEQUENCE CONFLICT
Severity: CRITICAL / SIGNIFICANT / MINOR
Defense Significance: [Why this matters — impeachment, reasonable doubt, severance, Brady]
Cross-Exam Seed: [One-line question exploiting this inconsistency]
Affected Clients: [Which defendants benefit from this finding]
```
**Inconsistency Types:**
- **DIRECT CONTRADICTION**: Witness says X happened in one case, says not-X in another
- **MATERIAL OMISSION**: Witness includes a critical detail in one case but omits it entirely from the other
- **DETAIL SHIFT**: Core claim is the same, but specifics change (time, distance, lighting, weapon type, number of people, sequence of events)
- **SEQUENCE CONFLICT**: Witness describes the same events in a different chronological order across cases

## Module S2 — CROSS-CASE OFFICER AUDIT [XO-###]

```
CROSS-CASE OFFICER AUDIT [XO-001]
Officer: [Name / Badge #]
Cases: [List all DMARs where this officer appears]
Finding Category: NARRATIVE INCONSISTENCY / TECHNIQUE PATTERN / MIRANDA PATTERN / REPORT PATTERN
Case A: [Description with DMAR section and source references]
Case B: [Description with DMAR section and source references]
Pattern: [What the cross-case comparison reveals]
Defense Significance: [Impeachment value, suppression argument, Brady obligation]
Cross-Exam Seeds: [Questions for each case where this officer testifies]
```

## Module S3 — CROSS-CASE TIMELINE CONFLICT [XT-###]

```
CROSS-CASE TIMELINE CONFLICT [XT-001]
Time Window: [HH:MM:SS] — [HH:MM:SS] on [Date]
Case A: [Client name] — [Event per Case A's DMAR timeline]
  Source: [File] @ [timestamp]
Case B: [Client name] — [Event per Case B's DMAR timeline]
  Source: [File] @ [timestamp]
Conflict: [Why these can't both be true simultaneously]
Defense Significance: [Alibi, misidentification, reasonable doubt]
Affected Clients: [Who benefits]
```

## Module S4 — CROSS-CASE BRADY/GIGLIO ALERT [XB-###]

```
CROSS-CASE BRADY/GIGLIO ALERT [XB-001]
Source Case: [Client whose DMAR contains the evidence]
Source: DMAR Section [X], [file/finding reference]
Evidence: "[Description of potentially exculpatory or impeachment material]"
Benefiting Case: [Client who should have received this in discovery]
Brady Category: EXCULPATORY (A) / IMPEACHMENT (B) / MITIGATION (C)
Disclosure Status: UNKNOWN — attorney should verify whether this was disclosed in [benefiting client]'s discovery
Recommended Action: [Check discovery ledger, file Brady motion if undisclosed]
```

## Module S5 — SEVERANCE INDICATOR [XS-###]

```
SEVERANCE INDICATOR [XS-001]
Type: BRUTON / ANTAGONISTIC DEFENSES / SPILLOVER PREJUDICE / IRRECONCILABLE TIMELINES
Case A Impact: [How this affects Client A]
Case B Impact: [How this affects Client B]
Source Findings: [List the XW/XO/XT/XB findings that support this indicator]
Legal Authority: [Bruton v. United States, Zafiro v. United States, State v. [relevant LA case]]
```
