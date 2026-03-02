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
    


def pair_coupling(pos1, pos2, dip1, dip2, C = 1):

    """Calculates the coupling of two chromophores with two different positions pos1 and pos1, two differnt transition dipole moments dip1 and dip2 and a constant C for SI/Natural conversion."""

    distance_vec = np.diff([pos1, pos2], axis=0).ravel()
    distance_scal = np.linalg.norm(distance_vec)
    r1 = distance_scal
    r2 = r1 * r1
    r3 = r2 * r1
    r5 = r2 * r3

    coupling = C * ((np.dot(dip1, dip2) / r3) - 3 * ( (np.dot(dip1, distance_vec) * np.dot(distance_vec, dip2)) / r5 ))

    return coupling


def chroms_hamiltonian(chroms):

    """computes the hamiltonian for electron coupling in a chromophor chain"""

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
    """Calculates the spectral intensities for a chromophor dimer""" #support added for longer chains
    outMatInt = []
    N = inMatEigV.shape[1]
    for i in range(N):
        
        c = inMatEigV[:, i]
        mu_i = np.matmul(inMatDip, c)
        outMatInt.append(np.dot(mu_i, mu_i))

    return outMatInt




if __name__ == "__main__":

    #test1 = chromophor("pos", "dipole")
    #print(test1.position, test1.dipole)
    #for j in chromophors:
    #    print(j.position, j.dipole)

    num_chromo = 7
    positions = np.array([[1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0], [5, 0, 0], [6, 0, 0], [7, 0, 0]]) # set positions for chromophors in a chain
    j_dipole_moment = [0, 1, 0]
    h_dipole_moment = [1, 0, 0]
    chromophors = []
    mode = "j" #set user preferance for dipole moment, "j" for j-type and "h" for h-type
    

    if mode == "j": #lazy way to select the dipole moment for the chromophors, could be done more elegant with a function or something but it works for now
        for iter in range(num_chromo):
            chromophors.append(chromophor(positions[iter], j_dipole_moment))
            temp = np.atleast_2d(j_dipole_moment).T
            
    elif mode == "h":
        for iter in range(num_chromo):
            chromophors.append(chromophor(positions[iter], h_dipole_moment))
            temp = np.atleast_2d(h_dipole_moment).T
    else:
        print("Select correct mode")


    mat_dipole = np.column_stack([ch.dipole for ch in chromophors])  # (3, N)
    print(mat_dipole)

    #print(chromophors)

    my_H = chroms_hamiltonian(chromophors)
    print(my_H)
    diag, eig = dg(my_H)
    #print(np.diag(diag))
    #print(eig)
    #print(eig[:, 0])
    print(intensities(mat_dipole, eig))
