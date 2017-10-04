# Maxwell Lin 46268364
import tkinter

DEFAULT_FONT = ('Helvetica', 14)


class grid_setting:
    def __init__(self):
        self._grid_window = tkinter.Toplevel()

        version_label = tkinter.Label(
            master = self._grid_window, text ='How do you want the settings?                FULL VERSION',
            font = DEFAULT_FONT)

        version_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        rows_label = tkinter.Label(
            master = self._grid_window, text ='Number of Rows: ',
            font = DEFAULT_FONT)

        rows_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._rows_entry = tkinter.Entry(
            master = self._grid_window, width = 20, font = DEFAULT_FONT)

        self._rows_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        cols_label = tkinter.Label(
            master = self._grid_window, text ='Number of Cols: ',
            font = DEFAULT_FONT)

        cols_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._cols_entry = tkinter.Entry(
            master = self._grid_window, width = 20, font = DEFAULT_FONT)

        self._cols_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        color_first_label = tkinter.Label(
            master = self._grid_window, text ="Which color goes first: (Please enter 'B' or 'W') ",
            font = DEFAULT_FONT)

        color_first_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._color_first_entry = tkinter.Entry(
            master = self._grid_window, width = 20, font = DEFAULT_FONT)

        self._color_first_entry.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        rules_label = tkinter.Label(
            master = self._grid_window, text ="What are the winning conditions: (Please enter '>' or'<') ",
            font = DEFAULT_FONT)

        rules_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._rules_entry = tkinter.Entry(
            master = self._grid_window, width = 20, font = DEFAULT_FONT)

        self._rules_entry.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        rules_label = tkinter.Label(
            master = self._grid_window, text ="Please enter valid values: \n for rows and cols enter an even integer between 4 to 16 and follow rules stated for color first and game rules.",
            font = DEFAULT_FONT)

        rules_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        button_frame = tkinter.Frame(master = self._grid_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)


        # Finally, we'll initialize some attributes that will carry information
        # about the outcome of this dialog box (i.e., whether the user clicked
        # "OK" to dismiss it, and what first and last name the user specified).

        self._ok_clicked = False
        self._rows = ''
        self._cols = ''
        self._color_first = ''
        self._rules = ''

    def show(self) -> None:
        # This is how we turn control over to our dialog box and make that
        # dialog box modal.
        self._grid_window.grab_set()
        self._grid_window.wait_window()

    # The next three methods allow us to ask our dialog box, after it's
    # been dismissed, what happened.  (It's too late to ask the Entry
    # widgets themselves by then, because the window will already have
    # been destroyed.)

    def was_ok_clicked(self) -> bool:
        return self._ok_clicked

    def get_rows(self) -> str:
        return self._rows

    def get_cols(self) -> str:
        return self._cols

    def get_color_first(self) -> str:
        return self._color_first

    def get_rules(self) -> str:
        return self._rules

    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._rows = self._rows_entry.get()
        self._cols = self._cols_entry.get()
        self._color_first = self._color_first_entry.get()
        self._rules = self._rules_entry.get()
        self._grid_window.destroy()


def pixel_to_grid_coordinate(x_pixel, y_pixel, rows, cols, total_width, total_height):
    x_cor = int(x_pixel / (total_width / cols))
    y_cor = int(y_pixel / (total_height / rows))
    return x_cor, y_cor


def grid_box_coordinate_to_center_in_pixel(x_grid_cor, y_grid_cor, rows, cols, total_width, total_height):
    x_pix = x_grid_cor * (total_width / cols) + (total_width / cols / 2)
    y_pix = y_grid_cor * (total_height / rows) + (total_height / rows / 2)
    return x_pix, y_pix

