# 8. the super() function 

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with the name: {self.name}")
        
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher teaches: {self.subject}")
        
Teacher1 = Teacher("Faria Usman", "GIAIC Python course") 