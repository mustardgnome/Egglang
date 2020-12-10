from bytecode import ByteCode, RETURN


class CompilerContext(object):

    def __init__(self):
        self.data = []
        self.constants = []

    def new_const(self, v):
        self.constants.append(v)
        return len(self.constants) - 1

    def emit(self, bc, arg=0):
        print(bc)
        self.data.append(chr(bc))
        self.data.append(chr(arg))

    def create_bytecode(self):
        print(self.data)
        return ByteCode(
            "".join(self.data),
            self.constants[:],
        )


class Compiler(object):

    def __init__(self):
        self.ctx = CompilerContext()

    def compile(self, ast):
        self.ctx.data = []
        ast.compile(self.ctx)
        self.ctx.emit(RETURN, 0)
        return self.ctx.create_bytecode()

def compile_ast(ast):
    return Compiler().compile(ast)