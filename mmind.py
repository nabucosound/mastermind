# Mastermind
# Pattern/guesses must be 4 pegs long
# Pegs are unique (no duplicates)


class Guess:

    def __init__(self, guess):
        # Red, Green, Blue, Yellow, White, Pink
        self.colors = ['R', 'G', 'B', 'Y', 'W', 'P']

        # Codemaker pattern
        self.pattern = ['R', 'G', 'B', 'Y']

        # Check that guess has exactly 4 pegs and no duplicate
        # colors exist (pegs are unique)
        if len(set(guess)) != 4:
            raise ValueError('Guess must be 4 pegs long, no duplicates')

        # Check for invalid pegs
        if not set(guess).issubset(self.colors):
            raise ValueError('Valid colors: {}'.format(' '.join(self.colors)))

        self.guess = guess

    def feedback(self):
        feedback = []

        # Build feedback
        for idx, val in enumerate(self.guess):
            if val in self.pattern:
                if self.pattern[idx] == val:
                    feedback.append('B')  # Matches color and position!
                else:
                    feedback.append('W')  # Matches color only
            else:
                feedback.append('-')  # Peg not used in codebreaker pattern

        # Sort items by black, white and empty values,
        # to obfuscate feedback for the codebreaker
        sorted(feedback, key=['B', 'W', '-'].index)

        return feedback
