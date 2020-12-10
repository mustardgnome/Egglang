import bytecode
import objects

class Node(object):
    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self == other

class Block(Node):
    def __init__(self, statements):
        self.statements = statements

    def compile(self, ctx):
        for statement in self.statements:
            statement.compile(ctx)

class Statement(Node):
    def __init__(self, expr):
        self.expr = expr

    def compile(self, ctx):
        self.expr.compile(ctx)
        ctx.emit(bytecode.POP_TOP)

class Number(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

    def compile(self, ctx):
        ctx.emit(bytecode.LOAD_CONST, ctx.new_const(objects.EggNumber(self.value)))

class BinOp(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def compile(self, ctx):
        self.left.compile(ctx)
        self.right.compile(ctx)
        ctx.emit(bytecode.BINOP[self.op])
