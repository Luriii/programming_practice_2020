import numpy as np
class Vector(object):
    def vector_norm(self, vector1):
        norm = str(np.sum(np.abs(vector1)))
        print("Норма вектора - " + norm)
    def add_vectors(self, vector1, vector2):
        print("Сумма векторов: "+str(vector1)+" + "+str(vector2)+" = "+str(vector1+vector2))
    def sub_vectors(self, vector1, vector2):
        print("Вектор вычитания: "+str(vector1)+" - "+str(vector2)+" = "+str(vector1 - vector2))
    def scalar_product(self, vector1, vector2):
        print("Скалярное произведение векторов равно "+str(np.dot(vector1, vector2)))
    def vector_product(self, vector1, vector2):
        print("Векторное произведение векторов равно "+str(np.cross(vector1, vector2)))
    def vector_on_constant(self, vector1, k):
        print("Умнжение вектора "+str(vector1)+" на число "+str(k)+" равно "+str((k * vector1)))
c, d = Vector(), Vector()
c.vector_on_constant(np.array([1, 2, 4]), 2)