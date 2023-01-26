from functools import reduce
from operator import mul
from itertools import starmap
from math import comb


def binomial_coefficient_product(n_collection, k_collection):
    return reduce(mul,
                  starmap(comb, zip(n_collection, k_collection)),
                  1)

