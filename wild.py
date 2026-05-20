import numpy as np
from dynamics_data import all_dynamics_plots, single_state_dynamics_plot

full_data = np.load(r"/home/praktikum/Chris/code/data/dynamics/test4/abs_coefficients_all.npy")

all_dynamics_plots(full_data)
