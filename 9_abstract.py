# 9. abstract classes and methods

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectuangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
        
    def area(self):
        return self.lenght * self.width
    
rect = Rectuangle(5,6)
print("Area of rectuangle:", rect.area())