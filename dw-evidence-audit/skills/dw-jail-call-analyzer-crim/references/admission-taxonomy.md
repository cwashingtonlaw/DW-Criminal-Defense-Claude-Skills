# Admission Taxonomy & Damage-Severity Scoring

Used by `dw-jail-call-analyzer-crim` Module B. Provides the canonical admission categories, the damage-severity rubric, and worked examples to anchor the scoring.

## The Seven Admission Categories

### 1. Location Admissions

Statements that place the client at, near, or away from a relevant location.

**Direct location admissions** — explicit references to a place tied to the offense or to a contested element (e.g., "I was at Joe's that night," "we drove through the cut-through behind the church"). Highest evidentiary value because the State can corroborate with surveillance, cell-site, or witness testimony.

**Indirect location admissions** — references that imply presence (e.g., "yeah, I saw him too when we were over there," "the cops rolled up like five minutes after we left"). Often more damaging than direct admissions because they feel casual and seem more credible to a jury.

**Negative location admissions** — statements placing the client *away* from the scene. These can be Module C exculpatory content if consistent and credible. They become Module B damage if they later prove false (the State will use them to show consciousness of guilt or to anchor a perjury argument).

### 2. Association Admissions

Statements that place the client with co-defendants, witnesses, or other charged parties.

Pay particular attention to first-person plural pronouns — "we," "us," "our" — when the antecedent is a co-defendant or charged party. A phrase like "after we got out of the car" is an association admission even if no co-defendant is named, provided context establishes who "we" refers to. The State will argue the antecedent at trial; preempt the argument by flagging the call.

Also flag references to coordination ("I told Marcus to..."), shared possession ("we had it in the trunk"), or shared knowledge ("everybody knew about..."). Each coordination reference carries additional weight if the case involves a conspiracy or principal-and-aider charge under La. R.S. 14:24.

### 3. Possession Admissions

Statements regarding possession or control of contraband, weapons, vehicles, phones, or other charged items.

Possession admissions are case-defining in drug, firearm, and stolen-property cases. Distinguish:

- **Actual possession admissions** — "I had it on me," "the phone was in my pocket"
- **Constructive possession admissions** — "I knew it was in the apartment," "the gun was under the seat"
- **Joint possession admissions** — "we kept it at the spot"
- **Past possession admissions** — "I used to have one like that" (rarely admissible substantively but high cross-exam fodder if the client testifies otherwise)

### 4. Intent / Motive Admissions

Statements bearing on mental state, plan, motive, knowledge, or specific intent.

Mental-state evidence is hard to prove and easy to lose, so intent admissions on calls are gold for the prosecutor. Flag any reference to:

- Pre-offense planning ("we'd been talking about it for weeks")
- Post-offense rationalization ("he had it coming")
- Knowledge of risk or consequence ("I knew it could go bad")
- References to specific intent elements (premeditation in homicide, intent to distribute in narcotics, intent to defraud in fraud cases)
- Statements bearing on heat-of-passion or sudden-quarrel mitigation (relevant to Louisiana manslaughter under La. R.S. 14:31)

### 5. Prior-Conduct Admissions

References to prior bad acts, prior arrests, prior charged conduct, or prior similar incidents. **404(B) exposure category.**

Most prior-conduct admissions are not directly admissible as character evidence, but the State may seek admission under La. C.E. Art. 404(B)'s motive-opportunity-intent-preparation-plan-knowledge-identity-absence-of-mistake exceptions. A jail-call admission to a prior similar offense is precisely the kind of "specific instance of conduct" the State will seek to introduce.

Cross-feed every Module B Category-5 flag to `dw-404b-opposition-crim` so the defense can prepare a 404(B) opposition before the State files notice.

### 6. Consciousness-of-Guilt Admissions

Statements indicating awareness of wrongdoing or efforts to avoid accountability:

- Flight or hiding ("I shouldn't have run but I panicked")
- Asset disposal ("we got rid of the car," "I tossed it in the bayou")
- Witness avoidance or coordination (cross-feeds to Module D)
- Story development ("here's what happened — make sure you tell it the same way")
- Instructions to others to lie or to refuse cooperation
- Awareness of the recording itself ("they record everything in here, watch what you say") — paradoxically, this admission is itself consciousness-of-guilt evidence because it contextualizes everything that follows on the call

### 7. Theory-of-Defense Contradictions

Any statement inconsistent with the operative defense theory. **The most dangerous category** because the State will use these admissions both substantively and — if the client testifies — as cross-fodder.

Cross-reference every Tier 1 call against the defense theory pulled from `dw-case-brain-crim` in Step 1. Each contradiction must be flagged with:

- The verbatim call statement
- The defense-theory proposition it contradicts
- The severity of the contradiction (does it eliminate the defense, weaken it, or merely complicate it?)

If contradictions are systemic and severe, the audit must escalate to Module B's cumulative-risk narrative and recommend a theory-of-defense reset to the assigned attorney.

## Damage-Severity Scoring (1-5)

