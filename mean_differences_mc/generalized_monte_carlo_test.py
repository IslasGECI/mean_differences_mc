from mean_differences_mc import *


def generalized_monte_carlo_test(sample_a, sample_b, switches):
    is_different_length = len(sample_a) != len(sample_b)
    if is_different_length:
        raise ValueError("sample_a and sample_b must be of the same length")
    mean_switched_differences = calculate_mean_switched_difference(sample_a, sample_b, switches)
    mean_difference = calculate_mean_difference(sample_a, sample_b)
    p_value = calculate_p_value_from_difference(
        difference=mean_difference, difference_array=mean_switched_differences
    )
    return p_value