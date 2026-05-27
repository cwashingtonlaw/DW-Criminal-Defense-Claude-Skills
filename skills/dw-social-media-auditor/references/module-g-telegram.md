# MODULE G — Telegram

| Architecture Feature | Defense Implications |
|---------------------|---------------------|
| **Cloud vs. Secret Chats** | Standard Telegram chats are cloud-based — Telegram can produce content via legal process (though cooperation varies). "Secret Chats" are E2EE and device-to-device only — Telegram cannot produce this content. Verify which chat type is at issue. |
| **Message Editing & Deletion** | Telegram allows editing sent messages (with no "edited" flag visible to recipients in some versions) and deleting messages for both parties. This creates significant fabrication and spoliation concerns. |
| **Cooperation Challenges** | Telegram has historically been resistant to law enforcement requests. If records were produced, verify the legal mechanism and completeness. If records were not obtainable, flag the gap. |
