import numpy as np
import matplotlib.pyplot as plt
from sympy import plot
from ssh_tools import plot_energy, plot_energy_comparison, npy_to_ndarray


# unused energies: 5.338, 5.369, 5.400, 5.428, 5.470, 5.489, 5.509, 5.555])


# The following arrays will be for BOTH dft and dft_b calculations. The fist row will be for the dft calculations, the second row for the dft_b calculations.
energies_tco = np.array([[4.215, 4.991, 5.138, 5.265, 5.366, 5.794, 6.431, 6.752, 6.899, 6.959, 7.134, 7.160], [4.047186, 4.440723, 4.946347, 5.078257, 5.416622, 6.103660, 6.191569, 6.623455, 6.756302, 6.821764, 7.007705, 7.073461]])
# energies_bam = np.array([[0.515, 0.914, 1.135, 1.926, 2.194, 2.363, 2.494, 2.830, 3.293, 3.527, 4.035, 4.126], []]) This structure was corrupted in the .xyz file, so the energies are wrong. Luca or I will have to fix the structure sometime

# the following arrays will contain the excitation energies for the strands of bases, calculated with the DFT program orca.


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
