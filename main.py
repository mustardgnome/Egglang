from lexer import Lexer
from parser_class import Parser

source_code = "1+1;"

lexer = Lexer().build_lexer()
token_stream = lexer.lex(source_code)


pg = Parser()
pg.parse()
parser = pg.build_parser()
parser.parse(token_stream)