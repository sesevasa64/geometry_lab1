import copy
from typing import *
import vectorNd as Vector


class Mat:
    def __init__(self, values: List[List[float]]):
        self.values = values

    def __mul__(self, other) -> Union['Mat', 'Vector.Vec']:
        if isinstance(other, Vector.Vec):
            return self._mul_vector(other)
        return self._mul_matrix(other)

    def __getitem__(self, index: int) -> List[float]:
        return self.values[index]

    def __setitem__(self, index: int, values: List[float]):
        self.values[index] = values

    def __str__(self) -> str:
        return f"Mat{self.values}"

    def _mul_vector(self, vec: 'Vector.Vec'):
        import trans
        return vec.from_list(trans.Trans.vec_mat_multiply(vec, self))

    def _mul_matrix(self, mat: 'Mat'):
        import trans
        return self.__class__(trans.Trans.mat_mat_multiply(self, mat))

    def row(self) -> int:
        return len(self.values)

    def column(self) -> int:
        return len(self.values[0])

    @staticmethod
    def _zero(size):
        res = []
        for i in range(size):
            res.append([])
            for j in range(size):
                res[i].append(0)
        return res

    @staticmethod
    def _unit(size):
        res = Mat._zero(size)
        for i in range(size):
            res[i][i] = 1
        return res

    @staticmethod
    def unit(size) -> 'Mat':
        return Mat(Mat._unit(size))

    @staticmethod
    def zero(size) -> 'Mat':
        return Mat(Mat._zero(size))

    def copy(self) -> 'Mat':
        return Mat(copy.deepcopy(self.values))

    @staticmethod
    def __not_zero_row(mat: 'Mat', idx: int) -> int:
        for k in range(idx, mat.row()):
            if mat[k][idx] != 0:
                return k
        return -1

    def triangular(self):
        c = self.copy()
        for i in range(c.row()-1):
            index = Mat.__not_zero_row(c, i)
            if index == -1:
                return
            (c[i], c[index]) = (c[index], c[i])
            for j in range(i+1, c.row()):
                val = -c[j][i] / c[i][i]
                c[j] = [val * c[i][t] + c[j][t] for t in range(c.column())]
        return c

    def det(self) -> float:
        c = self.triangular()
        res = 1
        for i in range(c.row()):
            res *= c[i][i]
        return res

    def inverse(self):
        c = self.copy()
        r = Mat.unit(c.row())
        for i in range(c.row()):
            index = Mat.__not_zero_row(c, i)
            if index == -1:
                return
            (c[i], c[index]) = (c[index], c[i])
            (r[i], r[index]) = (r[index], r[i])
            tmp = c[i][i]
            c[i] = [c[i][t] / tmp for t in range(c.column())]
            r[i] = [r[i][t] / tmp for t in range(r.column())]
            # print(f'i = {i}')
            # print(c[i], end=' ')
            # print(r[i])
            j = (i + 1) % c.row()
            while j != i:
                # print(f'j = {j}')
                for t in range(c.row()):
                    tmp = c[j][t]
                    c[j][t] = -tmp * c[i][t] + tmp
                    r[j][t] = -tmp * r[i][t] + r[j][t]
                # print(c[j], end=' ')
                # print(r[j])
                # print('------------')
                j = (j + 1) % c.row()
        return r
