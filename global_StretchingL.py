import numpy as np

def global_stretching(img_L,height, width):
    """
    Performs a global histogram stretching operation on a 2D array.

    This function scales the elements in the input array to the range [0, 100] based on the 1 percentile and 99 percentile of the elements. Elements less than the 1 percentile are set to 0, and elements greater than the 99 percentile are set to 100.

    Parameters:
    img_L (numpy.ndarray): The input array. This should be a 2D numpy array with shape (height, width).
    height (int): The height of the array.
    width (int): The width of the array.

    Returns:
    numpy.ndarray: A 2D numpy array with the same shape as the input, where each element has been scaled to the range [0, 100] based on the global histogram stretching operation.
    """
    length = height * width
    R_rray = (np.copy(img_L)).flatten()
    R_rray.sort()
    print('R_rray',R_rray)
    I_min = int(R_rray[int(length / 100)])
    I_max = int(R_rray[-int(length / 100)])
    print('I_min',I_min)
    print('I_max',I_max)
    array_Global_histogram_stretching_L = np.zeros((height, width))
    for i in range(0, height):
        for j in range(0, width):
            if img_L[i][j] < I_min:
                p_out = img_L[i][j]
                array_Global_histogram_stretching_L[i][j] = 0
            elif (img_L[i][j] > I_max):
                p_out = img_L[i][j]
                array_Global_histogram_stretching_L[i][j] = 100
            else:
                p_out = int((img_L[i][j] - I_min) * ((100) / (I_max - I_min)))
                array_Global_histogram_stretching_L[i][j] = p_out
    return (array_Global_histogram_stretching_L)

