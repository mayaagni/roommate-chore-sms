"""
SMS Sender using Twilio.
Sends chore reminder texts to roommates.

Setup:
  1. pip install twilio
  2. Set environment variables:
     - TWILIO_ACCOUNT_SID
     - TWILIO_AUTH_TOKEN
     - TWILIO_PHONE_NUMBER  (your Twilio phone number, e.g. "+15551234567")
  3. Update phone numbers in config.py
"""

import os
from config import ROOMMATES

# ─── Twilio Setup ─────────────────────────────────────────────
TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.environ.get("TWILIO_PHONE_NUMBER")


def send_sms(to_number: str, message: str, dry_run: bool = False) -> bool:
    """Send an SMS via Twilio. Returns True on success."""
    if dry_run:
        print(f"  [DRY RUN] Would send to {to_number}:")
        print(f"  {message[:100]}...")
        return True

    try:
        from twilio.rest import Client
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        msg = client.messages.create(
            body=message,
            from_=TWILIO_FROM,
            to=to_number,
        )
        print(f"  \u2705 Sent to {to_number} (SID: {msg.sid})")
        return True
    except Exception as e:
        print(f"  \u274c Failed to send to {to_number}: {e}")
        return False


def send_chore_reminders(assignments: list[dict], dry_run: bool = True):
    """
    Send SMS reminders for all chore assignments.

    Args:
        assignments: list of dicts from scheduler.get_chores_for_week()
        dry_run: if True, just prints messages without sending
    """
    print(f"\n\U0001f4f1 Sending chore reminders ({'DRY RUN' if dry_run else 'LIVE'})...\n")

    for a in assignments:
        name = a["name"]
        phone = ROOMMATES[name]["phone"]
        message = a["message"]

        print(f"\u2192 {name} \u2014 {a['chore']}")
        send_sms(phone, message, dry_run=dry_run)
        print()
