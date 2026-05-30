# Google Chat incoming webhook — one-time setup

The skill posts the weekly visit list to a Google Chat space via an incoming webhook. Webhooks are the simplest auth model Chat supports — a long URL with a secret token in the query string. Anyone with the URL can post to that space, so treat it like a password.

## Creating the webhook (2 minutes)

1. Open the Google Chat space you want the digest to land in. This can be:
   - A 1:1 space with yourself (`Cases — Chris`) — recommended for a private list.
   - A space shared with paralegals if you want them to see the list too.
2. Click the space name at the top → **Apps & integrations** → **Webhooks**.
3. Click **Add webhook**.
4. Name it `Court & Jail Tracker`, optionally upload an icon.
5. Click **Save**. Google generates a URL like:

   ```
   https://chat.googleapis.com/v1/spaces/AAAA.../messages?key=...&token=...
   ```

6. Copy that URL.
7. Open `~/.dw-tracker/config.json` and paste it as the value of `google_chat_webhook_url`.

## Testing it

```bash
curl -X POST "$WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{"text": "Court & Jail Tracker test message"}'
```

If you see the message in the space, you're done.

## What the skill posts

The `post_google_chat.py` script sends a `cardsV2` payload — a structured Chat card with collapsible sections per bucket (overdue visits, court ≤7 days, trials ≤30 days, new cases). It looks similar to the email but more compact.

## If the webhook stops working

- **404**: webhook was deleted or the space was archived. Generate a new one.
- **403**: token in URL was rotated. Generate a new one.
- **400 with "Invalid request"**: the card payload schema may have changed. Check Google's [Cards v2 reference](https://developers.google.com/workspace/chat/api/reference/rest/v1/cards) and update `build_card()` in `post_google_chat.py`.
