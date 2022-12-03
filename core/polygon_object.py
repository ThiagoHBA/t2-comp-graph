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

    def scaleObject(self, scaleMatrix: np.matrix):
        vertexMatrix = np.matrix(self.vertexes)
        self.vertexes = np.array(np.matmul(vertexMatrix,scaleMatrix))
        self.make()

    @abstractmethod
    def createVertex(self, point_list):
        pass

    def createEdges(self):
        pass

    def createFaces(self):
        pass

