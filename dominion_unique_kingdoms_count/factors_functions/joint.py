from dominion_unique_kingdoms_count.util.constants import (
    ACTION_LOW_CARD_TOTALS,
)

from dominion_unique_kingdoms_count.util.conditional_mul import (
    mul_if,
)


def joint_factors(
    action_low: int,
    other_low: int,
    action_liaison_low: int,
    other_liaison_low: int,
    action_fate_low: int,
    action_doom_low: int,
    druid: int,
    action_high: int,
    other_high: int,
    action_liaison_high: int,
    action_looter_high: int,
    action_fate_high: int,
    other_fate_high: int,
    action_doom_high: int,
    other_doom_high: int,
    knights: int,

    landscapes: int,
    obelisk: int,
    way_of_the_mouse: int,
):
    action_low_total = action_low + \
                       action_liaison_low + \
                       action_fate_low + \
                       action_doom_low + \
                       druid

    low_total = action_low_total + \
                other_low + \
                other_liaison_low

    action_high_total = action_high + \
                        action_liaison_high + \
                        action_fate_high + \
                        action_looter_high + \
                        action_doom_high + \
                        knights

    obelisk_choices = action_low_total + action_high_total

    result_unordered = mul_if(way_of_the_mouse > 0, ACTION_LOW_CARD_TOTALS - action_low_total) \
                     * mul_if(obelisk > 0 and obelisk_choices > 0, obelisk_choices + low_total * (obelisk_choices + 1), 1 + low_total)

    result_ordered = result_unordered

    return result_unordered, result_ordered

