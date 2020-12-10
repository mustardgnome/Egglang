class EggObject(object):
    pass

class EggNumber(EggObject):
    def __init__(self, value):
        self.value = value

    def add(self, other):
        assert isinstance(other, EggNumber)
        return EggNumber(self.value + other.value)