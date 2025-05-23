# 19. callable() and __call__()


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)

print(callable(double))

result = double(10)
print(result)  
