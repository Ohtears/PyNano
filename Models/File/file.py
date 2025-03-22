from abc import ABC, abstractmethod

class File(ABC):

    def __init__(self, name, format, directory):
        self.name = name
        self.format = format
        self.directory = directory
        self.full_path = directory / name

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def save(self):
        pass

