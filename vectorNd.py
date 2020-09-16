from typing import *
import matrixNd as Matrix


class Vec:
    def __init__(self, *args):
        self.values = list(args)

    def __str__(self) -> str:
        return f"Vec{self.values}"

    def __add__(self, other: 'Vec') -> 'Vec':
        return self._add(other)

    def __sub__(self, other: 'Vec') -> 'Vec':
        return self._sub(other)

    def __mul__(self, other: Union['Matrix.Mat', float]) -> 'Vec':
        if isinstance(other, Matrix.Mat):
            return self._mul_matrix(other)
        return self._mul_scalar(other)

    def __rmul__(self, other: float) -> 'Vec':
        return self._mul_scalar(other)

    def __truediv__(self, scalar: float) -> 'Vec':
        return self._div_scalar(scalar)

    def __getitem__(self, index: int) -> float:
        return self.values[index]

    def __setitem__(self, index: int, value: float):
        self.values[index] = value

    def len(self) -> int:
        return len(self.values)

    def normie(self) -> 'Vec':
        return self / self[self.len() - 1]

    def from_list(self, values: List[float]):
        vec = self.__class__()
        vec.values = values
        return vec

    def _add(self, other):
        return self.from_list([v1 + v2 for (v1, v2) in zip(self.values, other.values)])

    def _sub(self, other: 'Vec'):
        return self.from_list([v1 - v2 for (v1, v2) in zip(self.values, other.values)])

    def _div_scalar(self, scalar: float):
        return self.from_list([val / scalar for val in self.values])

    def _mul_matrix(self, matrix: 'Matrix.Mat'):
        import trans
        return self.from_list(trans.Trans.vec_mat_multiply(self, matrix))

    def _mul_scalar(self, scalar: float):
        return self.from_list([val * scalar for val in self.values])
