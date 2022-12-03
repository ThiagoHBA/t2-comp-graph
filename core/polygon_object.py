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

    @abstractmethod
    def createVertex(self, point_list):
        pass
