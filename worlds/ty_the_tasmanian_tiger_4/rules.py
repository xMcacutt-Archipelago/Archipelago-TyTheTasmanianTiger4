import enum
from typing import Dict
from .items import level_names

from BaseClasses import CollectionState







def get_rules(world):
    rules = {
        "locations": {

            "Attribute - Zoomerang":
                lambda state:
                    state.has("Golden Cog", world.player, world.options.cog_gating * 1),
            "Attribute - Multirang":
                lambda state:
                    state.has("Golden Cog", world.player, world.options.cog_gating * 2),
            "Rainbow Cliffs - All Picture Frames":
                lambda state:
                    state.can_reach_region("Final Gauntlet - PF", world.player) and
                    state.can_reach_region("Pippy Beach - PF", world.player) and
                    state.can_reach_region("Bli Bli Station Gate - PF", world.player),
            "WitP - Time Attack Challenge":
                lambda state:
                    state.can_reach_location("WitP - Wombat Race", world.player),
            "Snow Worries - Time Attack Challenge":
                lambda state:
                    state.can_reach_location("Snow Worries - Time Attack", world.player),
            "Outback Safari - Time Attack Challenge":
                lambda state:
                    state.can_reach_location("Outback Safari - Race Shazza", world.player),
            "LLPoF - Time Attack Challenge":
                lambda state:
                    state.can_reach_location("LLPoF - Time Attack", world.player),
            "BtBS - Time Attack Challenge":
                lambda state:
                    state.can_reach_location("BtBS - Wombat Rematch", world.player),
            "Beat Bull":
                lambda state:
                    state.can_reach_location("Frog Talisman", world.player),
            "Beat Crikey":
                lambda state:
                    state.can_reach_location("Platypus Talisman", world.player),
            "Beat Fluffy":
                lambda state:
                    state.can_reach_location("Cockatoo Talisman", world.player),
            "Beat Shadow":
                lambda state:
                    state.can_reach_location("Dingo Talisman", world.player),
            "Beat Cass":
                lambda state:
                    state.can_reach_location("Tiger Talisman", world.player)
        },
        "entrances": {
            "Menu -> Dag Nab 'Em":
                lambda state:
                    state.has("Blizzarang", world.player),
            "Menu -> Jack Squats":
                lambda state:
                    state.has("Blizzarang", world.player),
            "Menu -> Black Stump BBQ":
                lambda state:
                    state.has("Blizzarang", world.player),
            "Menu -> DIVE HARD":
                lambda state:
                state.has("Blizzarang", world.player),
        }
    }
    return rules

def create_events(world):
    for level_name in level_names:
        world.create_event(level_name, f"{level_name} Complete", "Level Complete")


def set_rules(world):
    from . import Ty4World
    world: Ty4World
    rules_lookup = get_rules(world)
    for entrance_name, rule in rules_lookup["entrances"].items():
        try:
            world.get_entrance(entrance_name).access_rule = rule
        except KeyError:
            pass

    for location_name, rule in rules_lookup["locations"].items():
        try:
            world.get_location(location_name).access_rule = rule
        except KeyError:
            pass

    world.create_event("As Ty Goes By...", "Beat Cass", "Beat Cass")
    world.get_location("Beat Cass").access_rule = lambda state:\
        state.has("Infinirang", world.player) or state.has("Progressive Rang", world.player, 4)
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Beat Cass", world.player)
