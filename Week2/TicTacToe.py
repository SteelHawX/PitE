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

"""Implements User Interface"""
class TicTacToeUI:
    def __init__(self):
        self.game = TicTacToeGame()
        self.row = -1
        self.column = -1

    def draw_game(self):
        for row in self.game.gameState:
            print('---------')
            line_to_print = ''
            for value in row:
                line_to_print += '|'
                line_to_print += value
                line_to_print += '|'
            print(line_to_print)
            print('---------')

    def print_whose_turn(self):
        print('Now is a player %s has a turn' % self.game.turn)

    def ask_for_coordinates(self):
        self.row = -1
        while not self.game.is_coordinate_in_row_range(self.row):
            self.row = int(input("Insert index of row (0 to 2)"))
        self.column = -1
        while not self.game.is_coordinate_in_column_range(self.column):
            self.column = int(input("Insert index of column (0 to 2)"))
        if not self.game.is_empty(self.row, self.column):
            print("This spot is already taken! Try different coordinates")
            self.ask_for_coordinates()

    def insert_value(self):
        self.game.insert_value(self.row, self.column)

    def is_game_finished(self):
        self.draw_game()
        if self.game.is_board_full():
            print("Game ends with a draw!")
            return True
        elif self.game.has_player_won():
            print("%s won the game!" % self.game.turn)
            return True
        else:
            return False

    def next_players_turn(self):
        self.game.end_players_turn()

    def run(self):
        while not self.is_game_finished():
            self.next_players_turn()
            self.draw_game()
            self.print_whose_turn()
            self.ask_for_coordinates()
            self.insert_value()

if __name__ == "__main__":
    TicTacToeUI().run()
