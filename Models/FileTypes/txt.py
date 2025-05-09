from Models.File.file_registry import register_file_type
from Models.File.file import File

@register_file_type('.txt')
class txtFile(File):
    
    def __init__(self, name, directory):
        super().__init__(name, format="txt", directory=directory)

    def open(self) -> list[str]:
        if not self.full_path.exists():
            self.full_path.touch()
        with open(self.full_path, 'r') as f:
            return f.read().splitlines(keepends=False) or ['']

    def save(self, lines: list[str]):
        with open(self.full_path, 'w') as f:
            f.write('\n'.join(lines) + '\n')
