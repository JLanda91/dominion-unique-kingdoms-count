from math import factorial
from config import CONFIG


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
