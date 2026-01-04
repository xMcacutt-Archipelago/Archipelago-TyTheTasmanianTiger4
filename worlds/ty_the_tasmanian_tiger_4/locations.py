from BaseClasses import Location, Region
from worlds.ty_the_tasmanian_tiger_4.options import Ty4Options


class Ty4Location(Location):
    game: str = "Ty the Tasmanian Tiger"


class LocData:
    def __init__(self, code: int, region: str):
        """
        Represents a location with associated conditions.

        :param code: A unique identifier for the location.
        :param region: Name of the containing region.
        """
        self.code = code
        self.region = region


def create_location(player: int, reg: Region, name: str, code: int):
    location = Ty4Location(player, name, code, reg)
    reg.locations.append(location)


def create_locations_from_dict(loc_dict, reg, player):
    for (key, data) in loc_dict.items():
        if data.region != reg.name:
            continue
        create_location(player, reg, key, data.code)


def create_locations(player: int, options: Ty4Options, reg: Region):
    # Level Completion
    create_locations_from_dict(level_completion_dict, reg, player)
    # Rang Shop
    create_locations_from_dict(rang_shop_dict, reg, player)
    # Costume Shop
    create_locations_from_dict(costume_shop_dict, reg, player)
    # TALISMANS
    create_locations_from_dict(berry_dict, reg, player)
    # ATTRIBUTES
    create_locations_from_dict(koala_dict, reg, player)
    #THUNDER EGGS
    create_locations_from_dict(thunder_egg_dict, reg, player)

level_completion_dict = {
    "Prologue": LocData(0x1, "Prologue"),
    "Up the Magpies": LocData(0x2, "127 Minutes - UtM - Ice Wall"),
    "Lenny's List": LocData(0x3, "127 Minutes - LL"),
    "127 Minutes": LocData(0x4, "127 Minutes"), #flame
    "Six Skink Shrink Sink": LocData(0x5, "Dam Busted - SSSS"),
    "Crocolossal Collapse": LocData(0x6, "Dam Busted - CC"),
    "Dam Busted": LocData(0x7, "Dam Busted"),
    "Tidal Trouble": LocData(0x8, "Three Hour Tour - TT"),
    "Ghastly Ghost Ships": LocData(0x9, "Three Hour Tour - GGS"),
    "Three Hour Tour": LocData(0xA, "Three Hour Tour"),
    "Fluffy's Follies": LocData(0xB, "Fluffy's Follies"),
    "Dag Nab 'Em": LocData(0xC, "Black Stump BBQ - DNE"),
    "Jack Squats": LocData(0xD, "Black Stump BBQ - JS"),
    "Black Stump BBQ": LocData(0xE, "Black Stump BBQ"),
    "Treasure of the Parrot's Beard": LocData(0xF, "Raise the TYtanic - TPB"),
    "Voyage to the Bottom of the Water": LocData(0x10, "Raise the TYtanic - VBW"),
    "Raise the TYtanic": LocData(0x11, "Raise the Tytanic"),
    "DIVE HARD": LocData(0x12, "Ranger in Danger - DH"), #Frosty
    "Dennis' Dilemma": LocData(0x13, "Ranger in Danger - DD"), #Frosty
    "Ranger in Danger": LocData(0x14, "Ranger in Danger"),
    "Sly Spy With My Little Eye": LocData(0x15, "Sly Spy With My Little Eye"),
    "Surf's Down": LocData(0x16, "That Lost Island - SD"), #Zappy
    "Mmmm... Lamingtons": LocData(0x17, "That Lost Island - ML"), #Zappy
    "That Lost Island": LocData(0x18, "That Lost Island"), #Zappy
    "Lunchabiblies": LocData(0x19, "Crabby Convoys - LB"), #yes, they misspelled bilbies in their own lunchables pun
    "DIVE HARDER": LocData(0x1A, "Crabby Convoys - DH"),
    "Crabby Convoys": LocData(0x1B, "Crabby Convoys"),
    "Nano-Proof Fence": LocData(0x1C, "Fair Dinkum Drinking - NPF"), #Zappy
    "Sheepskin Sweatshop": LocData(0x1D, "Fair Dinkum Drinking - SS"), #Zappy Flame
    "Fair Dinkum Drinking": LocData(0x1E, "Fair Dinkum Drinking"),
    "Around the Back Way": LocData(0x1F, "As TY Goes By... - ABW"),
    "As TY Goes By...": LocData(0x20, "As TY Goes By..."), #Infinirang



}

