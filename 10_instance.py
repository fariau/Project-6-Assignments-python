# 10. instance method 

class Dog:
    def __init__(self, name , breed):
        self.name = name
        self.breed = breed
        
    def brak(self):
        print(f"{self.name} says: woof woof!")
        
dog1 = Dog("BUDDY", "Aidi")
dog1.brak()