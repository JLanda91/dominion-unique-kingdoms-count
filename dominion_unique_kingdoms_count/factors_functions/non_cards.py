from dominion_unique_kingdoms_count.util.accumulators import (
    binomial_coefficient_product,
)

from dominion_unique_kingdoms_count.config import (
    CONFIG,
)


def non_cards_factors(
        landscapes: int,
        obelisk: int,
        way_of_the_mouse: int,
):
    result_unordered = binomial_coefficient_product(CONFIG.generators.non_cards.card_totals.values(),
                                                    tuple(locals().values()))
    result_ordered = result_unordered

    return result_unordered, result_ordered
