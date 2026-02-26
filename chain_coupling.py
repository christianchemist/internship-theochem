import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from ssh_tools import diagonalise as dg

class chromophor:
    
    """Class to describe a chromophor in a chain with a position and a dipole"""

    def __init__(self, position, dipole):
        self.position = position
        self.dipole = dipole


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


def chroms_hamiltonian(number, chroms):

    """computes the hamiltonian for electron coupling in a chromophor chain"""

    H = np.zeros((number, number))

    for i in range(number):
        
        i_pos = chroms[i].position
        i_dip = chroms[i].dipole

        for m in range(i + 1, number):
            m_pos = chroms[m].position
            m_dip = chroms[m].dipole

            temp = pair_coupling(i_pos, m_pos, i_dip, m_dip)
            H[i, m] = temp
            H[m, i] = temp

    return H


if __name__ == "__main__":

    #test1 = chromophor("pos", "dipole")
    #print(test1.position, test1.dipole)


    #for j in chromophors:
    #    print(j.position, j.dipole)

    num_chromo = 3
    positions = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]])
    dipole_moment = [1.2, 2.2, 3.2]
    chromophors = []

    for iter in range(num_chromo):
        chromophors.append(chromophor(positions[iter], dipole_moment))
    
    #print(chromophors)

    my_H = chroms_hamiltonian(num_chromo, chromophors)
    print(my_H)
    diag, eig = dg(my_H)
    print(np.diag(diag))