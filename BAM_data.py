import numpy as np
import matplotlib.pyplot as plt
from ssh_tools import plot_energy, plot_energy_comparison
from datastructure import data

# TODO: Improve __main__ function. maybe with a loop over a list, I will see


full_structure_energies = data["bam"]["full structure"]
#full_structure_energies = full_structure_energies[:12] # only plot the first 12 energies for better visibility
short_dimer_energies = data["bam"]["short dimer"]
long_dimer_energies = data["bam"]["long dimer"]
monomer_energies = data["bam"]["monomer"]
twox_energies = data["bam"]["2x"]
fourx_energies = data["bam"]["4x"]
adenine_energies = data["bases monomers"]["adenine"]
cytosine_energies = data["bases monomers"]["cytosine"]
guanine_energies = data["bases monomers"]["guanine"]
thymine_energies = data["bases monomers"]["thymine"]


if __name__ == "__main__":
    mode = input(" DFT/DFTB or comparison? (enter dft or dftb or comparison): ")
    if mode == "dft":
        plot_energy(full_structure_energies[0], title="Full BAM structure energies")
        plot_energy(long_dimer_energies[0], title="Long dimer energies")
        plot_energy(short_dimer_energies[0], title="Short dimer energies")
        plot_energy(monomer_energies[0], title="Monomer energies")
        plot_energy(twox_energies[0], title="2x dimer energies")
        plot_energy(fourx_energies[0], title="4x dimer energies")
        plot_energy(adenine_energies[0], title="Adenine monomer energies")
        plot_energy(cytosine_energies[0], title="Cytosine monomer energies")
        plot_energy(guanine_energies[0], title="Guanine monomer energies")
        plot_energy(thymine_energies[0], title="Thymine monomer energies")
    elif mode == "dftb":
        plot_energy(full_structure_energies[1], title="Full BAM structure energies with DFTB")
        plot_energy(long_dimer_energies[1], title="Long dimer energies with DFTB")
        plot_energy(short_dimer_energies[1], title="Short dimer energies with DFTB")
        plot_energy(monomer_energies[1], title="Monomer energies with DFTB")
        plot_energy(twox_energies[1], title="2x dimer energies with DFTB")
        plot_energy(fourx_energies[1], title="4x dimer energies with DFTB")
        plot_energy(adenine_energies[1], title="Adenine monomer energies with DFTB")
        plot_energy(cytosine_energies[1], title="Cytosine monomer energies with DFTB")
        plot_energy(guanine_energies[1], title="Guanine monomer energies with DFTB")
        plot_energy(thymine_energies[1], title="Thymine monomer energies with DFTB")
    elif mode == "comparison":
        plot_energy_comparison(full_structure_energies, ["DFT", "DFTB"], title="Full BAM structure energies")
        plot_energy_comparison(long_dimer_energies, ["DFT", "DFTB"], title="Long dimer energies")
        plot_energy_comparison(short_dimer_energies, ["DFT", "DFTB"], title="Short dimer energies")
        plot_energy_comparison(monomer_energies, ["DFT", "DFTB"], title="Monomer energies")
        plot_energy_comparison(twox_energies, ["DFT", "DFTB"], title="2x dimer energies")
        plot_energy_comparison(fourx_energies, ["DFT", "DFTB"], title="4x dimer energies")
        plot_energy_comparison(adenine_energies, ["DFT", "DFTB"], title="Adenine monomer energies")
        plot_energy_comparison(cytosine_energies, ["DFT", "DFTB"], title="Cytosine monomer energies")
        plot_energy_comparison(guanine_energies, ["DFT", "DFTB"], title="Guanine monomer energies")
        plot_energy_comparison(thymine_energies, ["DFT", "DFTB"], title="Thymine monomer energies")
    else:
        print("Invalid input. Please enter 'dft', 'dftb', or 'comparison'.")