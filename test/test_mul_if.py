from util.conditional_mul import mul_if

import unittest
from parameterized import parameterized

class TestConditionalMul(unittest.TestCase):

    @parameterized.expand([
        [True, 100, 50, 100],
        [False, 100, 50, 50],
    ])
    def test_mul_if_with_false_value(self, condition, val_true, val_false, outcome):
        self.assertEqual(outcome, mul_if(condition, val_true, val_false))

    @parameterized.expand([
        [True, 100, 100],
        [False, 100, 1],
    ])
    def test_mul_if_without_false_value(self, condition, val_true, outcome):
        self.assertEqual(outcome, mul_if(condition, val_true))


if __name__ == '__main__':
    unittest.main()
