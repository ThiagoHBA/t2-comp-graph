from polyhedron.cube import Cube
from polyhedron.parallelepiped import Parallelepiped
from polyhedron.pyramid import Pyramid
from polyhedron.pyramidTrunk import PyramidTrunk

def main():
    cube = Cube(edgeSize = 3.0).create()
    parallelepiped = Parallelepiped(width=3.0, heigth=3.0, depth=3.0).create()
    pyramid = Pyramid(baseSize=3.0, heigth=3.0).create()
    pyramidTrunk = PyramidTrunk(lowerBaseSize=3.0, higherBaseSize=6.0, heigth=8.0).create()

    print(pyramidTrunk.vertexes)

if __name__ == '__main__':
    main()