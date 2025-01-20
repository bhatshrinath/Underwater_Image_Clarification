import numpy as np


def stretching(img):
    """
    Performs global contrast stretching on an RGB image.

    This function enhances the contrast of an image by stretching the range of color values in each channel to span the full range of [0, 255]. This is done independently for each color channel, which can help to correct for color imbalances in the image.

    Parameters:
    img (numpy.ndarray): The input image. This should be a 3D numpy array with shape (height, width, 3), where the third dimension represents the red, green, and blue color channels.

    Returns:
    numpy.ndarray: The contrast-stretched image. This is a 3D numpy array with the same shape as the input, where the pixel values in each color channel have been scaled to span the full range of [0, 255].
    """
    height = len(img)
    width = len(img[0])
    for k in range(0, 3):
        Max_channel  = np.max(img[:,:,k])
        Min_channel  = np.min(img[:,:,k])
        for i in range(height):
            for j in range(width):
                img[i,j,k] = (img[i,j,k] - Min_channel) * (255 - 0) / (Max_channel - Min_channel)+ 0
    return img



