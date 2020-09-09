from typing import *
from math import *
import trans
import vectorNd as Vector


class Mat:
    def __init__(self, values: List[List]):
        self.values = values

    def row(self) -> int:
        return len(self.values)

    def column(self) -> int:
        return len(self.values[0])

    def __str__(self) -> str:
        return f"Mat{self.values}"

    def __mul__(self, other) -> Union['Mat', 'Vector.Vec']:
        if isinstance(other, Vector.Vec):
            return trans.Trans.vec_mat_multiply(other, self)
        if isinstance(other, Mat):
            return trans.Trans.mat_mat_multiply(self, other)
        raise NotImplementedError()

    def __getitem__(self, index) -> List:
        return self.values[index]

    @staticmethod
    def rotate(size, angle) -> 'Mat':
        if size == 2:
            return Mat([[cos(angle), sin(angle)],
                        [-sin(angle)], cos(angle)])
        raise NotImplementedError()

    @staticmethod
    def unit(size) -> 'Mat':
        res = Mat.zero(size)
        for i in range(size):
            res[i][i] = 1
        return res

    @staticmethod
    def zero(size) -> 'Mat':
        res = []
        for i in range(size):
            res.append([])
            for j in range(size):
                res[i].append(0)
        return Mat(res)

    @staticmethod
    def unit2() -> 'Mat':
        return Mat.unit(2)

    @staticmethod
    def mirror_OY() -> 'Mat':
        return Mat([[-1, 0],
                    [0, 1]])

    @staticmethod
    def mirror_OX() -> 'Mat':
        return Mat([[1, 0],
                    [0, -1]])

    @staticmethod
    def mirror_OO() -> 'Mat':
        return Mat([[-1, 0],
                    [0, -1]])

    @staticmethod
    def mirror_45d() -> 'Mat':
        return Mat([[0, 1],
                    [1, 0]])

    @staticmethod
    def mirror_135d() -> 'Mat':
        return Mat([[0, -1],
                    [-1, 0]])

    @staticmethod
    def scale_OX(a) -> 'Mat':
        return Mat([[a, 0],
                    [0, 1]])

    @staticmethod
    def scale_OY(d) -> 'Mat':
        return Mat([[1, 0],
                    [0, d]])

    @staticmethod
    def distortion_OX(c) -> 'Mat':
        return Mat([[1, 0],
                    [c, 1]])

    @staticmethod
    def distortion_OY(b) -> 'Mat':
        return Mat([[1, b],
                    [0, 1]])

    @staticmethod
    def common3(mat: 'Mat') -> 'Mat':
        if not (mat.row() == 2 and mat.column() == 2):
            raise ValueError()
        res = Mat.unit(3)
        for i in range(mat.row()):
            for j in range(mat.column()):
                res[i][j] = mat[i][j]
        return res

    @staticmethod
    def parallel3(k, _l) -> 'Mat':
        res = Mat.unit(3)
        res[0][2] = k
        res[1][2] = _l
        return res

    @staticmethod
    def scale3(s) -> 'Mat':
        res = Mat.unit(3)
        res[2][2] = s
        return res

    @staticmethod
    def project3(p, q) -> 'Mat':
        res = Mat.unit(3)
        res[2][0] = p
        res[2][1] = q
        return res

    @staticmethod
    def rotate_around_point(angle, k, _l) -> 'Mat':
        res = Mat.common3(Mat.rotate(3, angle))
        res[0][2] = k
        res[1][2] = _l
        return res
