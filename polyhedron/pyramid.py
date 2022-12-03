from core.polygon_object import PolygonObject

class Pyramid(PolygonObject):
    baseSize = 0.0
    heigth = 0.0

    def __init__(self, baseSize, heigth):
        self.baseSize = baseSize
        self.height = heigth

    def create(self):
        self.vertexes = self.createVertex()
        self.make()
        return self

    def createVertex(self):
        base = self.baseSize / 2
        baseYOrigin = (self.height / 2)
        return [
            #heigthOrigin
            [0, baseYOrigin, 0],
            #base
            [base, -baseYOrigin, base],
            [base, -baseYOrigin, -base],
            [-base, -baseYOrigin, -base],
            [-base, -baseYOrigin, base],
        ]

    def createEdges(self):
        self.edges = [
            #Base
            [self.vertexes[1], self.vertexes[2]],
            [self.vertexes[2], self.vertexes[3]],
            [self.vertexes[3], self.vertexes[4]],
            [self.vertexes[4], self.vertexes[1]],
            #Conecting with top
            [self.vertexes[1], self.vertexes[0]],
            [self.vertexes[2], self.vertexes[0]],
            [self.vertexes[3], self.vertexes[0]],
            [self.vertexes[4], self.vertexes[0]]
        ]

    def createFaces(self):
         self.faces = [
            #Base faces
            [
                self.vertexes[1],
                self.vertexes[2],
                self.vertexes[3],
                self.vertexes[4],
            ], 
            #Base+Top Faces
            [self.vertexes[0], self.vertexes[1], self.vertexes[4]], 
            [self.vertexes[1], self.vertexes[2], self.vertexes[4]], 
            [self.vertexes[2], self.vertexes[3], self.vertexes[4]],
            [self.vertexes[3], self.vertexes[0], self.vertexes[4]], 
        ]