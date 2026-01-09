import math
from typing import Dict, Optional


from BaseClasses import Item, ItemClassification, MultiWorld, Location
from worlds.ty_the_tasmanian_tiger_4.options import Ty4Options


class Ty4Item(Item):
    game: str = "Ty the Tasmanian Tiger 4"


def get_junk_item_names(rand, k: int) -> str:
    junk = rand.choices(
        list(junk_weights.keys()),
        weights=list(junk_weights.values()),
        k=k)
    return junk


def get_trap_item_names(world, rand, k: int) -> str:
    traps = rand.choices(
        list(world.trap_weights.keys()),
        weights=list(world.trap_weights.values()),
        k=k)
    return traps


def create_single(name: str, world: MultiWorld, player: int, item_class: ItemClassification = None) -> None:
    classification = ty4_item_table[name].classification if item_class is None else item_class
    world.worlds[player].itempool.append(Ty4Item(name, classification, ty4_item_table[name].code, player))


def create_multiple(name: str, amount: int, world: MultiWorld, player: int, item_class: ItemClassification = None):
    for i in range(amount):
        create_single(name, world, player, item_class)


def create_items(world: MultiWorld, options: Ty4Options, player: int):
    total_location_count: int = len(world.get_unfilled_locations(player))

    # Generic
    create_multiple("Fire Thunder Egg", 4, world, player)

    # Bilbies
    create_multiple("Bilby - Two Up", 5, world, player)
    create_multiple("Bilby - Walk in the Park", 5, world, player)
    create_multiple("Bilby - Ship Rex", 5, world, player)
    create_multiple("Bilby - Bridge on the River Ty", 5, world, player)
    create_multiple("Bilby - Snow Worries", 5, world, player)
    create_multiple("Bilby - Outback Safari", 5, world, player)
    create_multiple("Bilby - Lyre, Lyre Pants on Fire", 5, world, player)
    create_multiple("Bilby - Beyond the Black Stump", 5, world, player)
    create_multiple("Bilby - Rex Marks the Spot", 5, world, player)


    # Attributes
    if options.progressive_elementals:
        create_multiple("Progressive Rang", 8, world, player)
    else:
        create_single("Second Rang", world, player)
        world.early_items[player]["Second Rang"] = 1
        create_single("Swim", world, player)
        create_single("Aquarang", world, player)
        create_single("Dive", world, player)
        create_single("Flamerang", world, player)
        create_single("Frostyrang", world, player)
        create_single("Zappyrang", world, player)
        create_single("Doomerang", world, player)
    create_single("Zoomerang", world, player)
    create_single("Multirang", world, player)
    create_single("Infrarang", world, player)
    create_single("Megarang", world, player)
    create_single("Kaboomarang", world, player)
    create_single("Chronorang", world, player)


    # Junk
    remaining_locations: int = total_location_count - len(world.worlds[player].itempool)
    trap_count: int = round(remaining_locations * options.trap_fill_percentage / 100)
    junk_count: int = remaining_locations - trap_count
    junk = get_junk_item_names(world.random, junk_count)
    for name in junk:
        create_single(name, world, player)
    traps = get_trap_item_names(world.worlds[player], world.random, trap_count)
    for name in traps:
        create_single(name, world, player)
    world.itempool += world.worlds[player].itempool


def place_locked_items(world: MultiWorld, player: int):
    classification = ItemClassification.progression_skip_balancing
    a1_bilby_loc: Location = world.get_location("Two Up - Bilby Completion", player)
    a1_bilby_thegg: Ty4Item = Ty4Item("Fire Thunder Egg", classification, 0x8750000, player)
    a1_bilby_loc.place_locked_item(a1_bilby_thegg)
    a2_bilby_loc: Location = world.get_location("WitP - Bilby Completion", player)
    a2_bilby_thegg: Ty4Item = Ty4Item("Fire Thunder Egg", classification, 0x8750000, player)
    a2_bilby_loc.place_locked_item(a2_bilby_thegg)
    a3_bilby_loc: Location = world.get_location("Ship Rex - Bilby Completion", player)
    a3_bilby_thegg: Ty4Item = Ty4Item("Fire Thunder Egg", classification, 0x8750000, player)
    a3_bilby_loc.place_locked_item(a3_bilby_thegg)
    b1_bilby_loc: Location = world.get_location("BotRT - Bilby Completion", player)
    b1_bilby_thegg: Ty4Item = Ty4Item("Ice Thunder Egg", classification, 0x8750001, player)
    b1_bilby_loc.place_locked_item(b1_bilby_thegg)
    b2_bilby_loc: Location = world.get_location("Snow Worries - Bilby Completion", player)
    b2_bilby_thegg: Ty4Item = Ty4Item("Ice Thunder Egg", classification, 0x8750001, player)
    b2_bilby_loc.place_locked_item(b2_bilby_thegg)
    b3_bilby_loc: Location = world.get_location("Outback Safari - Bilby Completion", player)
    b3_bilby_thegg: Ty4Item = Ty4Item("Ice Thunder Egg", classification, 0x8750001, player)
    b3_bilby_loc.place_locked_item(b3_bilby_thegg)
    c1_bilby_loc: Location = world.get_location("LLPoF - Bilby Completion", player)
    c1_bilby_thegg: Ty4Item = Ty4Item("Air Thunder Egg", classification, 0x8750002, player)
    c1_bilby_loc.place_locked_item(c1_bilby_thegg)
    c2_bilby_loc: Location = world.get_location("BtBS - Bilby Completion", player)
    c2_bilby_thegg: Ty4Item = Ty4Item("Air Thunder Egg", classification, 0x8750002, player)
    c2_bilby_loc.place_locked_item(c2_bilby_thegg)
    c3_bilby_loc: Location = world.get_location("RMtS - Bilby Completion", player)
    c3_bilby_thegg: Ty4Item = Ty4Item("Air Thunder Egg", classification, 0x8750002, player)
    c3_bilby_loc.place_locked_item(c3_bilby_thegg)


