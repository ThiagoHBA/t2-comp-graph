from core.plot import Plot
from core.transformations import Transformations
from polyhedron.cube import Cube
from polyhedron.parallelepiped import Parallelepiped
from polyhedron.pyramid import Pyramid
from polyhedron.pyramidTrunk import PyramidTrunk

def main():
    showQ1()

def showQ1():
    cube = Cube(edgeSize = 3.0).create()
    parallelepiped = Parallelepiped(width=3.0, heigth=3.0, depth=6.0).create()
    pyramid = Pyramid(baseSize=3.0, heigth=3.0).create()
    pyramidTrunk = PyramidTrunk(lowerBaseSize=3.0, higherBaseSize=6.0, heigth=8.0).create()
  
    cube.multipleTransformations([
      Transformations.rotationMatrix(45),
      Transformations.scaleMatrix(1, 2, 3)
    ])

    cube.translation(Transformations.translationMatrix(2, 3, -4))

    Plot(size=(10,10)).plot_object(cube)

def showQ2():
    cube = Cube(edgeSize = 3.0).create()
    parallelepiped = Parallelepiped(width=3.0, heigth=3.0, depth=6.0).create()
    pyramid = Pyramid(baseSize=6.0, heigth=6.0).create()
    pyramidTrunk = PyramidTrunk(lowerBaseSize=3.0, higherBaseSize=6.0, heigth=8.0).create()

    pyramid.translation(Transformations.translationMatrix(10, 5, 4))
    cube.translation(Transformations.translationMatrix(15,10, 4))
    parallelepiped.translation(Transformations.translationMatrix(-15, 2, 10))
    pyramidTrunk.translation(Transformations.translationMatrix(-10, 5, 10))

    cube.scale(Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2))
    parallelepiped.scale(Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2))
    pyramid.scale(Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2))
    pyramidTrunk.scale(Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2))

    objectLists = [cube, parallelepiped, pyramidTrunk, pyramid]

    verifyObjects(objects=objectLists)
    Plot(size=(20,20)).plot_mutiple_objects(objects=objectLists)

def verifyObjects(objects):
    for polygon in objects:
            for i in range(len(polygon.vertexes)):
                for j in range(len(polygon.vertexes[i])):
                    if polygon.vertexes[i][j] > 10:
                        print("O OBJETO {} tem um vertice maior que 10, de valor: {}".format(polygon, polygon.vertexes[i][j]))

if __name__ == '__main__':
    main()