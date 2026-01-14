import enum
from typing import Dict
from .items import level_names

from BaseClasses import CollectionState







def get_rules(world):
    rules = {
        "locations": {

            "127 Minutes":
                lambda state:
                    state.has("Blazerang", world.player) or state.has("Progressive Rang", world.player, 1),
            "DIVE HARD":
                lambda state:
                    state.has("Blizzerang", world.player) or state.has("Progressive Rang", world.player, 2),
            "Dennis' Dilemma":
                lambda state:
                    state.has("Blizzerang", world.player) or state.has("Progressive Rang", world.player, 2),
            "Surf's Down":
                lambda state:
                    state.has("Plasmarang", world.player) or state.has("Progressive Rang", world.player, 3),
            "Mmmm... Lamingtons":
                lambda state:
                    state.has("Plasmarang", world.player) or state.has("Progressive Rang", world.player, 3),
            "That Lost Island":
                lambda state:
                    state.has("Plasmarang", world.player) or state.has("Progressive Rang", world.player, 3),
            "Nano-Proof Fence":
                lambda state:
                    state.has("Plasmarang", world.player) or state.has("Progressive Rang", world.player, 3),
            "Sheepskin Sweatshop":
                lambda state:
                (state.has("Blazerang", world.player) and state.has("Plasmarang", world.player))
                    or state.has("Progressive Rang", world.player, 3),
            "As TY Goes By...":
                lambda state:
                    state.has("Infinirang", world.player) or state.has("Progressive Rang", world.player, 4),
            "Treetop Terror Danger Arena":
                lambda state:
                    state.has("Blizzarang", world.player) or state.has("Progressive Rang", world.player, 2),
        },


        "entrances": {
            "Menu -> 127 Minutes - Up the Magpies":
                lambda state: state.has("127 Minutes - Up the Magpies Unlock", world.player),
            "127 Minutes - Up the Magpies -> 127 Minutes - Up the Magpies - Ice Wall":
                lambda state: state.has("Blazerang", world.player) or state.has("Progressive Rang", world.player, 1),
            "Menu -> 127 Minutes - Lenny's List":
                lambda state: state.has("127 Minutes - Lenny's List Unlock", world.player),
            "Menu -> 127 Minutes":
                lambda state: state.has("127 Minutes Unlock", world.player),
            "Menu -> Dam Busted - Six Skink Shrink Sink":
                lambda state: state.has("Dam Busted - Six Skink Shrink Sink Unlock", world.player),
            "Menu -> Dam Busted - Crocolossal Collapse":
                lambda state: state.has("Dam Busted - Crocolossal Collapse Unlock", world.player),
            "Menu -> Dam Busted":
                lambda state: state.has("Dam Busted Unlock", world.player),
            "Menu -> Three Hour Tour - Tidal Trouble":
                lambda state: state.has("Three Hour Tour -Tidal Trouble Unlock", world.player),
            "Menu -> Three Hour Tour - Ghastly Ghost Ships":
                lambda state: state.has("Three Hour Tour - Ghastly Ghost Ships Unlock", world.player),
            "Menu -> Three Hour Tour":
                lambda state: state.has("Three Hour Tour Unlock", world.player),
            "Menu -> Black Stump BBQ - Dag Nab 'Em":
                lambda state: state.has("Blizzarang", world.player)
                    and state.has("Black Stump BBQ - Dag Nab 'Em Unlock", world.player),
            "Menu -> Black Stump BBQ - Jack Squats":
                lambda state: state.has("Black Stump BBQ - Jack Squats Unlock", world.player)
                    and (state.has("Blizzarang", world.player) or state.has("Progressive Rang", world.player, 2)),
            "Menu -> Black Stump BBQ":
                lambda state: state.has("Black Stump BBQ Unlock", world.player)
                    and (state.has("Blizzarang", world.player) or state.has("Progressive Rang", world.player, 2)),
            "Menu -> Raise the TYtanic - Treasure of the Parrot's Beard":
                lambda state: state.has("Raise the TYtanic - Treasure of the Parrot's Beard Unlock", world.player),
            "Menu -> Raise the TYtanic - Voyage to the Bottom of the Water":
                lambda state: state.has("Raise the TYtanic - Voyage to the Bottom of the Water Unlock", world.player),
            "Menu -> Raise the TYtanic":
                lambda state: state.has("Raise the TYtanic Unlock", world.player),
            "Menu -> Ranger in Danger - DIVE HARD":
                lambda state: state.has("Ranger in Danger - DIVE HARD Unlock", world.player)
                    and (state.has("Blizzarang", world.player) or state.has("Progressive Rang", world.player, 2)),
            "Menu -> Ranger in Danger - Dennis' Dilemma":
                lambda state: state.has("Ranger in Danger - Dennis' Dilemma Unlock", world.player),
            "Menu -> Ranger in Danger":
                lambda state: state.has("Ranger in Danger Unlock", world.player),
            "Menu -> That Lost Island - Surf's Down":
                lambda state: state.has("That Lost Island - Surf's Down Unlock", world.player),
            "Menu -> That Lost Island - Mmmm... Lamingtons":
                lambda state: state.has("That Lost Island - Mmmm... Lamingtons Unlock", world.player),
            "Menu -> That Lost Island":
                lambda state: state.has("That Lost Island Unlock", world.player),
            "Menu -> Crabby Convoys - Lunchabiblies":
                lambda state: state.has("Crabby Convoys - Lunchabiblies Unlock", world.player),
            "Menu -> Crabby Convoys - DIVE HARDER":
                lambda state: state.has("Crabby Convoys - DIVE HARDER Unlock", world.player),
            "Menu -> Crabby Convoys":
                lambda state: state.has("Crabby Convoys Unlock", world.player),
            "Menu -> Fair Dinkum Drinking - Nano-Proof Fence":
                lambda state: state.has("Fair Dinkum Drinking - Nano-Proof Fence Unlock", world.player),
            "Menu -> Fair Dinkum Drinking - Sheepskin Sweatshop":
                lambda state: state.has("Fair Dinkum Drinking - Sheepskin Sweatshop Unlock", world.player),
            "Menu -> Fair Dinkum Drinking":
                lambda state: state.has("Fair Dinkum Drinking Unlock", world.player),

            "Menu -> 127 Minutes - All":
                lambda state: state.has("127 Minutes Unlock", world.player)
                    and state.has("127 Minutes - Up the Magpies Unlock", world.player)
                    and state.has("127 Minutes - Lenny's List Unlock", world.player)
                    and (state.has("Blazerang", world.player) and state.has("Blizzarang", world.player)
                         or state.has("Progressive Rang", world.player, 2))
                    and state.has("Cryptorang", world.player),

            "Menu -> Dam Busted - All":
                lambda state: state.has("Dam Busted Unlock", world.player)
                    and state.has("Dam Busted - Six Skink Shrink Sink Unlock", world.player)
                    and state.has("Dam Busted - Crocolossal Collapse", world.player)
                    and (state.has("Plasmarang", world.player) or state.has("Progressive Rang", world.player, 3))
                    and state.has("Cryptorang", world.player),

            "Menu -> Three Hour Tour - All":
                lambda state: state.has("Three Hour Tour Unlock", world.player)
                    and state.has("Three Hour Tour - Tidal Trouble Unlock", world.player)
                    and state.has("Three Hour Tour - Ghastly Ghost Ships Unlock", world.player)
                    and (state.has("Blazerang", world.player) and state.has("Blizzerang", world.player)
                         or state.has("Progressive Rang", world.player, 2))
                    and state.has("Cryptorang", world.player),

            "Menu -> Black Stump BBQ - All":
                lambda state: state.has("Black Stump BBQ Unlock", world.player)
                    and state.has("Black Stump BBQ - Dag Nab 'Em", world.player)
                    and state.has("Black Stump BBQ - Jack Squats", world.player)
                    and (state.has("Blazerang", world.player) and state.has("Blizzerang", world.player)
                         or state.has("Progressive Rang", world.player, 2))
                    and state.has("Cryptorang", world.player),

            "Menu -> Raise the TYtanic - All":
                lambda state: state.has("Raise the TYtanic Unlock", world.player)
                    and state.has("Raise the TYtanic - Treasure of the Parrot's Beard Unlock", world.player)
                    and state.has("Raise the TYtanic - Voyage to the Bottom of the Water Unlock", world.player),

            "Menu -> Ranger in Danger - All":
                lambda state: state.has("Ranger in Danger Unlock", world.player)
                    and state.has("Ranger in Danger - DIVE HARD", world.player)
                    and state.has("Ranger in Danger - Dennis' Dilemma", world.player)
                    and (state.has("Blazerang", world.player) and state.has("Blizzerang", world.player)
                         or state.has("Progressive Rang", world.player, 2))
                    and state.has("Cryptorang", world.player),

            "Menu -> That Lost Island - All":
                lambda state: state.has("That Lost Island Unlock", world.player)
                    and state.has("That Lost Island - Surf's Down", world.player)
                    and state.has("That Lost Island - Mmmm... Lamingtons Unlock", world.player)
                    and state.has("Cryptorang", world.player),

            "Menu -> Crabby Convoys - All":
                lambda state: state.has("Crabby Convoys Unlock", world.player)
                    and state.has("Crabby Convoys - Lunchabiblies", world.player)
                    and state.has("Crabby Convoys - DIVE HARDER", world.player)
                    and (state.has("Blazerang", world.player) and state.has("Plasmarang", world.player)
                         or state.has("Progressive Rang", world.player, 3))
                    and state.has("Cryptorang", world.player),

            "Menu -> Fair Dinkum Drinking - All":
                lambda state: state.has("Fair Dinkum Drinking Unlock", world.player)
                    and state.has("Fair Dinkum Drinking - Nano-Proof Fence", world.player)
                    and state.has("Fair Dinkum Drinking - Sheepskin Sweatshop", world.player)
                    and (state.has("Blazerang", world.player) or state.has("Progressive Rang", world.player, 1))
                    and state.has("Cryptorang", world.player),
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
