from enum import Enum

from BaseClasses import MultiWorld, Region, Entrance
from worlds.ty_the_tasmanian_tiger_4.options import Ty4Options
from worlds.ty_the_tasmanian_tiger_4.locations import create_locations
from typing import List, Dict




class Ty4Region(Region):
    subregions: List[Region] = []


def connect_regions(world: MultiWorld, player: int, from_name: str, to_name: str, entrance_name: str) -> Entrance:
    entrance_region = world.get_region(from_name, player)
    exit_region = world.get_region(to_name, player)
    return entrance_region.connect(exit_region, entrance_name)


def create_region(world: MultiWorld, player: int, options: Ty4Options, name: str):
    reg = Region(name, player, world)
    create_locations(player, options, reg)
    world.regions.append(reg)


def create_regions(world: MultiWorld, options: Ty4Options, player: int):
    create_region(world, player, options, "Menu")
    create_region(world, player, options, "Prologue")
    create_region(world, player, options, "127 Minutes")
    create_region(world, player, options, "127 Minutes - UtM")
    create_region(world, player, options, "127 Minutes - LL")
    create_region(world, player, options, "127 Minutes - All")
    create_region(world, player, options, "Dam Busted")
    create_region(world, player, options, "Dam Busted - SSSS")
    create_region(world, player, options, "Dam Busted - CC")
    create_region(world, player, options, "Dam Busted - All")
    create_region(world, player, options, "Three Hour Tour")
    create_region(world, player, options, "Three Hour Tour - TT")
    create_region(world, player, options, "Three Hour Tour - GGS")
    create_region(world, player, options, "Three Hour Tour - All")
    create_region(world, player, options, "Fluffy's Follies")
    create_region(world, player, options, "Black Stump BBQ")
    create_region(world, player, options, "Black Stump BBQ - DNE")
    create_region(world, player, options, "Black Stump BBQ - JS")
    create_region(world, player, options, "Black Stump BBQ - All")
    create_region(world, player, options, "Raise the TYtanic")
    create_region(world, player, options, "Raise the TYtanic - TPB")
    create_region(world, player, options, "Raise the TYtanic - VBW")
    create_region(world, player, options, "Raise the TYtanic - All")
    create_region(world, player, options, "Ranger in Danger")
    create_region(world, player, options, "Ranger in Danger - DH")
    create_region(world, player, options, "Ranger in Danger - DD")
    create_region(world, player, options, "Ranger in Danger - All")
    create_region(world, player, options, "Sly Spy With My Little Eye")
    create_region(world, player, options, "That Lost Island")
    create_region(world, player, options, "That Lost Island - SD")
    create_region(world, player, options, "That Lost Island - ML")
    create_region(world, player, options, "That Lost Island - All")
    create_region(world, player, options, "Crabby Convoys")
    create_region(world, player, options, "Crabby Convoys - LB")
    create_region(world, player, options, "Crabby Convoys - DH")
    create_region(world, player, options, "Crabby Convoys - All")
    create_region(world, player, options, "Fair Dinkum Drinking")
    create_region(world, player, options, "Fair Dinkum Drinking - NPF")
    create_region(world, player, options, "Fair Dinkum Drinking - SS")
    create_region(world, player, options, "Fair Dinkum Drinking - All")
    create_region(world, player, options, "As TY Goes By...")
    create_region(world, player, options, "As TY Goes By... - ABW")
    create_region(world, player, options, "Rang Shop")
    create_region(world, player, options, "Costume Shop")


