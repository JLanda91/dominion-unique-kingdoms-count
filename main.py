from itertools import product
from time import perf_counter_ns
from math import comb, factorial

from helpers import cartesian_product_eq_sum, cartesian_product_leq_sum


# pre-compute some constants
f_9 = factorial(9)
f_10 = factorial(10)
f_12 = factorial(12)


def kingdom_count(landscapes, obelisk, way_of_the_mouse, action_low, other_low, action_liaison_low, other_liaison_low,
                  action_fate_low, action_doom_low, druid, action_high, other_high, action_liaison_high,
                  action_looter_high, action_fate_high, other_fate_high, action_doom_high, other_doom_high,
                  knights, y_witch):
    count_unordered = 1

    count_unordered *= comb(98, action_low)
    count_unordered *= comb(16, other_low)
    count_unordered *= comb(4, action_liaison_low)
    count_unordered *= comb(3, action_fate_low)
    count_unordered *= comb(246, action_high)
    count_unordered *= comb(37, other_high)
    count_unordered *= comb(4, action_liaison_high)
    count_unordered *= comb(3, action_looter_high)
    count_unordered *= comb(3, action_fate_high)
    count_unordered *= comb(4, action_doom_high)
    count_unordered *= comb(113, landscapes)

    if obelisk:
        count_unordered *= max(1, action_low + action_liaison_low + action_fate_low + action_doom_low + druid + action_high + action_liaison_high + action_looter_high + action_fate_high + action_doom_high + knights + y_witch)

    if way_of_the_mouse:
        count_unordered *= 107 - (action_low + action_liaison_low + action_fate_low + action_doom_low + druid)

    if action_liaison_low + other_liaison_low + action_liaison_low + action_liaison_high:
        count_unordered *= 23

    if druid:
        count_unordered *= 220

    if y_witch:
        count_unordered *= action_low + other_low + action_liaison_low + other_liaison_low + action_fate_low + action_doom_low + druid

    count_ordered = count_unordered

    if action_fate_low + action_fate_high + other_fate_high:
        count_ordered *= f_9 if druid else f_12

    if action_doom_low + action_doom_high + other_doom_high:
        count_ordered *= f_12

    if knights:
        count_ordered *= f_10

    if action_looter_high:
        count_ordered *= 95098775054140

    return count_unordered, count_ordered


def get_total_count():
    landscapes_obelisk_way_of_the_mouse_ranges = (
        range(3),  # landscapes             0-2
        range(2),  # obelisk                0-1
        range(2),  # way_of_the_mouse       0-1
    )

    landscapes_obelisk_way_of_the_mouse_leq_2 = cartesian_product_leq_sum(*landscapes_obelisk_way_of_the_mouse_ranges, s=2)

    kingdom_ranges = (
        range(11),  # action_low            0-10
        range(11),  # other_low             0-10
        range(5),  # action_liaison_low     0-4
        range(2),  # other_liaison_low      0-1
        range(4),  # action_fate_low        0-3
        range(2),  # action_doom_low        0-1

        range(2),  # druid                  0-1

        range(11),  # action_high           0-10
        range(11),  # other_high            0-10
        range(5),  # action_liaison_high    0-4
        range(4),  # action_looter_high     0-3
        range(4),  # action_fate_high       0-3
        range(2),  # other_fate_high        0-1
        range(5),  # action_doom_high       0-4
        range(2),  # other_doom_high        0-1

        range(2),  # knights                0-1
    )

    kingdom_eq_10 = cartesian_product_eq_sum(*kingdom_ranges, s=10)

    y_witch_range = range(2)

    result_unordered = 0
    result_ordered = 0

    for l_o_w, kingdom, y_witch in product(landscapes_obelisk_way_of_the_mouse_leq_2, kingdom_eq_10, y_witch_range):
        y_witch_sum = sum(kingdom[:7])
        if y_witch > 0 and y_witch_sum == 0:
            continue
        incr_unordered, incr_ordered = kingdom_count(*l_o_w, *kingdom, y_witch)
        result_unordered += incr_unordered
        result_ordered += incr_ordered
    return result_unordered, result_ordered


if __name__ == '__main__':
    t1 = perf_counter_ns()
    total_unordered, total_ordered = get_total_count()
    t2 = perf_counter_ns()
    print(f"Total possibilities:\nUnordered stacks:\t{total_unordered}\nOrdered stacks:\t\t{total_ordered}\n\nElapsed time = {(t2 - t1) / 1e9} s")