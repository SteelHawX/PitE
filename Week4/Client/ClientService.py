

def ask_user_for_row():
    return input("Insert index of row (0 to 2)")

def ask_user_for_column():
    return input("Insert index of column (0 to 2)")

def draw_game(board):
    for row in board:
        print('---------')
        line_to_print = ''
        for value in row:
            line_to_print += '|'
            line_to_print += value
            line_to_print += '|'
        print(line_to_print)
        print('---------')

def show_info(info):
    print(info)
