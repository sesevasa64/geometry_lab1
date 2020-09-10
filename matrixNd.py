from typing import *
from math import *
import trans
import vectorNd as Vector


class Mat:
    def __init__(self, values: List[List]):
        self.values = values

    def __mul__(self, other) -> Union['Mat', 'Vector.Vec']:
        if isinstance(other, Vector.Vec):
            return trans.Trans.vec_mat_multiply(other, self)
        if isinstance(other, Mat):
            return trans.Trans.mat_mat_multiply(self, other)
        raise NotImplementedError()

    def size(self) -> int:
        return len(self.values)

    def row(self) -> int:
        return len(self.values)

    def column(self) -> int:
        return len(self.values[0])

    def __str__(self) -> str:
        return f"Mat{self.values}"

    def __getitem__(self, index) -> List:
        return self.values[index]

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
