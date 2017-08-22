import unittest


class MmindTestCase(unittest.TestCase):
    """Tests for the Mastermind app"""

    def setUp(self):
        self.pattern = ['R', 'G', 'B', 'Y']


if __name__ == '__main__':
    unittest.main()
