# Quick Reference Tables

## Legal Standards for Location Evidence

| Situation | Authority |
|-----------|-----------|
| Historical CSLI — warrant required | *Carpenter v. United States*, 585 U.S. 296 (2018) |
| GPS tracker — warrant required | *United States v. Jones*, 565 U.S. 400 (2012) |
| Third-party doctrine (pre-Carpenter) | *Smith v. Maryland*, 442 U.S. 735 (1979) — limited by *Carpenter* |
| Cell site simulator — warrant required | *United States v. Patrick*, 842 F.3d 540 (7th Cir. 2016); *United States v. Lambis*, 197 F. Supp. 3d 606 (S.D.N.Y. 2016) |
| Geofence warrant — particularity | *United States v. Chatrie*, 590 F. Supp. 3d 901 (E.D. Va. 2022) |
| Good-faith exception | *Davis v. United States*, 564 U.S. 229 (2011) |
| Stored Communications Act | 18 U.S.C. §§ 2701-2712 |
| Pen Register Act | 18 U.S.C. §§ 3121-3127 |
| Expert testimony reliability | La. C.E. Art. 702; *Daubert v. Merrell Dow*, 509 U.S. 579 (1993) |
| Business records (carrier CDRs) | La. C.E. Art. 803(6); Fed. R. Evid. 803(6) |
| Suppression of illegally obtained evidence | La. C.Cr.P. Art. 703; 4th Amendment |
| Brady obligations (undisclosed location data) | *Brady v. Maryland*, 373 U.S. 83 (1963) |
| Spoliation / destroyed location data | *Arizona v. Youngblood*, 488 U.S. 51 (1988) |
| La. warrant requirements | La. C.Cr.P. Art. 162 |
| La. electronic surveillance | La. R.S. 15:1301 et seq. |

## Carrier-Specific CSLI Notes

| Carrier | CDR Format Notes | Known Defense Concerns |
|---------|-----------------|----------------------|
| AT&T | CDRs typically include LACCI (Location Area Code / Cell ID); may use UTC timestamps | AT&T sector azimuths may not reflect actual mechanical or electrical tilt — demand antenna configuration data |
| T-Mobile | CDRs may include CGI format; data session records may be more granular than voice | T-Mobile's 5G deployment uses a mix of mmWave and sub-6 GHz — coverage characteristics differ dramatically |
| Verizon | CDRs typically include switch-level records; may report sector differently than GSM carriers | Verizon's CDMA legacy network handled tower selection differently from GSM-based carriers — handoff behavior matters |
| Sprint (now T-Mobile) | Legacy Sprint records may use different formats; historical cases may reference Sprint infrastructure | Sprint infrastructure is being integrated into T-Mobile — tower IDs and configurations may have changed between the offense date and the analyst's review |
