import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from ssh_tools import diagonalise as dg, ssh_hamiltonian as sshH

class chromophor:
    
    """Class to describe a chromophor in a chain with a position and a dipole"""

    def __init__(self, position, dipole):
        self.position = position
        self.dipole = dipole
    
    def __repr__(self):
        return f"chromophor(position={self.position}, dipole={self.dipole})"
    

def generate_positions(num_chromo, spacing=1, mode="trivial"):
    
    """Generates an array of positions for chromophors in a chain with a given spacing. Encodes if the spacing is supposed to respresent a trivial or topological chain by the start of alternate spacing"""
    
    if mode == "trivial":
        return np.array([[i * spacing + (i // 2), 0, 0] for i in range(num_chromo)])
    
    elif mode == "topological":
        return np.array([[i * spacing + ((i+1) // 2), 0, 0] for i in range(num_chromo)])
    
    else:
        raise ValueError("Invalid mode. Use 'trivial' or 'topological'.")
    

def pair_coupling(pos1, pos2, dip1, dip2, C = 1):

    """Calculates the coupling of two chromophores with two different positions pos1 and pos2, two different transition dipole moments dip1 and dip2 and a constant C for SI/Natural conversion."""

    distance_vec = np.diff([pos1, pos2], axis=0).ravel()
    distance_scal = np.linalg.norm(distance_vec)
    r1 = distance_scal
    r2 = r1 * r1
    r3 = r2 * r1
    r5 = r2 * r3

    coupling = C * ((np.dot(dip1, dip2) / r3) - 3 * ( (np.dot(dip1, distance_vec) * np.dot(distance_vec, dip2)) / r5 ))

    return coupling

def plot_energy_intensity(energies, intensities, mode="", sigma=0.1, x_label="Energy", y_label="Intensity", header="Spectrum"):
    
    """Plots the spectrum of a chromophor chain given the energies and intensities""" #fixed, peak height now proportional to intensity and not normalised to 1, also added option for delta peaks, gaussian peaks or both

    normalised_intensities = intensities / np.max(intensities)

    if mode == "delta":
        plt.vlines(energies, 0, normalised_intensities, colors='b', lw=2)
        plt.axhline(0, linewidth=1)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(header)
        plt.show()

    else:
        gaussians = np.zeros(2000)
        total_domain = np.linspace(min(energies) - 5*sigma, max(energies) + 5*sigma, 2000)
        
        for energy, intensity in zip(energies, normalised_intensities):
            
            y = intensity * np.exp(-0.5 * ((total_domain - energy) / sigma) ** 2) 
            gaussians += y
        plt.plot(total_domain, gaussians, color='b')
        
        if mode == "dual":
            plt.vlines(energies, 0, normalised_intensities, colors='r', lw=2)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(header)
        plt.show()


def chroms_hamiltonian(chroms):

    """Computes the hamiltonian for electron coupling in a chromophor chain. \n
    Onsite energy is neglected and only the coupling between chromophors is considered.\n
    Takes a list of chromophors as input and returns the hamiltonian matrix."""

    number = len(chroms)
    H = np.zeros((number, number))

    for i in range(number):
        
        i_pos = chroms[i].position
        i_dip = chroms[i].dipole

        for m in range(i + 1, number):
            m_pos = chroms[m].position
            m_dip = chroms[m].dipole

            temp = pair_coupling(i_pos, m_pos, i_dip, m_dip)
            H[i, m] = H[m, i] = temp

    return H

def intensities(inMatDip, inMatEigV):
    """Calculates the spectral intensities for a chromophor chain. \nTakes the matrix of dipole moments and the matrix of eigenvectors as input and returns a list of intensities for each eigenstate."""
    outMatInt = []
    N = inMatEigV.shape[1]
    for i in range(N):
        
        c = inMatEigV[:, i]
        mu_i = np.matmul(inMatDip, c)
        outMatInt.append(np.dot(mu_i, mu_i))

    return outMatInt

def helix_curve(t, r=1, h=1):
    """Simple WIP helix function"""
    vectorpos = np.array([r * np.cos(2*np.pi*t), r * np.sin(2*np.pi*t), h * t]) #this is the parametrisation of a helix, r is the radius and h is the height per winding, t is the parameter that goes from 0 to 1 for one winding, so for multiple windings we can just multiply t by the number of windings. The function returns the position of a point on the helix given the parameter t. 
    return vectorpos



if __name__ == "__main__":

    #test1 = chromophor("pos", "dipole")
    #print(test1.position, test1.dipole)
    #for j in chromophors:
    #    print(j.position, j.dipole)

    num_chromo = 10
    positions = generate_positions(num_chromo, spacing=1, mode="topological")
    helix_positions = np.array([helix_curve(t) for t in np.linspace(0, 1, num_chromo)]) 

    
    # place for dipole generatrion function, see TODO
    j_dipole_moment = [0, 1, 0]
    h_dipole_moment = [1, 0, 0]
    chromophors = []
    mode = "j" #set user preferance for dipole moment, "j" for j-type and "h" for h-type
    

    if mode == "j": #lazy way to select the dipole moment for the chromophors, could be done more elegant with a function or something but it works for now
        for iter in range(num_chromo):
            chromophors.append(chromophor(positions[iter], j_dipole_moment))

            
    elif mode == "h":
        for iter in range(num_chromo):
            chromophors.append(chromophor(positions[iter], h_dipole_moment))

    else:
        print("Select correct mode")


    mat_dipole = np.column_stack([ch.dipole for ch in chromophors])  # (3, N)
    #print(mat_dipole)

    #print(chromophors)

    my_H = chroms_hamiltonian(chromophors)
    #print(my_H)
    diag, eig = dg(my_H)
    diadiag = np.diag(diag)
    #print(diadiag)
    #print(eig)
    #print(eig[:, 0])
    intents = intensities(mat_dipole, eig)
    #print(intents)
    
    plot_energy_intensity(diadiag, intents, sigma=0.01)

#TODO: add position of chromophors on a helix to prepare for the real project. Wikipedia has a parametrised curve for a helix, should be easy to implement. Make dipolemoment perpendicular to z axis and make a function to generate dipMom with the position in the helix (angles).