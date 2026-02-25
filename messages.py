"""
Message templates for chore reminders.
Casual, friendly tone — edit these however you want!
"""

VACUUM_MESSAGE = """hiii {name}!! \U0001f9f9 you're on vacuum duty this week ~

here's what needs a good vacuum!
- kitchen floor
- entryway
- dining area
- living room
{hallway_note}
tysm you're an angel!! \U0001f495"""

VACUUM_HALLWAY_ADDON = """- also the shared hallway too if you're maya/bri :)!
"""

MOPPING_MESSAGE = """hiii {name}!! \U0001faa3 it's your month to mop :)

floors that need mopping!
- kitchen
- entryway
- dining room

lil heads up \u2014 {vacuum_person} is vacuuming this week so try to mop AFTER she's done so the floors are clear first! just coordinate w her.

also!! if the fridge is looking a bit full or dirty, rally the girls for a group fridge clean out \U0001f9ca\u2728 tysm!! \U0001f4ab"""

STEEL_MESSAGE = """hiii {name}!! \U0001fa9e it's your month for stainless steel duty ~

part 1 \u2014 stainless steel surfaces (grab the stainless steel wipes!):
- fridge exterior
- steel plate next to the burner
- oven exterior
- dishwasher exterior

part 2 \u2014 burner area:
- take out the burners
- wipe down all the steel underneath/around them
- pop the burners back in

part 3 \u2014 microwave:
- wipe down the inside of the microwave!

ty queen!! \U0001f451"""

BATHROOM_MESSAGE = """hiii {name}!! \U0001f6bf you're up for the biweekly bathroom clean!!

here's the full list:
- sink/tub \u2014 scrubbing bubbles spray + scrub daddy scrub
- toilet \u2014 bowl, seat, underseat, and base
- mirror \u2014 wipe
- swap out the rags for fresh ones

slay tysm!! \u2728"""


WIPEDOWN_MESSAGE = """hiii {name}!! \U0001e4ff you're on wipe-down duty this week ~

here's what needs a quick wipe!
- kitchen counters
- dining table
- console table
- if there are any spills on the floor, just a quick wipe (no full mop needed!)

quick and easy 5 min tops. tysm!! \U0001f495"""


def get_wipedown_message(name: str) -> str:
    return WIPEDOWN_MESSAGE.format(name=name)


def get_vacuum_message(name: str, include_hallway: bool) -> str:
    hallway_note = VACUUM_HALLWAY_ADDON if include_hallway else ""
    return VACUUM_MESSAGE.format(name=name, hallway_note=hallway_note)


def get_mopping_message(name: str, vacuum_person: str) -> str:
    return MOPPING_MESSAGE.format(name=name, vacuum_person=vacuum_person)


def get_steel_message(name: str) -> str:
    return STEEL_MESSAGE.format(name=name)


def get_bathroom_message(name: str) -> str:
    return BATHROOM_MESSAGE.format(name=name)
