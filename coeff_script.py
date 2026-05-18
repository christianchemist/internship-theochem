# USAGE: python coeff_script.py <steps> [--dir <directory>] ---- A bit obsolte since the output of DIALECT also gives the full array as an .npz
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser(description="Merge abs_coefficients_*.npy files in strict order into a single array and save as coeff_abs.npy.")
parser.add_argument("steps", type=int, help="Number of steps in dynamics calculation.")
parser.add_argument(
    "--dir",
    default=".",
    help="Directory containing the npy files. Default: current directory.")
args = parser.parse_args()

script_dir = os.path.abspath(args.dir)
save_array = []

for i in range(args.steps):
    file_name = f"abs_coefficients_{i}.npy"
    file_path = os.path.join(script_dir, file_name)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Required file missing: {file_path}")

    data = np.load(file_path)
    save_array.append(data)

save_array = np.stack(save_array, axis=0)

save_path = os.path.join(script_dir, "all_coeff_abs.npy")
np.save(save_path, save_array)

print(f"Saved array shape: {save_array.shape}")
print("Array save complete!")