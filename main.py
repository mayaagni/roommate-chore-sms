#!/usr/bin/env python3
"""
Chore Chart — Main Entry Point

Usage:
  python main.py preview          # Show the next 12 weeks of chores
  python main.py send --dry-run   # Preview what texts would be sent this week
  python main.py send             # Actually send the texts for this week

Automation (cron / GitHub Actions / etc.):
  Run `python main.py send` every Monday morning to text everyone their chores.
"""

import sys
from datetime import date
from scheduler import get_chores_for_week, preview_schedule
from sms import send_chore_reminders


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [preview|send] [--dry-run]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "preview":
        preview_schedule(weeks=12)

    elif command == "send":
        dry_run = "--dry-run" in sys.argv
        today = date.today()
        chores = get_chores_for_week(today)

        print(f"\U0001f4c5 Chores for week of {today.strftime('%B %d, %Y')}:\n")
        for c in chores:
            print(f"  \u2022 {c['chore']}: {c['name']}")
        print()

        send_chore_reminders(chores, dry_run=dry_run)

        if dry_run:
            print("\u2139\ufe0f  This was a dry run. Remove --dry-run to send real texts.")

    else:
        print(f"Unknown command: {command}")
        print("Usage: python main.py [preview|send] [--dry-run]")
        sys.exit(1)


if __name__ == "__main__":
    main()
