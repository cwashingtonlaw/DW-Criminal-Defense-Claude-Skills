# Mobile Forensic Extraction Audit Report Structure

Read at STEP 5 (Generate the Forensic Audit Report) of `dw-mobile-forensic-auditor-crim/SKILL.md` — the full seven-section report template.

### Output Structure

Produce a structured audit report with the following sections:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MOBILE FORENSIC EXTRACTION AUDIT
Daniels & Washington | [Case Name / Docket No.]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEVICE:        [Make / Model / OS Version]
TOOL:          [Name / Version]
EXTRACTION:    [Type: Logical / Adv. Logical / FFS / Physical]
EXAMINER:      [Name / Agency / Certifications]
DATE:          [Extraction Date]
HASH VERIFIED: [Yes — MD5: ___ SHA-256: ___ / No / Not Documented]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1: METHODOLOGY ADEQUACY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Extraction level classification, adequacy assessment against
charge severity, specific data categories forfeited by chosen
method, recommendation for re-extraction or independent exam]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2: OS SECURITY ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[OS-specific security layers, encryption state, tool
validation status for this OS version, barriers that may
have prevented complete extraction, undocumented risks]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3: TOOL INTEGRITY ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Known vulnerabilities, validation status, exploit
mitigation posture, Signal/Cellebrite findings if
applicable, proprietary exploit concerns]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4: CHAIN OF CUSTODY & PROCEDURAL GAPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Seizure-to-extraction timeline, storage conditions,
USB Restricted Mode status, device state documentation,
any gaps or anomalies]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5: CROSS-EXAMINATION AMMUNITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Numbered list of specific challenges, each with:
 - The deficiency
 - Why it matters
 - Suggested cross question
 - Source/exhibit reference
 - Applicable legal authority]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 6: DEFENSE ACTION ITEMS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Prioritized list:
 ⚖ Motion to Suppress (grounds)
 ⚖ Motion to Compel Re-Extraction / Independent Exam
 ⚖ Daubert / La. C.E. Art. 702 Challenge
 📋 Missing Discovery Demand items
 📋 Expert Witness needs
 📋 Items for Cross-Exam Architect skill]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 7: DISCOVERY GAP REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Expected forensic documentation not provided:
 - Extraction logs
 - Hash verification records
 - Tool validation certificates
 - Examiner CV / training records
 - Device intake photographs
 - Write-blocker documentation
 - Warrant / consent form
 Each with: why it matters + add to Missing Discovery Demand?]
```
