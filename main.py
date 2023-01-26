import itertools
from math import factorial
from time import perf_counter_ns

from config import CONFIG
from util.accumulators import pair_sum, pair_product, binomial_coefficient_product
from util.conditional_multiply import mul_if

# pre-compute some constants
F_9 = factorial(9)
F_10 = factorial(10)
F_12 = factorial(12)

DRUID_MULTIPLIER = 220
LIAISON_MULTIPLIER = 23
NUM_WAYS_STACKING_20_CARDS_FROM_5_PILES_EACH_WITH_10_IDENTICAL_CARDS = 95098775054140
ACTION_LOW_CARD_TOTALS = CONFIG.generators.kingdom_cards.card_totals.action_low + \
                         CONFIG.generators.kingdom_cards.card_totals.action_liaison_low + \
                         CONFIG.generators.kingdom_cards.card_totals.action_fate_low + \
                         CONFIG.generators.kingdom_cards.card_totals.action_doom_low + \
                         CONFIG.generators.kingdom_cards.card_totals.druid


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
    

def non_cards_factors(
    landscapes,
    obelisk,
    way_of_the_mouse
):
    result_unordered = binomial_coefficient_product(CONFIG.generators.non_cards.card_totals.values(),
                                                    locals().values())
    result_ordered = result_unordered

    return result_unordered, result_ordered


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


def main():
    t1 = perf_counter_ns()

    kingdom_gen = ((x, kingdom_cards_factors(*x)) for x in CONFIG.generators.kingdom_cards())
    non_gen = ((x, non_cards_factors(*x)) for x in CONFIG.generators.non_cards())
    joint_gen = ((kingdom_factors, non_factors, joint_factors(*kingdom_combi, *non_combi)) for (kingdom_combi, kingdom_factors), (non_combi, non_factors) in itertools.product(kingdom_gen, non_gen))
    total_unordered, total_ordered = pair_sum(map(pair_product, joint_gen))

    t2 = perf_counter_ns()

    print(f"Total unique kingdoms:")
    print(f"Not considering deck orderings:\t{total_unordered}")
    print(f"Considering deck orderings:\t\t{total_ordered}")
    print()
    print(f"Elapsed time: {(t2 - t1) / 1e9} s")


if __name__ == '__main__':
    main()
