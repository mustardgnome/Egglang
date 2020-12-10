bytecodes = [
    'LOAD_CONST',
    'POP_TOP',
    'BINARY_ADD',
    'RETURN'
]


for i, bytecode in enumerate(bytecodes):
    globals()[bytecode] = i

BINOP = {
    '+': globals()["BINARY_ADD"]
}


class ByteCode(object):
    _immutable_fields_ = ['code', 'constants[*]']

    def __init__(self, code, constants):
        self.code = code
        self.constants = constants

    def dump(self):
        lines = []
        for i in range(0, len(self.code), 2):
            c = self.code[i]
            c2 = self.code[i + 1]
            lines.append(bytecodes[ord(c)] + " " + str(ord(c2)))
        return '\n'.join(lines)