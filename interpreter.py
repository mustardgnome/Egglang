from lexer import Lexer
from parser_class import Parser
from compiler import Compiler
from bytecode import bytecodes

class Interpreter(object):
    def __init__(self, bc):
        self.bc = bc
        self.bytecode = self.bc.code
        self.constants = self.bc.constants
        self.call_stack = []

    """
    We need to keep track of where we are in the bytecode, so we just have a while loop here that loops through it.
    If we had for loops and while loops in our language, this would make more sense as we'd be using JUMP instructions to get around.
    """
    def interpret(self):
        pc = 0
        while pc < len(self.bytecode):
            opcode = self.bytecode[pc]
            opname = bytecodes[ord(opcode)]
            print(opname)
            pc = getattr(self, opname)(pc)

    """
    gets the argument by adding one since we send in the instruction and argument location in pairs.
    it then just adds the argument to the call stack
    """
    def LOAD_CONST(self,pc):
        arg = ord(self.bytecode[pc+1])
        self.call_stack.append(self.constants[arg])
        return pc + 2

    """
    Pretty simple, just pops what we just put onto the stack and adds them together.
    our number object has all of these add, subtract, etc methods attached to it
    """
    def BINARY_ADD(self, pc):
        right = self.call_stack.pop()
        left = self.call_stack.pop()
        self.call_stack.append(left.add(right))
        print(self.call_stack)
        return pc+2

    """
    POP_TOP just pops the top most item of the stack.
    Since we have no variables or a print method, theres really nothing to show what this does,
    so I just threw a print method in here so you can kind of see whats going on
    """
    def POP_TOP(self, pc):
        number = self.call_stack.pop()
        print(number.value)
        return pc+2

