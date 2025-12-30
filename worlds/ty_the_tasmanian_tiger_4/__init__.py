import dataclasses
from typing import List, Dict, Optional, Any
from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Region, Location
from Options import OptionError, PerGameCommonOptions
from worlds.AutoWorld import WebWorld, World

from .items import Ty4Item, ty4_item_table, create_items, ItemData, place_locked_items
from .locations import ty4_location_table, Ty4Location
from .options import Ty4Options, ty4_option_groups
from .regions import create_regions, connect_regions, connect_all_regions
from .rules import set_rules


class Ty4Web(WebWorld):
    theme = "jungle"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Ty the Tasmanian Tiger 4 randomizer connected to an Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["xMcacutt", "Dashieswag92"]
    )

    tutorials = [setup_en]
    option_groups = ty4_option_groups


class Ty4World(World):
    """
    Join TY on an exciting new adventure in the great Aussie Outback.
    Use your wits and boomerangs to find hidden treasures, help the colorful locals,
    and uncover the mysteries of the land Down Under.
    """
    game: str = "Ty the Tasmanian Tiger 4"
    options_dataclass = Ty4Options
    options: Ty4Options
    topology_present = True
    item_name_to_id = {name: item.code for name, item in ty4_item_table.items()}
    location_name_to_id = {name: item.code for name, item in ty4_location_table.items()}
    trap_weights = {}

    web = Ty4Web()

    # UT Stuff Here
    ut_can_gen_without_yaml = True

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.itempool = []

    def fill_slot_data(self) -> id:
        return {
            "ModVersion": "1.0.0",
            "Goal": self.options.goal.value,
            "ProgressiveElementals": self.options.progressive_elementals.value,
            "ProgressiveLevel": self.options.progressive_level.value,
            "LevelUnlockStyle": self.options.level_unlock_style.value,
            "TheggGating": self.options.thegg_gating.value,
            "ReqBosses": self.options.req_bosses.value,
            "PortalMap": self.portal_map,
            "AdvancedLogic": self.options.logic_difficulty.value,
            "DeathLink": self.options.death_link.value,
            "MulTyLink": self.options.mul_ty_link.value,
            "ExtraCog": self.options.extra_cogs.value,
        }

    def generate_early(self) -> None:
        # UT Stuff Here
        self.handle_ut_yamless(None)


        self.trap_weights = {
            "Exit Trap": self.options.exit_trap_weight.value,
        }

    def create_item(self, name: str) -> Item:
        item_info = ty4_item_table[name]
        return Ty4Item(name, item_info.classification, item_info.code, self.player)

    def create_items(self):
        create_items(self.multiworld, self.options, self.player)

    def create_event(self, region_name: str, event_name: str) -> None:
        region: Region = self.multiworld.get_region(region_name, self.player)
        loc: Ty4Location = Ty4Location(self.player, event_name, None, region)
        loc.place_locked_item(Ty4Item(event_name, ItemClassification.progression, None, self.player))
        region.locations.append(loc)

    def create_regions(self):
        create_regions(self.multiworld, self.options, self.player)
        place_locked_items(self.multiworld, self.player)
        self.create_event("Bull's Pen", "Beat Bull")

    def set_rules(self):
        set_rules(self)

