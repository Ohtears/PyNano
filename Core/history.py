from collections import deque
import copy

class Memento:
    def __init__(self, lines, cursor):
        self.lines_snapshot = copy.deepcopy(lines) # deep copy
        self.cursor_position = cursor # for saving cursor's position in redos
    
class HistoryManager:
    def __init__(self, max_depth=100):
        self.undo_stack = deque(maxlen=max_depth)
        self.redo_stack = deque(maxlen=max_depth)

    def save_state(self, lines, cursor):
        self.undo_stack.append(Memento(lines, cursor))
        self.redo_stack.clear()

    def undo(self, editor):
        if self.undo_stack:
            self.redo_stack.append(Memento(editor.buffer.get_lines(), editor.cursor))
            memento = self.undo_stack.pop()
            editor.buffer.set_lines(memento.lines_snapshot)
            editor.cursor = memento.cursor_position

    def redo(self, editor):
        if self.redo_stack:
            self.undo_stack.append(Memento(editor.buffer.get_lines(), editor.cursor))
            memento = self.redo_stack.pop()
            editor.buffer.set_lines(memento.lines_snapshot)
            editor.cursor = memento.cursor_position
