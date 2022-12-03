from polyhedron.cube import Cube
from typing import NewType

from polyhedron.parallelepiped import Parallelepiped

def main():
    cube = Cube(edgeSize = 3.0).create()
    parallelepiped = Parallelepiped(width=3.0, heigth=3.0, depth=3.0).create()
    

if __name__ == '__main__':
    main()