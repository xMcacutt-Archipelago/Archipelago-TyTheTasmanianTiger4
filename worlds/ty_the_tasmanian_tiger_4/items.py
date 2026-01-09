from worlds.ty_the_tasmanian_tiger_4 import *

from BaseClasses import Item, ItemClassification, MultiWorld, Location


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


def create_single(name: str, world: Ty4World, item_class: ItemClassification = None) -> None:
    classification = ty4_item_table[name].classification if item_class is None else item_class
    world.itempool.append(Ty4Item(name, classification, ty4_item_table[name].code, world.player))


def create_multiple(name: str, amount: int, world: Ty4World, item_class: ItemClassification = None):
    for i in range(amount):
        create_single(name, world, item_class)

level_names = [
"127 Minutes - Up the Magpies",
"127 Minutes - Lenny's List",
"127 Minutes",
"Dam Busted - Six Skink Shrink Sink",
"Dam Busted -Crocolossal Collapse",
"Dam Busted",
"Three Hour Tour -Tidal Trouble",
"Three Hour Tour -Ghastly Ghost Ships",
"Three Hour Tour",
"Black Stump BBQ - Dag Nab 'Em",
"Black Stump BBQ - Jack Squats",
"Black Stump BBQ",
"Raise the TYtanic - Treasure of the Parrot's Beard",
"Raise the TYtanic - Voyage to the Bottom of the Water",
"Raise the TYtanic",
"Ranger in Danger - DIVE HARD",
"Ranger in Danger - Dennis' Dilemma",
"Ranger in Danger",
"That Lost Island - Surf's Down",
"That Lost Island - Mmmm... Lamingtons",
"That Lost Island",
"Crabby Convoys - Lunchabiblies",
"Crabby Convoys - DIVE HARDER",
"Crabby Convoys",
"Fair Dinkum Drinking - Nano-Proof Fence",
"Fair Dinkum Drinking - Sheepskin Sweatshop",
"Fair Dinkum Drinking",
]

hub_level_names = [
"127 Minutes",
"Dam Busted",
"Three Hour Tour",
"Black Stump BBQ",
"Raise the TYtanic",
"Ranger in Danger",
"That Lost Island",
"Fair Dinkum Drinking",
]


def create_items(world: Ty4World):
    total_location_count: int = len(world.multiworld.get_unfilled_locations(world.player))

    starting_level = level_names[world.random.randint(0, len(level_names) - 1)]
    world.push_precollected(world.create_item(f"{starting_level} Unlock"))

    for level_name in level_names:
        if level_name != starting_level:
            create_single(f"{level_name} Unlock", world)



    # Rangs
    if options.progressive_elementals:
        create_multiple("Progressive Rang", 4, world)
    else:
        create_single("Blazerang", world)
        create_single("Blizzarang", world)
        create_single("Plasmarang", world)
        create_single("Infinirang", world)
    create_single("Cryptorang", world)
    create_single("Deadlyrang", world)
    create_single("Disruptorang", world)
    create_single("Doomerang", world)
    create_single("Chaosrang", world)
    create_single("Hyperang", world)


    # Junk
    remaining_locations: int = total_location_count - len(world.multiworld.worlds[world.player].itempool)
    trap_count: int = round(remaining_locations * options.trap_fill_percentage / 100)
    junk_count: int = remaining_locations - trap_count
    junk = get_junk_item_names(world.random, junk_count)
    for name in junk:
        create_single(name, world)
    traps = get_trap_item_names(world.multiworld.worlds[world.player], world.random, trap_count)
    for name in traps:
        create_single(name, world)
    world.itempool += world.multiworld.worlds[world.player].itempool



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
    "Progressive Level Unlock": ItemData(0x10, ItemClassification.progression),
    "Level - 127 Minutes - Up the Magpies Unlock": ItemData(0x11, ItemClassification.progression),
    "Level - 127 Minutes - Lenny's  Unlock": ItemData(0x12, ItemClassification.progression),
    "Level - 127 Minutes Unlock": ItemData(0x13, ItemClassification.progression),
    "Level - Dam Busted - Six Skink Shrink Sink Unlock": ItemData(0x14, ItemClassification.progression),
    "Level - Dam Busted - Crocolossal Collapse Unlock": ItemData(0x15, ItemClassification.progression),
    "Level - Dam Busted Unlock": ItemData(0x16, ItemClassification.progression),
    "Level - Three Hour Tour - Tidal Trouble Unlock": ItemData(0x17, ItemClassification.progression),
    "Level - Three Hour Tour - Ghastly Ghost Ships Unlock": ItemData(0x18, ItemClassification.progression),
    "Level - Three Hour Tour Unlock": ItemData(0x19, ItemClassification.progression),
    "Level - Fluffy's Follies": ItemData(0x1A, ItemClassification.progression),
    "Level - Black Stump BBQ - Dag Nab 'Em Unlock": ItemData(0x1B, ItemClassification.progression),
    "Level - Black Stump BBQ - Jack Squats Unlock": ItemData(0x1C, ItemClassification.progression),
    "Level - Black Stump BBQ Unlock": ItemData(0x1D, ItemClassification.progression),
    "Level - Raise the TYtanic - Treasure of the Parrot's Beard Unlock": ItemData(0x1E, ItemClassification.progression),
    "Level - Raise the TYtanic - Voyage to the Bottom of the Water Unlock": ItemData(0x1F, ItemClassification.progression),
    "Level - Raise the TYtanic Unlock": ItemData(0x20, ItemClassification.progression),
    "Level - Ranger in Danger - DIVE HARD Unlock": ItemData(0x21, ItemClassification.progression),
    "Level - Ranger in Danger - Dennis' Dilemma Unlock": ItemData(0x22, ItemClassification.progression),
    "Level - Ranger in Danger Unlock": ItemData(0x23, ItemClassification.progression),
    "Level - Sly Spy With My Little Eye": ItemData(0x24, ItemClassification.progression),
    "Level - That Lost Island - Surf's Down Unlock": ItemData(0x25, ItemClassification.progression),
    "Level - That Lost Island - Mmmm... Lamingtons Unlock": ItemData(0x26, ItemClassification.progression),
    "Level - That Lost Island Unlock": ItemData(0x27, ItemClassification.progression),
    "Level - Crabby Convoys - Lunchabiblies Unlock": ItemData(0x28, ItemClassification.progression),
    "Level - Crabby Convoys - DIVE HARDER Unlock": ItemData(0x29, ItemClassification.progression),
    "Level - Crabby Convoys Unlock": ItemData(0x2A, ItemClassification.progression),
    "Level - Fair Dinkum Drinking - Nano-Proof Fence Unlock": ItemData(0x2B, ItemClassification.progression),
    "Level - Fair Dinkum Drinking - Sheepskin Sweatshop Unlock": ItemData(0x2C, ItemClassification.progression),
    "Level - Fair Dinkum Drinking Unlock": ItemData(0x2D, ItemClassification.progression),
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
