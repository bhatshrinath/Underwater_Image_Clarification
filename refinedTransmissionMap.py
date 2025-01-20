import cv2
import numpy as np

from GuidedFilter import GuidedFilter


def  refinedtransmissionMap(transmissionB,transmissionG,transmissionR,img):
    """
    Refines the transmission maps of the blue, green, and red channels of an image using a guided filter.

    This function initializes a `GuidedFilter` with the input image, a radius of 50, and a regularization parameter of 10^-3, applies the guided filter to the transmission maps of the blue, green, and red channels, creates a new 3D array with the filtered transmission maps, and returns this array.

    Parameters:
    transmissionB (np.ndarray): The transmission map of the blue channel.
    transmissionG (np.ndarray): The transmission map of the green channel.
    transmissionR (np.ndarray): The transmission map of the red channel.
    img (np.ndarray): The input image.

    Returns:
    np.ndarray: The refined transmission map.
    """
    gimfiltR = 50
    eps = 10 ** -3
    guided_filter = GuidedFilter(img, gimfiltR, eps)
    transmissionB = guided_filter.filter(transmissionB)
    transmissionG = guided_filter.filter(transmissionG)
    transmissionR = guided_filter.filter(transmissionR)

    transmission = np.zeros(img.shape)
    transmission[:, :, 0] = transmissionB
    transmission[:, :, 1] = transmissionG
    transmission[:, :, 2] = transmissionR
    return transmission
