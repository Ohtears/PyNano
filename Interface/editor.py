from Interface.session_manager import SessionManager
from Interface.buffer import TextBuffer
from Core import __version__
from Core.history import HistoryManager
from Models.File.file import File
from Models.File.file_registry import load_all_file_types, get_file_class_by_extension

import curses
import signal
import os
import copy

signal.signal(signal.SIGTSTP, lambda signum, frame: None)

class Editor(SessionManager):
    
    #Constructor

    def __init__(self, session: SessionManager):
        self.session = session
        self.history = HistoryManager()
        self.buffer = TextBuffer()
        self.current_file = None 
        self.cursor = (0, 0)


    def open_file(self, filename: str):
        File_class = get_file_class_by_extension(filename)
        self.current_file = File_class(filename, directory=self.session.current_dir)
        self.buffer.set_lines(self.current_file.open())
        curses.wrapper(self.run_edit_loop)

    def run_edit_loop(self, stdscr):
        curses.curs_set(1)  # show cursor
        stdscr.keypad(True)
        stdscr.clear()

        while True:
            stdscr.clear()

            max_y, max_x = stdscr.getmaxyx()

            # stdscr.addstr(max_y - 2, 0, f"DEBUG: Cursor: {self.cursor} | Lines: {len(self.buffer.get_lines())}", curses.A_DIM)
            # *===== HEADER =====``
            header_text = f" PyNano Text Editor Version {__version__}".center(max_x, " ")
            stdscr.addstr(0, 0, header_text, curses.A_REVERSE)

            # *==== TEXT AREA =====
            for i, line in enumerate(self.buffer.get_lines()):
                if 1 + i >= max_y - 2:  # leave space for help bar
                    break
                stdscr.addstr(i + 1, 0, line.rstrip())

            # *===== FOOTER / HELP BAR =====
            help_text = " Ctrl+O: Save | Ctrl+X: Exit | Ctrl+U: Undo | Ctrl+R: Redo"
            stdscr.addstr(max_y - 1, 0, help_text[:max_x], curses.A_REVERSE)

            # Move cursor
            line, col = self.cursor
            stdscr.move(min(line + 1, max_y - 2), col)

            stdscr.refresh()

            key = stdscr.getch()

            # *===== KEYPRESS HANDLING =====
            if key == 24:  # Ctrl+X
                break

            elif key == 15:  # Ctrl+O
                self.save_file()

            elif key == 21:  # Ctrl+U
                self.undo()

            elif key == 18:  # Ctrl+R
                self.redo()

            elif key == curses.KEY_UP:
                self.move_cursor_up()
            elif key == curses.KEY_DOWN:
                self.move_cursor_down()
            elif key == curses.KEY_LEFT:
                self.move_cursor_left()
            elif key == curses.KEY_RIGHT:
                self.move_cursor_right()
            elif key == curses.KEY_BACKSPACE or key == 127:
                self.delete_char()
            elif key == 10:  # Enter
                self.buffer.insert_line(line + 1, "")
                self.cursor = (line + 1, 0)
            else:
                try:
                    char = chr(key)
                    self.insert_text(char)
                except ValueError:
                    pass

    
    def insert_text(self, char):
        self.history.save_state(copy.deepcopy(self.buffer.get_lines()), self.cursor)
        line, col = self.cursor
        self.buffer.insert(line, col, char)
        self.move_cursor_right()

    def delete_char(self):
        self.history.save_state(copy.deepcopy(self.buffer.get_lines()), self.cursor)
        line, col = self.cursor
        if col > 0:
            self.buffer.delete(line, col - 1)
            self.cursor = (line, col - 1)

    def move_cursor_right(self, steps=1):
        line, col = self.cursor
        text = self.buffer.get_line(line)
        col = min(col + steps, len(text))
        self.cursor = (line, col)

    def move_cursor_left(self, steps=1):
        line, col = self.cursor
        col = max(0, col - steps)
        self.cursor = (line, col)

    def move_cursor_up(self):
        line, col = self.cursor
        if line > 0:
            line -= 1
            col = min(col, len(self.buffer.get_line(line)))
        self.cursor = (line, col)

    def move_cursor_down(self):
        line, col = self.cursor
        if line < len(self.buffer.get_lines()) - 1:
            line += 1
            col = min(col, len(self.buffer.get_line(line)))
        self.cursor = (line, col)

    def save_file(self):
        if self.current_file:
            self.current_file.save(self.buffer.get_lines())

    def paste():
        pass

    def undo(self):
        self.history.undo(self)
        self._safe_cursor()

    def redo(self):
        self.history.redo(self)
        self._safe_cursor()

    def _safe_cursor(self):
        """Ensure the cursor stays within the new buffer bounds after undo/redo"""
        line, col = self.cursor
        lines = self.buffer.get_lines()
        line = min(line, len(lines) - 1)
        col = min(col, len(lines[line]))
        self.cursor = (line, col)