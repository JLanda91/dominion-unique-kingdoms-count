def pair_sum(pair_collection):
    r1, r2 = 0, 0
    for i1, i2 in pair_collection:
        r1 += i1
        r2 += i2
    return r1, r2


def pair_product(pair_collection):
    r1, r2 = 1, 1
    for i1, i2 in pair_collection:
        r1 *= i1
        r2 *= i2
    return r1, r2
