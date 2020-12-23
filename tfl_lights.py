from matplotlib import pyplot as plt
import numpy as np
from scipy import signal as sg

def get_coordinates(image, kernel, channel, brightness):
    convolved = sg.convolve(image[:, :, channel], kernel[:, :, channel], mode = 'full')
    plt.imshow(convolved, cmap='gray')
    coordinates = np.argwhere(convolved > brightness) #TODO get the max point of an area
    return coordinates.tolist


def get_red_coordinates(image):
    img_for_kernel = plt.imread('tfl_for_kernel.png')
    red_kernel = img_for_kernel[90:95, 1460:1465] # TODO change the crope? [87:92, 1455:1460]
    return get_coordinates(image, red_kernel, 0, 20.4)


def get_green_coordinates(image):
    img_for_kernel = plt.imread('tfl_for_kernel.png')
    green_kernel = img_for_kernel[127:132, 1420:1425]
    return get_coordinates(image, green_kernel, 1, 20.4)


def get_tfls(image_name):
    image = plt.imread(image_name)
    red_coordinates = get_red_coordinates(image)
    green_coordinates = get_green_coordinates(image)
    return red_coordinates + green_coordinates, ['R'] * len(red_coordinates) + ['G'] *len(green_coordinates)
    # plt.plot(green_coordinates[:, 1], green_coordinates[:, 0], 'g+')
    # plt.plot(red_coordinates[:, 1], red_coordinates[:, 0], 'r+')
    # plt.show()


get_tfls('tfl_for_kernel.png')
