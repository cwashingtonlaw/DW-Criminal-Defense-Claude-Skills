# Daubert/Foret Reliability Framework

## The Louisiana Standard

Louisiana adopted a modified Daubert framework in **State v. Foret, 628 So.2d 1116 (La. 1993)**. Under **La. C.E. Art. 702**, a witness qualified as an expert by knowledge, skill, experience, training, or education may testify in the form of an opinion or otherwise if:

1. The expert's scientific, technical, or other specialized knowledge will assist the trier of fact to understand the evidence or to determine a fact in issue;
2. The testimony is based upon sufficient facts or data;
3. The testimony is the product of reliable principles and methods; and
4. The expert has reliably applied the principles and methods to the facts of the case.

The trial court serves as a **gatekeeper** with a duty to ensure that expert testimony is both relevant and reliable before it reaches the jury. *Daubert v. Merrell Dow Pharmaceuticals, Inc.*, 509 U.S. 579 (1993); *State v. Foret*, 628 So.2d at 1121-22.

---

## The Five-Factor Reliability Analysis

Apply each factor to the expert's specific methodology and testimony. Not every factor applies in every case, and additional factors may be relevant. *Kumho Tire Co. v. Carmichael*, 526 U.S. 137, 141 (1999).

### Factor 1: Testability (Can the Theory or Technique Be Tested?)

**What to evaluate:**
- Is the expert's method empirically testable? Can it be subjected to controlled experiments that would reveal its accuracy or inaccuracy?
- Has the method actually been tested, or is it based solely on the expert's subjective judgment and experience?
- If tested, were the test conditions representative of real-world casework conditions, or were they artificially favorable?

**Discipline-specific considerations:**
- DNA: Probabilistic genotyping software should be validated with ground-truth samples of known composition. Has the specific software version been validated for the number of contributors and DNA quantity in this case?
- Fingerprints: ACE-V is testable in principle, but real-world testing (e.g., the FBI/Noblis Black Box study) reveals error rates the discipline historically denied.
- Firearms: AFTE criteria for "sufficient agreement" are subjectively applied; testing studies (Ames Laboratory, Miami-Dade) show measurable error rates.
- Bloodstain Pattern Analysis: Pattern interpretation is largely subjective; limited empirical testing exists for most classification and origin determinations.

**Key authority:** *Daubert*, 509 U.S. at 593 ("Scientific methodology today is based on generating hypotheses and testing them to see if they can be falsified"); *Foret*, 628 So.2d at 1121.

### Factor 2: Peer Review and Publication

**What to evaluate:**
- Has the methodology been published in peer-reviewed scientific literature?
- Has the methodology been subjected to critical scrutiny by other scientists in the field?
- Has peer review revealed limitations, criticisms, or concerns about the method?
- Distinguish between the general methodology (which may be published) and the specific application in this case (which may not have been subjected to peer review).

**Discipline-specific considerations:**
- Some forensic disciplines have extensive peer-reviewed literature (DNA, toxicology) while others have relatively little (bloodstain pattern analysis, firearm/toolmark comparison).
- Publication in "trade" journals (e.g., AFTE Journal) that are reviewed primarily by practitioners rather than independent scientists carries less weight than publication in journals with independent scientific peer review.
- The PCAST Report (2016) and NAS Report (2009) provide comprehensive assessments of the peer-reviewed literature supporting various forensic disciplines.

**Key authority:** *Daubert*, 509 U.S. at 593-94; *Foret*, 628 So.2d at 1121-22.

### Factor 3: Known or Potential Error Rate

**What to evaluate:**
- Does the methodology have an established error rate?
- If so, what is it? Is the expert aware of it? Will the expert acknowledge it in testimony?
- Was the error rate established under conditions comparable to this case?
- If no error rate exists, why not? Is the discipline resistant to error rate testing?

**Key authority:** *Daubert*, 509 U.S. at 594; *Foret*, 628 So.2d at 1122; *General Electric Co. v. Joiner*, 522 U.S. 136, 146 (1997) (court may examine "analytical gap" between data and opinion).

### Factor 4: Standards Controlling the Technique

**What to evaluate:**
- Do published standards exist for the methodology? Which standards body issued them (OSAC/NIST, SWGDAM, AFTE, IABPA, etc.)?
- Did the expert follow the applicable standards in this case?
- Were quality assurance and quality control measures employed?
- Was the analysis performed in an accredited laboratory? Was the accreditation current at the time of analysis?

**Key authority:** *Daubert*, 509 U.S. at 594; *Foret*, 628 So.2d at 1122.

### Factor 5: General Acceptance

**What to evaluate:**
- Is the methodology generally accepted in the relevant scientific community?
- Distinguish between the relevant scientific community (scientists who study the methodology) and the practitioner community (analysts who use it). A method may be accepted by practitioners but criticized by independent scientists.
- Has the methodology been challenged or questioned by authoritative scientific bodies (NAS, PCAST, NIST)?

**Key authority:** *Daubert*, 509 U.S. at 594 (general acceptance remains a factor but is no longer the sole test); *Foret*, 628 So.2d at 1122; *Frye v. United States*, 293 F. 1013 (D.C. Cir. 1923) (general acceptance was the exclusive test under Frye -- Louisiana no longer follows Frye alone).

---

## Additional Factors Beyond Daubert

### The Analytical Gap (Joiner)
Is there too great an analytical gap between the data and the expert's conclusion? Does the opinion logically follow from the methodology and data, or has the expert "leaped" to a conclusion not supported by the analysis? *General Electric Co. v. Joiner*, 522 U.S. 136, 146 (1997).

### Litigation-Driven Opinion
Whether the expert developed the opinion for litigation. An opinion developed specifically for testimony, rather than flowing from independent research, warrants heightened scrutiny. *Daubert v. Merrell Dow Pharmaceuticals, Inc.* (Daubert II), 43 F.3d 1311, 1317 (9th Cir. 1995).

### Kumho Flexibility
For non-scientific expert testimony (experience-based testimony), the court has discretion to determine which reliability factors are relevant. *Kumho Tire*, 526 U.S. at 150-52.

---

## Daubert/Foret Challenge Framework Template

For each expert the attorney seeks to exclude or limit, use this framework:

```
DAUBERT/FORET CHALLENGE FRAMEWORK
Expert: [Name]
Discipline: [Field]
Classification: [EXCLUDE / LIMIT]

I.   QUALIFICATION DEFICIENCIES
     [Specific gaps in credentials, training, or experience
      that undermine qualification under Art. 702]

II.  RELIABILITY ANALYSIS
     Factor 1 -- Testability: [Assessment]
     Factor 2 -- Peer Review: [Assessment]
     Factor 3 -- Error Rate: [Assessment]
     Factor 4 -- Standards: [Assessment]
     Factor 5 -- General Acceptance: [Assessment]
     Analytical Gap (Joiner): [Assessment]

III. RELEVANCE / FIT
     [Does the testimony "fit" the facts of the case?
      Is the expert applying their methodology to the
      specific facts, or offering a generic opinion?]

IV.  RECOMMENDED MOTION
     [Motion to Exclude Expert Testimony / Motion in Limine
      to Restrict Scope / Daubert Hearing Request]

V.   KEY AUTHORITIES
     [Case law and scientific literature supporting the challenge]

VI.  ANTICIPATED STATE RESPONSE & REBUTTAL
     [What the State will argue in opposition and how to counter]
```