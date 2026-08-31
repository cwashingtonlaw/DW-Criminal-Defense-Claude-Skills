# Module D — GPS / Vehicle Tracking Audit

GPS tracking evidence comes from dedicated tracking devices placed on vehicles, phone GPS data (from apps or carrier-assisted GPS), or court-ordered monitoring devices (ankle monitors).

## GPS Technical Audit

**Accuracy and Limitations:**
- Standard civilian GPS is accurate to approximately 3-5 meters in open sky conditions
- Accuracy degrades significantly indoors, in urban canyons (tall buildings), under heavy tree cover, and in parking garages
- Multipath errors (signal bouncing off buildings) can shift apparent position by tens of meters
- A-GPS (Assisted GPS, used by phones) uses cell tower data to speed up positioning but can produce less accurate fixes when satellite coverage is poor
- GPS altitude data is significantly less accurate than horizontal position — do not rely on floor-level claims in multi-story buildings

**GPS Tracking Device Audit:**
- [ ] Was a warrant obtained before placing the tracking device? (*United States v. Jones*, 565 U.S. 400 (2012) — warrant required for physical GPS trackers)
- [ ] When was the device installed and when was it removed? Does the monitoring period exceed the warrant's authorization?
- [ ] What is the device's recording interval? (Every 30 seconds? Every 5 minutes? Less frequent intervals create gaps in the track)
- [ ] How does the device handle lost satellite signal? (Does it record the last known position, or does it leave a gap?)
- [ ] Was the raw GPS data provided, or only a processed report? (Demand the raw NMEA data or equivalent — processed reports may omit fixes with poor accuracy indicators)
- [ ] Were accuracy indicators (HDOP, number of satellites, fix quality) preserved in the data?

**Phone GPS Data Audit:**
- [ ] What was the source of the phone GPS data — carrier records, Google Location History, Apple Significant Locations, an app's location logs?
- [ ] Was the data truly GPS-derived, or was it Wi-Fi- or cell-tower-assisted positioning presented as "GPS"? (Google Location History, for example, blends GPS, Wi-Fi, and cell data without always distinguishing them)
- [ ] What was the accuracy estimate for each data point? (Google Location History includes an accuracy radius — points with large radii are unreliable)
- [ ] How frequently were location fixes recorded? (Continuous tracking vs. periodic check-ins produce very different data quality)

---

## Module D Summary (moved from SKILL.md)

GPS tracking evidence comes from dedicated vehicle trackers, phone GPS data (apps or carrier-assisted GPS), or court-ordered monitoring (ankle monitors). Audit accuracy and limitations (3-5m open sky; degrades indoors, in urban canyons, under tree cover; multipath errors; A-GPS reliability; altitude unreliability), tracking-device authorization (*United States v. Jones*, 565 U.S. 400 (2012) — warrant required for physical GPS trackers), data integrity (recording interval, signal-loss handling, raw NMEA vs. processed reports, accuracy indicators preserved), and phone GPS data sources (carrier records, Google Location History, Apple Significant Locations — beware blended GPS/Wi-Fi/cell positioning presented as "GPS").
