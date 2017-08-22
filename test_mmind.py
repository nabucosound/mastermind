import unittest
from mmind import Guess


class MmindTestCase(unittest.TestCase):
    """Tests for the Mastermind app"""

    def setUp(self):
        self.pattern = ['R', 'G', 'B', 'Y']

    def test_invalid_guess_length(self):
        guess = ['R', 'G']
        self.assertRaises(ValueError, Guess, guess)

    def test_guess_with_duplicates(self):
        guess = ['R', 'R', 'R', 'R']
        self.assertRaises(ValueError, Guess, guess)

    def test_invalid_peg_colors(self):
        guess = ['I', 'N', 'V', 'A']
        self.assertRaises(ValueError, Guess, guess)


if __name__ == '__main__':
    unittest.main()
