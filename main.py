from Grammar import Grammar


def main():
    g = Grammar(['S', 'B', 'D', 'Q'],
                ['a', 'b', 'c', 'd'],
                {'S': ['aB', 'bB'], 'B': ['cD'], 'D': ['dQ', 'a'], 'Q': ['dB', 'dQ']},
                'S')
    fa = g.to_finite_automaton()

    strings = g.generate_string()
    print(strings)


if __name__ == '__main__':
    main()
