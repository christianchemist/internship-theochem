import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from sympy import plot
from chain_coupling import intensities, plot_energy_intensity
from ssh_tools import plot_energy


# def helix_curve(t, r=1, h=1):
#     """Simple WIP helix function"""
#     vectorpos = np.array([r * np.cos(2*np.pi*t), r * np.sin(2*np.pi*t), h * t])
#     return vectorpos

# windings = np.arange(0, 10, 0.01)
# helix_points = np.array([helix_curve(t) for t in windings])
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(helix_points[:, 0], helix_points[:, 1], helix_points[:, 2])
# plt.show()

# energies = np.array([3.822, 3.999, 4.552, 4.805, 4.986, 4.991, 5.062, 5.086, 5.142, 5.188, 5.288, 5.330, 5.338, 5.369, 5.400, 5.428, 5.470, 5.489, 5.509, 5.555])
# plot_energy(energies)

lcmo_spec = np.load("/home/praktikum/Chris/code/data/testdata/lcmo_spec.npy")
plot_energy_intensity(lcmo_spec[:, 0], lcmo_spec[:, 1], mode="delta", sigma=0.001)