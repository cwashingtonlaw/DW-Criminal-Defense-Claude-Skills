# Module B — Digital Evidence Chain Audit

## Module Overview (carried over from SKILL.md)

Digital evidence requires a specialized chain of custody analysis because digital data can be altered without leaving physical traces. Audit the seven integrity checkpoints — seizure & initial handling, write-blocking verification, forensic imaging, hash value verification, storage of digital evidence, analysis documentation, and reporting & court presentation. The chain must document not only physical transfers but also the integrity of the data at every stage.

Digital evidence requires a specialized chain of custody analysis because digital data can be altered without leaving physical traces. The chain must document not only physical transfers but also the integrity of the data at every stage.

## Digital Evidence — The Seven Integrity Checkpoints

**Checkpoint 1 — Seizure & Initial Handling:**
- Was the device powered on or off at the time of seizure? Was this documented?
- If powered on, was the device isolated from network connections (airplane mode, Faraday bag) to prevent remote wiping or data alteration?
- Was the device handled by personnel trained in digital evidence handling?
- Was the device photographed in situ showing its condition, screen state, and any visible identifiers (serial numbers, model numbers)?
- Was the device placed in an appropriate container (anti-static bag for storage media, Faraday bag for mobile devices)?

**Checkpoint 2 — Write-Blocking Verification:**
- Before any examination or imaging, was a validated write-blocker used to prevent any modification of the original storage media?
- Was the write-blocker hardware or software? Was it validated (NIST CFTT tested)?
- Is the write-blocker verification documented in the forensic report (make, model, firmware version, validation status)?
- If no write-blocker was used, was there any documented justification? (There is no valid justification for skipping write-blocking in standard forensic examinations.)

**Checkpoint 3 — Forensic Imaging:**
- Was a forensic image (bit-for-bit copy) created from the original media?
- What imaging tool was used (FTK Imager, dd, Cellebrite, GrayKey)? Was the tool validated?
- Was the imaging process documented (start time, end time, source device, destination media, any errors)?
- Was a verification image (second copy) created from the original for redundancy?
- Was the original media preserved unaltered after imaging?

**Checkpoint 4 — Hash Value Verification:**
- Was a cryptographic hash value (MD5, SHA-1, or SHA-256) calculated for the original media before imaging?
- Was a hash value calculated for the forensic image after creation?
- Do the source and image hash values match? If not, the image is not a faithful copy and analysis results are unreliable.
- Were hash values recalculated at every subsequent transfer point and upon lab receipt?
- Are hash values documented in the chain of custody paperwork (not just in the forensic report)?

**Checkpoint 5 — Storage of Digital Evidence:**
- Was the original device stored separately from the forensic image/working copies?
- Was the original device stored in a manner preventing accidental power-on, battery drainage, or physical damage?
- Were forensic images stored on verified, clean media?
- Were working copies (analysis copies) clearly distinguished from the forensic image (evidentiary copy)?
- Was access to the original device and forensic image restricted and logged?

**Checkpoint 6 — Analysis Documentation:**
- Was all analysis performed on a working copy (not the original or the evidentiary forensic image)?
- Were analysis tools and versions documented?
- Were search terms, filters, and examination parameters recorded?
- Were findings traceable to specific file paths, offsets, or record identifiers in the forensic image?
- Were hash values of individual extracted files documented where relevant?

**Checkpoint 7 — Reporting & Court Presentation:**
- Does the forensic report reference the chain of custody for the original device and the forensic image?
- Can the analyst testify to the complete chain from seizure through analysis?
- Were any exhibits (printed screenshots, extracted data) created from the verified forensic image or from an unverified source?
- Has the original device been available for defense examination? If the defense was denied access to the original (or to the forensic image), this is a due process concern.

## Digital Evidence Chain — Red Flag Matrix

| Red Flag | Severity | Why It Matters |
|----------|----------|---------------|
| No write-blocker used or documented | CRITICAL | Original data may have been modified during examination — all analysis results are unreliable |
| Hash values missing at any transfer point | CRITICAL | Data integrity cannot be verified — no assurance the data analyzed is the data seized |
| Source and image hash values do not match | CRITICAL | The forensic image is not a faithful copy — analysis results are derived from altered data |
| Analysis performed on original media (not working copy) | CRITICAL | Original evidence may have been modified by the analysis process |
| No Faraday bag or network isolation for seized mobile device | SIGNIFICANT | Remote wipe, remote data modification, or incoming communications may have altered device contents |
| Forensic image stored on reused (non-wiped) media | SIGNIFICANT | Pre-existing data on the storage media may contaminate the forensic image |
| Hash values documented only in the forensic report, not on chain of custody forms | SIGNIFICANT | Chain of custody documentation does not independently verify data integrity at transfer points |
| Device powered on during seizure with no documentation of screen state or activity | MINOR to SIGNIFICANT | Running processes may have modified data; active communications may have altered message records |
| Working copy not distinguished from evidentiary copy | MINOR | Risk of confusion between verified evidence and analysis artifacts |

## Digital Evidence — Key Standards

| Standard | Source | Application |
|----------|--------|------------|
| NIST SP 800-86 | National Institute of Standards and Technology | Guide to Integrating Forensic Techniques into Incident Response — foundational digital forensics methodology |
| NIST CFTT | Computer Forensic Tool Testing Program | Write-blocker and imaging tool validation |
| SWGDE (Scientific Working Group on Digital Evidence) | Best Practices for Computer Forensics, Mobile Device Forensics | Digital evidence handling, examination, and reporting |
| ISO 27037 | International Organization for Standardization | Guidelines for identification, collection, acquisition, and preservation of digital evidence |
| ACPO Good Practice Guide | Association of Chief Police Officers (UK, widely adopted) | Four principles of digital evidence: no action should change data, access must be competent, audit trail must exist, case officer is responsible |
| FBI RCFL (Regional Computer Forensic Laboratory) | FBI | Operating procedures for federal digital forensic examination |

## Top CRITICAL Red Flags at a Glance

Summary bullets carried over from SKILL.md Module B; the full matrix above is authoritative.

- No write-blocker used or documented — original data may have been modified during examination
- Hash values missing at any transfer point — data integrity cannot be verified
- Source and image hash values do not match — forensic image is not a faithful copy
- Analysis performed on original media (not working copy) — original evidence may have been modified
