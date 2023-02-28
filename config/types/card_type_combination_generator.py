from util.generators.constrained_product import ProductEQ, ProductLE


class CardTypeCombinationGenerator:
    __constraints = {
        'sum_eq': ProductEQ,
        'sum_le': ProductLE,
    }

    def __init__(self, card_totals, **kwargs):
        self.card_totals = card_totals
        self.call_t = 0
        self.n = 0
        for constraint, gen in CardTypeCombinationGenerator.__constraints.items():
            if (s := kwargs.pop(constraint, None)) is not None:
                self.__constraint = constraint
                self.__s = s
                self.__gen = gen
                break
        else:
            raise KeyError(f"CardTypeCombinationGenerator must contain either of: {', '.join(CardTypeCombinationGenerator.__constraints)}")

    def __call__(self):
        return self.__gen(*(range(t + 1) for t in self.card_totals.values()), s=self.__s)

    def __repr__(self):
        return f"{self.__constraint} = {self.__s}, {self.card_totals}"