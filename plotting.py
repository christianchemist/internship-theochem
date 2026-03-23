import numpy as np
import matplotlib.pyplot as plt
from ssh_tools import plot_energy, plot_energy_comparison, npy_to_ndarray
from datastructure import data

# set local energy variables for easier access
# Some of the arrays are 2D arrays, where the first row is for the dft calculations and the second row is for the dft_b calculations. This is the case for all the arrays in "bases monomers"

energies_a_bases = data["bases monomers"]["adenine"]
energies_c_bases = data["bases monomers"]["cytosine"]
energies_g_bases = data["bases monomers"]["guanine"]
energies_t_bases = data["bases monomers"]["thymine"]
energies_a_dimer = data["chromophor dimers"]["adenine"]
energies_c_dimer = data["chromophor dimers"]["cytosine"]
energies_g_dimer = data["chromophor dimers"]["guanine"]
energies_t_dimer = data["chromophor dimers"]["thymine"]


namelist = ["adenine", "cytosine", "guanine", "thymine"]



if __name__ == "__main__":
    # plot_energy(energies_a_dimer)
    # plot_energy(energies_c_dimer)
    # plot_energy(energies_g_dimer)
    # plot_energy(energies_t_dimer)

    nDimArray = np.array([energies_a_dimer, energies_c_dimer, energies_g_dimer, energies_t_dimer])
    # print(nDimArray.shape)
    bases_energies = np.array([energies_c_bases, energies_g_bases, energies_t_bases])
    plot_energy_comparison(bases_energies, list_setnames=["cytosine spacer", "guanine spacer", "thymine spacer"], mode="connected", title="DFT energy comparison plot for spacers")
    plot_energy_comparison(nDimArray, list_setnames=namelist, mode="connected", title="DFT calculation energy comparison plot for dimers")

    # DIALECT_energy_TotalArray = npy_to_ndarray(data_path = "/home/praktikum/Chris/code/data/")
    # dialect_dimer_array = np.load("/home/praktikum/Chris/code/data/dialect_dimer_calculations/c_dimer_excitation_energies.npy")
    # dialect_dimer_array = dialect_dimer_array[:12]

    # plot_energy(dialect_dimer_array, title="DIALECT dimer energy plot for cytosine")
    # plot_energy(energies_c_dimer, title="DFT dimer energy plot for cytosine")
    # both_c = np.array([energies_c_dimer, dialect_dimer_array])
    # plot_energy_comparison(both_c, list_setnames=["cytosine DFT", "cytosine DIALECT"], mode="connected", title="cytosine dimer energy comparison plot")
    # print(DIALECT_energy_TotalArray)
    # print(DIALECT_energy_TotalArray.shape)
    # plot_energy_comparison(nDimArray, list_setnames=namelist, mode="connected", title="DFT calculation energy comparison plot")
    # plot_energy_comparison(DIALECT_energy_TotalArray, list_setnames=namelist, mode="connected", title="DIALECT energy comparison plot")
    # plot_energy_comparison(energies_adenine, list_setnames=["adenine DFT", "adenine DFT_b"], mode="connected", title="adenine energy comparison plot")
    # plot_energy_comparison(energies_cytosine, list_setnames=["cytosine DFT", "cytosine DFT_b"], mode="connected", title="cytosine energy comparison plot")
    # plot_energy_comparison(energies_guanine, list_setnames=["guanine DFT", "guanine DFT_b"], mode="connected", title="guanine energy comparison plot")
    # plot_energy_comparison(energies_thymine, list_setnames=["thymine DFT", "thymine DFT_b"], mode="connected", title="thymine energy comparison plot")
    # plot_energy_comparison(energies_tco, list_setnames=["tco DFT", "tco DFT_b"], mode="connected", title="tco energy comparison plot")
    # all_bio_bases = np.array([energies_adenine[0], energies_cytosine[0], energies_guanine[0], energies_thymine[0]])
    # plot_energy_comparison(all_bio_bases, list_setnames=namelist, mode="connected", title="all bio bases energy comparison plot dft")
    # dftb_bio_bases = np.array([energies_adenine[1], energies_cytosine[1], energies_guanine[1], energies_thymine[1]])
    # plot_energy_comparison(dftb_bio_bases, list_setnames=namelist, mode="connected", title="all bio bases energy comparison plot dft_b")
