import pandas as pd
import numpy as np

class Tester_Significant_Difference:
    def __init__(self):
        self.__sample_a : np.array = np.array([])
        self.__sample_b : np.array = np.array([])

    @property
    def sample_a(self):
        return(np.array([3, 3, 3, 3]))

    @sample_a.setter
    def sample_a(self, sample_a : pd.DataFrame):
        pass