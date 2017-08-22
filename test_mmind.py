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

    def test_feedback_solved(self):
        guess = Guess(self.pattern)
        self.assertEqual(guess.feedback(), ['B', 'B', 'B', 'B'])

    def test_feedback_with_empty_pegs(self):
        guess = ['G', 'R', 'W', 'P']
        guess = Guess(guess)
        self.assertEqual(guess.feedback(), ['W', 'W', '-', '-'])

    def test_feedback_with_all_white_pegs(self):
        guess = ['B', 'Y', 'R', 'G']
        guess = Guess(guess)
        self.assertEqual(guess.feedback(), ['W', 'W', 'W', 'W'])

    def test_feedback_with_some_black_pegs(self):
        guess = ['R', 'G', 'Y', 'B']
        guess = Guess(guess)
        self.assertEqual(guess.feedback(), ['B', 'B', 'W', 'W'])


if __name__ == '__main__':
    unittest.main()
