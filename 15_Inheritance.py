# 15. Method Resolution Order (MRO) and Diamond Inheritance

class A:
    def show(self):
        return "Show from A"

class B(A):
    def show(self):
        return "Show from B"

class C(A):
    def show(self):
        return "Show from C"

class D(B, C):
    pass


d = D()
print(d.show()) 

print(D.__mro__)
