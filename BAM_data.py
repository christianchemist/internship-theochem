import numpy as np
import matplotlib.pyplot as plt
import os
from ssh_tools import plot_energy, plot_energy_comparison

full_structure_energies = np.array([0.421, 0.778, 1.438, 1.831, 1.837, 2.185, 2.559, 3.028, 3.073, 3.082, 3.131, 3.266])
short_dimer_energies = np.array([3.267, 3.335, 4.085, 4.091, 4.552, 4.555, 4.997, 5.183, 5.190, 5.231, 5.266, 5.270])
long_dimer_energies = np.array([3.297, 3.298, 4.102, 4.102, 4.568, 4.569, 5.192, 5.192, 5.267, 5.267, 5.556, 5.556])
monomer_energies = np.array([3.297, 4.100, 4.567, 5.192, 5.267, 5.553, 5.821, 5.934, 6.078, 6.264, 6.273, 6.531])

if __name__ == "__main__":
    plot_energy(full_structure_energies, title="Full BAM structure energies")
    plot_energy(long_dimer_energies, title="Long dimer energies")
    plot_energy(short_dimer_energies, title="Short dimer energies")
    plot_energy(monomer_energies, title="Monomer energies")