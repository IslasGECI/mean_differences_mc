import pandas as pd
import numpy as np

class Tester_Significant_Difference:
    def __init__(self):
        self.__sample_a : np.array = np.array([])
        self.__sample_b : np.array = np.array([])

    @property
    def sample_a(self):
        return(self.__sample_a)

    @sample_a.setter
    def sample_a(self, sample_a : pd.DataFrame):
        name_column = sample_a.columns[0]
        self.__sample_a = np.array(sample_a[name_column])

    @property
    def sample_b(self):
        return(self.__sample_b)

    @sample_b.setter
    def sample_b(self, sample_b : pd.DataFrame):
        name_column = sample_b.columns[0]
        self.__sample_b = np.array(sample_b[name_column])