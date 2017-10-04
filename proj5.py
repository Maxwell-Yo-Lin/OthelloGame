# Maxwell Lin 46268364

import othello_user_interface
import othello_game_logic
import grid
import point
import spots_model
import tkinter
import initial_board
import pop_up

DEFAULT_FONT = ('Helvetica', 14)


class OthelloApplication:
    def __init__(self, state: spots_model.SpotsState):
        loop = True
        while loop:
            # initial rules and grid setting
            game_rules_setting = grid.grid_setting()
            game_rules_setting.show()

            try:
                self._rows = int(game_rules_setting.get_rows())
                self._cols = int(game_rules_setting.get_cols())
                self._color_first = game_rules_setting.get_color_first()
                self._rules = game_rules_setting.get_rules()

                if self._color_first == 'W' or self._color_first == 'w':
                    self._turn_color = 'white'
                else:
                    self._turn_color = 'black'

                if (4<=self._rows<=16 and self._rows%2==0) and (4<=self._cols<=16 and self._cols%2==0) and (self._color_first=='B' or self._color_first == 'W') and (self._rules == '>' or self._rules == '<'):
                    loop = False
            except:
                loop = True

    # Initial_board
        initial_board_setting = initial_board.initial_board_setting( self._rows, self._cols, state)
        initial_board_setting.show()
        self._board_array = initial_board_setting.get_board_array()
        self._white_pieces = (othello_user_interface.tile_count(self._board_array))[1]
        self._black_pieces = (othello_user_interface.tile_count(self._board_array))[0]

        if othello_user_interface.is_possible_moves(self._board_array,(self._turn_color[0]).upper()) == False:
            self._switch_turn()
            if othello_user_interface.is_possible_moves(self._board_array, (self._turn_color[0]).upper()) == False:
                if othello_user_interface.winner_is(self._board_array,self._rules) == "N" :
                    pop_up.no_winner_message()
                elif othello_user_interface.winner_is(self._board_array,self._rules) == "B" :
                    pop_up.black_is_winner_message()
                elif othello_user_interface.winner_is(self._board_array,self._rules) == "W" :
                    pop_up.white_is_winner_message()

        # Board
        self._root_window = tkinter.Tk()
        self._canvas = tkinter.Canvas(
            master=self._root_window, width=600, height=600,
            background='#006000')

        self._canvas.grid(
            row=0, column=0, padx=10, pady=10,
            sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._canvas.update_idletasks()
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        self._width_frac = self._canvas.winfo_width()/self._cols
        self._height_frac = self._canvas.winfo_height()/self._rows

        self._draw_board()

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

    #Game State
        self._game_state = othello_game_logic.gamestate(self._board_array, (self._turn_color[0]).upper())

    #Spots State
        self._state = state

    #Setting Display
        turn_label = tkinter.Label(
            master = self._root_window, text ='Turn: '+str(self._turn_color),
            font = DEFAULT_FONT)

        turn_label.grid(
            row = 2, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        black_count_label = tkinter.Label(
            master = self._root_window, text ='Black Pieces: '+str(self._black_pieces),
            font = DEFAULT_FONT)

        black_count_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        white_count_label = tkinter.Label(
            master = self._root_window, text ='White Pieces: '+str(self._white_pieces),
            font = DEFAULT_FONT)

        white_count_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

    # Game ends / no moves code:

    def _switch_turn(self) -> None:
        if self._turn_color == 'white':
            self._turn_color = 'black'
        else:
            self._turn_color = 'white'

    def _determine_game_status(self):
        if othello_user_interface.is_possible_moves(self._board_array,(self._turn_color[0]).upper()) == False:
            self._switch_turn()
            if othello_user_interface.is_possible_moves(self._board_array, (self._turn_color[0]).upper()) == False:
                if othello_user_interface.winner_is(self._board_array,self._rules) == "N" :
                    pop_up.no_winner_message()
                elif othello_user_interface.winner_is(self._board_array,self._rules) == "B" :
                    pop_up.black_is_winner_message()
                elif othello_user_interface.winner_is(self._board_array,self._rules) == "W" :
                    pop_up.white_is_winner_message()


    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        # When the canvas is clicked, tkinter generates an event.  Since
        # we've bound to this method to that event, this method will be
        # called whenever the canvas is clicked.  The event object passed
        # to this method will have two useful attributes:
        #
        # * event.x, which specifies the x-coordinate where the click
        #   occurred
        # * event.y, which specifies the y-coordinate where the click
        #   occurred
        #
        # tkinter is not aware of the concept of fractional coordinates.
        # It always returns pixel coordinates.
        grid_x, grid_y = grid.pixel_to_grid_coordinate(event.x, event.y, self._rows, self._cols, self._canvas.winfo_width(), self._canvas.winfo_height())

        result = (othello_user_interface.make_move(self._board_array, (self._turn_color[0]).upper(), str((grid_y+1))+' '+str((grid_x+1))))

        radius = (1 / self._cols) / 2
        if (1 / self._cols) / 2 > (1 / self._rows) / 2:
            radius = (1 / self._rows) / 2

        if result == 'INVALID':
            pop_up.invalid_move_message()
        else:
            self._board_array = result
            self._state.clear_all()
            for row in range(len(self._board_array)):
                for col in range(len(self._board_array[row])):
                    if self._board_array[row][col] == 'B':

                        center_x_pix, center_y_pix = grid.grid_box_coordinate_to_center_in_pixel(col, row,
                                                                                                 self._rows, self._cols,
                                                                                                 self._canvas.winfo_width(),
                                                                                                 self._canvas.winfo_height())
                        click_point = point.from_pixel(
                            center_x_pix, center_y_pix, self._canvas.winfo_width(), self._canvas.winfo_height())
                        self._state.handle_click(click_point, radius, 'black')

                    elif self._board_array[row][col] == 'W':
                        center_x_pix, center_y_pix = grid.grid_box_coordinate_to_center_in_pixel(col, row,
                                                                                                 self._rows, self._cols,
                                                                                                 self._canvas.winfo_width(),
                                                                                                 self._canvas.winfo_height())
                        click_point = point.from_pixel(
                            center_x_pix, center_y_pix, self._canvas.winfo_width(), self._canvas.winfo_height())
                        self._state.handle_click(click_point, radius, 'white')

            self._switch_turn()

        self._white_pieces = (othello_user_interface.tile_count(self._board_array))[1]
        self._black_pieces = (othello_user_interface.tile_count(self._board_array))[0]

        self.re_draw_board()

        self._determine_game_status()

    def _draw_board(self):
        self._width_frac = self._canvas.winfo_width() / self._cols
        self._height_frac = self._canvas.winfo_height() / self._rows
        # verticle
        for i in range(self._cols):
            x_pixel = self._width_frac * i
            self._canvas.create_line(x_pixel, 0, x_pixel, self._canvas.winfo_height(), fill='red')
        # horizontal
        for i in range(self._rows):
            y_pixel = self._height_frac * i
            self._canvas.create_line(0, y_pixel, self._canvas.winfo_width(), y_pixel, fill='red')

    def _draw_pieces_based_on_array(self):
        for spot in self._state.all_spots():
            center_x, center_y= spot.center().pixel(self._canvas.winfo_width(), self._canvas.winfo_height())
            color = spot.piece_color()
            color_letter = (color[0]).upper()

            grid_x, grid_y = grid.pixel_to_grid_coordinate(center_x, center_y, self._rows, self._cols, self._canvas.winfo_width(), self._canvas.winfo_height())
            if self._board_array[grid_y][grid_x] == '.':
                self._board_array[grid_y][grid_x] = color_letter

            radius_x = spot.radius_frac() * self._canvas.winfo_width()
            radius_y = spot.radius_frac() * self._canvas.winfo_height()

            self._canvas.create_oval(
                center_x - radius_x, center_y - radius_y,
                center_x + radius_x, center_y + radius_y,
                fill=color, outline='#ffff00')

    def _on_canvas_resized(self, event: tkinter.Event):
        self.re_draw_board()

    def re_draw_board(self):
        self._canvas.delete(tkinter.ALL)
        self._draw_board()
        self._draw_pieces_based_on_array()

        turn_label = tkinter.Label(
            master = self._root_window, text ='Turn: '+str(self._turn_color),
            font = DEFAULT_FONT)

        turn_label.grid(
            row = 2, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        black_count_label = tkinter.Label(
            master=self._root_window, text='Black Pieces: ' + str(self._black_pieces),
            font=DEFAULT_FONT)

        black_count_label.grid(
            row = 3, column=0, padx=10, pady=10,
            sticky=tkinter.W)

        white_count_label = tkinter.Label(
            master=self._root_window, text='White Pieces: ' + str(self._white_pieces),
            font = DEFAULT_FONT)

        white_count_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

    def start(self) -> None:
        self._root_window.mainloop()

if __name__ == '__main__':
    OthelloApplication(spots_model.SpotsState()).start()
