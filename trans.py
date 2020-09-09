from typing import *
import vectorNd as Vector
import matrixNd as Matrix


class Trans:
    @staticmethod
    def vec_mat_multiply(vec: Vector.Vec, mat: Matrix.Mat) -> Vector.Vec:
        size = vec.len()
        res = [0] * size
        for i in range(size):
            for j in range(size):
                res[i] += mat[j][i] * vec[j]
        return Vector.Vec(res)

    @staticmethod
    def mat_mat_multiply(m1: Matrix.Mat, m2: Matrix.Mat) -> Matrix.Mat:
        res = []
        for i in range(m1.row()):
            res.append([])
            for j in range(m2.column()):
                res[i].append(0)
                for k in range(m1.column()):
                    res[i][j] += m1[i][k] * m2[k][j]
        return Matrix.Mat(res)
