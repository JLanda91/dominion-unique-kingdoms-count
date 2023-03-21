import unittest
from parameterized import parameterized, param

from dominion_unique_kingdoms_count.util.accumulators import (
    binomial_coefficient_product
)


class TestBinomialCoefficientProduct(unittest.TestCase):

    @parameterized.expand([
        param((), (), 1),
        param((0,), (0,), 1),
        param((4,), (2,), 6),
        param((4, 5, ), (2, 3, ), 60),
        param((4, 5, 3, ), (2, 3, 4, ), 0),
        param((100, 99, 98, 102, 101, 184,),(30, 41, 50, 82, 9, 63,), 2098319522102982430441665861541565828199409229552948100690454064018587110790598917073418963142137697568328851838229503768403781719730318547756519846058719633408000000),
        param((4, 5, 3,), (2, 3,), None),
        param((4, 5, 3,), (2, 3, -1,), None),
        param((4, 5, -1,), (2, 3, 2,), None),
    ])
    def test_binomial_coefficient_product(self, n_collection, k_collection, outcome):
        if len(n_collection) != len(k_collection):
            self.assertRaises(AssertionError, binomial_coefficient_product, n_collection, k_collection)
        elif any(map(lambda x: x < 0, n_collection + k_collection)):
            self.assertRaises(ValueError, binomial_coefficient_product, n_collection, k_collection)
        else:
            self.assertEqual(outcome, binomial_coefficient_product(n_collection, k_collection))


if __name__ == '__main__':
    unittest.main()
