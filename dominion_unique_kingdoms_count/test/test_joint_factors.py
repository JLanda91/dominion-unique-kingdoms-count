import unittest
from unittest.mock import patch, call
from parameterized import parameterized, param

from dominion_unique_kingdoms_count.factors_functions import (
    joint_factors,
)


class TestJointFactors(unittest.TestCase):
    args = [param("with way of the mouse without obelisk",
                  {
                      'action_low': 1,
                      'other_low': 1,
                      'action_liaison_low': 1,
                      'other_liaison_low': 0,
                      'action_fate_low': 1,
                      'action_doom_low': 1,
                      'druid': 1,
                      'action_high': 0,
                      'other_high': 0,
                      'action_liaison_high': 1,
                      'action_looter_high': 0,
                      'action_fate_high': 1,
                      'other_fate_high': 0,
                      'action_doom_high': 0,
                      'other_doom_high': 1,
                      'knights': 0,
                      'landscapes': 0,
                      'obelisk': 0,
                      'way_of_the_mouse': 1,
                  },
                  [
                      call(True, 92),
                      call(False, 55, 7)
                  ]
                 ),
            param("without way of the mouse with obelisk no choice",
                  {
                      'action_low': 0,
                      'other_low': 2,
                      'action_liaison_low': 0,
                      'other_liaison_low': 1,
                      'action_fate_low': 0,
                      'action_doom_low': 0,
                      'druid': 0,
                      'action_high': 0,
                      'other_high': 2,
                      'action_liaison_high': 0,
                      'action_looter_high': 0,
                      'action_fate_high': 0,
                      'other_fate_high': 2,
                      'action_doom_high': 0,
                      'other_doom_high': 2,
                      'knights': 0,
                      'landscapes': 0,
                      'obelisk': 1,
                      'way_of_the_mouse': 0,
                  },
                  [
                      call(False, 97),
                      call(False, 3, 4)
                  ]
                  ),
            param("without way of the mouse with obelisk no choice",
                  {
                      'action_low': 2,
                      'other_low': 2,
                      'action_liaison_low': 0,
                      'other_liaison_low': 1,
                      'action_fate_low': 0,
                      'action_doom_low': 0,
                      'druid': 0,
                      'action_high': 0,
                      'other_high': 0,
                      'action_liaison_high': 0,
                      'action_looter_high': 0,
                      'action_fate_high': 1,
                      'other_fate_high': 0,
                      'action_doom_high': 3,
                      'other_doom_high': 0,
                      'knights': 0,
                      'landscapes': 0,
                      'obelisk': 1,
                      'way_of_the_mouse': 0,
                  },
                  [
                      call(False, 95),
                      call(True, 41, 6)
                  ]
                  ),
            ]

    @parameterized.expand(args)
    @patch('dominion_unique_kingdoms_count.factors_functions.joint.mul_if')
    @patch('dominion_unique_kingdoms_count.factors_functions.joint.ACTION_LOW_CARD_TOTALS', 97)
    def test_joint_factors(self, _, joint_factor_args, mul_if_calls, mock_mul_if):
        """"Test Joint Factors"""
        mock_mul_if.side_effect = (83, 89,)
        self.assertEqual((7387, 7387), joint_factors(**joint_factor_args))
        mock_mul_if.assert_has_calls(mul_if_calls)


if __name__ == '__main__':
    unittest.main()
