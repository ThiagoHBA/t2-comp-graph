from abc import ABC, abstractmethod
from typing import List, Tuple, Any

class PolygonObject(ABC):
    vertexes: Any = None  
    edges: Any = None
    faces: Any = None

    def make(self):
        self.createEdges()
        self.createFaces()

    def createEdges(self):
        print("Create edges called")
        pass

    def createFaces(self):
        print("Create faces called")
        pass

    @abstractmethod
    def createVertex(self, point_list):
        pass
