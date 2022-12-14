from abc import ABC, abstractmethod
import numpy as np

from core.transformations import Transformations


class PolygonObject(ABC):
  vertexes = []
  edges = []
  faces = []
  color = "black"

  def make(self):
    self.createEdges()
    self.createFaces()

  def printVertexes(self):
    size = len(self.vertexes)
    for i in range(size):
      print("{}: {}".format(i + 1, self.vertexes[i]))

  def setVertexes(self, matrix: np.array):
    def transformatedMatrix():
      finalMatrix = []
      
      if matrix.shape[0] == 4:
        for line in matrix.T:
          finalMatrix.append(list(line.flat[0:3].flat))
        return np.array(finalMatrix)

      return matrix
      
    transformatedMatrix = transformatedMatrix()
    self.vertexes = transformatedMatrix
    self.make()

  def scale(self, scaleMatrix: np.matrix):
    currentPoint = self.getObjectCenter()

    self.multipleTransformations([
      Transformations.translationMatrix(-currentPoint[0], -currentPoint[1], -currentPoint[2]),
      scaleMatrix,
      Transformations.translationMatrix(currentPoint[0], currentPoint[1], currentPoint[2])
    ])

  def rotate(self, rotationMatrix: np.matrix):
    currentPoint = self.getObjectCenter()

    self.multipleTransformations([
      Transformations.translationMatrix(-currentPoint[0], -currentPoint[1], -currentPoint[2]),
      rotationMatrix,
      Transformations.translationMatrix(currentPoint[0], currentPoint[1], currentPoint[2])
    ])

  def translation(self, translationMatrix: np.matrix):
    homogeneousMatrix = self.__generateHomogeneousMatrix()
    resultant = np.matmul(translationMatrix, homogeneousMatrix)
    self.setVertexes(resultant)

  def changePerspective(self, perspectiveMatrix: list[np.matrix], vertex: int):
    homogeneousMatrix = self.__generateHomogeneousMatrix()
    homogeneousMatrix = homogeneousMatrix.T
    homogeneousMatrix[vertex] = np.matmul(perspectiveMatrix, homogeneousMatrix[vertex])
    
    self.setVertexes(homogeneousMatrix.T)
    
  def multipleTransformations(self, matrix_list: list[np.matrix]):
    if len(matrix_list) > 0:
      resultant = matrix_list[0]
      
      for i in range(1, len(matrix_list)):
        resultant = np.matmul(matrix_list[i], resultant)

      homogeneousMatrix = self.__generateHomogeneousMatrix()
      result = np.matmul(resultant, homogeneousMatrix)
      self.setVertexes(result)

  def getObjectCenter(self):
    xAxis = np.array(self.vertexes)[:,0]
    yAxis = np.array(self.vertexes)[:,1]
    zAxis = np.array(self.vertexes)[:,2]

    center = (np.mean(xAxis), np.mean(yAxis), np.mean(zAxis))
    return center

  @staticmethod
  def getVolumeCenter(objects):
    centers = []
    for polygon in objects:
        objectCenter = polygon.getObjectCenter()
        centers.append(objectCenter)

    xAxis = np.mean(np.array(centers)[:,0])
    yAxis = np.mean(np.array(centers)[:,1])
    zAxis = np.mean(np.array(centers)[:,2])
    
    volumeCenter = (xAxis, yAxis, zAxis)
    return volumeCenter

  def __generateHomogeneousMatrix(self):
    homogeneousMatrix = []

    for (x, y, z) in self.vertexes:
      homogeneousMatrix.append([x, y, z, 1])
      
    return np.array(homogeneousMatrix).T

  @abstractmethod
  def createVertex(self, point_list):
    pass

  def createEdges(self):
    pass

  def createFaces(self):
    pass
