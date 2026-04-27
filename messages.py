"""
Message builder for chore reminders.
Each person gets ONE consolidated text with their chores, group chores,
and what everyone else is doing.
"""

CHORE_DESCRIPTIONS = {
    "Vacuuming": "please vacuum kitchen floor, entryway, dining area, living room. Maya/Bri also do the shared hallway.",
    "Wipe-down": "please wipe kitchen counters, dining table, console table, and any floor spills.",
    "Mopping": "please mop kitchen, entryway, dining room. coordinate after that week's vacuum.",
    "Stainless Steel": "please wipe the steel on fridge, oven, dishwasher, burner area, and inside the microwave.",
    "Wash Rags & Towels": "please gather communal rags/towels and throw them in the wash.",
    "Bathroom": "please thoroughly clean sink/tub, toilet, mirror, floor, and swap rags.",
}

GROUP_DESCRIPTIONS = {
    "Fridge Clean Out": "everyone get together to clear out their old/expired stuff.",
}


def get_chore_description(chore: str) -> str:
    if chore in CHORE_DESCRIPTIONS:
        return CHORE_DESCRIPTIONS[chore]
    if chore in GROUP_DESCRIPTIONS:
        return GROUP_DESCRIPTIONS[chore]
    return ""


def build_person_message(name: str, personal_chores: list[dict],
                         group_chores: list[str],
                         others: dict[str, list[str]]) -> str:
    """Build one consolidated message for a person."""
    lines = [f"hi {name}!!", ""]
    lines.append("your chores for this week:")

    if personal_chores:
        for chore in personal_chores:
            desc = get_chore_description(chore["chore"])
            lines.append(f"-> {chore['chore']} \u2014 {desc}")
    else:
        lines.append("-> None")

    if group_chores:
        lines.append("")
        lines.append("group:")
        for chore_name in group_chores:
            desc = GROUP_DESCRIPTIONS.get(chore_name, "")
            lines.append(f"-> {chore_name} \u2014 {desc}")

    lines.append("")
    for other_name, chores in others.items():
        chore_str = ", ".join(chores) if chores else "none"
        lines.append(f"{other_name}'s chores: {chore_str}")

    return "\n".join(lines)
