class IdentityWithMap:

    def __init__(self, gen, map):
        self.__gen = gen
        self.__map = map

    def __iter__(self,):
        return ((x, self.__map(*x)) for x in self.__gen)
