# Module G — IP Geolocation Audit

IP geolocation attempts to determine a device's physical location from its IP address.

## Why IP Geolocation Is Almost Always Unreliable

- **Accuracy:** IP geolocation databases (MaxMind, IP2Location, etc.) are accurate to the **city level at best**, and often not even that. They determine location based on IP address block registration data, which may reflect the ISP's headquarters or a regional hub — not the user's location.
- **Dynamic IP assignment:** Most residential ISPs assign IP addresses dynamically. The same IP may be assigned to different users at different times.
- **VPNs and proxies:** VPN usage assigns the VPN server's IP address to the user's traffic — the geolocation will show the server's location, not the user's.
- **Mobile networks:** Cellular IP addresses are assigned from carrier pools that may geolocate to a city-level aggregation point, not the user's physical location.
- **Shared IPs (CGNAT):** Many carriers use Carrier-Grade NAT, where hundreds or thousands of users share a single public IP address.

## IP Geolocation Audit Checklist
- [ ] What geolocation database or service was used?
- [ ] What is the stated accuracy of that database for the IP address in question?
- [ ] Was the IP address static or dynamically assigned?
- [ ] Was the IP address verified as assigned to the defendant's account at the specific time (not just the same day or week)?
- [ ] Were VPN, proxy, or CGNAT possibilities investigated?
- [ ] Was the geolocation result independently verified against any other evidence?

---

## Module G Summary (moved from SKILL.md)

IP geolocation attempts to determine a device's physical location from its IP address. It is almost always unreliable — accurate to the city level at best, often worse. Dynamic IP assignment, VPNs/proxies, mobile network carrier pools, and CGNAT (hundreds or thousands of users sharing one public IP) all compound the unreliability.
