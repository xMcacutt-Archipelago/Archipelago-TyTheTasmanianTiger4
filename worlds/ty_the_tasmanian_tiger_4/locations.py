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
    create_locations_from_dict(talismans_dict, reg, player)
    # ATTRIBUTES
    create_locations_from_dict(attributes_dict, reg, player)
    # ELEMENTAL RANGS
    create_locations_from_dict(elemental_rangs_dict, reg, player)


level_completion_dict = {
    "Prologue": LocData(0x1, "Prologue"),
    "Up the Magpies": LocData(0x2, "127 Minutes - UtM"),
    "Lenny's List": LocData(0x3, "127 Minutes - LL"),
    "127 Minutes": LocData(0x4, "127 Minutes"),
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
    "DIVE HARD": LocData(0x12, "Ranger in Danger - DH"),
    "Dennis' Dilemma": LocData(0x13, "Ranger in Danger - DD"),
    "Ranger in Danger": LocData(0x14, "Ranger in Danger"),
    "Sly Spy With My Little Eye": LocData(0x15, "Sly Spy With My Little Eye"),
    "Surf's Down": LocData(0x16, "That Lost Island - SD"),
    "Mmmm... Lamingtons": LocData(0x17, "That Lost Island - ML"),
    "That Lost Island": LocData(0x18, "That Lost Island"),
    "Lunchabiblies": LocData(0x19, "Crabby Convoys - LB"), #yes, they misspelled bilbies in their own lunchables pun
    "DIVE HARDER": LocData(0x1A, "Crabby Convoys - DH"),
    "Crabby Convoys": LocData(0x1B, "Crabby Convoys"),
    "Nano-Proof Fence": LocData(0x1C, "Fair Dinkum Drinking - NPF"),
    "Sheepskin Sweatshop": LocData(0x1D, "Fair Dinkum Drinking - SS"),
    "Fair Dinkum Drinking": LocData(0x1E, "Fair Dinkum Drinking"),
    "As TY Goes By...": LocData(0x1F, "As TY Goes By..."),



}

rang_shop_dict = {
    "Hyperang": LocData(0x20, "Rang Shop"),
    "Chaosrang": LocData(0x21, "Rang Shop"),
    "Deadlyrang": LocData(0x22, "Rang Shop"),
    "Cryptorang": LocData(0x23, "Rang Shop"),
    "Disruptorang": LocData(0x24, "Rang Shop"),
    "Doomerang": LocData(0x25, "Rang Shop"),

}

costume_shop_dict = {
    "Ty1": LocData(0x26, "Costume Shop"),
    "Ty2": LocData(0x27, "Costume Shop"),
    "Bunyip Gauntlet": LocData(0x28, "Costume Shop"),
    "Ty5": LocData(0x29, "Costume Shop"),
    "Concept Ty": LocData(0x2A, "Costume Shop"),
    "Retro Ty": LocData(0x2B, "Costume Shop"),
    "Chicken Suit": LocData(0x2C, "Costume Shop"),
    "Secret Agent": LocData(0x2D, "Costume Shop"),
    "Rashy": LocData(0x2E, "Costume Shop"),
    "Snow Warrior": LocData(0x2F, "Costume Shop"),
    "Shazza": LocData(0x30, "Costume Shop"),
    "Shazza the Dingo": LocData(0x31, "Costume Shop"),
    "Sly": LocData(0x32, "Costume Shop"),
    "Sly Cape": LocData(0x33, "Costume Shop"),
    "Shadowy Figure": LocData(0x34, "Costume Shop"),
    "Kid Sly": LocData(0x35, "Costume Shop"),
    "Sly Fiver": LocData(0x36, "Costume Shop"),
    "Naomi": LocData(0x37, "Costume Shop"),
    "Producer Naomi": LocData(0x38, "Costume Shop"),
    "Di": LocData(0x39, "Costume Shop"),
    "Bri": LocData(0x3A, "Costume Shop"),
    "Betty": LocData(0x3B, "Costume Shop"),
    "Ridge": LocData(0x3C, "Costume Shop"),
    "Landscaping Ridge": LocData(0x3D, "Costume Shop"),
    "Brolga": LocData(0x3E, "Costume Shop"),
    "Garden Brolga": LocData(0x3F, "Costume Shop"),
    "Flinders": LocData(0x40, "Costume Shop"),
    "Pippa": LocData(0x41, "Costume Shop"),
    "Doomeranger": LocData(0x42, "Costume Shop"),
    "Frill Disguise": LocData(0x43, "Costume Shop"),
    "Cy X": LocData(0x44, "Costume Shop"),
    "Cyber": LocData(0x45, "Costume Shop"),
    "Skye": LocData(0x46, "Costume Shop"),
    "Bligh": LocData(0x46, "Costume Shop"),


}

picture_frames_dict = {
}

attributes_dict = {
}

talismans_dict = {
}

elemental_rangs_dict = {
}

scales_dict = {
}

opals_dict = {
}

time_attack_challenge_dict = {
}

signposts_dict = {
}


extra_lives_dict = {
}

conditional_items_dict = {
}

ty4_location_table = {
    **level_completion_dict,
    **rang_shop_dict,
    **costume_shop_dict,
    **picture_frames_dict,
    **attributes_dict,
    **talismans_dict,
    **elemental_rangs_dict,
    **scales_dict,
    **signposts_dict,
    **extra_lives_dict,
    **time_attack_challenge_dict,
    **opals_dict,
    **conditional_items_dict
}
