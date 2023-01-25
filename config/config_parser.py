from util.constrained_product import ProductEQ, ProductGE, ProductLE


class GenericAttributeMap:
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


class CardTypeCombinationGenerator:
    __constraints = {
        'sum_eq': ProductEQ,
        'sum_ge': ProductGE,
        'sum_le': ProductLE,
    }

    def __init__(self, card_totals, **kwargs):
        if all(kwargs.get(x, None) is None for x in CardTypeCombinationGenerator.__constraints):
            raise KeyError(f"CardTypeCombinationGenerator must contain either of {', '.join(CardTypeCombinationGenerator.__constraints)}")
        self.card_totals = card_totals
        for constraint, gen in CardTypeCombinationGenerator.__constraints.items():
            if (s := kwargs.pop(constraint, None)) is not None:
                self.__constraint = constraint
                self.__s = s
                self.__gen = gen
                # self.__gen = (GenericAttributeMap(**dict(zip(self.card_totals.keys(), combination))) for combination in gen(*(range(t+1) for t in self.card_totals.values()), s=s))

    def __call__(self):
        return (GenericAttributeMap(**dict(zip(self.card_totals.keys(), combination))) for combination in self.__gen(*(range(t+1) for t in self.card_totals.values()), s=self.__s))

    def __repr__(self):
        return f"Card combinations generator with {self.__constraint} = {self.__s} and card totals {self.card_totals}"


class Config:
    def __init__(self, generators):
        self.generators = generators

