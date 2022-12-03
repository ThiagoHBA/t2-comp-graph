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
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection="3d")
        return fig, ax

    def initialize_eixos(self, ax):
        ax.set_xlabel("Eixo X")
        ax.set_ylabel("Eixo Y")
        ax.set_zlabel("Eixo Z")

        # ax.plot([5.2, -5.2], [0, 0], [0, 0], color='Black', alpha=0.4)
        # ax.plot([0, 0], [5.2, -5.2], [0, 0], color='Black', alpha=0.4)
        # ax.plot([0, 0], [0, 0], [5.2, -5.2], color='Black', alpha=0.4)

    def plot_objeto(self, objeto: PolygonObject):
        _, ax = self.initialize_plot()

        for linha in objeto.edges:
            ax.plot(
                [linha[0][0], linha[1][0]],
                [linha[0][1], linha[1][1]],
                zs=[linha[0][2], linha[1][2]],
            )

        # ax.add_collection3d(Poly3DCollection(objeto.faces, linewidths=1.5))

        ax.set_zlim3d(-5, 5)
        ax.set_xlim3d(-5, 5)
        ax.set_ylim3d(-5, 5)

        self.initialize_eixos(ax)
        plt.show()


    # def plot_objetos(self, objetos: List[PolygonObject]):
    #     fig, ax = init_plot()

    #     for objeto in objetos:
    #         for linha in objeto.arestas:
    #             ax.plot(
    #                 [linha[0][0], linha[1][0]],
    #                 [linha[0][1], linha[1][1]],
    #                 zs=[linha[0][2], linha[1][2]],
    #             )

    #         ax.add_collection3d(Poly3DCollection(objeto.faces, linewidths=1.5))

    #     ax.set_zlim3d(-6, 6)
    #     ax.set_xlim3d(-6, 6)
    #     ax.set_ylim3d(-6, 6)

    #     init_eixos(ax)
    #     plt.show()