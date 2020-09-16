from typing import *
from vector2d import *
import matrix3d as m3d


class Vec3d(Vec):
    def __init__(self, *args):
        super().__init__(*args)

    def __add__(self, other: 'Vec3d') -> 'Vec3d':
        return self._add(other)

    def __sub__(self, other: 'Vec3d') -> 'Vec3d':
        return self._sub(other)

    def __mul__(self, other: Union['m3d.Mat3d', float]) -> 'Vec3d':
        if isinstance(other, m3d.Mat3d):
            return self._mul_matrix(other)
        return self._mul_scalar(other)

    def __rmul__(self, other: Union['m3d.Mat3d', float]) -> 'Vec3d':
        if isinstance(other, m3d.Mat3d):
            return self._mul_matrix(other)
        return self._mul_scalar(other)

    def __truediv__(self, scalar: float) -> 'Vec3d':
        return self._div_scalar(scalar)

    def to2d(self):
        return Vec2d([self[0], self[1]])
