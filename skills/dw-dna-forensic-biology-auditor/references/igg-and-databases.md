# IGG & Databases — Reference

Deep methodology reference for **Module F — IGG & Databases**. Load when the case involves CODIS hits, Investigative Genetic Genealogy (IGG), or other DNA-database investigative methodology.

---

## 1. CODIS — Combined DNA Index System

### What CODIS Is
A tiered FBI-managed database system housing offender, arrestee, forensic (crime-scene), and missing-persons DNA profiles. Tiers: LDIS (local) → SDIS (state) → NDIS (national). The system performs allele-by-allele matching across the 20 CODIS core loci (expanded from 13 in 2017).

### Upload Eligibility
- **Offender / arrestee profiles** must satisfy statutory authority (typically conviction or qualifying arrest under state law). Louisiana statute: La. R.S. 15:609.
- **Forensic (crime-scene) profiles** must meet quality criteria specified in the FBI QAS — typically a single-source or clearly deduced major profile; complex mixtures are generally not eligible.
- A profile rejected for CODIS upload but used to argue match in court is an audit finding.

### CODIS Hit Workflow
1. State lab uploads a crime-scene profile to LDIS/SDIS/NDIS.
2. Periodic database searches generate a candidate match.
3. The candidate is a **hit**, not a confirmed match — it is an investigative lead only.
4. The lab must perform a **confirmation re-test** comparing the original evidence profile against a freshly collected reference sample from the candidate person before reporting a match.
5. The CODIS administrator's logs (eligibility determinations, hit notifications, confirmation tracking) are discoverable.

**Audit:**
- Was the original CODIS profile eligible for upload per the FBI QAS criteria?
- Was a confirmation re-test performed with a fresh reference?
- Were the original profile, the CODIS hit notification, and the confirmation re-test all preserved and produced in discovery?
- Was the candidate identified and arrested before the confirmation re-test? (If yes, raises probable-cause questions for the arrest.)

### Database-Search Statistics
- A CODIS hit involves searching a database of profiles, not a single comparison. The relevant statistic is not the same as the single-comparison RMP.
- NRC II recommended a "database match probability" adjustment for database searches: divide the per-comparison probability by 1/N where N is the database size. The FBI has historically taken a different position. The defense should probe how the State characterizes the statistic in a CODIS-hit case.

---

## 2. Direct-to-Consumer (DTC) Genealogy Databases

### GEDmatch
- **What it is:** A third-party, free, publicly accessible database where users upload their genetic-genealogy data (SNP profiles from 23andMe, AncestryDNA, etc.) for relative matching and ethnicity analysis.
- **User opt-in regime (since 2019):** Users select whether their profile is visible to law enforcement (LE). GEDmatch users who opt out are not visible to LE searches.
- **Acquired by Verogen (now Qiagen) in 2019** — owner has commercial interest in LE search products.
- **Use in IGG:** Most IGG searches run on GEDmatch's LE-visible pool.

### FamilyTreeDNA
- **What it is:** A DTC genetic genealogy service.
- **Law enforcement program:** FamilyTreeDNA has had a controversial LE matching program; users may opt out.
- **Use in IGG:** Smaller pool than GEDmatch but supplements searches.

### 23andMe
- **Policy:** Has historically resisted law enforcement requests for individual user data without warrant; does not provide IGG-style search access.
- **Closed database:** Not used for routine IGG.

### Ancestry (AncestryDNA)
- **Policy:** Similar to 23andMe — restricts law enforcement access; does not provide search access for IGG.
- **Closed database:** Not used for routine IGG.

### Audit Questions
- Which database(s) did the genealogist search?
- Was each user opted in for law enforcement search?
- Were any non-opted-in profiles accessed (a potential 4th Amendment / terms-of-service issue)?
- Did the genealogist or LE create a fake profile to access additional matches (a documented practice in some IGG investigations)?

---

