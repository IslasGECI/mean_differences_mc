import unittest
from mean_differences_mc import *

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

    def test_switch_elements(self):
        """
        Verifica que la función `make_dict_from_id_index` genere el diccionario correcto. 
        """
        A_final, B_final = switch_elements(self.A_initial, self.B_initial, self.index)
        self.assertEqual(self.A_final, A_final)
        self.assertEqual(self.A_final, A_final)

if __name__ == '__main__':
    unittest.main()