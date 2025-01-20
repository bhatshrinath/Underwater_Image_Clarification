from scipy import stats
import numpy as np


def stretchrange(r_array, height, width):
    """
    Calculates the mode of an array and uses it to compute a lower bound and a specific value in the sorted array.

    This function flattens and sorts the input array, calculates its mode, and then uses the mode to compute a lower bound and a specific value in the sorted array. The lower bound is computed as (1 - 0.655) times the mode, and the specific value is the value located at a certain position in the sorted array, relative to the position of the mode.

    Parameters:
    r_array (numpy.ndarray): The input array. This should be a 2D numpy array representing an image or a channel of an image.
    height (int): The height of the image.
    width (int): The width of the image.

    Returns:
    tuple: A tuple containing three values: the computed lower bound, the specific value in the sorted array, and the mode of the array.
    """
    length = height * width
    R_rray = r_array.flatten()
    R_rray.sort()
    print('R_rray', R_rray)
    mode = stats.mode(R_rray).mode[0]
    mode_index_before = list(R_rray).index(mode)
    # count = stats.mode(R_rray).count[0]

    DR_min = (1-0.655) * mode

    SR_max = R_rray[int(-(length - mode_index_before) * 0.005)]

    print('mode', mode)
    print('DR_min', DR_min)
    print('SR_max', SR_max)

    return DR_min, SR_max, mode