#!/usr/bin/env python3
"""
Post the weekly visit list to a Google Chat space via incoming webhook.

Webhook setup is documented in references/google_chat_webhook_setup.md.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path


def build_card(visit_list):
    counts = visit_list["counts"]
    today = visit_list["today"]

    sections = []

    def add_section(header, items, line_fn):
        if not items:
            return
        widgets = [{"textParagraph": {"text": line_fn(it)}} for it in items[:25]]
        if len(items) > 25:
            widgets.append({"textParagraph": {"text": f"<i>…and {len(items) - 25} more</i>"}})
        sections.append({
            "header": header,
            "collapsible": True,
            "uncollapsibleWidgetsCount": min(3, len(widgets)),
            "widgets": widgets,
        })

    add_section(
        f"⚠️ Jail visits OVERDUE ({counts['jail_visits_overdue']})",
        visit_list["jail_visits_overdue"],
        lambda it: f"<b>{it['client']}</b> ({it['docket']}) — {it['status']}<br>{it['charges']}",
    )
    add_section(
        f"🏛️ Court within 7 days ({counts['court_within_7_days']})",
        visit_list["court_within_7_days"],
        lambda it: f"<b>{it['when']}</b> — {it['client']} ({it['docket']}) — {it.get('event', '')}",
    )
    add_section(
        f"⚖️ Trial within 30 days ({counts['trial_within_30_days']})",
        visit_list["trial_within_30_days"],
        lambda it: f"<b>{it['when']}</b> — {it['client']} ({it['docket']})",
    )
    add_section(
        f"🆕 New cases this week ({counts['new_cases']})",
        visit_list["new_cases"],
        lambda it: f"<b>{it['client']}</b> ({it['docket']})",
    )

    return {
        "cardsV2": [{
            "cardId": "weekly-visit-list",
            "card": {
                "header": {
                    "title": "Weekly Visit List",
                    "subtitle": today,
                },
                "sections": sections or [{
                    "widgets": [{"textParagraph": {"text": "Nothing on the list this week. Nice."}}]
                }],
            }
        }]
    }


def post(webhook_url, payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.status, resp.read().decode("utf-8", errors="replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--webhook-url", required=True)
    ap.add_argument("--visit-list", required=True, type=Path)
    args = ap.parse_args()

    visit_list = json.loads(args.visit_list.read_text())
    payload = build_card(visit_list)
    try:
        status, body = post(args.webhook_url, payload)
        print(json.dumps({"channel": "google_chat", "status": status, "ok": 200 <= status < 300}))
    except Exception as e:
        print(json.dumps({"channel": "google_chat", "ok": False, "error": str(e)}),
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
