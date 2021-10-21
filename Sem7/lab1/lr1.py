import matplotlib.pyplot as plt
from math import factorial, sqrt, exp
from scipy.stats import poisson
import numpy as np


def uniform_distribution(a, b, x):
    if (x < a):
        return 0
    elif (x >= b):
        return 1
    else:
        return (x - a) / (b - a)


def uniform_density(a, b, x):
    if (a <= x <= b):
        return 1 / (b - a)
    else:
        return 0


def poisson_distribution(x, mu):
    return poisson(mu).cdf(x)


def poisson_density(x, mu):
    return poisson(mu).pmf(x)


def draw_graphics(x, y_function, y_density, name):
    fig, axs = plt.subplots(2, figsize=(8, 6))

    fig.suptitle(name)
    axs[0].plot(x, y_function, color='blue')
    axs[1].plot(x, y_density, color='green')

    axs[0].set_xlabel('x')
    axs[0].set_ylabel('F(x)')

    axs[1].set_xlabel('x')
    axs[1].set_ylabel('f(x)')

    axs[0].grid(True)
    axs[1].grid(True)
    plt.show()


def main():
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    
    delta = b - a
    x = np.arange(a - delta / 2, b + delta / 2, 0.001)
    
    y_function = [uniform_distribution(a, b, _x) for _x in x]
    y_density = [uniform_density(a, b, _x) for _x in x]
    draw_graphics(x, y_function, y_density, 'Равномерное распределение')

    mu = float(input("Input mu: "))    
    x = np.arange(-1, 20)
    y_function = poisson_distribution(x, mu)
    y_density = poisson_density(x, mu)

    draw_graphics(x, y_function, y_density, 'Пуассоновское распределение')


if __name__ == '__main__':
    main()