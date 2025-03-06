from abc import ABC, abstractmethod

class UserInterface(ABC):

    _instance = None

    #Singleton pattern

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserInterface, cls).__new__(cls)
        return cls

    #Constructor

    def __init__(self):
        self.running = True

    @abstractmethod
    def run(self):
        pass
