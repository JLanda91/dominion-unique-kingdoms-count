import unittest
from unittest.mock import patch

from dominion_unique_kingdoms_count.factors_functions import (
    non_cards_factors,
)


class TestNonCardsFactors(unittest.TestCase):

    def setUp(self) -> None:
        self.n_collection = (4,5,6)
        self.k_collection = (1,2,3)

    @patch('dominion_unique_kingdoms_count.factors_functions.non_cards.CONFIG')
    @patch('dominion_unique_kingdoms_count.factors_functions.non_cards.binomial_coefficient_product')
    def test_non_cards_factors(self, mock_binom, mock_config):
        # Setting up return values for the config totals and binom product
        mock_config.generators.non_cards.card_totals.values.return_value = self.n_collection
        mock_binom.return_value = 42

        # Run function and test outcome
        self.assertEqual((42, 42), non_cards_factors(*self.k_collection))

        # mock asserts
        mock_config.generators.non_cards.card_totals.values.assert_called_once()
        mock_binom.called_once_with(self.n_collection, self.k_collection)


if __name__ == '__main__':
    unittest.main()
