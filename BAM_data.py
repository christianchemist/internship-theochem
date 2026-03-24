import numpy as np
import matplotlib.pyplot as plt
import os

from sympy import fu
from ssh_tools import plot_energy, plot_energy_comparison
from datastructure import data

full_structure_energies = data["bam"]["full structure"]
#full_structure_energies = full_structure_energies[:12] # only plot the first 12 energies for better visibility
short_dimer_energies = data["bam"]["short dimer"]
long_dimer_energies = data["bam"]["long dimer"]
monomer_energies = data["bam"]["monomer"]
twox_energies = data["bam"]["2x"]


if __name__ == "__main__":
    mode = input(" DFT/DFTB or comparison? (enter dft or dftb or comparison): ")
    if mode == "dft":
        plot_energy(full_structure_energies[0], title="Full BAM structure energies")
        plot_energy(long_dimer_energies[0], title="Long dimer energies")
        plot_energy(short_dimer_energies[0], title="Short dimer energies")
        plot_energy(monomer_energies[0], title="Monomer energies")
        plot_energy(twox_energies[0], title="2x dimer energies")
    elif mode == "dftb":
        plot_energy(full_structure_energies[1], title="Full BAM structure energies with DFTB")
        plot_energy(long_dimer_energies[1], title="Long dimer energies with DFTB")
        plot_energy(short_dimer_energies[1], title="Short dimer energies with DFTB")
        plot_energy(monomer_energies[1], title="Monomer energies with DFTB")
        plot_energy(twox_energies[1], title="2x dimer energies with DFTB")
    elif mode == "comparison":
        plot_energy_comparison(full_structure_energies, ["DFT", "DFTB"], title="Full BAM structure energies")
        plot_energy_comparison(long_dimer_energies, ["DFT", "DFTB"], title="Long dimer energies")
        plot_energy_comparison(short_dimer_energies, ["DFT", "DFTB"], title="Short dimer energies")
        plot_energy_comparison(monomer_energies, ["DFT", "DFTB"], title="Monomer energies")
        plot_energy_comparison(twox_energies, ["DFT", "DFTB"], title="2x dimer energies")