import gameuibase as guib
from enum import Enum


"""Implements game logic"""
class TicTacToeGame:
    def __init__(self):
        self.gameState = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.turn = 'X'

    """Returns gameState"""
    def get_board(self):
        return self.gameState

    """Inserts correct symbol into given row and column"""
    def insert_value(self, row, column):
        self.gameState[row][column] = self.turn

    """Ends players turn and commences turn of the other one"""
    def end_players_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        elif self.turn == 'O':
            self.turn = 'X'
        else:
            raise NameError(self.turn)

    """Checks if coordinate is valid(0,1 or 2"""
    def is_coordinate_in_row_range(self, coordinate):
        if coordinate in range(len(self.gameState)):
            return True
        else:
            return False

    """See above"""
    def is_coordinate_in_column_range(self, coordinate):
        if coordinate in range(len(self.gameState[0])):
            return True
        else:
            return False

    """Checks if value is equal ' ' """
    def is_empty(self, row, column):
        if self.gameState[row][column] == ' ':
            return True
        else:
            return False

    """Checks if all 9 fields are filled"""
    def is_board_full(self):
        for row in self.gameState:
            for column in row:
                if column == ' ':
                    return False
        return True

    """Checks all vertical possibilities of winning the game. Win flag is true at the beginning of the check of each
    column and changes to false only if finds "wrong" symbol(that does not belong to player that has a turn)"""
    def is_vertical_win_condition(self):
        for column in range(len(self.gameState[0])):
            win = True
            for row in range(len(self.gameState)):
                if self.gameState[row][column] is not self.turn:
                    win = False
            if win is True:
                return True
        return False

    """Checks all horizontal possibilities of winning the game. Win flag is true at the beginning of the check of each
    row and changes to false only if finds "wrong" symbol(that does not belong to player that has a turn)"""
    def is_horizontal_win_condition(self):
        for row in self.gameState:
            win = True
            for column in row:
                if column is not self.turn:
                    win = False
            if win is True:
                return True
        return False

    """Checks both diagonal possibilities of winning the game. Implementation analogical to those two above"""
    def is_diagonal_win_condition(self):
        win = True
        for row_n_column in range(len(self.gameState)):
            if self.gameState[row_n_column][row_n_column] is not self.turn:
                win = False
        if win is True:
            return True
        win = True
        for row_n_column in range(len(self.gameState)):
            if self.gameState[row_n_column][2 - row_n_column] is not self.turn:
                win = False
        if win is True:
            return True

    """Checks if any of win conditions is fulfilled"""
    def has_player_won(self):
        return self.is_horizontal_win_condition() or self.is_vertical_win_condition() or self.is_diagonal_win_condition()


class TicTacToeUI(guib.GameUIBase):
    def __init__(self):
        self._game = TicTacToeGame()
        self._row = -1
        self._column = -1
        # 0 - start of the game
        # 1 - waiting for input
        # 2 - validation failed
        # 3 - values inserted
        # 4 - game ended with a draw
        # 5 - player 1 won
        # 6 - player 2 won
        self._game_state = 0
        self._game_state_cycle_size = 4

    @staticmethod
    def name():
        return "TicTacToe"

    @staticmethod
    def players():
        return 2

    @staticmethod
    def string_to_input(string):
        return tuple(map(int, string.split(", ")))

    def string_is_valid(self, string):
        for substring in string.split(", "):
            if not substring.isdecimal():
                self._game_state = 2
                return False
        return True

    def initial_message(self):
        output = "I welcome you to the tic tac toe game.\n\n"
        output += self._draw_board()
        self._game_state = 1
        return output

    def _draw_board(self):
        output = ""
        for row in self._game.gameState:
            output += '---------\n'
            for value in row:
                output += '|'
                output += value
                output += '|'
            output += '\n'
        output += '---------\n'
        return output

    def state_of_the_game(self):
        if self._game_state == 1:
            output = "Please enter coordinates as: row, column. Remember that both variables has to have value" \
                   " of 0, 1 or 2.\n\n"
        elif self._game_state == 2:
            output = "You passed invalid arguments! Try again.\n\n"
        elif self._game_state == 3:
            output =  self._draw_board()
        elif self._game_state == 4:
            output = "Game ended with a draw!\n\n"
            output += self._draw_board()
        elif self._game_state == 5:
            output = "Player " + self._game.turn + " won!\n"
        else:
            raise ValueError
        return output

    def input_values_valid(self, input_values):
        if len(input_values) != 2:
            self._game_state = 2
            return False
        else:
            input_row = input_values[0]
            input_column = input_values[1]
        if self._game.is_coordinate_in_row_range(input_row) is True:
            if self._game.is_coordinate_in_column_range(input_column) is True:
                if self._game.is_empty(input_row, input_column) is True:
                    return True
        self._game_state = 2
        return False

    def insert_values(self, input_values):
        self._game.insert_value(input_values[0], input_values[1])
        self._game_state = 3

    def next_turn(self):
        self._game.end_players_turn()
        self._game_state = 3
        return self._game.turn

    def is_finished(self):
        if self._game.has_player_won():
            self._game_state = 5
            return True
        elif self._game.is_board_full() is True:
            self._game_state = 4
            return True
        else:
            return False


def run_the_game():
    ttt = TicTacToeUI()
    print(ttt.initial_message())
    game_in_progress = True
    while game_in_progress:
        while True:
            raw_input = input(ttt.state_of_the_game())
            true_input = tuple(map(int, raw_input.split(", ")))
            if ttt.input_values_valid(true_input):
                break
        ttt.insert_values(true_input)
        print(ttt.state_of_the_game())
        if ttt.is_finished() is True:
            print(ttt.state_of_the_game())
            game_in_progress = False
        ttt.next_turn()

if __name__ == '__main__':
    run_the_game()
