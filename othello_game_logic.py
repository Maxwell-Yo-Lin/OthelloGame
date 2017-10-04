# Maxwell Lin 46268364

class gamestate:

    def __init__(self,list_2d,turn):
        self._board = list_2d
        self._turn = turn

    def print_board(self):
        for rows in self._board:
            row = []
            for cols in rows:
                row.append(cols)
            print(' '.join(row))

    def print_turn(self):
        print ('TURN: '+self._turn)

    def switch_turn(self):
        if self._turn == 'B':
            self._turn = 'W'
        else:
            self._turn = 'B'

    def give_gamestate(self):
        return [self._board, self._turn]

    def give_board(self):
        return self._board

    def give_turn(self):
        return self._turn

    def change_board(self,list_2d):
        self._board = list_2d

