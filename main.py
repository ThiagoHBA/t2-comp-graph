from core.plot import Plot
from core.polygon_object import PolygonObject
from core.transformations import Transformations
from polyhedron.cube import Cube
from polyhedron.parallelepiped import Parallelepiped
from polyhedron.pyramid import Pyramid
from polyhedron.pyramidTrunk import PyramidTrunk
import numpy as np

def main():
    showQ4()

def showQ1():
    cube = Cube(edgeSize = 3.0).create()
    parallelepiped = Parallelepiped(width=3.0, heigth=3.0, depth=6.0).create()
    pyramid = Pyramid(baseSize=3.0, heigth=3.0).create()
    pyramidTrunk = PyramidTrunk(lowerBaseSize=3.0, higherBaseSize=6.0, heigth=8.0).create()
  
    cube.multipleTransformations([
      Transformations.rotationMatrix(90),
      Transformations.scaleMatrix(1, 2, 3)
    ])

    cube.translation(Transformations.translationMatrix(2, 3, -4))

    Plot(size=(10,10)).plot_object(cube)

def showQ2():
    cube = Cube(edgeSize = 3.0).create()
    parallelepiped = Parallelepiped(width=2.0, heigth=2.0, depth=5.0).create()
    pyramid = Pyramid(baseSize=5.0, heigth=5.0).create()
    pyramidTrunk = PyramidTrunk(lowerBaseSize=2.0, higherBaseSize=5.0, heigth=7.0).create()
    
    cube.multipleTransformations([
        Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2),
        Transformations.translationMatrix(7.5,5, 2)
    ])

    pyramid.multipleTransformations([
        Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2),
        Transformations.translationMatrix(5, 2.5, 2)
    ])

    parallelepiped.multipleTransformations([
        Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2),
        Transformations.translationMatrix(-7.5, 1, 5)
    ])

    pyramidTrunk.multipleTransformations([
        Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2),
        Transformations.translationMatrix(-5, 2.5, 5)
    ])

    objectLists = [cube, parallelepiped, pyramidTrunk, pyramid]

    verifyObjects(objects=objectLists)
    Plot(size=(10,10)).plot_multiple_objects(objects=objectLists)

def showQ3():
    cube = Cube(edgeSize = 3.0).create()
    parallelepiped = Parallelepiped(width=2.0, heigth=2.0, depth=5.0).create()
    pyramid = Pyramid(baseSize=5.0, heigth=5.0).create()
    pyramidTrunk = PyramidTrunk(lowerBaseSize=2.0, higherBaseSize=5.0, heigth=7.0).create()

    cube.multipleTransformations([
        Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2),
        Transformations.translationMatrix(7.5,5, 2)
    ])

    pyramid.multipleTransformations([
        Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2),
        Transformations.translationMatrix(5, 2.5, 2)
    ])

    parallelepiped.multipleTransformations([
        Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2),
        Transformations.translationMatrix(-7.5, 1, 5)
    ])

    pyramidTrunk.multipleTransformations([
        Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2),
        Transformations.translationMatrix(-5, 2.5, 5)
    ])

    objectLists = [cube, parallelepiped, pyramidTrunk, pyramid]

    cube.color = "red"
    parallelepiped.color = "green"
    pyramid.color = "black"
    pyramidTrunk.color = "blue"

    eyePoint = (5, -7.5, 0.5)
    volumeCenter = PolygonObject.getVolumeCenter(objects=objectLists)

    for polygon in objectLists:
        polygon.translation(Transformations.translationMatrix(-eyePoint[0], -eyePoint[1], -eyePoint[2]))
        
    cameraSystem = changeBase(eyePoint, volumeCenter)

    for polygon in objectLists:
        polygon.setVertexes(np.matmul(polygon.vertexes, cameraSystem))

    eye = Cube(edgeSize = 1.0).create()
    mediumPoint = Cube(edgeSize = 0.5).create()

    eye.translation(Transformations.translationMatrix(eyePoint[0], eyePoint[1], eyePoint[2]))
    eye.translation(Transformations.translationMatrix(-eyePoint[0], -eyePoint[1], -eyePoint[2]))

    mediumPoint.translation(Transformations.translationMatrix(volumeCenter[0], volumeCenter[1], volumeCenter[2]))
    mediumPoint.translation(Transformations.translationMatrix(-eyePoint[0], -eyePoint[1], -eyePoint[2]))

    objectLists.append(eye)
    objectLists.append(mediumPoint)

    Plot(size=(15,15)).plot_multiple_objects(objects=objectLists)

