from main import kingdom_count
from config.config_parser import GenericAttributeMap

if __name__ == '__main__':
    card_total = GenericAttributeMap(**{'action_low': 0, 'other_low': 0, 'action_liaison_low': 0, 'other_liaison_low': 0, 'action_fate_low': 0, 'action_doom_low': 0, 'druid': 0, 'action_high': 0, 'other_high': 0, 'action_liaison_high': 0, 'action_looter_high': 1, 'action_fate_high': 2, 'other_fate_high': 1, 'action_doom_high': 4, 'other_doom_high': 1, 'knights': 1})
    print(*kingdom_count(card_total))

