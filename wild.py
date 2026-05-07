import numpy as np
from dynamics_data import all_dynamics_plots, single_state_dynamics_plot, single_state_presentation

full_data = np.load(r"C:\Users\chris\OneDrive\Dokumente\Uni\internship-theochem\data\dynamics\test4\abs_coefficients_all.npy")

all_dynamics_plots(full_data)
single_state_presentation(full_data)