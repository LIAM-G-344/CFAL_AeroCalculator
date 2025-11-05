from pygasflow.solvers import rayleigh_solver
import matplotlib.pyplot as plt

#just a helper function
def rayleigh(x_value):
    results = rayleigh_solver("m", x_value, gamma=1.4, to_dict=True)
    return results

def rayleigh_graph():
    #list holding all x values
    x_list = []

    #makes the possible ratio y value graphs an array
    m = []
    prs = []
    drs = []
    trs = []
    tprs = []
    ttrs = []
    urs = []
    eps = []

    for i in range(100):
        #bruh
        #value at each .1 interval
        x_list.append(i*0.05)

        rayleigh_dict = rayleigh(i*0.05)

        #creates arrays for each possible graph's y values
        m.append(rayleigh_dict['m'])
        prs.append(rayleigh_dict['prs'])
        drs.append(rayleigh_dict['drs'])
        trs.append(rayleigh_dict['trs'])
        tprs.append(rayleigh_dict['tprs'])
        ttrs.append(rayleigh_dict['ttrs'])
        urs.append(rayleigh_dict['urs'])
        eps.append(rayleigh_dict['eps'])

    plt.plot(x_list, m, label="m")
    plt.plot(x_list, prs, label="prs")
    plt.plot(x_list, drs, label="drs")
    plt.plot(x_list, trs, label="trs")
    plt.plot(x_list, tprs, label="tprs")
    plt.plot(x_list, ttrs, label="ttrs")
    plt.plot(x_list, urs, label="urs")
    plt.plot(x_list, eps, label="eps")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(0,3)
    plt.legend()
    plt.show()
