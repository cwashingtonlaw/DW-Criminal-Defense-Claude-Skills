# Tool Integrity & Known Issues

Read at STEP 4 (Tool Integrity & Bypass Capability Audit) of `dw-mobile-forensic-auditor-crim/SKILL.md` — the adversarial-landscape framing and tool-by-tool known issues.

### The Adversarial Landscape of Forensic Tools
Commercial forensic tools operate in an adversarial environment: they exploit security vulnerabilities in consumer devices to extract data. This creates a fundamental reliability tension — **the same software vulnerabilities that enable extraction can compromise the integrity of the extracted data.**

### Cellebrite UFED / Cellebrite Premium — Known Issues

**Signal/Cellebrite Vulnerability Disclosure (April 2021):**
Signal's creator Moxie Marlinspike published research demonstrating that Cellebrite's UFED software contained critical security vulnerabilities:
- Cellebrite UFED loaded and executed unsigned code from the device being analyzed — meaning a crafted file on the target device could modify the extraction report, add fabricated data, or alter existing data without leaving an audit trail
- The software shipped with outdated FFmpeg DLLs (dating back years without security patches) containing known exploits
- Cellebrite's own software lacked basic exploit mitigations (ASLR, DEP) that are standard in consumer software

**Defense Implications:**
> If the extraction was performed with a Cellebrite UFED version predating the remediation of these vulnerabilities, the integrity of the entire extraction report is questionable. The examiner must establish: (1) the exact Cellebrite software version used, (2) whether that version contained the disclosed vulnerabilities, (3) what controls were in place to prevent report modification, and (4) whether the software has been independently validated for forensic reliability under *Daubert* / La. C.E. Art. 702.

### GrayKey (Grayshift) — Known Limitations
- Capability is highly iOS-version-dependent; Apple frequently patches exploited vulnerabilities
- GrayKey extraction capabilities degrade with each iOS update — a successful extraction on iOS 15.2 does not validate the tool for iOS 16.1
- GrayKey relies on undisclosed (proprietary) exploits — no peer review, no published methodology, no independent validation
- Extraction time estimates vary wildly (hours to days for passcode brute force) — verify actual extraction duration vs. tool's expected range for this passcode complexity

### MSAB XRY / Magnet AXIOM — Audit Points
- Cross-reference tool version against the vendor's published validation reports for the specific device
- Check whether the tool performed parsing (interpreting data) vs. acquisition (imaging data) — parsing introduces interpretation layers that can be challenged
- Verify that the tool's SQLite parser handled WAL (Write-Ahead Logging) files correctly — incorrect WAL merging is a known source of phantom artifacts and duplicated records
