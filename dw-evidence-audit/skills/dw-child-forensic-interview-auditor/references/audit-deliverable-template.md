# Audit Deliverable Template, Severity Classification & Cross-Exam Seeds

This reference covers the deliverable format for the Forensic Interview Audit (Word .docx export), the severity classification system used to rate findings, and the cross-examination seed format that feeds `dw-cross-exam-architect`.

## Severity Classification System

### **CRITICAL FINDINGS**
Any one of the following mandates strong defense argument:

1. **Leading/Suggestive Questions Introduced Core Allegations**
   - Example: Interviewer first mentions "genital touching" in a leading question ("He touched your private parts, didn't he?"), and child confirms
   - Impact: Core allegation not from child's memory; from interviewer's script

2. **Interviewer Provided Details Child Didn't Provide**
   - Example: Child says "He did bad things." Interviewer specifies "He took your clothes off," and child confirms
   - Impact: Child is confirming interviewer's version, not describing independent memory

3. **Repeated Questioning After Denial Until Answer Changed**
   - Example: Child says "No" to "Did he touch you?" Interviewer asks 3 more times. Child eventually says "Maybe" or "Yes"
   - Impact: Child's "Yes" is coerced, not reliable

4. **Complete Protocol Deviation**
   - Example: Stated protocol was NICHD; interview shows no rapport phase, no practice narrative, immediate leading questions
   - Impact: Interview is fundamentally unreliable

5. **No Recording (Audio or Video)**
   - Example: Interview occurred but no recording was made; only interviewer's notes exist
   - Impact: Cannot verify any claims about what questions were asked or how child responded

### **SIGNIFICANT FINDINGS**
Combination of these raises substantial reliability concerns:

1. **Excessive Closed/Yes-No Questions (>60% of questions)**
   - Impact: Child was not invited to provide narrative; interviewer imposed structure

2. **Failure to Explore Alternative Hypotheses**
   - Example: No questions like "Could it have been...?" or "Is it possible...?"
   - Impact: Interviewer appeared committed to one conclusion

3. **Inadequate Ground Rules**
   - Example: Child never told "Say 'I don't know' if you're not sure"
   - Impact: Child may have guessed rather than reported memory

4. **Multiple Interviewers Contaminating (3+ interviews in < 3 months)**
   - Impact: Impossible to distinguish child's original memory from learned details

5. **Developmentally Inappropriate Language**
   - Example: Complex sentence structures or abstract concepts beyond child's age
   - Impact: Child guessing rather than understanding

6. **Interviewer Not Blind to Allegations**
   - Example: Interviewer reviewed police report detailing allegations before interview
   - Impact: Confirmation bias; interviewer interprets ambiguous statements as confirming allegations

### **MINOR FINDINGS**
Technical or procedural concerns that alone are not disqualifying:

1. **Minor Protocol Deviations**
   - Example: RATAC protocol partially followed but not sequenced correctly

2. **Some Rapport-Building Shortcuts**
   - Example: Rapport phase was 2 minutes instead of 5-10 minutes

3. **Technical Recording Issues**
   - Example: Audio quality is subpar but intelligible

---

## Audit Deliverable Template (Word .docx)

When analysis is complete, generate a formal audit document in Word format with this structure:

### **Header:**
```
FORENSIC INTERVIEW AUDIT
[Case Name / Client Name]
[Date]
[Auditing Firm/Attorney Name]

CONFIDENTIAL — WORK PRODUCT
ATTORNEY-CLIENT PRIVILEGED
```

### **Executive Summary (1 page)**
- Child's age at interview
- Interview date and interviewer name/credentials
- Allegation(s) the interview was meant to investigate
- Overall severity rating: CRITICAL / SIGNIFICANT / MINOR
- 3-5 sentence summary of primary concerns

### **Methodology (½ page)**
- Protocols audited
- Modules applied
- Materials reviewed (recordings, transcripts, prior statements, etc.)

### **FINDINGS BY MODULE**

**Module A: Interviewer Qualifications**
- Certification status
- Training hours and protocols
- Experience level
- Bias/contamination control training
- Findings: [CRITICAL/SIGNIFICANT/MINOR]

**Module B: Environment & Setup**
- Location, recording equipment
- Personnel present
- Pre-interview contamination check
- Findings: [CRITICAL/SIGNIFICANT/MINOR]

**Module C: Rapport & Ground Rules**
- Rapport phase duration and quality
- Ground rules explicitly stated?
- Practice narrative provided?
- Findings: [CRITICAL/SIGNIFICANT/MINOR]

