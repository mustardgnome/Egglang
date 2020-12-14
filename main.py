from lexer import Lexer
from parser_class import Parser
from compiler import Compiler
from interpreter import Interpreter
source_code = "1+1;"


"""
This is the entire process of our interpreter broken up by whitespace so you can see how
each part works.
"""
def interpret(source_code):
    lexer = Lexer().build_lexer()
    token_stream = lexer.lex(source_code)

    pg = Parser()
    pg.parse()
    parser = pg.build_parser()
    ast = parser.parse(token_stream)

    compiler = Compiler()
    bc = compiler.compile(ast)

    interpreter = Interpreter(bc)
    interpreter.interpret()

interpret(source_code)