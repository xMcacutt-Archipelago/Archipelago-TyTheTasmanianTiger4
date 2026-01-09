from dataclasses import dataclass

from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionGroup, PerGameCommonOptions


class Goal(Choice):
    """
    Determines the goal of the seed

    Final Battle: Beat Boss Cass in Final Battle and rescue your parents from The Dreaming
    """
    display_name = "Goal"
    option_final_battle = 0
    default = 0


class GoalRequiresBosses(Toggle):
    """
    Determines if beating all bosses is a requirement to go to Final Battle
    """
    display_name = "Goal Requires Bosses"



class ProgressiveElementals(DefaultOnToggle):
    """
    Determines if elemental rangs are a progressive check
    """
    display_name = "Progressive Elemental Rangs"


class LevelUnlockStyle(Choice):
    """
    Determines how levels are unlocked

    Vanilla: All levels are unlocked from the start of the world

    Checks: The first level is unlocked from the start but all other levels are unlocked via checks

    Checks - No Bosses: The first level will be unlocked from the start. Bosses can be unlocked via hub Thunder Egg counts. All other levels must be unlocked via checks
    """
    display_name = "Level Unlock Style"
    option_vanilla = 0
    option_checks = 1
    option_checks_no_bosses = 2
    default = 2


class ProgressiveLevel(DefaultOnToggle):
    """
    Determines if level unlocks are progressive (only if levels are check based)
    """
    display_name = "Progressive Level"


class ThunderEggGating(Range):
    """
    If bosses are unlocked via hub Thunder Egg counts, required count per hub can be set here
    This also sets the required Thunder Egg count to receive the elemental attribute check after completing bosses
    """
    display_name = "Thunder Egg Gating"
    range_start = 0
    range_end = 24
    default = 17


class ExtraCogs(Range):
    """
    Sets number of additional golden cogs to add to the pool
    WARNING - Setting this value high without sanity is likely to lead to generation failures
    """
    display_name = "Extra Cogs"
    range_start = 0
    range_end = 90
    default = 30


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
        ThunderEggGating,
        ExtraCogs,
        LevelUnlockStyle,
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

    thegg_gating: ThunderEggGating
    extra_cogs: ExtraCogs

    level_unlock_style: LevelUnlockStyle
    progressive_level: ProgressiveLevel


    death_link: DeathLink
    trap_fill_percentage: TrapFill
    exit_trap_weight: ExitTrapWeight

