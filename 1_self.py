# 1. using self 

class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"Student Name : {self.name}")
        print(f"Student Marks : {self.marks}")
        
Student1 = Student("Faria", 90)
Student1.display()