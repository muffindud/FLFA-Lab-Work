import re
from src.Lexer import Lexer
from src.Tokens import tokens


class Parser:
    lexer = None
    tokens = tokens

    def __init__(self, lexer):
        self.lexer = lexer

    def parse(self):
        pass


