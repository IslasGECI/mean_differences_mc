import unittest
import datetime
import pandas as pd
import numpy as np
from mean_differences_mc import *


class TestTesterSignificantDifference(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.sample_a: pd.DataFrame = pd.DataFrame({"sample_a": [3.0, 3.0, 3.0, 3.0]})
        self.sample_a_array: np.array = np.array(self.sample_a["sample_a"])
        self.sample_b: pd.DataFrame = pd.DataFrame({"sample_b": [7, 7, 7, 7]})
        self.sample_b_array: np.array = np.array(self.sample_b["sample_b"])
        self.index: list = [1, 3]
        self.sample_a_final: np.array = np.array([3., 7., 3., 3.])
        self.sample_b_final: np.array = np.array([7., 7., 7., 3.])
        self.Probador_Diferencias_Significativas: Tester_Significant_Difference = Tester_Significant_Difference()

    def switch_elements_arrays(self):
        self.A_inicial = self.sample_a_array
        self.B_inicial = self.sample_b_array
        self.A_final: np.array = np.copy(self.A_inicial)
        self.A_final[self.index[0]] = B[self.index[1]]
        self.B_final: np.array = np.copy(self.B_inicial)
        self.B_final[self.index[1]] = A[self.index[0]]
        return(self.A_final, self.B_final)

    def test_initialization(self):
        """
        Verifica que los objetos de las clase `Tester_Significant_Difference` se construyan de manera correcta. 
        """
        self.assertEqual(
            type(self.Probador_Diferencias_Significativas),
            Tester_Significant_Difference,
        )

    def test_read_samples(self):
        """
        Verifica que los objetos de las clase `Tester_Significant_Difference` cargue la muestras a comparar. 
        """
        self.Probador_Diferencias_Significativas.sample_a = self.sample_a
        muestra_a: np.array = self.Probador_Diferencias_Significativas.sample_a
        self.assertTrue((self.sample_a_array == muestra_a).all())

        self.Probador_Diferencias_Significativas.sample_b = self.sample_b
        muestra_b: np.array = self.Probador_Diferencias_Significativas.sample_b
        self.assertTrue((self.sample_b_array == muestra_b).all())


    def test_switch_elements(self):
        """
        Verifica que los objetos de las clase `Tester_Significant_Difference` permute dos elementos 
        de las muestras. 
        """
        self.Probador_Diferencias_Significativas.sample_a = self.sample_a
        self.Probador_Diferencias_Significativas.sample_b = self.sample_b
        self.Probador_Diferencias_Significativas.switch_elements_arrays(self.index)
        muestra_a: np.array = self.Probador_Diferencias_Significativas.sample_a
        self.assertTrue((self.sample_a_final == muestra_a).all())
        muestra_b: np.array = self.Probador_Diferencias_Significativas.sample_b
        self.assertTrue((self.sample_b_final == muestra_b).all())

if __name__ == "__main__":
    unittest.main()
