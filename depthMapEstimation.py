import numpy as np

def depthMap(img):
    """
    Calculates a depth map of an image.

    This function calculates a depth map of an image based on a linear combination of the image's color channels. The depth map is calculated as theta_0 + theta_1 * x_1 + theta_2 * x_2, where x_1 is the maximum of the red and green channels, x_2 is the blue channel, and theta_0, theta_1, and theta_2 are predefined coefficients.

    Parameters:
    img (numpy.ndarray): The input image. This should be a 3D numpy array with shape (height, width, 3), where the third dimension represents the red, green, and blue color channels.

    Returns:
    numpy.ndarray: The depth map of the image. This is a 2D numpy array with the same height and width as the image.
    """
    theta_0 = 0.51157954
    theta_1 = 0.50516165
    theta_2 = -0.90511117
    img = img / 255.0
    x_1 = np.maximum(img[:, :, 0], img[:, :, 1])
    x_2 = img[:, :, 2]
    Deptmap = theta_0 + theta_1 * x_1 + theta_2 * x_2

    return Deptmap



