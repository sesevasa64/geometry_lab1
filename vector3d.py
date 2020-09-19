from typing import *
from vectorNd import *


class Vec3d(Vec):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self) -> str:
        return f"Vec3d{self._format()}"

    def __add__(self, other: 'Vec3d') -> 'Vec3d':
        return self._add(other)

    def __sub__(self, other: 'Vec3d') -> 'Vec3d':
        return self._sub(other)

    def __mul__(self, other: float) -> 'Vec3d':
        if isinstance(other, float):
            return self._mul_scalar(other)
        return NotImplemented

    def __rmul__(self, other: float) -> 'Vec3d':
        if isinstance(other, float):
            return self._mul_scalar(other)
        return NotImplemented

    def __truediv__(self, scalar: float) -> 'Vec3d':
        return self._div_scalar(scalar)
