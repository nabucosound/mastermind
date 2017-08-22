# Mastermind
# Pattern/guesses must be 4 pegs long
# Pegs are unique (no duplicates)


class Guess:

    def __init__(self, guess):
        # Red, Green, Blue, Yellow, White, Pink
        self.colors = ['R', 'G', 'B', 'Y', 'W', 'P']

        # Check that guess has exactly 4 pegs
        if len(set(guess)) != 4:
            raise ValueError('Guess must be 4 pegs long, no duplicates')

        # Check for invalid pegs
        if not set(guess).issubset(self.colors):
            raise ValueError('Valid colors: {}'.format(' '.join(self.colors)))

        self.guess = guess
