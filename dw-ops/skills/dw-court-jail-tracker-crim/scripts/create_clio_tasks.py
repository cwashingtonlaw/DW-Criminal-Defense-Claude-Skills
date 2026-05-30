#!/usr/bin/env python3
"""
Create one Clio Manage task per overdue jail visit.

Clio API docs: https://docs.developers.clio.com
Auth: Bearer access token (see references/clio_api_setup.md).
De-dupes against tasks created in the last 14 days so the same client doesn't
get double-tasked across runs.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import date, timedelta
from pathlib import Path

CLIO_API = "https://app.clio.com/api/v4"


def http(method, url, token, body=None):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
        return resp.status, json.loads(raw) if raw else {}


def find_matter_id(token, docket, client_name):
    """Look up the Clio matter id by docket # or client name. Returns None if not found."""
    # Try docket first (Clio's matter "display_number" often holds the docket)
    for query in (docket, client_name):
        if not query:
            continue
        params = urllib.parse.urlencode({"query": query, "fields": "id,display_number,client{name}"})
        try:
            status, data = http("GET", f"{CLIO_API}/matters?{params}", token)
            for m in data.get("data", []):
                # Prefer exact display_number match
                if m.get("display_number", "").strip() == docket.strip():
                    return m["id"]
            # Fall back to first hit
            if data.get("data"):
                return data["data"][0]["id"]
        except Exception:
            continue
    return None


def list_recent_tasks(token, since_date):
    """Return a set of task names created since `since_date` (ISO)."""
    params = urllib.parse.urlencode({
        "created_since": since_date.isoformat(),
        "fields": "id,name,created_at",
        "limit": 200,
    })
    try:
        status, data = http("GET", f"{CLIO_API}/tasks?{params}", token)
        return {t.get("name", "") for t in data.get("data", [])}
    except Exception:
        return set()


def create_task(token, name, description, due_date, assignee_user_id, matter_id=None):
    body = {
        "data": {
            "name": name,
            "description": description,
            "due_at": due_date.isoformat(),
            "assignee": {"id": int(assignee_user_id), "type": "User"},
            "priority": "high",
        }
    }
    if matter_id:
        body["data"]["matter"] = {"id": matter_id}
    status, data = http("POST", f"{CLIO_API}/tasks", token, body)
    return data.get("data", {}).get("id"), status


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--visit-list", required=True, type=Path)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    config = json.loads(args.config.read_text())
    token = config.get("clio_access_token", "")
    user_id = config.get("clio_user_id", "")

    if not token or token == "FILL_ME_IN":
        print(json.dumps({"channel": "clio", "ok": False, "skipped": "no token"}))
        return
    if not user_id or user_id == "FILL_ME_IN":
        print(json.dumps({"channel": "clio", "ok": False, "skipped": "no user_id"}))
        return

    visit_list = json.loads(args.visit_list.read_text())
    overdue = visit_list.get("jail_visits_overdue", [])
    if not overdue:
        print(json.dumps({"channel": "clio", "ok": True, "tasks_created": 0}))
        return

    due = date.today() + timedelta(days=7)
    recent_names = list_recent_tasks(token, date.today() - timedelta(days=14)) if not args.dry_run else set()

    created, skipped, errors = [], [], []
    for item in overdue:
        name = f"JAIL VISIT — {item['client']} ({item['docket']})"
        if name in recent_names:
            skipped.append({"name": name, "reason": "already created in last 14 days"})
            continue
        description = (
            f"{item.get('charges', '')}\n"
            f"Status: {item.get('status', '')}\n"
            f"Auto-created by dw-court-jail-tracker on {date.today().isoformat()}."
        )
        if args.dry_run:
            created.append({"name": name, "due": due.isoformat(), "dry_run": True})
            continue
        try:
            matter_id = find_matter_id(token, item["docket"], item["client"])
            task_id, status = create_task(token, name, description, due, user_id, matter_id)
            created.append({"name": name, "task_id": task_id, "matter_id": matter_id})
        except Exception as e:
            errors.append({"name": name, "error": str(e)})

    print(json.dumps({
        "channel": "clio",
        "ok": not errors,
        "tasks_created": len(created),
        "skipped": skipped,
        "errors": errors,
        "created": created,
    }, indent=2))


if __name__ == "__main__":
    main()
