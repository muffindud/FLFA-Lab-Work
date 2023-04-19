import unittest
from Grammar import Grammar


class TestGrammar(unittest.TestCase):
    def test_epsilon_elimination(self):
        grammar1 = Grammar(
            ['S', 'A', 'B', 'C', 'D'],
            ['a', 'b'],
            {
                'S': ['bA', 'BC'],
                'A': ['a', 'aS', 'bAaAb'],
                'B': ['A', 'bS', 'aAa'],
                'C': ['', 'AB'],
                'D': ['AB']
            },
            'S',
            sort=False
        )

        vn, vt, prod, start = grammar1.non_terminal, grammar1.terminal, grammar1.production, grammar1.start
        prod, vn = grammar1._Grammar__eliminate_epsilon(prod, vn)

        self.assertEqual(
            prod,
            {
                'S': ['bA', 'BC', 'B'],
                'A': ['a', 'aS', 'bAaAb'],
                'B': ['A', 'bS', 'aAa'],
                'C': ['AB'],
                'D': ['AB']
            }
        )

        self.assertEqual(
            vn,
            ['S', 'A', 'B', 'C', 'D']
        )

    def test_renaming_elimination(self):
        grammar1 = Grammar(
            ['S', 'A', 'B', 'C', 'D'],
            ['a', 'b'],
            {
                'S': ['bA', 'BC'],
                'A': ['a', 'aS', 'bAaAb'],
                'B': ['A', 'bS', 'aAa'],
                'C': ['', 'AB'],
                'D': ['AB']
            },
            'S',
            sort=False
        )

        vn, vt, prod, start = grammar1.non_terminal, grammar1.terminal, grammar1.production, grammar1.start
        prod, vn = grammar1._Grammar__eliminate_renaming(prod, vn)

        self.assertEqual(
            prod,
            {
                'S': ['bA', 'BC'],
                'A': ['a', 'aS', 'bAaAb'],
                'B': ['bS', 'aAa', 'a', 'aS', 'bAaAb'],
                'C': ['', 'AB'],
                'D': ['AB']
            }
        )

    def test_inaccessible_elimination(self):
        grammar1 = Grammar(
            ['S', 'A', 'B', 'C', 'D'],
            ['a', 'b'],
            {
                'S': ['bA', 'BC'],
                'A': ['a', 'aS', 'bAaAb'],
                'B': ['A', 'bS', 'aAa'],
                'C': ['', 'AB'],
                'D': ['AB']
            },
            'S',
            sort=False
        )

        vn, vt, prod, start = grammar1.non_terminal, grammar1.terminal, grammar1.production, grammar1.start
        prod, vn = grammar1._Grammar__eliminate_inaccessible(start, prod, vn)

        self.assertEqual(
            prod,
            {
                'S': ['bA', 'BC'],
                'A': ['a', 'aS', 'bAaAb'],
                'B': ['A', 'bS', 'aAa'],
                'C': ['', 'AB']
            }
        )

        self.assertEqual(
            vn,
            ['S', 'A', 'B', 'C']
        )

    def __test_to_cnf(self):
        grammar1 = Grammar(
            ['S', 'A', 'B', 'C', 'D'],
            ['a', 'b'],
            {
                'S': ['bA', 'BC'],
                'A': ['a', 'aS', 'bAaAb'],
                'B': ['A', 'bS', 'aAa'],
                'C': ['', 'AB'],
                'D': ['AB']
            },
            'S',
            sort=False
        )

        cnf = grammar1.to_cnf()

        self.assertEqual(
            cnf.production,
            {

            }
        )
