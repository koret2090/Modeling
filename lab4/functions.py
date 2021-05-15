from data import *
import numpy as np


def updateGlobalVars():
    global a1
    a1 = data['a1']
    global a2
    a2 = data['a2']
    global b1
    b1 = data['b1']
    global b2
    b2 = data['b2']
    global c1
    c1 = data['c1']
    global c2
    c2 = data['c2']
    global m1
    m1 = data['m1']
    global m2
    m2 = data['m2']
    global alpha0
    alpha0 = data['alpha0']
    global alphaN
    alphaN = data['alphaN']
    global l
    l = data['l']
    global T0
    T0 = data['T0']
    global R
    R = data['R']
    global F0
    F0 = data['F0']
    global tau
    tau = data['tau']
    global EpsTemp
    EpsTemp = data['EpsTemp']
    global N
    N = int(data['N'])
    global h
    h = l / N

    global TLast
    TLast = [0 for i in range(N+1)]
    global T
    T = [0 for i in range(N+1)]

    global eps
    eps = [0 for i in range(N+1)]
    global eta
    eta = [0 for i in range(N+1)]

# Мой вариант
def k(T):
    return a1 * (b1 + c1 * T**m1)

def c(T):
    return a2 + b2 * T**m2 - (c2 / T**2)

def alpha(x):
    d = (alphaN*l) / (alphaN-alpha0)
    c = - alpha0 * d
    return c / (x-d)

def p(x) :
    return (2/R) * alpha(x)

def f(x): 
    return (2*T0/R) * alpha(x)


def A(n):
    return tau/h * (k(TLast[n]) + k(TLast[n-1]))/2

def C(n):
    return tau/h * (k(TLast[n]) + k(TLast[n+1]))/2

def B(n):
    return A(n) + C(n) + h*c(TLast[n]) + h*tau*p(n*h)

def D(n):
    return h*tau*f(n*h) + res['T'][-1][n]*h*c(TLast[n])

def leftBoundaryCondition():
    c_plus = (c(TLast[0]) + c(TLast[1])) / 2
    k_plus = (k(TLast[0]) + k(TLast[1])) / 2
    c0 = c(TLast[0])
    
    K0 = h/8 * c_plus + h/4 * c0 + tau/h * k_plus + \
         tau * h/8 * p(h/2) + tau * h/4 * p(0)

    M0 = h/8 * c_plus - tau/h * k_plus + tau * h/8 * p(h/2)

    P0 = h/8 * c_plus * (res['T'][-1][0] + res['T'][-1][1]) + \
         h/4 * c0 * res['T'][-1][0] + F0 * tau + tau * h/8 * (3 * f(0) + f(h))

    return K0, M0, P0

def rightBoundaryCondition():
    c_minus = (c(TLast[N]) + c(TLast[N-1])) / 2
    k_minus = (k(TLast[N]) + k(TLast[N-1])) / 2
    cN = c(TLast[N])
    
    KN = h/8 * c_minus - tau/h * k_minus + tau * h/8 * p(l - h/2)

    MN = h/8 * c_minus + h/4 * cN + tau/h * k_minus + tau * alphaN + \
         tau * h/8 * p(l - h/2) + tau * h/4 * p(l)

    PN = h/8 * c_minus * (res['T'][-1][N] + res['T'][-1][N-1]) + \
         h/4 * cN * res['T'][-1][N] + tau * alphaN * T0 + tau * h/4 * (f(l) + f(l - h/2))

    return KN, MN, PN

# Винтерпумовский вариант - хуйня ебаная, она температуру с временем складывает
# def k(T):
#     return a1 * (b1 + c1 * T**m1)

# def c(T):
#     return a2 + b2 * T**m2 - (c2 / T**2)

# def alpha(x):
#     d = (alphaN*l) / (alphaN-alpha0)
#     c = - alpha0 * d
#     return c / (x-d)

# def p(x) :
#     return (2/R) * alpha(x)

# def f(x): 
#     return (2*T0/R) * alpha(x)


# def A(n):
#     return tau/h * approc_minus_half(k, TLast[n], tau)

# def C(n):
#     return tau/h * approc_plus_half(k, TLast[n], tau)

# def B(n):
#     return A(n) + C(n) + h*c(TLast[n]) + h*tau*p(n*h)

# def D(n):
#     return h*tau*f(n*h) + TLast[n]*h*c(TLast[n])

# def approc_plus_half(func, n, step):
#     return (func(n) + func(n + step)) / 2

# def approc_minus_half(func, n, step):
#     return (func(n) + func(n - step)) / 2

# def leftBoundaryCondition():
#     c_plus = approc_plus_half(c, TLast[0], tau)
#     k_plus = approc_plus_half(k, TLast[0], tau)
#     c0 = c(TLast[0])
    
#     K0 = h/8 * c_plus + h/4 * c0 + tau/h * k_plus + \
#          tau * h/8 * p(h/2) + tau * h/4 * p(0)

#     M0 = h/8 * c_plus - tau/h * k_plus + tau * h/8 * p(h/2)

#     P0 = h/8 * c_plus * (TLast[0] + TLast[1]) + \
#          h/4 * c0 * TLast[0] + F0 * tau + tau * h/8 * (3 * f(0) + f(h))

#     return K0, M0, P0

# def rightBoundaryCondition():
#     c_minus = approc_minus_half(c, TLast[N], tau)
#     k_minus = approc_minus_half(k, TLast[N], tau)
#     cN = c(TLast[N])
    
#     KN = h/8 * c_minus - tau/h * k_minus + tau * h/8 * p(l - h/2)

#     MN = h/8 * c_minus + h/4 * cN + tau/h * k_minus + tau * alphaN + \
#          tau * h/8 * p(l - h/2) + tau * h/4 * p(l)

#     PN = h/8 * c_minus * (TLast[N] + TLast[N-1]) + \
#          h/4 * cN * TLast[N] + tau * alphaN * T0 + tau * h/4 * (f(l) + f(l - h/2))

#     return KN, MN, PN

#-----------------------------------------------------
def checkTempDiff():
    for i in range(N+1):
        x = abs((res['T'][-1][i] - res['T'][-2][i]) / res['T'][-1][i])
        if x > 1e-4:
            return True
    return False

def iterationExitTemp():
    for i in range(N+1):
        x = abs((T[i] - TLast[i]) / T[i])
        if x > EpsTemp:
            return True
    return False

def calculate():
    updateGlobalVars()
    res['x'] = [i*h for i in range(N+1)]
    for i in range(N+1):
        T[i] = T0
    res['T'].append(T[:])
    flag = True

    while flag or checkTempDiff():
        flag = True
        while flag or iterationExitTemp():
            print("YES", len(res['T']))
            for i in range(N+1):
                TLast[i] = T[i]
            flag = False
            
            K0, M0, P0 = leftBoundaryCondition()
            KN, MN, PN = rightBoundaryCondition()

            eps[1] = -M0/K0
            eta[1] = P0/K0

            for i in range(2, N+1):
                eps[i] = C(i-1) / (B(i-1) - A(i-1) * eps[i-1])
                eta[i] = (D(i-1) + A(i-1) * eta[i-1]) / (B(i-1) - A(i-1) * eps[i-1])
            
            T[N] = (PN - KN*eta[N]) / (MN + KN*eps[N])
            for i in range(N-1, -1, -1):
                T[i] = eps[i+1] * T[i+1] + eta[i+1]
        
        res['T'].append(T[:])
    
            
