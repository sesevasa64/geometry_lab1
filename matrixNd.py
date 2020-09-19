import copy
from typing import *
import vectorNd as Vector


class Mat:
    data_type = Vector.Vec

    def __init__(self, values: List[List[float]]):
        self.values = []
        for val in values:
            self.values.append(self._new_vec(val))

    def __mul__(self, other: Union['Mat', 'Vector.Vec', float]) -> Union['Mat', 'Vector.Vec']:
        return self._mul(other)

    def __rmul__(self, other: Union['Mat', 'Vector.Vec', float]) -> Union['Mat', 'Vector.Vec']:
        return self._mul(other)

    def __truediv__(self, scalar: float):
        return self._mul(1 / scalar)

    def __add__(self, mat: 'Mat'):
        return self._add(mat)

    def __sub__(self, mat: 'Mat'):
        return self._sub(mat)

    def _add(self, mat):
        res = self.__class__(Mat._zero(self.row()))
        for i in range(res.row()):
            res[i] = self[i] + mat[i]
        return res

    def _sub(self, mat):
        res = self.__class__(Mat._zero(self.row()))
        for i in range(res.row()):
            res[i] = self[i] - mat[i]
        return res

    def _mul(self, other):
        if isinstance(other, Vector.Vec):
            return self._mul_vector(other)
        if isinstance(other, Mat):
            return self._mul_matrix(other)
        if isinstance(other, float):
            return self._mul_scalar(other)
        return NotImplemented

    def _new_vec(self, values: List[float]):
        vec = self.__class__.data_type()
        vec.values = values
        return vec

    def _mul_scalar(self, scalar: float):
        mat = self.copy()
        for i in range(self.row()):
            mat[i] = self[i] * scalar
        return mat

    def _mul_vector(self, vec):
        size = vec.len()
        res = [0] * size
        for i in range(size):
            for j in range(size):
                res[i] += self[j][i] * vec[j]
        return vec.from_list(res)

    def _mul_matrix(self, mat):
        res = []
        for i in range(self.row()):
            res.append([])
            for j in range(mat.column()):
                res[i].append(0)
                for k in range(self.column()):
                    res[i][j] += self[i][k] * mat[k][j]
        return self.__class__(res)

    def __getitem__(self, index: int) -> Vector.Vec:
        return self.values[index]

    def __setitem__(self, index: int, values: Vector.Vec):
        self.values[index] = values

    def __str__(self) -> str:
        res = "Mat("
        last = len(self.values) - 1
        for i in range(last):
            res += f"{self.values[i]}, "
        res += f"{self.values[last]})"
        return res

    def copy(self) -> 'Mat':
        res = self.__class__([])
        res.values = copy.deepcopy(self.values)
        return res

    def row(self) -> int:
        return len(self.values)

    def column(self) -> int:
        return self.values[0].len()

    def triangular(self):
        c = self.copy()
        for i in range(c.row()-1):
            index = Mat._not_zero_row(c, i)
            if index == -1:
                return
            (c[i], c[index]) = (c[index], c[i])
            for j in range(i+1, c.row()):
                val = -c[j][i] / c[i][i]
                row = [val * c[i][t] + c[j][t] for t in range(c.column())]
                c[j] = self._new_vec(row)
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
            index = Mat._not_zero_row(c, i)
            if index == -1:
                return
            (c[i], c[index]) = (c[index], c[i])
            (r[i], r[index]) = (r[index], r[i])
            tmp = c[i][i]
            c[i] /= tmp
            r[i] /= tmp
            j = (i + 1) % c.row()
            while j != i:
                tmp = c[j][i]
                c[j] -= c[i] * float(tmp)
                r[j] -= r[i] * float(tmp)
                j = (j + 1) % c.row()
        return r

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

    @staticmethod
    def _not_zero_row(mat: 'Mat', idx: int) -> int:
        for k in range(idx, mat.row()):
            if mat[k][idx] != 0:
                return k
        return -1
