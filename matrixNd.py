import copy
from typing import *
import vectorNd as Vector


class Mat:
    data_type = Vector.Vec

    def __init__(self, values: List[List[float]]):
        if not Mat.is_rectangular(values):
            raise ValueError()
        self.values = []
        for val in values:
            self.values.append(self._new_vec(val))

    def __str__(self) -> str:
        res = "Mat("
        last = len(self.values) - 1
        for i in range(last):
            res += f"{self.values[i]}, "
        res += f"{self.values[last]})"
        return res

    def __getitem__(self, index: int) -> Vector.Vec:
        return self.values[index]

    def __setitem__(self, index: int, values: Vector.Vec):
        self.values[index] = values

    def __mul__(self, other: Union['Mat', 'Vector.Vec', float]) -> Union['Mat', 'Vector.Vec']:
        return self._mul(other)

    def __rmul__(self, other: Union['Mat', 'Vector.Vec', float]) -> Union['Mat', 'Vector.Vec']:
        return self._mul(other)

    def __truediv__(self, scalar: float):
        return self._mul(1 / scalar)

    def __add__(self, mat: 'Mat'):
        if not Mat.is_equal_row_and_column(self, mat):
            raise ValueError()
        return self._add(mat)

    def __sub__(self, mat: 'Mat'):
        if not Mat.is_equal_row_and_column(self, mat):
            raise ValueError()
        return self._sub(mat)

    def _mul(self, other):
        if isinstance(other, Vector.Vec):
            if self.row() != other.len():
                raise ValueError()
            return self._mul_vector(other)
        if isinstance(other, Mat):
            if self.row() != other.column() or \
               self.column() != other.row():
                raise ValueError()
            return self._mul_matrix(other)
        if isinstance(other, float):
            return self._mul_scalar(other)
        return NotImplemented

    @classmethod
    def _empty_mat(cls, row: int):
        mat = cls([])
        mat.values = [Mat.data_type()] * row
        return mat

    def _add(self, mat):
        res = Mat._empty_mat(self.row())
        for i in range(res.row()):
            res[i] = self[i] + mat[i]
        return res

    def _sub(self, mat):
        res = Mat._empty_mat(self.row())
        for i in range(res.row()):
            res[i] = self[i] - mat[i]
        return res

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

    def copy(self) -> 'Mat':
        return copy.deepcopy(self)

    def row(self) -> int:
        return len(self.values)

    def column(self) -> int:
        return self.values[0].len()

    @staticmethod
    def is_rectangular(values: List[List[float]]):
        for i in range(1, len(values)):
            if len(values[i]) != len(values[i-1]):
                return False
        return True

    @staticmethod
    def is_equal_row_and_column(mat1: 'Mat', mat2: 'Mat'):
        return mat1.row() == mat2.row() and \
               mat1.column() == mat2.column()
