# Maxwell Lin 46268364
import othello_game_logic
"""
def user_interface():

    othello_version()
    board_rows = get_rows()
    board_cols = get_cols()
    color_turn = get_first_color()
    game_rule = get_game_rules()
    game_state = othello_game_logic.gamestate(get_board(board_rows),color_turn)
    if is_possible_moves(game_state.give_board(), game_state.give_turn()) == False:
        game_state.switch_turn()
        if is_possible_moves(game_state.give_board(), game_state.give_turn()) == False:
            black_white = tile_count(game_state.give_board())
            display_count(black_white)
            game_state.print_board()
            print(winner_is(game_state.give_board(), game_rule))
            return
    while True:
        black_white = tile_count(game_state.give_board())
        display_count(black_white)
        game_state.print_board()
        game_state.print_turn()
        game_state.change_board(make_move(game_state.give_board(),game_state.give_turn()))
        game_state.switch_turn()

        if is_possible_moves(game_state.give_board(),game_state.give_turn())==False:
            game_state.switch_turn()
            if is_possible_moves(game_state.give_board(), game_state.give_turn()) == False:
                black_white = tile_count(game_state.give_board())
                display_count(black_white)
                game_state.print_board()
                print(winner_is(game_state.give_board(),game_rule))
                return
"""


def othello_version()->None:
    'prints the type of game, FULL or SIMPLE'
    print('FULL')

def get_rows()->str:
    'returns the rows for the board by asking for input'
    row = input("")
    return row

def get_cols()->str:
    'returns the cols for the board by asking for input'
    col = input("")
    return col

def get_first_color()->str:
    'returns the color that goes first by asking for input'
    color_first = input("")
    return color_first

def get_game_rules()->str:
    """returns the rule for the game by asking for input,
     '>' : most pieces of a certain color wins,
     '<' : least pieces of a certain color wins. """
    rules = input("")
    return rules

def get_board(rows:str) -> list:
    'returns the 2D list that represents the board, by asking for input'
    board = []
    for i in range(int(rows)):
        list = input()
        list = list.split()
        board.append(list)
    print(board)
    return board

def tile_count(board:list)->list:
    'counts the total black tiles and white tiles then returns a list expressing how many of each there are; [black,white]'
    black =0
    white = 0
    for rows in board:
        for cols in rows:
            if cols == "B":
                black +=1
            elif cols == "W":
                white +=1
    return [black,white]

def display_count(BandW:list)->None:
    'prints the counts of the tiles given a list containing those numbers'
    print ("B: "+str(BandW[0])+"  W: "+str(BandW[1]))


def make_move(board:list,player_color:str,user_input:str)->list:
    'takes in the 2D list and returns a new 2D list with moves made'
    while True:
        move = user_input.split()
        # print(move)
        if check_move(move,board,player_color)[0]:

            new_board = check_move(move,board,player_color)[1]
            # print(new_board)
            return new_board
        else:
            return 'INVALID'


def check_move(move:list,board:list,player_color:str)->list:
    """Checks the move inputted on the board given the list containing the move and the board, then
    makes a new board if move is valid: returns a list of a boolean and a 2D array (new board)"""
    # check if you are making a move where there isn't a piece yet
    new_board = board
    valid_move = False
    row = int(move[0]) - 1
    col = int(move[1]) - 1
    if board[row][col] != '.':
        return [valid_move,new_board]
    #Right
    if test_right(move,board,player_color):
        valid_move = True
        new_board = move_right(move,new_board,player_color)
    #Up
    if test_up(move,board,player_color):
        valid_move = True
        new_board = move_up(move,new_board,player_color)
    #Down
    if test_down(move,board,player_color):
        valid_move = True
        new_board = move_down(move,new_board,player_color)
    #left
    if test_left(move,board,player_color):
        valid_move = True
        new_board = move_left(move,new_board,player_color)
    #Up_right
    if test_up_right(move,board,player_color):
        valid_move = True
        new_board = move_up_right(move,new_board,player_color)
    #Down_right
    if test_down_right(move,board,player_color):
        valid_move = True
        new_board = move_down_right(move,new_board,player_color)
    #Down_left
    if test_down_left(move,board,player_color):
        valid_move = True
        new_board = move_down_left(move,new_board,player_color)
    #Up_left
    if test_up_left(move,board,player_color):
        valid_move = True
        new_board = move_up_left(move,new_board,player_color)
    return [valid_move,new_board]

