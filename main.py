import Grammar
# import FiniteAutomaton


def main():
    grammar = Grammar.Grammar(['S', 'B', 'D', 'Q'],
                              ['a', 'b', 'c', 'd'],
                              {'S': ['aB', 'bB'], 'B': ['cD'], 'D': ['dQ', 'a'], 'Q': ['dB', 'dQ']},
                              'S')
    strings = grammar.generate_string()
    print(strings)


if __name__ == '__main__':
    main()
