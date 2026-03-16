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

energies_a_dimer = np.array([3.822, 3.999, 4.552, 4.805, 4.986, 4.991, 5.062, 5.086, 5.142, 5.188, 5.288, 5.330]) # 5.338, 5.369, 5.400, 5.428, 5.470, 5.489, 5.509, 5.555])
energies_c_dimer = np.array([3.798, 3.973, 4.447, 4.609, 4.825, 4.944, 5.030, 5.033, 5.046, 5.070, 5.148, 5.213])
energies_g_dimer = np.array([3.793, 3.992, 4.429, 4.636, 4.831, 4.989, 5.060, 5.086, 5.224, 5.233, 5.284, 5.319])
energies_t_dimer = np.array([3.795, 3.977, 4.441, 4.547, 4.916, 4.948, 5.042, 5.053, 5.053, 5.053, 5.053, 5.053])

if __name__ == "__main__":
    plot_energy(energies_a_dimer)
    plot_energy(energies_c_dimer)
    plot_energy(energies_g_dimer)
    plot_energy(energies_t_dimer)

# lcmo_spec = np.load("/home/praktikum/Chris/code/data/testdata/lcmo_spec.npy")
# plot_energy_intensity(lcmo_spec[:, 0], lcmo_spec[:, 1], mode="delta", sigma=0.001)