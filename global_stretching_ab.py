import numpy as np
import math
e = math.e

def global_Stretching_ab(a,height, width):
    """
    Performs a global histogram stretching operation on a 2D array.

    This function applies a non-linear transformation to each element in the input array, which can enhance the contrast in an image. The transformation is defined as `a[i][j] * (1.3 ** (1 - math.fabs(a[i][j] / 128)))`.

    Parameters:
    a (numpy.ndarray): The input array. This should be a 2D numpy array with shape (height, width).
    height (int): The height of the array.
    width (int): The width of the array.

    Returns:
    numpy.ndarray: A 2D numpy array with the same shape as the input, where each element has been transformed by the global histogram stretching operation.
    """
    array_Global_histogram_stretching_L = np.zeros((height, width), 'float64')
    for i in range(0, height):
        for j in range(0, width):
                p_out = a[i][j] * (1.3 ** (1 - math.fabs(a[i][j] / 128)))
                array_Global_histogram_stretching_L[i][j] = p_out
    return (array_Global_histogram_stretching_L)
