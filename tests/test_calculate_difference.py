import unittest
from mean_differences_mc import *

class TestCalculateDifference(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.A_initial: list = [3, 3, 3, 3]
        self.B_initial: list = [7, 7, 7, 7]
        self.difference: int = -16

    def test_calculate_difference(self):
        """
        Verifica que la función `calcualate_diference` genere el diccionario correcto. 
        """
        difference = calculate_difference(self.A_initial, self.B_initial)
        self.assertEqual(self.difference, difference)

if __name__ == '__main__':
    unittest.main()