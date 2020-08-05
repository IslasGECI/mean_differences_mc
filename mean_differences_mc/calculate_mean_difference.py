import numpy as np


def calculate_mean_difference(minuend, subtrahend):
    mean_minuend = np.mean(minuend)
    mean_subtrahend = np.mean(subtrahend)
    mean_diference = mean_minuend - mean_subtrahend
    return mean_diference
