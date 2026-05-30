# Clio Manage API setup — minting an access token

The skill writes tasks to Clio Manage via its public REST API (`https://app.clio.com/api/v4`). You need:

1. An access token (Bearer)
2. Your numeric Clio user id (so tasks get assigned to you, not unassigned)

Both go into `~/.dw-tracker/config.json` as `clio_access_token` and `clio_user_id`.

## Option A: Personal access token (fastest, recommended)

Clio Manage doesn't offer "personal access tokens" in the way GitHub does. The path of least resistance is to register a developer app and use the `client_credentials` or one-shot OAuth flow to get a long-lived token.

1. Go to <https://app.clio.com/settings/developer_applications> (Clio Settings → Developer Applications).
2. Click **New Application**:
   - Name: `dw-court-jail-tracker`
   - Redirect URI: `http://localhost:8080/callback` (placeholder; we'll handle the redirect manually)
   - Scopes: select **Tasks (Read & Write)** and **Matters (Read)**.
3. Copy the **Client ID** and **Client Secret** that Clio shows you.
4. In a browser, visit:

   ```
   https://app.clio.com/oauth/authorize?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost:8080/callback
   ```

5. Approve. Clio will redirect to `http://localhost:8080/callback?code=AUTH_CODE`. Copy the `code` param from your browser's URL bar (the redirect will fail because there's nothing listening — that's fine).
6. Exchange the code for tokens:

   ```bash
   curl -X POST https://app.clio.com/oauth/token \
     -d "grant_type=authorization_code" \
     -d "client_id=YOUR_CLIENT_ID" \
     -d "client_secret=YOUR_CLIENT_SECRET" \
     -d "code=AUTH_CODE" \
     -d "redirect_uri=http://localhost:8080/callback"
   ```

7. The response gives you `access_token` (short-lived, ~7 days) and `refresh_token` (long-lived).
8. Put `access_token` into `clio_access_token` in the config.

When the access token expires, refresh it:

```bash
curl -X POST https://app.clio.com/oauth/token \
  -d "grant_type=refresh_token" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "refresh_token=YOUR_REFRESH_TOKEN"
```

## Option B: Skip Clio for now

If you don't want to set up Clio yet, leave `clio_access_token` as `"FILL_ME_IN"`. The skill detects the placeholder and skips the Clio channel. Email, iMessage, and Google Chat will still fire.

## Finding your Clio user id

Once you have a token:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "https://app.clio.com/api/v4/users/who_am_i.json?fields=id,name,email"
```

The `id` field in the response is your `clio_user_id`.

## Future improvement: auto-refresh

Right now Chris will need to re-mint the access token every ~7 days, which is annoying. A future iteration of this skill should:

1. Store both `access_token` and `refresh_token` in the config.
2. In `create_clio_tasks.py`, on a 401, automatically refresh and retry once.

That's a TODO — not urgent for v1, but tag it.
