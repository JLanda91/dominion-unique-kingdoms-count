from itertools import product
from time import perf_counter_ns

from config import CONFIG
from util.accumulators.pair_accumulate import pair_sum, pair_product
from util.generators.identity_with_map import IdentityWithMap
from factors_functions import kingdom_cards_factors, non_cards_factors, joint_factors


def all_factors(kingdom_combination, kingdom_factors, non_combination, non_factors):
    return kingdom_factors, non_factors, joint_factors(*kingdom_combination, *non_combination)


def output_csv():
    t1 = perf_counter_ns()
    joint_gen = product(CONFIG.generators.kingdom_cards(), CONFIG.generators.non_cards())
    kingdom_gen_with_factors = IdentityWithMap(CONFIG.generators.kingdom_cards(), kingdom_cards_factors)
    non_gen_with_factors = IdentityWithMap(CONFIG.generators.non_cards(), non_cards_factors)
    all_factors_gen = (pair_product(all_factors(kingdom_combi, kingdom_factors, non_combi, non_factors)) for
                       (kingdom_combi, kingdom_factors), (non_combi, non_factors) in
                       product(kingdom_gen_with_factors, non_gen_with_factors))
    with open('combination_values.csv', 'w') as f:
        f.write(f"{','.join(tuple(CONFIG.generators.kingdom_cards.card_totals.keys()) + tuple(CONFIG.generators.non_cards.card_totals.keys()))}\n")
        for (kingdom_combi, non_combi), factors in zip(joint_gen, all_factors_gen):
            f.write(f"{','.join(map(str, kingdom_combi + non_combi + factors))}\n")
    t2 = perf_counter_ns()
    print("Written entire csv")
    print()
    print(f"Elapsed time: {(t2 - t1) / 1e9} s")


def main():
    t1 = perf_counter_ns()
    kingdom_gen_with_factors = IdentityWithMap(CONFIG.generators.kingdom_cards(), kingdom_cards_factors)
    non_gen_with_factors = IdentityWithMap(CONFIG.generators.non_cards(), non_cards_factors)
    all_factors_gen = (pair_product(all_factors(kingdom_combi, kingdom_factors, non_combi, non_factors)) for
                       (kingdom_combi, kingdom_factors), (non_combi, non_factors) in
                       product(kingdom_gen_with_factors, non_gen_with_factors))
    total_unordered, total_ordered = pair_sum(all_factors_gen)
    t2 = perf_counter_ns()

    print(f"Total unique kingdoms:")
    print(f"Not considering deck orderings:\t{total_unordered}")
    print(f"Considering deck orderings:\t\t{total_ordered}")
    print()
    print(f"Elapsed time: {(t2 - t1) / 1e9} s")


if __name__ == '__main__':
    main()
