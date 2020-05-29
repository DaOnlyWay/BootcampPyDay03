import numpy


class NumPyCreator():
    """Numpy tests"""

    def __init__(self):
        pass

    def from_list(self, args):
        print(numpy.array(args))
        return numpy.array(args)

    def from_tuple(self, args):
        print(numpy.array(args))
        return numpy.array(args)

    def from_iterable(self, args):
        print(numpy.array(args))
        return(numpy.array(args))

    def from_shape(self, shape, value=0):
        print(numpy.full(shape, value))
        return(numpy.full(shape, value))

    def random(self, shape):
        print(numpy.random.sample(shape))
        return(numpy.random.sample(shape))

    def identity(self, n):
        print(numpy.identity(n))
        return(numpy.identity(n))


nc = NumPyCreator()
nc.from_list([[1, 2, 3], [4, 5, 6]])
nc.from_tuple((1, 2, 3))
nc.from_iterable(range(5))
shape = (3, 5)
nc.from_shape(shape, 1)
nc.random(shape)
nc.identity(4)
