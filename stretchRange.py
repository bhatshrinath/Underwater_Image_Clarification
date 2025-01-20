from scipy import stats
import numpy as np

def stretchrange(r_array, height, width):
    """
    Calculates the minimum and maximum stretch range and the mode of a 2D array representing a single channel of an image.

    This function calculates the total number of elements in the array, creates a sorted list of all elements in the array, calculates the mode of the list, finds the index of the mode in the list, calculates the minimum stretch range as the element at the index `mode_index_before * 0.005` in the list, calculates the maximum stretch range as the element at the index `-(length - mode_index_before) * 0.005` in the list, and returns these values.

    Parameters:
    r_array (np.ndarray): The input 2D array.
    height (int): The height of the array.
    width (int): The width of the array.

    Returns:
    tuple: The minimum stretch range, the maximum stretch range, and the mode.
    """
    length = height * width
    R_rray = r_array.flatten()
    R_rray.sort()
    print('R_rray', R_rray)
    mode = stats.mode(R_rray).mode[0]
    mode_index_before = list(R_rray).index(mode)
 
    SR_min = R_rray[int(mode_index_before * 0.005)]
    SR_max = R_rray[int(-(length - mode_index_before) * 0.005)]

    print('mode',mode)
    print('SR_min',SR_min)
    print('SR_max',SR_max)

    return SR_min, SR_max, mode