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

#defining the function to return isentropic values
def isentropic(x_value):
    results = isentropic_solver("m", x_value, gamma=1.4, to_dict=True)
    return results

#list holding all x values
x_list = []

#makes the possible ratio y value graphs an array
pr = []
dr = []
tr = []
prs = []
drs = []
trs = []
urs = []
ars = []
ma = []
pm = []


for i in range(100):
    #bruh
    #value at each .1 interval
    x_list.append(i*0.05)
    print(x_list)

    isentropic_dict = isentropic(i*0.05)

    #creates arrays for each possible graph's y values
    pr.append(isentropic_dict['pr'])
    dr.append(isentropic_dict['dr'])
    tr.append(isentropic_dict['tr'])
    prs.append(isentropic_dict['prs'])
    drs.append(isentropic_dict['drs'])
    trs.append(isentropic_dict['trs'])
    urs.append(isentropic_dict['urs'])
    ars.append(isentropic_dict['ars'])

plt.plot(x_list, pr, label="pr")
plt.plot(x_list, dr, label="dr")
plt.plot(x_list, tr, label="tr")
plt.plot(x_list, prs, label="prs")
plt.plot(x_list, drs, label="drs")
plt.plot(x_list, trs, label="trs")
plt.plot(x_list, urs, label="urs")
plt.plot(x_list, ars, label="ars")

plt.xlabel("x")
plt.ylabel("y")
plt.ylim(0,3)
plt.legend()
plt.show()




