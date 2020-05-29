import matplotlib.pyplot as plt
import numpy as np


class ImageProcessor():
    """image display"""

    def load(self, path):
        nparray = plt.imread(path)
        return nparray

    def display(self, array):
        img = plt.imshow(array)
        plt.show()

    def juxtapose(self, array, n, axis):
        return np.concatenate((array, np.tile(array, n)), axis)
