from inspect import signature

from dominion_unique_kingdoms_count.factors_functions.kingdom_cards import (
    kingdom_cards_factors
)

from dominion_unique_kingdoms_count.factors_functions.non_cards import (
    non_cards_factors
)

from dominion_unique_kingdoms_count.factors_functions.joint import (
    joint_factors
)

from dominion_unique_kingdoms_count.config import (
    CONFIG
)


def __validate_factor_function_signatures():
    kingdom_cards_factors_params = tuple(signature(kingdom_cards_factors).parameters.keys())
    non_cards_factors_params = tuple(signature(non_cards_factors).parameters.keys())
    joint_factors_params = tuple(signature(joint_factors).parameters.keys())

    kingdom_card_types = tuple(CONFIG.generators.kingdom_cards.card_totals.keys())
    non_card_types = tuple(CONFIG.generators.non_cards.card_totals.keys())
    joint_types = kingdom_card_types + non_card_types

    if kingdom_cards_factors_params != kingdom_card_types:
        raise AssertionError(f"Kingdom card factor function parameters {kingdom_cards_factors_params} do not match the kingdom card types in the config {kingdom_card_types}")
    if non_cards_factors_params != non_card_types:
        raise AssertionError(f"Non card factor function parameters {non_cards_factors_params} do not match the non card types in the config {non_card_types}")
    if joint_factors_params != joint_types:
        raise AssertionError(f"Joint factor function parameters {joint_factors_params} do not match the kingdom + non card types in the config {joint_types}")


__validate_factor_function_signatures()
