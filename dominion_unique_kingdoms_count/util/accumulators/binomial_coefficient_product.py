from functools import reduce
from operator import mul
from itertools import starmap
from math import comb


def binomial_coefficient_product(n_collection, k_collection):
    assert len(n_collection) == len(k_collection), f"Unequal amount of n and k coefficients ({len(n_collection)} and {len(k_collection)} respectively)"
    return reduce(mul, starmap(comb, zip(n_collection, k_collection)), 1)

