import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from math import *

# table 1
table_I = [0.5, 1, 5, 10, 50, 200, 400, 800, 1200]
table_T0 = [6700, 6790, 7150, 7270, 8010, 9185, 10010, 11140, 12010]
table_m = [0.5, 0.55, 1.7, 3.0, 11.0, 32.0, 40.0, 41.0, 39.0]

# table 2
table_T = [4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000]
table_sigma = [0.031, 0.27, 2.05, 6.06, 12.0, 19.9, 29.6, 41.1, 54.1, 67.7, 81.5]

tw = 2000
global_rp = 0
gt0 = 0

graph_I = []
graph_U = []
graph_T = []
graph_Rp = []
graph_T0 = []

def interpolate(value, table_v, table):
    end = 1
    start = 0
    i = 0
    
    while ((i < (len(table_v))) and (value > table_v[i])):
        i += 1
        end = i

    start = end - 1

    return table[start] + (table[end] - table[start]) / (table_v[end] - table_v[start]) * (value - table_v[start])

def f_integr(I, z):
    t0 = interpolate(I, table_I, table_T0)
    global gt0
    gt0 = t0
    m = interpolate(I, table_I, table_m)
    t = t0 + (tw - t0) * (z ** m)
    sigma = interpolate(t, table_T, table_sigma)

    return sigma * z

def i_integr(I):
    a = 0
    b = 1
    n = 100
    h = (b - a) / n
    s = (f_integr(I, a) + f_integr(I, b)) / 2
    x = 0

    for _ in range(n - 1):
        x = x + h
        s = s + f_integr(I, x)
    s = s * h

    return s

def Rp(le, R, I):
    return le / (2 * pi * R * R * i_integr(I))

def f(I, U, le, R, Lk, Rk):
    global global_rp
    global_rp = Rp(le, R, fabs(I))
    return (U - (Rk + global_rp) * I) / Lk

def g(I, Ck):
    return -I / Ck

def runge_kutta_I_U(I, U, le, R, Lk, hn, Rk, Ck):
    k1 = f(I, U, le, R, Lk, Rk)
    q1 = g(I, Ck)

    k2 = f(I + hn * k1 / 2, U + hn * q1 / 2, le, R, Lk, Rk)
    q2 = g(I + hn * k1 / 2, Ck)

    k3 = f(I + hn * k2 / 2, U + hn * q2 / 2, le, R, Lk, Rk)
    q3 = g(I + hn * k2 / 2, Ck)

    k4 = f(I + hn * k3, U + hn * q3, le, R, Lk, Rk)
    q4 = g(I + hn * k3, Ck)

    return I + hn * (k1 + 2 * k2 + 2 * k3 + k4) / 6,\
        U + hn * (q1 + 2 * q2 + 2 * q3 + q4) / 6

def graf():
    gridsize = (3, 2)
    fig = plt.figure(figsize=(24, 16))
    ax1 = plt.subplot2grid(gridsize, (0, 0))
    ax1.set_xlabel('$t$')
    ax1.set_ylabel('$I$')
    '''
    ax2 = plt.subplot2grid(gridsize, (0, 1))
    ax2.set_xlabel('$t$')
    ax2.set_ylabel('$U$')

    ax3 = plt.subplot2grid(gridsize, (1, 0))
    ax3.set_xlabel('$t$')
    ax3.set_ylabel('$Rp$')

    ax4 = plt.subplot2grid(gridsize, (1, 1))
    ax4.set_xlabel('$t$')
    ax4.set_ylabel('$To$')

    ax5 = plt.subplot2grid(gridsize, (2, 0))
    ax5.set_xlabel('$t$')
    ax5.set_ylabel('$I*Rp$')
    '''
    ax1.plot(graph_T, graph_I)
    '''
    ax2.plot(graph_T, graph_U)
    ax3.plot(graph_T, graph_Rp)
    ax4.plot(graph_T, graph_T0)

    #IRPgraph = [x * y for x, y in zip(graph_I, graph_Rp)]
    IRPgraph = []
    for i in range(len(graph_I)):
        if (graph_T[i] > 0.000001):
            IRPgraph.append(graph_I[i] * graph_Rp[i])
        else:
           IRPgraph.append(0) 

    ax5.plot(graph_T, IRPgraph)
    '''
    plt.show()

def main():
    R = 0.35
    le = 12
    Lk = 187 * 10**(-6)
    Ck = 268 * 10**(-6)
    Rk = 0.25 
    Uc = 1400
    I = 0
    hn = 0.000001
    t = 0

    for _ in range(700):
        I, Uc = runge_kutta_I_U(I, Uc, le, R, Lk, hn, Rk, Ck)
        t += hn
        
        graph_I.append(I)
        graph_U.append(Uc)
        graph_T.append(t)
        graph_Rp.append(global_rp)
        graph_T0.append(gt0)

    graf()

if __name__ == "__main__":
    main()