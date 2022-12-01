from core.polygon_object import PolygonObject

class Cube(PolygonObject):
    @staticmethod 
    def create(edgeSize):
        obj = Cube()
        obj.vertexes = obj.createVertex()
        return obj

    def createVertex(self):
        print("Create vertex called")
        return []