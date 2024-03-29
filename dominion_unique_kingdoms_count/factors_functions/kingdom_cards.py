from dominion_unique_kingdoms_count.util.accumulators import (
    binomial_coefficient_product,
)

from dominion_unique_kingdoms_count.util.constants import (
    BOON_SHUFFLE_CHOICES_DRUID,
    RUINS_CHOICES,
    LIAISON_ALLY_CHOICES,
    HEX_SHUFFLE_CHOICES,
    DRUID_BOON_CHOICES,
    KNIGHT_SHUFFLE_CHOICES,
    BOON_SHUFFLE_CHOICES_NO_DRUID,
)

from dominion_unique_kingdoms_count.util.conditional_mul import (
    mul_if,
)

from dominion_unique_kingdoms_count.config import (
    CONFIG,
)


def kingdom_cards_factors(
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
):
    binomial_product = binomial_coefficient_product(CONFIG.generators.kingdom_cards.card_totals.values(),
                                                    tuple(locals().values()))

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
                      * mul_if(druid > 0, DRUID_BOON_CHOICES) \
                      * mul_if(liaison_total > 0, LIAISON_ALLY_CHOICES)

    result_ordered = result_unordered \
                    * mul_if(fate_total > 0, (BOON_SHUFFLE_CHOICES_DRUID if druid else BOON_SHUFFLE_CHOICES_NO_DRUID)) \
                    * mul_if(doom_total > 0, HEX_SHUFFLE_CHOICES) \
                    * mul_if(knights > 0, KNIGHT_SHUFFLE_CHOICES) \
                    * mul_if(action_looter_high > 0, RUINS_CHOICES)

    return result_unordered, result_ordered