rang_shop_dict = {
    "Hyperang": LocData(0x21, "Rang Shop"),
    "Chaosrang": LocData(0x22, "Rang Shop"),
    "Deadlyrang": LocData(0x23, "Rang Shop"),
    "Cryptorang": LocData(0x24, "Rang Shop"),
    "Disruptorang": LocData(0x25, "Rang Shop"),
    "Doomerang": LocData(0x26, "Rang Shop"),

}

costume_shop_dict = {
    "Ty1": LocData(0x27, "Costume Shop"),
    "Ty2": LocData(0x28, "Costume Shop"),
    "Bunyip Gauntlet": LocData(0x29, "Costume Shop"),
    "Ty5": LocData(0x2A, "Costume Shop"),
    "Concept Ty": LocData(0x2B, "Costume Shop"),
    "Retro Ty": LocData(0x2C, "Costume Shop"),
    "Chicken Suit": LocData(0x2D, "Costume Shop"),
    "Secret Agent": LocData(0x2E, "Costume Shop"),
    "Rashy": LocData(0x2F, "Costume Shop"),
    "Snow Warrior": LocData(0x30, "Costume Shop"),
    "Shazza": LocData(0x31, "Costume Shop"),
    "Shazza the Dingo": LocData(0x32, "Costume Shop"),
    "Sly": LocData(0x33, "Costume Shop"),
    "Sly Cape": LocData(0x34, "Costume Shop"),
    "Shadowy Figure": LocData(0x35, "Costume Shop"),
    "Kid Sly": LocData(0x36, "Costume Shop"),
    "Sly Fiver": LocData(0x37, "Costume Shop"),
    "Naomi": LocData(0x38, "Costume Shop"),
    "Producer Naomi": LocData(0x39, "Costume Shop"),
    "Di": LocData(0x3A, "Costume Shop"),
    "Bri": LocData(0x3B, "Costume Shop"),
    "Betty": LocData(0x3C, "Costume Shop"),
    "Ridge": LocData(0x3D, "Costume Shop"),
    "Landscaping Ridge": LocData(0x3E, "Costume Shop"),
    "Brolga": LocData(0x3F, "Costume Shop"),
    "Garden Brolga": LocData(0x40, "Costume Shop"),
    "Flinders": LocData(0x41, "Costume Shop"),
    "Pippa": LocData(0x42, "Costume Shop"),
    "Doomeranger": LocData(0x43, "Costume Shop"),
    "Frill Disguise": LocData(0x44, "Costume Shop"),
    "Cy X": LocData(0x45, "Costume Shop"),
    "Cyber": LocData(0x46, "Costume Shop"),
    "Skye": LocData(0x47, "Costume Shop"),
    "Bligh": LocData(0x48, "Costume Shop"),

}

minigame_dict = {
    "Rainforest Run Time Attack": LocData(0x49, "127 Minutes - UtM - Ice Wall"),
    "Treetop Terror Danger Arena": LocData(0x4A, "127 Minutes - LL"),
    "Red Rock Rush Time Attack": LocData(0x4B, "Dam Busted - CC "),
    "Sandy Shore Sprint Time Attack": LocData(0x4C, "Three Hour Tour - GGS"),
    "Surf Turkey": LocData(0x4D, "Three Hour Tour"),
    "Jive Turkey": LocData(0x4E, "Black Stump BBQ - DNE"),
    "Sleep With the Fishes Danger Arena": LocData(0x4F, "Raise the TYtanic"),
    "Outback Outrun Time Attack": LocData(0x50, "Ranger in Danger - DD"),
    "Splash Wave Scuttle Time Attack": LocData(0x51, "That Lost Island - SD"),
    "Scrub Turkey": LocData(0x52, "Crabby Convoys - LB"),
    "Dusty Dust-Up": LocData(0x53, "Fair Dinkum Drinking - SS"),

}

