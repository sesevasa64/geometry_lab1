from typing import *
from vectorNd import *
from matrix3d import *


class Vec3d(Vec):
    def __init__(self, values: Union[List, Vec]):
        if isinstance(values, Vec):
            values = values.values
            if len(values) != 3:
                raise ValueError()
        super().__init__(values)

    def __add__(self, other: 'Vec3d') -> 'Vec3d':
        return Vec3d(super().__add__(other))

    def __sub__(self, other: 'Vec3d') -> 'Vec3d':
        return Vec3d(super().__sub__(other))

    def __mul__(self, other: Union['Mat3d', int, float]) -> 'Vec3d':
        return Vec3d(super().__mul__(other))

    def __rmul__(self, other: Union['Mat3d', int, float]) -> 'Vec3d':
        return Vec3d(super().__rmul__(other))

    def __truediv__(self, scalar: Union[int, float]) -> 'Vec3d':
        return Vec3d(super().__truediv__(scalar))
