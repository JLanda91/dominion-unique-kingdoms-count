from itertools import chain


def cartesian_product_eq_sum(*ranges, s, curr_elems=None):
    if not ranges:
        return ()
    if curr_elems is None:
        curr_elems = tuple()
    next_range, *other_ranges = ranges
    if len(ranges) == 1:
        return ((curr_elems + (s,)),) if next(iter(next_range)) <= s <= next(iter(reversed(next_range))) else ()
    return chain.from_iterable(cartesian_product_eq_sum(*other_ranges, s=s - k, curr_elems=curr_elems + (k,)) for k in
                               filter(lambda k: k <= s, next_range))


def cartesian_product_leq_sum(*ranges, s, curr_elems=None):
    if not ranges:
        return ()
    if curr_elems is None:
        curr_elems = tuple()
    next_range, *other_ranges = ranges
    if len(ranges) == 1:
        return (curr_elems + (k,) for k in filter(lambda k: k <= s, next_range))
    return chain.from_iterable((cartesian_product_leq_sum(*other_ranges, s=s - k, curr_elems=curr_elems + (k,)) for k in
                                filter(lambda k: k <= s, next_range)))
