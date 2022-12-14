import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from typing import List
from core.polygon_object import PolygonObject

class Plot:
    size = (0.0, 0.0)

    def __init__(self, size = (10, 10)):
        self.size = size

    def initialize_plot(self):
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(111, projection="3d")
        return fig, ax

    def initialize_axis(self, ax):
        ax.set_xlabel("Eixo X")
        ax.set_ylabel("Eixo Y")
        ax.set_zlabel("Eixo Z")

        # ax.plot([5.2, -5.2], [0, 0], [0, 0], color='Black', alpha=0.4)
        # ax.plot([0, 0], [5.2, -5.2], [0, 0], color='Black', alpha=0.4)
        # ax.plot([0, 0], [0, 0], [5.2, -5.2], color='Black', alpha=0.4)

    def plot_object(self, objeto: PolygonObject):
        _, ax = self.initialize_plot()

        for line in objeto.edges:
            ax.plot(
                [line[0][0], line[1][0]],
                [line[0][1], line[1][1]],
                zs=[line[0][2], line[1][2]],
            )

        # ax.add_collection3d(Poly3DCollection(objeto.faces, linewidths=1.5))

        ax.set_zlim3d(-self.size[0], self.size[1])
        ax.set_xlim3d(-self.size[0], self.size[1])
        ax.set_ylim3d(-self.size[0], self.size[1])

        self.initialize_axis(ax)
        plt.show()


    def plot_mutiple_objects(self, objects: List[PolygonObject]):
        _, ax = self.initialize_plot()
        
        for polygon in objects:
            for line in polygon.edges:
                ax.plot(
                    [line[0][0], line[1][0]],
                    [line[0][1], line[1][1]],
                    zs=[line[0][2], line[1][2]],
                )

        ax.set_zlim3d(-self.size[0], self.size[1])
        ax.set_xlim3d(-self.size[0], self.size[1])
        ax.set_ylim3d(-self.size[0], self.size[1])

        self.initialize_axis(ax)
        plt.show()