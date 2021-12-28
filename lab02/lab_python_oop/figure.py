from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def calcSquare(self):
        pass