from itertools import product
from time import perf_counter_ns

from config import CONFIG
from util.accumulators import pair_sum, pair_product
from factors_functions import kingdom_cards_factors, non_cards_factors, joint_factors


def main():
    t1 = perf_counter_ns()

    kingdom_gen = ((x, kingdom_cards_factors(*x)) for x in CONFIG.generators.kingdom_cards())
    non_gen = ((x, non_cards_factors(*x)) for x in CONFIG.generators.non_cards())
    joint_gen = ((kingdom_factors, non_factors, joint_factors(*kingdom_combi, *non_combi)) for (kingdom_combi, kingdom_factors), (non_combi, non_factors) in product(kingdom_gen, non_gen))
    total_unordered, total_ordered = pair_sum(map(pair_product, joint_gen))

    t2 = perf_counter_ns()

    print(f"Total unique kingdoms:")
    print(f"Not considering deck orderings:\t{total_unordered}")
    print(f"Considering deck orderings:\t\t{total_ordered}")
    print()
    print(f"Elapsed time: {(t2 - t1) / 1e9} s")


if __name__ == '__main__':
    main()
