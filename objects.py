class EggObject(object):
    pass

"""
This is how objects (strings, ints, floats, etc.) are represented in our language. right now we just have numbers.
"""
class EggNumber(EggObject):
    def __init__(self, value):
        self.value = value

    def add(self, other):
        assert isinstance(other, EggNumber)
        return EggNumber(self.value + other.value)