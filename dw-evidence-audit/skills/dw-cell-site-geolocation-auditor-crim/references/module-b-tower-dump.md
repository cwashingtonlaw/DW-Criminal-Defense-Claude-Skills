# Module B — Tower Dump Audit

A tower dump is a request for all devices that connected to a specific cell tower during a specific time window. It produces a massive list of innocent people's phone identifiers alongside the suspect's.

## Tower Dump Methodology Audit

- **Scope of the dump:** How many towers were queried? What time window? How many unique devices were captured?
- **Narrowing methodology:** How did the analyst narrow the dump results to identify the suspect? What filtering criteria were applied, and in what order?
- **False positive risk:** How many innocent people's location data was captured and reviewed to identify one suspect? Were the privacy implications addressed in the warrant application?
- **Over-inclusion:** Was the time window broader than necessary? Were more towers included than the crime scene would require?
- **Legal authorization:** Was a warrant obtained for the tower dump, or a lesser court order? Post-*Carpenter*, the warrant requirement for tower dumps is still being litigated in many circuits — but the privacy interests are arguably even greater than historical CSLI because tower dumps are dragnet surveillance.

## Tower Dump Legal Landscape

Tower dumps exist in a legal gray area post-*Carpenter*. The Supreme Court held that obtaining 7 days of historical CSLI requires a warrant, but did not explicitly address tower dumps. Key cases to know:

- *In re Search of Information Associated with Cellular Towers*, various district courts have applied *Carpenter* to require warrants for tower dumps
- The 5th Circuit has not definitively resolved whether *Carpenter* extends to tower dumps — monitor for recent developments
- Even if the government obtained a warrant, challenge the particularity: did the warrant authorize a dump of all towers in a wide radius, capturing the location data of thousands of innocent people?

---

## Module B Summary (moved from SKILL.md)

A tower dump is a request for all devices that connected to a specific cell tower during a specific time window. It produces a massive list of innocent people's phone identifiers alongside the suspect's. Audit the scope of the dump, the narrowing methodology, the false-positive risk, the over-inclusion of towers and time windows, and the legal authorization (warrant vs. lesser order).

**Legal landscape:** Tower dumps exist in a legal gray area post-*Carpenter*. The Supreme Court did not explicitly address tower dumps; various district courts have applied *Carpenter* to require warrants for tower dumps. The 5th Circuit has not definitively resolved this — monitor for recent developments. Even if a warrant was obtained, challenge particularity for dragnet captures.
