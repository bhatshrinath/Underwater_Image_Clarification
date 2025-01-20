import numpy as np


def sceneRadianceRGB(img, transmission, AtomsphericLight):
    """
    Calculates the scene radiance of an image given the image, its transmission map, and the atmospheric light.

    This function initializes a 3D array of the same size as the input image with all elements set to zero, converts the image to a floating-point array, calculates the scene radiance for each channel of the image, sets the intensity of each pixel of the scene radiance to 255 if it's greater than 255 and to 0 if it's less than 0, converts the scene radiance to an unsigned integer array, and returns it.

    Parameters:
    img (np.ndarray): The input image.
    transmission (np.ndarray): The transmission map of the image.
    AtomsphericLight (list): The atmospheric light of the image.

    Returns:
    np.ndarray: The scene radiance of the image.
    """
    sceneRadiance = np.zeros(img.shape)
    img = np.float16(img)
    for i in range(0, 3):
        sceneRadiance[:, :, i] = (img[:, :, i] - AtomsphericLight[i]) / transmission[:, :, i]  + AtomsphericLight[i]

        for j in range(0, sceneRadiance.shape[0]):
            for k in range(0, sceneRadiance.shape[1]):
                if sceneRadiance[j, k, i] > 255:
                    sceneRadiance[j, k, i] = 255
                if sceneRadiance[j, k, i] < 0:
                    sceneRadiance[j, k, i] = 0
    sceneRadiance = np.uint8(sceneRadiance)

    return sceneRadiance