def showQ4():
    cube = Cube(edgeSize = 3.0).create()
    parallelepiped = Parallelepiped(width=2.0, heigth=2.0, depth=5.0).create()
    pyramid = Pyramid(baseSize=5.0, heigth=5.0).create()
    pyramidTrunk = PyramidTrunk(lowerBaseSize=2.0, higherBaseSize=5.0, heigth=7.0).create()

    cube.multipleTransformations([
        Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2),
        Transformations.translationMatrix(7.5,5, 2)
    ])

    pyramid.multipleTransformations([
        Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2),
        Transformations.translationMatrix(5, 2.5, 2)
    ])

    parallelepiped.multipleTransformations([
        Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2),
        Transformations.translationMatrix(-7.5, 1, 5)
    ])

    pyramidTrunk.multipleTransformations([
        Transformations.scaleMatrix(x=1/2, y=1/2, z=1/2),
        Transformations.translationMatrix(-5, 2.5, 5)
    ])

    objectLists = [cube, parallelepiped, pyramidTrunk, pyramid]

    cube.color = "red"
    parallelepiped.color = "green"
    pyramid.color = "black"
    pyramidTrunk.color = "blue"

    eyePoint = (5, -7.5, 0.5)
    volumeCenter = PolygonObject.getVolumeCenter(objects=objectLists)

    for polygon in objectLists:
        polygon.translation(Transformations.translationMatrix(-eyePoint[0], -eyePoint[1], -eyePoint[2]))
        
    cameraSystem = changeBase(eyePoint, volumeCenter)

    for polygon in objectLists:
        polygon.setVertexes(np.matmul(polygon.vertexes, cameraSystem))

    for polygon in objectLists:
        for i in range (len(polygon.vertexes)):
            perspectiveMatrix = Transformations.perspectiveMatrix(alpha=45, z=polygon.vertexes[i][2])
            polygon.changePerspective(perspectiveMatrix=perspectiveMatrix, vertex = i)

    # eye = Cube(edgeSize = 1.0).create()
    # eye.translation(Transformations.translationMatrix(10, -15, 1))
    # eye.translation(Transformations.translationMatrix(-10, 15, -1))

    # objectLists.append(eye)

    Plot(size=(20,20)).plot_multiple_2D_objects(objectLists)

def changeBase(eyePoint, volumeCenter):
    eyeDirection = np.subtract(eyePoint, volumeCenter)
    ortogonalVector = np.array(np.matmul(eyeDirection, Transformations.rotationMatrix(90)[:-1]))[0][0:3]
    internalProduct = np.cross(eyeDirection, ortogonalVector)

    #Normalizing
    nomalizedDirection = (eyeDirection / np.linalg.norm(eyeDirection))
    normalizedOrtogonal = (ortogonalVector / np.linalg.norm(ortogonalVector))
    normalizedInternal = (internalProduct / np.linalg.norm(internalProduct))

    eyeCordinateSystem = [nomalizedDirection, normalizedOrtogonal, normalizedInternal]

    '''
        MUDANÇA DE BASE
    '''

    inverseSystem = np.linalg.inv(eyeCordinateSystem)

    return inverseSystem

def verifyObjects(objects):
    for polygon in objects:
            for i in range(len(polygon.vertexes)):
                for j in range(len(polygon.vertexes[i])):
                    if polygon.vertexes[i][j] > 10:
                        print("O OBJETO {} tem um vertice maior que 10, de valor: {}".format(polygon, polygon.vertexes[i][j]))

if __name__ == '__main__':
    main()