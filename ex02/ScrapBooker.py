import numpy as np


class ScrapBooker():
    """image gestion"""

    def crop(array, dimensions, position=(0, 0)):
        if dimensions[1] <= array.shape[0] and dimensions[0] <= array.shape[1]:
            return(array[position[1]:dimensions[1] + position[1],
                         position[0]:dimensions[0] + position[0]])

    def thin(self, array, n, axis):
        if axis == 1:
            return np.delete(array, [range(n-1, array.shape[0], n)], 0)
        if axis == 0:
            return np.delete(array, [range(n-1, array.shape[1], n)], 1)

    def juxtapose(array, n, axis):
        return np.concatenate([array for i in range[n], axis])

    def mosaic(self, array, dimensions):
        return np.tile(array, dimensions)
