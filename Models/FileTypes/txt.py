from Models.File.file_registry import register_file_type
from Models.File.file import File

@register_file_type('.txt')
class txtFile(File):
    
    def __init__(self, name):
        super().__init__(name, format="txt")

    def open(self) -> list[str]:
        with open(self.name, 'r') as f:
            return f.readlines()

    def save(self, lines: list[str]):
        with open(self.name, 'w') as f:
            f.writelines(lines)

