from math import factorial, comb

from dominion_unique_kingdoms_count.config import CONFIG
from dominion_unique_kingdoms_count.util.generators import ProductEQ


def __num_ruins_choices(num_players: int):
    ruins_picks = 10*(num_players-1)

    def ruins_multinom(*args):
        result = 1
        n = ruins_picks
        for k in args:
            result *= comb(n, k)
            n -= k
            if n == 0:
                break
        return result

    return sum(ruins_multinom(*x) for
               x in
               ProductEQ(*(range(CONFIG.other_card_totals.ruins_per_type + 1) for
                           _ in
                           range(CONFIG.other_card_totals.ruins_types)), s=ruins_picks))


BOON_SHUFFLE_CHOICES_NO_DRUID = factorial(CONFIG.other_card_totals.boons)
BOON_SHUFFLE_CHOICES_DRUID = factorial(CONFIG.other_card_totals.boons - CONFIG.constants.druid_boon_picks)
HEX_SHUFFLE_CHOICES = factorial(CONFIG.other_card_totals.hexes)
KNIGHT_SHUFFLE_CHOICES = factorial(CONFIG.other_card_totals.knights)

DRUID_BOON_CHOICES = comb(CONFIG.other_card_totals.boons, CONFIG.constants.druid_boon_picks)
LIAISON_ALLY_CHOICES = CONFIG.other_card_totals.allies
RUINS_CHOICES = __num_ruins_choices(num_players=2)
ACTION_LOW_CARD_TOTALS = CONFIG.generators.kingdom_cards.card_totals.action_low + \
                         CONFIG.generators.kingdom_cards.card_totals.action_liaison_low + \
                         CONFIG.generators.kingdom_cards.card_totals.action_fate_low + \
                         CONFIG.generators.kingdom_cards.card_totals.action_doom_low + \
                         CONFIG.generators.kingdom_cards.card_totals.druid
