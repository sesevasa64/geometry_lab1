from typing import *
from vectorNd import *


class Vec2d(Vec):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self) -> str:
        return f"Vec2d{self._format()}"

    def __add__(self, other: 'Vec2d') -> 'Vec2d':
        return self._add(other)

    def __sub__(self, other: 'Vec2d') -> 'Vec2d':
        return self._sub(other)

    def __mul__(self, other: float) -> 'Vec2d':
        if isinstance(other, float):
            return self._mul_scalar(other)
        return NotImplemented

    def __rmul__(self, other: float) -> 'Vec2d':
        if isinstance(other, float):
            return self._mul_scalar(other)
        return NotImplemented

    def __truediv__(self, scalar: float) -> 'Vec2d':
        return self._div_scalar(scalar)
