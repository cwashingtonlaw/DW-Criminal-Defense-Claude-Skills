# Quick Reference Tables

Read from the Quick Reference sections of `dw-mobile-forensic-auditor-crim/SKILL.md` (used throughout the audit) — legal standards for digital forensic evidence and common forensic tool versions with known issues.

## Legal Standards for Digital Forensic Evidence

| Situation | Authority |
|-----------|-----------|
| Expert testimony reliability | La. C.E. Art. 702; *Daubert v. Merrell Dow* |
| Suppression of illegally obtained evidence | La. C.Cr.P. Art. 703; 4th Amendment |
| Cell phone search warrant requirement | *Riley v. California*, 573 U.S. 373 (2014) |
| Historical cell-site location info | *Carpenter v. United States*, 585 U.S. 296 (2018) |
| Good faith exception | *United States v. Leon*, 468 U.S. 897 (1984) |
| Warrant particularity (digital) | *United States v. Ganias*, 824 F.3d 199 (2d Cir. 2016) |
| Authentication of digital evidence | La. C.E. Art. 901; Fed. R. Evid. 901(b)(9) |
| Best evidence rule (digital) | La. C.E. Art. 1001–1004 |
| Brady obligations (withheld exculpatory data) | *Brady v. Maryland*; *Giglio v. United States* |
| Chain of custody | La. C.E. Art. 901(B)(1); *State v. Toney* |

*Adapt all rules when jurisdiction toggle is set to federal or another state.*

## Common Forensic Tool Versions & Known Issues

| Tool | Known Concern | Defense Action |
|------|--------------|----------------|
| Cellebrite UFED (pre-2021 patch) | Signal vulnerability disclosure — unsigned code execution, report tampering risk | Demand version number; challenge under Art. 702 |
| Cellebrite UFED (all versions) | Proprietary parsing — no open-source validation | Request raw database files, not just parsed reports |
| GrayKey (all versions) | Undisclosed proprietary exploits — no peer review | Challenge as unreliable methodology under *Daubert* |
| MSAB XRY | SQLite WAL merging errors documented | Request raw .db + .wal files for independent verification |
| Magnet AXIOM | Parsing layer can create phantom artifacts | Distinguish acquisition artifacts from parsed interpretations |
| Oxygen Forensic Detective | Limited FFS capability on newer devices | Verify extraction type actually achieved vs. attempted |
