from ssh_tools import ssh_hamiltonian, diagonalise
import numpy as np
import matplotlib.pyplot as plt 

test_cells, fixed_w = 10, 1

var_r = np.linspace(0, 2, 100)

saved_energies = np.empty((0, test_cells*2))

for r in var_r:
    
    #for every point in var_r the hamiltonian gets diagonalised and the energies stored into saved_energies

    energies_mat, temp = diagonalise(ssh_hamiltonian(test_cells, v=r, w=fixed_w))
    saved_energies = np.vstack((saved_energies, np.diag(energies_mat)))

R = np.repeat(var_r, saved_energies.shape[1])
E = saved_energies.ravel()



if __name__ == "__main__":
    plt.scatter(R, E, s=5)
    plt.axhline(0, linewidth=1)
    plt.xlabel("r")
    plt.ylabel("energy")
    plt.show()


