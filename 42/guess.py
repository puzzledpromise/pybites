import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._answer = get_random_number()
        self._guesses = set()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        while(True):
            guess = input(f"Guess a number between {START} and {END}: ")

            if guess is None:
                print("Please enter a number")
                raise ValueError()
            try:
                guess = int(guess)
            except:
                print("Should be a number")
                raise ValueError()

            if guess > END or guess < START:
                print("Number not in range")
                raise ValueError()
            
            if guess in self._guesses:
                print("Already guessed")
                raise ValueError()

            self._guesses.add(guess)
            return guess




        

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        if guess > self._answer:
            print(f"{guess} is too high")
            return False
        elif guess < self._answer:
            print(f"{guess} is too low")
            return False

        self._win = True

        print(f"{guess} is correct!")
        return True

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while(True):
            try:
                guess = self.guess() 
                result = self._validate_guess(guess)
            except ValueError:
                continue
            
            if result:
                print(f"It took you {len(self._guesses)} guesses")
                break
            
            if len(self._guesses) == MAX_GUESSES:
                print(f"Guessed {len(self._guesses)} times, answer was {self._answer}")
                break
        


if __name__ == '__main__':
    game = Game()
    game()
