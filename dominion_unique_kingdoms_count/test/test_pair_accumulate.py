import unittest
from parameterized import parameterized, param

from dominion_unique_kingdoms_count.util.accumulators import (
    pair_product,
    pair_sum,
)


class TestPairAccumulate(unittest.TestCase):

    @parameterized.expand([
        param([], (0, 0)),
        param([(49, 20)], (49, 20)),
        param([(49, 20), (-50, 2)], (-1, 22)),
    ])
    def test_pair_sum(self, pair_collection, outcome):
        self.assertEqual(outcome, pair_sum(pair_collection))

    @parameterized.expand([
        param([], (1, 1)),
        param([(1, -1)], (1, -1)),
        param([(4, -3), (-1, -2)], (-4, 6)),
    ])
    def test_pair_product(self, pair_collection, outcome):
        self.assertEqual(outcome, pair_product(pair_collection))


if __name__ == '__main__':
    unittest.main()
