import numpy as np
a = np.array([1, 2, 3])
b = np.array([3, 4, 5])
class Vector(object):
    def vector_norm(self, vector1):
        print("Норма вектора - "+np.sum(np.abs(vector1)))
    def add_vectors(self, vector1, vector2):
        print("Сумма векторов: "+vector1+" + "+vector2+" = {}".format(vector1+vector2))
    def sub_vectors(self, vector1, vector2):
        print("Вектор вычитания: "+vector1+" - "+vector2+" = {}".format(vector1 - vector2))
    def scalar_product(self, vector1, vector2):
        print("Скалярное произведение векторов равно "+np.dot(vector1, vector2))
    def vector_product(self, vector1, vector2):
        print("Векторное произведение векторов равно "+np.cross(vector1, vector2))
    def vector_on_constant(self, vector1, k):
        new_vector = k * vector1
        print("Умнжение вектора на число "+k+" равно "+(k * new_vector))
    def matrix_multiplication(self, matrix1, matrix2):
        np.dot(matrix1, matrix2) # one more variant - matrix1 @ matrix2
    def element_wise_multiplicsation(self, matrix1, matrix2):
        np.multiply(matrix1, matrix2)
        np.multiply(matrix1, matrix1)
        np.multiply(matrix2, matrix2)
    def transpose(self, matrix):
        matrix.T
    def determinant(self,matrix):
        np.linalg.det(matrix)
    def trace(self, matrix):
        np.transpose(matrix)
    def identity_matrix(self, n):
        np.eye(n)