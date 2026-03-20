import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from chain_coupling import plot_energy_intensity
import os


data_path = "/home/praktikum/Chris/code/data/" #Change according to directory in which the script is being ran

if __name__ == "__main__":
    for entry in os.scandir(data_path):
        if entry.is_file() and entry.name.endswith(".npy"):
            calculations = np.load(entry.  path)
            plot_energy_intensity(calculations[:, 0], calculations[:, 1], mode="gaussian", sigma=0.005, header=f"LCMO Spectrum for {entry.name}")