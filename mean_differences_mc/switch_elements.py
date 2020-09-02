import numpy as np
import pandas as pd


def switch_elements(A: list, B: list, index: list):
    a_final: list = A.copy()
    a_final[index[0]] = B[index[1]]
    b_final: list = B.copy()
    b_final[index[1]] = A[index[0]]
    return (a_final, b_final)


def switch_elements_arrays(A: np.array, B: np.array, index: list):
    a_final: np.array = np.copy(A)
    a_final[index[0]] = B[index[1]]
    b_final: np.array = np.copy(B)
    b_final[index[1]] = A[index[0]]
    a_final_dataframe = pd.DataFrame(a_final)
    b_final_dataframe = pd.DataFrame(b_final)
    return (a_final_dataframe, b_final_dataframe)
