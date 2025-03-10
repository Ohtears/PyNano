from abc import ABC, abstractmethod

class File(ABC):

    def __init__(self, name, format):
        self.name = name
        self.format = format

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def save(self):
        pass

