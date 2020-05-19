import unittest
import datetime
import pandas as pd
import numpy as np
from mean_differences_mc import *
from random import seed


class TestTesterSignificantDifference(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.sample_a: pd.DataFrame = pd.DataFrame({"sample_a": [1.0, 2.0, 3.0, 4.0]})
        self.sample_a_array: np.array = np.array(self.sample_a["sample_a"])
        self.sample_b: pd.DataFrame = pd.DataFrame({"sample_b": [5, 6, 7, 8]})
        self.sample_b_array: np.array = np.array(self.sample_b["sample_b"])
        self.index: list = [1, 3]
        self.sample_a_final: np.array = np.array([1., 8., 3., 4.])
        self.sample_b_final: np.array = np.array([5., 6., 7., 2.])
        self.Probador_Diferencias_Significativas: Tester_Significant_Difference = Tester_Significant_Difference()
        self.testing_index: list = [1, 0, 2, 0, 15, 24]
        seed(1)

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
        self.Probador_Diferencias_Significativas.switch_elements(self.index)
        muestra_a: np.array = self.Probador_Diferencias_Significativas.sample_a
        self.assertTrue((self.sample_a_final == muestra_a).all())
        muestra_b: np.array = self.Probador_Diferencias_Significativas.sample_b
        self.assertTrue((self.sample_b_final == muestra_b).all())

    def test_index_to_switch(self):
        """
        Verifica que la función `index_to_switch` genere dos indices correctos
        """
        sample_a: pd.DataFrame = pd.DataFrame({"sample_a": range(3)})
        self.Probador_Diferencias_Significativas.sample_a = sample_a
        index = self.Probador_Diferencias_Significativas.index_to_switch()
        self.assertEqual(self.testing_index[0:2], index)
        index = self.Probador_Diferencias_Significativas.index_to_switch()
        self.assertEqual(self.testing_index[2:4], index)
        sample_a: pd.DataFrame = pd.DataFrame({"sample_a": range(30)})
        self.Probador_Diferencias_Significativas.sample_a = sample_a
        index = self.Probador_Diferencias_Significativas.index_to_switch()
        self.assertEqual(self.testing_index[4:6], index)

if __name__ == "__main__":
    unittest.main()
