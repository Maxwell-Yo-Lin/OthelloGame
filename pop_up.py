# Maxwell Lin 46268364
import tkinter

DEFAULT_FONT = ('Helvetica', 14)


class invalid_move_message:
    def __init__(self):
        self._message_window = tkinter.Toplevel()

        message_label = tkinter.Label(
            master = self._message_window, text ='That move was invalid, Please click again!',
            font = DEFAULT_FONT)

        message_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        button_frame = tkinter.Frame(master = self._message_window)

        button_frame.grid(
            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)


    def show(self) -> None:
        # This is how we turn control over to our dialog box and make that
        # dialog box modal.
        self._message_window.grab_set()
        self._message_window.wait_window()

    def _on_ok_button(self) -> None:
        self._message_window.destroy()

class black_is_winner_message:
    def __init__(self):
        self._message_window = tkinter.Toplevel()

        message_label = tkinter.Label(
            master = self._message_window, text ='Black color wins! (The final score is shown on the board)',
            font = DEFAULT_FONT)

        message_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        button_frame = tkinter.Frame(master = self._message_window)

        button_frame.grid(
            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)


    def show(self) -> None:
        # This is how we turn control over to our dialog box and make that
        # dialog box modal.
        self._message_window.grab_set()
        self._message_window.wait_window()

    def _on_ok_button(self) -> None:
        self._message_window.destroy()

class white_is_winner_message:
    def __init__(self):
        self._message_window = tkinter.Toplevel()

        message_label = tkinter.Label(
            master = self._message_window, text ='White color wins! (The final score is shown on the board)',
            font = DEFAULT_FONT)

        message_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        button_frame = tkinter.Frame(master = self._message_window)

        button_frame.grid(
            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)


    def show(self) -> None:
        # This is how we turn control over to our dialog box and make that
        # dialog box modal.
        self._message_window.grab_set()
        self._message_window.wait_window()

    def _on_ok_button(self) -> None:
        self._message_window.destroy()

class no_winner_message:
    def __init__(self):
        self._message_window = tkinter.Toplevel()

        message_label = tkinter.Label(
            master = self._message_window, text ='The game is a tie! (The final score is shown on the board)',
            font = DEFAULT_FONT)

        message_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        button_frame = tkinter.Frame(master = self._message_window)

        button_frame.grid(
            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)


    def show(self) -> None:
        # This is how we turn control over to our dialog box and make that
        # dialog box modal.
        self._message_window.grab_set()
        self._message_window.wait_window()

    def _on_ok_button(self) -> None:
        self._message_window.destroy()