class ItemData:
    def __init__(self, code: Optional[int], classification: Optional[ItemClassification]):
        self.code = code
        self.classification = classification


ty4_item_table: Dict[str, ItemData] = {

    # Rangs
    "Blazerang": ItemData(0x1, ItemClassification.progression),
    "Blizzarang": ItemData(0x2, ItemClassification.progression),
    "Doomerang": ItemData(0x3, ItemClassification.progression),
    "Plasmarang": ItemData(0x4, ItemClassification.progression),
    "Infinirang": ItemData(0x5, ItemClassification.useful),
    "Cryptorang": ItemData(0x6, ItemClassification.progression),
    "Deadlyrang": ItemData(0x7, ItemClassification.useful),
    "Disruptorang": ItemData(0x8, ItemClassification.progression),
    "Chaosrang": ItemData(0x9, ItemClassification.useful),
    "Hyperang": ItemData(0xA, ItemClassification.useful),

    # Levels
    "Progressive Level": ItemData(0x10, ItemClassification.progression),
    "Level - 127 Minutes - Up the Magpies": ItemData(0x11, ItemClassification.progression),
    "Level - 127 Minutes - Lenny's List": ItemData(0x12, ItemClassification.progression),
    "Level - 127 Minutes": ItemData(0x13, ItemClassification.progression),
    "Level - Dam Busted - Six Skink Shrink Sink": ItemData(0x14, ItemClassification.progression),
    "Level - Dam Busted - Crocolossal Collapse": ItemData(0x15, ItemClassification.progression),
    "Level - Dam Busted": ItemData(0x16, ItemClassification.progression),
    "Level - Three Hour Tour - Tidal Trouble": ItemData(0x17, ItemClassification.progression),
    "Level - Three Hour Tour - Ghastly Ghost Ships": ItemData(0x18, ItemClassification.progression),
    "Level - Three Hour Tour": ItemData(0x19, ItemClassification.progression),
    "Level - Fluffy's Follies": ItemData(0x1A, ItemClassification.progression),
    "Level - Black Stump BBQ - Dag Nab 'Em": ItemData(0x1B, ItemClassification.progression),
    "Level - Black Stump BBQ - Jack Squats": ItemData(0x1C, ItemClassification.progression),
    "Level - Black Stump BBQ": ItemData(0x1D, ItemClassification.progression),
    "Level - Raise the TYtanic - Treasure of the Parrot's Beard": ItemData(0x1E, ItemClassification.progression),
    "Level - Raise the TYtanic - Voyage to the Bottom of the Water": ItemData(0x1F, ItemClassification.progression),
    "Level - Raise the TYtanic": ItemData(0x20, ItemClassification.progression),
    "Level - Ranger in Danger - DIVE HARD": ItemData(0x21, ItemClassification.progression),
    "Level - Ranger in Danger - Dennis' Dilemma": ItemData(0x22, ItemClassification.progression),
    "Level - Ranger in Danger": ItemData(0x23, ItemClassification.progression),
    "Level - Sly Spy With My Little Eye": ItemData(0x24, ItemClassification.progression),
    "Level - That Lost Island - Surf's Down": ItemData(0x25, ItemClassification.progression),
    "Level - That Lost Island - Mmmm... Lamingtons": ItemData(0x26, ItemClassification.progression),
    "Level - That Lost Island": ItemData(0x27, ItemClassification.progression),
    "Level - Crabby Convoys - Lunchabiblies": ItemData(0x28, ItemClassification.progression),
    "Level - Crabby Convoys - DIVE HARDER": ItemData(0x29, ItemClassification.progression),
    "Level - Crabby Convoys": ItemData(0x2A, ItemClassification.progression),
    "Level - Fair Dinkum Drinking - Nano-Proof Fence": ItemData(0x2B, ItemClassification.progression),
    "Level - Fair Dinkum Drinking - Sheepskin Sweatshop": ItemData(0x2C, ItemClassification.progression),
    "Level - Fair Dinkum Drinking": ItemData(0x2D, ItemClassification.progression),
    "Level - As TY Goes By": ItemData(0x2E, ItemClassification.progression),

    # Junk
    "Quarter Pie": ItemData(0x100, ItemClassification.filler),
    "Full Pie": ItemData(0x101, ItemClassification.filler),
    "500 Opals": ItemData(0x102, ItemClassification.filler),

    # Trap
    "Exit Trap": ItemData(0x103, ItemClassification.trap),
}


junk_weights = {
    "Quarter Pie": 20,
    "Full Pie": 10,
    "500 Opals": 20,
}
