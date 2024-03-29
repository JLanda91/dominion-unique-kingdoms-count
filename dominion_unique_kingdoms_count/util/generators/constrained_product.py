from itertools import chain


class ProductEQ:
    def __init__(self, *ranges, s: int):
        self.__gen = (self.__impl(*ranges, s=s))

    def __impl(self, *ranges, s, current_elements=None):
        if not ranges:
            return ()
        if current_elements is None:
            current_elements = tuple()
        next_range, *other_ranges = ranges
        if len(ranges) == 1:
            return ((current_elements + (s,)),) if s in next_range else ()
        return chain.from_iterable(
            self.__impl(
                *other_ranges,
                s=s - k,
                current_elements=current_elements + (k,)
            )
            for k in filter(lambda k: k <= s, next_range)
        )

    def __iter__(self):
        return iter(self.__gen)


class ProductLE:
    def __init__(self, *ranges, s: int):
        self.__gen = (self.__impl(*ranges, s=s))

    def __impl(self, *ranges, s, current_elements=None):
        if not ranges:
            return ()
        if current_elements is None:
            current_elements = tuple()
        next_range, *other_ranges = ranges
        if len(ranges) == 1:
            return (current_elements + (k,) for k in filter(lambda k: k <= s, next_range))
        return chain.from_iterable(
            self.__impl(
                *other_ranges,
                s=s - k,
                current_elements=current_elements + (k,)
            )
            for k in filter(lambda k: k <= s, next_range)
        )

    def __iter__(self):
        return iter(self.__gen)