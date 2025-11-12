import numpy as np
import matplotlib.pyplot as plt
from pygasflow.nozzles import (
    CD_Conical_Nozzle,
    CD_TOP_Nozzle,
    CD_Min_Length_Nozzle
)

Ri = 0.4         # inlet radius of the convergent section
Rt = 0.2         # throat radius
Re = 1.2         # exit (outlet) radius of the divergent section
Rj = 0.1         # junction radius between the convergent and divergent at
                 # the throat section. Used in the conical nozzle.
R0 = 0           # junction radius between the combustion chamber and the convergent
theta_c = 40     # half cone angle of the convergent section
theta_N = 15     # half cone angle of the divergent section
# fractional lengths. Used to construct TOP nozzles.
K = [0.6, 0.7, 0.8, 0.9, 1]

geom_type = "axisymmetric"
nozzles = []
nozzles.append(CD_Conical_Nozzle(Ri, Re, Rt, Rj, R0, theta_c=theta_c, theta_N=theta_N, geometry_type=geom_type))
for k in K:
    nozzles.append(CD_TOP_Nozzle(Ri, Rt, R0, theta_c, k, geometry_type=geom_type))

plt.figure()

for i, g in enumerate(nozzles):
    lbl = "Conical"
    if i != 0:
        lbl = "TOP: K = {}".format(K[i-1])
    x, y = g.build_geometry()
    plt.plot(x, y, label=lbl)
plt.legend()
plt.xlabel("Length")
plt.ylabel("Radius")
plt.title("Axisymmetric")
plt.minorticks_on()
plt.grid(which='major', linestyle='-', alpha=0.7)
plt.grid(which='minor', linestyle=':', alpha=0.5)
plt.axis('equal')
plt.show()

geom_type = "planar"

conical = CD_Conical_Nozzle(Ri, Re, Rt, Rj, R0, theta_c=theta_c, theta_N=theta_N, geometry_type=geom_type)

# fractional length of the TOP nozzle
K = 0.7
top = CD_TOP_Nozzle(Ri, Rt, R0, theta_c, 0.7, geometry_type=geom_type)
print(top)

# number of characteristics
n = 15
# specific heats ratio
gamma = 1.4

moc = CD_Min_Length_Nozzle(Ri, Re, Rt, Rj, R0, theta_c, n, gamma)

x1, y1 = conical.build_geometry()
x2, y2 = top.build_geometry()
x3, y3 = moc.build_geometry()
plt.figure()
plt.plot(x1, y1, label="conical")
plt.plot(x2, y2, label="TOP: K = {}".format(top.fractional_length))
plt.plot(x3, y3, label="MOC")
plt.legend()
plt.xlabel("Length")
plt.ylabel("Half Height")
plt.title("Planar")
plt.minorticks_on()
plt.grid(which='major', linestyle='-', alpha=0.7)
plt.grid(which='minor', linestyle=':', alpha=0.5)
plt.axis('equal')
plt.show()