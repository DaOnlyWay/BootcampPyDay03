import numpy as np


class ColorFilter():
    """color filter"""

    def invert(self, array):
        tmp = array[:]
        tmp[:] = 1.0 - tmp[:]
        return array

    def to_blue(self, array):
        new = array[:, :, :2] = 0
        return array

    def to_green(self, array):
        array[:, :, 0:3:2] = 0
        return array

    def to_red(self, array):
        array[:, :, 1:3] = 0
        return array
