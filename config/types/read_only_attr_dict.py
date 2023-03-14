class ReadOnlyAttrDict:
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