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
        self.sample_a : pd.DataFrame = pd.DataFrame({'sample_a' : [3., 3., 3., 3.]})
        self.sample_a_array : np.array = np.array(self.sample_a['sample_a'])
        self.sample_b : pd.DataFrame = pd.DataFrame({'sample_b' : [7, 7, 7, 7]})
        self.sample_b_array : np.array = np.array(self.sample_b['sample_b'])
        self.Probador_Diferencias_Significativas : Tester_Significant_Difference = Tester_Significant_Difference()

    def test_initialization(self):
        """
        Verifica que los objetos de las clase `Tester_Significant_Difference` se construyan de manera correcta. 
        """
        self.assertEqual(type(self.Probador_Diferencias_Significativas), Tester_Significant_Difference)

    def test_read_samples(self):
        """
        Verifica que los objetos de las clase `Tester_Significant_Difference` cargue la muestras a comparar. 
        """
        self.Probador_Diferencias_Significativas.sample_a = self.sample_a
        muestra_a : np.array = self.Probador_Diferencias_Significativas.sample_a
        self.assertTrue((self.sample_a_array == muestra_a).all())

        self.Probador_Diferencias_Significativas.sample_b = self.sample_b
        muestra_b : np.array = self.Probador_Diferencias_Significativas.sample_b
        self.assertTrue((self.sample_b_array == muestra_b).all())

if __name__ == '__main__':
    unittest.main()