def func(x, u):
    return x ** 2  + u ** 2

# Эйлер
def euler(h, x):
    y = 0
    x0 = h
    while (x0 < x + h / 2):
        try:
            y += h * func(x0, y)
            x0 += h
        except:
            return 'null'
    
    return y


# Рунге
def runge(h, x):
    alpha = 1
    y = 0
    x0 = h
    while (x0 < x + h / 2):
        try:
            k1 = func(x0, y)
            k2 = func(x0 + h / 2 / alpha, y + h / 2 / alpha * k1)
            y += h * ((1 - alpha) * k1 + alpha * k2)
            x0 += h
        except:
            return 'null'
    
    return y

# Пикар
def approximation1(arg):
        return arg ** 3 / 3

def approximation2(arg):
    return approximation1(arg) + arg ** 7 / 63

def approximation3(arg):
    return approximation2(arg) + (arg ** 11) * (2 / 2079) + (arg ** 15) / 59535

def approximation4(arg):
    return approximation3(arg) + (arg ** 15)*(2 / 93555) + (arg ** 19)*(2 / 3393495) + \
    (arg ** 19)*(2 / 2488563) + (arg ** 23)*(2 / 86266215) + (arg ** 23)*(1 / 99411543) + \
             (arg ** 27)*(2 / 3341878155) + (arg ** 31)*(1 / 109876902975)

def picar(x):
    y_approx1 = approximation1(x)
    y_approx2 = approximation2(x)
    y_approx3 = approximation3(x)
    y_approx4 = approximation4(x)

    return [y_approx1, y_approx2, y_approx3, y_approx4]       

def task():
    h = 0.05   
    x = 0
    end = 2.3

    print("|   x    |   Пикара 1    |    Пикара 2   |    Пикара 3   |    Пикара 4   |     Эйлера    |     Рунге     |")
    print("-" * 106)

    while x < end:
        picar_res = picar(x)
        try:
            print("|{:^8.2f}|{:^15.2f}|{:^15.2f}|{:^15.2f}|{:^15.2f}|{:^15.2f}|{:^15.2f}|".format\
                (x, picar_res[0], picar_res[1], picar_res[2], picar_res[3], euler(10**-5, x), runge(10**-5, x)))
        except ValueError:
            print("|{:^8.2f}|{:^15.2f}|{:^15.2f}|{:^15.2f}|{:^15.2f}|{:^15.5}|{:^15.5}|".format\
                (x, picar_res[0], picar_res[1], picar_res[2], picar_res[3], euler(10**-5, x), runge(10**-5, x)))
        
        x += h
task()