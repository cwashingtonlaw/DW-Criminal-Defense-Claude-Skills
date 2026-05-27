# Module A — Historical CSLI Audit

Historical CSLI is the most common form of cell site evidence in criminal cases and the most frequently overstated. A CSLI record shows which cell tower and sector a phone connected to — it does not show where the phone was located within that sector's coverage area.

## Understanding CSLI Records

**What the records contain:**
- **Call Detail Records (CDRs):** date/time of each call, text, or data session; the cell tower (identified by a Cell Global Identity / CGI, or LAC/CID) and sector the phone connected to at the start (and sometimes end) of the communication; call duration; called/calling number
- **Cell site information:** the physical location (latitude/longitude) of each tower referenced in the CDRs, and the azimuth (compass direction) of each sector antenna

**What the records do NOT contain:**
- The phone's actual geographic coordinates
- The distance between the phone and the tower
- Whether the phone was stationary or moving
- Why the phone connected to a particular tower (proximity is one factor, but not the only one)

## The Precision Problem

This is the single most important issue in CSLI evidence. The defense must understand and communicate that **a CSLI record places the phone within the coverage area of a sector — not at a specific point.**

**Sector coverage areas vary enormously:**
- Urban areas with dense tower deployment: sectors may cover a few hundred meters to a mile
- Suburban areas: sectors may cover 1-3 miles
- Rural areas: sectors may cover 5-20+ miles
- Terrain, building density, foliage, weather, and network load all affect coverage

**The state's analyst will often present a map with the tower location and the sector's azimuth, drawing a narrow wedge on the map. This is misleading because:**
- The wedge represents the antenna's boresight direction, not the actual coverage area
- Sector antennas have a beamwidth (typically 65° to 120°), and signal propagates beyond the nominal beamwidth through sidelobes
- A phone can connect to a sector antenna from behind or beside the antenna (backlobe reception), especially at close range
- RF propagation is not a clean wedge — it is affected by terrain, buildings, foliage, atmospheric conditions, and interference
- The map does not show the outer boundary of the sector's coverage, which is where the phone might actually be

**What to demand:**
- RF propagation analysis (drive testing or propagation modeling) for the specific towers at issue — not just a wedge drawn on a map
- Documentation of the analyst's methodology for determining coverage boundaries
- Acknowledgment that the phone could have been anywhere within the sector's coverage area, not just within the drawn wedge

## CSLI Audit Checklist

**Data Integrity:**
- [ ] Are the CDRs complete — do they cover the full requested time period?
- [ ] Are timestamps in a consistent and identified time zone? (Carriers may use UTC, billing address time zone, or local time — and this is not always documented)
- [ ] Do the CDRs include both call and data session records? (Data sessions are more frequent and provide more granular connection data)
- [ ] Are cell site coordinates provided by the carrier, or did the analyst geocode them independently? (Analyst-geocoded tower locations may contain errors)
- [ ] For each referenced tower, is the sector number, azimuth, and technology type (2G/3G/4G/5G) documented?

**Analysis Methodology:**
- [ ] Did the analyst rely solely on azimuth wedge mapping, or did they perform actual coverage analysis (drive testing, propagation modeling)?
- [ ] Did the analyst account for the possibility that the phone could connect to a non-nearest tower?
- [ ] Did the analyst acknowledge that sector coverage areas overlap and that tower selection depends on load balancing, signal strength, and other factors — not just proximity?
- [ ] Did the analyst consider and address alternative tower connections that would be consistent with the phone being at a different location than the crime scene?
- [ ] Was "first and last" tower analysis used? (If so, this is notoriously unreliable — the tower at the start of a call and the tower at the end of a call do not necessarily indicate the direction of travel)

**Granularity and Limitations:**
- [ ] What network technology was in use — 2G (GSM/CDMA), 3G (UMTS/EVDO), 4G LTE, or 5G? (Each has different tower density, sector configuration, and connection behavior)
- [ ] Were small cells or distributed antenna systems (DAS) present in the area? (These complicate the relationship between tower ID and geographic location — DAS nodes may share a single tower ID but span a large building or campus)
- [ ] For 5G networks: was mmWave (very short range, high precision) or sub-6 GHz (similar to 4G coverage) in use?
- [ ] Did the analyst assess whether the phone was in an area with overlapping coverage from multiple towers, which would make tower selection less deterministic?

## Common Prosecution Overstatements to Challenge

| What the Analyst Says | What the Data Actually Shows | Challenge |
|-----------------------|------------------------------|-----------|
| "The phone was at the crime scene" | The phone connected to a tower whose coverage area includes the crime scene — and also includes the defendant's home, workplace, or other locations | Demand acknowledgment of full coverage area |
| "The phone traveled from location A to location B" | The phone's tower connections changed in a sequence that is *consistent with* but does not *prove* that route — other routes connecting to the same towers are possible | Demand mapping of all possible paths connecting those towers |
| "The phone was not at the defendant's claimed location" | If the defendant's claimed location is within the same sector's coverage area, the data does not exclude it | Demand the analyst map the defendant's claimed location relative to coverage |
| "The phone's location is accurate to within X meters" | CSLI records contain no distance measurement — this claim has no basis in the data itself | Demand the scientific basis for the precision claim |
| "This tower is the closest tower to the crime scene" | Closest tower is irrelevant — phones do not always connect to the closest tower. Load balancing, signal strength, terrain, and network optimization all affect tower selection | Demand documentation of when and why phones connect to non-nearest towers |
