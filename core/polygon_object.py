from abc import ABC, abstractmethod
from typing import List, Tuple, Any

class PolygonObject(ABC):
    vertexes = []  
    edges = []
    faces = []

    def make(self):
        self.createEdges()
        self.createFaces()

    def createEdges(self):
        pass

    def createFaces(self):
        pass

    def printVertexes(self):
        size = len(self.vertexes)
        for i in range(size):
            print("{}: {}".format(i + 1, self.vertexes[i]))

    @abstractmethod
    def createVertex(self, point_list):
        pass
