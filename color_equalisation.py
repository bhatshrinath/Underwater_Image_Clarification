import numpy as np

def cal_equalisation(img,ratio):
    """
    Performs color equalization on an image.

    This function multiplies the pixel values of an image by a given ratio, and then clips the resulting values to the range [0, 255] to ensure that they are valid pixel values. This operation can be used to adjust the brightness and contrast of the image.

    Parameters:
    img (numpy.ndarray): The input image. This should be a 3D numpy array with shape (height, width, 3), where the third dimension represents the red, green, and blue color channels.
    ratio (float): The ratio to multiply the pixel values by.

    Returns:
    numpy.ndarray: The equalized image. This is a 3D numpy array with the same shape as the input, where the pixel values have been multiplied by the given ratio and clipped to the range [0, 255].
    """
    Array = img * ratio
    Array = np.clip(Array, 0, 255)
    return Array

def RGB_equalisation(img):
    """
    Performs color equalization on an RGB image.

    This function calculates the average pixel value for each color channel in the image, computes a ratio for each channel by dividing 128 by the average pixel value, and then applies color equalization to each color channel using the `cal_equalisation` function and the computed ratio.

    Parameters:
    img (numpy.ndarray): The input image. This should be a 3D numpy array with shape (height, width, 3), where the third dimension represents the red, green, and blue color channels.

    Returns:
    numpy.ndarray: The equalized image. This is a 3D numpy array with the same shape as the input, where the pixel values in each color channel have been equalized according to the computed ratio.
    """
    img = np.float32(img)
    avg_RGB = []
    for i in range(3):
        avg = np.mean(img[:,:,i])
        avg_RGB.append(avg)
    avg_RGB = 128/np.array(avg_RGB)
    ratio = avg_RGB

    # for i in range(0,2):
    #     img[:,:,i] = cal_equalisation(img[:,:,i],ratio[i])
    for i in range(0,3):
        img[:,:,i] = cal_equalisation(img[:,:,i],ratio[i])
    return img