def test_up (move:list,board:list,player_color:str)->bool:
    'test if we can flip the tiles above'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 2
    while True:
        try:
            up_color = board[row-1][col]
            end_piece = board[row-i][col]
            # checking for negative iterators
            if row-1<0 or row-i<0:
                return False
            # EX: B .
            if up_color == '.' or up_color == player_color:
                return False
            # EX: B W B
            if up_color != player_color and end_piece == player_color:
                return True
            # EX: B w .
            if up_color != player_color and end_piece == '.':
                return False
            # EX: B W W B
            if (up_color != player_color and up_color != '.') and (end_piece != player_color and end_piece != '.'):
                i += 1
        except:
            return False

def move_up(move:list,board:list,player_color:str)->list:
    'flip the tiles on above'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 1
    new_board = board
    new_board[row][col] = player_color
    while True:
        if new_board[row-i][col] != player_color:
            new_board[row-i][col] = player_color
        else:
            return new_board
        i += 1

def test_right(move:list,board:list,player_color:str)->bool:
    'test if we can flip the tiles on right'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 2
    while True:
        try:
            right_color = board[row][col+1]
            end_piece = board[row][col+i]
            # EX: B .
            if right_color == '.' or right_color == player_color:
                return False
            # EX: B W B
            if right_color != player_color and end_piece == player_color:
                return True
            # EX: B w .
            if right_color != player_color and end_piece == '.':
                return False
            # EX: B W W B
            if (right_color != player_color and right_color != '.') and (end_piece != player_color and end_piece != '.'):
                i += 1
        except:
            return False


def move_right(move:list,board:list,player_color:str)->list:
    'flip the tiles on the right'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 1
    new_board = board
    new_board[row][col] = player_color
    while True:
        if new_board[row][col+i] != player_color:
            new_board[row][col+i] = player_color
        else:
            return new_board
        i += 1

def test_down(move:list,board:list,player_color:str)->bool:
    'test if we can flip the tiles beneath'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 2
    while True:
        try:
            down_color = board[row+1][col]
            end_piece = board[row+i][col]
            # EX: B .
            if down_color == '.' or down_color == player_color:
                return False
            # EX: B W B
            if down_color != player_color and end_piece == player_color:
                return True
            # EX: B w .
            if down_color != player_color and end_piece == '.':
                return False
            # EX: B W W B
            if (down_color != player_color and down_color != '.') and (end_piece != player_color and end_piece != '.'):
                i += 1
        except:
            return False


def move_down(move:list,board:list,player_color:str)->list:
    'flip the tiles beneath'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 1
    new_board = board
    new_board[row][col] = player_color
    while True:
        if new_board[row+i][col] != player_color:
            new_board[row+i][col] = player_color
        else:
            return new_board
        i += 1

def test_left (move:list,board:list,player_color:str)->bool:
    'test if we can flip the tiles to the left'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 2
    while True:
        try:
            left_color = board[row][col-1]
            end_piece = board[row][col-i]
            # checking for negative iterators
            if col-1<0 or col-i<0:
                return False
            # EX: B .
            if left_color == '.' or left_color == player_color:
                return False
            # EX: B W B
            if left_color != player_color and end_piece == player_color:
                return True
            # EX: B w .
            if left_color != player_color and end_piece == '.':
                return False
            # EX: B W W B
            if (left_color != player_color and left_color != '.') and (end_piece != player_color and end_piece != '.'):
                i += 1
        except:
            return False

def move_left(move:list,board:list,player_color:str)->list:
    'flip the tiles on the left'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 1
    new_board = board
    new_board[row][col] = player_color
    while True:
        if new_board[row][col-i] != player_color:
            new_board[row][col-i] = player_color
        else:
            return new_board
        i += 1

def test_up_right (move:list,board:list,player_color:str)->bool:
    'test if we can flip the tiles to the top right'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 2
    while True:
        try:
            up_right_color = board[row-1][col+1]
            end_piece = board[row-i][col+i]
            # checking for negative iterators
            if row-1<0 or row-i<0:
                return False
            # EX: B .
            if up_right_color == '.' or up_right_color == player_color:
                return False
            # EX: B W B
            if up_right_color != player_color and end_piece == player_color:
                return True
            # EX: B w .
            if up_right_color != player_color and end_piece == '.':
                return False
            # EX: B W W B
            if (up_right_color != player_color and up_right_color != '.') and (end_piece != player_color and end_piece != '.'):
                i += 1
        except:
            return False

def move_up_right(move:list,board:list,player_color:str)->list:
    'flip the tiles to the top right'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 1
    new_board = board
    new_board[row][col] = player_color
    while True:
        if new_board[row-i][col+i] != player_color:
            new_board[row-i][col+i] = player_color
        else:
            return new_board
        i += 1
