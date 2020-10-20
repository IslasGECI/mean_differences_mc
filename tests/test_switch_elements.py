from random import seed

import pandas as pd
import pytest

from mean_differences_mc import (
    switch_elements,
    index_to_switch,
    calculate_mean_difference,
    calculate_mean_switched_difference,
    calculate_p_value_from_difference,
    generalized_monte_carlo_test,
)


a_initial_test: list = [3, 3, 3, 3]
b_initial_test: list = [7, 7, 7, 7]
index_test: list = [1, 3]
a_final_test: list = [3, 7, 3, 3]
b_final_test: list = [7, 7, 7, 3]
testing_index: list = [1, 0, 2, 0, 15, 24]
expected_mean_switched_difference = [-2.0, -2.0, -2.0, -2.0, -2.0, -2.0]
expected_p_value: float = 0
expected_mean_switched_difference_2 = [4.0, 0.0, 0.0, 0.0, 0.0, 0.0]
expected_p_value_2: float = 1 / 6
chapman_4_2_p_value: float = 0.00
sample_a: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample_b: list = [11, 12, 13, 14, 15, 16, 17, 18, 19]

seed(1)


def test_switch_elements():
    """
    Verifica que la función `switch_elements` genere dos listas con elementos cambiados
    """
    a_final, b_final = switch_elements(a_initial_test, b_initial_test, index_test)
    assert a_final_test == a_final
    assert b_final_test == b_final
    a_final, b_final = switch_elements(a_final_test, b_final_test, index_test)
    assert a_initial_test == a_final
    assert b_initial_test == b_final


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


def test_calculate_mean_difference():
    """
    Verifica que calcula bien las diferencias de los promedios
    """
    expected_mean_difference = -4.0
    obtained_mean_difference = calculate_mean_difference(a_initial_test, b_initial_test)
    assert expected_mean_difference == pytest.approx(obtained_mean_difference, 0.01)
    expected_mean_difference = -2.0
    obtained_mean_difference = calculate_mean_difference(a_final_test, b_final_test)
    assert expected_mean_difference == pytest.approx(obtained_mean_difference, 0.01)


def test_calculate_mean_switched_difference():
    """
    Verifica que calcula un arreglo de diferencias
    """
    obtained_mean_switched_difference = calculate_mean_switched_difference(
        a_initial_test, b_initial_test, n_switches=6
    )
    assert expected_mean_switched_difference == obtained_mean_switched_difference


def test_calculate_p_value_from_difference():
    """
    Verifica que el p-valor sea el correcto
    """
    obtained_p_value = calculate_p_value_from_difference(
        difference=4, difference_array=expected_mean_switched_difference
    )
    assert expected_p_value == pytest.approx(obtained_p_value, rel=1e-3)
    obtained_p_value = calculate_p_value_from_difference(
        difference=4, difference_array=expected_mean_switched_difference_2
    )
    assert expected_p_value_2 == pytest.approx(obtained_p_value, rel=1e-3)


def test_generalized_monte_carlo_test():
    data_chapman_example_4_2 = pd.read_csv("reports/tables/ejemplo_4_2_chapman.csv")
    data_males = _select_sex(data_chapman_example_4_2, "males")
    data_females = _select_sex(data_chapman_example_4_2, "females")
    obtained_p_value = generalized_monte_carlo_test(data_males, data_females, n_switches=100)
    assert chapman_4_2_p_value == obtained_p_value


def _select_sex(data_chapman_example_4_2, sex):
    return (
        data_chapman_example_4_2[data_chapman_example_4_2["sex"] == sex]
        .reset_index(drop=True)["mandible_lengths"]
        .values.tolist()
    )


def test_generalized_monte_carlo_test_value_error():
    with pytest.raises(ValueError, match="^sample_a and sample_b must be of the same length$"):
        generalized_monte_carlo_test(sample_a, sample_b, 10)
