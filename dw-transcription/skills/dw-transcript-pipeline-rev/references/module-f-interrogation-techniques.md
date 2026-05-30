# Module F — Interrogation Technique Analysis

*REPLICATES MirandaAI's Reid Technique and coercion detection*

**Runs only on files classified as `INTERROGATION`.**

Scan for the following interrogation techniques and flag each instance:

## F.1 — Reid Technique Components

| Technique | What to Look For | Flag Level |
|-----------|-----------------|------------|
| **Positive Confrontation** | "We know you did this," "The evidence shows..." | SIGNIFICANT |
| **Theme Development** | Minimizing moral blame, offering justifications | SIGNIFICANT |
| **Handling Denials** | Cutting off denials, not allowing suspect to speak | CRITICAL |
| **Overcoming Objections** | Dismissing suspect's reasons for innocence | SIGNIFICANT |
| **Retention of Attention** | Physical proximity, eye contact demands, touching | SIGNIFICANT |
| **Handling Passive Mood** | Crying, withdrawal — detective intensifies | SIGNIFICANT |
| **Alternative Question** | Offering two choices, both incriminating | CRITICAL |
| **Oral Confession Development** | Leading suspect to provide details | SIGNIFICANT |
| **Written Confession** | Moving to written/recorded statement | INFO |

## F.2 — Coercion Indicators

| Indicator | What to Look For | Flag Level |
|-----------|-----------------|------------|
| **False Evidence Ploy** | "Your fingerprints were found," "Your DNA matched" (if potentially false) | CRITICAL |
| **Implicit Promises** | "Things will go better if you cooperate," "Help yourself out" | CRITICAL |
| **Explicit Promises** | "I'll talk to the DA," "You'll go home tonight" | CRITICAL |
| **Threats** | "You'll never see your kids," "You're looking at life" | CRITICAL |
| **Minimization** | "It was an accident," "Anyone would have done the same" | SIGNIFICANT |
| **Maximization** | "This is the worst thing I've ever seen," "You're going down for murder" | SIGNIFICANT |
| **Sleep/Food/Bathroom Deprivation** | Long duration without breaks, requests denied | CRITICAL |
| **Isolation Pressure** | "Nobody can help you but yourself," "Your co-defendant is talking" | SIGNIFICANT |
| **Deception About Law** | Misrepresenting charges, penalties, or legal rights | CRITICAL |
| **Fatigue Exploitation** | Increased pressure during late hours or after long wait | SIGNIFICANT |

## F.3 — False Confession Risk Factors

Flag the presence of any recognized false confession risk factors:
- Juvenile suspect (under 18)
- Intellectual disability indicators (comprehension problems, acquiescence)
- Mental illness indicators (delusions, confusion, disorientation)
- Substance intoxication/withdrawal
- Interrogation duration exceeding 2 hours (flag), 4 hours (critical), 6+ hours (extreme)
- Suspect provides details that were fed by detective (contamination)
- Statement contains implausible or impossible claims
- Suspect changes story to match detective's theory

For each finding:
```
INTERROGATION TECHNIQUE [IT-001]
File: [name] @ [timestamp range]
Category: REID TECHNIQUE / COERCION / FALSE CONFESSION RISK
Specific Technique: [from tables above]
Flag Level: CRITICAL / SIGNIFICANT / INFO
Detective: [name if known]
Verbatim Exchange:
  DETECTIVE @ [timestamp]: "[what detective said]"
  SUSPECT @ [timestamp]: "[suspect's response]"
Analysis: [Why this is significant]
Legal Framework: [Relevant case law — e.g., State v. Blank, Edwards, etc.]
Suppress?: [Yes/No/Maybe]
Cross-Exam Seed: [One-line impeachment question for this detective]
```
