import unittest
from unittest.mock import patch, call
from parameterized import parameterized

from factors_functions import kingdom_cards_factors


class TestKingdomCardsFactors(unittest.TestCase):

    def setUp(self) -> None:
        self.n_collection = list(2 * n + 1 for n in range(16))
        self.k_collection = list(n + 1 for n in range(16))

    @parameterized.expand([
        (True,),
        (False,),
    ])
    @patch('factors_functions.kingdom_cards.CONFIG')
    @patch('factors_functions.kingdom_cards.binomial_coefficient_product')
    @patch('factors_functions.kingdom_cards.mul_if')
    @patch('factors_functions.kingdom_cards.DRUID_BOON_CHOICES', 17)
    @patch('factors_functions.kingdom_cards.LIAISON_ALLY_CHOICES', 13)
    @patch('factors_functions.kingdom_cards.BOON_SHUFFLE_CHOICES_NO_DRUID', 11)
    @patch('factors_functions.kingdom_cards.BOON_SHUFFLE_CHOICES_DRUID', 7)
    @patch('factors_functions.kingdom_cards.HEX_SHUFFLE_CHOICES', 5)
    @patch('factors_functions.kingdom_cards.KNIGHT_SHUFFLE_CHOICES', 3)
    @patch('factors_functions.kingdom_cards.RUINS_CHOICES', 2)
    def test_non_cards_factors_druid(self, is_druid, mock_mul_if, mock_binomial_coefficient_product, mock_config):
        # if we test without druid, set coefficient in the arguments to 0
        if not is_druid:
            self.k_collection[6] = 0

        # Setting up return values for the config totals, binomial coefficient product and mul_if
        mock_config.generators.kingdom_cards.card_totals.values.return_value = self.n_collection
        mock_binomial_coefficient_product.return_value = 123
        mock_mul_if.side_effect = (2, 3, 5, 7, 11, 13)

        # Run function and verify test outcome
        self.assertEqual((738, 3693690), kingdom_cards_factors(*self.k_collection))

        # mock asserts
        mock_config.generators.kingdom_cards.card_totals.values.assert_called_once()
        mock_binomial_coefficient_product.called_once_with(self.n_collection, self.k_collection)
        mul_if_expected_args = [call(7 if is_druid else 0, 17),     # mul_if(druid, DRUID_BOON_CHOICES)
                                call(17, 13),                       # mul_if(liaison_total, LIAISON_ALLY_CHOICES)
                                call(30, 7 if is_druid else 11),    # mul_if(fate_total, (BOON_SHUFFLE_CHOICES_DRUID if druid else BOON_SHUFFLE_CHOICES_NO_DRUID))
                                call(35, 5),                        # mul_if(doom_total, HEX_SHUFFLE_CHOICES)
                                call(16, 3),                        # mul_if(knights, KNIGHT_SHUFFLE_CHOICES)
                                call(11, 2)]                        # mul_if(action_looter_high, RUINS_CHOICES)
        mock_mul_if.has_calls(mul_if_expected_args)


if __name__ == '__main__':
    unittest.main()
