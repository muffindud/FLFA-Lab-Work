from Grammar import Grammar
from NFA import NFA


def main_1():
    g = Grammar(['S', 'B', 'D', 'Q'],
                ['a', 'b', 'c', 'd'],
                {
                    'S': ['aB', 'bB'],
                    'B': ['cD'],
                    'D': ['dQ', 'a'],
                    'Q': ['dB', 'dQ']
                },
                'S')

    # The Grammar.generate_string(n) function will generate n (default: 5)
    # strings corresponding to the specified grammar
    strings = g.generate_string()
    print('Generated strings:')
    print(strings, end='\n\n')

    # The Grammar.to_finite_automaton will convert final automaton format
    fa = g.to_nfa()
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


def main_2():
    nfa = NFA(['q0', 'q1', 'q2', 'q3', 'q4'],
              ['a', 'b', 'c'],
              'q0',
              {
                  ('q0', 'a'): ['q1'],
                  ('q1', 'b'): ['q2', 'q3'],
                  ('q2', 'c'): ['q0'],
                  ('q3', 'a'): ['q4'],
                  ('q3', 'b'): ['q0']
              },
              ['q4'])

    dfa = nfa.to_dfa()
    print(dfa.states)
    print(dfa.transitions)

    # g = fa.to_grammar()
    #
    # print(fa.transitions)
    # print(g.production)
    # print('Automata type: ' + fa.get_type())

    # nfa.show_graph()


if __name__ == '__main__':
    main_2()
