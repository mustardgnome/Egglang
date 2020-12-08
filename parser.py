from rply import ParserGenerator
import ast
from lexer import *

pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['NUMBER',
     'PLUS',
     'SEMICOLON'
    ], cache_id = "Egglang")

@pg.production("main : statements")
def main(s):
    return s[0]

@pg.production("statements : statements statement")
def statements(s):
    return ast.Block(s[0].getastlist() + [s[1]])

@pg.production("statements : statement")
def statements_statement(s):
    return ast.Block([s[0]])

@pg.production("statement : expr SEMICOLON")
def statement_expr(s):
    return ast.Statement(s[0])

@pg.production("expr : NUMBER")
def expr_number(s):
    return ast.Number(int(s[0].getstr()))

@pg.production("expr : expr PLUS expr")
def expr_binop(s):
    left = s[0]
    right = s[2]
    print(left.eval())
    print(right.eval())
    if s[1].gettokentype() == 'PLUS':
        return ast.Add(left, right)
    else:
        raise AssertionError('Oops, this should not be possible!')

parser = pg.build()

print(parser.parse(source).eval()[0].eval().eval())

