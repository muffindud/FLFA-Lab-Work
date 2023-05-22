from src.Lexer import Lexer


class Parser:
    def __init__(self, path):
        program = Lexer(path)
        self.tokens = program.tokenize()
        self.index = 0

    def parse(self):
        pass

    def parse_block(self):
        pass

    def parse_assignment(self):
        pass

    def parse_expression(self):
        pass

    def parse_if(self):
        pass

    def parse_print(self):
        pass

    def show_ast(self):
        pass
