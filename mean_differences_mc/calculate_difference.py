import numpy as np
def calculate_difference(A : list, B : list):
    difference_array : np.array = np.array(A) - np.array(B)
    difference : int = difference_array.sum()
    return(difference)