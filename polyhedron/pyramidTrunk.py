from core.polygon_object import PolygonObject


class PyramidTrunk(PolygonObject):
    lowerBaseSize = 0.0
    higherBaseSize = 0.0
    heigth = 0.0

    def __init__(self, lowerBaseSize, higherBaseSize, heigth):
        self.lowerBaseSize = lowerBaseSize
        self.higherBaseSize = higherBaseSize
        self.height = heigth

    def create(self):
        self.vertexes = self.createVertex()
        self.make()
        return self

    def createVertex(self):
        lowerBaseSize = self.lowerBaseSize / 2
        higherBaseSize = self.higherBaseSize / 2
        baseYOrigin = (self.height / 2)
        return [
            #LowerBase
            [lowerBaseSize, -baseYOrigin, lowerBaseSize],
            [lowerBaseSize, -baseYOrigin, -lowerBaseSize],
            [-lowerBaseSize, -baseYOrigin, -lowerBaseSize],
            [-lowerBaseSize, -baseYOrigin, lowerBaseSize],
            #higherBase
            [higherBaseSize, baseYOrigin, higherBaseSize],
            [higherBaseSize, baseYOrigin, -higherBaseSize],
            [-higherBaseSize, baseYOrigin, -higherBaseSize],
            [-higherBaseSize, baseYOrigin, higherBaseSize],
        ]

    def createEdges(self):
        self.edges = [
            #LowerBase
            [self.vertexes[0], self.vertexes[1]],
            [self.vertexes[1], self.vertexes[2]],
            [self.vertexes[2], self.vertexes[3]],
            [self.vertexes[3], self.vertexes[0]],
            #Conecting with top
            [self.vertexes[4], self.vertexes[5]],
            [self.vertexes[5], self.vertexes[6]],
            [self.vertexes[6], self.vertexes[7]],
            [self.vertexes[7], self.vertexes[4]],
            #Conecting
            [self.vertexes[0], self.vertexes[4]],
            [self.vertexes[1], self.vertexes[5]],
            [self.vertexes[2], self.vertexes[6]],
            [self.vertexes[3], self.vertexes[7]],
        ]

    def createFaces(self):         
        self.faces = [
            #lowerBaseFaces
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
            #Base+Top Faces
            #TODO
        ]