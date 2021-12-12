from numpy.random import uniform, normal, poisson
import random


class UniformDistribution:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def generate(self):
        return uniform(self.a, self.b)

class PoissonDistribution:
    def __init__(self, lyambda):
        self.lyambda = lyambda
    
    def generate(self):
        return poisson(self.lyambda)

class NormalDistribution:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def generate(self):
        return normal(self.mu, self.sigma)
