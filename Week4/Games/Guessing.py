import gameuibase as guib
import random

"""Implements game logic"""
class GuessingGame:
    maximum_number_of_guesses = 14

    def __init__(self):
        self.number = random.randint(1, 101)
        self.guess = 0
        self.number_of_guesses = 0


    """Save user guess"""
    def insert_value(self, guess):
        self.guess = guess

    """Increments number of guesses value"""
    def increase_number_of_guesses(self):
        self.number_of_guesses += 1

    """Check if player won game"""
    def has_player_won(self):
        return self.guess == self.number

    """Check if player can guess again"""
    def can_player_guess_again(self):
        return self.number_of_guesses < GuessingGame.maximum_number_of_guesses

    """Check if guessed number is smaller than the actual number"""
    def is_guess_smaller(self):
        return self.guess < self.number

    """Check if guessed number is bigger than the actual number"""
    def is_guess_bigger(self):
        return self.guess > self.number


class GuessingGameUI(guib.GameUIBase):
    def __init__(self):
        self._game = GuessingGame()
        # 0 - start of the game
        # 1 - waiting for input
        # 2 - validation failed
        # 3 - value inserted
        # 4 - player won
        # 5 - player lost
        self._game_state = 0

    @staticmethod
    def name():
        return "Simple game of guessing"

    @staticmethod
    def players():
        return 1

    def initial_message(self):
        output = "I welcome you to guessing game.\n Computer drew a number, try to guess it!\n\n"
        self._game_state = 1
        return output

    def state_of_the_game(self):
        if self._game_state == 1:
            output = "Please enter number(1-100) "
        elif self._game_state == 2:
            output = "You passed invalid arguments! Try again.\n\n"
        elif self._game_state == 3:
            output = "You guessed number"
            if self._game.is_guess_smaller():
                output += " smaller than"
            elif self._game.is_guess_bigger():
                output += " bigger than"
            else:
                output += " equal to"
            output += " an actual number"
        elif self._game_state == 4:
            output = "You won!\n\n"
        elif self._game_state == 5:
            output = "Unfortunately you lost :(\n\n"
        else:
            raise ValueError
        return output

    @staticmethod
    def string_to_input(string):
        return int(string)

    def string_is_valid(self, string):
        if string.isdecimal():
            return True
        else:
            self._game_state = 2
            return False

    def input_values_valid(self, input_values):
        if input_values in range(1, 101):
            return True
        else:
            self._game_state = 2
            return False

    def insert_values(self, input_values):
        self._game.insert_value(input_values)
        self._game.increase_number_of_guesses()
        self._game_state = 3

    def next_turn(self):
        self._game_state = 1

    def is_finished(self):
        if self._game.has_player_won():
            self._game_state = 4
            return  True
        elif not self._game.can_player_guess_again():
            self._game_state = 5
            return True
        else:
            return False



def run_the_game():
    gg = GuessingGameUI()
    print(gg.initial_message())
    game_in_progress = True
    while game_in_progress:
        while True:
            raw_input = input(gg.state_of_the_game())
            number_input = int(raw_input)
            if gg.input_values_valid(number_input):
                break
        gg.insert_values(number_input)
        print(gg.state_of_the_game())
        if gg.is_finished():
            print(gg.state_of_the_game())
            game_in_progress = False
        gg.next_turn()


if __name__ == '__main__':
    run_the_game()




