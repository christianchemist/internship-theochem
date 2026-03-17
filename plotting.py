from operator import index

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from sympy import plot
from chain_coupling import intensities, plot_energy_intensity
from ssh_tools import plot_energy, plot_energy_comparison, npy_to_ndarray
import os


energies_a_dimer = np.array([3.822, 3.999, 4.552, 4.805, 4.986, 4.991, 5.062, 5.086, 5.142, 5.188, 5.288, 5.330]) # unused energies: 5.338, 5.369, 5.400, 5.428, 5.470, 5.489, 5.509, 5.555])
energies_c_dimer = np.array([3.798, 3.973, 4.447, 4.609, 4.825, 4.944, 5.030, 5.033, 5.046, 5.070, 5.148, 5.213])
energies_g_dimer = np.array([3.793, 3.992, 4.429, 4.636, 4.831, 4.989, 5.060, 5.086, 5.224, 5.233, 5.284, 5.319])
energies_t_dimer = np.array([3.795, 3.977, 4.441, 4.547, 4.916, 4.948, 5.042, 5.053, 5.053, 5.053, 5.053, 5.053])

# The following arrays will be for BOTH dft and dft_b calculations. The fist row will be for the dft calculations, the second row for the dft_b calculations.

energies_adenine = np.array([[5.515, 5.868, 6.012, 6.155, 6.453, 7.103, 7.292, 7.338, 7.563, 7.702, 7.877, 8.247], [5.233690, 5.996207, 6.013295, 6.057118, 6.207766, 6.863728, 6.985533, 7.414946, 7.552868, 7.641801, 7.749937, 8.072777]])
energies_cytosine = np.array([[5.178, 5.267, 5.691, 5.959, 6.334, 6.801, 7.336, 7.465, 7.668, 7.911, 8.248, 8.397], [4.243206, 4.876276, 5.024468, 5.938865, 6.299383, 6.978410, 7.262634, 7.789460, 7.874877, 8.234659, 8.410087, 8.630745]])
energies_guanine = np.array([[5.480, 5.528, 6.142, 6.518, 6.546, 6.901, 7.220, 7.255, 7.546, 7.703, 7.742, 7.935], [5.381263, 5.718185, 6.052325, 6.197257, 6.295626, 6.372635, 7.307451, 7.353391, 7.612550, 7.672059, 7.705717, 7.783890]])
energies_thymine = np.array([[5.069, 5.650, 6.453, 6.980, 7.241, 7.287, 7.481, 7.634, 8.399, 8.651, 8.752, 8.791], [4.563477, 5.741185, 5.837907, 6.370803, 6.661360, 7.061982, 7.407662, 7.700230, 7.754883, 8.287659, 8.394256, 8.756388]])

energies_tco = np.array([[4.215, 4.991, 5.138, 5.265, 5.366, 5.794, 6.431, 6.752, 6.899, 6.959, 7.134, 7.160], [4.047186, 4.440723, 4.946347, 5.078257, 5.416622, 6.103660, 6.191569, 6.623455, 6.756302, 6.821764, 7.007705, 7.073461]])
# energies_bam = np.array([[0.515, 0.914, 1.135, 1.926, 2.194, 2.363, 2.494, 2.830, 3.293, 3.527, 4.035, 4.126], []]) This structure was corrupted in the .xyz file, so the energies are wrong. Luca or I will have to fix the structure sometime

namelist = ["adenine", "cytosine", "guanine", "thymine"]

if __name__ == "__main__":
    # plot_energy(energies_a_dimer)
    # plot_energy(energies_c_dimer)
    # plot_energy(energies_g_dimer)
    # plot_energy(energies_t_dimer)

    nDimArray = np.array([energies_a_dimer, energies_c_dimer, energies_g_dimer, energies_t_dimer])
    # print(nDimArray.shape)
    DIALECT_energy_TotalArray = npy_to_ndarray(data_path = "/home/praktikum/Chris/code/data/")
    print(DIALECT_energy_TotalArray)
    print(DIALECT_energy_TotalArray.shape)
    #plot_energy_comparison(nDimArray, list_setnames=namelist, mode="connected", title="DFT calculation energy comparison plot")
    #plot_energy_comparison(DIALECT_energy_TotalArray, list_setnames=namelist, mode="connected", title="DIALECT energy comparison plot")
    plot_energy_comparison(energies_adenine, list_setnames=["adenine DFT", "adenine DFT_b"], mode="connected", title="adenine energy comparison plot")
    plot_energy_comparison(energies_cytosine, list_setnames=["cytosine DFT", "cytosine DFT_b"], mode="connected", title="cytosine energy comparison plot")
    plot_energy_comparison(energies_guanine, list_setnames=["guanine DFT", "guanine DFT_b"], mode="connected", title="guanine energy comparison plot")
    plot_energy_comparison(energies_thymine, list_setnames=["thymine DFT", "thymine DFT_b"], mode="connected", title="thymine energy comparison plot")
    plot_energy_comparison(energies_tco, list_setnames=["tco DFT", "tco DFT_b"], mode="connected", title="tco energy comparison plot")
