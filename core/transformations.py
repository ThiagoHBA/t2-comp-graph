import numpy as np
from math import sin, cos, tan, radians

class Transformations:
    @staticmethod
    def scaleMatrix(x = 1, y = 1, z = 1):
        scaleMatrix = np.matrix([
            [x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]
        ])
        return scaleMatrix

    @staticmethod
    def rotationMatrix(alpha: float, axis = "x"):
        if axis == "x":
            return np.matrix(
            [
              [1, 0, 0, 0],
              [0, cos(alpha), -sin(alpha), 0],
              [0, sin(alpha), cos(alpha), 0],
              [0, 0, 0, 1]
            ])
        if axis == "y":
            return np.matrix(
            [
              [cos(alpha), 0, -sin(alpha), 0],
              [0, 1, 0, 0],
              [sin(alpha), 0, cos(alpha), 0],
              [0, 0, 0, 1]
            ])
        if axis == "z":
            return np.matrix(
            [
              [cos(alpha), sin(alpha), 0, 0],
              [-sin(alpha), cos(alpha), 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]
            ])

        raise Exception()

    @staticmethod 
    def translationMatrix(x = 1, y = 1, z = 1):
        translationMatrix = np.matrix([
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ])

        return translationMatrix
    
    # @staticmethod 
    # def perspectiveMatrix(alpha, z, r = 1):
    #     return np.matrix([
    #         [1/(r*z*tan(alpha/2)), 0, 0, 0],
    #         [0, 1/(z*tan(alpha/2)), 0, 0],
    #         [0, 0, 0, 1/tan(alpha/2)],
    #         [0, 0, 0, 1]
    #     ])

    @staticmethod
    def perspectiveMatrix(alpha, near, far, rad=False, r = 1):
        a = alpha if rad else radians(alpha)

        t = tan(a/2)
        A = far/(far-near)
        B = -far*near/(far-near)

        m = np.array([
            [1/(r*t), 0, 0, 0],
            [0, 1/t, 0, 0],
            [0, 0, A, B],
            [0, 0, 1, 0]
        ])

        return m