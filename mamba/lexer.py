from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add("PRINT", r"print")
        # Parenthesis
        self.lexer.add("OPEN_PAREN", r"\(")
        self.lexer.add("CLOSE_PAREN", r"\)")
        # Semi Colon
        self.lexer.add("SEMI_COLON", r"\;")
        # Operators
        self.lexer.add("PLUS", r"\+")
        self.lexer.add("MINUS", r"-")
        self.lexer.add("MUL", r"\*")
        self.lexer.add("DIV", r"/")
        # Number
        self.lexer.add("NUMBER", r"\d+")
        # Ignore spaces
        self.lexer.ignore(r"\s+")

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
