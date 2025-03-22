class TextBuffer:
    def __init__(self, lines=None):
        self.lines = lines if lines is not None else []

    def insert(self, line, col, text):
        """Insert text at given line and column."""
        current_line = self.lines[line]
        new_line = current_line[:col] + text + current_line[col:]
        self.lines[line] = new_line

    def delete(self, line, col, length=1):
        """Delete `length` characters from given position."""
        current_line = self.lines[line]
        new_line = current_line[:col] + current_line[col + length:]
        self.lines[line] = new_line

    def insert_line(self, index, content=''):
        self.lines.insert(index, content)

    def delete_line(self, index):
        if 0 <= index < len(self.lines):
            self.lines.pop(index)

    def get_line(self, line):
        return self.lines[line]

    def get_lines(self):
        return self.lines

    def get_text(self):
        return ''.join(self.lines)

    def set_lines(self, lines):
        self.lines = lines
