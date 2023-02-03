from util.accumulators import binomial_coefficient_product
from util.constants import *
from util.conditional_multiply import mul_if
from config import CONFIG


def kingdom_cards_factors(
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
    knights
):
    binomial_product = binomial_coefficient_product(CONFIG.generators.kingdom_cards.card_totals.values(),
                                                    locals().values())

    liaison_total = action_liaison_low + \
                    other_liaison_low + \
                    action_liaison_high

    fate_total = action_fate_low + \
                 action_fate_high + \
                 other_fate_high

    doom_total = action_doom_low + \
                 action_doom_high + \
                 other_doom_high

    result_unordered = binomial_product \
                      * mul_if(druid, DRUID_MULTIPLIER) \
                      * mul_if(liaison_total, LIAISON_MULTIPLIER)

    result_ordered = result_unordered \
                    * mul_if(fate_total, (F_9 if druid else F_12)) \
                    * mul_if(doom_total, F_12) \
                    * mul_if(knights, F_10) \
                    * mul_if(action_looter_high,
                             NUM_WAYS_STACKING_20_CARDS_FROM_5_PILES_EACH_WITH_10_IDENTICAL_CARDS)

    return result_unordered, result_ordered
