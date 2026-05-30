# Quick Reference Tables

## Legal Standards for Social Media Evidence

| Situation | Authority |
|-----------|-----------|
| Authentication requirement | La. C.E. Art. 901(B)(1) (testimony of witness with knowledge); Art. 901(B)(4) (distinctive characteristics) |
| Business records exception (platform records) | La. C.E. Art. 803(6) — requires custodian certification |
| Self-authentication of domestic records | La. C.E. Art. 902(11) — certified domestic records of regularly conducted activity |
| Hearsay — admission by party-opponent | La. C.E. Art. 801(D)(2) — defendant's own statements on social media |
| Best evidence rule (digital) | La. C.E. Art. 1001–1004 — original vs. duplicate; screenshot is a "duplicate" |
| Stored Communications Act | 18 U.S.C. §§ 2701–2712 — legal process requirements for platform data |
| Warrant requirement (digital content) | *Riley v. California*, 573 U.S. 373 (2014); *Carpenter v. United States*, 585 U.S. 296 (2018) |
| Suppression of illegally obtained evidence | La. C.Cr.P. Art. 703; 4th Amendment |
| Expert testimony reliability | La. C.E. Art. 702; *Daubert v. Merrell Dow* |
| Prior inconsistent statements | La. C.E. Art. 613 — foundation for impeachment |
| Brady obligations (withheld exculpatory data) | *Brady v. Maryland*; *Giglio v. United States* |
| Spoliation / preservation duty | Federal common law; *Zubulake v. UBS Warburg* (civil, but principles apply) |
| Computer Fraud and Abuse Act | 18 U.S.C. § 1030 — relevant when account access is disputed |

*Adapt all rules when jurisdiction toggle is set to federal or another state.*

## Platform Data Retention & Legal Process

| Platform | Content Retention | Metadata Retention | Legal Process for Content | Legal Process for Metadata | Cooperation Level |
|----------|------------------|--------------------|--------------------------|---------------------------|-------------------|
| **Facebook/Meta** | Indefinite (unless user deletes) | Extensive (IPs, sessions, device IDs) | Search warrant (§ 2703(a)) | Court order (§ 2703(d)) or subpoena | Generally responsive |
| **Instagram** | Indefinite (posts); 24hr (Stories) | Similar to Facebook | Same as Facebook | Same as Facebook | Generally responsive |
| **Snapchat** | Deleted after viewing / 30 days unopened | Limited logs retained | Search warrant | Court order / subpoena | Responsive but limited data |
| **TikTok** | Indefinite (unless user deletes) | Login logs, device IDs | Search warrant | Court order / subpoena | Variable; data residency concerns |
| **Twitter/X** | Indefinite (unless user deletes) | Login IPs, session data | Search warrant | Court order / subpoena | Variable post-2023 |
| **WhatsApp** | E2EE — not available to Meta | Sender/receiver, timestamps, group info | N/A (E2EE) — device extraction only | Court order / subpoena | Metadata only |
| **Telegram** | Cloud chats: retained; Secret chats: E2EE | Limited | Varies by jurisdiction | Varies | Historically resistant |
| **Signal** | Minimal — registration date, last connection only | Almost none | N/A — no content to produce | Subpoena (minimal data) | Cooperative but has nothing |

*Retention policies change frequently. Verify current policies when auditing evidence older than 6 months.*
