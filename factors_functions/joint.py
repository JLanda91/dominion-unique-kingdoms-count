from util.constants import *
from util.conditional_multiply import mul_if


def joint_factors(
    action_low,
    other_low,
    action_liaison_low,
    other_liaison_low,
    action_fate_low,
    action_doom_low,
    druid,
    action_high,
    other_high,
    action_liaison_high,
    action_looter_high,
    action_fate_high,
    other_fate_high,
    action_doom_high,
    other_doom_high,
    knights,

    landscapes,
    obelisk,
    way_of_the_mouse
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
                        action_fate_low + \
                        action_looter_high + \
                        action_doom_high + \
                        knights

    obelisk_choices = action_low_total + action_high_total

    result_unordered = mul_if(way_of_the_mouse, (ACTION_LOW_CARD_TOTALS - action_low_total)) \
                     * mul_if(obelisk and obelisk_choices,
                              obelisk_choices + low_total * (obelisk_choices + 1),
                              1 + low_total)

    result_ordered = result_unordered

    return result_unordered, result_ordered

