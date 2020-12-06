from rply import ParserGenerator
import ast

pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['NUMBER',
     'PLUS',
     'SEMICOLON'
    ], cache_id = "Egglang")
parser = pg.build()