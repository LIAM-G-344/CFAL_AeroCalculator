#this imports all solvers
from pygasflow.solvers import normal_shockwave_solver
import matplotlib.pyplot as plt

#defines the function to return normal shock values
def normal_shockwave(x_value):
    results = normal_shockwave_solver("mu", x_value, gamma = 1.4, to_dict=True)
    return results

def normal_shock_graphs():
    x_list = []

    md = []
    pr = []
    dr = []
    tr = []
    tpr = []

    for i in range(160):
        x_list.append(i*0.05)

        normal_shock_dict = normal_shockwave(i*0.05)

        md.append(normal_shock_dict['md'])
        pr.append((normal_shock_dict['pr'])/(100))
        dr.append((normal_shock_dict['dr'])/(10))
        tr.append((normal_shock_dict['tr'])/(10))
        tpr.append(normal_shock_dict['tpr'])

    #keep mind in that the values with /100 or /10 are for some reason on a different scale
    plt.plot(x_list, md, label="Downstream Mach Number on the Shockwave")
    plt.plot(x_list, pr, label="Pressure Ratio (p2/p1) / 100")
    plt.plot(x_list, dr, label="Density Ratio (rho2/rho1) / 10")
    plt.plot(x_list, tr, label="Temperature Ratio (T2/T1) / 10")
    plt.plot(x_list, tpr, label="Total Pressure Ratio (P02/P01)")

    plt.xlabel("Upstream Mach Number")
    plt.ylabel("Ratios")
    plt.ylim(0,1.5)
    plt.xlim(1,8)
    plt.legend()
    plt.show()







