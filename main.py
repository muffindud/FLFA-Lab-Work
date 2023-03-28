from time import sleep
from Lexer import Lexer


def main_legal():
    program = Lexer("demo.txt")
    toks = program.tokenize()
    for t in toks:
        print(t)


def main_illegal():
    program = Lexer("illegal_demo.txt")
    toks = program.tokenize()
    for t in toks:
        print(t)


if __name__ == '__main__':
    main_legal()
    sleep(1)
    main_illegal()
