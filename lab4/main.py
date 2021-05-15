import matplotlib.pyplot as plt 
import data as const
from functions import *

from tkinter import *
root = Tk()

varList = {
    "a1": StringVar(),
    "a2": StringVar(),
    "b1": StringVar(),
    "b2": StringVar(),
    "c1": StringVar(),
    "c2": StringVar(),
    "m1": StringVar(),
    "m2": StringVar(),
    "alpha0": StringVar(),
    "alphaN": StringVar(),
    "l": StringVar(),
    "T0": StringVar(),
    "R": StringVar(),
    "F0": StringVar(),
    "tau": StringVar(),
    "EpsTemp": StringVar(),
    "N": StringVar()
}

def create_grid(root):
    i = 0
    for var in varList.keys(): 
        label = Label(root, text=var)
        label.grid(row=i, column=0, sticky="e")
        entry = Entry(root,width=10,textvariable=varList[var])
        entry.grid(row=i, column=1)
        entry.insert(0, str(const.data[var]))
        i+=1

def check_is_num():
    for var in varList.values():
        try:
            float(var.get())
        except ValueError:
            return False
    return True    


def clear_graphs(): 
    const.res['x'].clear()
    const.res['T'].clear()

def start_work(Event):
    clear_graphs()
    if not check_is_num():
        print("WARNING NOT DIGIT")
        return
    for var in varList.keys():
        const.data[var] = float(varList[var].get())
    calculate()

    fig, (first_graph, second_graph) = plt.subplots(nrows=1, ncols=2)
    t = len(res['T']) - 1
    N = int(data['N'])
    h = data['l'] / N

    NCut = N
    resCut = {
        'x': res['x'][0:NCut+1],
        'T': [i[0:NCut+1] for i in res['T']]
    }

    # NCut = N//5
    # resCut = {
    #     'x': res['x'][0:NCut],
    #     'T': [i[0:NCut] for i in res['T']]
    # }


    step = 20
    for i in range(0, t+1, step):
        first_graph.plot(resCut['x'], resCut['T'][i], label = str(i) + " s")
    #first_graph.plot(res['x'], res['T'][-1], label = str(t) + " s")
    first_graph.set_xlabel("x, cm")
    first_graph.set_ylabel("T, K")
    first_graph.grid()
    first_graph.legend()

    te = list(range(t+1))
    step = 100
    for i in range(0, NCut+1, step):
        line = [j[i] for j in res['T']]
        second_graph.plot(te, line, label = "{:3.1f} sm".format(i*h))
    second_graph.set_xlabel("t, sec")
    second_graph.set_ylabel("T, K")
    second_graph.grid()
    second_graph.legend()
    
    fig.show()

if __name__ == '__main__':
    
    btn = Button(root, text="START") 
    create_grid(root)

    btn.bind("<Button-1>", start_work)       
    btn.grid(column=1, padx=10, pady=10)                          
    root.mainloop()