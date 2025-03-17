import unittest
from latex_tokenize import latex_tokenize


class TestLatexTokenizer(unittest.TestCase):

    def setUp(self):
        """Set up test cases."""
        # You can add any setup code here if needed
        pass

    def test_simple_parentheses(self):
        """Test expressions with simple parentheses."""
        self.assertEqual(
            latex_tokenize("()"),
            [
                {"type": "parenthesis", "value": "("},
                {"type": "parenthesis", "value": ")"},
            ],
        )

    def test_whitespace_handling(self):
        """Test tokenizer properly ignores whitespace."""
        self.assertEqual(
            latex_tokenize("     (      )    "),
            [
                {"type": "parenthesis", "value": "("},
                {"type": "parenthesis", "value": ")"},
            ],
        )
        self.assertEqual(latex_tokenize("    "), [])

    def test_basic_arithmetic(self):
        """Test basic arithmetic expressions."""
        self.assertEqual(
            latex_tokenize("1 + 2"),
            [
                {"type": "number", "value": "1"},
                {"type": "single_character_operator", "value": "+"},
                {"type": "number", "value": "2"},
            ],
        )
        self.assertEqual(
            latex_tokenize("3-4"),
            [
                {"type": "number", "value": "3"},
                {"type": "single_character_operator", "value": "-"},
                {"type": "number", "value": "4"},
            ],
        )
        self.assertEqual(
            latex_tokenize("5*6"),
            [
                {"type": "number", "value": "5"},
                {"type": "single_character_operator", "value": "*"},
                {"type": "number", "value": "6"},
            ],
        )
        self.assertEqual(
            latex_tokenize("x*6 + y/5"),
            [
                {"type": "letter", "value": "x"},
                {"type": "single_character_operator", "value": "*"},
                {"type": "number", "value": "6"},
                {"type": "single_character_operator", "value": "+"},
                {"type": "letter", "value": "y"},
                {"type": "single_character_operator", "value": "/"},
                {"type": "number", "value": "5"},
            ],
        )
        self.assertEqual(
            latex_tokenize("x*66 + y/55"),
            [
                {"type": "letter", "value": "x"},
                {"type": "single_character_operator", "value": "*"},
                {"type": "number", "value": "66"},
                {"type": "single_character_operator", "value": "+"},
                {"type": "letter", "value": "y"},
                {"type": "single_character_operator", "value": "/"},
                {"type": "number", "value": "55"},
            ],
        )

    def test_latex_symbols(self):
        """Test LaTeX symbol tokenization."""
        self.assertEqual(
            latex_tokenize(r"\cos x + \; 5"),
            [
                {"type": "single_character_symbol", "value": "\\cos"},
                {"type": "letter", "value": "x"},
                {"type": "single_character_operator", "value": "+"},
                {"type": "number", "value": "5"},
            ],
        )


if __name__ == "__main__":
    # Use TextTestRunner with increased verbosity for nicer output
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
