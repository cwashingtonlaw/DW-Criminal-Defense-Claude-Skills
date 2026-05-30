# MODULE A — Facebook / Meta (including Messenger)

The core question for every platform audit: **what does this platform retain, what does it strip, and what can be fabricated?**

| Architecture Feature | Defense Implications |
|---------------------|---------------------|
| **Account Creation** | Facebook accounts can be created with any name and a burner email/phone. The existence of an account in a name does not prove the defendant created or controls it. Demand: account registration IP, registration email/phone, and device fingerprint from Meta's records. |
| **Content Mutability** | Posts can be edited after publication. Facebook retains edit history, but this is only available through platform-produced records — screenshots capture only the current state. If the prosecution relies on a screenshot of a post, demand the edit history from Meta. |
| **Messenger Encryption** | Standard Messenger is not end-to-end encrypted by default (E2EE was rolled out as default in late 2023). Meta can produce standard Messenger content via legal process. However, "Vanish Mode" and "Secret Conversations" (E2EE) are not available to Meta — only device-side forensic extraction can recover these. Verify which mode was used. |
| **IP & Session Logs** | Meta retains login IP addresses and session data. These can corroborate or undermine account attribution. If not provided, demand them. Note: IP address alone does not identify a person — it identifies a network connection (shared Wi-Fi, VPN, cellular NAT). |
| **Photo/Video Metadata** | Facebook strips EXIF data from uploaded photos. Original upload metadata (timestamp, upload IP) is retained server-side but not visible in screenshots. Demand server-side upload metadata through legal process. |
| **Records Production Format** | Meta produces records in response to legal process as downloadable data packages (JSON/HTML format). Verify the production is complete — compare the date ranges requested vs. date ranges produced. Meta may produce partial records without flagging gaps. |
