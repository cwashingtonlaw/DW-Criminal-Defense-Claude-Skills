# Module C — Cell Site Simulator (CSS) Audit

Cell site simulators (marketed as Stingray, Hailstorm, Crossbow, DRTBox, Jugular, etc.) are devices that impersonate a cell tower to force nearby phones to connect, allowing law enforcement to determine a target phone's location with much greater precision than passive CSLI analysis.

## How CSS Devices Work

A CSS broadcasts as a cell tower with a strong signal, causing phones in the vicinity to connect to it. By measuring the signal strength from the target phone, and by physically moving the device (or using directional antennas), the operator can locate the target phone to within a building or room.

**The problem for the defense — and the reason CSS evidence is often concealed:**
- CSS devices capture ALL phones in the area, not just the target — this is dragnet surveillance
- Federal agencies (particularly the FBI and U.S. Marshals) have historically required local law enforcement to sign non-disclosure agreements (NDAs) prohibiting them from revealing CSS use in court
- Law enforcement may use "parallel construction" — using the CSS to locate the suspect, then manufacturing an alternative explanation for how they found the person (e.g., a "confidential informant tip")
- Some agencies have dismissed cases rather than disclose CSS use

## CSS Detection Indicators

Because CSS use is often concealed, look for these indicators in the discovery:

| Indicator | What It Suggests |
|-----------|-----------------|
| Vague description of how suspect was located ("through investigative means") | Possible parallel construction concealing CSS use |
| Pen register / trap-and-trace order instead of a search warrant | CSS often deployed under pen register authority — which is legally inadequate post-*Carpenter* |
| Reference to "technical assistance" from FBI, U.S. Marshals, or a regional task force | These agencies operate CSS programs and loan devices to local agencies |
| Suspect located in a building with no independent basis for knowing they were inside | CSS can locate to building-level; passive CSLI cannot |
| Discovery references to "cell phone tracking" without specifying the method | May be concealing whether tracking was active (CSS) or passive (carrier records) |
| Non-disclosure agreement or NDA referenced in agency records | Direct evidence of CSS use with a concealment agreement |

## CSS Legal Challenges

- **Warrant requirement:** Many courts now require a warrant for CSS use. *United States v. Patrick*, 842 F.3d 540 (7th Cir. 2016) — warrant required. *United States v. Lambis*, 197 F. Supp. 3d 606 (S.D.N.Y. 2016) — pen register order insufficient.
- **Non-disclosure and parallel construction:** If CSS use was concealed through parallel construction, the defendant's rights to full discovery, confrontation, and due process are implicated. *Brady v. Maryland* requires disclosure of the actual investigative method.
- **Dragnet capture:** CSS devices capture all phones in the area — challenge the scope of the intrusion and the absence of minimization procedures.
- **5th Circuit:** Monitor for circuit-specific CSS rulings.
