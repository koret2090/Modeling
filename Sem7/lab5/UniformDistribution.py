from random import uniform

class UniformDistribution:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def generate(self):
        return uniform(self.a, self.b)
