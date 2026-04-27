# Message Previews

Each person gets **one text per week** with their chores, any group chores, and what everyone else is doing. Edit descriptions in `messages.py`.

---

## Example: Regular week (Apr 30)

Maya has Wipe-down, Sophie has Laundry, Bri has Bathroom, Alizeh has Vacuuming.

**Maya's text:**

> hi Maya!!
>
> your chores for this weekend:
> 1. Wipe-down — please wipe kitchen counters, dining table, console table, and any floor spills.
>
> Sophie's chores: Wash Rags & Towels
> Bri's chores: Bathroom
> Alizeh's chores: Vacuuming

---

## Example: Fridge week (May 21)

Bri has Vacuuming + Hallway, Sophie has Mopping, Alizeh has Wipe-down, everyone has Fridge.

**Bri's text:**

> hi Bri!!
>
> your chores for this weekend:
> 1. Vacuuming — please vacuum kitchen floor, entryway, dining area, living room. Maya/Bri also do the shared hallway.
>
> group:
> 1. Fridge Clean Out — everyone get together to clear out their old/expired stuff.
>
> Maya's chores: none
> Sophie's chores: Mopping
> Alizeh's chores: Wipe-down

---

## Chore descriptions

| Chore | Description |
|-------|-------------|
| Vacuuming | please vacuum kitchen floor, entryway, dining area, living room. Maya/Bri also do the shared hallway. |
| Wipe-down | please wipe kitchen counters, dining table, console table, and any floor spills. |
| Mopping | please mop kitchen, entryway, dining room. coordinate after that week's vacuum. |
| Stainless Steel | please wipe the steel on fridge, oven, dishwasher, burner area, and inside the microwave. |
| Wash Rags & Towels | please gather communal rags/towels and throw them in the wash. |
| Bathroom | please thoroughly clean sink/tub, toilet, mirror, floor, and swap rags. |
| Fridge Clean Out | everyone get together to clear out their old/expired stuff. |

---

## Rotation orders

| Chore | Frequency | Rotation order |
|-------|-----------|----------------|
| Vacuuming | Weekly | Sophie → Bri → Alizeh → Maya |
| Wipe-down | Weekly | Bri → Alizeh → Maya → Sophie |
| Mopping | Every 2 weeks | Bri → Alizeh → Maya → Sophie |
| Stainless Steel | Every 4 weeks | Alizeh → Maya → Sophie → Bri |
| Wash Rags & Towels | Every 2 weeks | Maya → Sophie → Bri → Alizeh |
| Bathroom | Every 2 weeks | Bri → Maya → Sophie |
| Fridge Clean Out | Every 4 weeks | All 4 (group message) |

*To edit chore descriptions, open `messages.py` and change `CHORE_DESCRIPTIONS` or `GROUP_DESCRIPTIONS`.*
