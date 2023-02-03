from util.accumulators import binomial_coefficient_product
from config import CONFIG


def non_cards_factors(
    landscapes,
    obelisk,
    way_of_the_mouse
):
    result_unordered = binomial_coefficient_product(CONFIG.generators.non_cards.card_totals.values(),
                                                    locals().values())
    result_ordered = result_unordered

    return result_unordered, result_ordered
