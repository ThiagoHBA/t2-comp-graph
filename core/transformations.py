import numpy as np

class Transformations:
    @staticmethod
    def scale(x = 1, y = 1, z = 1):
        matrix = np.matrix([[x, 0, 0], [0, y, 0], [0, 0, z]])
        return matrix