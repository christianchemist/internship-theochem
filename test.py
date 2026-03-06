import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


# def pair_coupling(pos1, pos2):

#     """Calculates the coupling of 2 different chromophores with two different positions pos1 and pos1 and two differnt transition dipole moments dip1 and dip2"""

#     difference = np.diff([pos1, pos2], axis=0)
#     return difference

# t1 = np.array([1, 3, 5])
# t2 = np.array([2, 4, 6])

# temp = pair_coupling(t1, t2)
# temp2 = temp.ravel()

# print(temp.shape)
# print(temp2.shape)

# t2 = np.array([1, 2, 3])
# print(t2.shape)

# num_chromo = 10
# positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# dipole_moments = [1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2, 10.2]
# chromophors = []

# for iter in range(num_chromo):
#     chromophors.append(chromophor(positions[iter], dipole_moments[iter]))

# for j in chromophors:
#     print(j.position, j.dipole)

# [1, 2, 3]

# positions = np.array([[1, 0, 0], [10, 0, 0], [3, 0, 0], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10]])


def helix_curve(t, r=1, h=1):
    """Simple WIP helix function"""
    vectorpos = np.array([r * np.cos(2*np.pi*t), r * np.sin(2*np.pi*t), h * t])
    return vectorpos

windings = np.arange(0, 10, 0.01)
helix_points = np.array([helix_curve(t) for t in windings])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(helix_points[:, 0], helix_points[:, 1], helix_points[:, 2])
plt.show()