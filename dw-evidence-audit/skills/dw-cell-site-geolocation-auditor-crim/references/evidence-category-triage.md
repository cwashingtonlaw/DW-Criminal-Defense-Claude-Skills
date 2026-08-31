# Geolocation Evidence Category Triage

Read at STEP 2 of `dw-cell-site-geolocation-auditor-crim/SKILL.md` — the Evidence Category Matrix and Conspicuous Absence flag template moved verbatim from SKILL.md.

### Evidence Category Matrix

| Category | What It Is | Typical Source | Precision Claimed vs. Actual | Audit Module |
|----------|-----------|---------------|------------------------------|--------------|
| **Historical CSLI** | Records of which cell towers a phone connected to during calls/texts/data sessions | Carrier records (CDRs) | Often claimed as "placing phone at location" — actual precision is the tower's entire coverage area (potentially miles) | Module A |
| **Tower Dump** | All devices that connected to a specific tower during a time window | Carrier records via warrant/order | Used to place a suspect's phone near a crime scene — but captures thousands of innocent users too | Module B |
| **Cell Site Simulator (CSS)** | Device that mimics a cell tower to force phones to connect, revealing location | Law enforcement (Stingray, Hailstorm, Crossbow, DRTBox) | Can locate to within a building, but at the cost of capturing all phones in the area | Module C |
| **GPS / Vehicle Tracking** | Satellite-based positioning from a tracking device or the phone itself | GPS tracker on vehicle, phone GPS data, ankle monitor | Precise (3-15 meters outdoors) but degrades indoors, in urban canyons, and when satellites are obstructed | Module D |
| **Geofence Warrant** | Reverse-location query: "show me all devices in this area at this time" | Google (Sensorvault), Apple, other providers | Varies by data source — Google Location History can be Wi-Fi-assisted (precise) or cell-only (imprecise) | Module E |
| **Wi-Fi Positioning** | Location derived from connection to or proximity to Wi-Fi access points | Device logs, app data, carrier Wi-Fi offload records | Typically within 15-40 meters of the access point, but access point location databases contain errors | Module F |
| **IP Geolocation** | Location inferred from an IP address | ISP records, web service logs, app logs | Wildly imprecise — often accurate only to the city or region level; many databases contain stale or wrong data | Module G |

### Conspicuous Absence Flags

When the charge type strongly implies location evidence should exist but does not appear in discovery:

> **CONSPICUOUS ABSENCE — [Category]:** In a [charge type] case where the state alleges the defendant was at [location] at [time], [location evidence type] would be standard investigative evidence. No [evidence type] appears in the discovery provided. This absence should be explored: was it obtained and not disclosed (*Brady* concern)? Was it not obtained (investigative deficiency — potentially favorable, as it may suggest the data did not support the state's theory)? Was it obtained and the results were unfavorable to the prosecution (*Brady/Youngblood*)? Flag for: Missing Discovery Demand + cross-examination of lead investigator.
