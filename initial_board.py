# Maxwell Lin 46268364

import grid
import point
import spots_model
import tkinter


DEFAULT_FONT = ('Helvetica', 14)


class initial_board_setting:
    def __init__(self, rows, cols, state: spots_model.SpotsState):

        self._board_array = make_empty_board_array(rows, cols)
        self._turn_color = 'black'

        self._rows = rows
        self._cols = cols

        self._given_rows = int(rows)
        self._given_cols = int(cols)

        self._initial_board_window = tkinter.Toplevel()

        initial_board_setup_label = tkinter.Label(
            master = self._initial_board_window, text ='Please pick all the initial black pieces first, hit NEXT, then white pieces, then NEXT again',
            font = DEFAULT_FONT)

        initial_board_setup_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        button_frame = tkinter.Frame(master=self._initial_board_window)

        button_frame.grid(
            row=1, column=0, columnspan=2, padx=10, pady=10,
            sticky= tkinter.W)

        next_button = tkinter.Button(
            master = button_frame, text = 'NEXT', font = DEFAULT_FONT,
            command = self._on_next_button)

        next_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        # Board
        self._canvas = tkinter.Canvas(
            master=self._initial_board_window, width=600, height=600,
            background='#006000')

        self._canvas.grid(
            row=2, column=0, padx=10, pady=10,
            sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._canvas.update_idletasks()
        self._initial_board_window.rowconfigure(0, weight=1)
        self._initial_board_window.columnconfigure(0, weight=1)

        self._width_frac = self._canvas.winfo_width() / self._cols
        self._height_frac = self._canvas.winfo_height() / self._rows

        self._draw_board()

        self._canvas.bind('<Configure>', self._on_canvas_resized)

        # dots
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        self._state = state

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
        # It always returns pixel coordinates.  But that's okay,
        # because we can simply create a Point object and let it
        # do the appropriate conversion for us.
        grid_x, grid_y = grid.pixel_to_grid_coordinate(event.x, event.y, self._rows, self._cols, self._canvas.winfo_width(), self._canvas.winfo_height())

        if self._board_array[grid_y][grid_x] != '.':
            self._board_array[grid_y][grid_x] = '.'

        center_x_pix, center_y_pix = grid.grid_box_coordinate_to_center_in_pixel(grid_x, grid_y, self._rows, self._cols,
                                                                                 self._canvas.winfo_width(),
                                                                                 self._canvas.winfo_height())
        click_point = point.from_pixel(
            center_x_pix, center_y_pix, self._canvas.winfo_width(), self._canvas.winfo_height())

        # Ask the SpotsState object to handle the click, by either
        # adding or removing a spot.
        radius = (1 / self._cols) / 2
        if (1 / self._cols) / 2 > (1 / self._rows) / 2:
            radius = (1 / self._rows) / 2
        self._state.handle_click(click_point, radius, self._turn_color)

        # Now that a spot has either been added or removed, redraw
        # the dots.
        self.re_draw_board()

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

    def _draw_pieces(self):
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
        self._draw_pieces()


    def show(self) -> None:
        # This is how we turn control over to our dialog box and make that
        # dialog box modal.
        self._initial_board_window.grab_set()
        self._initial_board_window.wait_window()

    # The next three methods allow us to ask our dialog box, after it's
    # been dismissed, what happened.  (It's too late to ask the Entry
    # widgets themselves by then, because the window will already have
    # been destroyed.)

    def was_ok_clicked(self) -> bool:
        return self._ok_clicked

    def get_board_array(self) -> list:
        return self._board_array

    def get_turn_color(self) -> str:
        return self._turn_color

    def _on_next_button(self) -> None:
        self._ok_clicked = True
        self._board_array = self._board_array
        self._turn_color = self._turn_color
#        print(self._board_array)
        if self._turn_color == 'white':
            self._initial_board_window.destroy()
        else:
            self._turn_color = "white"



def make_empty_board_array(row:int, col:int)-> list:
    result = []
    for i in range(row):
        row_list = []
        for j in range (col):
            row_list.append('.')
        result.append(row_list)
    return result