def test_down_right (move:list,board:list,player_color:str)->bool:
    'test if we can flip the tiles to the down right'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 2
    while True:
        try:
            down_right_color = board[row+1][col+1]
            end_piece = board[row+i][col+i]
            # EX: B .
            if down_right_color == '.' or down_right_color == player_color:
                return False
            # EX: B W B
            if down_right_color != player_color and end_piece == player_color:
                return True
            # EX: B w .
            if down_right_color != player_color and end_piece == '.':
                return False
            # EX: B W W B
            if (down_right_color != player_color and down_right_color != '.') and (end_piece != player_color and end_piece != '.'):
                i += 1
        except:
            return False

def move_down_right(move:list,board:list,player_color:str)->list:
    'flip the tiles to the down right'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 1
    new_board = board
    new_board[row][col] = player_color
    while True:
        if new_board[row+i][col+i] != player_color:
            new_board[row+i][col+i] = player_color
        else:
            return new_board
        i += 1

def test_down_left (move:list,board:list,player_color:str)->bool:
    'test if we can flip the tiles to the down left'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 2
    while True:
        try:
            down_left_color = board[row+1][col-1]
            end_piece = board[row+i][col-i]
            # checking for negative iterators
            if col-1<0 or col-i<0:
                return False
            # EX: B .
            if down_left_color == '.' or down_left_color == player_color:
                return False
            # EX: B W B
            if down_left_color != player_color and end_piece == player_color:
                return True
            # EX: B w .
            if down_left_color != player_color and end_piece == '.':
                return False
            # EX: B W W B
            if (down_left_color != player_color and down_left_color != '.') and (end_piece != player_color and end_piece != '.'):
                i += 1
        except:
            return False

def move_down_left(move:list,board:list,player_color:str)->list:
    'flip the tiles to the down left'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 1
    new_board = board
    new_board[row][col] = player_color
    while True:
        if new_board[row+i][col-i] != player_color:
            new_board[row+i][col-i] = player_color
        else:
            return new_board
        i += 1

def test_up_left (move:list,board:list,player_color:str)->bool:
    'test if we can flip the tiles to the top left'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 2
    while True:
        try:
            up_left_color = board[row-1][col-1]
            end_piece = board[row-i][col-i]
            # checking for negative iterators
            if col-1<0 or col-i<0 or row-1<0 or row-i<0:
                return False
            # EX: B .
            if up_left_color == '.' or up_left_color == player_color:
                return False
            # EX: B W B
            if up_left_color != player_color and end_piece == player_color:
                return True
            # EX: B w .
            if up_left_color != player_color and end_piece == '.':
                return False
            # EX: B W W B
            if (up_left_color != player_color and up_left_color != '.') and (end_piece != player_color and end_piece != '.'):
                i += 1
        except:
            return False

def move_up_left(move:list,board:list,player_color:str)->list:
    'flip the tiles to the top left'
    row = int(move[0])-1
    col = int(move[1])-1
    i = 1
    new_board = board
    new_board[row][col] = player_color
    while True:
        if new_board[row-i][col-i] != player_color:
            new_board[row-i][col-i] = player_color
        else:
            return new_board
        i += 1

def check_move_only (move:list,board:list,player_color:str)->bool:
    """Checks the move inputted on the board given the list containing the move and the board, then
    return a bool (True mean valif and False means invalid move"""
    # check if you are making a move where there isn't a piece yet
    valid_move = False
    row = int(move[0]) - 1
    col = int(move[1]) - 1
    if board[row][col] != '.':
        return False
    #Right
    if test_right(move,board,player_color):
        valid_move = True
    #Up
    if test_up(move,board,player_color):
        valid_move = True
    #Down
    if test_down(move,board,player_color):
        valid_move = True
    #left
    if test_left(move,board,player_color):
        valid_move = True
    #Up_right
    if test_up_right(move,board,player_color):
        valid_move = True
    #Down_right
    if test_down_right(move,board,player_color):
        valid_move = True
    #Down_left
    if test_down_left(move,board,player_color):
        valid_move = True
    #Up_left
    if test_up_left(move,board,player_color):
        valid_move = True
    return valid_move

def is_possible_moves(board:list,player_color:str)->bool:
    'check if there are any moves to make'
    are_moves = False
    possiblilities = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == '.':
                possiblilities.append([row+1, col+1])
    for i in possiblilities:
        # print(i)
        if check_move_only(i,board,player_color):
            are_moves = True
    # print (are_moves)
    return are_moves

def winner_is (board:list, rules:str)->None:
    blacks = tile_count(board)[0]
    whites = tile_count(board)[1]
    if blacks == whites:
        return ("N")
    if eval(str(blacks)+rules+str(whites)):
        return("B")
    else:
        return("W")




#board = get_board(4)
# is_possible_moves(board,'W')
#
