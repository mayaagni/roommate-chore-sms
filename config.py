"""
Chore Chart Configuration
Apartment: Maya, Sophie, Bri, Alizeh

All sensitive data (phone numbers, API keys) lives in .env — not here.
"""

import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()

# ─── Roommates ───────────────────────────────────────────────
# Phone numbers are loaded from .env (see .env.example)
ROOMMATES = {
    "Maya":   {"phone": os.environ.get("MAYA_PHONE", "")},
    "Sophie": {"phone": os.environ.get("SOPHIE_PHONE", "")},
    "Bri":    {"phone": os.environ.get("BRI_PHONE", "")},
    "Alizeh": {"phone": os.environ.get("ALIZEH_PHONE", "")},
}

# ─── Schedule Start Date ─────────────────────────────────────
# Week 1 starts on this Monday. Rotations are calculated from here.
SCHEDULE_START = date(2025, 2, 17)

# ─── Rotation Orders ─────────────────────────────────────────
# Vacuuming: weekly, all 4 roommates
VACUUM_ROTATION = ["Sophie", "Bri", "Alizeh", "Maya"]

# Mopping: monthly (every 4 weeks), all 4 roommates
# Starts Week 3 (first full March week) since Maya mopped ~2 weeks before start
MOPPING_ROTATION = ["Bri", "Alizeh", "Maya", "Sophie"]
MOPPING_START_WEEK = 3  # week offset from SCHEDULE_START

# Stainless Steel: monthly (every 4 weeks), all 4 roommates
STEEL_ROTATION = ["Alizeh", "Maya", "Sophie", "Bri"]
STEEL_START_WEEK = 3

# Bathroom: every 2 weeks, only Maya/Sophie/Bri
BATHROOM_ROTATION = ["Maya", "Sophie", "Bri"]
BATHROOM_START_WEEK = 2  # starts week 2

# Common Hallway: included when Maya or Bri vacuum
HALLWAY_PEOPLE = {"Maya", "Bri"}
