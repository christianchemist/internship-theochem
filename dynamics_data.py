import numpy as np
import matplotlib.pyplot as plt
import os


def all_dynamics_plots(data_array):
    """Creates a heatmap of the dynamics data, showing the evolution of coefficients over time.\n
    Takes in the total dynamics data array, which should be of shape (num_steps, num_states)."""
    plt.imshow(data_array.T, aspect="auto", origin="lower")
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

if __name__ == "__main__":
    data_array = np.load("/home/praktikum/Chris/code/data/dynamics/test3/abs_coefficients_all.npy") #linux path, change if on windows
    single_state_dynamics_plot(data_array, state_index=0)
    single_state_dynamics_plot(data_array, state_index=1) 
    single_state_dynamics_plot(data_array, state_index=2)