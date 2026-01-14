from .items import level_names



def can_burn(world, state):
        return state.has("Blazerang", world.player) or state.has("Progressive Rang", world.player, 1)
def can_freeze(world, state):
        return state.has("Blizzerang", world.player) or state.has("Progressive Rang", world.player, 2)
def can_zap(world, state):
        return state.has("Zappyrang", world.player) or state.has("Progressive Rang", world.player, 3)



def get_rules(world):
    rules = {
        "locations": {

            "127 Minutes":
                lambda state:
                    can_burn(world, state),
            "DIVE HARD":
                lambda state:
                    can_freeze(world, state),
            "Dennis' Dilemma":
                lambda state:
                    can_freeze(world, state),
            "Surf's Down":
                lambda state:
                    can_zap(world, state),
            "Mmmm... Lamingtons":
                lambda state:
                    can_zap(world, state),
            "That Lost Island":
                lambda state:
                    can_zap(world, state),
            "Nano-Proof Fence":
                lambda state:
                    can_zap(world, state),
            "Sheepskin Sweatshop":
                lambda state:
                can_burn(world, state) and can_zap(world, state),
            "As TY Goes By...":
                lambda state:
                    state.has("Infinirang", world.player) or state.has("Progressive Rang", world.player, 4),
            "Treetop Terror Danger Arena":
                lambda state:
                    can_freeze(world, state),
            "Up the Magpies Berry 2":
                lambda state:
                    can_freeze(world, state),
            "Lenny's List Berry 3":
                lambda state:
                    can_burn(world, state),
            "Crocolossal Collapse Berry 2":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Dam Busted Berry 1":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Dam Busted Berry 2":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Dam Busted Berry 3":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Tidal Trouble Berry 2":
                lambda state:
                    can_burn(world, state) and can_freeze(world, state),
            "Ghastly Ghost Ships Berry 2":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Three Hour Tour Berry 1":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Three Hour Tour Berry 3":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Dag Nab 'Em Berry 1":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Jack Squats Berry 1":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Jack Squats Berry 2":
                lambda state:
                    can_burn(world, state),
            "Raise the TYtanic Berry 3":
                lambda state:
                    state.has("Cryptorang", world.player),
            "DIVE HARD Berry 1":
                lambda state:
                    state.has("Cryptorang", world.player),
            "DIVE HARD Berry 2":
                lambda state:
                    can_burn(world, state),
            "DIVE HARD Berry 3":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Dennis' Dilemma Berry 2":
                lambda state:
                    can_burn(world, state) and can_freeze(world, state),
            "Dennis' Dilemma Berry 3":
                lambda state:
                    can_freeze(world, state),
            "Ranger in Danger Berry 1":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Ranger in Danger Berry 2":
                lambda state:
                    can_freeze(world, state),
            "Ranger in Danger Berry 3":
                lambda state:
                    can_freeze(world, state),
            "That Lost Island Berry 1":
                lambda state:
                    state.has("Cryptorang", world.player),
            "That Lost Island Berry 3":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Lunchabiblies Berry 3":
                lambda state:
                    state.has("Cryptorang", world.player),
            "DIVE HARDER Berry 2":
                lambda state:
                    state.has("Cryptorang", world.player),
            "DIVE HARDER Berry 3":
                lambda state:
                    can_zap(world, state),
            "Crabby Convoys Berry 2":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Crabby Convoys Berry 3":
                lambda state:
                    can_burn(world, state),
            "Nano-Proof Fence Berry 1":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Nano-Proof Fence Berry 3":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Sheepskin Sweatshop Berry 3":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Fair Dinkum Drinking Berry 2":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Lenny's List Koala 2":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Dam Busted Koala 1":
                lambda state:
                    can_zap(world, state),
            "Tidal Trouble Koala 1":
                lambda state:
                    can_burn(world,state),
            "Dag Nab 'Em Koala 2":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Dennis' Dilemma Koala 1":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Dennis' Dilemma Koala 2":
                lambda state:
                    can_freeze(world, state),
            "Ranger in Danger Koala 2":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Surf's Down Koala 2":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Mmmm... Lamingtons Koala 2":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Lunchabiblies Koala 1":
                lambda state:
                    can_freeze(world, state) and state.has("Cryptorang", world.player),
            "Lunchabiblies Koala 2":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Crabby Convoys Koala 2":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Nano-Proof Fence Koala 1":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Nano-Proof Fence Koala 2":
                lambda state:
                    can_burn(world, state),
            "Sheepskin Sweatshop Koala 2":
                lambda state:
                    can_burn(world, state),
            "Fair Dinkum Drinking Koala 1":
                lambda state:
                    state.has("Cryptorang", world.player),
            "Crocolossal Collapse - Escort Ranger Ken":
                lambda state:
                    can_burn(world, state),
            "Ghastly Ghost Ships - Ghost Ships":
                lambda state:
                    state.has("Cryptorang", world.player),
            "That Lost Island - SOS":
                lambda state:
                    can_zap(world, state),
            "Nano-Proof Fence - Fence Patches":
                lambda state:
                    can_freeze(world, state),
        },


        "entrances": {
            "Menu -> 127 Minutes - Up the Magpies":
                lambda state: state.has("127 Minutes - Up the Magpies Unlock", world.player),
            "127 Minutes - Up the Magpies -> 127 Minutes - Up the Magpies - Ice Wall":
                lambda state: can_burn(world, state),
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
                lambda state: can_freeze(world, state)
                    and state.has("Black Stump BBQ - Dag Nab 'Em Unlock", world.player),
            "Menu -> Black Stump BBQ - Jack Squats":
                lambda state: state.has("Black Stump BBQ - Jack Squats Unlock", world.player)
                    and can_freeze(world, state),
            "Menu -> Black Stump BBQ":
                lambda state: state.has("Black Stump BBQ Unlock", world.player)
                    and can_freeze(world, state),
            "Menu -> Raise the TYtanic - Treasure of the Parrot's Beard":
                lambda state: state.has("Raise the TYtanic - Treasure of the Parrot's Beard Unlock", world.player),
            "Menu -> Raise the TYtanic - Voyage to the Bottom of the Water":
                lambda state: state.has("Raise the TYtanic - Voyage to the Bottom of the Water Unlock", world.player),
            "Menu -> Raise the TYtanic":
                lambda state: state.has("Raise the TYtanic Unlock", world.player),
            "Menu -> Ranger in Danger - DIVE HARD":
                lambda state: state.has("Ranger in Danger - DIVE HARD Unlock", world.player)
                    and can_freeze(world, state),
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
                    and can_burn(world, state)
                    and can_freeze(world, state)
                    and state.has("Cryptorang", world.player),

            "Menu -> Dam Busted - All":
                lambda state: state.has("Dam Busted Unlock", world.player)
                    and state.has("Dam Busted - Six Skink Shrink Sink Unlock", world.player)
                    and state.has("Dam Busted - Crocolossal Collapse", world.player)
                    and can_zap(world, state)
                    and state.has("Cryptorang", world.player),

            "Menu -> Three Hour Tour - All":
                lambda state: state.has("Three Hour Tour Unlock", world.player)
                    and state.has("Three Hour Tour - Tidal Trouble Unlock", world.player)
                    and state.has("Three Hour Tour - Ghastly Ghost Ships Unlock", world.player)
                    and can_burn(world, state)
                    and can_freeze(world, state)
                    and state.has("Cryptorang", world.player),

            "Menu -> Black Stump BBQ - All":
                lambda state: state.has("Black Stump BBQ Unlock", world.player)
                    and state.has("Black Stump BBQ - Dag Nab 'Em", world.player)
                    and state.has("Black Stump BBQ - Jack Squats", world.player)
                    and can_burn(world, state)
                    and can_freeze(world, state)
                    and state.has("Cryptorang", world.player),

            "Menu -> Raise the TYtanic - All":
                lambda state: state.has("Raise the TYtanic Unlock", world.player)
                    and state.has("Raise the TYtanic - Treasure of the Parrot's Beard Unlock", world.player)
                    and state.has("Raise the TYtanic - Voyage to the Bottom of the Water Unlock", world.player),

            "Menu -> Ranger in Danger - All":
                lambda state: state.has("Ranger in Danger Unlock", world.player)
                    and state.has("Ranger in Danger - DIVE HARD", world.player)
                    and state.has("Ranger in Danger - Dennis' Dilemma", world.player)
                    and can_burn(world, state)
                    and can_freeze(world, state)
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
                    and can_burn(world, state)
                    and can_zap(world, state)
                    and state.has("Cryptorang", world.player),

            "Menu -> Fair Dinkum Drinking - All":
                lambda state: state.has("Fair Dinkum Drinking Unlock", world.player)
                    and state.has("Fair Dinkum Drinking - Nano-Proof Fence", world.player)
                    and state.has("Fair Dinkum Drinking - Sheepskin Sweatshop", world.player)
                    and can_burn(world, state)
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
