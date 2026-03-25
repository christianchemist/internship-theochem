import array

import numpy as np
import matplotlib.pyplot as plt
from ssh_tools import plot_energy, plot_energy_comparison
from datastructure import data

# "improved" solution for loading all the data, its just not as blocky and a bit more compressed than the previous version. The arrays are stored in a list and the names of the arrays are stored in a separate list, so that they can be easily accessed and plotted. The dataset names are also stored in a separate list for easy access when plotting comparisons.
array_list = [data["bam"]["full structure"], data["bam"]["short dimer"], data["bam"]["long dimer"], data["bam"]["monomer"], data["bam"]["2x"], data["bam"]["4x"], data["bases monomers"]["adenine"], data["bases monomers"]["cytosine"], data["bases monomers"]["guanine"], data["bases monomers"]["thymine"], data["bam"]["4x no bases"]]
array_names = ["full structure", "short dimer", "long dimer", "monomer", "2x dimer", "4x dimer", "adenine monomer", "cytosine monomer", "guanine monomer", "thymine monomer", "4x dimer no bases"]
dataset_names = ["DFT", "DFTB"]


if __name__ == "__main__":
    mode = input(" DFT/DFTB or comparison? (enter dft or dftb or comparison): ")
    if mode == "dft":
        for array, name in zip(array_list, array_names):
            plot_energy(array[0], title=f"{name} energies")

    elif mode == "dftb":
        for array, name in zip(array_list, array_names):
            plot_energy(array[1], title=f"{name} energies with DFTB")

    elif mode == "comparison":
        for array, name in zip(array_list, array_names):
            plot_energy_comparison(array, list_setnames=dataset_names, mode="connected", title=f"{name} energy comparison plot")
    else:
        print("Invalid input. Please enter 'dft', 'dftb', or 'comparison'.")