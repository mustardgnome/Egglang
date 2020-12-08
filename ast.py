class Node(object):
    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self == other

class Block(Node):
    def __init__(self, statements):
        self.statements = statements

    def eval(self):
        return self.statements

class Statement(Node):
    def __init__(self, expr):
        self.expr = expr

    def eval(self):
        return self.expr

class Number(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class BinOp(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinOp):
    def eval(self):
        return self.left.eval() + self.right.eval()