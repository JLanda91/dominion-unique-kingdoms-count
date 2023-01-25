import itertools
import operator
from functools import reduce
from math import comb, factorial
from time import perf_counter_ns

from config import CONFIG

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


def kingdom_count(kingdom_cards_combination):

    kingdom_cards_binomial_product = reduce(operator.mul,
                                            (comb(getattr(CONFIG.generators.kingdom_cards.card_totals, k), getattr(kingdom_cards_combination, k)) for k in kingdom_cards_combination),
                                            1)

    action_low_total = kingdom_cards_combination.action_low + \
                       kingdom_cards_combination.action_liaison_low + \
                       kingdom_cards_combination.action_fate_low + \
                       kingdom_cards_combination.action_doom_low + \
                       kingdom_cards_combination.druid

    low_total = action_low_total + \
                kingdom_cards_combination.other_low + \
                kingdom_cards_combination.other_liaison_low

    action_high_total = kingdom_cards_combination.action_high + \
                        kingdom_cards_combination.action_liaison_high + \
                        kingdom_cards_combination.action_fate_low + \
                        kingdom_cards_combination.action_looter_high + \
                        kingdom_cards_combination.action_doom_high + \
                        kingdom_cards_combination.knights

    liaison_total = kingdom_cards_combination.action_liaison_low + \
                    kingdom_cards_combination.other_liaison_low + \
                    kingdom_cards_combination.action_liaison_high

    fate_total = kingdom_cards_combination.action_fate_low + \
                 kingdom_cards_combination.action_fate_high + \
                 kingdom_cards_combination.other_fate_high

    doom_total = kingdom_cards_combination.action_doom_low + \
                 kingdom_cards_combination.action_doom_high + \
                 kingdom_cards_combination.other_doom_high

    kingdom_count_unordered = kingdom_cards_binomial_product * \
                              (DRUID_MULTIPLIER if kingdom_cards_combination.druid else 1) * \
                              (LIAISON_MULTIPLIER if liaison_total else 1)

    kingdom_count_ordered = kingdom_count_unordered \
                            * ((F_9 if kingdom_cards_combination.druid else F_12) if fate_total else 1) \
                            * (F_12 if doom_total else 1)  \
                            * (F_10 if kingdom_cards_combination.knights else 1) \
                            * (NUM_WAYS_STACKING_20_CARDS_FROM_5_PILES_EACH_WITH_10_IDENTICAL_CARDS if kingdom_cards_combination.action_looter_high else 1)

    def non_cards_count(non_cards_combination):
        non_cards_binomial_product = reduce(operator.mul, (
            comb(getattr(CONFIG.generators.non_cards.card_totals, k), getattr(non_cards_combination, k)) for k in
            non_cards_combination), 1)
        non_cards_count_unordered = non_cards_binomial_product
        non_cards_count_unordered *= ((ACTION_LOW_CARD_TOTALS - action_low_total) if non_cards_combination.way_of_the_mouse else 1)
        non_cards_count_unordered *= ((max(1, action_low_total + action_high_total) if non_cards_combination.obelisk else 1)  # no young witch
                                      + low_total * ((action_low_total + action_high_total + 1) if non_cards_combination.obelisk else 1))  # young witch
        non_cards_count_ordered = non_cards_count_unordered
        return non_cards_count_unordered, non_cards_count_ordered

    non_cards_total_unordered = 0
    non_cards_total_ordered = 0
    for incr_unordered, incr_ordered in map(non_cards_count, CONFIG.generators.non_cards()):
        non_cards_total_unordered += incr_unordered
        non_cards_total_ordered += incr_ordered
        # print(f"{incr_unordered:25}\t{total_unordered:25}\t|\t{incr_ordered:50}\t{total_ordered:50}")

    # non_cards_total_unordered, non_cards_total_ordered = reduce(lambda x, y: tuple(map(sum, zip(x, y))), map(non_cards_count, CONFIG.non_cards), (0, 0))

    ans_unordered = kingdom_count_unordered * non_cards_total_unordered
    ans_ordered = kingdom_count_ordered * non_cards_total_ordered
    return ans_unordered, ans_ordered


def total_count():
    total_unordered = 0
    total_ordered = 0
    for incr_unordered, incr_ordered in map(kingdom_count, CONFIG.generators.kingdom_cards()):
        total_unordered += incr_unordered
        total_ordered += incr_ordered
    return total_unordered, total_ordered


def main():
    t1 = perf_counter_ns()
    total_unordered, total_ordered = total_count()
    t2 = perf_counter_ns()
    print(f"Total unique kingdoms:")
    print(f"Not considering deck orderings:\t{total_unordered}")
    print(f"Considering deck orderings:\t\t{total_ordered}")
    print()
    print(f"Elapsed time: {(t2 - t1) / 1e9} s")


if __name__ == '__main__':
    main()
