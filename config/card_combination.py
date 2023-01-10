from util.constrained_product import ProductEQ, ProductGE, ProductLE
from itertools import product


class CardTotals:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __iter__(self):
        return iter(self.__dict__)

    def items(self):
        return self.__dict__.items()

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def __getitem__(self, item):
        return self.__dict__.__getitem__(item)

    def __repr__(self):
        return self.__dict__.__repr__()


class CardCombinationGenerator:
    __constraints = {
        'sum_eq': ProductEQ,
        'sum_ge': ProductGE,
        'sum_le': ProductLE,
    }

    def __init__(self, card_totals, **kwargs):
        if all(kwargs.get(x, None) is None for x in CardCombinationGenerator.__constraints):
            raise KeyError(f"CardCombinationGenerator must contain either of {', '.join(CardCombinationGenerator.__constraints)}")
        self.card_totals = card_totals
        for constraint, gen in CardCombinationGenerator.__constraints.items():
            if (s := kwargs.pop(constraint, None)) is not None:
                self.__constraint = constraint
                self.__s = s
                self.__gen = (CardTotals(**dict(zip(self.card_totals.keys(), combination))) for combination in gen(*(range(t+1) for t in self.card_totals.values()), s=s))

    def __iter__(self):
        return iter(self.__gen)

    def __repr__(self):
        return f"Card combinations generator with {self.__constraint} = {self.__s} and card totals {self.card_totals}"


class CardCombinationGenerators:
    def __init__(self, generators):
        self.__dict__ = generators

    def __iter__(self):
        return iter(product(*(iter(gen) for gen in self.__dict__.values())))
