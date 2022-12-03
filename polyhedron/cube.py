from core.polygon_object import PolygonObject

class Cube(PolygonObject):
    edgeSize = 0.0

    def __init__(self, edgeSize):
        self.edgeSize = edgeSize

    def create(self):
        self.vertexes = self.createVertex()
        self.make()
        return self

    def createVertex(self):
        center = self.edgeSize/2
        return [
            [center, center, center],
            [center, center, -center],
            [-center, center, -center],
            [-center, center, center],
            [center, -center, center],
            [center,- center, -center],
            [-center, -center, -center],
            [-center, -center, center],
        ]

    def createEdges(self):
        self.edges = [
            [self.vertexes[0], self.vertexes[1]],
            [self.vertexes[1], self.vertexes[2]],
            [self.vertexes[2], self.vertexes[3]],
            [self.vertexes[3], self.vertexes[0]],
            [self.vertexes[4], self.vertexes[5]],
            [self.vertexes[5], self.vertexes[6]],
            [self.vertexes[6], self.vertexes[7]],
            [self.vertexes[7], self.vertexes[4]],
            
            [self.vertexes[0], self.vertexes[4]],
            [self.vertexes[1], self.vertexes[5]],
            [self.vertexes[2], self.vertexes[6]],
            [self.vertexes[3], self.vertexes[7]]
        ]

    def createFaces(self):
         self.faces = [
            [
                self.vertexes[0],
                self.vertexes[1],
                self.vertexes[2],
                self.vertexes[3],
            ], 
            [
                self.vertexes[4],
                self.vertexes[5],
                self.vertexes[6],
                self.vertexes[7],
            ],
            [
                self.vertexes[2],
                self.vertexes[3],
                self.vertexes[7],
                self.vertexes[6],
            ], 
            [
                self.vertexes[1],
                self.vertexes[2],
                self.vertexes[6],
                self.vertexes[5],
            ], 
            [
                self.vertexes[0],
                self.vertexes[1],
                self.vertexes[5],
                self.vertexes[4],
            ],  
            [
                self.vertexes[0],
                self.vertexes[3],
                self.vertexes[7],
                self.vertexes[4],
            ], 
        ]