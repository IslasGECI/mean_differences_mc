import numpy as np

def switch_elements(A : list, B : list, index : list):
    A_final: list = A.copy()
    A_final[index[0]] = B[index[1]]
    B_final: list = B.copy()
    B_final[index[1]] = A[index[0]]
    return(A_final, B_final)

def switch_elements_arrays(A : np.array, B : np.array, index : list):
    A_final: np.array = np.copy(A)
    A_final[index[0]] = B[index[1]]
    B_final: np.array = np.copy(B)
    B_final[index[1]] = A[index[0]]
    return(A_final, B_final)