**Module D: Questioning Technique**
- [DETAILED TABLE: Question-by-question analysis with classification, score, analysis]
- Cumulative question score
- Ratio analysis (% open vs. % closed vs. % leading)
- Specific problematic techniques identified
- Findings: [CRITICAL/SIGNIFICANT/MINOR]

**Module E: Disclosure Analysis**
- Spontaneous vs. prompted
- Consistency across interviews
- Detail quality (sensory, peripheral, contextual)
- Findings: [CRITICAL/SIGNIFICANT/MINOR]

**Module F: Multi-Interview Contamination**
- [TABLE: All prior interviews documented]
- Contamination risk assessment
- Source monitoring failures
- Findings: [CRITICAL/SIGNIFICANT/MINOR]

**Module G: Developmental Competency**
- Child's language/memory/suggestibility profile
- Age-appropriate assessment
- Research-based vulnerabilities
- Competency score
- Findings: [CRITICAL/SIGNIFICANT/MINOR]

**Module H: Post-Interview Contamination Indicators**
- Temporal proximity analysis (legal events vs. disclosure timeline)
- Adult voice detection (age-inappropriate terminology tracing)
- Reward system documentation
- Findings: [CRITICAL/SIGNIFICANT/MINOR]

**Module I: Multi-Interview Comparative Analysis (Escalation Tracker)**
- Original claim extraction (first mention)
- Narrative evolution across sequential interviews
- Contradiction tracking between interview versions
- Findings: [CRITICAL/SIGNIFICANT/MINOR]

**Module J: External Validity Cross-Check (Behavioral Baseline)**
- School attendance correlation with abuse timeline
- Academic performance baseline comparison
- Behavioral incident analysis during alleged abuse period
- Findings: [CRITICAL/SIGNIFICANT/MINOR]

### **Consolidated Findings & Severity Rating**

| Finding | Module | Severity | Explanation |
|---------|--------|----------|-------------|
| [Finding #1] | [Module] | CRITICAL/SIGNIFICANT/MINOR | [Explanation] |
| [Finding #2] | | | |

**Overall Assessment:** Statements have [HIGH/MODERATE/LIMITED] reliability for purposes of [specific allegation].

### **Legal Analysis**

See `references/legal-authority-and-research.md` for the full Daubert / Crawford / Davis / Idaho v. Wright / La. C.E. 801-803 / La. C.E. 702 / La. Ch.C. 329 / State v. Langley framework. Apply each section in turn against the audit findings; conclude whether the interview methodology meets the relevant admissibility/reliability standard.

### **Cross-Examination Seeds for dw-cross-exam-architect**

```
Chapter 1: Interviewer's Pre-Interview Bias
Witness: [Interviewer Name]
Goal: Establish that interviewer had predetermined conclusion before interview.
Source: [Police report dated X, reviewed by interviewer before interview; see discovery doc page Y]
Key Questions:
1. "Before you began the interview on [date], had you reviewed the police report alleging [specific allegation]?"
2. "What specific language in that report influenced your expectations for what [child] would say?"
3. "Did you design your questions to test the police report's allegations, or to let [child] freely describe what happened?"
Impeachment: [If interviewer answers "I was neutral," produce questions that confirm allegations like "He touched you down here, right?"]

Chapter 2: Leading Question #7 — Genital Touching
Witness: [Interviewer Name]
Goal: Show that interviewer introduced genital-touching allegation, not child.
Source: [Interview transcript page 8, question 47]
Key Questions:
1. "At that point in the interview, had [child] yet mentioned any genital touching?"
2. "Why did you ask the question, 'He touched you down here, didn't he?' using the anatomical doll?"
3. "Did you intend that question to suggest what kind of touching you expected [child] to describe?"
Impeachment: [If interviewer denies suggestion, note this was the FIRST mention of genitals in the interview; all subsequent disclosures of genital abuse follow this question.]

Chapter 3: Repeated Questioning After Denial
Witness: [Interviewer Name]
Goal: Show coercive pressure.
Source: [Interview transcript pages 10-12, questions 58-65]
Key Questions:
1. "When [child] first answered your question about whether [suspect] touched his private parts, what was [child]'s answer?"
2. "When [child] said no the first time, why did you ask the same question again?"
3. "After [child] said no three times, what made you ask, 'Some kids don't like to talk about this, but did he?'"
Impeachment: [Child eventually said "maybe" or "yes," but only after denying 3+ times; this indicates pressure, not reliable memory.]
```
