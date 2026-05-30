# Module B — Witness Interview Questionnaire Builder

Generate case-specific interview questionnaires tailored to the witness type and their role in the case.

## Witness Classification

| Witness Type | Interview Approach |
|---|---|
| **Prosecution Eyewitness** | Challenge perception, memory, bias; establish inconsistencies with physical evidence |
| **Prosecution Expert** | Not typically interviewed by defense investigator; flag for attorney/defense expert |
| **Prosecution Character Witness** | Explore basis of knowledge, bias, relationship limitations |
| **Defense Alibi Witness** | Corroborate defendant's account; establish specificity and reliability of recollection |
| **Defense Character Witness** | Establish community knowledge, specific instances of relevant character traits |
| **Defense Fact Witness** | Establish facts favorable to defense theory |
| **Neutral/Bystander Witness** | Open-ended exploration; determine what they observed without leading |
| **Reluctant/Hostile Witness** | Careful rapport building; document refusal if witness declines |
| **Law Enforcement Witness** | Generally not interviewed directly; investigate through records and prior testimony |

## Standard Interview Questionnaire Structure

Every witness interview questionnaire must include these sections:

**Section 1: Interview Administration**
- Date, time, and location of interview
- Investigator name and license number
- Witness full legal name, DOB, address, phone, email, employer
- Relationship to defendant, victim, and other witnesses
- Prior contact with law enforcement regarding this case
- Prior contact with prosecution regarding this case
- Consent to interview (document verbal consent at minimum)
- Recording consent (Louisiana is a one-party consent state — La. R.S. 15:1303)

**Section 2: General Background**
- How long have you lived at your current address?
- Where were you living at the time of the incident?
- What is your current employment?
- What was your employment at the time of the incident?
- Do you have any prior convictions? (Relevant for impeachment under La. C.E. Art. 609)
- Do you have any pending criminal cases?
- Have you been promised anything or threatened in connection with this case?
- Have you been contacted by any attorney, investigator, or law enforcement about this case?

**Section 3: Case-Specific Questions**
- [Generated based on witness type and case facts — see below]

**Section 4: Perception and Memory Foundations**
- Where exactly were you when you observed/experienced [event]?
- What was the lighting like?
- What was the weather like?
- How far away were you from [event/person]?
- Were there any obstructions to your view?
- How long did you observe [event/person]?
- Were you under the influence of any substances at the time?
- Do you have any vision or hearing impairments?
- When did you first report what you observed? To whom?
- Have you discussed your observations with anyone else?
- Have you reviewed any media coverage of this case?
- Have you seen any photos or social media posts about this case?

**Section 5: Prior Statement Comparison**
- [If witness gave a prior statement to law enforcement, generate questions addressing each factual assertion in that statement]
- Is there anything in your prior statement that you would like to correct, clarify, or add to?
- Did the officer accurately record what you told them?
- Did you review your statement before signing it?
- Were you under any stress, pressure, or influence when you gave your prior statement?

**Section 6: Closing**
- Is there anything else you think is important that I haven't asked about?
- Is there anyone else you think I should speak with about this case?
- Would you be willing to testify in court about what you've told me today?
- May I contact you again if I have follow-up questions?
- [Provide investigator contact information]

## Case-Specific Question Generation Rules

When generating Section 3 questions, apply these rules based on case type:

**Identification Cases:**
- Walk through the identification process step by step
- Cross-racial identification factors
- Suggestiveness of identification procedure
- Prior familiarity with defendant
- Confidence level at time of initial identification vs. now
- Exposure to photos, media, or other images of defendant between event and identification
- Description provided before identification vs. defendant's actual appearance

**Self-Defense Cases:**
- Who was the initial aggressor?
- What specific actions did each party take, in order?
- Did the defendant attempt to retreat or de-escalate?
- What was the relative size/strength of the parties?
- Were any weapons visible or used?
- What was the defendant's demeanor before, during, and after?
- What was the alleged victim's demeanor and reputation for violence?

**Drug Cases:**
- Where exactly were the substances found?
- Who had access to that location?
- Did you see the defendant in possession of any substances?
- Describe the packaging
- Were there any signs of personal use vs. distribution?
- Who else was present?
- What was the basis for the initial stop or search?

**DUI/DWI Cases:**
- Describe the defendant's driving pattern
- What first drew your attention?
- Describe the defendant's appearance, speech, and behavior
- Did you observe any field sobriety testing?
- Were there any medical conditions or physical limitations you noticed?
- Road and weather conditions
- Time between your observation and law enforcement contact
