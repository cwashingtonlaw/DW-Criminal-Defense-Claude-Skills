# Module E — Miranda Rights & Constitutional Events Detection

*REPLICATES MirandaAI's core Miranda detection capability*

**This module runs on ALL transcripts but produces detailed output only for files classified as `INTERROGATION` or `WITNESS_INTERVIEW`.**

Scan every transcript for the following constitutional event categories:

## E.1 — Miranda Rights Analysis

Search for any variation of Miranda warnings. Flag:

| Finding | What to Look For | Severity |
|---------|-----------------|----------|
| `MIRANDA-COMPLETE` | All four warnings given clearly | INFO |
| `MIRANDA-PARTIAL` | Some warnings given, others omitted | CRITICAL |
| `MIRANDA-ABSENT` | No Miranda warnings in custodial interrogation | CRITICAL |
| `MIRANDA-TIMING` | Warnings given AFTER substantive questioning began | CRITICAL |
| `MIRANDA-WAIVER-ORAL` | Verbal waiver without written form | SIGNIFICANT |
| `MIRANDA-WAIVER-EQUIVOCAL` | Ambiguous waiver ("I guess," "sure, whatever") | CRITICAL |
| `MIRANDA-INVOCATION` | Suspect invokes right to silence or counsel | CRITICAL |
| `MIRANDA-INVOCATION-IGNORED` | Questioning continues after invocation | CRITICAL |
| `MIRANDA-RE-INITIATION` | Police re-approach after invocation | SIGNIFICANT |

The four Miranda components to check:
1. Right to remain silent
2. Anything said can be used against you
3. Right to an attorney
4. If you cannot afford an attorney, one will be appointed

For each finding, record:
```
MIRANDA EVENT [ME-001]
File: [name] @ [timestamp]
Type: [from table above]
Speaker: [who gave/received warnings]
Verbatim: "[exact words from transcript]"
Analysis: [What's missing, ambiguous, or problematic]
Legal Significance: [Which Miranda prong is affected]
Suppress?: [Yes/No/Maybe — with brief reasoning]
```

## E.2 — Right to Counsel Invocations

Specifically scan for any statement that could constitute an invocation of the right to counsel, including ambiguous statements. MirandaAI's key insight is that invocations are often subtle:

**Clear invocations**: "I want a lawyer," "I need to talk to my attorney," "Get me a lawyer"
**Ambiguous invocations** (Edwards v. Arizona analysis required):
- "Maybe I should talk to a lawyer"
- "Do I need a lawyer?"
- "Can I call my attorney?"
- "I think I want a lawyer"
- "My mama told me to get a lawyer"
- "How do I get a public defender?"

Flag ALL of these. For ambiguous invocations, note that under Edwards v. Arizona and Louisiana jurisprudence, police should have stopped questioning and clarified.

## E.3 — Custody Determination Markers

Flag statements and circumstances indicating whether the suspect was "in custody" for Miranda purposes:
- Told they are free to leave (or not told)
- Door locked/unlocked
- Handcuffs on/off
- Transport in police vehicle
- Location (police station, home, street, vehicle)
- Duration of encounter
- Number of officers present
- Tone of questioning (accusatory vs. investigative)
