import numpy as np
import math


def  minDepth(img, BL):
    """
    Calculates the minimum depth of an image.

    This function calculates the minimum depth of an image given the image and its background light. The minimum depth is calculated based on the maximum absolute difference between each color channel in the image and the corresponding color channel in the background light.

    Parameters:
    img (numpy.ndarray): The input image. This should be a 3D numpy array with shape (height, width, 3), where the third dimension represents the red, green, and blue color channels.
    BL (numpy.ndarray): The background light of the image. This should be a 1D numpy array with 3 elements, representing the red, green, and blue components of the background light.

    Returns:
    float: The minimum depth of the image.
    """
    img = img/255.0
    BL = BL/255.0
    Max = []
    img = np.float32(img)
    for i in range(0,3):
        Max_Abs =  np.absolute(img[i] - BL[i])
        Max_I = np.max(Max_Abs)
        Max_B = np.max([BL[i],(1 -BL[i])])
        temp  = Max_I / Max_B
        Max.append(temp)
    K_b = np.max(Max)
    min_depth = 1 - K_b

    return min_depth