## 3. Fourth Amendment Issues Post-*Carpenter*

### *Carpenter v. United States*, 585 U.S. 296 (2018)
Held that the third-party doctrine does not extend to historical CSLI; individuals retain a reasonable expectation of privacy in detailed records of their location even when held by third parties. The opinion repeatedly emphasized the unique nature of cell-phone location data but signaled a more nuanced approach to third-party data generally.

### Application to Genetic Genealogy
- **Third-party doctrine question:** Does an individual who uploads their genetic data to GEDmatch retain a reasonable expectation of privacy?
- **Opt-in users** — arguably no, because they consented to LE matching.
- **Non-opt-in users captured via fake profiles or accidental exposure** — strong 4th Amendment argument that LE conducted a search without authority.
- **Defendants identified via a relative's profile** — the most contested area. The defendant did not upload their own DNA; the relative did. Does the defendant have standing to challenge the genealogist's search of the relative's profile? Most courts to date have found no, but the issue is unsettled.

### *Maryland v. King*, 569 U.S. 435 (2013)
Upheld arrestee DNA collection as a reasonable booking procedure. Limited holding; does not extend to DTC databases.

### Particularity and Scope
- Many IGG investigations begin without judicial authorization — the search of GEDmatch is treated by LE as a query of a private database, not a Fourth Amendment search.
- Defense argument: IGG is a general search of millions of individuals' genetic data to find one suspect; lacks particularity required by the 4th Amendment.

### Brady / Discovery Issues
- The IGG methodology — what searches were run, what filters were applied, what assumptions were made about the family tree — is rarely fully documented or produced in discovery.
- Brady demand should specifically cover the genealogist's working notes, draft family trees, candidate-list filtering decisions, and communications between LE and the genealogist.

---

## 4. IGG Workflow

1. **SNP Profile Generation** — the crime-scene evidence DNA is extracted; a SNP profile is generated, typically by a private lab (Parabon NanoLabs, Othram, Verogen). This is **not** the same as a STR profile; the underlying lab methodology is different (microarray or sequencing-based).
2. **Database Upload** — the SNP profile is uploaded to GEDmatch (and possibly FamilyTreeDNA) for relative matching.
3. **Match List** — the database returns putative biological relatives with estimated relationship distance.
4. **Family Tree Construction** — a genealogist (working for the private lab or independently) constructs family trees of the matched individuals to identify common ancestors who could be ancestors of the unknown source.
5. **Candidate Identification** — the genealogist proposes candidates whose family tree position is consistent with being the source.
6. **Confirmation** — law enforcement obtains a reference sample from the candidate (covertly or after arrest) and the lab performs an STR comparison against the original evidence.

### Audit Points Per Step
- **SNP profile generation** — was the lab accredited? Was the methodology *Daubert/Foret*-validated? (See Section 5.)
- **Database upload** — opt-in regime followed? Fake profiles used?
- **Match list** — was the full match list preserved and produced?
- **Family tree construction** — genealogist's notes preserved?
- **Candidate identification** — multiple candidates considered? Were any candidates excluded incorrectly?
- **Confirmation** — STR re-test conducted? Original evidence preserved sufficient for re-test?

---

## 5. Lab Transition Issues — Private SNP Labs

### Parabon NanoLabs
- Provides SNP profile generation and IGG genealogist services.
- Some of its earlier methodology has been criticized for limited validation transparency.

### Othram
- Provides SNP profiling, particularly for degraded samples (sequencing-based).
- Aggressive marketing in cold-case work; *Daubert/Foret* validation status varies by jurisdiction.

### Verogen / Qiagen
- Sequencing-based forensic genomics company; owns GEDmatch.
- Provides ForenSeq and related SNP/STR sequencing.

