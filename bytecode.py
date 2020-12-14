"""
these are the bytecode instructions that we will be using and converting our code into
"""
bytecodes = [
    'LOAD_CONST',
    'POP_TOP',
    'BINARY_ADD',
    'RETURN'
]

"""
creates an global variable thats the index for that said instruction
"""
for i, bytecode in enumerate(bytecodes):
    globals()[bytecode] = i

"""
this is for the binary operation as there could be different operations being used
"""
BINOP = {
    '+': globals()["BINARY_ADD"]
}

"""
the bytecode object
"""
class ByteCode(object):
    def __init__(self, code, constants):
        self.code = code
        self.constants = constants