berry_dict = {
    "Up the Magpies Berry 1": LocData(0x5A, "127 Minutes - UtM"), # no reqs
    "Up the Magpies Berry 2": LocData(0x5B, "127 Minutes - UtM - Ice Wall"), # frosty
    "Up the Magpies Berry 3": LocData(0x5C, "127 Minutes - UtM - Ice Wall"), # end of level teleport shrooms
    "Lenny's List Berry 1": LocData(0x5D, "127 Minutes - LL"), # no reqs
    "Lenny's List Berry 2": LocData(0x5E, "127 Minutes - LL"), # shrooms after lenny's house
    "Lenny's List Berry 3": LocData(0x5F, "127 Minutes - LL"), # Flame
    "127 Minutes Berry 1": LocData(0x60, "127 Minutes"), # stupid coyote time jump
    "127 Minutes Berry 2": LocData(0x61, "127 Minutes"), # shrooms
    "127 Minutes Berry 3": LocData(0x62, "127 Minutes"), # button at end
    "Six Skink Shrink Sink Berry 1": LocData(0x63, "Dam Busted - SSSS"), # sheep
    "Six Skink Shrink Sink Berry 2": LocData(0x64, "Dam Busted - SSSS"), # timed berry
    "Six Skink Shrink Sink Berry 3": LocData(0x65, "Dam Busted - SSSS"), # no reqs
    "Crocolossal Collapse Berry 1": LocData(0x66, "Dam Busted - CC"), # no reqs
    "Crocolossal Collapse Berry 2": LocData(0x67, "Dam Busted - CC"), # infra
    "Crocolossal Collapse Berry 3": LocData(0x68, "Dam Busted - CC"), # no reqs
    "Dam Busted Berry 1": LocData(0x69, "Dam Busted"), # infra
    "Dam Busted Berry 2": LocData(0x6A, "Dam Busted"), # infra
    "Dam Busted Berry 3": LocData(0x6B, "Dam Busted"), # infra at end
    "Tidal Trouble Berry 1": LocData(0x6C, "Three Hour Tour - TT"), # underwater at start
    "Tidal Trouble Berry 2": LocData(0x6D, "Three Hour Tour - TT"), # Flame, Frosty
    "Tidal Trouble Berry 3": LocData(0x6E, "Three Hour Tour - TT"), # Shrooms
    "Ghastly Ghost Ships Berry 1": LocData(0x6F, "Three Hour Tour - GGS"), # Shrooms to behind start
    "Ghastly Ghost Ships Berry 2": LocData(0x70, "Three Hour Tour - GGS"), # infra
    "Ghastly Ghost Ships Berry 3": LocData(0x71, "Three Hour Tour - GGS"), # Lenny's insanely difficult puzzle
    "Three Hour Tour Berry 1": LocData(0x72, "Three Hour Tour"), # Infra
    "Three Hour Tour Berry 2": LocData(0x73, "Three Hour Tour"), # Shrooms
    "Three Hour Tour Berry 3": LocData(0x74, "Three Hour Tour"), # Infra
    "Dag Nab 'Em Berry 1": LocData(0x75, "Black Stump BBQ - DNE"), # Infra
    "Dag Nab 'Em Berry 2": LocData(0x76, "Black Stump BBQ - DNE"), # Button lower elevator in cave
    "Dag Nab 'Em Berry 3": LocData(0x77, "Black Stump BBQ - DNE"), # Button at far left side of sheep drop down
    "Jack Squats Berry 1": LocData(0x78, "Black Stump BBQ - JS"), # Infra
    "Jack Squats Berry 2": LocData(0x79, "Black Stump BBQ - JS"), # Flame behind dennis museum
    "Jack Squats Berry 3": LocData(0x7A, "Black Stump BBQ - JS"), # Above dennis museum
    "Black Stump BBQ Berry 1": LocData(0x7B, "Black Stump BBQ"), # fan platform cave at start
    "Black Stump BBQ Berry 2": LocData(0x7C, "Black Stump BBQ"), # behind dunny before flame 2
    "Black Stump BBQ Berry 3": LocData(0x7D, "Black Stump BBQ"), # Shrooms at koala 1
    "Treasure of the Parrot's Beard Berry 1": LocData(0x7E, "Raise the TYtanic - TPB"), # drop down at start
    "Treasure of the Parrot's Beard Berry 2": LocData(0x7F, "Raise the TYtanic - TPB"), # underwater below parrotbeard
    "Treasure of the Parrot's Beard Berry 3": LocData(0x80, "Raise the TYtanic - TPB"), # underwater in next section after parrotbeard
    "Voyage to the Bottom of the Water Berry 1": LocData(0x81, "Raise the TYtanic - VBW"),
    "Voyage to the Bottom of the Water Berry 2": LocData(0x82, "Raise the TYtanic - VBW"),
    "Voyage to the Bottom of the Water Berry 3": LocData(0x83, "Raise the TYtanic - VBW"),
    "Raise the TYtanic Berry 1": LocData(0x84, "Raise the TYtanic"), # Left underwater below Lenny
    "Raise the TYtanic Berry 2": LocData(0x85, "Raise the TYtanic"), # Right underwater below lenny - Timed button
    "Raise the TYtanic Berry 3": LocData(0x86, "Raise the TYtanic"), # Up and left after clam section - Infra
    "DIVE HARD Berry 1": LocData(0x87, "Ranger in Danger - DH"), # infra top of left side at first split
    "DIVE HARD Berry 2": LocData(0x88, "Ranger in Danger - DH"), # flame light all 4 torches
    "DIVE HARD Berry 3": LocData(0x89, "Ranger in Danger - DH"), # infra timed target at end of level
    "Dennis' Dilemma Berry 1": LocData(0x8A, "Ranger in Danger - DD"), # Above 3rd water wheel
    "Dennis' Dilemma Berry 2": LocData(0x8B, "Ranger in Danger - DD"), # Frosty Flame spy eggs spawned by lighting torch
    "Dennis' Dilemma Berry 3": LocData(0x8C, "Ranger in Danger - DD"), # Frosty spy eggs down at end of level
    "Ranger in Danger Berry 1": LocData(0x8D, "Ranger in Danger"), # Infra up after second dunny
    "Ranger in Danger Berry 2": LocData(0x8E, "Ranger in Danger"), # Frosty above croc pit before 2nd rock run frosty on torch to spawn spy eggs
    "Ranger in Danger Berry 3": LocData(0x8F, "Ranger in Danger"), # Frosty freeze torches at end of level to make log platform lower
    "Surf's Down Berry 1": LocData(0x90, "That Lost Island - SD"), # Up Left from Time Attack
    "Surf's Down Berry 2": LocData(0x91, "That Lost Island - SD"), # Underwater alcove right of Rex
    "Surf's Down Berry 3": LocData(0x92, "That Lost Island - SD"), # Above sand between Generators 3 and 4
    "Mmmm... Lamingtons Berry 1": LocData(0x93, "That Lost Island - ML"), # Above water at start - Timed Button
    "Mmmm... Lamingtons Berry 2": LocData(0x94, "That Lost Island - ML"), # Underwater between Generators 2 and 3 - Hit 3 buttons
    "Mmmm... Lamingtons Berry 3": LocData(0x95, "That Lost Island - ML"), # Above generator 3
    "That Lost Island Berry 1": LocData(0x96, "That Lost Island"), # Infra directly above start
    "That Lost Island Berry 2": LocData(0x97, "That Lost Island"), # Bottom Right underwater between Generator 3 and 4
    "That Lost Island Berry 3": LocData(0x98, "That Lost Island"), # Infra up after Generator 4
    "Lunchabiblies Berry 1": LocData(0x99, "Crabby Convoys - LB"), # Up left from first piston log
    "Lunchabiblies Berry 2": LocData(0x9A, "Crabby Convoys - LB"), # Hidden grotto bottom left corner
    "Lunchabiblies Berry 3": LocData(0x9B, "Crabby Convoys - LB"), # Infra end of level
    "DIVE HARDER Berry 1": LocData(0x9C, "Crabby Convoys - DH"), # Above first cactus
    "DIVE HARDER Berry 2": LocData(0x9D, "Crabby Convoys - DH"), # Infra - Timed button after Generator 4
    "DIVE HARDER Berry 3": LocData(0x9E, "Crabby Convoys - DH"), # Zappy Hit all 5 Generators
    "Crabby Convoys Berry 1": LocData(0x9F, "Crabby Convoys"), # Above Start
    "Crabby Convoys Berry 2": LocData(0x100, "Crabby Convoys"), # Infra lower path after crabdozer 2
    "Crabby Convoys Berry 3": LocData(0x101, "Crabby Convoys"), # Flame Bush behind ice wall at end of level
    "Nano-Proof Fence Berry 1": LocData(0x102, "Fair Dinkum Drinking - NPF"), # Infra after generator 2
    "Nano-Proof Fence Berry 2": LocData(0x103, "Fair Dinkum Drinking - NPF"), # Teleport shrooms under bridge at fence
    "Nano-Proof Fence Berry 3": LocData(0x104, "Fair Dinkum Drinking - NPF"), # Infra above generator 3
    "Sheepskin Sweatshop Berry 1": LocData(0x105, "Fair Dinkum Drinking - SS"), # Timed button - cave below lenny danger arena
    "Sheepskin Sweatshop Berry 2": LocData(0x106, "Fair Dinkum Drinking - SS"), # up from sheep 6
    "Sheepskin Sweatshop Berry 3": LocData(0x107, "Fair Dinkum Drinking - SS"), # Infra above sheep 7
    "Fair Dinkum Drinking Berry 1": LocData(0x108, "Fair Dinkum Drinking"), # above 1st pipe
    "Fair Dinkum Drinking Berry 2": LocData(0x109, "Fair Dinkum Drinking"), # Infra teleport shrooms in pit past pipe one - Timed Button dive to bottom of water
    "Fair Dinkum Drinking Berry 3": LocData(0x10A, "Fair Dinkum Drinking"), # Above 2nd pipe drop-off spot

}

