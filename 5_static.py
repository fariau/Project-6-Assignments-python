# 5. static variable and static method 

class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b
    
result = MathUtils.add(10,20)
print("Sum of 2 numbers are:", result)