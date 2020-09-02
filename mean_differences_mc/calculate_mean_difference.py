import numpy as np
from mean_differences_mc import *


def calculate_mean_difference(minuend, subtrahend):
    mean_minuend = np.mean(minuend)
    mean_subtrahend = np.mean(subtrahend)
    mean_diference = mean_minuend - mean_subtrahend
    return mean_diference


def calculate_mean_switched_difference(minuend, subtrahend, switches):
    max_lim = len(minuend) - 1
    minuend_switched = minuend
    subtrahend_switched = subtrahend
    mean_switched_difference = []
    for _ in range(switches):
        index_test = index_to_switch(max_lim)
        minuend_switched, subtrahend_switched = switch_elements(
            minuend_switched, subtrahend_switched, index_test
        )
        mean_defference = calculate_mean_difference(minuend_switched, subtrahend_switched)
        mean_switched_difference.append(mean_defference)
    return mean_switched_difference


def calculate_p_value_from_difference(difference, difference_array):
    mask = np.array(difference_array) >= difference
    significant_diferences = np.sum([mask])
    return significant_diferences / len(difference_array)
