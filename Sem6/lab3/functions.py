from data import *
import numpy as np


def update_vars():
    global np
    np = data['np']
    global l
    l = data['l']
    global T0
    T0 = data['T0']
    global sigma
    sigma = data['sigma']
    global F0
    F0 = data['F0']
    global alpha
    alpha = data['alpha']
    global eps_temp
    eps_temp = data['eps_temp']
    global eps_balance
    eps_balance = data['eps_balance']
    global coef_relax
    coef_relax = data['coef_relax']
    global T_start
    T_start = data['T_start']
    global N
    N = int(data['N'])
    global h
    h = l / N

    global T_relax
    T_relax = [T_start for i in range(N+1)]
    global T
    T = [T_start for i in range(N+1)]

    global eps
    eps = [0 for i in range(N+1)]
    global eta
    eta = [0 for i in range(N+1)]

def interpolate(table_x, table_y, x):
    index_flag = False
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    y = 0
    for i in range(len(table_x) - 1):
        if (table_x[i] <= x and table_x[i + 1] >= x):
            y1 = table_y[i]
            y2 = table_y[i + 1]
            x1 = table_x[i]
            x2 = table_x[i + 1]
            index_flag = True
    if (index_flag):
        y = y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)
    else:
        if (x < table_x[0]):
            y = table_y[0]
        if (x > table_x[-1]):
            y = table_y[-1]
            
    return y

def integrand_func(i):
    return k(i) * (T[i] ** 4 - T0 ** 4)

def integr_simpson():
    result = 0
    for i in range(N // 2):
        result += h / 3 * (integrand_func(2 * i) + \
            4 * integrand_func(2 * i + 1) + integrand_func(2 * (i + 1)))
    return result

def lamb(n):
    return interpolate(T_lamb[0], T_lamb[1], T_relax[n])

def k(n):
    return interpolate(T_k[0], T_k[1], T_relax[n])

def f(n):
    return -4 * k(n) * np * np * sigma * (T_relax[n] ** 4 - T0 ** 4)

def iteration_exit_temp():
    i = 0
    while i < (N + 1):
        x = abs((T[i] - T_relax[i]) / T[i])
        if x > eps_temp:
            return True
        i += 1
    
    return False

def iteration_exit_energy_balance():
    i = 0
    while i < (N + 1):
        f1 = F0 - alpha * (T[N] - T0)
        f2 = 4 * np * np * sigma * integr_simpson()
        x = abs((f1 - f2) / f1)
        if x > eps_balance:
            return True
        i += 1
    
    return False

def calculate():
    update_vars()
    flag = True
    while (iteration_exit_temp() and iteration_exit_energy_balance() or flag):
        flag = False
        for i in range(N+1):
            T_relax[i] = T_relax[i] + coef_relax * (T[i] - T_relax[i])
        
        K0 = (lamb(0) + lamb(1)) / 2
        M0 = -K0
        P0 = h * F0 + h * h / 4 * (3 * f(0) + f(1)) / 2

        KN = -(lamb(N - 1) + lamb(N)) / 2
        MN = h * alpha - KN
        PN = h * alpha * T0 + h * h /4 * (3 * f(N) + f(N - 1)) / 2

        eps[1] = -M0 / K0
        eta[1] = P0 / K0

        for i in range(2, N+1):
            eps[i] = (lamb(i - 1) + lamb(i)) \
            / (((lamb(i - 1) + lamb(i - 2)) + (lamb(i - 1) + lamb(i)) - \
            (lamb(i - 1) + lamb(i - 2))) * eps[i - 1])
            
            eta[i] = (f(i - 1) * h + (lamb(i - 1) + lamb(i - 2)) / 2 / h * eta[i - 1]) \
            / (((lamb(i - 1) + lamb(i - 2)) + (lamb(i - 1) + lamb(i)) \
            - (lamb(i - 1) + lamb(i - 2))) / 2 / h * eps[i - 1])

        T[N] = (PN - KN * eta[N]) / (MN + KN * eps[N])
        for i in range(N-1, -1, -1):
            T[i] = eps[i + 1] * T[i + 1] + eta[i + 1]

    graph['x'] = [i * h for i in range(N + 1)]
    graph['T'] =  T.copy()

    f1 = F0 - alpha * (T[N] - T0)
    f2 = 4 * np * np * sigma * integr_simpson()
    x = abs((f1 - f2) / f1)
    print(f1, f2)
    print(eps[N], eta[N])