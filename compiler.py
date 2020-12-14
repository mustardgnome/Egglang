from bytecode import ByteCode


class Context(object):

    def __init__(self):
        self.data = []
        self.constants = []

    def new_const(self, v):
        self.constants.append(v)
        return len(self.constants) - 1

    """
    the emit function basically just appends the bytecode instruction and the argument to our data
    """
    def emit(self, bc, arg=0):
        print(bc)
        self.data.append(chr(bc))
        self.data.append(chr(arg))

    def create_bytecode(self):
        return ByteCode(
            self.data,
            self.constants[:]
        )

class Compiler(object):
    def __init__(self):
        self.ctx = Context()

    def compile(self, ast):
        self.ctx.data = []
        ast.compile(self.ctx)
        return self.ctx.create_bytecode()