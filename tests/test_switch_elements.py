import unittest
from mean_differences_mc import *
from random import seed

class TestSwitchElements(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.A_initial: list = [3, 3, 3, 3]
        self.B_initial: list = [7, 7, 7, 7]
        self.index: list = [1, 3]
        self.A_final: list = [3, 7, 3, 3]
        self.B_final: list = [7, 7, 7, 3]
        self.testing_index: list = [1, 0]
        seed(1)

    def test_switch_elements(self):
        """
        Verifica que la función `switch_elements` genere dos listas con elementos cambiados
        """
        A_final, B_final = switch_elements(self.A_initial, self.B_initial, self.index)
        self.assertEqual(self.A_final, A_final)
        self.assertEqual(self.B_final, B_final)
        A_final, B_final = switch_elements(self.A_final, self.B_final, self.index)
        self.assertEqual(self.A_initial, A_final)
        self.assertEqual(self.B_initial, B_final)

    def test_index_to_switch(self):
        """
        Verifica que la función `index_to_switch` genere dos indices correctos
        """
        index = index_to_switch()
        self.assertEqual(self.testing_index, index)

if __name__ == '__main__':
    unittest.main()