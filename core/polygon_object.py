from abc import ABC, abstractmethod
import numpy as np


class PolygonObject(ABC):
  vertexes = []
  edges = []
  faces = []

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
    
      if matrix.shape[1] == 4:
        for line in matrix:
          finalMatrix.append(line[0:3])
        return np.array(finalMatrix)

      return matrix
      
    transformatedMatrix = transformatedMatrix()
    self.vertexes = transformatedMatrix
    self.make()

  def scale(self, scaleMatrix: np.matrix):
    vertexMatrix = self.__generateHomogeneousMatrix()
    resultant = np.array(np.matmul(vertexMatrix, scaleMatrix))
    self.setVertexes(resultant)

  def rotate(self, rotationMatrix: np.matrix):
    vertexMatrix = self.__generateHomogeneousMatrix()
    resultant =  np.array(np.matmul(vertexMatrix, rotationMatrix))
    self.setVertexes(resultant)

  def translation(self, translationMatrix: np.matrix):
    homogeneousMatrix = self.__generateHomogeneousMatrix()
    resultantMatrix = []
    
    for i in range(len(homogeneousMatrix)):
       result = np.array(np.matmul(translationMatrix, homogeneousMatrix[i]))
       resultantMatrix.append(result[0][:-1])
      
    self.setVertexes(np.array(resultantMatrix))

  def changePerspective(self, perspectiveMatrix: np.matrix):
    vertexMatrix = self.__generateHomogeneousMatrix()
    resultant =  np.array(np.matmul(vertexMatrix, perspectiveMatrix))
    self.setVertexes(resultant)
    
  def multipleTransformations(self, matrix_list: list[np.matrix]):
    if len(matrix_list) > 0:
      resultant = matrix_list[0]
      
      for i in range(1, len(matrix_list)):
        resultant = np.matmul(resultant, matrix_list[i])

      homogeneousMatrix = self.__generateHomogeneousMatrix()
      result = np.array(np.matmul(homogeneousMatrix, resultant))
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
      
    return np.array(homogeneousMatrix)

  @abstractmethod
  def createVertex(self, point_list):
    pass

  def createEdges(self):
    pass

  def createFaces(self):
    pass
