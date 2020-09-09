from typing import *
import trans
import matrixNd as Matrix


class Vec:
    def __init__(self, values: List):
        self.values = values

    def len(self) -> int:
        return len(self.values)

    def __str__(self) -> str:
        return f"Vec{self.values}"

    def __add__(self, other: 'Vec') -> 'Vec':
        return Vec([v1 + v2 for (v1, v2) in zip(self.values, other.values)])

    def __sub__(self, other: 'Vec') -> 'Vec':
        return Vec([v1 - v2 for (v1, v2) in zip(self.values, other.values)])

    def __mul__(self, other) -> 'Vec':
        if isinstance(other, Matrix.Mat):
            return trans.Trans.vec_mat_multiply(self, other)
        return Vec([val * other for val in self.values])

    def __rmul__(self, other) -> 'Vec':
        return Vec([val * other for val in self.values])

    def __truediv__(self, scalar) -> 'Vec':
        return Vec([val / scalar for val in self.values])

    def __getitem__(self, index) -> int:
        return self.values[index]

    def normie(self):
        return self / self[self.len() - 1]

