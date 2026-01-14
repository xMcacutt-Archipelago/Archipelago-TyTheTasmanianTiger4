from dataclasses import dataclass

from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionGroup, PerGameCommonOptions


class Goal(Choice):
    """
    Determines the goal of the seed

    Beat Boss Cass: Beat Boss Cass in As Ty Goes By... and save the world
    """
    display_name = "Goal"
    option_final_battle = 0
    default = 0


class GoalRequiresBosses(Toggle):
    """
    Determines if beating all bosses is a requirement to go to As Ty Goes By...
    """
    display_name = "Goal Requires Bosses"



class ProgressiveElementals(DefaultOnToggle):
    """
    Determines if elemental rangs are a progressive check
    """
    display_name = "Progressive Elemental Rangs"



class ProgressiveLevel(DefaultOnToggle):
    """
    Determines if level unlocks are progressive (only if levels are check based)
    """
    display_name = "Progressive Level"




class TrapFill(Range):
    """
    Determines the percentage of the junk fill which is filled with traps.
    """
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0



class ExitTrapWeight(Range):
    """The weight of Exit Traps in the trap pool.
    Exit Traps immediately force you out of the current level, putting you back in Rainbow Cliffs."""
    display_name = "Exit Trap Weight"
    range_start = 0
    range_end = 100
    default = 20


ty4_option_groups = [
    OptionGroup("Goal Options", [
        Goal,
        GoalRequiresBosses,
    ]),
    OptionGroup("Logic Options", [
        ProgressiveElementals,
        ProgressiveLevel,
    ]),
    OptionGroup("Sanity Options", [
    ]),
    OptionGroup("Traps", [
        TrapFill,
        ExitTrapWeight,
    ]),
    OptionGroup("Death Link", [
        DeathLink
    ]),
    OptionGroup("Mul-Ty Link", [

    ])
]


@dataclass
class Ty4Options(PerGameCommonOptions):
    goal: Goal
    req_bosses: GoalRequiresBosses

    progressive_elementals: ProgressiveElementals


    progressive_level: ProgressiveLevel


    death_link: DeathLink
    trap_fill_percentage: TrapFill
    exit_trap_weight: ExitTrapWeight

