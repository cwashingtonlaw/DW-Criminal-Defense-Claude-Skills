# Screenshot & Digital Artifact Integrity Audit

Screenshots are the most common — and most unreliable — form of social media evidence. Apply this analysis to every screenshot or printout in the evidence.

## Fabrication Methods (What Defense Should Raise)

The prosecution must establish that screenshots are what they claim to be. The defense should be prepared to demonstrate how easily they can be fabricated:

1. **Browser Developer Tools (Inspect Element):** Any text, image, or timestamp displayed in a web browser can be altered in seconds using built-in developer tools. No technical expertise required. The altered page looks identical to the original — no visual artifacts, no pixelation, no signs of editing. This is not theoretical — it is a standard web development tool available in every modern browser.

2. **Fake Conversation Generators:** Websites and apps exist specifically to generate realistic-looking fake social media conversations for every major platform. These produce images indistinguishable from genuine screenshots without forensic analysis.

3. **Image Editing:** Standard tools (Photoshop, GIMP, even phone photo editors) can alter screenshots — changing text, timestamps, profile pictures, or message content.

4. **Screen Recording Editing:** Video editing tools can alter screen recordings, though this is more difficult to do seamlessly than static image manipulation.

## Metadata Verification Checklist

For every screenshot or digital image presented as evidence:
- [ ] **EXIF data present?** Screenshots typically contain device metadata (device model, OS version, screenshot timestamp) but NOT the original content's metadata. Social media platforms strip EXIF data from uploaded content.
- [ ] **Screenshot timestamp vs. content timestamp:** Does the screenshot's creation date (from EXIF or file system) align with the alleged date of the social media content? A screenshot taken months after the alleged post date raises questions about what may have changed.
- [ ] **Resolution and format consistency:** Is the image resolution consistent with the claimed capture device? Are there compression artifacts suggesting the image was re-saved or transmitted through a messaging app?
- [ ] **URL bar visible?** For browser screenshots — is the URL visible and does it show the correct platform domain? (Note: URLs can also be altered via developer tools.)
- [ ] **Full context captured?** Does the screenshot show the complete post/conversation, or is it cropped? Cropping removes context that may change the meaning entirely.
- [ ] **Profile verification visible?** Does the screenshot show enough of the profile page to link the account to the defendant (bio, mutual friends, phone number, linked accounts)?
- [ ] **Hash verification:** Was the screenshot hashed (MD5/SHA-256) at the time of capture? If not, there is no way to verify it hasn't been altered since.

## Platform Records Integrity Checklist

For platform-produced records (subpoena/warrant responses):
- [ ] **Records custodian certification present?** Required for business records exception under La. C.E. Art. 803(6)
- [ ] **Production date range matches request date range?** Platforms sometimes produce partial records without flagging gaps
- [ ] **Data format is native platform export?** (JSON, HTML data package) vs. reformatted/summarized by law enforcement
- [ ] **Account subscriber information included?** Registration email, phone, IP address at registration, device identifiers
- [ ] **Login/session history included?** IP addresses, device fingerprints, timestamps for each session
- [ ] **Content completeness:** Are there gaps in message threads? Missing attachments? Threads that start mid-conversation (suggesting deleted earlier messages)?
- [ ] **Metadata fields populated:** timestamps, sender/receiver identifiers, read receipts, delivery status
