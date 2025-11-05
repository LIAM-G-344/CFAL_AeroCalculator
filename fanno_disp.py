#this imports all solvers
from pygasflow.solvers import (
    isentropic_solver,
    normal_shockwave_solver,
    oblique_shockwave_solver,
    conical_shockwave_solver,
    fanno_solver,
    gas_solver,
    rayleigh_solver
)
import matplotlib.pyplot as plt

def fanno(x_value):
    results = fanno_solver("m" ,x_value, gamma = 1.4, to_dict=True)
    return results

def fanno_graph():
    prs = []
    drs = []
    trs = []
    tprs = []
    urs = []
    fps = []
    eps = []

    x_list = []

    for i in range(100):
        x_list.append(i*0.05)

        fanno_dict = fanno(i*0.05)

        prs.append(fanno_dict['prs'])
        drs.append(fanno_dict['drs'])
        trs.append(fanno_dict['drs'])
        tprs.append(fanno_dict['tprs'])
        urs.append(fanno_dict['urs'])
        fps.append(fanno_dict['fps'])
        eps.append(fanno_dict['eps'])

    plt.plot(x_list, prs, label="prs")
    plt.plot(x_list, drs, label="drs")
    plt.plot(x_list, trs, label="trs")
    plt.plot(x_list, tprs, label="tprs")
    plt.plot(x_list, urs, label="urs")
    plt.plot(x_list, fps, label="fps")
    plt.plot(x_list, eps, label="eps")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(0,5)
    plt.ylim(0,3)
    plt.legend()
    plt.show()
