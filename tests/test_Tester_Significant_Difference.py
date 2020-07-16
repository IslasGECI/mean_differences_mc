import unittest
import datetime
import pandas as pd
import numpy as np
from mean_differences_mc import *
from random import seed


sample_a_test: pd.DataFrame = pd.DataFrame({"sample_a": [1.0, 2.0, 3.0, 4.0]})
sample_a_test_array: np.array = np.array(sample_a_test["sample_a"])
sample_b_test: pd.DataFrame = pd.DataFrame({"sample_b": [5, 6, 7, 8]})
sample_b_test_array: np.array = np.array(sample_b_test["sample_b"])
index_test: list = [1, 3]
sample_a_test_final: np.array = np.array([1.0, 8.0, 3.0, 4.0])
sample_b_test_final: np.array = np.array([5.0, 6.0, 7.0, 2.0])
Probador_Diferencias_Significativas_test: Tester_Significant_Difference = Tester_Significant_Difference()
testing_index_test: list = [1, 0, 2, 0, 15, 24]
seed(1)

def test_initialization():
    """
    Verifica que los objetos de las clase `Tester_Significant_Difference` se construyan de manera correcta. 
    """
    assert (
        type(Probador_Diferencias_Significativas_test) == Tester_Significant_Difference,
    )

def test_read_samples():
    """
    Verifica que los objetos de las clase `Tester_Significant_Difference` cargue la muestras a comparar. 
    """
    Probador_Diferencias_Significativas_test.sample_a = sample_a_test
    muestra_a: np.array = Probador_Diferencias_Significativas_test.sample_a
    assert np.array_equal(sample_a_test_array, muestra_a)

    Probador_Diferencias_Significativas_test.sample_b = sample_b_test
    muestra_b: np.array = Probador_Diferencias_Significativas_test.sample_b
    assert np.array_equal(sample_b_test_array, muestra_b)

def test_switch_elements():
    """
    Verifica que los objetos de las clase `Tester_Significant_Difference` permute dos elementos 
    de las muestras. 
    """
    Probador_Diferencias_Significativas_test.sample_a = sample_a_test
    Probador_Diferencias_Significativas_test.sample_b = sample_b_test
    Probador_Diferencias_Significativas_test.switch_elements(index_test)
    muestra_a: np.array = Probador_Diferencias_Significativas_test.sample_a
    assert np.array_equal(sample_a_test_final, muestra_a)
    muestra_b: np.array = Probador_Diferencias_Significativas_test.sample_b
    assert np.array_equal(sample_b_test_final, muestra_b)

def test_index_to_switch():
    """
    Verifica que la función `index_to_switch` genere dos indices correctos
    """
    sample_a: pd.DataFrame = pd.DataFrame({"sample_a": range(3)})
    Probador_Diferencias_Significativas_test.sample_a = sample_a
    index = Probador_Diferencias_Significativas_test.index_to_switch()
    assert testing_index_test[0:2] == index
    index = Probador_Diferencias_Significativas_test.index_to_switch()
    assert testing_index_test[2:4] == index
    sample_a: pd.DataFrame = pd.DataFrame({"sample_a": range(30)})
    Probador_Diferencias_Significativas_test.sample_a = sample_a
    index = Probador_Diferencias_Significativas_test.index_to_switch()
    assert testing_index_test[4:6] == index

