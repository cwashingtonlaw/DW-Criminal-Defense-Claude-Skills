# NotebookLM Audit Prompts

Copy-paste these prompts directly into NotebookLM after uploading the CAC interview transcript and case documents.

## Prompt A — Forensic Interview Audit

```
Act as a Forensic Interviewing Expert Defense Witness (similar to the role of Dr. Michaeleen Maher or Dr. Stephen Ceci).

Review the provided CAC interview transcript/summary and audit it for adherence to the NICHD Protocol and best practices for minimizing suggestibility.

Your Task: Identify instances where the interviewer may have contaminated the child's memory.

Please generate a 'Methodology Flaw Report' covering these four specific areas:

1. The 'Free Recall' vs. 'Directed' Ratio
   - Did the child disclose the abuse spontaneously during the 'free narrative' phase (e.g., 'Tell me everything that happened')?
   - Or did the disclosure only happen after the interviewer introduced the topic or asked a specific, leading question?
   - Flag the exact moment/question where the allegation was first solidified.

2. Linguistic Contamination (Adult Terminology)
   - Identify words or phrases the child uses that are age-inappropriate or inconsistent with their previous language (e.g., using specific legal/anatomical terms).
   - Check if these terms originated from the child or were first spoken by the interviewer/parent and then adopted by the child.

3. The 'Option-Posing' Trap
   - List instances where the interviewer used 'Option-Posing' questions (e.g., 'Did he touch you over or under your clothes?') instead of open-ended questions.
   - Did the child simply agree with the option presented?

4. Coercive Reinforcement
   - Highlight moments where the interviewer praised the child specifically for making an incriminating statement (e.g., 'You are doing a great job telling the truth') but remained silent or neutral when the child denied abuse or said 'I don't know.'

Output: A bulleted list of specific 'Impeachment Opportunities' based on these protocol violations.
```

## Prompt B — Red Team Simulation (Prosecution's View)

```
Act as the Lead Prosecutor. Review the file and draft your Closing Argument. Highlight the 3 most damning pieces of evidence against the defendant and explain how you will explain away the inconsistencies in the child's timeline.
```

## Prompt C — Behavioral Baseline Check

```
Review the school records and report cards from [Year 1] to [Year 3]. Is there an objective correlation between the dates of alleged abuse and the child's academic performance or attendance? Or did the grades remain consistent?
```

## Prompt D — Coaching & Motive Scan

```
Analyze the context surrounding the first outcry.

Search for evidence of 'Motive to Fabricate' or 'Parental Alienation':
- Temporal Proximity: How close was the first accusation to a significant legal event (divorce filing, custody ruling, disciplinary event)?
- The 'Adult Voice': Identify phrases in the child's statement that sound like they were mimicked from an adult.
- The 'Reward' System: Is there any evidence the child received special privileges, gifts, or lack of discipline from the other parent immediately following a disclosure?

Output: A summary titled 'Indicators of External Influence and Coaching.'
```

## Prompt E — Escalation Tracker

```
Trace the evolution of the allegations from the very first mention through to the final police report.

Step 1: What was the original claim? (Usually simple or vague).
Step 2: How did the claim change after each interview? Look for new, more graphic details that were 'remembered' only after speaking with investigators or therapists.
Step 3: Highlight contradictions. Where does the story of the same event change completely between versions?

Output: A chronological list showing the 'Growth of the Allegation' over time.
```

## Golden Rule for NotebookLM

If answers are too generic or neutral, use this follow-up:
```
You are being too neutral. Rewrite that last response, but assume the police officer is mistaken or lying. How does the evidence look then?
```