Every flagged admission is scored on a 1-5 scale. The score is a function of:

- **Directness** — how explicit is the admission?
- **Voice clarity** — is it unambiguously the client's voice, on a clean recording?
- **Element fit** — does it admit a charged element, or merely surrounding context?
- **Theory contradiction** — does it contradict the defense theory?
- **Corroboration risk** — can the State independently corroborate the admission?

### Severity 5 — Case-Defining

Direct admission to a charged element, on a clear recording, in the client's voice, contradicting the defense theory, that the State can corroborate with independent evidence.

*Example:* In a second-degree murder case where the defense theory is misidentification (the client was not present), the client says on a recorded call: *"Look, I was there but it wasn't supposed to go down like that — Marcus was the one who pulled."* This admits presence (contradicting alibi) and association (placing the client with a co-defendant) and provides the State with both substantive evidence and a guaranteed cross-exam landmine.

### Severity 4 — Severely Damaging

Strong admission with some interpretive flexibility, OR direct admission on a recording that is partially obscured or lacks corroboration.

*Example:* Same case, the client says: *"I told you man, this whole thing — I shouldn't have been over there."* Implies presence ("over there"), expresses regret (consciousness of guilt), but the location is not specified and the statement could be read as a generic regret about associating with the co-defendant rather than presence at the scene.

### Severity 3 — Significant

Material admission requiring context to be damaging. Often a category-2 association admission or a category-1 indirect location admission.

*Example:* Client says: *"After we got back to the apartment, I just wanted to go to sleep."* The "we" implicates association; the "got back" implies prior collective movement; but neither directly admits a charged element. The State will pair it with other circumstantial evidence to build presence and association.

### Severity 2 — Notable but Defensible

Statement that hurts but has a plausible innocent reading or is cumulative with already-known evidence.

*Example:* Client says: *"Yeah I knew Marcus had been into some things, but that's his life, not mine."* Acknowledges association and awareness but explicitly disclaims joint involvement. The State may use it to anchor a relationship; the defense can argue it actually supports separation.

### Severity 1 — Background Concern

Tone, attitude, or peripheral fact that the State might exploit but cannot independently prove an element with. Includes demeanor concerns (laughter at inappropriate moments, bragging, profanity directed at victims), passing references to the criminal justice system that signal familiarity, and lifestyle references that may color the jury's perception.

*Example:* Client laughs and says: *"They got nothing on me though, watch."* Does not admit any element, but the cocky tone is fodder for the prosecutor's closing if the case ever gets to a jury.

## Worked Scoring Examples

| Verbatim Quote | Category | Severity | Reasoning |
|----------------|----------|----------|-----------|
| "I was at the corner of Common and St. Charles when it happened" | Location (direct) | 5 | Places client at scene; corroborable by surveillance |
| "We pulled up around midnight, like I told you" | Location + Association | 4 | "We" = co-defendants; time-frame matches charging window |
| "Marcus had the gun, not me" | Possession (negative) | 3 | Disclaims possession but admits proximity and knowledge — 14:24 principal exposure |
| "I shouldn't have hung around that crew" | Association + Consciousness of guilt | 2 | Vague regret; defense can argue it shows separation |
| "Don't say nothing to the DA, just say you don't remember" | Witness coordination | 5 | Direct obstruction — also Module D CRITICAL |
| "You know how I get when I'm drinking" | Prior conduct | 2 | 404(B) exposure depending on charge; defense can argue inadmissible character |
| "They can't prove nothing without [witness name]" | Witness contact awareness | 4 | Implies knowledge of the State's case structure; close to obstruction if followed by contact |

## Cumulative Theory-of-Defense Risk Assessment

After all individual admissions are scored, the audit must assess the **cumulative** picture:

- **SURVIVABLE** — Theory of defense remains viable; admissions can be explained, contextualized, or kept out via motion.
- **CONTESTED** — Theory of defense is materially weakened by the calls; trial strategy must adapt; consider whether the defense should pivot from a denial theory to a partial-defense / lesser-included theory.
- **RECONSIDER** — The calls are inconsistent with the operative defense theory in fundamental ways. The audit recommends an attorney conference to re-evaluate theory; pleas, lesser-included strategies, or sentencing-focused defense may now dominate.

The cumulative assessment is not the analyzer's call to override the assigned attorney; it is a flag for attorney decision-making. State the cumulative risk plainly, cite the controlling admissions, and let the attorney decide.

## Severity Ladder Cross-Reference

For audit-report consistency, the Module B severity scale (1-5) maps to the consolidated severity table:

- Severity 5 → CRITICAL
- Severity 4 → CRITICAL or SIGNIFICANT (analyst judgment based on element fit)
- Severity 3 → SIGNIFICANT
- Severity 2 → MODERATE
- Severity 1 → MINOR

The consolidated table in Step 3 of the SKILL uses CRITICAL/SIGNIFICANT/MODERATE/MINOR. The Module B numerical scale exists because admission damage is more granular than the four-tier severity scale and because trial-prep teams use the numerical scale to triage clip-selection decisions.
