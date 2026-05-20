import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def all_dynamics_plots(data_array):
    """Creates a heatmap of the dynamics data, showing the evolution of coefficients over time.\n
    Takes in the total dynamics data array, which should be of shape (num_steps, num_states)."""
    plt.matshow(data_array.T, aspect="auto", origin="lower")
    plt.xlabel("dynamics step")
    plt.ylabel("coefficient / site index")
    plt.colorbar(label=r"$|c_i(t)|^2$")
    plt.show()

def single_state_dynamics_plot(data_array, state_index):
    """Plots the time evolution of a single coefficient (state) across all dynamics steps.\n
    Takes in the total dynamics data array and the index of the state to plot."""
    plt.plot(data_array[:, state_index])
    plt.xlabel("dynamics step")
    plt.ylabel(r"$|c_i(t)|^2$")
    plt.title(f"Time evolution of coefficient for state {state_index}")
    plt.show()

def consecutive_state_presentation(data_array, start_index, end_index):
    """Plots the time evolution of a single coefficient (state) across all dynamics steps, asking the user for the last state index to plot.\n
    Takes in the total dynamics data array, the start index of the state to plot, and the end index of the state to plot."""
    for i in range(start_index, end_index + 1):
        single_state_dynamics_plot(data_array, state_index=i)

def data_load(path):
    """Loads the dynamics data from a .npy or .npz file and returns it as a numpy array."""
    path = Path(path)
    if path.suffix == ".npy":
        return np.load(path)
    elif path.suffix == ".npz":
        data = np.load(path)
        arrays = [data[key] for key in data.files]
        return np.stack(arrays, axis=0)
    else:
        raise ValueError("Unsupported file format. Please provide a .npy or .npz file.")
    
def array_average(data_array):
    """Takes in a 3D array of shape (num_runs, num_steps, num_states) and averages each state across all runs, returning a 2D array of shape (num_steps, num_states). Useless since np has this built in, but I wanted to write it for practice. Turns out its not difficult at all..."""
    return np.mean(data_array, axis=0)


if __name__ == "__main__":
    data_array = np.load("/home/praktikum/Chris/code/data/dynamics/test3/abs_coefficients_all.npy") #linux path, change if on windows
    single_state_dynamics_plot(data_array, state_index=0)
    single_state_dynamics_plot(data_array, state_index=1) 
    single_state_dynamics_plot(data_array, state_index=2)