from math import *
from vector2d import *
from matrixNd import *


class Mat2d(Mat):
    data_type = Vec2d

    def __init__(self, values: List[List[float]]):
        super().__init__(values)

    def __mul__(self, other: Union['Mat2d', 'Vec2d', float]) -> Union['Mat2d', 'Vec2d']:
        return self._mul(other)

    def __rmul__(self, other: Union['Mat2d', 'Vec2d', float]) -> Union['Mat2d', 'Vec2d']:
        return self._mul(other)

    def __truediv__(self, scalar: float):
        return self._mul(1 / scalar)

    def __add__(self, mat: 'Mat2d'):
        return self._add(mat)

    def __sub__(self, mat: 'Mat2d'):
        return self._sub(mat)

    def _mul(self, other: Union['Mat2d', float]):
        if isinstance(other, Vec2d):
            return self._mul_vector(other)
        if isinstance(other, Mat2d):
            return self._mul_matrix(other)
        if isinstance(other, Mat) and other.row() == 2:
            return self._mul_matrix(other)
        if isinstance(other, float):
            return self._mul_scalar(other)
        return NotImplemented

    @staticmethod
    def unit() -> 'Mat2d':
        return Mat2d(Mat2d._unit(2))

    @staticmethod
    def zero() -> 'Mat2d':
        return Mat2d(Mat2d._zero(2))

    @staticmethod
    def rotate(angle: float) -> 'Mat2d':
        return Mat2d([[cos(angle),   sin(angle)],
                      [-sin(angle),  cos(angle)]])

    @staticmethod
    def mirror_OY() -> 'Mat2d':
        return Mat2d([[-1, 0],
                      [0, 1]])

    @staticmethod
    def mirror_OX() -> 'Mat2d':
        return Mat2d([[1, 0],
                     [0, -1]])

    @staticmethod
    def mirror_OO() -> 'Mat2d':
        return Mat2d([[-1, 0],
                      [0, -1]])

    @staticmethod
    def mirror_45d() -> 'Mat2d':
        return Mat2d([[0, 1],
                      [1, 0]])

    @staticmethod
    def mirror_135d() -> 'Mat2d':
        return Mat2d([[0, -1],
                      [-1, 0]])

    @staticmethod
    def scale_OX(a: float) -> 'Mat2d':
        return Mat2d([[a, 0],
                      [0, 1]])

    @staticmethod
    def scale_OY(d: float) -> 'Mat2d':
        return Mat2d([[1, 0],
                      [0, d]])

    @staticmethod
    def distortion_OX(c: float) -> 'Mat2d':
        return Mat2d([[1, 0],
                      [c, 1]])

    @staticmethod
    def distortion_OY(b: float) -> 'Mat2d':
        return Mat2d([[1, b],
                      [0, 1]])
