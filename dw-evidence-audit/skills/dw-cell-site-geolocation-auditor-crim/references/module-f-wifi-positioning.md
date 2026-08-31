# Module F — Wi-Fi Positioning Audit

Wi-Fi positioning determines a device's location based on the Wi-Fi networks the device can detect or has connected to.

## Technical Limitations

- **Accuracy:** Typically 15-40 meters, but depends entirely on the accuracy of the Wi-Fi access point location database (maintained by Google, Apple, and others). If the database has an incorrect location for an access point, the position estimate will be wrong.
- **Access point movement:** If a Wi-Fi router is moved (e.g., a user moves to a new home but the database still shows the old address), the positioning system may place the device at the router's old location.
- **Range:** Wi-Fi signals propagate approximately 50-100 meters indoors, further outdoors. A device detecting a Wi-Fi network is not necessarily close to it.
- **Crowdsourced databases:** The location databases used by Google and Apple are built from crowdsourced data — they contain errors, outdated entries, and imprecise coordinates.

## Wi-Fi Evidence Audit Checklist
- [ ] Was the location derived from a Wi-Fi connection or merely from Wi-Fi scanning (detecting nearby networks)?
- [ ] Was the access point location verified in the field, or was a database lookup used?
- [ ] Was the access point location current at the time of the alleged offense, or could it have changed?
- [ ] What was the reported accuracy estimate for the Wi-Fi-derived location?

---

## Module F Summary (moved from SKILL.md)

Wi-Fi positioning determines a device's location based on Wi-Fi networks the device can detect or has connected to. Typical accuracy is 15-40 meters but depends entirely on the accuracy of crowdsourced access-point location databases (Google, Apple). Access-point movement, range overestimation (a device detecting a network is not necessarily close to it), and database errors all undermine reliability.
