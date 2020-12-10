from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lg = LexerGenerator()

    def add_tokens(self):
        self.lg.ignore(r"\s+")
        self.lg.add('NUMBER', r'\d+')
        self.lg.add('PLUS', r'\+')
        self.lg.add('SEMICOLON', r';')

    def build_lexer(self):
        self.add_tokens()
        return self.lg.build()
