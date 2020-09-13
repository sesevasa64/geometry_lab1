from typing import *
from vectorNd import *


class Vec2d(Vec):
    def __init__(self, values: Union[List, Vec]):
        if isinstance(values, Vec):
            values = values.values
            if len(values) != 2:
                raise ValueError()
        super().__init__(values)

    def __add__(self, other: 'Vec2d') -> 'Vec2d':
        return Vec2d(super().__add__(other))

    def __sub__(self, other: 'Vec2d') -> 'Vec2d':
        return Vec2d(super().__sub__(other))

    def __mul__(self, other) -> 'Vec2d':
        return Vec2d(super().__mul__(other))

    def __rmul__(self, other) -> 'Vec2d':
        return Vec2d(super().__rmul__(other))

    def __truediv__(self, scalar) -> 'Vec2d':
        return Vec2d(super().__truediv__(scalar))
