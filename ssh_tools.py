import numpy as np
import matplotlib.pyplot as plt

def ssh_hamiltonian(cells, v, w, exEnerg=0.0, start="v"):

    """Generates a Hamiltonian for the SSH polyacetylene model. Takes in the amount of cells (2 carbons, might change later), strangth of v, strngth of w, and optionally the excitation Energy and the starting bond. Returns a 2N*2N array"""

    n = 2*cells
    
    H = np.zeros((n, n), dtype=float)
    np.fill_diagonal(H, exEnerg)
    
    t = np.empty(n - 1, dtype=float)
    if start == "v":
        t[0::2] = v
        t[1::2] = w
    else:
        t[0::2] = w
        t[1::2] = v

    i = np.arange(n - 1)
    H[i, i + 1] = t
    H[i + 1, i] = t

    return H


def diagonalise(inMat):

    """Takes in a square Matrix/array and returns the diagonalised matrix D and the eigenvectors P"""

    eig_vals, P = np.linalg.eigh(inMat)
    D = np.diag(eig_vals)
    return D, P


def plot_energy(inArray, v_in="N/A", w_in="N/A"):
    
    """Takes a flattened matrix (1D array) to plot the energy Eigenvalues."""

    x = np.arange(1, len(inArray)+1)
    y = inArray
    fig, ax = plt.subplots(figsize=(5, 4), layout="constrained")
    ax.plot(x, y, "go", label="test")
    ax.set_xlabel("Unit cell")
    ax.set_ylabel("Energy")
    ax.set_title(f"energy plot - v = {v_in} w = {w_in}")
    plt.show()

def plot_coefficients(inD, inP):

    idx = np.argsort(np.abs(inD))[:2] # gibt ja 2 eigenzustände nahe der gap

    for i in idx: # einen plot für beide zustände, loop weil
        psi = inP[:, i]

        x = np.arange(len(psi))
        plt.bar(x, psi)
        plt.xlabel("site index")
        plt.ylabel("coefficients")
        plt.title(f"State {i}, E = {inD[i]:.6g}")
        plt.show()        




# TEST STATEMENTS
if __name__ == "__main__":
    c, v_var, w_var = 20, 0.8, 2.55 # set parameters for the hamiltonian
    #test = ssh_hamiltonian(c, v_var, w_var, start="v") 

    #diag_mat, temp = diagonalise(test)
    #oneDdiag = np.diag(diag_mat)
    #print(diag_mat)
    #print(test)
    #print(oneDdiag)
    #plot_energy(oneDdiag)
    #plot_coefficients(oneDdiag, temp)