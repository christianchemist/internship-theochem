import numpy as np
import matplotlib.pyplot as plt
import os
from ssh_tools import plot_energy, plot_energy_comparison
from datastructure import data

full_structure_energies = data["bam"]["full structure"]
short_dimer_energies = data["bam"]["short dimer"]
long_dimer_energies = data["bam"]["long dimer"]
monomer_energies = data["bam"]["monomer"]


if __name__ == "__main__":
    plot_energy(full_structure_energies, title="Full BAM structure energies")
    plot_energy(long_dimer_energies, title="Long dimer energies")
    plot_energy(short_dimer_energies, title="Short dimer energies")
    plot_energy(monomer_energies, title="Monomer energies")