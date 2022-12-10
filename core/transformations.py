import numpy as np
from math import sin, cos

class Transformations:
    @staticmethod
    def scaleMatrix(x = 1, y = 1, z = 1):
        scaleMatrix = np.matrix([
          # [x, 0, 0], [0, y, 0], [0, 0, z]
            [x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]
        ])
        return scaleMatrix

    @staticmethod
    def rotationMatrix(alpha: float):
        rotationMatrix = np.matrix(
            [
              [1, 0, 0, 0],
              [0, cos(alpha), -sin(alpha), 0],
              [0, sin(alpha), cos(alpha), 0],
              [0, 0, 0, 1]
                # [cos(alpha), -sin(alpha), 0],
                # [sin(alpha), cos(alpha), 0],
                # [0, 0, 1]
            ])
        return rotationMatrix

    @staticmethod 
    def translationMatrix(x = 1, y = 1, z = 1):
        translationMatrix = np.matrix([
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ])

        return translationMatrix