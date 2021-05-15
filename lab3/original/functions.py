from data import *
import numpy as np


def updateGlobalVars():
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
    global epsTemp
    epsTemp = data['EpsTemp']
    global epsBalance
    epsBalance = data['EpsBalance']
    global coefRelax
    coefRelax = data['CoefRelax']
    global TStart
    TStart = data['TStart']
    global N
    N = int(data['N'])
    global h
    h = l / N

    global TRelax
    TRelax = [TStart for i in range(N+1)]
    global T
    T = [TStart for i in range(N+1)]

    global eps
    eps = [0 for i in range(N+1)]
    global eta
    eta = [0 for i in range(N+1)]

def interpolate(tableX, tableY, x):
    interpolateIndexFound = False
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    y = 0
    for i in range(len(tableX) - 1):
        if (tableX[i] <= x and tableX[i + 1] >= x):
            y1 = tableY[i]
            y2 = tableY[i + 1]
            x1 = tableX[i]
            x2 = tableX[i + 1]
            interpolateIndexFound = True
    if (interpolateIndexFound):
        y = y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)
    else:
        if (x < tableX[0]):
            y = tableY[0]
        if (x > tableX[-1]):
            y = tableY[-1]
            
    return y

def integrand_func(i):
    return k(i) * (T[i]**4 - T0**4)

def integrateSimpson():
    # Берётся шаг интегрирования 2h. Предполагается, что N - чётное
    result = 0
    for i in range(N//2):
        result += h / 3 * (integrand_func(2*i) + 4 * integrand_func(2*i+1) + integrand_func(2*(i+1)))
    return result

def lamb(n):
    return interpolate(T_lamb[0], T_lamb[1], TRelax[n])

def k(n):
    return interpolate(T_k[0], T_k[1], TRelax[n])

def f(n):
    return -4 * k(n) * np * np * sigma * (TRelax[n]**4 - T0**4)

def A(n): 
    return (lamb(n) + lamb(n-1)) / 2 / h

def C(n):
    return (lamb(n) + lamb(n+1)) / 2 / h

def B(n):
    return A(n) + C(n)

def D(n):
    return f(n) * h

def iterationExitTemperature():
    for i in range(N+1):
        x = abs((T[i] - TRelax[i]) / T[i])
        if x > epsTemp:
            return True
    return False

def iterationExitEnergyBalance():
    for i in range(N+1):
        f1 = F0 - alpha * (T[N] - T0)
        f2 = 4 * np * np * sigma * integrateSimpson()
        x = abs((f1 - f2) / f1)
        if x > epsBalance:
            return True
    return False

def calculate():
    updateGlobalVars()
    flag = True
    while (iterationExitTemperature() and iterationExitEnergyBalance()
          or flag):
        flag = False
        for i in range(N+1):
            TRelax[i] = TRelax[i] + coefRelax * (T[i] - TRelax[i])
        
        K0 = (lamb(0) + lamb(1)) / 2
        M0 = -K0
        P0 = h*F0 + h*h/4 * (3*f(0) + f(1))/2

        KN = -(lamb(N-1) + lamb(N)) / 2
        MN = h*alpha - KN
        PN = h*alpha*T0 + h*h/4 * (3*f(N) + f(N-1))/2

        eps[1] = -M0/K0
        eta[1] = P0/K0

        for i in range(2, N+1):
            eps[i] = C(i-1) / (B(i-1) - A(i-1) * eps[i-1])
            eta[i] = (D(i-1) + A(i-1) * eta[i-1]) / (B(i-1) - A(i-1) * eps[i-1])

        T[N] = (PN - KN*eta[N]) / (MN + KN*eps[N])
        for i in range(N-1, -1, -1):
            T[i] = eps[i+1] * T[i+1] + eta[i+1]

    graph['x'] = [i*h for i in range(N+1)]
    graph['T'] = T[:]

    f1 = F0 - alpha * (T[N] - T0)
    f2 = 4 * np * np * sigma * integrateSimpson()
    x = abs((f1 - f2) / f1)
    print(f1, f2)