### *Daubert / Foret* Posture for IGG SNP Work
- Most IGG SNP work has not been *Daubert/Foret*-tested in the appellate courts.
- Defense should file pretrial motion to exclude under *Foret* and require the State to lay foundation:
  - Has the method been tested?
  - Has it been subjected to peer review?
  - Known error rate?
  - Standards controlling its operation?
  - General acceptance?
- The IGG output is a candidate identification, not a match. The match is established by the subsequent STR re-test. The defense should clarify whether the State seeks to introduce the IGG methodology or only the confirmation re-test result. If only the re-test, the IGG methodology may still be relevant for:
  - 4th Amendment scope (was the candidate identified through an unlawful search?).
  - Brady (was the candidate list confounded by other candidates also matching?).
  - Reliability of the chain that led to the defendant.

---

## 6. DOJ Interim Policy on IGG (2019, Updated 2021)

The U.S. Department of Justice issued an Interim Policy on Forensic Genetic Genealogical DNA Analysis and Searching (effective November 1, 2019) governing federal IGG use:
- Limits use to violent crimes and unidentified human remains.
- Requires that traditional investigative methods be exhausted first.
- Requires use of GEDmatch and FamilyTreeDNA only (with terms-of-service compliance).
- Prohibits fake profiles.
- Requires confirmation re-test before arrest based on IGG.

**Audit:** Does the IGG investigation in this case comply with the DOJ interim policy? Even where the case is state, the policy is a relevant reference for due-process arguments. State-level policy may differ.

---

## 7. Notable Cases

- **Joseph James DeAngelo / Golden State Killer (2018)** — the first widely publicized IGG identification. Spurred the IGG industry but raised privacy concerns.
- **Numerous subsequent IGG-based identifications** — cold cases dating back decades, plus some current-event cases. Defense challenges have grown.
- ***State v. Hartman*** (Pennsylvania, ongoing) — IGG and related challenges.
- **Maryland v. Phillip Adams**; **Multiple Louisiana cases** — state-level IGG litigation is emerging; track for current developments.

---

## 8. Defense Challenges Summary

| Challenge | Vehicle | Authority |
|---|---|---|
| 4th Amendment — non-opt-in search | Motion to Suppress | *Carpenter* principles; particularity |
| Standing to challenge relative's profile search | Motion to Suppress | Unsettled; argue analogically to 4th Amendment |
| IGG SNP methodology not validated | *Daubert/Foret* | *State v. Foret*; *Daubert*; La. C.E. 702 |
| Brady on IGG methodology, genealogist notes, candidate list | Motion to Compel / Brady motion | *Brady v. Maryland* |
| Fake profile / TOS violation | Motion to Suppress | Property/contract theories; potentially CFAA |
| Confirmation re-test deficiencies | Daubert / chain | *Foret*; foundation |
| Lab accreditation / *Daubert* for SNP private lab | Motion in Limine | *Foret*; La. C.E. 702 |

---

## 9. Audit Checklist — IGG & Databases

- [ ] CODIS hit (if any): original upload eligibility verified
- [ ] CODIS confirmation re-test performed with fresh reference
- [ ] CODIS administrator logs produced
- [ ] IGG SNP-profile lab identified; accreditation and validation documents produced
- [ ] IGG databases searched identified; opt-in status of all matches verified
- [ ] No fake profile / TOS violation
- [ ] Full match list preserved and produced
- [ ] Genealogist's working notes, drafts, candidate-list filtering produced
- [ ] Multiple candidates considered; exclusion of alternatives documented
- [ ] Confirmation STR re-test performed and documented
- [ ] DOJ interim policy compliance assessed (if federal) / analog state policy (if state)
- [ ] *Daubert/Foret* posture of IGG SNP methodology assessed
- [ ] 4th Amendment scope challenge considered
- [ ] Brady demand on full IGG workflow filed if not produced

---

*See also: `louisiana-dna-case-law.md` (Foret/Daubert), `defense-dna-experts.md` (IGG specialists), `statistical-challenges.md` (database-search statistics).*
