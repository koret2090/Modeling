from math import ceil, sqrt

def func(x, u):
    return x ** 2  + u ** 2

# Эйлер
def euler(n, h, x, y):
    result = []
    i = 0
    while i < n:
        try:
            y += h * func(x, y)
            result.append(y)
            x += h
        except:
            result.append('too big')
            while i < n:
                result.append('null')
                i += 1

        i += 1

    return result 


# Рунге
def runge(n, h, x, y):
    result = []
    alpha = 1

    i = 0
    while i < n:
        try:
            k1 = func(x, y)
            k2 = func(x + h / 2 / alpha, y + h / 2 / alpha * k1)
            y += h * ((1 - alpha) * k1 + alpha * k2)
            result.append(y)
            x += h
        except:
            result.append('too big')
            while i < n:
                result.append('null')
                i += 1

        i += 1
    
    return result

# Пикар
def approximation1(arg):
        return arg ** 3 / 3

def approximation2(arg, approx1):
    return approx1 + arg ** 7 / 63

def approximation3(arg, approx2):
    return approx2 +  (arg ** 11) * (2 / 2079) + (arg ** 15) / 59535

def approximation4(arg, approx3):
    return approx3 + (arg ** 15)*(2 / 93555) + (arg ** 19)*(2 / 3393495) + \
    (arg ** 19)*(2 / 2488563) + (arg ** 23)*(2 / 86266215) + (arg ** 23)*(1 / 99411543) + \
             (arg ** 27)*(2 / 3341878155) + (arg ** 31)*(1 / 109876902975)

def picar(n, h, x, y0):
    result = [[y0, y0, y0, y0]]
    i = 1
    while i < n:
        x += h
        y_approx1 = approximation1(x)
        y_approx2 = approximation2(x, y_approx1)
        y_approx3 = approximation3(x, y_approx2)
        y_approx4 = approximation4(x, y_approx3)

        result.append([y_approx1, y_approx2, y_approx3, y_approx4])

        i += 1

    return result       

def task():
    h = 10 ** -5   
    x = 0
    y0 = 0
    end = 2.1

    n = int(abs(end - x) / h) + 1 # количество повторений

    x_arr = [0] * n
    for i in range(n):
        x_arr[i] = x + h * i

    y1 = euler(n, h, x, y0)
    y2 = runge(n, h, x, y0)
    y3 = picar(n, h, x, y0)

    print("|    x   |   Пикара 1    |    Пикара 2   |    Пикара 3   |    Пикара 4   |     Эйлера    |     Рунге     |")
    print("-" * 106)
    step = int(n / 100) # выводим только 100 значений в таблице 
    for i in range(0, n, step):
        try:
            print("|{:^8.5f}|{:^15.8f}|{:^15.8f}|{:^15.8f}|{:^15.8f}|{:^15.8f}|{:^15.8f}|".format\
                (x_arr[i], y3[i][0], y3[i][1], y3[i][2], y3[i][3], y1[i], y2[i]))
        except ValueError:
            print("|{:^8.5f}|{:^15.8f}|{:^15.8f}|{:^15.8f}|{:^15.8f}|{:^15.15}|{:^15.15}|".format\
                (x_arr[i], y3[i][0], y3[i][1], y3[i][2], y3[i][3], y1[i], y2[i]))
        
task()