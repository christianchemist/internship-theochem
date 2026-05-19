import numpy as np

scrambled_vector_list = np.array([[0, 100, 0], [100, 0, 0], [5, 5, 5], [0, 0, 0], [10, 10, 10], [15, 15, 15], [20, 20, 20], [1, 1, 1], [6, 6, 6], [11, 11, 11], [16, 16, 16], [2, 2, 2], [7, 7, 7], [12, 12, 12], [17, 17, 17], [3, 3, 3], [8, 8, 8], [13, 13, 13], [18, 18, 18], [4, 4, 4], [9, 9, 9], [14, 14, 14], [19, 19, 19], [20.1,20.1 ,20.1]])

def check_vectors(vector_list: np.ndarray, norm_tolerance=0.5, vec_tolerance=0.2, verbose=False):
    """Takes in a list of vectors and checks if any of them are close to each other, first by comparing their norms and then by using np.allclose to check if the vectors themselves are close.
    The function prints out the pairs of vectors that are close to each other, along with their indices and norm values.
    
    The norm_tolerance parameter controls how close the norms of the vectors need to be for them to be considered close, while the vec_tolerance parameter controls how close the vectors themselves need to be for them to be considered close."""

    norm_list = np.linalg.norm(vector_list, axis=1) # calculate the norm of each vector in the list
    enumerated_normlist = list(enumerate(norm_list)) # create a list of tuples containing the index and the corresponding norm value, so that we can sort the list while keeping track of the original indices
    sorted_by_second = sorted(enumerated_normlist, key=lambda tup: tup[1]) # sort the list of tuples based on the second element (the norm value) using a lambda function as the key for sorting

    close_vectors = []
    for i, current_vec in enumerate(sorted_by_second):
        current_index, current_norm = current_vec

        for previous_index in range(i):
            other_index, other_norm = sorted_by_second[previous_index]

            if current_norm - other_norm > norm_tolerance:
                continue

            if verbose:
                print(f"Close vector norms at index {current_index} (norm: {current_norm:.2f}) and vector at index {other_index} (norm: {other_norm:.2f})")
            close_vectors.append((current_index, other_index))
            
    # print("Close vector pairs (indices):", close_vectors)
    for element in close_vectors:
        if verbose:
            print("-" * 50)
            print(f"Comparing vector at index {element[0]} and vector at index {element[1]}:")
            print(f"Vector 1: {vector_list[element[0]]}")
            print(f"Vector 2: {vector_list[element[1]]}")
            print(f"Are the vectors close? {np.allclose(vector_list[element[0]], vector_list[element[1]], atol=vec_tolerance)}")
            print("-" * 50)
        else:
            print(f"Vectornorms at indices {element[0]} and {element[1]} are close. Are the vectors close? {np.allclose(vector_list[element[0]], vector_list[element[1]], atol=vec_tolerance)}")

if __name__ == "__main__":
    check_vectors(scrambled_vector_list, norm_tolerance=0.5, vec_tolerance=0.2, verbose=False)