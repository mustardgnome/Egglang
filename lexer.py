from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lg = LexerGenerator()

    """
    This is the acceptable tokens for the language
    """
    def add_tokens(self):
        self.lg.ignore(r"\s+")
        self.lg.add('NUMBER', r'\d+')
        self.lg.add('PLUS', r'\+')
        self.lg.add('SEMICOLON', r';')

    """
    Pretty self explanatory, just adds the tokens that we defined then builds the lexer so we can use it.
    """
    def build_lexer(self):
        self.add_tokens()
        return self.lg.build()
