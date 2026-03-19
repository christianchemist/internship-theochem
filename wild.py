import numpy as np

c_1 = np.load("/home/praktikum/Chris/code/data/dialect_dimer_calculations/c_dimer_excitation_energies.npy")
c_2 = np.load("/home/praktikum/Chris/code/data/c_spacer_cutout.npy")

print(c_1[:12])
print(c_2[:12, 0])

