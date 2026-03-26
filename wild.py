import numpy as np
import matplotlib.pyplot as plt
from sympy import comp
from ssh_tools import plot_energy, compare_values
from datastructure import data

bam_monomer = data["bam"]["monomer"][0][0]
bam_short_dimer = data["bam"]["short dimer"][0][0:2]
bam_long_dimer = data["bam"]["long dimer"][0][0:2]


print("BAM monomer energies:", bam_monomer)
print("BAM short dimer energies:", bam_short_dimer)
print("BAM long dimer energies:", bam_long_dimer)

compare_values(bam_monomer, bam_short_dimer)
compare_values(bam_monomer, bam_long_dimer)