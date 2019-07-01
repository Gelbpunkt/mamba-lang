from ast import Div, Mul, Number, Print, Sub, Sum

from rply import ParserGenerator


class Parser:
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            [
                "NUMBER",
                "PRINT",
                "OPEN_PAREN",
                "CLOSE_PAREN",
                "SEMI_COLON",
                "PLUS",
                "MINUS",
                "MUL",
                "DIV",
            ],
            precedence=[("left", ["PLUS", "MINUS"]), ("left", ["MUL", "DIV"])],
        )
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production(
            "program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON"
        )
        def program(p):
            return Print(self.builder, self.module, self.printf, p[2])

        @self.pg.production("expression : expression PLUS expression")
        @self.pg.production("expression : expression MINUS expression")
        @self.pg.production("expression : expression MUL expression")
        @self.pg.production("expression : expression DIV expression")
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == "PLUS":
                return Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == "MINUS":
                return Sub(self.builder, self.module, left, right)
            elif operator.gettokentype() == "MUL":
                return Mul(self.builder, self.module, left, right)
            elif operator.gettokentype() == "DIV":
                return Div(self.builder, self.module, left, right)

        @self.pg.production("expression : NUMBER")
        def number(p):
            return Number(self.builder, self.module, p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
