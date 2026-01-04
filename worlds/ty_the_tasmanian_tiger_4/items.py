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
    "Blazerang": ItemData(0x8750010, ItemClassification.progression),
    "Blizzarang": ItemData(0x8750011, ItemClassification.progression),
    "Doomerang": ItemData(0x8750012, ItemClassification.progression),
    "Plasmarang": ItemData(0x8750013, ItemClassification.progression),
    "Infinirang": ItemData(0x8750014, ItemClassification.useful),
    "Cryptorang": ItemData(0x8750015, ItemClassification.progression),
    "Deadlyrang": ItemData(0x8750016, ItemClassification.useful),
    "Disruptorang": ItemData(0x8750017, ItemClassification.progression),
    "Chaosrang": ItemData(0x8750018, ItemClassification.useful),
    "Hyperang": ItemData(0x8750019, ItemClassification.useful),

    # Levels
    "Progressive Level": ItemData(0x8750071, ItemClassification.progression),
    "Level - 127 Minutes": ItemData(0x8750030, ItemClassification.progression),
    "Level - Dam Busted": ItemData(0x8750031, ItemClassification.progression),
    "Level - Three Hour Tour": ItemData(0x8750032, ItemClassification.progression),
    "Level - Fluffy's Follies": ItemData(0x8750033, ItemClassification.progression),
    "Level - Black Stump BBQ": ItemData(0x8750034, ItemClassification.progression),
    "Level - Raise the TYtanic": ItemData(0x8750035, ItemClassification.progression),
    "Level - Ranger in Danger": ItemData(0x8750036, ItemClassification.progression),
    "Level - Sly SPy With My Little Eye": ItemData(0x8750037, ItemClassification.progression),
    "Level - That Lost Island": ItemData(0x8750038, ItemClassification.progression),
    "Level - Crabby Convoys": ItemData(0x8750039, ItemClassification.progression),
    "Level - Fair Dinkum Drinking": ItemData(0x875003A, ItemClassification.progression),
    "Level - As TY Goes By": ItemData(0x875003B, ItemClassification.progression),

    # Junk
    "Quarter Pie": ItemData(0x8750084, ItemClassification.filler),
    "Full Pie": ItemData(0x8750085, ItemClassification.filler),

    # Trap
    "Exit Trap": ItemData(0x8750094, ItemClassification.trap),
}


junk_weights = {
    "Quarter Pie": 20,
    "Full Pie": 10,
}