koala_dict = {
    "Up the Magpies Koala 1": LocData(0x10B, "127 Minutes - UtM - Ice Wall"), # teleport shrooms
    "Up the Magpies Koala 2": LocData(0x10C, "127 Minutes - UtM - Ice Wall"), #no reqs
    "Lenny's List Koala 1": LocData(0x10D, "127 Minutes - LL"), # no reqs
    "Lenny's List Koala 2": LocData(0x10E, "127 Minutes - LL"), # infra
    "127 Minutes Koala 1": LocData(0x10F, "127 Minutes"), # no reqs
    "127 Minutes Koala 2": LocData(0x110, "127 Minutes"), # target quick run
    "Six Skink Shrink Sink Koala 1": LocData(0x111, "Dam Busted - SSSS"), # no reqs
    "Six Skink Shrink Sink Koala 2": LocData(0x112, "Dam Busted - SSSS"), # no reqs
    "Crocolossal Collapse Koala 1": LocData(0x113, "Dam Busted - CC"), # no reqs
    "Crocolossal Collapse Koala 2": LocData(0x114, "Dam Busted - CC"), # no reqs
    "Dam Busted Koala 1": LocData(0x115, "Dam Busted"), # Zappy
    "Dam Busted Koala 2": LocData(0x116, "Dam Busted"), # Delayed glide off of bouncy shroom
    "Tidal Trouble Koala 1": LocData(0x117, "Three Hour Tour - TT"), # Flame
    "Tidal Trouble Koala 2": LocData(0x118, "Three Hour Tour - TT"), # Behind Cacti in cave hidden underwater
    "Ghastly Ghost Ships Koala 1": LocData(0x119, "Three Hour Tour - GGS"), # timed target
    "Ghastly Ghost Ships Koala 2": LocData(0x11A, "Three Hour Tour - GGS"), # no reqs
    "Three Hour Tour Koala 1": LocData(0x11B, "Three Hour Tour"), # Underwater near start
    "Three Hour Tour Koala 2": LocData(0x11C, "Three Hour Tour"), # Underwater near Keith
    "Dag Nab 'Em Koala 1": LocData(0x11D, "Black Stump BBQ - DNE"), # elevated platforms near sheep
    "Dag Nab 'Em Koala 2": LocData(0x11E, "Black Stump BBQ - DNE"), # Infra at end
    "Jack Squats Koala 1": LocData(0x11F, "Black Stump BBQ - JS"), # Underwater near start
    "Jack Squats Koala 2": LocData(0x120, "Black Stump BBQ - JS"), # Drop down after Berry 1
    "Black Stump BBQ Koala 1": LocData(0x121, "Black Stump BBQ"), # fan platform
    "Black Stump BBQ Koala 2": LocData(0x122, "Black Stump BBQ"), # Spy eggs after Berry 3
    "Treasure of the Parrot's Beard Koala 1": LocData(0x123, "Raise the TYtanic - TPB"), # above parrotbeard
    "Treasure of the Parrot's Beard Koala 2": LocData(0x124, "Raise the TYtanic - TPB"), # cliffs above Ty the Whale
    "Voyage to the Bottom of the Water Koala 1": LocData(0x125, "Raise the TYtanic - VBW"),
    "Voyage to the Bottom of the Water Koala 2": LocData(0x126, "Raise the TYtanic - VBW"),
    "Raise the TYtanic Koala 1": LocData(0x127, "Raise the TYtanic"), # Underwater bottom right hidden by seagrass
    "Raise the TYtanic Koala 2": LocData(0x128, "Raise the TYtanic"), # Fan platform final area
    "DIVE HARD Koala 1": LocData(0x129, "Ranger in Danger - DH"), # Underwater cave near start
    "DIVE HARD Koala 2": LocData(0x12A, "Ranger in Danger - DH"), # Up from last torch for berry 2
    "Dennis' Dilemma Koala 1": LocData(0x12B, "Ranger in Danger - DD"), # infra above first water wheel
    "Dennis' Dilemma Koala 2": LocData(0x12C, "Ranger in Danger - DD"), # Frosty up and left after 2nd freeze log
    "Ranger in Danger Koala 1": LocData(0x12D, "Ranger in Danger"), # down and left from first dunny, hit buttons above
    "Ranger in Danger Koala 2": LocData(0x12E, "Ranger in Danger"), # Infra up after 2nd rock run"Surf's Down Berry 1": LocData(0x90, "That Lost Island - SD"), #
    "Surf's Down Koala 1": LocData(0x12F, "That Lost Island - SD"), # Up Right from Time Attack - Timed Button
    "Surf's Down Koala 2": LocData(0x130, "That Lost Island - SD"), # Infra Platforming left of Rex
    "Mmmm... Lamingtons Koala 1": LocData(0x131, "That Lost Island - ML"), # Bottom of water at start
    "Mmmm... Lamingtons Koala 2": LocData(0x132, "That Lost Island - ML"), # Infra above water between Generators 2 and 3
    "That Lost Island Koala 1": LocData(0x133, "That Lost Island"), # Bottom left of water after Generator 1
    "That Lost Island Koala 2": LocData(0x134, "That Lost Island"), # Fan Platform above Generator 3
    "Lunchabiblies Koala 1": LocData(0x135, "Crabby Convoys - LB"), # Infra Frosty above Lunch Delivery
    "Lunchabiblies Koala 2": LocData(0x136, "Crabby Convoys - LB"), # Infra hit the 3 buttons
    "DIVE HARDER Koala 1": LocData(0x137, "Crabby Convoys - DH"), # Bouncy Shrooms above first dunny
    "DIVE HARDER Koala 2": LocData(0x138, "Crabby Convoys - DH"), # Disappearing platforms after Generator 5
    "Crabby Convoys Koala 1": LocData(0x139, "Crabby Convoys"), # Up from first crabdozer
    "Crabby Convoys Koala 2": LocData(0x13A, "Crabby Convoys"), # Infra after crabdozer 3
    "Nano-Proof Fence Koala 1": LocData(0x13B, "Fair Dinkum Drinking - NPF"), # Infra above start
    "Nano-Proof Fence Koala 2": LocData(0x13C, "Fair Dinkum Drinking - NPF"), # Light all 4 torches to open gate by Shazza
    "Sheepskin Sweatshop Koala 1": LocData(0x13D, "Fair Dinkum Drinking - SS"), # Above first sheep
    "Sheepskin Sweatshop Koala 2": LocData(0x13E, "Fair Dinkum Drinking - SS"), # Flame above lenny's danger zone
    "Fair Dinkum Drinking Koala 1": LocData(0x13F, "Fair Dinkum Drinking"), # Infra Cave below 2nd pipe
    "Fair Dinkum Drinking Koala 2": LocData(0x140, "Fair Dinkum Drinking"), # above 3rd pipe


}

