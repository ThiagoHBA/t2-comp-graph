import numpy as np
from math import sin, cos

class Transformations:
    @staticmethod
    def scaleMatrix(x = 1, y = 1, z = 1):
        scaleMatrix = np.matrix([[x, 0, 0], [0, y, 0], [0, 0, z]])
        return scaleMatrix

    @staticmethod
    def rotationMatrix(alpha: float):
        rotationMatrix = np.matrix(
            [
                [cos(alpha), -sin(alpha), 0],
                [sin(alpha), cos(alpha), 0],
                [0, 0, 1]
            ])
        return rotationMatrix
