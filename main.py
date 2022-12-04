from core.plot import Plot
from core.transformations import Transformations
from polyhedron.cube import Cube
from polyhedron.parallelepiped import Parallelepiped
from polyhedron.pyramid import Pyramid
from polyhedron.pyramidTrunk import PyramidTrunk
import matplotlib.pyplot as plt

def main():
    cube = Cube(edgeSize = 3.0).create()
    parallelepiped = Parallelepiped(width=3.0, heigth=3.0, depth=6.0).create()
    pyramid = Pyramid(baseSize=3.0, heigth=3.0).create()
    pyramidTrunk = PyramidTrunk(lowerBaseSize=3.0, higherBaseSize=6.0, heigth=8.0).create()

    scaleMatrix = Transformations.scaleMatrix(x=2, y=2, z=2)
    rotationMatrix = Transformations.rotationMatrix(alpha=45)
    cube.rotate(rotationMatrix)
    # cube.scaleObject(matrix)
    Plot().plot_objeto(cube)

if __name__ == '__main__':
    main()