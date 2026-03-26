import os
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

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

def placeholder():

    """Placeholder function for testing purposes. Returns a 2N*2N array with random values."""

    n = 20
    H = np.random.rand(n, n)
    H = (H + H.T) / 2 # make it symmetric
    return H

def diagonalise(inMat):

    """Takes in a square Matrix/array and returns the diagonalised matrix D and the eigenvectors P"""

    eig_vals, P = np.linalg.eigh(inMat)
    D = np.diag(eig_vals)
    return D, P


def plot_energy(inArray, title="energy plot", v_in="N/A", w_in="N/A"):
    
    """Takes a flattened matrix (1D array) to plot the energy Eigenvalues."""

    x = np.arange(1, len(inArray)+1)
    y = inArray
    fig, ax = plt.subplots(figsize=(5, 4), layout="constrained")
    ax.plot(x, y, "go", label="test")
    ax.set_xlabel("Eigenvalue Index")
    ax.set_ylabel(r"$E_{exc}$ in eV")
    ax.grid(True, which="both", linestyle="--", linewidth=0.5)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    if v_in != "N/A" and w_in != "N/A":
        ax.set_title(f"{title} --- v = {v_in} w = {w_in}")
    else:
        ax.set_title(title)
    plt.show()

def npy_to_ndarray(data_path=""):
    """Takes n .npy files and converts it to an n-Dimensional numpy array. Returns the numpy array. Hyperspecific implementation for the DIALECT energy data, assumes that the energies are in the first column and that we only want the first 12 values. The function can be easily adapted to other datasets by changing the values variable and the way the files are selected."""
    
    outArr = []
    files = []
    for entry in os.scandir(data_path):
        if entry.is_file() and entry.name.endswith("cutout.npy"):
            files.append(entry.path)

    for file in files:
        data = np.load(file)
        values = data[:12, 0] # energies are in the first column, we only want the first 12 values
        outArr.append(values)

    outArr = np.array(outArr)
    return outArr


def plot_energy_comparison(inArrayMultDim, list_setnames=["dataset 1", "dataset 2", "dataset 3", "dataset 4"], mode="connected", title="energy comparison plot"):

    """Takes in an n-Dimensional array and plots the energy corresponding to the eingenvalue Index. Uses multiple colors to differentiate between the different datasets. Can connect the dots with a slim line to make it easier to follow the trend. """
    
    x = np.arange(1, inArrayMultDim.shape[1]+1)
    fig, ax = plt.subplots(figsize=(5, 4), layout="constrained")
    for i in range(inArrayMultDim.shape[0]):
        y = inArrayMultDim[i]
        if mode == "connected":
            ax.plot(x, y, "o-", label=f"{list_setnames[i]}")
        else:
            ax.plot(x, y, "o", label=f"{list_setnames[i]}")
    ax.set_xlabel("Eigenvalue Index")
    ax.set_ylabel(r"$E_{exc}$ in eV")
    ax.set_title(f"{title}")
    ax.legend()
    plt.show()

def plot_coefficients(inD, inP):

    idx = np.argsort(np.abs(inD))[:2] # gibt ja 2 eigenzustände nahe der gap

    for i in idx: # einen plot für beide zustände, loop weil
        psi = inP[:, i]

        x = np.arange(len(psi))
        plt.bar(x, psi)
        plt.xlabel("site index")
        plt.ylabel(r"$c_i$")
        plt.title(f"State {i}, E = {inD[i]:.6g}")
        plt.show()        


def compare_values(inValue, inCompArray):

    """Hyperspecific function to compare a momomer value to the splitting of the dimers. Takes the monomer value as a float and the dimer values as an array. Plots the monomer value at the center and the dimer values on the zame vertical axis."""

    x = np.arange(0, 5)
    fig, ax = plt.subplots(figsize=(5, 6), layout="constrained")
    ax.plot([2, 2], [inCompArray[0], inCompArray[1]], "o", linestyle = "none", markerfacecolor="none", markeredgecolor="gray", label="dimer splitting")
    ax.plot(2, inValue, "o", color="gray", label="monomer energy")
    ax.set_xlabel("Eigenvalue Index")
    ax.set_ylabel(r"$E_{exc}$ in eV")
    ax.set_title("Monomer energy vs Dimer splitting")
    ax.grid(True, which="both", linestyle="--", linewidth=0.5)
    ax.legend()
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