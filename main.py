from Grammar import Grammar


def main():
    g = Grammar(['S', 'B', 'D', 'Q'],
                ['a', 'b', 'c', 'd'],
                {'S': ['aB', 'bB'], 'B': ['cD'], 'D': ['dQ', 'a'], 'Q': ['dB', 'dQ']},
                'S')

    # The Grammar.generate_string(n) function will generate n (default: 5)
    # strings corresponding to the specified grammar
    strings = g.generate_string()
    print('Generated strings:')
    print(strings, end='\n\n')

    # The Grammar.to_finite_automaton will convert final automaton format
    fa = g.to_finite_automaton()
    print('Generated transition:')
    print(fa.transitions, end='\n\n')

    # The FinalAutomaton.check(s) will check if the string s is derived from
    # the transition
    print('Corresponding strings:')
    for s in strings:
        print(fa.check(s))

    print()

    # Un-corresponding strings
    print('Un-corresponding:')
    print(fa.check('aa'))
    print(fa.check('mna'))
    print(fa.check('acdca'))


if __name__ == '__main__':
    main()
