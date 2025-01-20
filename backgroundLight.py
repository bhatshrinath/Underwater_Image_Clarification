import numpy as np
import cv2


def BLEstimation(img, DepthMap):
    """
    Estimates the background light of an image.

    This function estimates the background light of an image by considering the colors of the brightest pixels in the image. The color with the largest magnitude is selected as the estimated background light.

    Parameters:
    img (numpy.ndarray): The input image. This should be a 3D numpy array with shape (height, width, 3), where the third dimension represents the red, green, and blue color channels.
    DepthMap (numpy.ndarray): The depth map of the image. This should be a 2D numpy array with the same height and width as the image.

    Returns:
    numpy.ndarray: The estimated background light. This is a 1D numpy array with 3 elements, representing the red, green, and blue components of the estimated background light.
    """
    h, w, c = img.shape
    if img.dtype == np.uint8:
        img = np.float32(img) / 255
    n_bright = int(np.ceil(0.001 * h * w))
    reshaped_Jdark = DepthMap.reshape(1, -1)
    Y = np.sort(reshaped_Jdark)
    Loc = np.argsort(reshaped_Jdark)
    Ics = img.reshape(1, h * w, 3)
    ix = img.copy()
    dx = DepthMap.reshape(1, -1)
    Acand = np.zeros((1, n_bright, 3), dtype=np.float32)
    Amag = np.zeros((1, n_bright, 1), dtype=np.float32)
    for i in range(n_bright):
        x = Loc[0, h * w - 1 - i]
        j = int(x / w)
        k = int(x % w)
        ix[j, k, 0] = 0
        ix[j, k, 1] = 0
        ix[j, k, 2] = 1
        Acand[0, i, :] = Ics[0, Loc[0, h * w - 1 - i], :]
        Amag[0, i] = np.linalg.norm(Acand[0, i, :])
    reshaped_Amag = Amag.reshape(1, -1)
    Y2 = np.sort(reshaped_Amag)

    Loc2 = np.argsort(reshaped_Amag)
    A_1 = Acand[0, Loc2[0, (n_bright - 1):n_bright], :]

    A_1 = A_1[0]

    return A_1
