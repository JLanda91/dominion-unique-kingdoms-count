import unittest
from unittest.mock import Mock, patch, call
from parameterized import parameterized

from factors_functions import non_cards_factors


class TestNonCardsFactors(unittest.TestCase):

    @patch('factors_functions.non_cards.CONFIG')
    @patch('factors_functions.non_cards.binomial_coefficient_product')
    def test_non_cards_factors(self, binom_mock, config_mock):
        n_collection = (4,5,6)
        k_collection = (1,2,3)

        # Setting up return values for the config totals and binom product
        config_mock.generators.non_cards.card_totals.values.return_value = n_collection
        binom_mock.return_value = 42

        # Run function and test outcome
        self.assertEqual((42, 42), non_cards_factors(*k_collection))

        # mock asserts
        config_mock.generators.non_cards.card_totals.values.assert_called_once()
        binom_mock.called_once_with(n_collection, k_collection)


if __name__ == '__main__':
    unittest.main()
