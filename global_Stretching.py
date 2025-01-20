import numpy as np

def global_stretching(img_L):
    """
    Performs a global histogram stretching operation on a 2D array.

    This function scales the elements in the input array to the range [0, 1] based on the 0.05 percentile and 99.95 percentile of the elements. Elements less than the 0.05 percentile are set to 0, and elements greater than the 99.95 percentile are set to 1.

    Parameters:
    img_L (numpy.ndarray): The input array. This should be a 2D numpy array with shape (height, width).

    Returns:
    numpy.ndarray: A 2D numpy array with the same shape as the input, where each element has been scaled to the range [0, 1] based on the global histogram stretching operation.
    """
    height = len(img_L)
    width = len(img_L[0])
    length = height * width
    R_rray = []
    for i in range(height):
        for j in range(width):
            R_rray.append(img_L[i][j])
    R_rray.sort()
    I_min = R_rray[int(length / 2000)]
    I_max = R_rray[-int(length / 2000)]
    # print('I_min',I_min)
    # print('I_max',I_max)
    array_Global_histogram_stretching_L = np.zeros((height, width))
    for i in range(0, height):
        for j in range(0, width):
            if img_L[i][j] < I_min:
                p_out = img_L[i][j]
                array_Global_histogram_stretching_L[i][j] = 0
            elif (img_L[i][j] > I_max):
                p_out = img_L[i][j]
                array_Global_histogram_stretching_L[i][j] = 1
            else:
                p_out = (img_L[i][j] - I_min) * ((1-0) / (I_max - I_min))+ 0
                array_Global_histogram_stretching_L[i][j] = p_out
    return (array_Global_histogram_stretching_L)

