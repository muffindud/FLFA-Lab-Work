from Grammar import Grammar
from FinalAutomata import FinalAutomata
from Lexer import Lexer


def main():
    nfa = FinalAutomata(['q0', 'q1', 'q2', 'q3', 'q4'],
                        ['a', 'b', 'c'],
                        'q0',
                        {
                            ('q0', 'a'): ['q1'],
                            ('q1', 'b'): ['q2', 'q3'],
                            ('q2', 'c'): ['q0'],
                            ('q3', 'a'): ['q4'],
                            ('q3', 'b'): ['q0']
                        },
                        'q4')

    g1 = Grammar(['S', 'B', 'D', 'Q'],
                 ['a', 'b', 'c', 'd'],
                 {
                     'S': ['aB', 'bB'],
                     'B': ['cD'],
                     'D': ['dQ', 'a'],
                     'Q': ['dB', 'dQ']
                 },
                 'S')

    # Task 2
    print('Task 2:')
    print('Grammar classification: ' + g1.get_classification())
    print()

    # Task 3a
    print('Task 3a:')
    g2 = nfa.to_grammar()
    print('Grammar non-terminals: ', g2.non_terminal)
    print('Grammar terminals: ', g2.terminal)
    print('Grammar start: ', g2.start)
    print('Grammar productions: ', g2.production)
    print()

    # Task 3b
    print('Task 3b:')
    print('FA1:', nfa.get_type())
    print()

    # Task 3c
    print('Task 3c:')
    dfa = nfa.to_dfa()
    print('FA2:', dfa.get_type())
    print('DFA states: ', dfa.states)
    print('DFA alphabet: ', dfa.alphabet)
    print('DFA initial state: ', dfa.initial_state)
    print('DFA transitions: ', dfa.transitions)
    print('DFA final states: ', dfa.final_states)
    print()

    # Task 3d
    # Will work only if graphviz is installed and in system path
    # Please refer to:
    # https://stackoverflow.com/questions/35064304/runtimeerror-make-sure-the-graphviz-executables-are-on-your-systems-path-aft
    nfa.show_graph('nfa')
    dfa.show_graph('dfa')


def main_2():
    program = Lexer('demo.txt')
    print(program.tokenize())


if __name__ == '__main__':
    main_2()
