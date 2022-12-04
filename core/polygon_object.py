from abc import ABC, abstractmethod
import numpy as np

class PolygonObject(ABC):
    vertexes = []  
    edges = []
    faces = []

    def make(self):
        self.createEdges()
        self.createFaces()

    def printVertexes(self):
        size = len(self.vertexes)
        for i in range(size):
            print("{}: {}".format(i + 1, self.vertexes[i]))

    def scale(self, scaleMatrix: np.matrix):
        vertexMatrix = self.__vertexMatrix()
        self.vertexes = np.array(np.matmul(vertexMatrix,scaleMatrix))
        self.make()

    def rotate(self, rotationMatrix: np.matrix):
        vertexMatrix = self.__vertexMatrix()
        self.vertexes = np.array(np.matmul(vertexMatrix, rotationMatrix))
        self.make()

    def translation(self, translationMatrix: np.matrix):
        homogeneousMatrix = self.__generateHomogeneousMatrix()
        resultantMatrix = []

        for i in range(len(homogeneousMatrix)):
            result = np.array(np.matmul(translationMatrix, homogeneousMatrix[i]))
            resultantMatrix.append(result[0][:-1])

        self.vertexes = resultantMatrix
        self.make()

    def __vertexMatrix(self):
        return np.matrix(self.vertexes)

    def __generateHomogeneousMatrix(self):
        homogeneousMatrix = []
        for (x, y, z) in self.vertexes:
            homogeneousMatrix.append([x, y , z, 1])
        return np.array(homogeneousMatrix)

    @abstractmethod
    def createVertex(self, point_list):
        pass

    def createEdges(self):
        pass

    def createFaces(self):
        pass

