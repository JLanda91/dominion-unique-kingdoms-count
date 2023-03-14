from util.accumulators import pair_product, pair_sum

import unittest
from parameterized import parameterized

class TestPairAccumulate(unittest.TestCase):

    @parameterized.expand([
        [[], (0, 0)],
        [[(49, 20)], (49, 20)],
        [[(49, 20), (-50, 2)], (-1, 22)],
    ])
    def test_pair_sum(self, pair_collection, outcome):
        self.assertEqual(outcome, pair_sum(pair_collection))

    @parameterized.expand([
        [[], (1, 1)],
        [[(1, -1)], (1, -1)],
        [[(4, -3), (-1, -2)], (-4, 6)],
    ])
    def test_pair_product(self, pair_collection, outcome):
        self.assertEqual(outcome, pair_product(pair_collection))


if __name__ == '__main__':
    unittest.main()