def connect_all_regions(world: MultiWorld, player: int, options: Ty4Options, portal_map: List[int]):
    if options.level_shuffle and not hasattr(world, "re_gen_passthrough"):
        world.random.shuffle(portal_map)
    connect_regions(world, player, "Menu",
                    "Rainbow Cliffs", "Menu -> Z1")
    connect_regions(world, player, "Rainbow Cliffs",
                    "Rainbow Cliffs - PF", "Z1 - PF")
    connect_regions(world, player, "Rainbow Cliffs",
                    "Bli Bli Station", "Z1 -> A Zone")
    connect_regions(world, player, "Bli Bli Station",
                    "Bli Bli Station Gate", "A Zone Gate")
    connect_regions(world, player, "Bli Bli Station Gate",
                    "Bli Bli Station Gate - PF", "A Zone Gate - PF")
    connect_regions(world, player, "Rainbow Cliffs",
                    "Pippy Beach", "Z1 -> B Zone")
    connect_regions(world, player, "Pippy Beach",
                    "Pippy Beach - PF", "B Zone - PF")
    connect_regions(world, player, "Rainbow Cliffs",
                    "Lake Burril", "Z1 -> C Zone")
    connect_regions(world, player, "Rainbow Cliffs",
                    "Final Gauntlet", "Z1 -> E Zone")
    connect_regions(world, player, "Final Gauntlet",
                    "Final Gauntlet - PF", "E Zone - PF")
    connect_regions(world, player, "Final Gauntlet",
                    "Cass' Pass", "E1 Portal")
    connect_regions(world, player, "Cass' Pass",
                    "Cass' Crest", "E1 -> D2")
    connect_regions(world, player, "Cass' Crest",
                    "Final Battle", "D2 -> E4")
    connect_regions(world, player, "Two Up",
                    "Two Up - PF", "Two Up - PF")
    connect_regions(world, player, "Two Up",
                    "Two Up - Upper Area", "Two Up - Upper Area")
    connect_regions(world, player, "Two Up - Upper Area",
                    "Two Up - Upper Area - PF", "Two Up - Upper Area - PF")
    connect_regions(world, player, "Two Up",
                    "Two Up - End Area", "Two Up - End Area")
    connect_regions(world, player, "Walk in the Park",
                    "Walk in the Park - PF", "Walk in the Park - PF")
    connect_regions(world, player, "Ship Rex",
                    "Ship Rex - PF", "Ship Rex - PF")
    connect_regions(world, player, "Ship Rex",
                    "Ship Rex - Beyond Gate", "Ship Rex - Sea Gate")
    connect_regions(world, player, "Ship Rex - Beyond Gate",
                    "Ship Rex - Beyond Gate - PF", "Ship Rex - Gate - PF")
    connect_regions(world, player, "Bridge on the River Ty",
                    "Bridge on the River Ty - Underwater", "Bridge on the River Ty - Underwater")
    connect_regions(world, player, "Bridge on the River Ty",
                    "Bridge on the River Ty - PF", "Bridge on the River Ty - PF")
    connect_regions(world, player, "Bridge on the River Ty",
                    "Bridge on the River Ty - Beyond Broken Bridge", 
                    "Bridge on the River Ty - Broken Bridge Glide")
    connect_regions(world, player, "Bridge on the River Ty - Beyond Broken Bridge",
                    "Bridge on the River Ty - Beyond Broken Bridge Underwater",
                    "Bridge on the River Ty - Beyond Broken Bridge Underwater")
    connect_regions(world, player, "Bridge on the River Ty - Beyond Broken Bridge",
                    "Bridge on the River Ty - Beyond Broken Bridge - PF", 
                    "Bridge on the River Ty - Broken Bridge - PF")
    connect_regions(world, player, "Snow Worries",
                    "Snow Worries - PF", "Snow Worries - PF")
    connect_regions(world, player, "Snow Worries",
                    "Snow Worries - Underwater", "Snow Worries - Underwater")
    connect_regions(world, player, "Lyre, Lyre Pants on Fire",
                    "Lyre, Lyre Pants on Fire - PF", "Lyre, Lyre Pants on Fire - PF")
    connect_regions(world, player, "Beyond the Black Stump",
                    "Beyond the Black Stump - PF", "Beyond the Black Stump - PF")
    connect_regions(world, player, "Beyond the Black Stump",
                    "Beyond the Black Stump - Upper Area", "Beyond the Black Stump - Upper Area")
    connect_regions(world, player, "Beyond the Black Stump - Upper Area",
                    "Beyond the Black Stump - Glide Behind the Mountain",
                    "Beyond the Black Stump - Glide")
    connect_regions(world, player, "Beyond the Black Stump - Upper Area",
                    "Beyond the Black Stump - Upper Area - PF", 
                    "Beyond the Black Stump - Upper Area - PF")
    connect_regions(world, player, "Rex Marks the Spot",
                    "Rex Marks the Spot - PF", "Rex Marks the Spot, PF")
    connect_regions(world, player, "Rex Marks the Spot",
                    "Rex Marks the Spot - Underwater", "Rex Marks the Spot - Underwater")
    # 0.6.0 ENTRANCE RANDO SUPPORT
    # if options.level_shuffle:
        # disconnect_entrance_for_randomization(ent_a1, 0)
        # disconnect_entrance_for_randomization(ent_a2, 0)
        # disconnect_entrance_for_randomization(ent_a3, 0)
        # disconnect_entrance_for_randomization(ent_b1, 0)
        # disconnect_entrance_for_randomization(ent_b2, 0)
        # disconnect_entrance_for_randomization(ent_b3, 0)
        # disconnect_entrance_for_randomization(ent_c1, 0)
        # disconnect_entrance_for_randomization(ent_c2, 0)
        # disconnect_entrance_for_randomization(ent_c3, 0)
        # target_group_lookup: Dict[int, List[int]] = {0: [0]}
        # return randomize_entrances(world.worlds[player], True, target_group_lookup)
