# Mastermind
# Pattern/guesses must be 4 pegs long
# Pegs are unique (no duplicates)


class Guess:

    def __init__(self, guess):

        # Check that guess has exactly 4 pegs
        if len(set(guess)) != 4:
            raise ValueError('Guess must be 4 pegs long, no duplicates')

        self.guess = guess
