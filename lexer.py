from rply import LexerGenerator

lg = LexerGenerator()
lg.ignore(r"\s+")
lg.add('NUMBER', r'\d+')
lg.add('PLUS', r'\+')
lg.add('SEMICOLON', r';')
lexer = lg.build()

source = lexer.lex('1+1;')
