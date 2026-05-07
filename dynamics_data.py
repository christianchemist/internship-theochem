import numpy as np
import matplotlib.pyplot as plt
import os


def all_dynamics_plots(data_array):
    plt.imshow(data_array.T, aspect="auto", origin="lower")
    plt.xlabel("dynamics step")
    plt.ylabel("coefficient / site index")
    plt.colorbar(label=r"$|c_i(t)|^2$")
    plt.show()

def single_state_dynamics_plot(data_array, state_index):
    plt.plot(data_array[:, state_index])
    plt.xlabel("dynamics step")
    plt.ylabel(r"$|c_i(t)|^2$")
    plt.title(f"Time evolution of coefficient for state {state_index}")
    plt.show()

def single_state_presentation(data_array):
    end = int(input("how many states do you want to plot? (starts at 0) "))
    for i in range(end):
        single_state_dynamics_plot(data_array, state_index=i)

if __name__ == "__main__":
    data_array = np.load("/home/praktikum/Chris/code/data/dynamics/test3/abs_coefficients_all.npy") #linux path, change if on windows
    single_state_dynamics_plot(data_array, state_index=0)
    single_state_dynamics_plot(data_array, state_index=1) 
    single_state_dynamics_plot(data_array, state_index=2)