from math import factorial, comb
from config import CONFIG


BOON_SHUFFLE_CHOICES_NO_DRUID = factorial(CONFIG.other_card_totals.boons)
BOON_SHUFFLE_CHOICES_DRUID = factorial(CONFIG.other_card_totals.boons - CONFIG.constants.druid_boon_picks)
HEX_SHUFFLE_CHOICES = factorial(CONFIG.other_card_totals.hexes)
KNIGHTS_SHUFFLE_CHOICES = factorial(CONFIG.other_card_totals.knights)

DRUID_BOON_CHOICES = comb(CONFIG.other_card_totals.boons, CONFIG.constants.druid_boon_picks)
LIAISON_ALLY_CHOICES = CONFIG.other_card_totals.allies
NUM_WAYS_STACKING_20_CARDS_FROM_5_PILES_EACH_WITH_10_IDENTICAL_CARDS = 95098775054140
ACTION_LOW_CARD_TOTALS = CONFIG.generators.kingdom_cards.card_totals.action_low + \
                         CONFIG.generators.kingdom_cards.card_totals.action_liaison_low + \
                         CONFIG.generators.kingdom_cards.card_totals.action_fate_low + \
                         CONFIG.generators.kingdom_cards.card_totals.action_doom_low + \
                         CONFIG.generators.kingdom_cards.card_totals.druid
