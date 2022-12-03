from core.polygon_object import PolygonObject

class Parallelepiped(PolygonObject):
    width = 0.0
    height = 0.0
    depth = 0.0

    def __init__(self, width, heigth, depth):
        self.width = width
        self.height = heigth
        self.depth = depth

    def create(self):
        self.vertexes = self.createVertex()
        self.make()
        return self

    def createVertex(self):
        width, heigth, depth = self.width/2, self.height/2, self.depth/2
        return [
            [width, heigth, depth],
            [width, heigth, -depth],
            [-width, heigth,-depth],
            [-width, heigth, depth],
            [width, -heigth, depth],
            [width, -heigth, -depth],
            [-width, -heigth, -depth],
            [-width, -heigth, depth],
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