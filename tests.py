import unittest
from core.expression import Expression


class TestExpression(unittest.TestCase):
    def setUp(self) -> None:
        self.prefixses = ["a|b", "a|-B", "-a|-c&d>e~z"]
        self.postfixses = ["AB|", "AB-|", "A-C-D&|E>Z~"]
        self.tables = [[["00", False], ["01", True], ["10", True], ["11", True]],
                       [["00", True], ["01", False], ["10", True], ["11", True]], ]

    def test_infix_to_postfix(self):
        for i in range(len(self.prefixses)):
            self.assertEqual(Expression(self.prefixses[i]).postfix, list(self.postfixses[i]))

    def test_evaluate_table(self):
        for i in range(len(self.tables)):
            self.assertEqual(Expression(self.prefixses[i]).evaluate_table(), self.tables[i])


if __name__ == '__main__':
    unittest.main()
