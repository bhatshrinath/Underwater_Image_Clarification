import cv2
from skimage.color import rgb2hsv,hsv2rgb
import numpy as np
from skimage.color import rgb2lab, lab2rgb

from global_StretchingL import global_stretching
from global_stretching_ab import global_Stretching_ab


def  LABStretching(sceneRadiance):
    """
    Performs a stretching operation on an image in the LAB color space.

    This function clips the pixel values of the input image to the range [0, 255], converts the image to 8-bit unsigned integer format, converts the image from RGB to LAB color space, applies the `global_stretching` function to the L channel and the `global_Stretching_ab` function to the a and b channels, creates a new 3D array with the stretched channels, converts the array back to RGB color space, scales the pixel values by 255, and returns the resulting image.

    Parameters:
    sceneRadiance (np.ndarray): The input image.

    Returns:
    np.ndarray: The output image after the stretching operation.
    """
    sceneRadiance = np.clip(sceneRadiance, 0, 255)
    sceneRadiance = np.uint8(sceneRadiance)
    height = len(sceneRadiance)
    width = len(sceneRadiance[0])
    img_lab = rgb2lab(sceneRadiance)
    L, a, b = cv2.split(img_lab)

    img_L_stretching = global_stretching(L, height, width)
    img_a_stretching = global_Stretching_ab(a, height, width)
    img_b_stretching = global_Stretching_ab(b, height, width)

    labArray = np.zeros((height, width, 3), 'float64')
    labArray[:, :, 0] = img_L_stretching
    labArray[:, :, 1] = img_a_stretching
    labArray[:, :, 2] = img_b_stretching
    img_rgb = lab2rgb(labArray) * 255

    return img_rgb
