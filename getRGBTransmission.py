import numpy as np
import math


def getRGBTransmissionESt(depth_map):
    """
    Calculates the transmission maps for the red, green, and blue color channels of an image.

    This function calculates each transmission map as a power of the depth map, with a different base for each color channel. The bases are 0.97 for blue, 0.95 for green, and 0.83 for red.

    Parameters:
    depth_map (numpy.ndarray): The depth map of the image. This should be a 2D numpy array with the same height and width as the image.

    Returns:
    tuple: A tuple containing three 2D numpy arrays representing the transmission maps for the blue, green, and red color channels, respectively.
    """
    transmissionB = 0.97 ** depth_map
    transmissionG = 0.95 ** depth_map
    transmissionR = 0.83 ** depth_map

    return transmissionB, transmissionG, transmissionR