thunder_egg_dict = {
    "Up the Magpies - Boonie's Trophy": LocData(0x200, "127 Minutes - UtM - Ice Wall"),
    "Lenny's List - Lenny's Package": LocData(0x201, "127 Minutes -  LL"),
    "127 Minutes - Dennis Escort": LocData(0x202, "127 Minutes"), # Flame
    "Six Skink Shrink Sink - Polluting Skinks": LocData(0x203, "Dam Busted - SSSS"),
    "Crocolossal Collapse - Escort Ranger Ken": LocData(0x204, "Dam Busted - CC"), # Flame
    "Dam Busted OoB Thunder Egg 1": LocData(0x205, "Dam Busted"), # OoB at start
    "Dam Busted OoB Thunder Egg 2": LocData(0x206, "Dam Busted"), # OoB at start
    "Dam Busted OoB Thunder Egg 3": LocData(0x207, "Dam Busted"), # OoB at start
    "Dam Busted - Plug the Dam": LocData(0x208, "Dam Busted"),
    "Tidal Trouble - Tidal Turbines": LocData(0x209, "Three Hour Tour - TT"),
    "Ghastly Ghost Ships - Ghost Ships": LocData(0x20A, "Three Hour Tour - GGS"), # Infra
    "Three Hour Tour - Rescue Keith": LocData(0x20B, "Three Hour Tour"),
    "Dag Nab 'Em - Bruno's Sheep": LocData(0x20C, "Black Stump BBQ - DNE"),
    "Jack Squats - Save the Thunder Egg Museum": LocData(0x20D, "Black Stump BBQ - JS"),
    "Black Stump BBQ - Save the Lab": LocData(0x20E, "Black Stump BBQ"),
    "Treasure of the Parrot's Beard - Parrotbeard's Treasure": LocData(0x20F, "Raise the TYtanic - TPB"),
    "Voyage to the Bottom of the Water - Sea Dragon Kids": LocData(0x210, "Raise the TYtanic - VBW"),
    "Raise the TYtanic - Save the Ship": LocData(0x211, "Raise the TYtanic"),
    "DIVE HARD - DIVE HARD!": LocData(0x212, "Ranger in Danger - DH"),
    "Dennis' Dilemma - Wacky Water Wheels": LocData(0x213, "Ranger in Danger - DD"),
    "Ranger in Danger - Save Ken": LocData(0x214, "Ranger in Danger"),
    "Surf's Down - Rexy's Surfboard": LocData(0x215, "That Lost Island - SD"),
    "Mmmm... Lamingtons - Elle's Coconuts": LocData(0x216, "That Lost Island - ML"),
    "That Lost Island - SOS": LocData(0x217, "That Lost Island"), # Zappy
    "Lunchabiblies - Food Delivery": LocData(0x218, "Crabby Convoys - LB"),
    "DIVE HARDER - DIVE HARDER!": LocData(0x219, "Crabby Convoys - DH"),
    "Crabby Convoys - Save the Rainforests!": LocData(0x21A, "Crabby Convoys"),
    "Nano-Proof Fence - Fence Patches": LocData(0x21B, "Fair Dinkum Drinking - NPF"), #Frosty
    "Sheepskin Sweatshop - Bruno's Sheep 2: Electric Boogaloo": LocData(0x21C, "Fair Dinkum Drinking - SS"),
    "Fair Dinkum Drinking - Thirsty Thylacines": LocData(0x21D, "Fair Dinkum Drinking"),
    "127 Minutes - Berry Completion": LocData(0x21E, "127 Minutes - All"),
    "127 Minutes - Koala Completion": LocData(0x21F, "127 Minutes - All"),
    "Dam Busted - Berry Completion": LocData(0x220, "Dam Busted - All"),
    "Dam Busted - Koala Completion": LocData(0x221, "Dam Busted - All"),
    "Three Hour Tour - Berry Completion": LocData(0x222, "Three Hour Tour - All"),
    "Three Hour Tour - Koala Completion": LocData(0x223, "Three Hour Tour - All"),
    "Black Stump BBQ - Berry Completion": LocData(0x224, "Black Stump BBQ - All"),
    "Black Stump BBQ - Koala Completion": LocData(0x225, "Black Stump BBQ - All"),
    "Raise the TYtanic - Berry Completion": LocData(0x226, "Raise the TYtanic - All"),
    "Raise the TYtanic - Koala Completion": LocData(0x227, "Raise the TYtanic - All"),
    "Ranger in Danger - Berry Completion": LocData(0x228, "Ranger in Danger - All"),
    "Ranger in Danger - Koala Completion": LocData(0x229, "Ranger in Danger - All"),
    "That Lost Island - Berry Completion": LocData(0x22A, "That Lost Island - All"),
    "That Lost Island - Koala Completion": LocData(0x22B, "That Lost Island - All"),
    "Crabby Convoys - Berry Completion": LocData(0x22C, "Crabby Convoys - All"),
    "Crabby Convoys - Koala Completion": LocData(0x22D, "Crabby Convoys - All"),
    "Fair Dinkum Drinking - Berry Completion": LocData(0x22E, "Fair Dinkum Drinking - All"),
    "Fair Dinkum Drinking - Koala Completion": LocData(0x22F, "Fair Dinkum Drinking - All"),
}



ty4_location_table = {
    **level_completion_dict,
    **rang_shop_dict,
    **costume_shop_dict,
    **minigame_dict,
    **berry_dict,
    **koala_dict,
    **thunder_egg_dict,
}
