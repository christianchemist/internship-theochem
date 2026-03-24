import numpy as np


vector_list = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 9, 9], [10, 10, 10], [11, 11, 11], [12, 12, 12], [13, 13, 13], [14, 14, 14], [15, 15, 15], [16, 16, 16], [17, 17, 17], [18, 18, 18], [19, 19, 19], [20, 20, 20], [20, 20.1, 20.1]])

def check_vectors(inMatVectors, spacing_threshold=0.05):
    """Checks if the input vectors are too close together, which detects errors in .xyz files. If the vectors are too close together, it prints a warning message and returns False. Otherwise, it returns True."""
    for i in range(len(inMatVectors)):
        for j in range(i+1, len(inMatVectors)):
            distance = np.linalg.norm(inMatVectors[i] - inMatVectors[j])
            if distance < spacing_threshold:
                print(f"Warning: Vectors {i} and {j} are too close together (distance: {distance:.4f}). This may indicate an error in the .xyz file.")
                return False
    return True

if __name__ == "__main__":
    result = check_vectors(vector_list)
    print(f"Result of vector check: {result}")