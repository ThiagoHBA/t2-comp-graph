from polyhedron.cube import Cube
from typing import NewType

def main():
    cube = Cube.create(edgeSize=3.0)
    cube.make()

if __name__ == '__main__':
    main()