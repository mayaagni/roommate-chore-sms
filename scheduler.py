"""
Chore Scheduler
Determines who is responsible for each chore in a given week,
then builds one consolidated message per person.
"""

from datetime import date, timedelta
from config import (
    SCHEDULE_START,
    VACUUM_ROTATION,
    WIPEDOWN_ROTATION,
    MOPPING_ROTATION,
    MOPPING_START_WEEK,
    STEEL_ROTATION,
    STEEL_START_WEEK,
    BATHROOM_ROTATION,
    BATHROOM_START_WEEK,
    LAUNDRY_ROTATION,
    LAUNDRY_START_WEEK,
    FRIDGE_START_WEEK,
    ROOMMATES,
)
from messages import build_person_message


ALL_NAMES = list(ROOMMATES.keys())


def get_week_number(target_date: date) -> int:
    """Get the week number (0-indexed) from the schedule start date."""
    days_since_start = (target_date - SCHEDULE_START).days
    return days_since_start // 7


def get_chores_for_week(target_date: date) -> list[dict]:
    """
    Returns a list of per-person messages for the week.
    Each item: {"name": str, "message": str, "chores": list[str]}
    """
    week_num = get_week_number(target_date)

    # Collect individual chore assignments: {name: [{"chore": str, "vacuum_person": str}]}
    personal = {name: [] for name in ALL_NAMES}
    group_chores = []

    # ── Weekly: Vacuuming ──
    vacuum_person = VACUUM_ROTATION[week_num % len(VACUUM_ROTATION)]
    personal[vacuum_person].append({"chore": "Vacuuming"})

    # ── Weekly: Wipe-down ──
    wipe_person = WIPEDOWN_ROTATION[week_num % len(WIPEDOWN_ROTATION)]
    personal[wipe_person].append({"chore": "Wipe-down"})

    # ── Biweekly: Mopping ──
    weeks_since_mop_start = week_num - MOPPING_START_WEEK
    if weeks_since_mop_start >= 0 and weeks_since_mop_start % 2 == 0:
        mop_index = weeks_since_mop_start // 2
        mop_person = MOPPING_ROTATION[mop_index % len(MOPPING_ROTATION)]
        personal[mop_person].append({"chore": "Mopping"})

    # ── Monthly (every 4 weeks): Stainless Steel ──
    weeks_since_steel_start = week_num - STEEL_START_WEEK
    if weeks_since_steel_start >= 0 and weeks_since_steel_start % 4 == 0:
        steel_index = weeks_since_steel_start // 4
        steel_person = STEEL_ROTATION[steel_index % len(STEEL_ROTATION)]
        personal[steel_person].append({"chore": "Stainless Steel"})

    # ── Biweekly: Wash Rags & Towels ──
    weeks_since_laundry_start = week_num - LAUNDRY_START_WEEK
    if weeks_since_laundry_start >= 0 and weeks_since_laundry_start % 2 == 0:
        laundry_index = weeks_since_laundry_start // 2
        laundry_person = LAUNDRY_ROTATION[laundry_index % len(LAUNDRY_ROTATION)]
        personal[laundry_person].append({"chore": "Wash Rags & Towels"})

    # ── Biweekly: Bathroom ──
    weeks_since_bath_start = week_num - BATHROOM_START_WEEK
    if weeks_since_bath_start >= 0 and weeks_since_bath_start % 2 == 0:
        bath_index = weeks_since_bath_start // 2
        bath_person = BATHROOM_ROTATION[bath_index % len(BATHROOM_ROTATION)]
        personal[bath_person].append({"chore": "Bathroom"})

    # ── Monthly (every 4 weeks): Fridge Clean Out (group) ──
    weeks_since_fridge_start = week_num - FRIDGE_START_WEEK
    if weeks_since_fridge_start >= 0 and weeks_since_fridge_start % 4 == 0:
        group_chores.append("Fridge Clean Out")

    # Build one message per person (everyone gets a text every week)
    results = []
    for name in ALL_NAMES:

        # Build the "others" dict: what everyone else is doing
        others = {}
        for other in ALL_NAMES:
            if other == name:
                continue
            other_chore_names = [c["chore"] for c in personal[other]]
            others[other] = other_chore_names

        message = build_person_message(
            name=name,
            personal_chores=personal[name],
            group_chores=group_chores,
            others=others,
        )

        chore_names = [c["chore"] for c in personal[name]]
        if group_chores:
            chore_names.extend(group_chores)

        results.append({
            "name": name,
            "chores": chore_names,
            "message": message,
        })

    return results


def preview_schedule(weeks: int = 12):
    """Print a preview of the schedule for the next N weeks."""
    print(f"\U0001f4c5 Chore Schedule (starting {SCHEDULE_START})\n")
    print("=" * 70)

    for w in range(weeks):
        week_date = SCHEDULE_START + timedelta(weeks=w)
        week_end = week_date + timedelta(days=6)
        results = get_chores_for_week(week_date)

        print(f"\n\U0001f4c6 Week {w + 1}: {week_date.strftime('%b %d')} \u2013 {week_end.strftime('%b %d, %Y')}")
        print("-" * 50)
        for r in results:
            chores_str = ", ".join(r["chores"])
            print(f"  {r['name']:.<20} {chores_str}")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    preview_schedule()
