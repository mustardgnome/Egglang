from rply import ParserGenerator
import ast

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names, accepted by the parser.
            ['NUMBER',
             'PLUS',
             'SEMICOLON'
            ], precedence=[
        ('left', ['PLUS'])
    ],cache_id = "Egglang")

    def parse(self):
        @self.pg.production("main : statements")
        def main(s):
            return s[0]

        @self.pg.production("statements : statements statement")
        def statements(s):
            return ast.Block(s[0].getastlist() + [s[1]])

        @self.pg.production("statements : statement")
        def statements_statement(s):
            return ast.Block([s[0]])

        @self.pg.production("statement : expr SEMICOLON")
        def statement_expr(s):
            return ast.Statement(s[0])

        @self.pg.production("expr : NUMBER")
        def expr_number(s):
            return ast.Number(int(s[0].getstr()))

        @self.pg.production("expr : expr PLUS expr")
        def expr_binop(s):
            left = s[0]
            right = s[2]
            return ast.BinOp(s[1].getstr(), left, right)

    def build_parser(self):
        return self.pg.build()

