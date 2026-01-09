from enum import Enum

from BaseClasses import MultiWorld, Region, Entrance
from worlds.ty_the_tasmanian_tiger_4 import *
from typing import List, Dict
from .items import level_names, hub_level_names
from worlds.ty_the_tasmanian_tiger_4.locations import create_locations




class Ty4Region(Region):
    subregions: List[Region] = []


def connect_regions(world: Ty4World, from_name: str, to_name: str, entrance_name: str) -> Entrance:
    entrance_region = world.multiworld.get_region(from_name, world.player)
    exit_region = world.multiworld.get_region(to_name, world.player)
    return entrance_region.connect(exit_region, entrance_name)


def create_region(world: Ty4World, name: str):
    reg = Region(name, world.player, world.multiworld)
    create_locations(world, reg)
    world.multiworld.regions.append(reg)


def create_regions(world: Ty4World, reg: Region):
    create_region(world, "Menu")
    create_region(world, "Prologue")
    create_region(world, "Fluffy's Follies")
    create_region(world, "Sly Spy with My Little Eye")
    create_region(world, "As TY Goes By...")
    create_region(world, "Rang Shop")
    create_region(world, "Costume Shop")
    create_region(world, "127 Minutes - Up the Magpies - Ice Wall")
    for level_name in level_names:
        create_region(world, f"{level_name}")
    for hub_level_name in hub_level_names:
        create_region(world, f"{hub_level_name} - All")


def connect_all_regions(world: Ty4World):
    connect_regions(world, "Menu",
                    "Rang Shop", "Menu -> Rang Shop")
    connect_regions(world, "Menu",
                    "Costume Shop", "Menu -> Costume Shop")
    connect_regions(world, "Menu",
                    "Prologue", "Menu -> Prologue")
    for level_name in level_names:
        connect_regions(world, "Menu", level_name, f"Menu -> {level_name}")
    connect_regions(world, "127 Minutes - Up the Magpies",
                    "127 Minutes - Up the Magpies - Ice Wall", "Up the Magpies Ice Wall")

