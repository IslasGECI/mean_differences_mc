import unittest
from mean_differences_mc import *
from random import seed


A_initial_test: list = [3, 3, 3, 3]
B_initial_test: list = [7, 7, 7, 7]
index_test: list = [1, 3]
A_final_test: list = [3, 7, 3, 3]
B_final_test: list = [7, 7, 7, 3]
testing_index: list = [3, 3, 3, 1, 3, 15]
seed(1)

def test_switch_elements():
    """
    Verifica que la función `switch_elements` genere dos listas con elementos cambiados
    """
    A_final, B_final = switch_elements(A_initial_test, B_initial_test, index_test)
    assert A_final_test == A_final
    assert B_final_test == B_final
    A_final, B_final = switch_elements(A_final_test, B_final_test, index_test)
    assert A_initial_test == A_final
    assert B_initial_test == B_final

def test_index_to_switch():
    """
    Verifica que la función `index_to_switch` genere dos indices correctos
    """
    max_lim = 3
    index = index_to_switch(max_lim)
    assert testing_index[0:2] == index
    index = index_to_switch(max_lim)
    assert testing_index[2:4] == index
    max_lim = 30
    index = index_to_switch(max_lim)
    assert testing_index[4:6] == index
