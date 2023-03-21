class IdentityWithMap:

    def __init__(self, gen, mapper):
        self.__gen = gen
        self.__map = mapper

    def __iter__(self,):
        return ((x, self.__map(*x)) for x in self.__gen)
