"""
Chore Scheduler
Determines who is responsible for each chore in a given week.
"""

from datetime import date, timedelta
from config import (
    SCHEDULE_START,
    VACUUM_ROTATION,
    MOPPING_ROTATION,
    MOPPING_START_WEEK,
    STEEL_ROTATION,
    STEEL_START_WEEK,
    BATHROOM_ROTATION,
    BATHROOM_START_WEEK,
    HALLWAY_PEOPLE,
)
from messages import (
    get_vacuum_message,
    get_mopping_message,
    get_steel_message,
    get_bathroom_message,
)


def get_week_number(target_date: date) -> int:
    """Get the week number (0-indexed) from the schedule start date."""
    days_since_start = (target_date - SCHEDULE_START).days
    return days_since_start // 7


def get_chores_for_week(target_date: date) -> list[dict]:
    """
    Returns a list of chore assignments for the week containing target_date.
    Each item: {"name": str, "chore": str, "message": str}
    """
    week_num = get_week_number(target_date)
    assignments = []

    # ── Weekly: Vacuuming ──
    vacuum_person = VACUUM_ROTATION[week_num % len(VACUUM_ROTATION)]
    include_hallway = vacuum_person in HALLWAY_PEOPLE
    assignments.append({
        "name": vacuum_person,
        "chore": "Vacuuming",
        "message": get_vacuum_message(vacuum_person, include_hallway),
    })

    # ── Monthly (every 4 weeks): Mopping ──
    weeks_since_mop_start = week_num - MOPPING_START_WEEK
    if weeks_since_mop_start >= 0 and weeks_since_mop_start % 4 == 0:
        mop_index = weeks_since_mop_start // 4
        mop_person = MOPPING_ROTATION[mop_index % len(MOPPING_ROTATION)]
        assignments.append({
            "name": mop_person,
            "chore": "Mopping",
            "message": get_mopping_message(mop_person),
        })

    # ── Monthly (every 4 weeks): Stainless Steel ──
    weeks_since_steel_start = week_num - STEEL_START_WEEK
    if weeks_since_steel_start >= 0 and weeks_since_steel_start % 4 == 0:
        steel_index = weeks_since_steel_start // 4
        steel_person = STEEL_ROTATION[steel_index % len(STEEL_ROTATION)]
        assignments.append({
            "name": steel_person,
            "chore": "Stainless Steel Clean",
            "message": get_steel_message(steel_person),
        })

    # ── Biweekly: Bathroom ──
    weeks_since_bath_start = week_num - BATHROOM_START_WEEK
    if weeks_since_bath_start >= 0 and weeks_since_bath_start % 2 == 0:
        bath_index = weeks_since_bath_start // 2
        bath_person = BATHROOM_ROTATION[bath_index % len(BATHROOM_ROTATION)]
        assignments.append({
            "name": bath_person,
            "chore": "Bathroom Deep Clean",
            "message": get_bathroom_message(bath_person),
        })

    return assignments


def preview_schedule(weeks: int = 12):
    """Print a preview of the schedule for the next N weeks."""
    print(f"\U0001f4c5 Chore Schedule (starting {SCHEDULE_START})\n")
    print("=" * 70)

    for w in range(weeks):
        week_date = SCHEDULE_START + timedelta(weeks=w)
        week_end = week_date + timedelta(days=6)
        chores = get_chores_for_week(week_date)

        print(f"\n\U0001f4c6 Week {w + 1}: {week_date.strftime('%b %d')} \u2013 {week_end.strftime('%b %d, %Y')}")
        print("-" * 50)
        for c in chores:
            print(f"  {c['chore']:.<30} {c['name']}")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    preview_schedule()
