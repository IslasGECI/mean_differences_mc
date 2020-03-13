import unittest
import datetime 
from mean_difference_mc import *


class TestTesterSignificantDifference(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.sample_a : pd.DataFrame = pd.DataFrame({'sample_a' : [3, 3, 3, 3]})
        self.sample_b : pd.DataFrame = pd.DataFrame({'sample_b' : [7, 7, 7, 7]})

    def test_initialization(self):
        """
        Verifica que los objetos de las clase `Trap` se construyan de manera correcta e su propiedad `effort`. 
        """
        Probador_Diferencias_Significativas : Tester_Significant_Difference = Tester_Significant_Difference()


    def test_read_samples(self):
        """
        Verifica que los objetos de las clase `Trap` se construyan de manera correcta e su propiedad `effort`. 
        """

if __name__ == '__main__':
    unittest.main()